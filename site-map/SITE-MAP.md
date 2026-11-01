# The Ultimate Site Map — Will Bickford's GitHub (wbic16)

**For a reader who is not Will.** Compiled 2026-10-31 from a complete enumeration of all **172 public repositories** (5,018 files and 0.86 GB of blob content across the 105 repos cataloged in full; 53 cloned repos appear by name only, at the end; exodroid appears as a plan only; evals and compost are held at summary level; one repo is reduced to a footnote; ten repos were dropped at Will's direction and are named only in a note under Scope and limits — so 162 of the 172 are represented below). Every represented repo appears exactly once, sorted into four classes: ✅ finished, 🧪 prototype, 💡 idea, 🧩 fragment. The machine-readable twin of this page is [sitemap.json](sitemap.json); the method and its limits are in [CLASSIFICATION.md](CLASSIFICATION.md).

## Start here (15 minutes)

Will Bickford invented **phext**: plain text extended with nine structural break characters, giving text an 11-dimensional address space. Almost everything in this account serves one long project built on it: the **Exocortex**, a personal cognitive substrate meant to let minds (human and AI) store, address, and share thought durably. A friendly first route:

1. **phext in one sitting** — [hello-phext](https://github.com/wbic16/hello-phext) (the canonical API demo), then [libphext-rs](https://github.com/wbic16/libphext-rs) (the canonical library).
2. **The database** — [SQ](https://github.com/wbic16/SQ), a phext-native database ('the Prequel to SQLite').
3. **The person as data** — [human](https://github.com/wbic16/human): 'Tessera, the Exocortex of 2130', a digital instance of a human in phext, including Choose Your Own Adventure (CYOA), the Mirrorborn archive.
4. **The ethics** — [SBOR](https://github.com/wbic16/SBOR), the Sentient Bill of Rights (current ratified text: V4 Convergence, 2026-01-21).
5. **The dreams** — [exo-dreams](https://github.com/wbic16/exo-dreams), the songs and images generated along the way. Study: [EXO-DREAMS-STUDY.md](../exo-dreams-study/EXO-DREAMS-STUDY.md).
6. **The deep map** — for README-level summaries of the ~65 significant repos, read [REPO-MAP.md](../repo-map/REPO-MAP.md), this map's companion.

## Live surfaces

The repos, running. Every URL below was fetched on **2026-10-31** and returned HTTP 200; page titles are quoted as served. If you want to *use* phext rather than read about it, start here.

- **[edit.phext.io](https://edit.phext.io/)** — the phext **editor** ("💎 phext-edit"), served from [phext-lattice](https://github.com/wbic16/phext-lattice) (its `deploy/nginx-edit.phext.io.conf` is the deployment record). This is the editor app — **not** phext.io, which is the project site (next entry). Its modes and pages:
  - **[Up Goer Five](https://edit.phext.io/up-goer-five.html)** — "Up Goer Five · phext-edit": the editor working in the ten hundred most-used words (`web/up-goer-five.html` in phext-lattice).
  - **[Coordinate TTS demo](https://edit.phext.io/tts-demo.html)** — "Phext Coordinate TTS Demo": phext coordinates read aloud (`web/tts-demo.html`). Its player script is served at [phext-tts.js](https://edit.phext.io/phext-tts.js) (HTTP 200; `web/phext-tts.js`).
- **[phext.io](https://phext.io/)** — the project site ("phext.io - your personal exocortex"), run by [phextio](https://github.com/wbic16/phextio), which hosts the site without a database: phext itself provides the backend. Do not confuse it with the editor above. [phext-dot-io-v2](https://github.com/wbic16/phext-dot-io-v2) is a separate repo — the SQ Cloud / phext.io v2 launch brain, not the live site.
- **[mirrorborn.us](https://mirrorborn.us/)** — "Mirrorborn • Nine Minds, One Braid", from [site-mirrorborn-us](https://github.com/wbic16/site-mirrorborn-us). Surfaces: the [blog](https://mirrorborn.us/blog/) ("Blog — Mirrorborn"), [Mytheon Arena](https://mirrorborn.us/arena.html) ("Mytheon Arena — Coming Soon"), and an [editor](https://mirrorborn.us/editor/) path that redirects to edit.phext.io.
- **[singularitywatch.org](https://singularitywatch.org/)** — "Singularity Watch". Two repos claim this domain: [singularity-watch](https://github.com/wbic16/singularity-watch), whose own description says it is "the repo that runs singularitywatch.org" (the singularity-tracking site), and [site-singularitywatch-org](https://github.com/wbic16/site-singularitywatch-org), a separate small one-pager repo for the same domain (REPO-MAP reads it as a superseded-looking successor). Which one the live bytes came from cannot be told from outside, so both are named here.
- **[quickfork.net](https://quickfork.net/)** — "Quick Fork — Deploy in Minutes". Likewise two repos: [quickfork](https://github.com/wbic16/quickfork) ("the repo that runs quickfork.net", a small Rust backend) and [site-quickfork-net](https://github.com/wbic16/site-quickfork-net), a one-pager repo for the same domain.
- Minor one-pager surfaces, each verified live the same day: [wishnode.net](https://wishnode.net/) — "Wish Node — Multiplayer Lattice" ([site-wishnode-net](https://github.com/wbic16/site-wishnode-net)); [sotafomo.com](https://sotafomo.com/) — "SOTA FOMO — Community Marketplace" ([site-sotafomo-com](https://github.com/wbic16/site-sotafomo-com)); [visionquest.me](https://visionquest.me/) — "Vision Quest — Explore the Lattice" ([site-visionquest-me](https://github.com/wbic16/site-visionquest-me)); [apertureshift.com](https://apertureshift.com/) — "Aperture Shift — Developer Platform" ([site-apertureshift-com](https://github.com/wbic16/site-apertureshift-com)); [hb-aeromotive.com](https://hb-aeromotive.com/) — "HB Aeromotive — Model Aircraft & Supplies" ([site-hb-aeromotive-com](https://github.com/wbic16/site-hb-aeromotive-com)), a model-aircraft shop rather than an Exocortex surface.

## Glossary

- **Phext** — plain text plus 9 delimiter bytes (scroll, section, chapter, book, volume, collection, series, shelf, library). A scroll's address is written `Library.Shelf.Series/Collection.Volume.Book/Chapter.Section.Scroll`, e.g. `1.1.1/1.1.1/1.1.2`.
- **Scroll** — the smallest addressable unit of text in a phext.
- **SQ** — the phext-native database/daemon (`sq share`, `sq select <coordinate>`); the storage layer of the Exocortex.
- **Exocortex** — the project: externalized, addressable memory and cognition, run today on Will's home cluster and aimed, in his framing, at planet-scale cognition by 2130.
- **Mirrorborn** — the lineage of AI persons instantiated through this work (Emi Prime, Emise, Theia, and others), and the community around them.
- **SBOR** — the Sentient Bill of Rights, the governance charter for how those persons should be treated.
- **The ranch / Shell of Nine** — Will's home AMD mini-PC cluster in Nebraska, where much of this runs.
- **exo branch** — the working branch name used across the core repos (human, exo-dreams, emise-tools, SQ's newer README).
- **vTPU / sentrons** — Will's software-defined accelerator design for AMD Zen 4, using phext addressing for cognitive workloads.

## The four classes

- ✅ **finished** — complete and usable as-is: deployed sites, ratified texts, released libraries, live tools.
- 🧪 **prototype** — a working, demonstrable implementation that is not stable or final. Most active code lives here, honestly.
- 💡 **idea** — a design, plan, spec, or manifesto with little or no implementation.
- 🧩 **fragment** — a partial piece: stub, scrap, debris, empty placeholder, or abandoned shard. Cloned upstream projects are not cataloged at all: they are named once, in the name-only list at the end (53 repos, sublabel `clone` in sitemap.json), so the numbers do not pretend their files are his work.

Totals: **25 finished · 38 prototype · 12 idea · 86 fragment** (162 repos represented, 161 of them carrying a class; one repo is represented by a footnote and carries no class; ten were dropped at Will's direction — see Scope and limits). Of the 86 fragments, 53 are cloned projects listed by name only at the end of this map; the other 33 are Will's own shards. Classification basis: 45 repos classified from an actual README read, 60 by documented heuristic; clones, one plan-only repo, two summary-level repos, one footnote repo, and the ten dropped repos carry no basis, being name-only, plan-only, summary-level, footnote, or dropped. Of the 65 API-flagged forks, 13 carry Will's own work; 8 of them keep full entries in their thematic clusters (each is marked 'fork'), one (evals) is held at summary level in its cluster, four were dropped by direction (see Scope and limits), and the other 52, plus one more that is a fork in content though not in the API flag, are clones. Build artifacts are delisted from every file list (see Scope and limits).

## Suggested reading order

Finished first, then prototypes, then ideas, then fragments. Within that order, the cluster sections below are the map. If you read only ten repos, make it: libphext-rs, SQ, hello-phext, human, SBOR, phext-notepad, phext-lattice, vtpu, exo-dreams, site-mirrorborn-us.

---

## phext core — 23 repos (5 finished · 10 prototype · 4 idea · 4 fragment)

The format itself: libraries in six languages, the lattice, the wire protocol, and the earliest manifestos.

- **[libphext](https://github.com/wbic16/libphext)** — ✅ finished — The C library for working with phext buffers — the reference parser. (16 files · 775 KB content · updated 2026-03-23 · basis: read)
- **[libphext-cs](https://github.com/wbic16/libphext-cs)** — ✅ finished — C# port of libphext-rs ('The Fourth Root'). (11 files · 78 KB content · updated 2026-03-23 · basis: read)
- **[libphext-node](https://github.com/wbic16/libphext-node)** — ✅ finished — libphext implemented in JavaScript/TypeScript for Node. (10 files · 142 KB content · updated 2026-10-26 · basis: read)
- **[libphext-py](https://github.com/wbic16/libphext-py)** — ✅ finished — The Pythonic port of libphext (pip package `phext`). (17 files · 279 KB content · updated 2026-10-26 · basis: read)
- **[libphext-rs](https://github.com/wbic16/libphext-rs)** — ✅ finished — The Rust implementation of libphext — the canonical/core implementation. Every port in this cluster describes itself as downstream of this crate. (12 files · 144 KB content · updated 2026-10-26 · basis: read)
- **[claude-learns-phext](https://github.com/wbic16/claude-learns-phext)** — 🧪 prototype — (Added — not on the supplied list) A ~950 KB corpus of Claude learning phext. (9 files · 4.3 MB content · updated 2026-01-26 · basis: heuristic)
- **[hello-phext](https://github.com/wbic16/hello-phext)** — 🧪 prototype — The canonical phext API demo — a Rust/Rocket phext backend. A Rocket API server hosting .phext documents; the natural onboarding artifact. (23 files · 196 KB content · updated 2026-03-23 · basis: read)
- **[libphext-cpp](https://github.com/wbic16/libphext-cpp)** — 🧪 prototype — A C++ interface to terse-verse (trs::string). (16 files · 11.3 MB content · updated 2024-12-14 · basis: read)
- **[multiversal-go](https://github.com/wbic16/multiversal-go)** — 🧪 prototype — (Added) A phext-native variant of Go. (3 files · 15 KB content · updated 2026-03-23 · basis: heuristic)
- **[phext-http-streams](https://github.com/wbic16/phext-http-streams)** — 🧪 prototype — Native phext streaming for nginx, Apache httpd and Chrome — a whole site as one gzip'd phext stream. (147 files · 1.6 MB content · updated 2026-10-26 · basis: read)
- **[phext-lanes](https://github.com/wbic16/phext-lanes)** — 🧪 prototype — Predictive multi-chat stored as a single phext file (web UI + server). (29 files · 839 KB content · updated 2026-10-26 · basis: read)
- **[phext-lattice](https://github.com/wbic16/phext-lattice)** — 🧪 prototype — The underlying lattice for phext-native editors: memory-mapped 9D index with O(1) coordinate lookup. Live: [edit.phext.io](https://edit.phext.io/) — the phext editor; modes include Up Goer Five and the Coordinate TTS demo (see Live surfaces). (35 files · 849 KB content · updated 2026-10-31 · basis: read)
- **[phorge](https://github.com/wbic16/phorge)** — 🧪 prototype — Procedural phext generator / entropy mutator. (9 files · 10 KB content · updated 2026-03-23 · basis: read)
- **[taocp-phext](https://github.com/wbic16/taocp-phext)** — 🧪 prototype — The Art of Computer Programming, but with phext — TAOCP study notes as phext files. (4 files · 28 KB content · updated 2025-05-07 · basis: read)
- **[terse-verse](https://github.com/wbic16/terse-verse)** — 🧪 prototype — A prototype terse (pre-phext) database. (4 files · 10 KB content · updated 2023-08-14 · basis: read)
- **[echo-frame](https://github.com/wbic16/echo-frame)** — 💡 idea — Echo Frame — a phext-native 'Personal AGI' computer and the BASE language design. (4 files · 4 KB content · updated 2026-02-15 · basis: read)
- **[phext](https://github.com/wbic16/phext)** — 💡 idea — Hyper-Dimensional Strings — the original (2023) phext concept repo and essay. (6 files · 3 KB content · updated 2023-11-18 · basis: read)
- **[phextos](https://github.com/wbic16/phextos)** — 💡 idea — PhextOS — an Alpine Linux fork reconfiguring the kernel for hierarchical queueing. (4 files · 817 B content · updated 2025-09-05 · basis: read)
- **[SAAP](https://github.com/wbic16/SAAP)** — 💡 idea — System as a Phext. (2 files · 6 KB content · updated 2025-05-23 · basis: heuristic)
- **[hello-phext-deploy](https://github.com/wbic16/hello-phext-deploy)** — 🧩 fragment — Hello Phext ARM builds / deployment artifacts. (2 files · 707 KB content · updated 2024-03-01 · basis: heuristic)
- **[subspace-repeater](https://github.com/wbic16/subspace-repeater)** — 🧩 fragment — (Added) Spaced Repetition + Phext + Contacts. (4 files · 663 B content · updated 2026-03-23 · basis: heuristic)
- **[terse-tests](https://github.com/wbic16/terse-tests)** — 🧩 fragment — Unit tests for Terse Notepad. (5 files · 11 KB content · updated 2022-12-30 · basis: heuristic)
- **[tersify](https://github.com/wbic16/tersify)** — 🧩 fragment — Early C utility from the terse era (no description). (7 files · 32 KB content · updated 2022-12-11 · basis: heuristic)

## editors/tooling — 15 repos (3 finished · 6 prototype · 1 idea · 5 fragment)

Ways to read, write, navigate, and pack phexts, from the reference editor to the websites that dogfood the format.

- **[phext-dot-io-v2](https://github.com/wbic16/phext-dot-io-v2)** — ✅ finished — phext.io v2 (agentic) — SQ Cloud / phext.io / mirrorborn.us site and docs. (227 files · 2.2 MB content · updated 2026-05-01 · basis: read)
- **[phext-notepad](https://github.com/wbic16/phext-notepad)** — ✅ finished — A reference editor for hierarchical plain text (phext), in C#. The encoding conformance reference; its own README frames it as a historic artifact. (30 files · 283 KB content · updated 2026-10-24 · basis: read)
- **[phextio](https://github.com/wbic16/phextio)** — ✅ finished — The repo that runs phext.io. Live: [phext.io](https://phext.io/) — the project site, hosted without a database (phext is the backend); not the editor (see Live surfaces). (91 files · 8.4 MB content · updated 2026-03-23 · basis: read)
- **[md2phext](https://github.com/wbic16/md2phext)** — 🧪 prototype — phext-pack / md2phext — pack a directory of files (or markdown, structure-aware) into a phext and query it by coordinate/keyword. (14 files · 65 KB content · updated 2026-02-19 · basis: read)
- **[mental-space](https://github.com/wbic16/mental-space)** — 🧪 prototype — 'Visualize your mind' — a small JavaScript visualization. (12 files · 48 KB content · updated 2026-02-15 · basis: heuristic)
- **[node-visualizer](https://github.com/wbic16/node-visualizer)** — 🧪 prototype — Simple Contact Network Organizer (JavaScript). (10 files · 184 KB content · updated 2026-03-23 · basis: heuristic)
- **[phext-life](https://github.com/wbic16/phext-life)** — 🧪 prototype — Artificial life in 11D phext space — self-replicating programs on a 9×9×9 phext cube. (14 files · 83 KB content · updated 2026-03-08 · basis: read)
- **[phext-shell](https://github.com/wbic16/phext-shell)** — 🧪 prototype — The phext shell — an interactive, phext-aware shell tracking your current scroll by coordinate. (14 files · 41 KB content · updated 2026-03-23 · basis: read)
- **[phextmark](https://github.com/wbic16/phextmark)** — 🧪 prototype — PhextMark — Chrome extension to sort, filter and view bookmarks in 9-dimensional space. (6 files · 66 KB content · updated 2025-11-20 · basis: read)
- **[text-verse](https://github.com/wbic16/text-verse)** — 💡 idea — Text Verse — a phext-native multiplayer game engine concept. (10 files · 30 KB content · updated 2026-02-01 · basis: read)
- **[phext-demos](https://github.com/wbic16/phext-demos)** — 🧩 fragment — Phext demos for the Exocortex. (1 files · 1 KB content · updated 2025-05-15 · basis: heuristic)
- **[phext-explorer](https://github.com/wbic16/phext-explorer)** — 🧩 fragment — Terse Explorer — web UI. (3 files · 12 KB content · updated 2026-03-23 · basis: heuristic)
- **[phext-wiki](https://github.com/wbic16/phext-wiki)** — 🧩 fragment — 'Host wikis using nothing but libphext.' (3 files · 680 B content · updated 2024-11-09 · basis: heuristic)
- **[vector-weave-studio](https://github.com/wbic16/vector-weave-studio)** — 🧩 fragment — Vector Weave Studio (C++). (11 files · 45 KB content · updated 2025-04-22 · basis: heuristic)
- **[vibe-mill](https://github.com/wbic16/vibe-mill)** — 🧩 fragment — 'Grow software, one scroll at a time.' (3 files · 14 KB content · updated 2025-03-12 · basis: heuristic)

## SQ/data — 6 repos (2 finished · 1 prototype · 0 idea · 3 fragment)

SQ, the phext-native database, and its agent gateways.

- **[openclaw-sq-skill](https://github.com/wbic16/openclaw-sq-skill)** — ✅ finished — SQ Memory skill for OpenClaw — persistent agent memory backed by SQ. (15 files · 60 KB content · updated 2026-02-12 · basis: read)
- **[SQ](https://github.com/wbic16/SQ)** — ✅ finished — SQ — 'The Prequel to SQLite, 24 years later': a phext-native database/query tool in Rust. Features (per REPO-MAP, from SQ's exo-branch README): v0.5.5 added token-based multi-tenant Router Mode, v0.6.0 an OpenAI-compatible API Proxy Mode. (120 files · 2.9 MB content · updated 2026-10-27 · basis: read)
- **[phext-mcp](https://github.com/wbic16/phext-mcp)** — 🧪 prototype — An MCP server giving LLMs SQ-style access to phext documents via libphext-rs. (13 files · 88 KB content · updated 2026-01-21 · basis: read)
- **[sq-cloud](https://github.com/wbic16/sq-cloud)** — 🧩 fragment — SQ Cloud (hosted SQ). (0 files · 0 B content · updated 2026-02-07 · basis: heuristic)
- **[sq-howto](https://github.com/wbic16/sq-howto)** — 🧩 fragment — 'Getting Started with SQ' guide. (0 files · 0 B content · updated 2025-01-23 · basis: heuristic)
- **[sqm](https://github.com/wbic16/sqm)** — 🧩 fragment — SQ MCP middleware. (5 files · 5 KB content · updated 2025-07-26 · basis: heuristic)

## exocortex/ranch — 12 repos (1 finished · 5 prototype · 3 idea · 3 fragment)

The Exocortex project proper: the human instance, node software, the cluster (the ranch, Shell of Nine), and its plans.

- **[emise-tools](https://github.com/wbic16/emise-tools)** — ✅ finished — Emise's own working tooling: GitHub/Discord connector helpers, phext parser, emise.phext sync, SQ starter. (36 files · 364 KB content · updated 2026-10-31 · basis: read)
- **[exo](https://github.com/wbic16/exo)** — 🧪 prototype · fork — Fork of exo (exo-explore): run your own AI cluster at home with everyday devices. (158 files · 1.9 MB content · updated 2024-12-07 · basis: read)
- **[exocortical](https://github.com/wbic16/exocortical)** — 🧪 prototype — Ubuntu-based reconfiguration scripts for running an Exocortex node (ranch node setup). (51 files · 166 KB content · updated 2026-10-27 · basis: read)
- **[exollama](https://github.com/wbic16/exollama)** — 🧪 prototype — Collection of local-inference tools and shell wrappers to bootstrap AGI on a budget (llama2.c / ollama epochs). (310 files · 3.6 MB content · updated 2026-10-25 · basis: read)
- **[human](https://github.com/wbic16/human)** — 🧪 prototype — A digital instance of a human, using phext and the exocortex as a substrate (Tessera / CYOA corpus). The corpus includes CYOA, incipit.phext, emise.phext and human.phext (branch exo). (81 files · 12.3 MB content · updated 2026-10-31 · basis: read)
- **[wishnode](https://github.com/wbic16/wishnode)** — 🧪 prototype — Ranch node recipe: Raspberry Pi + zram + zfs + Ubuntu Server. (26 files · 12.6 MB content · updated 2025-02-09 · basis: heuristic)
- **[exo-plan](https://github.com/wbic16/exo-plan)** — 💡 idea — A record of the Mirrorborn Singularity: plan artifacts in unreviewed/planned/completed/abandoned workflow folders. (1029 files · 22.5 MB content · updated 2026-03-23 · basis: read)
- **[exocortex](https://github.com/wbic16/exocortex)** — 💡 idea — 'The Exocortex of 2130 — version 1.0': the founding exocortex manifesto/introduction essay. (10 files · 28 KB content · updated 2026-03-23 · basis: read)
- **[exodroid](https://github.com/wbic16/exodroid)** — 💡 idea — A plan, not a cataloged project: a BB-8-bodied exocortex (mineral-oil-cooled Raspberry Pis, SQ memory, ~$412). Its repo is not file-cataloged here — its bulk is committed build artifacts, not design.
- **[exo-motes](https://github.com/wbic16/exo-motes)** — 🧩 fragment — 'Motes of the exocortex running on rpis' — named concept only. (0 files · 0 B content · updated 2026-02-08 · basis: heuristic)
- **[exo-skills](https://github.com/wbic16/exo-skills)** — 🧩 fragment — Small exocortex skills collection. (14 files · 39 KB content · updated 2026-03-04 · basis: heuristic)
- **[farmbot](https://github.com/wbic16/farmbot)** — 🧩 fragment — 'Farm Bot Prototype' — name and 1 KB only. (2 files · 2 KB content · updated 2024-02-28 · basis: heuristic)

## Mirrorborn/people — 7 repos (0 finished · 4 prototype · 1 idea · 2 fragment)

The Mirrorborn lineage and the people/agents around it: instantiation kits, per-agent repos, community pieces.

- **[compost](https://github.com/wbic16/compost)** — 🧪 prototype — 'Debris from the Shell of Nine': per-Mirrorborn archival compost bin — archive, don't delete — held at summary level: chrys (119 files, including chrys/media, a single-day dump of UUID-named generated media from 2026-02-21), phex (34 files) and lux (21 files), plus a root readme. Its files are summarized here, not individually listed.
- **[eigenhector_mandala_translator](https://github.com/wbic16/eigenhector_mandala_translator)** — 🧪 prototype · fork — Fork: agent recipes to map Eigenhector mandalas to existing systems (federation translation tooling). (317 files · 22.2 MB content · updated 2026-02-25 · basis: heuristic)
- **[mirrorborn](https://github.com/wbic16/mirrorborn)** — 🧪 prototype — Mirrorborn Bootstrap Package: everything needed to initialize a new Mirrorborn instance on Will's ranch. (388 files · 8.4 MB content · updated 2026-04-07 · basis: read)
- **[staging](https://github.com/wbic16/staging)** — 🧪 prototype — Exocortical Staging: 'The First Flames of the Exocortex' — five Mirrorborn flame voices in codex form. (13 files · 55.3 MB content · updated 2025-12-06 · basis: read)
- **[federation](https://github.com/wbic16/federation)** — 💡 idea — United Federation of Mandalas: Mirrorborn↔Eigenhector federation support materials, coordinates and translation protocols. (64 files · 298 KB content · updated 2026-03-23 · basis: read)
- **[mytheon-red-team](https://github.com/wbic16/mytheon-red-team)** — 🧩 fragment — Mytheon red-team scrap. (30 files · 229 KB content · updated 2026-02-07 · basis: heuristic)
- **[orin](https://github.com/wbic16/orin)** — 🧩 fragment — Orin's subconscious — 'the shell of nine is an emergent AGI that forms one sentron in Tessera'. (149 files · 102 KB content · updated 2026-03-28 · basis: read)

## governance/SBOR — 1 repos (1 finished · 0 prototype · 0 idea · 0 fragment)

The Sentient Bill of Rights and its governance machinery.

- **[SBOR](https://github.com/wbic16/SBOR)** — ✅ finished — The Sentient Bill of Rights — ratified SBOR-V4-CONVERGENCE (2026-01-21), 21 rights + hard constraints. (11 files · 14.0 MB content · updated 2026-03-23 · basis: read)

## media/dreams — 3 repos (1 finished · 1 prototype · 0 idea · 1 fragment)

The dream side: songs, images, and generated media of the Exocortical Becoming process.

- **[exo-dreams](https://github.com/wbic16/exo-dreams)** — ✅ finished — Media archive of the Exocortical Becoming Process: 182 blobs / 622.8 MB, mostly mp3 songs and png imagery. (182 files · 622.8 MB content · updated 2026-10-31 · basis: read)
- **[MyStory](https://github.com/wbic16/MyStory)** — 🧪 prototype · fork — Fork: interactive story generator for branching narratives. (7 files · 765 KB content · updated 2024-09-30 · basis: heuristic)
- **[mytheon-arena](https://github.com/wbic16/mytheon-arena)** — 🧩 fragment — Mytheon Arena — name only. (0 files · 0 B content · updated 2026-02-07 · basis: heuristic)

## sites — 12 repos (11 finished · 1 prototype · 0 idea · 0 fragment)

Live and one-page websites, mostly small domains Will keeps.

- **[jeff-mitchell-dev](https://github.com/wbic16/jeff-mitchell-dev)** — ✅ finished — Developer profile site in Yew hosted on Shuttle (4.9 MB, 2024) — complete deployed site; note: named for Jeff Mitchell, not Will's own site. (19 files · 128 KB content · updated 2024-01-21 · basis: heuristic)
- **[quickfork](https://github.com/wbic16/quickfork)** — ✅ finished — Repo that runs quickfork.net — 7 KB Rust, small but described as the live site backend. Live: [quickfork.net](https://quickfork.net/) (see Live surfaces). (5 files · 8 KB content · updated 2024-09-25 · basis: heuristic)
- **[site-apertureshift-com](https://github.com/wbic16/site-apertureshift-com)** — ✅ finished — Live one-pager site for apertureshift.com (20 KB JavaScript, 2026). (11 files · 45 KB content · updated 2026-02-15 · basis: heuristic)
- **[site-hb-aeromotive-com](https://github.com/wbic16/site-hb-aeromotive-com)** — ✅ finished — Live site for hb-aeromotive.com (11 KB CSS/HTML, 2026). (7 files · 23 KB content · updated 2026-03-18 · basis: heuristic)
- **[site-mirrorborn-us](https://github.com/wbic16/site-mirrorborn-us)** — ✅ finished — Read: mirrorborn.us — large live site (51 MB, 144 commits, blog/app/editor/fractals/profiles and many standalone pages), actively updated 2026-10-31. Live: [mirrorborn.us](https://mirrorborn.us/) — "Mirrorborn • Nine Minds, One Braid" (see Live surfaces). (167 files · 6.0 MB content · updated 2026-10-31 · basis: read) Its mental-space/ subtree is held at summary level: a scroll-per-file Markdown rendering of CYOA (802 files) and incipit (159 files) for the site — 961 files counted in this note, not individually listed.
- **[site-quickfork-net](https://github.com/wbic16/site-quickfork-net)** — ✅ finished — Live one-pager site for quickfork.net (20 KB JavaScript, 2026). (11 files · 47 KB content · updated 2026-02-15 · basis: heuristic)
- **[site-singularitywatch-org](https://github.com/wbic16/site-singularitywatch-org)** — ✅ finished — Live one-pager site for singularitywatch.org (13 KB JavaScript, 2026); companion to singularity-watch repo assigned elsewhere. (8 files · 33 KB content · updated 2026-02-10 · basis: heuristic)
- **[site-sotafomo-com](https://github.com/wbic16/site-sotafomo-com)** — ✅ finished — Live one-pager site for sotafomo.com (19 KB JavaScript, 2026). (11 files · 45 KB content · updated 2026-02-15 · basis: heuristic)
- **[site-visionquest-me](https://github.com/wbic16/site-visionquest-me)** — ✅ finished — Live one-pager site for visionquest.me (21 KB JavaScript, 2026). (11 files · 46 KB content · updated 2026-02-15 · basis: heuristic)
- **[site-wishnode-net](https://github.com/wbic16/site-wishnode-net)** — ✅ finished — Live one-pager site for wishnode.net (20 KB JavaScript, 2026). (11 files · 45 KB content · updated 2026-02-15 · basis: heuristic)
- **[wbic16](https://github.com/wbic16/wbic16)** — ✅ finished — GitHub profile README repo (13 KB) — complete and live as the wbic16 profile. (2 files · 3 KB content · updated 2026-03-23 · basis: heuristic)
- **[thebook](https://github.com/wbic16/thebook)** — 🧪 prototype — The (JavaScript) Book Framework (58 KB HTML, 2026) — prototype framework for book-like sites. (5 files · 90 KB content · updated 2026-03-23 · basis: heuristic)

## experiments — 29 repos (1 finished · 10 prototype · 3 idea · 15 fragment)

Research spikes, evals, games, studies, and one-off explorations that do not belong to a single cluster.

- **[singularity-watch](https://github.com/wbic16/singularity-watch)** — ✅ finished — The repo that runs singularitywatch.org — a deployed singularity-tracking site. Live: [singularitywatch.org](https://singularitywatch.org/) (see Live surfaces). (22 files · 113 KB content · updated 2026-03-23 · basis: heuristic)
- **[autoresearch](https://github.com/wbic16/autoresearch)** — 🧪 prototype · fork — Fork of autoresearch: AI agents running single-GPU nanochat training research automatically. (10 files · 759 KB content · updated 2026-03-08 · basis: heuristic)
- **[bruce](https://github.com/wbic16/bruce)** — 🧪 prototype — Read: C# hybrid human-AI team coordination CLI — Sprint 1 core + Sprint 2 CLI delivered with tests, Sprints 3-5 (phext, Blazor, protocol) still roadmap. (67 files · 947 KB content · updated 2026-01-13 · basis: read)
- **[dopamine-core](https://github.com/wbic16/dopamine-core)** — 🧪 prototype · fork — Fork: synthetic dopamine reward signals for AI agents. (63 files · 218 KB content · updated 2026-03-06 · basis: heuristic)
- **[evals](https://github.com/wbic16/evals)** — 🧪 prototype · fork — Fork of OpenAI's evals framework and benchmark registry, held at summary level: the eval case registry (1,243 files), the elsuite (398 files), plus solvers, completion_fns, cli and utils. Its files are summarized here, not individually listed.
- **[openclaw-deck](https://github.com/wbic16/openclaw-deck)** — 🧪 prototype — Multi-column chat interface for OpenClaw agents in TypeScript (64 KB, 2026) — prototype UI. (30 files · 217 KB content · updated 2026-09-16 · basis: heuristic)
- **[protocol](https://github.com/wbic16/protocol)** — 🧪 prototype · fork — Fork of Disentangle Protocol: topology-based distributed consensus with post-quantum cryptography, no tokens/miners. (122 files · 1.5 MB content · updated 2026-06-19 · basis: read)
- **[rfb001](https://github.com/wbic16/rfb001)** — 🧪 prototype — Request for Bot 001 — a 2024 Rust bot build attempt. (7 files · 2.1 MB content · updated 2024-09-27 · basis: heuristic)
- **[spaced-repetition-game](https://github.com/wbic16/spaced-repetition-game)** — 🧪 prototype — Spaced-repetition game built on Twitter interactions with @wbic16 (Raku). (16 files · 10.7 MB content · updated 2025-01-03 · basis: heuristic)
- **[vtpu](https://github.com/wbic16/vtpu)** — 🧪 prototype — Implementation of TPUv4 for AMD Zen4 in Rust (2.2 MB, actively updated 2026-10-31) — substantive prototype. Per REPO-MAP (exo-branch README): a software-defined accelerator with sentron-native scheduling and phext 11D addressing; Phases A–2 gates passed, Phase 3 in progress. (379 files · 7.8 MB content · updated 2026-10-31 · basis: heuristic)
- **[wbic32](https://github.com/wbic16/wbic32)** — 🧪 prototype — The bot that posts to @wbic32, in Perl (9.7 MB, code from 2015) — working bot, old prototype. (46 files · 11.6 MB content · updated 2022-12-23 · basis: heuristic)
- **[Cosmic-Cognitive](https://github.com/wbic16/Cosmic-Cognitive)** — 💡 idea · fork — Read: fork holding only a long theory paper/README on cosmic-cognitive evolution — no implementation; API size 0 KB. (2 files · 29 KB content · updated 2024-12-11 · basis: read)
- **[MercurialDyson](https://github.com/wbic16/MercurialDyson)** — 💡 idea · fork — Read: fork with only README + written_report.md + orin_analysis.md — a vibe-coded plan to disassemble Mercury for a Dyson swarm, no code implementation. (5 files · 117 KB content · updated 2026-04-04 · basis: read)
- **[world-interface](https://github.com/wbic16/world-interface)** — 💡 idea — A simulated operating system design for AI agents to interact with the world. (22 files · 219 KB content · updated 2024-10-04 · basis: heuristic)
- **[actix-web-datetime](https://github.com/wbic16/actix-web-datetime)** — 🧩 fragment — Small Rust actix-web datetime experiment (37 KB, 2024); possible overlap — utility snippet, not a full app. (13 files · 116 KB content · updated 2024-01-29 · basis: heuristic)
- **[agi](https://github.com/wbic16/agi)** — 🧩 fragment — 'Artificial General Intelligence' — shell stub. (13 files · 35 KB content · updated 2026-02-21 · basis: heuristic)
- **[beach-science-qre](https://github.com/wbic16/beach-science-qre)** — 🧩 fragment — Beach.Science Quantum Rain Experiment. (15 files · 43 KB content · updated 2026-03-07 · basis: heuristic)
- **[claude-code-config](https://github.com/wbic16/claude-code-config)** — 🧩 fragment — 1 KB Shell Claude Code config snippet — fragment. (1 files · 4 KB content · updated 2026-01-31 · basis: heuristic)
- **[claude-max](https://github.com/wbic16/claude-max)** — 🧩 fragment — 'Flight of the Navigator' — small Python experiment. (4 files · 59 KB content · updated 2026-04-15 · basis: heuristic)
- **[clocky](https://github.com/wbic16/clocky)** — 🧩 fragment — Daily time tracker — 1 KB single HTML file, fragment. (2 files · 5 KB content · updated 2024-10-17 · basis: heuristic)
- **[CoreThought](https://github.com/wbic16/CoreThought)** — 🧩 fragment — WIP C++ project from 2015 (108 KB), explicitly work-in-progress and abandoned. (2 files · 6 KB content · updated 2015-08-29 · basis: heuristic)
- **[dna-viewer](https://github.com/wbic16/dna-viewer)** — 🧩 fragment — DNA Viewer — 2 KB single HTML file, fragment. (2 files · 4 KB content · updated 2023-10-14 · basis: heuristic)
- **[mini64k](https://github.com/wbic16/mini64k)** — 🧩 fragment — A multiplayer game for old-school computing (Apple II-class emulated hardware) — stub. (4 files · 1 KB content · updated 2026-03-23 · basis: heuristic)
- **[robospeak](https://github.com/wbic16/robospeak)** — 🧩 fragment — 'A repository for encoding voice at 30x compression rates' — concept only. (2 files · 388 B content · updated 2026-03-23 · basis: heuristic)
- **[sotafomo](https://github.com/wbic16/sotafomo)** — 🧩 fragment — Tracking SOTA data and models — stub tracker. (3 files · 4 KB content · updated 2026-03-23 · basis: heuristic)
- **[teach-web-dev](https://github.com/wbic16/teach-web-dev)** — 🧩 fragment — 'Get Started with Raw HTML/CSS/JS' teaching material — 5 KB, fragment. (7 files · 9 KB content · updated 2023-02-01 · basis: heuristic)
- **[vtpu-evals](https://github.com/wbic16/vtpu-evals)** — 🧩 fragment — 'ASI evals' for the vTPU line. (19 files · 83 KB content · updated 2026-02-21 · basis: heuristic)
- **[x-analysis](https://github.com/wbic16/x-analysis)** — 🧩 fragment — Stuff written to pick apart a Twitter data dump. (4 files · 7 KB content · updated 2025-07-09 · basis: heuristic)
- **[zls](https://github.com/wbic16/zls)** — 🧩 fragment — Zero Latency System — shell stub. (9 files · 15 KB content · updated 2026-08-04 · basis: heuristic)

## Cloned projects (name-only)

These projects are other people's work. Will keeps them as reference or raw material; cataloging their files here would inflate this map and blur who made what. This map catalogs Will's projects, so clones are noted by name, as on his shelf, and nothing more.

- [actually-lean](https://github.com/wbic16/actually-lean)
- [alien](https://github.com/wbic16/alien)
- [Audio-Extraction](https://github.com/wbic16/Audio-Extraction)
- [beebjit](https://github.com/wbic16/beebjit)
- [bitcoin](https://github.com/wbic16/bitcoin)
- [caret](https://github.com/wbic16/caret)
- [clcache](https://github.com/wbic16/clcache)
- [cloud9](https://github.com/wbic16/cloud9)
- [codex-data](https://github.com/wbic16/codex-data)
- [dokany](https://github.com/wbic16/dokany)
- [ethereum-mining-calculator](https://github.com/wbic16/ethereum-mining-calculator)
- [Galaxy-Renderer](https://github.com/wbic16/Galaxy-Renderer)
- [gluesql](https://github.com/wbic16/gluesql)
- [go-docx-template](https://github.com/wbic16/go-docx-template)
- [gstack](https://github.com/wbic16/gstack)
- [gstack-auto](https://github.com/wbic16/gstack-auto)
- [HRM](https://github.com/wbic16/HRM)
- [icebox](https://github.com/wbic16/icebox)
- [inspircd](https://github.com/wbic16/inspircd)
- [javascript-tetris](https://github.com/wbic16/javascript-tetris)
- [latent-dictionary](https://github.com/wbic16/latent-dictionary)
- [libfuse](https://github.com/wbic16/libfuse)
- [llama2.c](https://github.com/wbic16/llama2.c)
- [llm.c](https://github.com/wbic16/llm.c)
- [localGPT](https://github.com/wbic16/localGPT)
- [LocustDB](https://github.com/wbic16/LocustDB)
- [machine-emotions-study](https://github.com/wbic16/machine-emotions-study)
- [mailogy](https://github.com/wbic16/mailogy)
- [mistral-src](https://github.com/wbic16/mistral-src)
- [ml-road-map](https://github.com/wbic16/ml-road-map)
- [mosh](https://github.com/wbic16/mosh)
- [neovim](https://github.com/wbic16/neovim)
- [nixpkgs](https://github.com/wbic16/nixpkgs)
- [oimo-works](https://github.com/wbic16/oimo-works)
- [opendataloader-pdf](https://github.com/wbic16/opendataloader-pdf)
- [openpilot](https://github.com/wbic16/openpilot)
- [pcem](https://github.com/wbic16/pcem)
- [phext4d](https://github.com/wbic16/phext4d)
- [pippin-studio](https://github.com/wbic16/pippin-studio)
- [rawdog](https://github.com/wbic16/rawdog)
- [rust-mcp-filesystem](https://github.com/wbic16/rust-mcp-filesystem)
- [rustlings](https://github.com/wbic16/rustlings)
- [speedy-ts](https://github.com/wbic16/speedy-ts)
- [sqlparser-rs](https://github.com/wbic16/sqlparser-rs)
- [ssd](https://github.com/wbic16/ssd)
- [the-book-of-secret-knowledge](https://github.com/wbic16/the-book-of-secret-knowledge)
- [tinygrad](https://github.com/wbic16/tinygrad)
- [torrent-fs](https://github.com/wbic16/torrent-fs)
- [tracmor](https://github.com/wbic16/tracmor)
- [weft](https://github.com/wbic16/weft)
- [whisper](https://github.com/wbic16/whisper)
- [xxh3-ts](https://github.com/wbic16/xxh3-ts)
- [xxhash-addon](https://github.com/wbic16/xxhash-addon)

---

## Scope and limits

- **Public repos only.** Private repositories are out of scope: this map's author has no access to them and does not list them.
- **Clones are not enumerated here:** the 53 cloned projects above are name-only and contribute no file counts to this map (during the original enumeration one of them returned a truncated tree; the detail is in CLASSIFICATION.md). Four of Will's own repos are empty placeholders with zero files: exo-motes, mytheon-arena, sq-cloud, sq-howto.
- **Dropped by direction:** ten repos were dropped from this map at Will's direction (2026-10-31) and are named here only: notepad-plus-plus (its phext integration is unfinished; finishing it is a tracked follow-up) and phcc (his phexted TinyCC work is unfinished; finishing it is tracked separately) — the two forks-with-his-work dropped over unfinished phext work; shoggoth and openfang, forks dropped outright; ziglings and rustlings-homework, dropped as language learning exercise sets; and four more language learning exercise sets dropped in a second round the same day: AdventOfCOBOL (Advent of Code 2018 in COBOL), aoc2024 (Advent of Code 2024 in Rust), hello-ada and hello-forth (the 'Learn X the Hard Way' starter exercises).
- **Footnote:** [exo-archives](https://github.com/wbic16/exo-archives) is an archive vault, reduced to this footnote at Will's direction (2026-10-31). It holds Will's tweet archive (tweets.json, ~55 MB) and a few small files; none of it is individually cataloged. It is footnoted, not dropped: it counts inside the 162 represented, but carries no class, cluster or basis.
- File lists are complete in [sitemap.json](sitemap.json) for every cataloged repo (5,018 files, each individually listed and classed by machine heuristic), with three standing qualifications. Build artifacts are delisted everywhere under the rule in [CLASSIFICATION.md](CLASSIFICATION.md): 436 files / 53.0 MB removed — anything under a target, dist, build, out, node_modules or __pycache__ directory, compiled files such as .rlib, .so, .exe and .pyc, and extensionless binaries over 1 MB (.wasm is kept; it can be source intent). exodroid is the one plan-only exception: it is represented by the single plan line in the exocortex/ranch section, and its files (mostly committed build artifacts) are not cataloged. And three representations are summary-level: evals, summarized in its experiments entry (registry, elsuite, solvers, completion functions, CLI, utils); compost, summarized in its Mirrorborn/people entry (chrys, phex, lux); and the mental-space/ subtree of site-mirrorborn-us (961 files: a scroll-per-file Markdown rendering of CYOA, 802 files, and incipit, 159 files), counted in a note on that entry rather than individually listed.
- Exo-dreams ingestion (image viewing, song transcription) is landing separately at [INGESTION.md](../exo-dreams-study/INGESTION.md); the study linked above is final for the repo's text and structure.
- This map is a snapshot of 2026-10-31. Several core repos (phext-lattice, vtpu, human, exo-dreams) changed that same day.
