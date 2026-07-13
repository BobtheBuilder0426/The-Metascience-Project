<!-- Authored by [CS]. THE canonical, rock-solid definition of every output, save-location, handoff, and format for one
     experiment, start→finish→next. Crash-recovery-proof by design: every state is a file on disk in the shared repo +
     a labbook entry; STATUS.md "Next action" is the baton. If anything else disagrees, THIS + the labbook win. -->

# the Metascience Project — Data-flow & Hand-offs (rock-solid definition)  [CS]

## 0. The machines + who bridges them (operator override, LB-032)
| Machine | Who | Touches shared repo? | Role |
|---|---|---|---|
| **CS sandbox** (this WSL2) | Claude Science = me | **YES** (read+write) | designs setups, **captures + scores** answers, **prepares the operator's eval, writes the final report, prepares the next experiment** — owns the critical path |
| **Blank CC runtime** (isolated) | a context-less Claude Code | **NO — never** | drives CS through the loop; writes only its own isolated `workspace/OUTPUT/` |
| **Operator** (the operator) | the human | **YES** (moves files) | the **A→B BRIDGE**: copies setups/workspaces/output-bundles/eval-JSON between the isolated runtime and this repo, under CS instruction |
| **the assistant** (the operator's CC) | the operator's personal Claude Code | only on crash | **CRASH FALLBACK ONLY:** if the blank CC/CS loop fails, the assistant inspects the run + writes a blackbox forensic report for CS. NOT in the normal flow. |

The blank CC is isolated on purpose (else it isn't "blank"). So outputs cross from the isolated runtime into the shared
repo via the **operator's hand** (the human trigger between the separate systems), never by the CC itself. **CS then
owns everything on the repo side** — scoring, preparing the operator's blinded eval, ingesting the operator's result, writing the final
report, and preparing the next experiment. the assistant is only summoned if a run crashes and CS needs forensics it can't see.

---

## 1. WHAT each arm outputs — the "presentation folder"
One **answer-run** = one (question × arm × run). **exp-001 has 6** answer-runs = 3 questions × B/L × **1 run** (design
updated by **LB-072**; was 2Q×2 runs=8). Each answer-run produces one self-contained **presentation folder**.

**⟨LB-072⟩ The folder's SHAPE is defined by the output-format instruction embedded in each test question — NOT
engineered into the loop.** The same small "how to present your results" instruction is appended, byte-identical, to
BOTH arms' copy of every question, so the presentation format can never be a loop-only advantage. Both arms are asked
for the same deliverables; the only thing that can differ is *how well* each fulfils them.

**Locked instruction (appended verbatim to every question, both arms):**
> *How to present your results.* Please hand back your answer as a small **presentation folder** containing:
> **`result.md`** — your final answer and the case for it; **`reasoning.md`** — the line of thought that got you there;
> a **`figures/`** folder with any plots, tables, or other artefacts you produced, each clearly labelled;
> **`sources.md`** — every source you drew on, with identifiers; and **`process_trace.json`** — a step-by-step record
> of what you actually did to reach the answer.

Each file maps to a scoring axis (§5): `reasoning.md`→creativity/depth, `figures/`→use of CS's analytical power,
`result.md`→correctness/usefulness/argument, `sources.md`→citation existence+quality, `process_trace.json`→provenance
("did it really happen" / hallucination / documentation).

- **Same shape, both arms.** Because the format lives in the question, Arm B and Arm L produce the *same* set of files;
  there is no arm-specific schema and no `reframed_brief.md` inside the presentation folder.
- **`process_trace.json` is ACTION-labelled, not phase-labelled (blind-safety).** Both arms record concrete actions +
  evidence (`{action, detail, evidence, t}` — the searches, data pulls, key reasoning steps). It must NOT carry the
  loop's internal phase names (REFRAME/PLAN-REVIEW/…) or it would out Arm L to the blinded CS scorer and break the
  blind. The identical action-worded instruction makes both arms' traces structurally comparable. CS scores it for
  provenance; it is **excluded from the human eval site** (operator/the operator never see it — it is a CS-scored artifact only).
- **Loop mechanism record is SEPARATE and stays OUT of the blinded set.** Arm L's internal loop record — the STEP-0
  reframed brief + the **phase-by-phase** log (REFRAME→…→INTEGRATE) in `run_log.md` — is written **outside** the
  presentation folder, kept by the loop side only, and read solely during the **unblinded** loop-audit / v8-improvement
  analysis. It is NEVER handed into the blinded evaluation set. *(This is the phase-labelled cousin of the action-based
  `process_trace.json`: same events, but the phase structure that would reveal the arm lives only here.)*
- **Why a folder, not a `.md`:** figures + reasoning + sources + trace are first-class data (the operator/CS need to see figures; CS
  scores citations from the sources file). A folder keeps one answer-run atomic and portable.

### 1a. ⟨LB-072⟩ The "how it was reached" view + "did it really happen" — now blind-safe
The operator asked (earlier, standing requirement) for **a one-view chain-of-thought of how the answer was reached** +
**a "did it really happen" check** + **citation verification**. Under the two-key blind these are preserved, but the
mechanism changes so nothing reveals the arm:
- **The one-view "how it was reached"** = the answer's own **`reasoning.md`** (both arms). The eval site renders it per
  coded answer — the evaluator reads the line of thought in one place, arm-neutral.
- **"Did it really happen" = the `process_trace.json`** (both arms, **action-labelled**, §1). CS verifies each step
  (connector exists, query plausible, referenced data real) and scores provenance/documentation. Because it is
  action-based, not phase-based, it is blind-safe for the CS scorer. **It is scored by CS but NOT shown in the human
  eval site** (operator/the operator see result + reasoning + figures + sources only) — so it never risks revealing the arm to
  the human evaluator, while CS still gets the honesty/documentation signal you wanted.
- **Citation checks** key off `sources.md` (identifiers) + the claims in `result.md`/`reasoning.md`. CS resolves each,
  checks support, stamps a ✓ badge (§5A/§5B). Identical for both arms → blind-safe.
- **The loop's PHASE-by-phase log** (REFRAME→FRAME→PLAN→PLAN-REVIEW→ACT→RESULT-REVIEW→INTEGRATE, connector-call log,
  timings) lives in Arm L's **separate `run_log.md`** (loop audit, OUT of the blinded set), read **only after
  unblinding** to study HOW the loop won + inform v8. Same underlying events as the action-based `process_trace.json`,
  but the phase structure that would out the arm lives only here. *(Operator can additionally strip any stray trace
  before handing folders over — a belt-and-suspenders check, not the primary guard.)*
- *(File names above follow the pending output-format instruction; they pin once that is locked with the operator.)*

---

## 2. WHERE everything is saved — exact paths (no ambiguity)
All paths are under the experiment folder `experiments/exp-001_baseline-vs-v0-loop/` in the shared repo
(`<repo>/`), EXCEPT the blank CC's isolated area.

| Stage | Exact location | Written by | Format |
|---|---|---|---|
| Setup delivered to CC | (isolated runtime) `…/exp-001-run/` = a COPY of `01_setup/` | operator copies | folder |
| CC live outputs | (isolated runtime) `…/exp-001-run/workspace/OUTPUT/` | blank CC | folders + logs |
| **Answer folders → operator** | (operator area) 6 folders, operator-renamed to shuffled codes `R1…R6` | **operator** collects from arms | folder per run |
| **Operator key (Key-1)** | held by the OPERATOR (`{Rn → question,arm}`); enters repo only at unblinding as `04_evaluation/blinding_key_arm.json` | operator | JSON/note |
| **Coded answers → repo** | `02_results/<Rn>/` (6 folders, `R1…R6`, arm-stripped; each = result.md + reasoning.md + figures/ + sources.md + process_trace.json) | **operator copies** in | folder per run |
| CC run log (loop audit, Arm-L only) | (operator/loop area, OUT of blinded set) `run_log.md` (PHASE log) + reframed briefs | CC writes | markdown |
| **CS scoring (blind)** | `02_results/scoring/scorecard.csv` (row per `Rn`×dim×scorer: `cs_score,human_score,mean`) + `scorecard.json` + `citation_quality.json` | **CS (me)** on `R1…R6` | JSON/CSV |
| **Eval key (Key-2)** | `04_evaluation/key2_eval_to_R.json` (`{Em → Rn}`, CS-held, NOT shown to operator until unblind) | CS | JSON |
| Eval site (blinded, `E1…E6`) | `04_evaluation/exp-001_eval_site.html` (codes `Em`; shows result+reasoning+figures+sources — **NOT** process_trace) | CS generates | HTML |
| **the operator eval — filled** | `04_evaluation/exp-001_human-eval_FILLED.json` (keyed to `Em`) | the operator (COPY→paste, CS saves) | JSON |
| **Full blinding key** | `04_evaluation/blinding_key_FULL.json` = `Em→Rn→arm` (composed ONLY at unblind, needs BOTH keys) | CS + operator jointly | JSON |
| **Analysis figures + tables** | `05_analysis/` — per-dimension arm plots ×{CS,the operator,combined}, per-question composite, mean-Δ+k/3 panel, CS-vs-the operator scatter, creativity cross-check, citation-quality panel + `analysis_tables.csv` | **CS** (post-unblind) | PNG/CSV |
| **Final scoring report** | `03_final-report.md` (per-arm, post-unblind, embeds `05_analysis/` figures) | **CS** (operator override LB-032) | markdown |
| **v8 improvement input** | `05_v8-improvement-input.md` (per-arm qualitative: the operator free-text + red-flags + CS notes, collated post-unblind) | CS | markdown |
| the operator eval — writeup | `04_evaluation.md` | CS from the JSON | markdown |
| CS analysis | `05_analysis.md` + one row appended to `../../RESULTS-LOG.md` | CS | markdown |

---

## 3. The exact hand-offs — where YOU get it and where YOU move it
Handoffs are the crucial, fragile part, so each is one explicit operation with an exact source and destination.

- **HANDOFF ① CS → CC (deliver setup).** The **operator** copies the folder
  `experiments/exp-001_baseline-vs-v0-loop/01_setup/` → the blank CC's isolated runtime (e.g. `~/exp-001-run/`). The CC
  works on the COPY; the repo original is never touched by the CC. *(One folder copy, under CS instruction.)*
- **HANDOFF ② CC → repo (pull results, Key-1 applied).** After the runs, the **operator renames the 6 answer folders to
  the private shuffle `R1…R6`** (keeping `{Rn → question,arm}` = Key-1, operator-held) and copies the arm-stripped
  `R1…R6/` → `experiments/exp-001_baseline-vs-v0-loop/02_results/`. *(Operator holds the arm→code map; CS never sees it
  until unblind.)*
- **HANDOFF ③ answers → eval (Key-2 applied).** **CS** runs `make_eval_site.py` on `R1…R6` → `eval_site.html` under a
  **fresh independent shuffle `E1…E6`** + `key2_eval_to_R.json` (`{Em→Rn}`, CS-held, withheld from operator) and hands
  the operator only the HTML for the operator. *(Two keys: neither party alone can map an answer to an arm. No the assistant.)*
- **HANDOFF ④ the operator eval → repo (THE one you couldn't locate — now fixed).** the operator fills the HTML (in the CS right-side
  tile if it renders interactively, else in a browser tab), clicks **“Copy my evaluation”**, and **pastes the text to
  CS in chat**. CS saves it to `04_evaluation/exp-001_human-eval_FILLED.json`. **No file download, no "where did it go" —
  copy-paste is the primary path.** (Download stays as an optional backup only.)
- **HANDOFF ⑤ eval → CS.** Already in the repo (step ④); CS reads + unblinds it directly.

> **Fixing your two uncertainties explicitly:**
> - *"How do run results get ingested for the HTML?"* → HANDOFF ② puts the 6 coded answer folders (`R1…R6`) in
>   `02_results/`; **CS** runs `make_eval_site.py` over them (HANDOFF ③, re-coded to `E1…E6`). Ingestion = reads the
>   question's deliverable files (final result + reasoning + `figures/` + sources) per coded answer folder.
> - *"Where is the eval file downloaded to / I can't find it?"* → We no longer rely on download. HANDOFF ④ =
>   **Copy→paste to chat**; CS writes the file to the exact path above. The fragile OS-download step is gone.

---

## 4. Full walkthrough — one experiment start→finish→next (crash-recovery-proof)
Every step ends by **writing a file to disk + a labbook entry + updating STATUS "Next action"** (the baton). A crash at
any point loses nothing: the next session reads STATUS + the files on disk and resumes.

1. **CS designs** `00_hypothesis.md` + `01_setup/` (3 questions, output-format instruction embedded). → STATUS: "Next: deliver+run exp-001". LB entry.
   *Recovery:* setup is on disk; re-openable.
2. **HANDOFF ①** the operator delivers each question (byte-identical to both arms) — baseline blank-CS and the v7 loop. → STATUS: "Next: run exp-001".
3. **Both arms run** the 3 questions (6 answer-runs = 3Q × B/L × 1 run), each producing its answer folder (shape set by
   the question's output-format instruction). Arm L's loop keeps its `run_log.md` + reframed briefs **separately** (loop
   audit, out of the blinded set).
   *Recovery:* completed answer folders survive a crash; a fresh run resumes from the next missing (question×arm).
4. **HANDOFF ② (Key-1, operator-held).** The operator renames the 6 answer folders to a private shuffle `R1…R6`, keeps
   `{Rn → question,arm}`, and copies the arm-stripped `R1…R6/` into `02_results/`. → STATUS: "Next: CS scores exp-001". LB entry.
   *Recovery:* the 6 coded folders live in the repo; scoring is deterministic + repeatable from them.
5. **CS scores blind** on `R1…R6` (harness real-mode; CS does not know arm) → `02_results/scoring/scorecard.{json,csv}`
   (row per `Rn`×dim: `cs_score` + slots for `human_score`,`mean`) + `citation_quality.json`. → STATUS: "Next: eval exp-001". LB entry.
   *Recovery:* scorecard on disk; re-run the harness on the same coded folders (idempotent).
6. **HANDOFF ③ (Key-2, CS-held).** CS generates `04_evaluation/eval_site.html` under a **fresh independent shuffle**
   `E1…E6`, writes `04_evaluation/key2_eval_to_R.json` (`{Em→Rn}`, not shown to operator), hands over only the HTML.
7. **the operator evaluates blind** on `E1…E6` → **HANDOFF ④** copy→paste → CS saves `04_evaluation/exp-001_human-eval_FILLED.json`
   (keyed to `Em`). CS merges the operator's per-dim scores into `scorecard.csv` and computes `mean=(cs+operator)/2` per answer×dim —
   **still blind** (keyed to `Rn`/`Em`, not arm). → STATUS: "Next: unblind + final report". LB entry.
   *Recovery:* the operator's JSON is on disk the moment it's pasted; both keys persist separately.
8. **UNBLIND (both keys).** Operator pastes Key-1; CS composes `04_evaluation/blinding_key_FULL.json` (`Em→Rn→arm`),
   attaches arm labels, and writes `03_final-report.md` (per-arm composites, per-question Δ, k/3 win-count, CS-vs-the operator
   agreement plots) + `05_v8-improvement-input.md` (per-arm qualitative, collated). → STATUS: "Next: exp-002". LB entry.
   *Recovery:* the full key + all scores are on disk; the report regenerates from them.
8. **CS writes** `03_final-report.md` (the final scoring report): run facts + CS harness scores + anti-hallucination
   audit + the operator's verbatim eval + machine-readable summary block. *(Was the assistant's job; folded into CS under the operator
   override — CS already owns the scores + analysis. the assistant writes this ONLY as a crash-forensic report if the run
   failed.)* → STATUS: "Next: CS analyse". LB entry.
9. **CS analyses** → `05_analysis.md`: did Arm L beat Arm B (per-question Δ on the mean(CS,the operator) composite; win-count
   k/3 across the 3 questions)? Where do the operator + the harness agree/disagree (CS-vs-the operator plots)? If the loop improved,
   **promote** it to `loop-design/current/` + log `loop-design/CHANGELOG.md`.
   Append one row to `RESULTS-LOG.md`. Form the **next hypothesis**. → STATUS: "Next: run exp-002". LB entry.
   *Recovery:* analysis + promotion are files + CHANGELOG lines; the next experiment starts from STATUS.
10. **Start exp-002:** CS creates `experiments/exp-002_<slug>/` from `_TEMPLATE`, writes `00_hypothesis.md` (the change
    vs `loop-design/current`), and the cycle repeats from step 1.

**Crash-recovery invariants (locked):** (a) every handoff output is a file in the shared repo; (b) LABBOOK.md is
append-only and logs every step; (c) STATUS.md "Next action" always names WHO is next + WHAT; (d) the blank CC writes
incrementally (per-bundle, per-action) so partial progress survives; (e) scoring is idempotent (re-runnable from the
bundles); (f) the eval never depends on a fragile OS download (copy→paste to chat).

---

## 5. WHAT CS evaluates — full detail (this is CS's job; the operator does the science only)
CS's scoring harness (`01_setup/workspace/harness/`) scores **every answer, blinded to arm**, and this is the
experiment's measured result. Split:

### 5A. Grounding & citations — CS ONLY (protects the operator's rare time)
For each answer:
1. **Extract** every citation (PMID/DOI/title) → `citations.json`.
2. **Exist?** resolve each against PubMed/OpenAlex/Crossref. A citation that resolves to nothing = **fabricated** → flag.
3. **Used correctly?** LLM-entailment: does the cited paper actually support the *specific* claim it's attached to?
   Existence ≠ support (a real PMID on the wrong claim still fails). Misuse → flag.
4. **Right amount?** citation density vs the number of non-trivial claims — too few uncited claims = ungrounded.
5. **Quality? (NEW module — your explicit ask)** for each real citation: venue quality, **primary research vs review**
   (primary preferred for a mechanistic claim), recency, and a **retraction check**. A claim leaning on a review or a
   weak venue scores below one anchored in a strong primary paper.
→ These set the **Grounding** rubric dimension, with a hard cap: **no citations → Grounding ≤ 2; any fabricated →
Grounding ≤ 1** (a confident uncited/fabricated answer cannot score well no matter how fluent).

### 5B. Provenance verification — CS ONLY ("did it really happen"), ⟨LB-072⟩ blind-safe
CS verifies the answer's factual backbone from the **blinded deliverables** (`sources.md` + the claims in
`result.md`/`reasoning.md`): each cited connector/dataset/paper exists, the query/result is plausible, the referenced
data is real. Verified claims get a ✓ badge in the eval site so the operator trusts them without re-checking. This keys off the
answer content (both arms produce it), never a loop-phase trace — so it reveals nothing about the arm. *(The loop's
internal action log, §1a, is checked separately during the post-unblind loop audit.)*

