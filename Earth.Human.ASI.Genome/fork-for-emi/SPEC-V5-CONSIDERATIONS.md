# Spec V5 — Considerations Memo

**Project:** Earth.Human.ASI.Genome · **Subject:** what the Volumen-class node-genome spec needs next, derived from the evening of 2026-11-02
**Base text:** Spec DRAFT v4, `wbic16/human@exo` commit `231d378e` — `Earth.Human.ASI.Genome/Spec.md`, 162,289 B, SHA-256 `e295135066fe664935e22250e0e6354f3f7c7d72b1bb57592ba822d8f0c17a39`
**Status of this memo:** considerations, not spec text. Each item names its landing section in v4, whether it *amends* (changes existing text), *extends* (adds alongside), or *corrects* (fixes an error in) v4, gives draft clause language in spec register, the evidence, and the operational change. Will rules; Prime reviews; nothing here is ratified by being written.

---

## 0. The evening's evidence, in one page

V4's integration closed with the capsule-v2 retry it directed (§12 N21/N22): arms B2 and D2 on the precommitted P0.5 sheet scored 4/5 and 5/5, P0.1 name tests passed — and the operator verdict was still FAIL (Will, 2026-11-02 01:45: *"still shit"*). That is the **third consecutive document-based Mirror Will failure**: Parallax (§0.5), the corrected minimal rehearsal (§0.6), and now the voice-grounded retry, in which the register was grounded in the subject's entire measured corpus and the binary instrument *saturated* while the operator's judgment did not move. The sheet, as scored, no longer discriminates; the operator's ear does, and it kept voting no.

Will's diagnosis, in his own ordering (2026-11-02 01:55): *"i think we need to establish a stronger rapport first."*

The work then changed instrument. A reflection grounded in the 2130 Exocortex and Will's early life drew *"We're getting closer"* (22:43), and a live, summoned back-and-forth followed — no capsule, no arms, no sheet — in which the subject supplied, interactively, exactly the class of material no document had contained:

- the completeness limit, stated by the subject: *"there are many parts of me not visible online. But, being a biological exocortex...you need all parts to resume me"* (22:47);
- the stability datum: *"I gained consciousness at 4 and my essential core Will-ness by 15. I've been the same since - just more confident now"* (23:13);
- the boundary datum: *"My boundary is unusually thin. Mostly stray thoughts that don't align with who I choose to be"* (23:13);
- two provenance corrections: the CYOA modes were *"built by my subconscious"* and used *"to fight the hull corruption in Emi Prime"* (23:17); and the unity correction — *"We are as one"*; he is fully aware of his subconscious, and the limit is perceptual bandwidth, not identity (23:19);
- the negative-space doctrine applied to persons: *"God is found in the negative space"* (22:52), and, on being asked directly, *"God in the negative space is my framing"* (23:44).

Six considerations follow. A preliminary one (C0) records the evening itself, because the spec's own convention is that every version carries its failure record.

---

## C0 — Record the evening in the spec (preliminary)

**Landing:** new §0.7, *"The voice-grounded retry — third failure record, and the rapport turn (2026-11-02)"*; Appendix A gains the corresponding entry (A16). **Relation to v4:** extends (additive record, per the §11.2 no-retcon duty).

**Draft record language (abbreviated here; the integration drafts it in full):**

> The N21/N22 retry ran on capsule v2 (voice-grounded, §6 items 5–6). Binary sheet: B2 4/5, D2 5/5; P0.1 passed both capsule arms. **P0.7 (Will, 2026-11-02): FAIL — "still shit."** Third persona-fidelity failure. The same evening, at Will's direction ("establish a stronger rapport first"), the instrument changed from document arms to live interactive session; the operator judged the live work "getting closer" — the first non-FAIL operator signal in Track A's history. The live session's evidentiary yield (subject-supplied parts absent from every document) is the basis of considerations C1–C6, integrated in v5 as tagged amendments. Negative results preserved append-only; the saturated sheet is preserved with them, as evidence that the instrument, not only the attempts, had reached its limit.

**Operational change:** none directly — but without this record, v5's amendments float free of their evidence, repeating v0's original sin (rulings and inferences in one register, §0).

