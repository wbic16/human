#!/usr/bin/env python3
"""resonate.py: route any text to the phext scrolls it rings against.

Usage:  python3 resonate.py "some text" file1.phext [file2.phext ...] [-n 8]

Reads phext natively (9 delimiter dimensions), builds an unmerged
word -> scroll-set index, and scores scrolls with BM25. No embeddings,
no averaging of coordinates: a word keeps every address it lives at.
"""
import sys, re, math, collections

BREAKS = {0x01:0, 0x1F:1, 0x1E:2, 0x1D:3, 0x1C:4, 0x1A:5, 0x19:6, 0x18:7, 0x17:8}

def parse(data):
    coord, start, out = [1]*9, 0, []
    for i, b in enumerate(data):
        if b in BREAKS:
            if i > start: out.append((tuple(coord), data[start:i]))
            d = BREAKS[b]; coord[d] += 1
            for j in range(d+1, 9): coord[j] = 1
            start = i + 1
    if len(data) > start: out.append((tuple(coord), data[start:]))
    return out

def fmt(c): return "%d.%d.%d/%d.%d.%d/%d.%d.%d" % c
def toks(t): return re.findall(r"[a-z0-9']+", t.lower())

def build(paths):
    docs = []
    for p in paths:
        for c, s in parse(open(p, 'rb').read()):
            t = s.decode('utf-8', 'replace')
            docs.append((p.split('/')[-1], c, t.strip().split('\n')[0][:70], collections.Counter(toks(t))))
    df = collections.Counter()
    for *_, tf in docs: df.update(tf.keys())
    return docs, df

def resonate(text, docs, df, n=8, k1=1.2, b=0.75):
    N = len(docs); avg = sum(sum(tf.values()) for *_, tf in docs) / N
    q = collections.Counter(toks(text)); scored = []
    for name, c, title, tf in docs:
        L = sum(tf.values()); s = 0.0; hits = []
        for w in q:
            f = tf.get(w, 0)
            if f:
                idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * L / avg)); hits.append((idf, w))
        if s: scored.append((s, name, c, title, [w for _, w in sorted(hits, reverse=True)[:5]]))
    return sorted(scored, reverse=True)[:n], [w for w in q if w not in df]

if __name__ == '__main__':
    a = sys.argv[1:]; n = 8
    if '-n' in a: i = a.index('-n'); n = int(a[i+1]); del a[i:i+2]
    docs, df = build(a[1:])
    top, unknown = resonate(a[0], docs, df, n)
    for s, name, c, title, hits in top:
        print(f"{s:6.2f}  {fmt(c):36s} {title}\n        [{name}] via: {', '.join(hits)}")
    if unknown: print("words with no home in these phexts:", ', '.join(unknown))
