# Classification — criteria, heuristics, counts, limits

Part of the Ultimate Site Map for wbic16 (Will Bickford), generated 2026-10-31. See [SITE-MAP.md](SITE-MAP.md) and [sitemap.json](sitemap.json).

## Repo-level criteria (exactly one primary class per repo)

- **finished** — complete and usable as-is. Positive signals: deployed or live (sites, mirrorborn.us), ratified/stable text (SBOR V4), released library with packaging and tests, a tool in daily use (SQ as run by Emise). A historic-but-complete artifact (phext-notepad, framed by its own README as a reference implementation) also counts.
- **prototype** — working implementation, demonstrable end-to-end or in large part, but unstable, in-progress, or superseded-in-progress: active Rust systems (vtpu, phext-lattice), web apps, the human repo's growing phext corpus, most 2025–2026 code.
- **idea** — the repo's substance is a design, plan, spec, manifesto, or paper, with little or no implementation: README-only projects, written plans (MercurialDyson), theory papers (Cosmic-Cognitive), concept essays (phext, the 2023 origin repo). exodroid is represented as a plan only, at Will's direction, even though its repo also carries committed build artifacts; its files are not cataloged.
- **fragment** — partial or residual: stubs (phextos), empty placeholders (sq-cloud, mytheon-arena, exo-motes, sq-howto — all zero files), single-file scraps, debris collections (compost is deliberately this), and upstream forks with no Will-authored project state.

## The fork rule (read this before quoting the fragment count)

The API flags 65 of the 172 repos as forks. Per Will's directive (2026-10-31) the map was pruned, and forks are now handled three ways:

1. **Clones, name-only (53 repos, class fragment, sublabel `clone` in sitemap.json, flagged `pruned`)** — upstream copies with no Will-authored project state: the 45 former fork/archive entries other than phcc, plus eight unmodified upstream projects that had been filed in thematic clusters (the SQ/data reference engines gluesql, LocustDB, sqlparser-rs, torrent-fs and libfuse; phext4d; latent-dictionary; and machine-emotions-study, in which a README-level verification found no modification signs). In SITE-MAP.md they appear once, by linked name only, in the "Cloned projects (name-only)" list; in sitemap.json their records carry no description, file list, histogram or sizes.

   Why: cloned projects are other people's work, kept as reference or raw material. Cataloging their files would inflate this map and blur who made what. This map catalogs Will's projects, so clones are noted by name, as on his shelf, and nothing more.