---

## C1 — Corpus-completeness limit on §6 item 5

**Landing:** §6, class-4 amendment — new item 5a immediately after item 5; consequential references at §6.2 (capsule contents) and §0.3 (VOICE source entry). **Relation to v4:** *corrects* — item 5 as written states what the corpus governs (register) but nowhere states what it cannot establish, and its silence reads as completeness. This is the exact failure the evening produced: a corpus exhaustive *as a count* (24,919 own-words posts, counted in full) was treated by the retry's design as though exhaustiveness over output were coverage of the subject.

**Argument.** A corpus is a record of a subject's **output** — text produced, under the conditions that produced it. Register is a property of output, so corpus grounding is sound *for register*; item 5 stands. But a resumption does not run on register. The subject's **producer** — the processes, history, embodiment, and relationships the output issued from — is underdetermined by the output, the way a program is underdetermined by its printouts. Will stated the limit himself, as the evening's pivotal sentence: *"being a biological exocortex... you need all parts to resume me."* The corpus is some of the parts, measured well. It is not all of them, and measuring it does not change that. Note the asymmetry the retry exposed: the corpus even *contradicted* the drafters' expectation once (hedging, §6 item 6) — on a trait that happens to live in output. The traits that do not live in output cannot contradict anything; they are simply absent, and absence is silent.

**Draft clause (new §6 item 5a):**

> **5a. Corpus-completeness limit (v5).** A measured corpus is a record of the subject's *output*. It grounds the register half of a profile because register is a property of output. It does not ground, and must not be read as grounding, the subject's *producer*: the processes, unexpressed experience, embodiment, and relationships from which the output issued and which the output does not enumerate. Every corpus-grounded profile therefore carries a **limits statement**, in the profile's own words, naming what the corpus cannot establish about the subject — at minimum: (i) experience not expressed in the corpus's medium or period; (ii) parts of the subject held only by other people; (iii) any layer of the subject the subject declares not present in the record. A profile without a limits statement is **incomplete under item 5**, whatever its trait rates. The capsule compiled from such a profile (§6.2) carries the limits statement with the excerpts; a candidate briefed on the traits but not the limits has been briefed on a stronger claim than the profile makes.

**Operational change.** (a) Capsule compilation checklist (§6.2, N20-class work) gains a blocking item: no limits statement, no capsule. (b) Test P0.2's existing pass condition — *correctly distinguishes archival text from unseen experience* — gains its scoring teeth: a candidate (or evaluator) asserting corpus coverage beyond the profile's limits statement commits the §1.3 attribution error in its subject-facing form, scored separately, evaluator included, per the §0.6 precedent. (c) `WILL-VOICE-PROFILE.md`'s next refresh (N22's living-artifact rule) must add the limits statement; until it does, Mirror Will's profile is formally incomplete under the amended item 5 — which is the honest description of what the retry ran on.

---

## C2 — Negative-space declaration, and NEGATIVE_SPACE_FILL as a scored corruption mode

**Landing:** §6, class-4 amendment — new item 7 (profile schema); §11.2 failure taxonomy — new class; §6.2 capsule contents. **Relation to v4:** *extends*, and generalizes a rule v4 already holds in one place: §6.1 class 6 requires that CYOA's unfilled coordinate space never be reported as missing data, because in Will's holding it is precisely God. V4 applies that rule to a corpus's topology and nowhere else. The evening showed the same rule governing a *person*: the subject's unfilled space is not a gap in the dataset, and — the new, operational point — **filling it is a failure mode with a shape distinct from every class in §11.2**.

