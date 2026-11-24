"""Singular game server — stdlib-only HTTP/WebSocket container.

Implements the Coworld game role contract:
- listens on COGAME_HOST:COGAME_PORT (default 0.0.0.0:8080)
- reads the concrete config from COGAME_CONFIG_URI, seats from
  COGAME_PLAYER_SEATS_URI (game-hosted mode)
- GET /healthz, /client/player, /client/global, /client/replay, /replay
- WS /player and /global (RFC 6455, Ping answered with Pong)
- writes seat logs, player_status, replay (gzip) and finally results.json
  (the completion marker) to the COGAME_*_URI destinations
"""

import base64
import gzip
import hashlib
import json
import os
import struct
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

from .engine import run_episode

WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_uri(uri):
    if uri.startswith("file://"):
        path = urlparse(uri).path
    else:
        path = uri
    with open(path, "rb") as fh:
        return fh.read()


def write_uri(uri, data):
    if uri.startswith("file://"):
        path = urlparse(uri).path
    else:
        path = uri
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, path)


# ---------------------------------------------------------------- websockets

class WSConn:
    def __init__(self, sock, wfile):
        self.sock = sock
        self.wfile = wfile
        self.lock = threading.Lock()

    def send_text(self, text):
        data = text.encode()
        header = bytearray([0x81])
        if len(data) < 126:
            header.append(len(data))
        elif len(data) < 65536:
            header.append(126)
            header += struct.pack(">H", len(data))
        else:
            header.append(127)
            header += struct.pack(">Q", len(data))
        with self.lock:
            self.wfile.write(bytes(header) + data)
            self.wfile.flush()

    def send_pong(self, payload):
        with self.lock:
            self.wfile.write(bytes([0x8A, len(payload)]) + payload)
            self.wfile.flush()


def ws_accept(key):
    digest = hashlib.sha1((key + WS_GUID).encode()).digest()
    return base64.b64encode(digest).decode()


def read_frame(rfile):
    """Read one client frame. Returns (opcode, payload) or None on close."""
    head = rfile.read(2)
    if len(head) < 2:
        return None
    opcode = head[0] & 0x0F
    masked = head[1] & 0x80
    length = head[1] & 0x7F
    if length == 126:
        length = struct.unpack(">H", rfile.read(2))[0]
    elif length == 127:
        length = struct.unpack(">Q", rfile.read(8))[0]
    mask = rfile.read(4) if masked else b"\x00" * 4
    payload = bytearray()
    while len(payload) < length:
        chunk = rfile.read(length - len(payload))
        if not chunk:
            return None
        payload += chunk
    if masked:
        payload = bytearray(b ^ mask[i % 4] for i, b in enumerate(payload))
    return opcode, bytes(payload)


# ---------------------------------------------------------------- shared state

class Hub:
    def __init__(self):
        self.global_clients = set()
        self.player_clients = {}
        self.lock = threading.Lock()
        self.latest = None  # latest broadcast JSON (state snapshot)
        self.done = threading.Event()

    def broadcast(self, message):
        self.latest = message
        with self.lock:
            clients = list(self.global_clients)
            players = [c for cs in self.player_clients.values() for c in cs]
        for conn in clients + players:
            try:
                conn.send_text(message)
            except OSError:
                pass


HUB = Hub()

PLAYER_PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Singular — player</title></head>
<body style="font-family:monospace;background:#111;color:#eee">
<h1>Singular</h1><p id="msg">Connecting…</p><pre id="state"></pre>
<script>
const q = new URLSearchParams(location.search);
const ws = new WebSocket(`ws://${location.host}/player?slot=${q.get('slot')||0}&token=${q.get('token')||''}`);
ws.onopen = () => document.getElementById('msg').textContent =
  'Connected. In game-hosted mode this seat is played by its submitted phext; you are spectating it.';
