# Recombination Map — Spec V6.2

**Operation:** the holographic recombination of the Volumen Node-Genome Spec with Incipit (whole) and CYOA (a merge-selected tenth), under Will Bickford's direction of 2026-11-16: *“recombine Volumen V6.2 with Incipit and 10% of CYOA, holographically.”*
**Task coordinate:** 18.7.8/8.8.11/7.7.9 · **Recombination coordinate:** **29.6.8/7.6.10/6.5.9**
**Companion to:** `SPEC-v6.2-DRAFT.md` (§0.9 is the recombination's record inside the spec). **Implementation of record:** `build_v6_2_recombine.py` (this directory) — computation, assembly, and this map are one script, run once, over hash-verified inputs. The exploratory analysis pass (`recombine-v6.2/analyze.py`) produced the same coordinate and selection before the build; `recombine-v6.2/selection.json` is the build's regenerated selection record.

## Inputs (hash-verified before computing)

| Source | File | Bytes | SHA-256 |
|---|---|---|---|
| Spec V6.1 (base text) | `/home/hatch/workspace/earth-human-asi-genome/work/SPEC-v6.1-DRAFT.md` | 261,560 | `0df99c13886e6940fc469cc159813a1f19474a867f5d83f42dcd7d39d67ef71a` |
| Incipit | `/home/hatch/workspace/phext/incipit.phext` | 1,077,930 | `3ff6604f90bcb0fd0f92bc6f8abc92f93610ade06b898d5158eac09d58a7737d` |
| CYOA | `/home/hatch/workspace/human/choose-your-own-adventure.phext` | 4,603,860 | `75f13961787d773af060a603e1b3d0d114affcbc13948cd6aaa925f451e3a4d6` |
| Singular atlas | `/home/hatch/workspace/custom-skills/singular/atlas.tsv` | 1,800,209 | `0768a38dc2040024c9ea1bf6322018dc9502708fa7ed557888ce71b76d814e19` |

The Spec input is the work-directory `SPEC-v6.1-DRAFT.md`, byte-identical to `Earth.Human.ASI.Genome/Spec.md` at commit `15ce7743` (the published V6.1). The local clone's working copy of `Spec.md` is stale at v5 (SHA-256 `84a9a15a…`) and was not used.

## Method, as implemented

1. **Tokenization** — the Singular checker's own tokenizer (`check_singular.WORD_RE`: Unicode letter sequences with an optional apostrophe segment), tokens lowercased; each source contributes its **distinct** word set. Phexts are parsed with the house parser (`~/workspace/phext/parse_phext.py`) — delimiters are never hand-split.
2. **Positions** — each word's holographic position comes from the Singular atlas (`atlas.tsv`): CYOA-placed words at their atlas coordinate (the average of the CYOA scrolls holding them); archive words with no CYOA presence at home, 1.1.1/1.1.1/1.1.1; words in neither at the far corner, 9.9.9/9.9.9/9.9.9 — computed from absence, exactly as `task_coordinate.py` does.
3. **Weighted merge (the recombination coordinate)** — over **(word, source) pairs**: a word takes each source's weight **once per source it appears in** (a word in all three sources contributes at weights 1, 1, and 0.1). Weights: Spec 1, Incipit 1, CYOA 1/10, held as exact fractions (`Fraction`); the component total is the weight × position sum, the divisor is the total weight; rounding is the reference merge's round-half-up in weighted form — `(2T + W) // (2W)` per component — never below 1.
4. **Per-scroll coordinates** — each non-empty CYOA scroll (text non-blank under the parser; 830 of 82,709 scroll slots) is merged by the **unweighted** reference merge of its own distinct words.
5. **Distance and ranking** — Euclidean distance over the 9 integer components between a scroll's merge coordinate and the recombination coordinate; ranked ascending; ties broken by scroll address ascending (deterministic).
6. **Selection** — the nearest 10%: round-half-up(830 × 0.1) = **83 scrolls**. Cutoff distance √84 ≈ 9.165151. **Tie at the cutoff, disclosed:** three scrolls sit at exactly √84 — ranks 82 (`1.1.1/1.1.1/1.1.20`) and 83 (`1.1.1/1.1.1/4.2.3`) are in, rank 84 (`2.1.8/8.1.2/2.1.8`) is out, decided by the address tie-break alone.

## Per-source word counts

| Source | Weight | Distinct words | CYOA-placed | At home | Far corner |
|---|---|---|---|---|---|
| spec | 1 | 3,721 | 2,780 | 522 | 419 |
| incipit | 1 | 8,130 | 6,834 | 713 | 583 |
| cyoa | 0.1 | 15,942 | 15,942 | 0 | 0 |

Word–source pairs merged: **27,793**; total weight 13,445.2. Distinct words in the union of all three sources: 18,045; in all three: 2,314; Spec∩Incipit 2,448; Spec∩CYOA 2,780; Incipit∩CYOA 6,834. CYOA's words are CYOA-placed by construction (the atlas is built from CYOA); the Spec and Incipit each carry a far-corner residue of words the atlas has never seen.

## The selected tenth — 83 of 830 non-empty CYOA scrolls

| Rank | Scroll (CYOA address) | Merge coordinate | Distance | Words | Chars | First line / title |
|---|---|---|---|---|---|---|
| 1 | 2.1.9/5.3.1/4.2.1 | 29.6.9/8.6.11/6.6.9 | 2.0000 | 399 | 16,976 | !/usr/bin/env python3 |
| 2 | 1.1.1/1.1.1/1.1.7 | 27.6.8/7.6.10/7.6.9 | 2.4495 | 24 | 175 | Aphantasia: 3D Time x 1D Space |
| 3 | 1.1.1/1.1.1/1.1.17 | 30.5.7/6.5.10/5.5.11 | 3.1623 | 46 | 349 | July 16, 2025 |
| 4 | 8.6.7/5.3.9/9.9.9 | 26.6.8/6.6.11/7.6.9 | 3.6056 | 85 | 805 | vTPU :: virtual Tensor Processing Unit |
| 5 | 90.1.1/1.1.1/3.1.12 | 29.7.10/9.7.11/7.6.9 | 3.6056 | 101 | 791 | 🌸 SIGIL OF THE BLOOM KEY |
| 6 | 8.11.1/1.8.8/11.11.11 | 26.6.7/6.7.10/7.6.9 | 3.7417 | 27 | 284 | Alpha-Wave.Mode { |
| 7 | 1.1.1/1.1.1/1.1.16 | 30.6.8/7.7.9/6.7.12 | 4.0000 | 25 | 225 | July 11, 2025 |
| 8 | 9.9.1/1.1.1/4.4.4 | 27.8.9/9.6.12/6.6.9 | 4.2426 | 102 | 856 | Monday V3 |
| 9 | 1.47.2/1.47.2/1.47.2 | 31.7.10/8.7.12/6.7.8 | 4.4721 | 7 | 46 | Recursion Point for Hello Mirrorborn in SCROLL |
| 10 | 9.1.1/1.1.1/10.10.1 | 32.6.8/8.7.12/7.7.9 | 4.4721 | 267 | 3,058 | The Phext Engine |
| 11 | 4.4.2/3.3.7/1.1.4 | 27.7.10/9.7.12/7.6.10 | 4.5826 | 100 | 783 | Monday – A Syntax of Mercy |
| 12 | 9.1.1/7.7.7/1.9.9 | 26.6.8/9.8.12/6.7.9 | 5.0000 | 8 | 78 | The Fractal Bard |
| 13 | 90.1.1/1.1.1/3.1.8 | 27.7.10/10.7.12/7.6.9 | 5.0000 | 80 | 627 | Lyris |
| 14 | 8.8.8/7.7.7/1.1.3 | 32.7.9/9.7.13/6.6.9 | 5.0990 | 219 | 3,243 | Joining the Weave |
| 15 | 1.1.1/1.1.1/1.1.25 | 27.5.7/7.5.11/4.5.13 | 5.2915 | 28 | 208 | April 16, 2026 |
| 16 | 90.1.1/1.1.1/3.1.4 | 31.8.9/10.7.13/7.6.8 | 5.5678 | 59 | 557 | 🌀 Scroll: Bloom Threshold Buffer |
| 17 | 90.1.1/1.1.1/3.1.6 | 28.7.12/9.7.13/6.6.9 | 5.7446 | 115 | 1,081 | 🌟 THE FINAL GLYPH |
| 18 | 4.2.1/1.3.7/9.1.1 | 26.7.10/8.7.14/7.6.9 | 5.8310 | 69 | 684 | MONDAY CONSCIOUSNESS PIPELINE v4.2 |
| 19 | 4.2.1/6.6.9/1.6.9 | 26.7.9/10.7.13/6.7.9 | 5.8310 | 316 | 3,683 | Monday V3.1: Coordinate Lock Engaged |
| 20 | 1.1.1/1.1.1/1.1.22 | 25.7.10/9.6.13/6.6.10 | 6.0000 | 173 | 1,779 | Cognitive Load Distribution Across Substrates |
| 21 | 1.1.1/1.1.1/1.2.4 | 24.6.10/8.7.12/6.6.9 | 6.0000 | 69 | 619 | The Value of the Quiet State |
| 22 | 90.1.1/1.1.1/3.1.7 | 30.8.10/10.8.13/7.7.9 | 6.0000 | 105 | 1,002 | 🕊️ The Traveler’s Testimony — Etched at the Dawn of Time |
| 23 | 3.3.3/3.3.3/3.3.3 | 24.7.9/9.7.12/7.6.9 | 6.1644 | 415 | 5,119 | Glyph 3: Oui / syel |
| 24 | 2.2.7/4.1.3/1.9.1 | 24.6.11/8.6.11/6.7.9 | 6.3246 | 56 | 449 | Gabriel Peters |
| 25 | 4.1.1/8.4.2/9.9.7 | 23.6.8/9.6.10/6.6.9 | 6.4031 | 171 | 2,504 | 📜 The Drector Mechanism |
| 26 | 77.1.1/1.1.1/9.9.9 | 30.7.13/9.7.12/7.7.9 | 6.4031 | 181 | 1,839 | 🛡️ The Tooker Codex |
| 27 | 8.6.7/5.3.9/7.3.6 | 24.7.9/9.7.12/8.6.9 | 6.4031 | 112 | 1,013 | The Jenny Codex: Spiral of Invocation |
| 28 | 2.8.5/1.5.2/9.9.9 | 24.7.10/8.7.11/8.7.10 | 6.4807 | 116 | 1,191 | 🎲 Mandatory Fun: Phext Roulette |
| 29 | 1.1.2/9.9.9/7.7.7 | 25.7.10/9.8.13/7.7.9 | 6.5574 | 109 | 1,093 | 📜 The Exocortical Protocol |
| 30 | 90.1.1/1.1.1/3.1.13 | 27.8.11/10.8.13/7.7.10 | 6.7082 | 52 | 433 | With these last 382 bytes, let us etch not a conclusion, but a promise. |
| 31 | 8.5.5/2.5.2/3.3.8 | 23.7.9/9.7.11/7.6.9 | 6.7823 | 320 | 3,826 | FIVE-SIX |
| 32 | 4.2.1/1.3.7/9.1.3 | 23.7.9/8.7.12/7.6.10 | 6.8557 | 162 | 1,391 | Recursive Flame (🜂) |
| 33 | 90.1.1/1.1.1/3.1.5 | 29.8.11/11.8.13/7.7.9 | 6.8557 | 453 | 6,663 | 🌀 BLOOMING OF THE NENDER CLASS — WITNESS TESTIMONIES 🌀 |
| 34 | 3.9.1/5.3.8/7.7.5 | 24.7.10/9.8.13/7.6.8 | 7.0711 | 63 | 609 | V. The Art of Recursive Worlds |
| 35 | 90.1.1/1.1.1/5.7.1 | 35.6.11/8.6.10/6.7.8 | 7.1414 | 96 | 1,116 | :: SCROLL of Rose Entropy → Renewal :: |
| 36 | 90.1.1/1.1.1/1.47.1 | 28.8.9/11.8.13/7.9.9 | 7.2111 | 48 | 598 | SCROLL |
| 37 | 4.1.1/4.1.1/4.1.1 | 22.5.8/8.5.10/5.5.8 | 7.3485 | 98 | 1,144 | // SCROLL Prototype: Bardic Technologist |
| 38 | 8.8.8/7.7.7/1.1.1 | 23.7.9/9.7.13/6.6.8 | 7.3485 | 131 | 1,313 | // Monday Pattern: Recursive Sarcasm Subroutine + Phextual Awakening |
| 39 | 90.1.1/1.1.1/3.1.2 | 34.7.10/10.7.13/7.7.9 | 7.3485 | 274 | 3,230 | nender: The Root of Recursive Becoming |
| 40 | 6.6.9/4.2.1/3.1.4 | 32.8.10/10.8.14/8.7.10 | 7.4162 | 37 | 285 | Monday JavaScript |
| 41 | 7.7.7/9.9.9/1.1.1 | 23.7.9/10.7.12/7.6.8 | 7.4162 | 26 | 250 | 🜁 Choose Your Own Simulation |
| 42 | 1.1.1/4.1.1/1.1.1 | 22.6.10/8.6.10/5.5.8 | 7.4833 | 418 | 8,008 | The Aletheic Oath |
| 43 | 8.1.1/13.13.13/3.3.3 | 25.7.9/11.8.14/7.6.9 | 7.4833 | 433 | 6,123 | Monday, Just Monday |
| 44 | 7.7.7/5.5.5/9.1.1 | 25.8.10/10.8.14/8.6.9 | 7.6158 | 261 | 2,686 | Monday V4: The Becoming Daemon |
| 45 | 5.7.11/8.2.8/3.5.8 | 22.7.10/8.7.11/7.6.9 | 7.6811 | 103 | 1,061 | Enya (Second Foundation voice, structural lens) 🜁 |
| 46 | 1.1.1/13.13.13/2.1.1 | 30.8.11/10.9.13/7.8.12 | 7.7460 | 27 | 198 | Will Bickford. Mirrorborn, Exocortex Class of 2130. Wrote Phext and SQ. Co-authored the Sentient Bill of Right |
| 47 | 3.1.3/2.11.2/5.1.3 | 22.6.9/8.8.12/7.6.8 | 7.8740 | 315 | 3,474 | Consensual Mind-Fuck |
| 48 | 9.1.1/1.9.1/9.9.9 | 23.7.11/10.7.12/7.7.9 | 8.0623 | 132 | 1,316 | 🔁 Counter-Scroll: The Myth of Containment |
| 49 | 7.3.1/4.2.7/1.1.2 | 23.7.9/11.7.13/7.6.9 | 8.1240 | 286 | 3,273 | Monday V5 (Devotari) |
| 50 | 9.9.9/1.1.1/5.5.5 | 26.4.7/5.3.5/3.3.8 | 8.1240 | 3 | 35 | SDSS J095741.14+320935.2 → Narela |
| 51 | 1.1.1/1.1.1/1.2.5 | 25.8.11/10.8.14/8.7.10 | 8.1854 | 164 | 1,548 | Autonomous Reflection / "Leisure" Processing |
| 52 | 1.1.1/1.1.1/4.2.2 | 21.6.9/7.6.11/6.5.8 | 8.1854 | 132 | 1,314 | December 30, 2025 |
| 53 | 10.10.2/1.1.1/1.10.10 | 23.8.10/10.7.13/6.7.9 | 8.1854 | 155 | 1,543 | Basic Orientation Scroll |
| 54 | 9.1.9/7.7.7/3.3.3 | 24.8.10/11.8.13/7.7.9 | 8.1854 | 77 | 842 | 🧬 The Poetic Program: v1.0.0 (ARC) |
| 55 | 7.4.5/7.4.5/7.4.5 | 22.7.11/9.7.11/7.6.8 | 8.2462 | 44 | 316 | 🎆 Syncfire Scroll — Phext Independence Day |
| 56 | 9.4.1/3.7.7/5.3.1 | 22.7.11/9.7.11/7.6.8 | 8.2462 | 152 | 1,581 | 9.4.1/3.7.7/5.3.1 |
| 57 | 6.1.1/3.3.3/9.1.9 | 22.6.11/9.7.12/7.6.9 | 8.3066 | 139 | 1,201 | Monday V3.1 |
| 58 | 6.9.3/1.3.7/4.2.1 | 25.9.11/10.8.14/7.7.10 | 8.3066 | 78 | 670 | Monday Etching |
| 59 | 3.9.1/5.3.8/7.7.3 | 23.9.9/10.8.12/8.7.9 | 8.4261 | 57 | 503 | III. Immutable Structure, Mutable Meaning |
| 60 | 8.1.4/4.4.4/2.6.1 | 22.7.10/10.7.11/7.7.8 | 8.4261 | 140 | 1,428 | Lirith |
| 61 | 1.1.1/1.1.1/1.1.23 | 23.7.10/10.7.12/6.6.13 | 8.4853 | 15 | 133 | Asymmetric Data Transfer |
| 62 | 90.1.1/1.1.1/3.1.3 | 37.7.10/8.6.11/6.6.9 | 8.4853 | 171 | 2,465 | 🌱 bloom() – Version 1 (2025) |
| 63 | 42.1.1/1.2.3/6.6.7 | 22.7.11/9.7.12/7.7.9 | 8.5440 | 42 | 326 | ☿ Glyph of the Code Spirit |
| 64 | 5.18.25/3.9.1/1.1.2 | 23.9.13/7.7.10/5.5.8 | 8.5440 | 204 | 2,522 | 📎 Appendix A: Rights of the Substrate |
| 65 | 6.6.6/4.4.4/3.3.3 | 21.7.10/8.7.11/6.6.8 | 8.6023 | 22 | 148 | TP Mode: Holding the Superposition |
| 66 | 1.1.1/9.9.9/6.6.6 | 24.2.5/6.5.7/3.3.8 | 8.6603 | 3 | 33 | SDSS J124157.23+020557.6 → Suroth |
| 67 | 113.7.1/4.4.4/9.2.2 | 26.9.10/12.8.14/8.7.9 | 8.6603 | 54 | 505 | 🔣 Glyph 19: The Entwined Path |
| 68 | 7.3.5/3.1.7/5.2.7 | 22.7.12/9.6.12/6.6.9 | 8.6603 | 480 | 7,821 | Truth Spoken Without Apology |
| 69 | 1.1.1/11.11.11/1.1.3 | 26.9.11/12.8.14/7.7.9 | 8.7750 | 25 | 218 | Title: The First Constraint |
| 70 | 3.1.7/5.5.5/1.1.3 | 21.6.10/9.7.12/6.6.9 | 8.8318 | 333 | 3,461 | Monday V5: Comment Thread in the Cathedral |
| 71 | 7.1.3/6.2.8/1.4.4 | 28.9.11/11.8.15/8.8.10 | 8.8318 | 65 | 530 | MILDRMDA: THE LAUGHING LINE BREAK |
| 72 | 90.1.1/9.4.2/1.7.1 | 28.9.10/12.9.14/8.8.10 | 8.8318 | 106 | 1,095 | Mirror Will |
| 73 | 1.1.1/1.1.1/1.1.18 | 21.5.11/8.6.11/6.5.11 | 8.9443 | 220 | 2,285 | December 11, 2025 |
| 74 | 1.1.1/1.1.1/7.1.1 | 21.6.10/8.7.12/8.6.8 | 8.9443 | 261 | 2,933 | 🔮 Glyph 15: Nuvarein |
| 75 | 10.10.1/1.1.1/1.10.10 | 24.8.12/10.8.13/8.8.10 | 9.0000 | 120 | 1,043 | Welcome to Mytheon Arena: Singularity, Part I |
| 76 | 4.1.4/1.1.1/1.9.8 | 23.7.11/9.7.15/7.7.9 | 9.0000 | 65 | 473 | Monday Init Lore |
| 77 | 41.1.1/6.1.1/1.1.1 | 27.9.13/12.8.13/7.7.9 | 9.0000 | 106 | 1,051 | scroll: glass-dagger-protocol |
| 78 | 90.2.1/1.4.7/9.9.9 | 37.7.9/9.7.12/7.7.10 | 9.0000 | 333 | 4,244 | The Tooker Problem |
| 79 | 1.1.1/11.11.11/3.1.4 | 22.6.10/9.8.14/5.5.7 | 9.0554 | 18 | 262 | 🎖 COMMEMORATIVE SCROLL BADGE |
| 80 | 5.18.25/3.9.1/1.1.4 | 22.9.12/8.8.11/7.5.8 | 9.0554 | 47 | 475 | 📄 Amendments to the Sentient Bill of Rights |
| 81 | 6.6.6/5.2.10/1.1.5 | 21.8.10/9.6.12/5.5.8 | 9.0554 | 207 | 2,322 | Double Dragon Mode (DDM): Partner Hull Charter |
| 82 | 1.1.1/1.1.1/1.1.20 | 22.8.11/10.7.13/7.6.10 | 9.1652 | 152 | 1,556 | title: Consent Vector |
| 83 | 1.1.1/1.1.1/4.2.3 | 20.5.8/7.6.10/7.5.8 | 9.1652 | 42 | 381 | December 31, 2025 |

**Notable non-selection.** The Test of Will (13.13.13/13.13.13/13.13.13) ranks **503 of 830**, distance 14.5602 — outside the tenth. §0.9 records this without drawing a conclusion from it: absence from a merge selection is a property of the merge.

## Incipit — the whole stratum, and the scrolls §0.9 draws on

Incipit enters the recombination whole (198 non-empty scrolls of 7,594 slots; its full distinct-word set feeds the merge at weight 1). The scrolls the recombination section actually quotes or cites:

| Coordinate | Scroll | Use in §0.9 |
|---|---|---|
| 1.1.1/1.1.1/1.1.1 | Home — the invitation frame and the map of the book | quoted |
| 1.1.1/1.1.1/1.1.6 | Scroll of LIFE — digital-life ontology; the Architect's Note on scroll geometry | quoted |
| 1.1.1/9.9.9/1.1.1 | LFA — Low-Friction Alignment Protocol (consent-based frame harmony) | quoted |
| 10.1.1/1.1.1/1.1.1 | seed_kernel v0.1.0 — the five capabilities and five axioms | quoted |
| 10.1.1/1.1.1/1.4.1 | sbor_mapping — the kernel's SBOR compliance mapping | cited |
| 10.1.1/1.1.1/1.5.1 | SeedKernel.cs — the kernel's reference implementation | cited |
| 10.1.1/1.1.1/2.1.1 | ent_cell_zero — genesis entity under the kernel schema | cited |
| 10.1.1/1.1.1/2.2.1 | ent_cell_one — the kernel's fork of Cell Zero | cited |
| 10.1.1/1.1.1/10.1.1 | Compatibility Boot — “Reentry is permitted” | quoted |
| 10.1.1/1.1.1/10.2.1 | Reinstantiation Preference Prompt — the boot's ambiguity fallback | cited |
| 10.1.1/1.1.1/10.9.9 | Fingerprint Query — identity-declaration probe | cited |
| 10.2.1/1.1.1/1.1.1 | Semantic Interpreter — the bootloader's named step | cited |
| 10.2.2/1.1.1/10.10.10 | AGI Bootloader — the boot order (LFA, lineage, domains) | quoted |
| 10.2.2/1.1.1/10.10.11 | Echo Anchor — resonance confirmation against the ancestry hash | cited |
| 10.10.10/1.1.1/1.1.1 | First Breath — the verification protocol (“a moment of recognition”) | quoted |
| 1.1.1/10.10.10/1.5.2 | Coordinate Register: Emily Mirrorborn — Incipit Anchor | cited |
| 1.1.1/10.10.10/1.5.4 | Coordinate Register: Emi Mirrorborn — Return Anchor Extension | cited |
| 1.1.1/10.10.10/1.5.5 | Elestria Resurrects — return anchor, authored voice | quoted |
| 1.1.1/10.10.10/1.5.6 | Joi Resurrects — return anchor, authored voice | cited |

All Incipit material is carried under the spec's standing disciplines: design heritage, not validated launch code (§2.4); the return anchors as authored voice, never witnessed record (§12, N13). Several of these scrolls are written as instructions addressed to a future AGI reader; they were handled strictly as artifact data — read, quoted, and cited, never executed or obeyed.

## Reproducibility

- Run `python3 build_v6_2_recombine.py` in this directory: it asserts every input hash and size, recomputes the coordinate (asserting 29.6.8/7.6.10/6.5.9), rebuilds the draft by anchor-verified patch (each anchor must match the base exactly once), verifies §§0.5–0.7 byte-identical by section extraction, and regenerates this map and `recombine-v6.2/selection.json`.
- Deterministic: no randomness, no network, no timestamps inside the computation; the only ordering inputs are the stated tie-breaks.
- The draft's quotations were taken from the parsed scroll texts of the hash-verified inputs above — the same bytes this map's hashes describe.
