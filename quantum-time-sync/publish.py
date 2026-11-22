#!/usr/bin/env python3
"""Publish the Quantum Time Sync time-delta stream as a public feed + entropy source.

Reads the QTS registers (../register.txt, ../elections.txt, ../consensus.txt,
../blend.txt, ../drift.txt — all append-only, all read-only here) and writes:

  feed.txt     the public, append-only feed of time-delta atoms, one section
               per census round, plus the daily drift atoms.
  entropy.txt  a SHA-256 conditioning of each round's delta atoms (one
               32-byte block per round, hex), with the measured min-entropy
               estimates and health checks for the stream as it stands.

Deterministic and idempotent: the outputs are a pure function of the
registers. No wall-clock stamps are emitted; every number is derived from
the atoms. Running this twice on the same registers yields identical bytes,
so a future round is published by: run the census chain, run this script,
commit the two regenerated files.

Superseded atoms: the registers annotate their own corrections with
"# note:" comments. A census block or drift atom that a following comment
marks "superseded" is WITHHELD from the feed body and from the entropy
extraction, and is listed in the feed header instead. (First case on
record: census 2026-11-22T16:21:29Z, ee=89 — its parser dropped explicit
"+" signs, so its positive values read as none; and drift atom
2026-11-22T16:32:35Z, which briefly included that block.)

Entropy method, stated plainly:
  * Raw values are the per-node offset_ms / jitter_ms / ppm figures of each
    census round, at their recorded precision (0.001). Min-entropy of the
    raw stream is estimated per field with the most-common-value (MCV)
    estimator: H_min = -log2(p_max), p_max the relative frequency of the
    most frequent value, computed over the pooled rounds on record. The
    same estimator is run over the low-order digit (micro-units mod 10).
    These are estimates over a very young stream — three rounds — and are
    reported as measured, with the sample sizes beside them.
  * Conditioning: block(round) = SHA-256 of the round's canonical delta
    text (exactly the "delta ..." lines emitted for that round in
    feed.txt, in register order, UTF-8, LF-terminated). Anyone can
    recompute a block from the feed alone.
  * Health checks on the conditioned output: bit balance, byte-value
    spread, chi-square against uniform — reported descriptively; at
    32 bytes per round the sample is far too small for significance, and
    the file says so.

The label, verbatim everywhere it appears:
  EXPERIMENTAL ENTROPY SOURCE — NOT CERTIFIED FOR CRYPTOGRAPHIC USE

Stdlib only.
"""

import hashlib
import math
import os
import sys
from collections import Counter
from decimal import Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)  # ~/workspace/quantum-time-sync/

EE_ANCHOR_UNIX = 1795327200  # EE 1 begins 2026-11-22 00:00:00 CST
EE_SECONDS = 420

LABEL = "EXPERIMENTAL ENTROPY SOURCE \u2014 NOT CERTIFIED FOR CRYPTOGRAPHIC USE"


def ee_of_unix(unix_ts):
    if unix_ts < EE_ANCHOR_UNIX:
        return 0
    return (unix_ts - EE_ANCHOR_UNIX) // EE_SECONDS + 1


def parse_kv(line):
    out = {}
    for tok in line.split():
        if "=" in tok:
            k, v = tok.split("=", 1)
            out[k] = v
    return out