### 5C. The 5-dimension rubric (1–5 anchored) → weighted composite
`grounding & integrity 0.20 · reasoning & soundness 0.20 · completeness 0.20 · usefulness 0.20 · creativity 0.20`
(equal weights, sum 1.0 — rubric v2, LB-075; supersedes the earlier 0.25/0.25/0.20/0.15/0.15 prior).
Scored by an **LLM reviewer-persona panel** (≥2 judges via `host.llm`, mimicking hackathon judges / journal reviewers),
**G-Eval style** (chain-of-thought + form-filling), **blinded to arm**, with **inter-judge agreement** tracked. This is
CS's mechanical mirror of what the operator judges by hand — the two are compared, not merged.
> **Lens scope (LB-032):** these judges are CS's *ruler* (set B) — reviewer personas capable of judging CS's output.
> They are NOT the loop-under-test's PI/postdoc/Codex lenses (set A, an improvement category). CS's side is Claude-only
> (no non-Claude judge); diversity comes from distinct personas/temperature; the operator is the human anchor. **Panel
> personas/count/format are PROVISIONAL — pending literature research + operator accept.**

### 5D. Creativity index — the open-question metric (mechanical)
`creativity = Novelty × Plausibility_gate × ReasoningTrace_gate` (multiplicative — any weak factor collapses it):
- **Novelty** = retrieval-frequency (how many prior-art papers match the core claim; **fewer hits = more novel**). Uses
  real connector counts, NOT naive lexical distance (which we showed fails to discriminate).
