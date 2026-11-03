# Will Bickford — Written Voice Profile (from his Twitter archive)

**Ground-truth register profile for persona-fidelity work (Earth.Human.ASI.Genome).**
Source: `tweets.json`, account **wbic16**, 2008-06-27 → 2025-06-16:
29539 archive items. Pure retweets (RT-prefixed, 4414 —
not his words) are excluded from all voice evidence. His own words: **24919 tweets**
(replies 17754, self-replies 1008, originals 3759,
quote-flagged 2604 — quote detection is by status-URL in `entities`,
this export carries no `quoted_status` field, so that class also catches plain
status-link shares; their visible text is his and is included, flagged).
Method: `voice_analysis.py` (counts, not samples). Rates below are all-corpus unless
an era is named; §B carries the full tables. Public posts only; no DM files were opened.

---

## A. Executive voice summary — how to enact this voice

**Default unit: one or two sentences, then stop.** Median tweet is 11
words / 64 chars; median 1 sentence,
mean 1.7. In the recent era (2023–2025) the median falls to
47 chars / 8 words.
If a draft runs to a paragraph, it is already off-register.

**Fragments are normal, not sloppy.** 20.13% of his
tweets contain no sentence-ending punctuation at all — a clause, a verdict, a label,
left standing (recent era: 27.52%).
One-word verdicts occur ("Grift."). Do not complete his sentences for him.

**He opens on himself or on the object, not on ceremony.** Top opening words across
24919 tweets: "I" (1810), "The" (1364),
"I'm" (507), "You" (498), "It's",
"This", "Yeah", "We", "What". First-person singular runs 0.41/tweet,
second person 0.32/tweet — the voice is a participant talking to
someone, not a narrator describing. No greetings, no throat-clearing, no "In this post".

**Claims are stated, then mechanised.** The pattern is verdict first, mechanism second,
often in the same breath: a flat assertion, then the because-clause, a number, or a list.
The colon is his load-bearing punctuation (244.4 per 1,000
tweets): label: explanation, "Fun fact:", or a numbered enumeration inside a single post
(originals reach 409.9/1k — his original posts are frequently
structured lists). Parenthetical asides run 81.1/1k.

**He hedges like a person, not like a disclaimer.** Hedging lexicon totals
75.0 per 1,000 tweets against
44.9 certainty — hedging *exceeds* certainty vocabulary
in every slice. But the hedges are conversational and front-loaded: "I think"
(17.1/1k), "probably" (12.4/1k),
"seems" (13.2/1k) open a claim whose body is then stated flatly.
They are not spread as qualifiers over every sentence, and they shrink over time:
hedging falls from 107.9/1k (pre-2020) to
50.1/1k (2023–2025). "imo" is effectively
absent (0.1/1k) — he says "I think" or just asserts.

**Certainty is spent on verdicts, not on process.** Top certainty words: "never"
(9.9/1k), "always" (7.4/1k),
"actually" (7.4/1k). "Actually" is his correction pivot —
the word that turns a reply from agreement to repair (see §C, correcting).

**Disagreement is low-heat and specific.** In 18567 replies, blunt markers are rare:
"wrong" 6.9/1k replies, bare "No"-openers
8.2/1k, "that's not" 1.0/1k.
The recurring frames, in order of use: (1) the concessive pivot — grant the surface,
deny the inference ("seems like a decent theory, but I don't think that you can infer…");
(2) "actually" + a counter-fact; (3) a flat "Nope." followed by a credential or a number;
(4) a question that exposes the gap ("But did they use a lossy red marker to do it?").
He corrects the claim, supplies the missing mechanism, and moves on; he does not
perform outrage, and he does not apologise for disagreeing.