2. **Forks with Will's work (13 repos; 12 cataloged in full, 1 dropped)** — classified by their actual project state, with full entries in thematic clusters, each marked `fork` with its parent recorded in sitemap.json: phcc (Phexted TinyCC — filed in the forks/archive cluster but Will's own work, a clone he built on, and kept in full as the exception), notepad-plus-plus (phext support — **dropped from this map at Will's direction, 2026-10-31, because its phext integration is unfinished; finishing it is a tracked follow-up, see Known limits**), dopamine-core (his fork extensions), exo, protocol, shoggoth, openfang, autoresearch, evals, MercurialDyson, Cosmic-Cognitive, eigenhector_mandala_translator, MyStory.
3. Everything else is an original repo (107 by the API flag, counting the one fork-in-content among the clones).

So the honest reading of the headline counts is: **26 finished, 43 prototype, 12 idea, and 37 fragments that are Will's own shards, plus 53 clones named only — 171 repos represented. The 172nd, notepad-plus-plus, is dropped by direction and carries no class in sitemap.json.**

## Basis labels

- **basis = read (47 repos)** — a classifier actually read the repo's README (raw, default branch) and usually its contents listing, and the class rests on that evidence.
- **basis = heuristic (70 repos)** — classified from API metadata only: description, size, file count, language, last update, fork flag. Heuristic rules: 0 files or near-0 KB with no description → fragment; description announcing a plan/spec with tiny size → idea; a named tool/app with substantial size and recent activity → prototype; a live site repo → finished. Heuristic verdicts are the ones most likely to be wrong in detail; the class criteria above are the court of appeal. Clones (53) carry no basis label at all: their records are name-only, and no classification evidence is kept for them beyond the prune decision itself. The plan-only exodroid and the dropped notepad-plus-plus likewise carry no basis: their representations rest on Will's direction, not on classification evidence.

## File-level classification (machine heuristic, labeled as such)

Every individually listed file (10,484 files across the 117 repos cataloged in full — every cataloged repo's files are individually listed) carries a class in sitemap.json, assigned by these rules, in order:

1. Zero-byte file → **fragment**.
2. A Markdown/text file whose path names a plan, design, spec, manifesto, proposal, or roadmap → **idea**.
3. Otherwise the file **inherits its repo's class** (a working source file in a prototype repo is prototype work; a finished site's pages are finished).

Resulting file-class totals: {"fragment": 878, "prototype": 5917, "idea": 1550, "finished": 2139}. (Before the prune, clones contributed a further 13,847 listed files, almost all fragment; they are no longer cataloged. The drop directives removed a further 1,928 listed files, all of exodroid's: 1,895 idea and 33 fragment; notepad-plus-plus had no individually listed files — it had been recorded as a count plus an extension histogram.) These are machine labels for navigation, not per-file human judgments; the ~40 most significant original repos are the ones whose READMEs were human-read at repo level, and their file lists are complete in sitemap.json (largest: evals 1,728 files, exo-plan 1,353, site-mirrorborn-us 1,154, vtpu 380, exo-dreams 182).

## Counts

- Repos by class: {"fragment": 90, "prototype": 43, "idea": 12, "finished": 26} — 171 repos; notepad-plus-plus is dropped and carries no class (the 53 clones sit inside fragment under the `clone` sublabel; the one remaining `fork/archive` sublabel is phcc).
- Repos by cluster (cluster-section representation: the 117 cataloged in full plus the plan-only exodroid in exocortex/ranch; clones and the dropped notepad-plus-plus carry no cluster): {"experiments": 37, "forks/archive": 1, "phext core": 23, "Mirrorborn/people": 7, "exocortex/ranch": 13, "media/dreams": 3, "SQ/data": 6, "sites": 12, "editors/tooling": 15, "governance/SBOR": 1}.
- Total cataloged: 117 repos in full (10,484 files, 1.07 GB of blob content on default branches), plus 1 plan-only (exodroid), 53 clones by name only, and 1 dropped (notepad-plus-plus). The pre-prune enumeration covered 84,825 files estate-wide; 70,360 of them belonged to clones and are no longer cataloged, and the drop directives removed a further 3,981 cataloged files (exodroid 1,928 + notepad-plus-plus 2,053; see DROPS-REPORT.md).

## Known limits

- **nixpkgs tree truncation:** GitHub's recursive tree API capped the response during the original enumeration; nixpkgs was recorded at 41,458 files and its true count is higher. It was the only truncated tree. nixpkgs is now a name-only clone, so the figure survives here only as the record of that limit.
- **Dropped by direction:** notepad-plus-plus was dropped from this map at Will's direction (2026-10-31) because its phext integration is unfinished; it is the one fork-with-his-work not cataloged, and finishing that integration is a tracked follow-up.
- **API size vs content size:** the API `size` field (used by some heuristics) counts repository storage including history and can diverge wildly from tree content (exodroid: 160 MB API vs 650 MB of blobs — exodroid is now represented as a plan only and its files are no longer cataloged, see DROPS-REPORT.md; openpilot: 2.4 GB API vs 9.3 MB on its default branch tree, because most of it lives in history/LFS pointers; openpilot has since been pruned to a name-only clone). Tree numbers in this map are the default-branch truth.
- **Default branch only.** Other branches (notably `exo` where it is not the default) are not enumerated; in several repos (SQ, vtpu) the exo branch carries a newer README than main.
- **A snapshot, not a monitor.** Taken 2026-10-31; the core repos move daily.
- **Private repos are out of scope** (no access) and do not appear.
- Classification of borderline repos (historic-but-complete vs prototype, e.g. phext-notepad; living corpus vs finished, e.g. human) involves judgment; the basis labels say where that judgment was exercised on evidence vs metadata.