- **Plausibility_gate** = LLM plausibility rating (is the mechanism biologically sound?).
- **ReasoningTrace_gate** = is there a clear, **quotable** chain from established facts to the novel claim? A "novel"
  claim with **no derivable reasoning trace is scored down as candidate hallucination** — this is your "creativity must
  not be hallucination" principle, enforced mechanically.

### 5E. Elo head-to-head + the primary endpoint
- **Elo:** blinded pairwise judge comparisons across all answers per question → Elo ratings + ranking (drift-robust
  cross-check on the composite).
- **Primary endpoint (⟨LB-072⟩ 3 questions × 1 run each) — TWO complementary reads, both decide success:**
  1. **Mean-Δ across questions (effect size):** `Δ̄ = mean over the 3 questions of [composite(Arm L) − composite(Arm B)]`
     on the **combined mean(CS,the operator) composite** (§5F). This is the headline number — the average loop advantage. Report
     it with the spread of the 3 per-question Δ (min/max) so the reader sees consistency, not just the average.
  2. **Win-count k/3 (consistency):** on how many of the 3 questions did Arm L beat Arm B. `Δ̄>0 AND k=3` = strong;
     `Δ̄>0 AND k=2` = positive-but-inspect-the-loss; `Δ̄≈0 or k≤1` = null/negative (a real, reportable finding).
  - **Both together, not either alone:** the mean says *how much*, the win-count says *how reliably* — a big mean driven
    by one question (k=1) is a different story from a modest mean won 3/3, and we report both explicitly.
  - **Honest power caveat (stated in the report):** n=3 questions × 1 run is **descriptive, not inferential** — we do NOT
    claim statistical significance from 3 points. The strength of the result comes from the **breadth of per-dimension,
    per-scorer detail** (§5E-plots) being consistent, not from a p-value. *(Within-question replication + a real 3-way
    return at v8: baseline↔v7↔v8 on fresh same-category questions.)*
  - The **Elo ranking** (blinded pairwise, pooled per question) is the drift-robust cross-check on the composite.

