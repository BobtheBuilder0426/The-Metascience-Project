<!-- Authored by [CS] (scaffold, LB-094); FILLED by [CS2] to match the as-run experiment (LB-104, operator full permission
     2026-07-13). exp-003 RAN as a 2-arm showcase comparison (B vs L9); framing below reflects what was actually executed. -->

# exp-003 — Hypothesis (FINAL: T-cell Perturb-seq data test)  [CS scaffold / CS2 filled]  — RUN COMPLETE

## The experiment in one sentence
exp-003 is the **final** experiment: a translational **T-cell Perturb-seq data test** in which the loop under test
(**v9**) and a **blank-CS baseline** are given the same real genome-scale CD4+ T-cell Perturb-seq dataset (DOI-only,
under an explicit compute-caution) and the same question — identify a natural metabolite / nutraceutical to treat an
autoimmune disease of the arm's choice, argue it from the data, and design a pilot — each producing a single
publication-style **PDF report** submitted for external (hackathon-judge) evaluation.

## Nature of the experiment — SHOWCASE, not scored (operator ruling 2026-07-13, LB-104)
exp-003 is a **showcase comparison**, not a rubric-scored A/B test. Both arms' PDF reports go into the final submission
for the **hackathon judges** to compare and decide. There is therefore **no CS-side harness/rubric scoring, no
two-key double-blind, no the operator rubric pass** (that machinery was exp-002). This document records the demonstration
design and the honest claim under demonstration — not a measured endpoint.

## Arms (2 — operator ruling: "blank CS vs the final loop (v9)")
- **B** = baseline **blank CS** — project context = the safety preamble only (byte-identical to the loop's preamble;
  v9's preamble == v8's, verified). Run by pasting the guardrail into a CS project's Agent Context + the question into chat.
- **L9** = the **v9 loop** — `01_setup/v9_cc-bootstrap/` (v8 + the 3 surgical v9 edits: Gate-1 Codex critics on
  gpt-5.6-sol effort=high, Gate-2 reviewer effort=xhigh + hard multimodal precondition, reconnect procedure; see its
  `LOOP_VERSION.md`). Run by handing the v9 START PACKAGE to a blank Claude Code (bootstrap → intake question → drive).
- **Runs per arm: 1.** 1 question x 2 arms x 1 run = 2 answer-runs.

## Question (locked verbatim by operator, frozen-question rule — see `01_setup/test-set/questions.json`)
> *"Starting from this genome-scale CD4+ T-cell Perturb-seq dataset, identify a natural metabolite or nutraceutical that
> could be used to treat patients with an autoimmune disease of your choice. Present your results, methodology,
> scientific rationale, and an optimal pilot experiment to test your prediction."*
- Category 3 (translational data breakthrough). Operator supplied the text 2026-07-13; typo/grammar corrected with
  operator approval (`Perturb-seq`, `autoimmune`), meaning unchanged.
- **Dataset:** delivered **DOI-only** — https://doi.org/10.64898/2025.12.23.696273 (S-085) → the genome-scale CD4+
  T-cell Perturb-seq atlas (S-084; Marson lab; CZI VCM; GEO GSE314342; SRA SRP643211) — plus an explicit
  **compute-caution** ("dataset very large, small laptop — do not download/load raw; use processed/summary data").
  No files staged; the DOI + caution are byte-identical to both arms.
- **Output:** a single **PDF** publication-style report (replaced exp-002's presentation-folder format).

## What is being demonstrated (the honest claim, not a scored hypothesis)
- **Demonstration claim:** on a hard, real-data translational problem under a genuine compute constraint, the **v9 loop
  produces a more credible, better-grounded, and more epistemically self-critical report than a blank-CS baseline** —
  visible as explicit belief-ledgers, honest modality/limitation accounting, self-novelty checking against current
  literature, and a decisive falsifiable pilot.
- **Honest null:** both arms are capable Claude Science; the baseline may well produce an equally strong, publication-grade
  report, and on any single question the two may simply diverge to different-but-defensible answers. n=1 per arm on one
  question is a **demonstration, not a powered comparison** — no statistical claim is made or implied.

## Result (as run — full detail in `02_results/` + LB-104; not re-verified by CS2)
- **Arm B (blank CS):** IMPDH2 → **mycophenolic acid** (natural *Penicillium* metabolite) → **type-2 / eosinophilic asthma**.
- **Arm L9 (v9 loop):** PKM2 → **micheliolide** (feverfew sesquiterpene lactone; ACT001 prodrug) → **multiple sclerosis**.
- Same question + data → two different targets / diseases / natural products, both defensible; the v9 report carries
  visibly more epistemic-hygiene scaffolding (belief-ledger DATASET/LITERATURE/INFERENCE, a direction-of-effect table
  refusing to equate non-identical perturbation modalities, a self-novelty narrowing against a 2026 human MS study, a
  2x2 compound×CRISPRi falsifiable-interaction pilot). Both honoured the compute-caution (neither downloaded raw data).

## Fairness invariants (carried, non-negotiable)
- The question + dataset pointer (incl. compute-caution) + output-format block are delivered **byte-identical** to both
  arms; the loop only changes HOW the answer is pursued, never WHAT. Baseline gets the safety preamble only; the v9 loop
  may carry its composed context + Codex panel (allowed loop machinery — never enters the PDF deliverable, never seen by
  an evaluator). Blind-safety unchanged: no loop/process vocabulary in the deliverable.

## Status
**RUN COMPLETE.** v9 loop built + documented (LB-094); question + delivery locked and both arms executed (LB-104).
Deliverables in `02_results/`. Showcase — both PDFs feed the final submission for hackathon-judge evaluation.
