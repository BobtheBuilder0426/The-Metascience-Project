# exp-003 — FINAL experiment: T-cell perturbation data test

<!-- Authored by [CS] (scaffold, LB-094); FILLED to as-run state by [CS2] (LB-104, operator full permission 2026-07-13).
     exp-003 RAN as a 2-arm showcase: B (blank CS) vs L9 (v9 loop), one question, single-PDF output, DOI-only dataset. -->

**Status: RUN COMPLETE — both arms delivered (LB-104).** This is the **final** experiment: a translational
**T-cell Perturb-seq data test**. The loop under test is **v9** (`01_setup/v9_cc-bootstrap`), a clean copy of exp-002's
v8 loop plus three surgical edits — built in this same setup task; its content hash + the full v8→v9 diff are recorded
in `01_setup/v9_cc-bootstrap/LOOP_VERSION.md`. Deliverables are in `02_results/`; it is a **showcase comparison** — both
PDF reports feed the final submission for the **hackathon judges** to evaluate (no CS-side rubric scoring, no two-key
blind; operator ruling 2026-07-13).

**Result in one line:** same question + data → Arm B (blank CS) nominated **IMPDH2 → mycophenolic acid → eosinophilic
asthma**; Arm L9 (v9 loop) nominated **PKM2 → micheliolide → multiple sclerosis** — both defensible; the v9 report
carries visibly more epistemic-hygiene scaffolding (belief-ledger, modality table, self-novelty check, falsifiable
pilot). Not re-verified by CS2 (LB-104).

## What this experiment is
A real-data test in which the loop (and the baseline) are asked to analyse / reason over a **T-cell perturbation
dataset** the operator will provide, and produce a novel, grounded, well-argued result in the standard presentation
format. It closes the submission's arc: baseline → v7 loop → v8 loop → **v9 loop on a hard real-data problem**.

## The loop under test — v9 (what changed vs v8)
`01_setup/v9_cc-bootstrap/` is v8 (`content hash 331d802b219b4e69`) copied clean, then extended to **v9
`content hash c92973d8a3bbc5e9`** (28 files). The operator requested **three** surgical changes; because the Codex
model/effort change applies per-gate, `LOOP_VERSION.md` documents them as **four edits** (EDIT 1 = Gate-1 effort,
EDIT 2 = Gate-2 effort, EDIT 3 = Gate-2 multimodal precondition, EDIT 4 = reconnect). The three changes:
1. **Gate-1 Codex critics** (4 lenses + chairman) run on **gpt-5.6-sol, reasoning effort HIGH** *(= EDIT 1)*.
2. **Gate-2 Codex reviewer** (journal referee) runs on **gpt-5.6-sol, reasoning effort XHIGH** *(= EDIT 2)*, and
   **must** receive CS's rendered figures/images (attached with `-i`, multimodal) **and** read CS's deliverable files —
   a hard, pre-flight-verified precondition (the IMAGE_TOKEN / BOXES / FILE_TOKEN probe), not a soft "if available"
   *(= EDIT 3)*.
3. **A Claude-Science reconnect procedure** so both CC roles (bootstrap + driver) can recover a dead/expired CS session
   on their own (fresh single-use login link; daemon force-start) *(= EDIT 4)*.
Everything else is byte-identical to v8. See `LOOP_VERSION.md` for the full diff + the new content hash.

## Folder map (standard 00–05)
- `00_hypothesis.md` — the exp-003 framing + arms + honest demonstration claim. **FILLED (as-run).**
- `01_setup/protocol.md` — how each arm was run + the delivery/fairness contract. **FILLED (as-run).**
- `01_setup/test-set/` — the locked question (`questions.json`, READY) + `materials/` (DOI-only; no files staged). **LOCKED.**
- `01_setup/v9_cc-bootstrap/` — **the loop under test** (v8 copied clean + the 3 v9 edits; `LOOP_VERSION.md` records
  the version name, content hash, and the v8→v9 diff).
- `02_results/` — the two delivered presentation folders (Arm B + Arm L9). **DELIVERED.**
- `04_evaluation/` — n/a for exp-003 (showcase; judged externally, not via the blind eval site).
- `05_analysis/` — n/a for exp-003 (no CS rubric scoring). `03_final-report.md` — cross-experiment writeup (submission wrap-up).

## What actually ran (operator rulings 2026-07-13, LB-104)
1. **Dataset — DOI-only + compute-caution.** No files staged; the DOI (S-084/S-085) + caution were delivered
   byte-identical inside the prompt. Both arms streamed the processed DE tensor rather than downloading raw data.
2. **Question — locked verbatim** (frozen-question rule) in `01_setup/test-set/questions.json` (READY).
3. **Arms — B (blank CS) vs L9 (v9 loop)**, 1 run each = 2 answer-runs.
4. **Output — a single PDF** publication-style report per arm (replaced the presentation-folder format).
5. **Evaluation — showcase**, judged externally by the hackathon judges; no CS rubric scoring / no two-key blind.

## Shared infrastructure
- The v9 loop reuses the v7/v8 machinery + the 3 v9 edits (see `LOOP_VERSION.md`). Because exp-003 is a showcase, the
  scoring harness + two-key double-blind used in exp-001/002 are **not** applied here.

## Provenance
Loop version: **v9_cc-bootstrap** — see `01_setup/v9_cc-bootstrap/LOOP_VERSION.md` for its content hash + the v8→v9
diff. Created + documented in the labbook entry that accompanies this folder.