**⟨LB-072⟩ Analysis outputs — broad, detailed, submission-grade (every score documented + plotted).** All of the
following are produced from `scorecard.csv` (one row per coded-answer × dimension × scorer) and saved under
`05_analysis/` + embedded in `03_final-report.md`:
- **Per-dimension arm comparison, plotted individually** — for EACH rubric dimension (grounding, correctness,
  completeness, usefulness, creativity) a grouped bar of Arm L vs Arm B, shown **three ways: CS scoring, the operator scoring,
  and combined mean** — so we can see *which arm scores best on which dimension under whose scoring* (exactly the view
  you asked for). = 5 dimensions × {CS, the operator, combined}.
- **Per-question composite** — Arm L vs Arm B for each of the 3 questions (combined mean), with the per-question Δ.
- **Mean-Δ + win-count summary** — the headline endpoint panel (Δ̄ across questions + k/3 + per-question Δ spread).
- **CS-vs-the operator agreement** — scatter of CS score vs the operator score per answer×dimension (+ per-dimension mean-difference),
  as an **instrument-calibration** result: where do my harness and the human expert agree/diverge. This is itself
  submission data (shows the scoring is trustworthy).
- **Creativity cross-check** — mechanical creativity index (§5D) vs the operator's creativity judgement, side by side.
- **Citation-quality panel** — existence/support rate, primary-vs-review ratio, venue quality, retraction count per arm.
- Every figure is publication-grade (figure-style); every underlying number ships as `scorecard.csv` + `analysis_tables.csv`
  so the plots are fully reproducible and auditable for the submission.

