<!-- Authored by [CS] for exp-001. The OPERATOR-facing run protocol (two-session model). Rewritten by LB-074 to match the
     locked design: 3 questions × 1 run = 6, output-format-in-the-question, presentation folder, mean(CS,the operator) scoring,
     two-key double-blind. Canonical companions (if anything disagrees, these + the labbook win):
       • loop-design/current/dataflow-and-handoffs.md      (outputs, paths, handoffs, scoring §5, blind §5G)
       • loop-design/current/blinding-protocol.md          (the two-key double-blind method)
       • loop-design/current/output-format-instruction.md  (the block appended to every question) -->

# exp-001 — Run Protocol (operator-facing)  [CS-authored]

exp-001 runs **3 questions**, and for EACH produces answers from two arms so they can be compared. **Both arms start
from the SAME naive question — the exact plain-language string a curious scientist would type, byte-identical** (plus,
for Q_ERGO, the same two PDFs), **with the identical output-format instruction appended** (see
`loop-design/current/output-format-instruction.md`). The arms differ ONLY in the machinery behind that question:
- **Arm B (baseline) — LOCKED:** the naive question → a **blank Claude Science session** → **one** response. No loop, no
  reframe, no plan-review, no multi-phase driving. The operator pastes the question (+ Q_ERGO PDFs), captures the single
  answer, adds nothing. This is what any scientist gets by pasting the question into CS today; GOAL D4's "blank-CS" control.
- **Arm L (loop) — LOCKED:** the **same** naive question → a **blank Claude Code given the whole `v7_cc-bootstrap`
  folder** as its workspace. The blank CC self-bootstraps (pre-flight, bridge, PDF-digest, CS project creation), then its
  **driver** reframes the question itself (STEP 0) and drives CS through the loop → final answer. Everything Arm L needs
  is inside `v7_cc-bootstrap/`; this protocol does not re-describe it. Loop version = whatever the bootstrap folder is
  (here **v7**); the `v0-loop` in the folder slug is legacy naming for "the first loop we test."

**Fairness invariant:** the human-typed input is byte-identical across arms; every output difference is attributable to
the loop machinery, not to a better-worded prompt. Arm L's reframed brief is saved in the driver's **`run_log/`** (NOT in
the evaluated folder) — the audit trail that it enriched only the *approach*, not the *question asked*.

**Design: 3 questions × 2 arms × 1 run = 6 answer-runs** (LB-072). Success = mean-Δ across the 3 questions AND win-count
k/3 on the combined mean(CS,the operator) composite; n=3×1 is descriptive, not a powered study (see `00_hypothesis.md`).

**Test-set:** the 3 questions in `test-set/README.md` / `questions.json` (test-set version pinned there). **Q_ERGO**
(category 1: ingest given papers → hypothesis + experiment) and **Q3** (category 3: translational repurposing) are LOCKED;
the **category-2 question (big-think new hypothesis) is PENDING operator lock.** Use each question's wording **verbatim
and identically** across its arms — the core fairness rule. Do not paraphrase, expand, or add hints to either arm. The
output-format instruction is part of that verbatim wording and is identical for both arms.

**SHARED MATERIALS (Q_ERGO only):** the two ergothioneine PDFs **must be attached, identical, to BOTH arms of Q_ERGO** —
the question's starting material, given equally. (Arm L digests them via its own PDF-digest subagent; Arm B gets them
attached to the CS session.) The other two questions have no attached materials.

## Output — the PRESENTATION FOLDER (identical shape for both arms)
Each answer-run produces ONE **presentation folder** whose shape is set by the question's output-format instruction, NOT
by the loop: `result.md` + `reasoning.md` + `figures/` + `sources.md` + `process_trace.json`. Because the format lives in
the question, both arms produce the same files; only *how well* differs.
- **Arm B:** the operator captures CS's single response into that folder shape.
- **Arm L:** the driver has CS write `OUTPUT/run-01/presentation/` (the evaluated folder) with a sibling
  `OUTPUT/run-01/run_log/` (loop machinery — reframed brief, phase log, RUN_REPORT — **never evaluated**).
- **`process_trace.json` is ACTION-labelled, never phase-labelled** (blind-safety, enforced in the v7 driver): it records
  what CS actually did, so CS can score provenance without the trace revealing which arm produced it.
- **No self-scoring.** Neither arm rates/grades/scores its own answer on any scale — scoring is done later by CS + the operator.
  (The v7 driver's INTEGRATE step produces the answer + factual capture only; the self-scorecard was removed, LB-070.)

## Running the two arms
- **Arm B (baseline):** open a **new** CS project; paste the `CS_PROJECT_PREAMBLE.md` safety preamble into its Agent
  Context (fill the `⟨INSERT HERE⟩` slot with the project name+address); for Q_ERGO attach the two PDFs first; send CS
  **exactly** the question text (naive question + appended output-format instruction) and nothing else. Capture the one
  response into the presentation-folder shape.
- **Arm L (loop):** hand a **blank CC** the `v7_cc-bootstrap` folder as its workspace and start it per that folder's
  `START_HERE.md`. It self-bootstraps and, at its intake step, receives the same naive question (+ the same output-format
  instruction) and any Q_ERGO PDFs. It drives the loop and writes its `presentation/` folder.
- Each run uses a **fresh CS session** (prevents context leaking between runs/arms). Arm L uses the CS project the
  bootstrap created (e.g. `AL-run-NN`), with the **same** safety preamble bytes as Arm B (only the run-specific
  name/address differs).

## Blinding — the operator's two-key duty (see blinding-protocol.md)
After the 6 runs, **before** handing anything to CS for scoring:
1. **Rename** the 6 presentation folders to a **private random shuffle `R1…R6`** and keep the map `{Rn → (question,arm)}`
   — this is **Key-1, held by YOU (operator)**; do NOT give it to CS until unblinding. Copy the arm-stripped `R1…R6/`
   into `02_results/`.
2. CS scores `R1…R6` blind, builds the eval site under its own independent shuffle `E1…E6` (Key-2, CS-held), the operator scores
   blind, means are computed — all before any arm label is attached.
3. **Unblind** only at the end, when you paste Key-1 and CS composes `Em→Rn→arm`. Neither key alone deanonymizes an arm.
This two-key double-blind is a demonstrated method of the submission.

## Documentation + report (Arm L, produced by the driver)
The driver keeps `run_log/run_log.md` (per-action + phase timings) and a `run_log/RUN_REPORT.md` (short blackbox: what
happened each phase, where CS did well/struggled, human touches, total time, a plain fairness attestation that wording
was byte-identical across arms and Arm B got no loop help). These live in `run_log/`, **out of the evaluated set**, read
only after unblinding. Arm B's capture is trivial (one response) and needs no such log.

## What CS does with the runs (the contract)
CS scores all 6 presentation folders **blind (on `R1…R6`)** with the Metascience Project harness (5-dimension rubric via the reviewer
panel + citation verification & QUALITY + creativity gate + Elo) and verifies each `process_trace.json` step really
happened. the operator scores blind on `E1…E6`; per answer×dimension CS keeps **cs_score, human_score, and their mean**. The
experiment asks: **does Arm L beat Arm B on the combined mean composite — by how much (mean-Δ across the 3 questions) and
how reliably (win-count k/3)?** Faithful runs + honest action-traces are what make that measurement trustworthy.

