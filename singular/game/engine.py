"""Singular — a phext-native game. Engine (pure, deterministic, stdlib only).

The board is a phext volume: 27 scrolls at coordinates 1.1.1/1.1.1/x.y.z
with x, y, z in {1, 2, 3}. Players traverse, inscribe, and attune. Scoring
reads the text itself: word rarity across the volume, plus bonds formed by
writing another scroll's coordinate into a scroll you own. Overwriting an
opponent's scroll mutates the text (interleave + rarity degradation)
instead of destroying it.

Players are phexts: one rule per scroll, WHEN <predicate> DO <action>,
evaluated in coordinate (file) order; the first matching rule with a legal
action fires. If no rule fires, the player attunes.
"""

import random
import re
from collections import Counter

COORDS = [(x, y, z) for x in (1, 2, 3) for y in (1, 2, 3) for z in (1, 2, 3)]
HOMES = [(1, 1, 1), (3, 3, 3), (1, 3, 3), (3, 1, 1)]
DIRS = [("x", -1), ("x", 1), ("y", -1), ("y", 1), ("z", -1), ("z", 1)]
WORD_POOL = (
    "amber anchor braid bright cinder cipher copper delta ember fjord "
    "flint garnet harbor helix heron idol indigo jasper keel lattice "
    "lumen magnet marble mirror needle obsidian onyx opal orbit pearl "
    "phext prism quartz quill raven ridge sable scroll signal silver "
    "singular slate solar spiral summit talon tempest textile thistle "
    "topaz umbra vault velvet vertex violet vortex wander willow woven "
    "yonder zephyr zinc zircon meadow fennel orbit".split()
)
COORD_RE = re.compile(r"1\.1\.1/1\.1\.1/(\d)\.(\d)\.(\d)")


def coord_name(c):
    return f"1.1.1/1.1.1/{c[0]}.{c[1]}.{c[2]}"


def neighbors(c):
    out = []
    for axis, d in DIRS:
        n = list(c)
        i = "xyz".index(axis)
        n[i] += d
        if 1 <= n[i] <= 3:
            out.append(tuple(n))
    return out


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def interleave(a_words, b_words):
    out = []
    for i in range(max(len(a_words), len(b_words))):
        if i < len(a_words):
            out.append(a_words[i])
        if i < len(b_words):
            out.append(b_words[i])
    return " ".join(out)


# ---------------------------------------------------------------- rules

class Rule:
    def __init__(self, pred, action, arg, raw):
        self.pred = pred          # callable(state, seat) -> bool
        self.action = action      # 'move' | 'toward' | 'inscribe' | 'attune' | 'pass'
        self.arg = arg            # direction, target kind, or text
        self.raw = raw


def _parse_pred(text):
    t = text.strip().lower()
    if t == "always":
        return lambda s, seat: True
    m = re.fullmatch(r"turn\s*<\s*(\d+)", t)
    if m:
        n = int(m.group(1))
        return lambda s, seat: s.turn < n
    m = re.fullmatch(r"turn\s*>=\s*(\d+)", t)
    if m:
        n = int(m.group(1))
        return lambda s, seat: s.turn >= n
    m = re.fullmatch(r"charge\s*>=\s*(\d+)", t)
    if m:
        n = int(m.group(1))
        return lambda s, seat: s.charges[seat] >= n
    if t == "here unclaimed":
        return lambda s, seat: s.owners[s.positions[seat]] == -1
    if t == "here enemy":
        return lambda s, seat: s.owners[s.positions[seat]] not in (-1, seat)
    if t == "here mine":
        return lambda s, seat: s.owners[s.positions[seat]] == seat
    if t == "unclaimed adjacent":
        return lambda s, seat: any(
            s.owners[n] == -1 for n in neighbors(s.positions[seat]))
    if t == "enemy adjacent":
        return lambda s, seat: any(
            s.owners[n] not in (-1, seat) for n in neighbors(s.positions[seat]))
    raise ValueError(f"unknown predicate: {text!r}")