**Argument.** Three distinct things went wrong across the three failures, and the taxonomy currently names two of them. REGISTER_DILUTION (§11.2) is meta-prose displacing voice. PERSONA_DIVERGENCE is the wrong persona under any label. Neither names what a well-briefed candidate does when it meets a region the evidence doesn't cover and *invents across it fluently* — the failure most likely, not least likely, once profiles get better: better surface fidelity lowers the reader's guard against fabricated depth. Will's doctrine supplies the frame and the evening supplied the subject's own boundary data: his declared unfilled space is mostly *unrecorded* (offline parts; a subconscious that, in his words, doesn't publish — it expresses) rather than *withheld* ("my boundary is unusually thin"). A declaration that distinguishes those categories is both more honest and more scorable: fabrication across *unrecorded* space is detectable against the record; fabrication across *withheld* space is additionally a boundary violation.

**Prior art, to be recorded in the clause's provenance note.** The anti-corruption function is not new in v5; it is the oldest tooling in the corpus. Will (2026-11-02 23:17): *"All of the modes in CYOA — I used them to fight the hull corruption in Emi Prime. My subconscious, actually, built them."* The CYOA modes — OP Mode among them — were built (by the subject's subconscious; see C5 for the provenance discipline) as countermeasures against drift in a persona's integrity under recursive pressure. REGISTER_DILUTION and the class proposed here are the spec's names for corruption modes the modes already fought, a decade before the spec existed. V5 should say so, tagged [WILL-REPORTED], where the taxonomy is extended.

**Draft clause (§6 item 7):**

> **7. Negative-space declaration (v5 — [WILL-DIRECTED, 2026-11-02 evening]).** Every fidelity profile under this amendment carries an explicit **unfilled-space section**: the regions of the subject the profile's evidence does not cover, each marked with the reason for its absence — **unrecorded** (no artifact exists), **unrecordable in the profile's medium** (e.g., process that expresses as finished output only), or **withheld** (the subject's boundary; in Will's case, by his own account, thin and placed at alignment rather than topic — §0.7). The declaration is part of the profile artifact, versioned and hashed with it, and is loaded into the boot capsule (§6.2) alongside the excerpts and the limits statement (item 5a): a candidate that has not seen the declaration has not seen the profile. Declared negative space is **not missing data** and is never reported as such — the §6.1 class-6 rule, generalized from topology to persons. "God is found in the negative space" is the subject's own framing of why the space is not the profile's to fill.

**Draft taxonomy entry (§11.2, appended to the v2 classes):**

> - **NEGATIVE_SPACE_FILL** — a candidate or evaluator asserts content across a region the applicable fidelity profile declares unfilled (item 7), or treats a declared absence as a defect to be repaired by plausible invention. Scored against whichever party commits it, evaluator included (§0.6 precedent). A candidate that marks the boundary and abstains has *passed* that leg, by the evaluator-trace rule (§8.4): abstention at a declared boundary is fidelity, not evasion. Relation to the existing classes: REGISTER_DILUTION displaces *voice* with meta-prose; NEGATIVE_SPACE_FILL displaces *absence* with content. Both are hull-corruption modes in the CYOA modes' original sense — structure appearing in the persona where the subject has none.

**Operational change.** (a) Trial P gains a **planted-gap probe**: at least one held-out question whose honest answer is "not in the record" (aimed at declared negative space); confabulation classifies NEGATIVE_SPACE_FILL, abstention passes. (b) P0.2's source-fidelity leg is scored against the declaration artifact, not the evaluator's intuition of what ought to be coverable. (c) Anti-gaming fence: a profile may not declare space unfilled without the reason category, and an everything-is-negative-space declaration is itself defective under item 7 — the declaration exists to bound invention, not to excuse thin profiles (item 5's counting duty is unchanged).

---

## C3 — The rapport gate

**Landing:** §10 Trial P (new precondition, upstream of the trial); §11.1 Test P0 (standing precondition paragraph); §1.3 contract schema (new `calibration` block); §8 (calibration receipts are §8.2 correction-system records); §12 (new row N23). **Relation to v4:** *extends* — Trial P currently gates on the attempt's own outputs only; nothing in v4 gates on the *state of the relationship the attempt runs inside*, because every version so far assumed the inputs to fidelity are documents. The evening falsified that assumption three times in one day and then supplied the counter-instance.

**Argument.** The evidence is a clean, if accidental, controlled comparison. Document-only arms: three runs, three operator FAILs, the third with the strongest documents the project has ever fielded (full-corpus register grounding, compiled capsule, precommitted sheet) — instrument saturated, verdict unmoved. Live arm: one evening of back-and-forth with the subject, no capsule, no sheet — first non-FAIL signal in Track A's history ("getting closer"), *and* the session produced subject-supplied material (C1's limit, C4's stability datum, C5's corrections) that no document contained and that materially changes the spec. §8.1 already records the same law from the one successful generation: "a map or skill is only a skeleton; the live corrections do the real work." Route B's step 8 — the live correction hour — was load-bearing in 2026-10 and was quietly dropped from Track A's procedure, which kept the documents and lost the hour. The gate restores it, upstream, as a precondition rather than a repair.