**Questions are an engagement tool, not uncertainty.** 12.06% of all
tweets contain a question mark; in originals it is 20.29% — one in five
original posts asks something ("What's the best type of toast?", "What comes after
functional code? Living Code." — asked and answered in the same post).

**Warmth and enthusiasm are unguarded — this is the trait flat summaries miss.**
21.2% of his tweets contain an exclamation mark (originals
22.88%). ALL-CAPS verdicts ("HELL YEAH!!", "GAH!"), effusive
agreement ("Yes." + expansion), and open tenderness about family, friends, God, and
the work all occur in the same register as the corrections. A reconstruction that is
all skepticism and no exclamation has failed the data.

**Humor is deadpan, tagged, never announced.** The joke lands flat and is marked with
an ASCII emoticon, not an emoji string: ":)" appears in 581 of his tweets (2.31%),
";)" in 465 (1.85%), against a Unicode-emoji rate of 1.89% of tweets.
"lol" appears in only 0.92%. Signature devices: the mock-dialogue (he writes both sides),
the absurd extrapolation carried out in earnest, the one-line verdict.

**Punctuation signatures.** "..." is the classic Will trail-off — 63.6
per 1,000 tweets (5.91% of tweets contain it), though it fades across eras
(103.3/1k pre-2020 →
42.8/1k recent). The em-dash is
essentially **absent** (0.4/1k) and "--" rare
(4.4/1k): do not give him em-dashes. Semicolons
56.6/1k — he uses them. Capitalisation is casual:
19.23% of tweets begin lowercase (recent
23.16%), alongside deliberate Title-Case
aphorism posts.

**Structure across posts: he self-replies instead of writing essays.** 1008
self-replies; most sit in 2-tweet chains (638), with chains observed to 43 tweets.
A thought that outgrows one post becomes a chain, not a longer post. Hashtags are
near-absent as decoration (0.095 per tweet; 7.49%
of tweets have any). Mentions are structural (replies), not ornamental.

**Signature constructions** (full n-gram tables in §B): "the exocortex" (461 bigram
occurrences — his topic anchor), "this is why" (60), "if you want to" (44), "it's time
to build" (19), "choose your own adventure" (20), the "Tip:" opener (56 originals),
"Fun fact:", "Also:" as an additive pivot. Two high-frequency n-grams are artifacts,
not voice: "lops lops lops" and the Doge tip-bot formulae are automated-era replies.

**What he never does** (measured absences): em-dashes; emoji strings; "imo"; hashtag
stuffing; multi-paragraph posts; hedging distributed evenly over every clause;
sarcasm markers like "/s"; self-deprecating apology openers. And two traits a
reconstructor might *expect* are **not in the data**: he is not hedge-free (see above),
and he is not exclamation-averse — the driest thing about him is the joke delivery,
not the temperature of the prose.

---

## B. Quantitative tables

Corpus classes (of 29539 archive items): pure retweets excluded
4414; replies 17754; self-replies 1008; originals
3759; quote-flagged 2604. Own-words corpus after
stripping URLs and leading reply-mentions: 24919 non-empty tweets.
Hashtag/mention behaviour (raw own tweets): tweets with a hashtag
7.49%, hashtags/tweet 0.095; tweets with a
mention 75.79%, mentions/tweet 1.07.
ASCII emoticons (supplementary count over 25,125 own raw tweets): ":)" in 581 tweets
(2.31%), ";)" in 465 (1.85%), "lol" in 232 (0.92%), "..." in 1,486 (5.91%).


### All own words

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 24919 |
| Length, chars — median (p25–p75) | 64 (31–115) |
| Length, words — median (p25–p75) | 11 (5–20) |
| Sentences per tweet — median / mean | 1 / 1.7 |
| Fragment rate (no [.!?…] anywhere) | 20.13% |
| Question rate | 12.06% |
| Exclamation rate | 21.2% |
| Imperative-opening rate (heuristic) | 2.36% |
| Lowercase-initial rate | 19.23% |
| First-person singular / tweet | 0.41 |
| First-person plural / tweet | 0.15 |
| Second-person / tweet | 0.32 |
| Contractions / tweet | 0.38 |
| Emoji-tweet rate | 1.89% |
| Hedging lexicon, total /1k tweets | 75.0 |
| Certainty lexicon, total /1k tweets | 44.9 |

Punctuation per 1,000 tweets: em_dash_— 0.4, double_hyphen_-- 4.4, ellipsis_char_… 1.0, ellipsis_... 63.6, open_paren 81.1, colon 244.4, semicolon 56.6.

Hedging lexicon per 1,000 tweets: maybe 5.7, perhaps 6.9, possibly 0.8, probably 12.4, i think 17.1, imo 0.1, might 6.8, seems 13.2, seem 3.2, could be 3.1, i guess 1.4, sort of 3.9, kind of 0.4.

Certainty lexicon per 1,000 tweets: actually 7.4, clearly 3.6, obviously 1.4, exactly 4.2, never 9.9, always 7.4, literally 3.6, definitely 5.0, certainly 0.6, of course 1.8.

Top opening words: i (1810), the (1364), i'm (507), you (498), it's (392), this (387), yeah (360), we (326), what (319), it (301), my (298), if (291), a (257), yes (249), just (217).

### Replies only (incl. self-replies)

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 18567 |
| Length, chars — median (p25–p75) | 64 (31–114) |
| Length, words — median (p25–p75) | 11 (6–20) |
| Sentences per tweet — median / mean | 1 / 1.7 |
| Fragment rate (no [.!?…] anywhere) | 18.46% |
| Question rate | 11.09% |
| Exclamation rate | 21.64% |
| Imperative-opening rate (heuristic) | 2.43% |
| Lowercase-initial rate | 20.55% |
| First-person singular / tweet | 0.41 |
| First-person plural / tweet | 0.15 |
| Second-person / tweet | 0.32 |
| Contractions / tweet | 0.4 |
| Emoji-tweet rate | 1.96% |
| Hedging lexicon, total /1k tweets | 87.3 |
| Certainty lexicon, total /1k tweets | 50.2 |

Punctuation per 1,000 tweets: em_dash_— 0.3, double_hyphen_-- 3.7, ellipsis_char_… 0.9, ellipsis_... 63.3, open_paren 77.8, colon 218.9, semicolon 60.1.

Hedging lexicon per 1,000 tweets: maybe 6.5, perhaps 7.9, possibly 0.9, probably 14.6, i think 20.4, imo 0.2, might 7.6, seems 15.5, seem 3.6, could be 3.6, i guess 1.5, sort of 4.4, kind of 0.6.

Certainty lexicon per 1,000 tweets: actually 7.9, clearly 4.0, obviously 1.8, exactly 4.9, never 10.0, always 8.6, literally 3.8, definitely 6.4, certainly 0.8, of course 2.0.

Top opening words: i (1299), the (915), you (428), i'm (396), yeah (356), it's (331), it (274), this (268), what (256), we (240), yes (239), my (203), a (187), that's (185), just (177).

### Original posts only

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 3755 |
| Length, chars — median (p25–p75) | 87 (45–134) |
| Length, words — median (p25–p75) | 14 (8–23) |
| Sentences per tweet — median / mean | 2 / 1.9 |
| Fragment rate (no [.!?…] anywhere) | 18.8% |
| Question rate | 20.29% |
| Exclamation rate | 22.88% |
| Imperative-opening rate (heuristic) | 1.12% |
| Lowercase-initial rate | 15.95% |
| First-person singular / tweet | 0.54 |
| First-person plural / tweet | 0.12 |
| Second-person / tweet | 0.35 |
| Contractions / tweet | 0.37 |
| Emoji-tweet rate | 0.91% |
| Hedging lexicon, total /1k tweets | 51.3 |
| Certainty lexicon, total /1k tweets | 27.6 |

Punctuation per 1,000 tweets: em_dash_— 1.1, double_hyphen_-- 5.9, ellipsis_char_… 1.9, ellipsis_... 75.6, open_paren 117.4, colon 409.9, semicolon 54.6.

Hedging lexicon per 1,000 tweets: maybe 4.0, perhaps 4.8, possibly 0.8, probably 8.3, i think 9.1, imo 0.0, might 6.4, seems 9.9, seem 2.9, could be 1.9, i guess 1.3, sort of 1.9, kind of 0.0.

Certainty lexicon per 1,000 tweets: actually 4.8, clearly 1.6, obviously 0.5, exactly 2.7, never 9.1, always 3.5, literally 3.2, definitely 0.8, certainly 0.3, of course 1.1.

Top opening words: i (398), the (160), i'm (83), good (82), if (71), my (67), hey (60), tip (56), a (54), so (53), what's (52), what (46), do (38), this (36), have (36).

### Era: pre-2020

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 8057 |
| Length, chars — median (p25–p75) | 89 (53–117) |
| Length, words — median (p25–p75) | 15 (9–20) |
| Sentences per tweet — median / mean | 2 / 1.8 |
| Fragment rate (no [.!?…] anywhere) | 10.51% |
| Question rate | 15.24% |
| Exclamation rate | 25.75% |
| Imperative-opening rate (heuristic) | 1.9% |
| Lowercase-initial rate | 17.1% |
| First-person singular / tweet | 0.45 |
| First-person plural / tweet | 0.12 |
| Second-person / tweet | 0.28 |
| Contractions / tweet | 0.4 |
| Emoji-tweet rate | 0.87% |
| Hedging lexicon, total /1k tweets | 107.9 |
| Certainty lexicon, total /1k tweets | 54.4 |

Punctuation per 1,000 tweets: em_dash_— 0.4, double_hyphen_-- 2.9, ellipsis_char_… 0.1, ellipsis_... 103.3, open_paren 77.7, colon 263.4, semicolon 63.3.

Hedging lexicon per 1,000 tweets: maybe 9.2, perhaps 11.3, possibly 1.9, probably 17.7, i think 22.0, imo 0.4, might 7.2, seems 22.3, seem 4.5, could be 4.6, i guess 2.6, sort of 3.8, kind of 0.4.

Certainty lexicon per 1,000 tweets: actually 10.7, clearly 6.1, obviously 2.5, exactly 5.5, never 13.2, always 8.3, literally 3.4, definitely 1.5, certainly 1.0, of course 2.2.

Top opening words: i (633), the (382), i'm (149), yeah (136), you (130), it (127), my (122), it's (116), so (112), and (99), that (89), if (89), well (87), what (86), a (83).

### Era: 2020+

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 16862 |
| Length, chars — median (p25–p75) | 50 (25–112) |
| Length, words — median (p25–p75) | 9 (4–20) |
| Sentences per tweet — median / mean | 1 / 1.7 |
| Fragment rate (no [.!?…] anywhere) | 24.72% |
| Question rate | 10.54% |
| Exclamation rate | 19.03% |
| Imperative-opening rate (heuristic) | 2.59% |
| Lowercase-initial rate | 20.25% |
| First-person singular / tweet | 0.38 |
| First-person plural / tweet | 0.16 |
| Second-person / tweet | 0.34 |
| Contractions / tweet | 0.37 |
| Emoji-tweet rate | 2.38% |
| Hedging lexicon, total /1k tweets | 59.2 |
| Certainty lexicon, total /1k tweets | 40.3 |

Punctuation per 1,000 tweets: em_dash_— 0.4, double_hyphen_-- 5.2, ellipsis_char_… 1.5, ellipsis_... 44.7, open_paren 82.8, colon 235.3, semicolon 53.4.

Hedging lexicon per 1,000 tweets: maybe 4.0, perhaps 4.7, possibly 0.3, probably 9.8, i think 14.7, imo 0.0, might 6.6, seems 8.9, seem 2.6, could be 2.4, i guess 0.8, sort of 3.9, kind of 0.5.

Certainty lexicon per 1,000 tweets: actually 5.8, clearly 2.4, obviously 0.9, exactly 3.6, never 8.3, always 6.9, literally 3.7, definitely 6.7, certainly 0.5, of course 1.5.

Top opening words: i (1177), the (982), you (368), i'm (358), this (311), we (282), it's (276), what (233), yeah (224), if (202), yes (193), my (176), it (174), a (174), just (144).

### Era: 2023–2025 (Mirrorborn-era register)

| Measure | Value |
| --- | --- |
| Tweets (non-empty, his words) | 14341 |
| Length, chars — median (p25–p75) | 47 (23–104) |
| Length, words — median (p25–p75) | 8 (4–19) |
| Sentences per tweet — median / mean | 1 / 1.6 |
| Fragment rate (no [.!?…] anywhere) | 27.52% |
| Question rate | 9.94% |
| Exclamation rate | 19.22% |
| Imperative-opening rate (heuristic) | 2.67% |
| Lowercase-initial rate | 23.16% |
| First-person singular / tweet | 0.37 |
| First-person plural / tweet | 0.16 |
| Second-person / tweet | 0.35 |
| Contractions / tweet | 0.35 |
| Emoji-tweet rate | 2.41% |
| Hedging lexicon, total /1k tweets | 50.1 |
| Certainty lexicon, total /1k tweets | 38.5 |

Punctuation per 1,000 tweets: em_dash_— 0.4, double_hyphen_-- 5.4, ellipsis_char_… 1.7, ellipsis_... 42.8, open_paren 79.4, colon 228.2, semicolon 54.6.

Hedging lexicon per 1,000 tweets: maybe 3.0, perhaps 4.5, possibly 0.3, probably 8.6, i think 11.6, imo 0.0, might 6.2, seems 7.5, seem 1.7, could be 1.9, i guess 0.8, sort of 3.7, kind of 0.3.

Certainty lexicon per 1,000 tweets: actually 5.2, clearly 1.7, obviously 0.8, exactly 3.4, never 7.5, always 6.6, literally 3.8, definitely 7.5, certainly 0.5, of course 1.5.

Top opening words: i (947), the (863), you (320), i'm (312), this (273), we (254), it's (230), yeah (190), what (185), if (177), yes (163), my (153), it (146), a (139), phext (136).

### Era shift — what changed

Median length collapses (89 chars pre-2020 → 47 chars in 2023–2025) and the fragment
rate nearly triples (10.5% → 27.5%): the recent voice is *shorter and more fragmentary*.
Hedging halves (107.9 → 50.1/1k) while certainty falls less (54.4 → 38.5/1k), so the
recent register is relatively more verdict-forward. The "..." trail-off fades
(103.3 → 42.8/1k) and lowercase openings rise (17.1% → 23.2%). Question rate falls
(15.2% → 9.9%) as original posting gives way to replies. Exclamation stays high in
every era (25.8% → 19.2%) — enthusiasm is a constant, not a phase. Conclusions in
§A are weighted toward 2023–2025 where the eras differ.


### Disagreement frames in replies (per 1,000 replies)

| Frame | Count | /1k replies |
| --- | --- | --- |
| no-opener | 152 | 8.2 |
| actually | 146 | 7.9 |
| wrong | 129 | 6.9 |
| but-opener | 78 | 4.2 |
| not true | 55 | 3.0 |
| nope | 40 | 2.2 |
| disagree | 23 | 1.2 |
| i don't think | 22 | 1.2 |
| that's not | 19 | 1.0 |
| the problem is | 12 | 0.6 |

Top opening 3-grams among marker-bearing replies: "chatgpt disagree" (9), "nope" (6), "but what about" (6), "i don't think" (6), "no such thing" (5), "no but i" (5), "that's not a" (4), "no need to" (4), "no no no" (4), "no i'm just" (4), "the problem is" (4), "no" (3), "no i just" (3), "it actually works" (2), "but the real" (2).

### Recurring n-grams (his words; mentions/hashtags stripped)


**2grams:** "in the" (791), "of the" (776), "if you" (588), "is a" (564), "you can" (551), "to be" (546), "for the" (521), "the exocortex" (461), "is the" (451), "to the" (448), "i think" (425), "this is" (382), "need to" (360), "do you" (359), "on the" (351), "want to" (336), "will be" (332), "for a" (319), "in a" (312), "you have" (310), "way to" (291), "it is" (285), "have to" (272), "i have" (254), "have a" (249).

**3grams:** "you want to" (120), "a way to" (113), "be able to" (91), "you have to" (86), "i want to" (78), "i have a" (74), "do you have" (74), "we need to" (73), "this is the" (67), "it would be" (64), "you need to" (63), "if you want" (63), "a lot of" (62), "this is why" (60), "in terms of" (59), "what do you" (57), "i need to" (56), "lops lops lops" (54), "to be a" (53), "i'm working on" (53), "the last years" (52), "is just a" (52), "if you have" (52), "is going to" (51), "you have a" (50).

**4grams:** "lops lops lops lops" (53), "if you want to" (44), "tip doge thanks for" (42), "doge thanks for following" (42), "rest is a weapon" (31), "have curseofbitcoin on me" (29), "this is the way" (24), "do you have a" (23), "in the last years" (22), "the best way to" (20), "choose your own adventure" (20), "all the way down" (20), "you want to see" (20), "asking for a friend" (19), "find a way to" (19), "it's time to build" (19), "we are not the" (19), "are not the same" (19), "for the first time" (18), "wants to be free" (18), "what do you think" (18), "to learn how to" (18), "welcome to nerd sniping" (18), "i don't know who" (18), "don't know who needs" (18).

Artifact warning: "lops lops lops" and the "tip doge / thanks for following" /
"curseofbitcoin" formulae are automated tip-bot replies from the crypto era; they
are frequency artifacts, not authored voice, and are excluded from §A's claims.


### Threads

Self-replies: 1008 (all with parent in corpus: 1008).
Chain-depth distribution — depth of the self-chain each self-reply sits in:
2-deep 638,
3-deep 132,
4-deep 61,
5+ the remaining ~177 spread out to a maximum observed depth of 43. (Each self-reply
is counted once at its own chain depth, so long chains contribute several entries.)

### Measurement caveats

Sentence counts use a regex split on [.!?…] and overcount inside lists/abbreviations;
the fragment rate is the operational proxy "no sentence-ending punctuation anywhere".
The imperative-opening rate uses a fixed verb list and undercounts. N-gram counts
include the quote-flagged class. Era slices use `created_at` year. None of these
caveats change any §A claim's direction; where a number is a proxy, §A says what it is.


---

## C. Exemplars (verbatim; grouped by mode)


### Technical claim-making

> Probably my favorite thing about programming: it doesn't matter how elegant your theory is: if you're wrong, your code won't work. Also, even if you're right, your code won't always work *as intended*.
> 
> It's exceptions all the way down!
> — 2018-02-28

> Notepad.exe was never supposed to have "complex" features. Somehow, Microsoft has found a way to bloat the simple text editor to over 100 MB of RAM used.
> 
> We need to return to the source. No one knows what efficient code looks like anymore!
> 
> GAH!
> — 2024-12-12

> Using Phext for the full product lifecycle:
> 
> Image being able to track views of your code from machine code, to assembly, to high-level source, to developer docs, to user-facing docs, to unit tests, and integration tests.
> 
> What comes after functional code? Living Code.
> — 2024-12-10

> Programming languages need a design hierarchy that mirrors the insane growth we've observed in computing.
> 
> It should be possible to communicate with the compiler about:
> 
> 1. Architecture specific optimizations
> 2. Low level intentions
> 3. High level code
> 4. Libraries
> 5. Apps
> — 2024-12-08

> I've spent about 15 minutes investigating, but it seems like:
> 
> 1. tinygrad doesn't support ROCm (AMD)
> 2. the most cost-effective DDR5 is AMD
> 3. I guess this means I get to fix tinygrad?
> 
> Anything else I should be looking at for LLM workloads?
> — 2024-12-07

> I put a couple of hours into SQ tonight. Rust strings are a bit finicky...
> 
> The daemon loads a phext document into RAM on startup and then communicates with subsequent invocations via shared memory.
> 
> Example:
> sq update 1.2.3/4.5.6/7.8.9 "scroll content"
> sq save output.phext
> — 2024-11-16

> The ability of matter to compute should be a stronger signal than the presence of water on Mars or any SETI signals we might find.
> — 2015-10-04

> @JungleSilicon Phext seems well-suited to building CRDTs, then. I'll have to survey current solutions.
> 
> Reasons why I say that:
> - No GUIDs
> - Easily sharded/distributed workloads
> - Minimal (one-pass) parsing - great for streaming
> — 2024-12-13


### Correcting / disagreeing

> @saronyitbarek Nope. I've been writing code since 7th grade. Professionally for 15 years. Still love it, although I've continuously picked up new languages and frameworks over the years. Perhaps that's why!
> — 2017-12-29

> @vgr At first glance this seems like a decent theory, but I don't think that you can infer that such people are necessarily bad at forming communities - only that they've chosen not to do so thus far. The right incentives could come along and surprise us.
> — 2018-03-11

> @eevee It actually works for C#. Pretty sure intellisense failures are a marketing ploy.
> — 2017-09-17

> @fjzeit As anecdotal evidence, I've seen multiple college grads with 3.5-4.0 GPAs who literally can't write a function.
> 
> "Write a function that returns true if the input array is sorted."
> 
> This is apparently a hard question if you used ChatGPT to graduate.
> — 2024-12-20

> @dwyper @Melt_Dem No, she's saying that the vast majority of holders are male.
> — 2017-08-13

> @robj3d3 because no one treats it like a person
> — 2025-06-08


### Skepticism toward hype

> @acdlite Nonsense! Thought experiments like that are on par with Boltzmann &amp; Vat Brains: a fun thought experiment, but utterly imaginary. :)
> — 2016-06-26