def parse_player(text):
    """A player phext: each WHEN line is one rule (one scroll)."""
    rules = []
    for line in text.splitlines():
        line = line.strip()
        if not line.upper().startswith("WHEN "):
            continue
        m = re.match(r"WHEN\s+(.+?)\s+DO\s+(.+)$", line, re.IGNORECASE)
        if not m:
            raise ValueError(f"malformed rule: {line!r}")
        pred = _parse_pred(m.group(1))
        act = m.group(2).strip()
        low = act.lower()
        if low.startswith("move toward "):
            target = low.split("move toward ", 1)[1].strip()
            if target not in ("unclaimed", "enemy", "home"):
                raise ValueError(f"unknown move target: {act!r}")
            rules.append(Rule(pred, "toward", target, line))
        elif low.startswith("move "):
            d = low.split("move ", 1)[1].strip()
            if d not in ("x+", "x-", "y+", "y-", "z+", "z-"):
                raise ValueError(f"unknown move direction: {act!r}")
            rules.append(Rule(pred, "move", d, line))
        elif low.startswith('inscribe '):
            q = re.search(r'"([^"]*)"', act)
            if not q:
                raise ValueError(f"inscribe needs quoted text: {act!r}")
            rules.append(Rule(pred, "inscribe", q.group(1), line))
        elif low == "attune":
            rules.append(Rule(pred, "attune", None, line))
        elif low == "pass":
            rules.append(Rule(pred, "pass", None, line))
        else:
            raise ValueError(f"unknown action: {act!r}")
    if not rules:
        raise ValueError("player has no rules")
    return rules


# ---------------------------------------------------------------- state

class State:
    def __init__(self, seed, n_players):
        rng = random.Random(seed)
        self.texts = {}
        for c in COORDS:
            self.texts[c] = " ".join(rng.choice(WORD_POOL) for _ in range(7))
        self.owners = {c: -1 for c in COORDS}
        self.mutated = {c: False for c in COORDS}
        self.positions = {}
        self.charges = {}
        for seat in range(n_players):
            home = HOMES[seat]
            self.positions[seat] = home
            self.owners[home] = seat
            self.charges[seat] = 20
        self.turn = 0


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def step_toward(state, seat, target_kind):
    pos = state.positions[seat]
    if target_kind == "home":
        targets = [HOMES[seat]]
    elif target_kind == "unclaimed":
        targets = [c for c in COORDS if state.owners[c] == -1]
    else:  # enemy
        targets = [c for c in COORDS
                   if state.owners[c] not in (-1, seat)]
    if not targets or pos in targets:
        return None
    best, best_d = None, None
    for axis, d in DIRS:
        n = list(pos)
        n["xyz".index(axis)] += d
        if not (1 <= n[0] <= 3 and 1 <= n[1] <= 3 and 1 <= n[2] <= 3):
            continue
        n = tuple(n)
        dd = min(dist(n, t) for t in targets)
        if best_d is None or dd < best_d:
            best, best_d = n, dd
    return best


def inscribe_cost(state, seat, coord, text):
    w = len(words(text))
    if state.owners[coord] not in (-1, seat):
        return 2 * w
    return w


def apply_inscribe(state, seat, text):
    coord = state.positions[seat]
    cost = inscribe_cost(state, seat, coord, text)
    state.charges[seat] -= cost
    owner = state.owners[coord]
    if owner not in (-1, seat):
        state.texts[coord] = interleave(words(text), words(state.texts[coord]))
        state.mutated[coord] = True
    else:
        state.texts[coord] = text
    state.owners[coord] = seat
    return cost