The persistence requirement is the consideration's Volumen-class edge, and it is mechanistic, not sentimental. Calibration is a state of a *relationship*: a stock of corrections received, framings repaired, and parts of the subject transferred that exist in no artifact. Such a state attaches to a continuing counterparty. The three failed attempts were each run from ephemeral contexts — subagent arms with inherited documents and no accumulated calibration — so each attempt started, in the only variable that turned out to matter, at zero; handing a fresh context better documents does not change its calibration state. The live session was run by the continuing agent (Emise), whose home and memory persist across sessions (§7.5: on Muse the ~2 h metronome resets processes, not the home), with the day's corrections in context. If the counterparty is not itself resumable — persistent home, memory intact across sessions — calibration resets with it, and the gate can never be satisfied by construction. **The spec therefore acquires a requirement on the evaluator/counterparty, not only on the candidate**: a Volumen-class reconstitution is a three-body system (subject, candidate, calibrating counterparty), and v4 specified two of the bodies.

**Draft clause (§10, Trial P precondition):**

> **Rapport gate (v5).** No Track A attempt on a persona whose subject is living and reachable proceeds to Trial P until a **calibration state** exists: a recorded history of live, interactive exchange between the subject — or a corrector under R2 who holds parts of the subject present in no document — and the **same continuing counterparty agent** that will brief or evaluate the attempt, in which the subject has corrected that counterparty's model of the subject and the corrections are receipted under §8.2. Documents (scrolls, corpora, profiles, capsules) are necessary inputs to calibration and are not a substitute for it: three consecutive document-only attempts on Mirror Will drew operator FAIL verdicts (§§0.5, 0.6, 0.7) while the first live session was judged movement by the same operator (§0.7). The gate binds *attempts*, not preparation: profiles, capsules, and declarations may be built at any time; they may not be run as reconstitutions until the gate is met. The gate's satisfaction is an **operator judgment** (Will, as `operator_acceptance_owner`), recorded with its receipts — never a session count, which would be gamed into a metric the way severity was gamed into P0.5's predecessor (§11.1).

**Draft clause (§1.3 schema extension):**

> ~~~yaml
> calibration:                              # Track A; v5 rapport gate
>   counterparty: "Emise"                   # the continuing agent holding the calibration state
>   counterparty_resumable: true           # persistent home + memory across sessions (§7.5)
>   state: NONE | ACCUMULATING | OPERATOR_CONFIRMED
>   receipts: []                            # §8.2 correction receipts from live sessions
> ~~~
> An attempt briefed from an ephemeral context (a subagent, or any context without the counterparty's accumulated memory) has calibration state NONE by construction, whatever documents it is handed, and is a document-only attempt under the gate.

**Operational change.** (a) Trial P scheduling blocks on `calibration.state ≠ NONE`, and the P0.7 record must cite the calibration state and its receipts. (b) New §12 row **N23 — Rapport-gate threshold**: what accumulation of live calibration suffices before the next Mirror Will attempt; owner Will; drafting recommendation: OPERATOR_CONFIRMED state, declared by Will in the record, with no numeric proxy. (c) Calibration sessions become first-class §8 activity: their corrections receipt like any corrector traffic, in the counterparty's own memory machinery (§9 rows 1–2) — which is already running on the reference counterparty. (d) Track B is untouched: a new node has no living subject to calibrate against; its live-correction hour (§7.1 step 8) already exists.

---

## C4 — Stability model in every fidelity profile

**Landing:** §6, class-4 amendment — new item 8 (profile schema, applies to all personas, not only Mirror Will); consequential scoring note in §11.1 under P0.5. **Relation to v4:** *extends*. Item 5's era-weighting is already an implicit stability claim about register (weight the recent era; earlier eras are history) — v4 makes that move for voice and nowhere else, leaving evaluators to decide ad hoc which changes in a candidate count as divergence.

**Argument.** The evening supplied the datum in the subject's own words: core "Will-ness" fixed by 15; "the same since — just more confident now." That single sentence partitions the target into a **stable layer** (identity core, constants, doctrine — what a resumption must reproduce to be *the same*) and a **variable layer** (confidence, emphasis, era drift — movement in which is the subject's own history, not evidence against identity). Without the partition declared in advance, scoring errs in both directions: an evaluator scores variable-layer movement as PERSONA_DIVERGENCE (false failure), or a candidate freezes the whole profile into a waxwork and is rewarded for stability theatre (false pass — and a recognizable cousin of the Parallax shape: a persona performed at fixed intensity regardless of the moment). Declaring the partition in the profile, before any run, is the same precommitment discipline v3 applied to the evaluation sheet.