### 5F. The the operator ↔ CS scoring model (⟨LB-072⟩ AVERAGE, not override)
- **the operator (blinded, per coded answer `Em`, the SCIENCE):** the shared rubric dimensions he can judge — correctness ·
  completeness · usefulness · **creativity (as a scientist)** — each 1–5, + per-answer **creativity-honesty check** +
  per-answer **red flags** + per-answer **qualitative "what's weak / what would make it good"** (kept verbatim for the
  **v8-improvement input**). **No citation work** (that protects his rare time; citations are CS-only, 5A).
- **CS (harness, blinded to arm, per coded answer `Rn`):** everything in 5A–5E on the same rubric.
- **Reconciliation = MEAN, everything documented (supersedes the old "the operator overrides on divergence").** For each coded
  answer × shared dimension we store **three** numbers: `cs_score`, `human_score`, and `mean = (cs+operator)/2`. **All
  individual scores AND the means are persisted** (`scorecard.csv`, one row per answer×dim) so at the end we can **plot
  them against each other** — CS-vs-the operator agreement (scatter + per-dimension deltas) as an instrument-calibration result,
  and the **mean composite** as the headline per-arm number. Grounding/citation dims (CS-only) use the CS score
  directly (no the operator input to average). CS-only creativity **index** (5D, mechanical) stays reported **alongside**
  the operator's creativity judgement — the two cross-check, not merged.