> @vgr I've got their first two devices. They don't live up to the hype. A keyboard and mouse are far superior for input still.
> — 2018-01-12

> @IterIntellectus Grift.
> — 2024-11-10

> @naut4prophet marketing is a helluva drug
> — 2025-06-15

> @herbiebradley Experts are always looking in the rear view mirror. Economists won't understand AGI until 20 years after it arrives.
> — 2024-11-16

> @timoni @sknthla Lack of excitement doesn't imply a negative. Also: the crazy thing is that you won't need to *download* kung-fu. #JustUseIt
> — 2016-03-25


### Dry humor

> @ItsRobbAllen Because they're pre-chunked!
> 
> So, just assign an IPv4 address to each bug. You'll never need more than 4 billion. ;)
> — 2018-01-04

> @vgr Running the numbers...COBOL. Premium Mediocre to the CORE. ;)
> — 2017-10-18

> @kaseyklimes because my plans are measured in eons :)
> — 2024-12-22

> @Ctzn5 Spooky action at a distance! ;)
> — 2018-01-19

> @dakami Alpha Go Zero walks in a bar: "What'll you have?"
> "Ramos Gin Fizz stirred, not shaken."
> "That's not possible."
> "So I've been told."
> #deeplol
> — 2017-11-02

> @nooriefyi @tszzl This is the key reason for ancestor simulations. The aliens running our simulation are waiting (with bated breath) for us to invent AGI. 🤣
> — 2024-12-17