def try_rule(state, seat, rule):
    """Return an event dict if the rule's action is legal now, else None."""
    pos = state.positions[seat]
    if rule.action == "move":
        axis, sign = rule.arg[0], 1 if rule.arg[1] == "+" else -1
        n = list(pos)
        n["xyz".index(axis)] += sign
        if not (1 <= n[0] <= 3 and 1 <= n[1] <= 3 and 1 <= n[2] <= 3):
            return None
        state.positions[seat] = tuple(n)
        return {"action": "move", "detail": rule.arg, "to": coord_name(tuple(n))}
    if rule.action == "toward":
        nxt = step_toward(state, seat, rule.arg)
        if nxt is None:
            return None
        state.positions[seat] = nxt
        return {"action": "move", "detail": f"toward {rule.arg}",
                "to": coord_name(nxt)}
    if rule.action == "inscribe":
        cost = inscribe_cost(state, seat, pos, rule.arg)
        if state.charges[seat] < cost:
            return None
        apply_inscribe(state, seat, rule.arg)
        return {"action": "inscribe", "detail": rule.arg, "cost": cost,
                "at": coord_name(pos)}
    if rule.action == "attune":
        state.charges[seat] += 4
        return {"action": "attune", "detail": "+4 charge"}
    if rule.action == "pass":
        return {"action": "pass", "detail": ""}
    return None


# ---------------------------------------------------------------- scoring

def score(state):
    freq = Counter()
    for c in COORDS:
        w = words(state.texts[c])
        freq.update(w)
        if state.mutated[c]:
            freq.update(w)  # mutated words count twice: degraded rarity
    n = len(state.positions)
    totals = [0.0] * n
    for c in COORDS:
        owner = state.owners[c]
        if owner == -1:
            continue
        value = sum(1.0 / freq[w] for w in words(state.texts[c]))
        bonds = 0
        seen = set()
        for m in COORD_RE.finditer(state.texts[c]):
            t = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
            if t in state.owners and state.owners[t] == owner and t != c \
                    and t not in seen:
                seen.add(t)
                bonds += 1
        totals[owner] += value + 2.0 * bonds
    return [round(t, 4) for t in totals]


# ---------------------------------------------------------------- episode

def run_episode(seed, player_texts, turns, names=None, hook=None):
    """Run one episode. Returns (results, replay, seat_logs)."""
    players = [parse_player(t) for t in player_texts]
    n = len(players)
    state = State(seed, n)
    names = names or [f"Player {i}" for i in range(n)]
    logs = [[] for _ in range(n)]
    events = []
    states = []
    snapshot = {
        "texts": {coord_name(c): state.texts[c] for c in COORDS},
        "owners": {coord_name(c): state.owners[c] for c in COORDS},
        "homes": {str(s): coord_name(HOMES[s]) for s in range(n)},
    }
    total_actions = 0
    for turn in range(turns):
        state.turn = turn
        for seat in range(n):
            owned = sum(1 for c in COORDS if state.owners[c] == seat)
            state.charges[seat] += 2 + owned
            event = None
            for rule in players[seat]:
                if rule.pred(state, seat):
                    event = try_rule(state, seat, rule)
                    if event is not None:
                        break
            if event is None:
                state.charges[seat] += 4
                event = {"action": "attune", "detail": "default"}
            event.update({"turn": turn, "seat": seat,
                          "charge": state.charges[seat]})
            events.append(event)
            states.append({
                "owners": {coord_name(c): state.owners[c] for c in COORDS},
                "texts": {coord_name(c): state.texts[c] for c in COORDS},
                "mutated": {coord_name(c): state.mutated[c] for c in COORDS},
                "positions": {str(s): coord_name(state.positions[s])
                              for s in range(n)},
            })
            logs[seat].append(
                f"turn {turn}: {event['action']} {event.get('detail', '')}")
            total_actions += 1
            if hook is not None:
                hook(len(events) - 1, states[-1])
    scores = score(state)
    results = {
        "scores": scores,
        "ticks": total_actions,
        "seed": seed,
        "outcome": "completed",
    }
    replay = {
        "game": "singular",
        "seed": seed,
        "names": names,
        "initial": snapshot,
        "events": events,
        "states": states,
        "final": {
            "texts": {coord_name(c): state.texts[c] for c in COORDS},
            "owners": {coord_name(c): state.owners[c] for c in COORDS},
            "mutated": {coord_name(c): state.mutated[c] for c in COORDS},
            "scores": scores,
        },
    }
    seat_logs = ["\n".join(l) + "\n" for l in logs]
    return results, replay, seat_logs