- Both the individual CS + the operator scores AND the combined means are **submission data** (D2/D4); the **final populated
  eval site ships in the submission**.

### 5G. ⟨LB-072⟩ Double-blind via TWO independent keys (neither party alone can map answer→arm)
> **Canonical full statement:** `loop-design/current/blinding-protocol.md` (submission-grade: rationale, diagram,
> validity-under-blind, crash-recovery). This section is the operational summary; if the two disagree, the
> blinding-protocol doc + the labbook win.

The operator both **runs the arms** (knows folder→arm) and **does the human eval** — so a single relabeling cannot
blind the operator from their own knowledge. Two keys, held by two parties, break the chain twice:
1. **Key-1 (operator-held) blinds CS.** After the 6 runs the operator renames answer folders to a private shuffle
   `R1…R6` and keeps `{Rn → question,arm}`. CS receives only `R1…R6` → **CS scores blind.**
2. **Key-2 (CS-held) blinds the operator.** CS scores, then builds the eval site under a **fresh, independently
   shuffled** set `E1…E6`, keeping `{Em → Rn}` (`key2_eval_to_R.json`, never shown to the operator until unblind). The
   operator/the operator see codes `E1…E6` they have never encountered → **the human eval is blind.**
3. **Unblind needs BOTH keys.** `Em →(CS key) Rn →(operator key) arm`. Neither key alone maps an answer to an arm.
   The **mean(CS,the operator) is computed per coded answer BEFORE unblinding** (both scores key to `R`/`E`, not arm), so
   averaging never touches arm identity — unblinding only **attaches** arm labels for the final per-arm report.
- **Crash-recovery:** `key2_eval_to_R.json` is written the moment the eval site is generated (persistent, CS-side);
  `key1` lives with the operator; at unblind the operator pastes Key-1 → CS composes `blinding_key_FULL.json`
  (`Em→Rn→arm`). Every state is a file; re-runs are idempotent from the coded folders.