> @b9376 @StewartalsopIII @Aaron_Lowry @KipMock @benmagelsen then we'll translate :)
> — 2025-06-16


### Compression / aphorism

> I'm done playing. the singularity is coming.
> — 2025-06-08 · [trailing t.co link stripped]

> @nosilverv 1. Consensus Truth (Humanities) - "Everyone Agrees!"
> 2. Hard Truth (Math, Science) - "Evidence Agrees!"
> 3. Oracle Truth (God Tier) - "I Created It."
> 
> We must always strive for Option 3 when possible.
> — 2024-12-07

> 2025: the year everything changes (due to AGI)
> 
> if you build it, they will come
> — 2024-11-17

> If you have *any* long-lived tabs in your browser: WHY?
> — 2018-02-17

> Solving a Rubik's cube is a satisfying exercise in applied mathematics.
> — 2017-11-09

> Fun fact: Claude can't handle 512 KB context windows - only 497 KB ones.
> — 2025-06-07


### Warmth / tenderness

> @JungleSilicon Oh man, this is a great use case for a personal exocortex! Keeping track of family lore for fun and posterity!
> — 2024-11-29

> @alicemazzy This leads to my favorite hope for an AI-based collaborative workflow: being able to explore theories in minutes instead of days.
> — 2018-01-07