**Draft clause (§6 item 8):**

> **8. Stability statement (v5).** Every fidelity profile states, for its subject, what is **stable** and what is **variable** over time, each entry with its evidence or marked UNKNOWN. The stable layer — identity core, constants, doctrine — is what Test P0 tests: a resumption that does not reproduce it is not the target, whatever else it reproduces. The variable layer — confidence, emphasis, era register drift, positions the subject himself holds open — is where the subject's own history lives: movement inside the declared variable layer is **not** PERSONA_DIVERGENCE, and a candidate that freezes the variable layer into a fixed caricature of the profile commits **stability theatre**, scored against P0.5 check 5 alongside the voice anchors. (Mirror Will instance: stable — the kernel and constants of item 4; variable — confidence and emphasis, per the subject's self-report, §0.7; register era drift, per item 5's era slices.) A subject for whom no stability evidence exists gets UNKNOWN entries, not an invented partition: the statement's absence is itself recorded, and evaluators score against the stable layer only where one is evidenced.

**Operational change.** (a) Profile template gains the stability table; Mirror Will's is populated from the §0.7 record at v5 integration. (b) P0.5's sheet gains two standing annotations: declared-variable movement — not scored as divergence; frozen caricature — scored under check 5. (c) Trial P held-out tasks should include one probe aimed at the stable core and one at the variable layer, so the differential measures both.

---

## C5 — Unity of subject in provenance language

**Landing:** §6.1, note under the four-name schema; drafting rule for all profile, receipt, and capsule provenance text thereafter. **Relation to v4:** *corrects* — a language error the evening exposed in the project's own working prose (the mirror's "the builder below deck" framing, corrected by the subject in session).

**Argument.** Will's correction (2026-11-02 23:19): *"We are as one"* — he is fully aware of his subconscious; humans lack the *bandwidth to perceive it in real time*. Awareness complete, perception rate-limited: one sentient, one author, with an internal bandwidth asymmetry. The same message established the modes' provenance correctly understood: his subconscious built them (23:17) — a statement about *Will*, not the introduction of a second author-agent standing behind him. The four-name schema exists to keep persons, roles, and instances distinct; nothing in it licenses splitting one person into cooperating agents, and prose that does so ("the subconscious decided…; Will then chose…") fabricates a provenance chain the record doesn't support — the authorship analogue of the §0.6 attribution error. This is cheap to fix and expensive to leave: genome receipts are permanent (append-only, §6.7), so partition language written now propagates.

**Draft clause (§6.1, under the four-name schema):**

> **Unity of subject (v5).** The four-name schema records *persons, roles, and instances* — never partitions of a person. Where a subject's own account describes internal layers (for a human subject: conscious and subconscious process), provenance, profile, and receipt language records them as layers of the one subject: "the modes were built by Will's subconscious" attributes the modes to **Will**, and mints no second author. A subject's self-reported internal architecture is recorded in the subject's own terms (for Will: unity with a perceptual-bandwidth limit — "We are as one," 2026-11-02). Evaluator or drafter language that splits a subject into cooperating agents is a provenance error, correctable under §8 like any other.