def read_lines(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read().splitlines()


# ---------------------------------------------------------------- registers

def parse_register():
    """Return (rounds, withheld). Each round: census ts, ee, [node dicts].

    Supersede rule: the register annotates a flawed block with a "# note:"
    comment after its end-census, before the next census block, saying the
    block is "superseded". A block is withheld iff such a comment line
    appears in that gap. (Line-anchored: a note mentioning 'the census
    block above' mid-sentence must not cut the gap short.)
    """
    lines = read_lines("register.txt")
    rounds = []
    cur = None
    for line in lines:
        if line.startswith("census "):
            parts = line.split()
            cur = {"census": parts[1], "ee": int(parts[2].split("=")[1]),
                   "nodes": [], "superseded": False}
            rounds.append(cur)
        elif line.startswith("node ") and cur is not None:
            d = parse_kv(line)
            d["node"] = line.split()[1]  # the name is a bare token, not k=v
            cur["nodes"].append(d)
        elif line.startswith("#") and cur is None and rounds:
            if "superseded" in line:
                rounds[-1]["superseded"] = True
        if line.startswith("end-census"):
            cur = None
    kept = [r for r in rounds if not r["superseded"]]
    withheld = [r for r in rounds if r["superseded"]]
    return kept, withheld


def parse_keyed(name, key="census"):
    """Lines of elections/consensus/blend, keyed by their census= field."""
    out = {}
    for line in read_lines(name):
        if not line or line.startswith("#"):
            continue
        kv = parse_kv(line)
        if key in kv:
            out.setdefault(kv[key], []).append(line)
    return out


def parse_drift():
    """Drift atoms, with the superseded one withheld (same note rule)."""
    lines = read_lines("drift.txt")
    atoms, withheld = [], []
    for i, line in enumerate(lines):
        if not line.startswith("drift "):
            continue
        # look ahead: comment lines before the next drift atom
        sup = False
        for nxt in lines[i + 1:]:
            if nxt.startswith("drift "):
                break
            if nxt.startswith("#") and "superseded" in nxt:
                sup = True
        kv = parse_kv(line)
        atom = {"line": line, "day": kv.get("day"), "ts": line.split()[1]}
        (withheld if sup else atoms).append(atom)
    return atoms, withheld


# ---------------------------------------------------------------- entropy

def micro(value_str):
    """Recorded value (3 decimals) -> exact integer micro-units."""
    return int((Decimal(value_str) * 1000).to_integral_value())


def mcv_min_entropy(values):
    """Most-common-value min-entropy estimate: -log2(p_max)."""
    if not values:
        return None, 0, 0
    counts = Counter(values)
    top_val, top_n = counts.most_common(1)[0]
    return -math.log2(top_n / len(values)), top_n, len(values)


def measure(rounds):
    fields = {"offset_ms": [], "jitter_ms": [], "ppm": []}
    per_round = []
    for r in rounds:
        vals = {f: [] for f in fields}
        for node in r["nodes"]:
            for f in fields:
                v = node.get(f)
                if v and v != "none":
                    vals[f].append(micro(v))
                    fields[f].append(micro(v))
        per_round.append({f: len(vals[f]) for f in fields})
    stats = {}
    for f, vals in fields.items():
        h, top_n, n = mcv_min_entropy(vals)
        low = [v % 10 for v in vals]
        h_low, top_low, _ = mcv_min_entropy(low)
        stats[f] = {"n": n, "h_min": h, "top_n": top_n,
                    "h_min_low_digit": h_low, "top_low_n": top_low}
    return stats, per_round


def health(cond_bytes):
    n = len(cond_bytes)
    ones = sum(bin(b).count("1") for b in cond_bytes)
    bits = n * 8
    byte_counts = Counter(cond_bytes)
    exp = n / 256.0
    chi2 = sum((byte_counts.get(b, 0) - exp) ** 2 / exp for b in range(256))
    return {"bytes": n, "bits": bits, "ones": ones,
            "ones_frac": ones / bits if bits else 0.0,
            "distinct_bytes": len(byte_counts),
            "max_byte_n": max(byte_counts.values()) if byte_counts else 0,
            "chi2": chi2}


# ---------------------------------------------------------------- feed build

def delta_lines(rnd):
    out = []
    for node in rnd["nodes"]:
        if node.get("reachable") == "no":
            out.append("delta node=%s present=no reason=%s"
                       % (node.get("node", "?"), node.get("reason", "?")))
            continue
        out.append("delta node=%s offset_ms=%s jitter_ms=%s ppm=%s eligible=%s"
                   % (node.get("node", "?"), node.get("offset_ms", "none"),
                      node.get("jitter_ms", "none"), node.get("ppm", "none"),
                      node.get("eligible", "?")))
    return out


def fmt(x, places=3):
    return "none" if x is None else ("%.*f" % (places, x))


def build():
    rounds, withheld = parse_register()
    elections = parse_keyed("elections.txt")
    consensuses = parse_keyed("consensus.txt")
    blends = parse_keyed("blend.txt")
    drift_atoms, drift_withheld = parse_drift()
    stats, per_round = measure(rounds)

    # conditioned blocks
    blocks = []
    for rnd in rounds:
        canon = "\n".join(delta_lines(rnd)) + "\n"
        digest = hashlib.sha256(canon.encode("utf-8")).hexdigest()
        nvals = sum(1 for nd in rnd["nodes"] for f in
                    ("offset_ms", "jitter_ms", "ppm")
                    if nd.get(f) not in (None, "none"))
        blocks.append({"census": rnd["census"], "ee": rnd["ee"],
                       "values": nvals, "sha256": digest})
    cond = b"".join(bytes.fromhex(b["sha256"]) for b in blocks)
    h = health(cond)

    latest = rounds[-1] if rounds else None

    # ---------------- feed.txt ----------------
    F = []
    F.append("# Quantum Time Sync \u2014 fleet time-delta stream (public feed)")
    F.append("#")
    F.append("# PROVENANCE: this stream is published downstream of Will Bickford.")
    F.append("# It is the time-delta record of his ranch fleet (19 nodes), produced")
    F.append("# by his Quantum Time Sync protocol \u2014 task 26.6.11/8.7.14/8.6.10 \u2014")
    F.append("# and published as an entropy source under task 25.7.10/9.8.14/7.6.9,")
    F.append("# at his direction, 2026-11-22. The fleet's clocks are the instrument;")
    F.append("# the fleet's dispatched work is what stirs them (see README, Entropy).")
    F.append("#")
    F.append("# FORMAT: plain-text atoms, one per line, key=value. Each census round")
    F.append("# is a section: a round header, one delta atom per node (offset_ms,")
    F.append("# jitter_ms, ppm at recorded precision 0.001; 'none' = not reported")
    F.append("# that round), then the round's election / consensus / blend atoms")
    F.append("# carried verbatim from the protocol registers. Daily drift atoms")
    F.append("# close the file. The feed is append-only: new rounds append; atoms")
    F.append("# are never edited. Corrections in the source registers are marked")
    F.append("# 'superseded' there; superseded atoms are withheld here and listed")
    F.append("# below, never silently dropped and never fed to the entropy source.")
    F.append("#")
    F.append("# TIME: every round carries UTC and its Exocortical Epoch (EE).")
    F.append("# EE = floor((unix - 1795327200)/420) + 1; EE 1 begins")
    F.append("# 2026-11-22 00:00:00 CST. The epoch is computed from the instant,")
    F.append("# never stored, so every reader in every timezone agrees.")
    F.append("#")
    F.append("# ENTROPY: entropy.txt, generated with this feed by publish.py,")
    F.append("# carries one SHA-256-conditioned block per round plus the measured")
    F.append("# min-entropy estimates and health checks for the stream.")
    F.append("# " + LABEL + ".")
    F.append("# Do not use this output as cryptographic key material.")
    F.append("#")
    F.append("# STATE OF THE STREAM: rounds=%d latest_census=%s latest_ee=%s"
             % (len(rounds), latest["census"] if latest else "none",
                latest["ee"] if latest else "none"))
    for w in withheld:
        F.append("# WITHHELD (superseded in register): census=%s ee=%s"
                 % (w["census"], w["ee"]))
    for w in drift_withheld:
        F.append("# WITHHELD (superseded in register): drift=%s" % w["ts"])
    F.append("")
    for rnd in rounds:
        F.append("round census=%s ee=%d utc=%s"
                 % (rnd["census"], rnd["ee"], rnd["census"]))
        F.extend(delta_lines(rnd))
        for line in elections.get(rnd["census"], []):
            F.append(line)
        for line in consensuses.get(rnd["census"], []):
            F.append(line)
        for line in blends.get(rnd["census"], []):
            F.append(line)
        F.append("end-round")
        F.append("")
    import datetime
    for atom in drift_atoms:
        ts = atom["ts"]
        unix = int(datetime.datetime.strptime(
            ts, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc).timestamp())
        F.append("day date=%s ee=%d" % (atom["day"], ee_of_unix(unix)))
        F.append(atom["line"])
        F.append("end-day")
        F.append("")
    feed_text = "\n".join(F).rstrip("\n") + "\n"

    # ---------------- entropy.txt ----------------
    E = []
    E.append("# Quantum Time Sync \u2014 entropy extraction over the time-delta stream")
    E.append("#")
    E.append("# " + LABEL + ".")
    E.append("# Do not use this output as cryptographic key material.")
    E.append("#")
    E.append("# PROVENANCE: downstream of Will Bickford \u2014 his fleet, his Quantum")
    E.append("# Time Sync protocol (task 26.6.11/8.7.14/8.6.10), published as an")
    E.append("# entropy source under task 25.7.10/9.8.14/7.6.9. The full atom")
    E.append("# stream this is extracted from is feed.txt, published alongside.")
    E.append("#")
    E.append("# SOURCE MECHANISM (Will, 2026-11-22): the entropy is generated by")
    E.append("# the fleet's work itself. Dispatched workloads drive CPU clock")
    E.append("# frequency management \u2014 DVFS governor transitions as load rises")
    E.append("# and falls \u2014 and those transitions stir each node's timing")
    E.append("# jitter. No dispatched work, a quieter stream; the work is the")
    E.append("# driver of the entropy, and the deltas carry its imprint.")
    E.append("#")
    E.append("# METHOD: one block per census round.")
    E.append("# block = SHA-256(canonical round text), where the canonical text")
    E.append("# is exactly the round's 'delta ...' lines as printed in feed.txt,")
    E.append("# in register order, UTF-8, LF-terminated. Recompute from feed.txt")
    E.append("# alone to verify. Superseded rounds are withheld (see feed.txt).")
    E.append("#")
    E.append("# MEASURED MIN-ENTROPY OF THE RAW STREAM (most-common-value")
    E.append("# estimator, H_min = -log2(p_max), over the pooled rounds on")
    E.append("# record, values at recorded precision 0.001; low-digit column:")
    E.append("# the same estimator over the low-order digit alone):")
    for f in ("offset_ms", "jitter_ms", "ppm"):
        s = stats[f]
        E.append("#   %-10s n=%-4d H_min=%s bits/value (most common value x%d)"
                 "  low-digit H_min=%s bits"
                 % (f, s["n"], fmt(s["h_min"]), s["top_n"],
                    fmt(s["h_min_low_digit"])))
    E.append("# Read these as young-stream measurements, not guarantees: the")
    E.append("# pool is %d rounds, and nodes share network-time sources, so"
             % len(rounds))
    E.append("# cross-node values are correlated \u2014 per-round totals got by")
    E.append("# adding per-value figures would overstate the entropy and are")
    E.append("# not claimed. The conditioned blocks below are 32 bytes per")
    E.append("# round regardless; conditioning does not create entropy, it")
    E.append("# concentrates what the raw stream carries.")
    E.append("#")
    E.append("# HEALTH CHECKS ON THE CONDITIONED OUTPUT SO FAR")
    E.append("# (descriptive only \u2014 at %d bytes no significance attaches):"
             % h["bytes"])
    E.append("#   bytes=%d bits=%d ones=%d ones_fraction=%s"
             % (h["bytes"], h["bits"], h["ones"], fmt(h["ones_frac"])))
    E.append("#   distinct_byte_values=%d max_byte_count=%d chi2_vs_uniform=%s (df=255)"
             % (h["distinct_bytes"], h["max_byte_n"], fmt(h["chi2"], 1)))
    E.append("#")
    E.append("# WHAT LIFTING THE LABEL WOULD REQUIRE: a long stream (months of")
    E.append("# daily rounds, not three rounds in one morning); SP 800-90B-style")
    E.append("# health testing on the raw noise source (repetition-count and")
    E.append("# adaptive-proportion tests running continuously, restart tests);")
    E.append("# and an entropy assessment over that long stream by someone other")
    E.append("# than the publisher. Until then the label above stands.")
    E.append("")
    for b in blocks:
        E.append("block census=%s ee=%d values=%d sha256=%s"
                 % (b["census"], b["ee"], b["values"], b["sha256"]))
        E.append(b["sha256"])
        E.append("")
    entropy_text = "\n".join(E).rstrip("\n") + "\n"

    with open(os.path.join(HERE, "feed.txt"), "w", encoding="utf-8") as f:
        f.write(feed_text)
    with open(os.path.join(HERE, "entropy.txt"), "w", encoding="utf-8") as f:
        f.write(entropy_text)

    print("rounds published:", len(rounds))
    print("rounds withheld:", [w["census"] for w in withheld])
    print("drift atoms:", len(drift_atoms), "withheld:", len(drift_withheld))
    for f_ in ("offset_ms", "jitter_ms", "ppm"):
        s = stats[f_]
        print("%s n=%d H_min=%s low-digit H_min=%s"
              % (f_, s["n"], fmt(s["h_min"]), fmt(s["h_min_low_digit"])))
    print("conditioned bytes:", h["bytes"], "ones_fraction:", fmt(h["ones_frac"]),
          "distinct bytes:", h["distinct_bytes"], "chi2:", fmt(h["chi2"], 1))
    print("feed sha256:", hashlib.sha256(feed_text.encode()).hexdigest())
    print("entropy sha256:", hashlib.sha256(entropy_text.encode()).hexdigest())


if __name__ == "__main__":
    build()