ws.onmessage = e => document.getElementById('state').textContent = e.data;
</script></body></html>"""

GLOBAL_PAGE = """<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Singular — live</title></head>
<body style="font-family:monospace;background:#111;color:#eee">
<h1>Singular — live volume</h1><pre id="state">Waiting for the episode…</pre>
<script>
const ws = new WebSocket(`ws://${location.host}/global`);
ws.onmessage = e => document.getElementById('state').textContent = e.data;
</script></body></html>"""


def viewer_html():
    path = os.path.join(ROOT, "viewer", "index.html")
    try:
        with open(path) as fh:
            return fh.read()
    except OSError:
        return "<!DOCTYPE html><title>Singular replay</title><p>Replay viewer.</p>"


# ---------------------------------------------------------------- episode

def run_episode_from_env():
    config = {}
    cfg_uri = os.environ.get("COGAME_CONFIG_URI")
    if cfg_uri:
        config = json.loads(read_uri(cfg_uri))
    seats = []
    status_uri = None
    seats_uri = os.environ.get("COGAME_PLAYER_SEATS_URI")
    if seats_uri:
        seats_doc = json.loads(read_uri(seats_uri))
        if isinstance(seats_doc, dict):
            seats = sorted(seats_doc.get("seats", []),
                           key=lambda s: s.get("slot", 0))
            status_uri = seats_doc.get("player_status_uri")
        else:
            seats = seats_doc
    names = [p.get("name", f"Player {i}")
             for i, p in enumerate(config.get("players", []))]
    player_texts = []
    for i, seat in enumerate(seats):
        player_texts.append(read_uri(seat["file_uri"]).decode())
    if not player_texts:  # standalone smoke mode: bundled baseline vs weaver
        base = os.path.join(ROOT, "players")
        player_texts = [open(os.path.join(base, "baseline.phext")).read(),
                        open(os.path.join(base, "weaver.phext")).read()]
        names = names or ["Baseline", "Weaver"]
    seed = int(config.get("seed", 2026))
    turns = int(config.get("turns", 48))

    def hook(idx, state):
        HUB.broadcast(json.dumps({"type": "state", "index": idx,
                                  "state": state}))
        time.sleep(0.05)

    results, replay, seat_logs = run_episode(
        seed, player_texts, turns, names, hook=hook)
    # seat logs and status first; results.json is the completion marker
    for i, seat in enumerate(seats):
        if seat.get("log_uri"):
            write_uri(seat["log_uri"], seat_logs[i].encode())
    if status_uri:
        write_uri(status_uri, json.dumps(
            {"slots": [{"slot": i, "status": "completed"}
                       for i in range(len(player_texts))]}).encode())
    replay_uri = os.environ.get("COGAME_SAVE_REPLAY_URI")
    if replay_uri:
        write_uri(replay_uri, gzip.compress(json.dumps(replay).encode()))
    results_uri = os.environ.get("COGAME_RESULTS_URI")
    if results_uri:
        write_uri(results_uri, json.dumps(results).encode())
    HUB.broadcast(json.dumps({"type": "results", "results": results}))
    HUB.done.set()
    print(f"episode complete: {results}", flush=True)


# ---------------------------------------------------------------- http

class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        data = body.encode() if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/healthz":
            self._send(200, "ok", "text/plain")
        elif path == "/client/player":
            self._send(200, PLAYER_PAGE)
        elif path == "/client/global":
            self._send(200, GLOBAL_PAGE)
        elif path == "/client/replay":
            self._send(200, viewer_html())
        elif path == "/replay":
            uri = os.environ.get("COGAME_LOAD_REPLAY_URI")
            if uri:
                try:
                    self._send(200, read_uri(uri), "application/gzip")
                    return
                except OSError:
                    pass
            self._send(404, "no replay", "text/plain")
        elif path in ("/player", "/global"):
            self._upgrade(parsed, path)
        else:
            self._send(404, "not found", "text/plain")

    def _upgrade(self, parsed, path):
        key = self.headers.get("Sec-WebSocket-Key")
        if not key:
            self._send(400, "websocket key required", "text/plain")
            return
        self.send_response(101)
        self.send_header("Upgrade", "websocket")
        self.send_header("Connection", "Upgrade")
        self.send_header("Sec-WebSocket-Accept", ws_accept(key))
        self.end_headers()
        conn = WSConn(self.connection, self.wfile)
        slot = None
        if path == "/global":
            with HUB.lock:
                HUB.global_clients.add(conn)
        else:
            qs = parse_qs(parsed.query)
            try:
                slot = int(qs.get("slot", ["0"])[0])
            except ValueError:
                slot = 0
            with HUB.lock:
                HUB.player_clients.setdefault(slot, set()).add(conn)
        if HUB.latest:
            try:
                conn.send_text(HUB.latest)
            except OSError:
                pass
        try:
            while True:
                frame = read_frame(self.rfile)
                if frame is None:
                    break
                opcode, payload = frame
                if opcode == 0x9:  # Ping -> Pong, same payload
                    conn.send_pong(payload)
                elif opcode == 0x8:  # Close
                    break
                # other client messages are accepted and ignored:
                # game-hosted seats are played by their submitted files
        except OSError:
            pass
        finally:
            with HUB.lock:
                HUB.global_clients.discard(conn)
                if slot is not None and slot in HUB.player_clients:
                    HUB.player_clients[slot].discard(conn)


def main():
    host = os.environ.get("COGAME_HOST", "0.0.0.0")
    port = int(os.environ.get("COGAME_PORT", "8080"))
    server = ThreadingHTTPServer((host, port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"singular game server on {host}:{port}", flush=True)
    if os.environ.get("COGAME_LOAD_REPLAY_URI"):
        thread.join()  # replay mode: serve only
        return
    try:
        run_episode_from_env()
    except Exception as exc:  # surface as a plain failure, no results
        print(f"episode failed: {exc}", flush=True)
        raise
    # keep serving the live surface briefly for late viewers
    time.sleep(2)
    server.shutdown()


if __name__ == "__main__":
    main()