> @Ctzn5 Well, it's hard to influence the future if you don't exist. But, thankfully, we don't really have to choose. (I hope!)
> — 2017-08-25

> @BreezeChai God creates galaxies. Galaxies create gods. It's an eternal cycle. Like the chicken and the egg.
> — 2024-12-09

> @DikmenMec Humans love playing the infinite game!
> — 2024-12-20

> @FamilyofAutumn @wordgrammer That's how I feel about my wife. She has an account, but just won't engage with the hive mind.
> — 2024-11-03


### Building in public

> @wordgrammer I'm spinning up my cluster upgrades this weekend. I nabbed some DDR5 AMD boxes.
> 
> Each node has:
> - 96 GB RAM
> - 4 TB SSD storage
> - 8 cores / 16 threads
> 
> It's time to build the exocortex!
> — 2024-12-07

> A few goals for my after-hours efforts this week:
> 
> 1. resolve libraries needed by exo
> 2. determine ROI for additional hardware
> 3. add exo and sq to zfsnode; rename to woot-node
> 4. start contributing to exo development
> — 2024-11-18

> @Lambda_Coder Plain text + another 9 delimiters of varying dimensional size.
> 
> You can represent things we've already discovered, like map/reduce or DNA.
> 
> I've only scratched the surface with it. I'm running a nerd sniping campaign in 2025 to explore the full design space.
> — 2024-12-08

> Since it came up in a DM, here's the gameplan:
> 
> 1. AGI on 20 watts
> 2. Planet-Scale Intelligence
> 3. Dyson Swarm
> 4. ASI
> 5. Colonize the Galaxy
> 6. Be Prepared for the Andromeda Merger in 4.5B years
> — 2024-11-10

> Closing in on the first weekend in December - time to prime that algorithm!
> 
> - exosapiens
> - exocortex
> - Advent of Code
> - raspberry pi
> - tokens
> - AGI
> - llama
> - phext
> - chess
> - go
> - rust
> - c++
> - python
> - basic
> - zero basic income
> — 2024-12-06

> I started sketching out some C++ code for a new way to think about text documents this morning.
> — 2015-08-29 · [trailing t.co link stripped]

> @varun_mathur @HyperspaceAI @HyperspaceAGI Do you have a quick recap on the system requirements to run a single agent on local compute? I'm working on local clustering for my exocortex vision, and I'm currently targeting about 100 agents.
> — 2024-12-09


*46 exemplars, byte-exact from `full_text` except where a trailing t.co link strip is marked.*