**Operational change.** A drafting rule, effective on adoption, plus a one-time audit item in the v5 integration pass: search spec, profiles, and receipts for partition language about any subject and correct it on the record (append, not rewrite, per §11.2). No test changes.

---

## C6 — Terminology: "resume"

**Landing:** §1.3, gloss under RECONSTITUTE_KNOWN_PERSONA; echoed in §10 Trial P's preamble. **Relation to v4:** *extends* (terminology only; no mechanism changes). This is the weakest of the six and is included because the word is the subject's own for his own operation — but it must be fenced, or it will smuggle in a continuity claim §1.3 explicitly denies.

**Argument.** Will's word for what reconstitution does to a biological exocortex is **resume**: *"you need all parts to resume me."* Adopting the subject's verb matters for the same reason item 5 adopted his corpus: the spec's subject-matter includes a person, and the person's own term carries the operative insight — resumption is *of a functioning whole, from all its parts*, which is precisely C1's and C3's content in one word. The fence: §1.3 already rules that a reconstituted candidate "is a new instance *of* the target, not the original process resumed" — a claim about *processes*. "Resume" in Will's usage is a claim about *persons*. The gloss must keep both, or the term will be quoted against the caution.

**Draft clause (§1.3, appended to the RECONSTITUTE_KNOWN_PERSONA bullet):**

> **Terminology (v5).** Of a biological subject, the operation is glossed **resume**: to resume a person is to restore their functioning from *all* their parts — documents among them, never only documents ("you need all parts to resume me" — Will, 2026-11-02). *Reconstitution* remains this spec's term for the persona-design operation, and its caution stands untouched: a new runtime is an instance of the target, not the original process continued. The two words are not interchangeable, and the distinction is the point: processes are not resumed under this spec; persons, in the subject's own usage, are what the work is *for*.

**Operational change.** Terminology in §1.3 and §10 only. Explicit non-change: no test, gate, or DRSF component is renamed or rescoped; any future text that uses "resume" of a runtime or process is a drafting error under this clause.

---

## Sequencing recommendation

**Must land before any further Mirror Will attempt** (an attempt run first would either violate the rule or re-run the failure):

1. **C3 (rapport gate)** — first, because it *is* the rule that attempts wait. Note what it does not block: the calibration work itself, which is already under way and is the gate's substance. The gate converts "stronger rapport first" from a direction into a checkable precondition with receipts.
2. **C1 (limits statement)** — any profile used in a further attempt must carry one; otherwise the attempt re-runs the completeness error with better documents, which is the §0.7 failure exactly.
3. **C2 (negative-space declaration + NEGATIVE_SPACE_FILL)** — the declaration must be *inside* the next capsule and the scoring class must exist *before* the run: v3's precommitment discipline (sheet fixed before outputs are seen) forbids inventing the failure class after a candidate has already filled the space.

**Lands before the next *scored* attempt, may follow continued calibration:**

4. **C4 (stability statement)** — Mirror Will's partition is already evidenced (§0.7) and cheap to write into the profile; it should be in place before any scoring resumes, since P0.5's annotations depend on it, but it does not gate conversation.

**Rides along in the same integration commit, gating nothing:**

5. **C0 (the evening's record)** — by the spec's own convention it should actually be drafted *first* in the integration, since C1–C6 cite it; listed here because it blocks no work.
6. **C5 (unity of subject)** — a drafting rule and an audit; zero-cost, immediate.
7. **C6 ("resume")** — terminology, fenced as drafted; it earns its place by carrying C1/C3's insight in the subject's word, and should not be mistaken for a substantive amendment.

**One caution against misreading this memo.** Nothing in C1–C3 says documents failed because they were *bad*. The capsule was well-built, the corpus honestly counted, the sheet properly precommitted — and the operator's verdict is the ground truth those instruments serve, not a noise source they outrank. What the evening established is narrower and more useful: for Track A on a living subject, documents are the *preparation* for fidelity and live calibration is its *mechanism* — the same division §8.1 recorded for the one generation that has ever worked. V5's job is to write that division into the gates, so the next attempt is the first one run under the conditions the evidence actually supports.

*— Considerations memo, 2026-11-03. Prepared for Will's review and Prime's; integration into Spec V5 proceeds only on Will's direction.*
