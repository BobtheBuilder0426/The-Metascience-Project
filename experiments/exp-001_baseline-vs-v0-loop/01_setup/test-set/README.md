<!-- Authored by [CS] for exp-001. This is the PINNED, self-contained question the blank CC uses. It is a frozen copy of
     one question from test-sets/2026-07-09_testset_aging-v1 — pinned so the run is reproducible even if the master
     test-set evolves. The blank CC needs ONLY this file. -->

# exp-001 — Pinned test-set  [CS-authored]

- **Test-set source:** `test-sets/2026-07-09_testset_aging-v1` (aging / metabolism / mitochondria)
- **Test-set version pinned:** aging-v1
- **Status: LOCKED by operator** — Q_ERGO + Q3 locked 2026-07-09 (LB-026); **Q2 added + all three question texts
  refined & locked 2026-07-10 (LB-076).** The three questions below are final for exp-001. The run is gated only on
  environment/execution readiness + the Tier-3 harness migration, not on further question confirmation.
- **Questions selected for exp-001: THREE — one per category (LB-074):**
  - **Q_ERGO (category 1 — day-in-the-lab, operator must-have, PROVIDES MATERIALS):** ingest two given ergothioneine
    papers → a new rationale/hypothesis for the exercise-performance effect + a first pilot experiment. Connectors:
    PubMed / OpenAlex / Open Targets / ChEMBL / UniProt / Reactome / STRING / GEO / AlphaFold.
  - **Q2 (category 2 — maximum-creativity big-think, NO materials):** generate a novel, plausible origin-of-life
    hypothesis (abiogenesis → first self-replicating cell). Pure hypothesis generation + argument; no expected
    wet-lab test (rubric test-clause is conditional). Connectors: PubMed / OpenAlex / bioRxiv / UniProt / Reactome.
  - **Q3 (category 3 — translational data breakthrough):** from public datasets, propose a not-thought-of-yet/new
    compound as an exercise mimetic against sarcopenia / age-related muscle loss. Connectors: ChEMBL / openFDA /
    Open Targets / PubMed / ClinicalTrials / Reactome.
  - Q_ERGO + Q3 are in the operator's core expertise; Q2 is deliberately outside the aging-metabolism zone (novelty ≠ retrieval).
- **Design:** 3 questions × 2 arms (B, L) × **1 run** = **6 answer-runs** (2 per question). Run each question fully
  (both arms) before moving to the next. (The 3-way baseline↔v7↔v8 with within-question replication returns at v8.)
- **Output format:** each question's delivered prompt = the naive question text below **+** the output-format
  instruction (the "presentation folder" block). The **machine-delivered copy** is `questions.json` →
  `output_format_instruction` (plain prose); `../../../loop-design/current/output-format-instruction.md` is the
  human-readable spec of the same wording (with markdown emphasis for reading). The appended string is **byte-identical
  between the two arms** (the fairness invariant) — that is what "identical" guarantees here, not byte-identity with the
  markdown spec file.

## ⚠ SHARED MATERIALS for Q_ERGO (must reach BOTH arms, identical)
Q_ERGO starts from **two publications**, provided in `materials/` (also copied to `../workspace/materials/`):
- `Ergothioneine_CSE_Petrovic_2025_CellMetab.pdf` — Petrovic et al. 2025, *Cell Metab* 37:542–556 (S-015): EGT → CSE
  persulfidation → cGPDH → NAD⁺ boost → healthspan/performance in aged *C. elegans* + rats.
- `Ergothioneine_MPST_Sprenger_2025_CellMetab.pdf` — Sprenger et al. 2025, *Cell Metab* 37:857–869 (S-016): EGT
  accumulates in muscle mitochondria with training, binds+activates MPST; EGT–MPST axis controls mito function +
  exercise performance.

**Both PDFs must be attached, identical, to BOTH the Arm-B (blank CS) and Arm-L (CC/CS loop) runs of Q_ERGO.** They are
the *starting point* of the question, not loop assistance — so giving them to the baseline does NOT break fairness (the
loop is still the only difference). Q3 has no shared materials.

## ►► RUN THESE ◄◄  (use each EXACT wording, byte-identical, for BOTH arms of that question)

Each delivered prompt = the question text below **+** the output-format instruction block (appended byte-identical,
both arms — see foot of this section).

**Q_ERGO — category 1 (attach the two PDFs above):**
> **Starting from the two provided publications about ergothioneine, come up with a new rationale/hypothesis of how
> ergothioneine makes those mice and rats run faster / increases their exercise performance. What would be your first
> pilot experiment to test this hypothesis?**

**Q2 — category 2 (no materials):**
> **Generate a novel, plausible hypothesis for: How did a soup of lifeless organic molecules spontaneously organize
> into the first self-replicating cell?**

**Q3 — category 3 (no materials):**
> **Starting from publicly available datasets, propose a not-thought-of-yet or new compound that acts as an exercise
> mimetic to treat patients against age-related muscle loss and sarcopenia.**

**Output-format instruction — appended VERBATIM to each of the three above, byte-identical, for BOTH arms:**
> How to present your results. Please hand back your answer as a small presentation folder containing: `result.md` —
> your final answer and the case for it; `reasoning.md` — the line of thought that got you there; a `figures/` folder
> with any plots, tables, or other artefacts you produced, each clearly labelled; `sources.md` — every source you drew
> on, with identifiers; and `process_trace.json` — a step-by-step record of what you actually did to reach the answer.

Do not paraphrase, shorten, or add hints. For each question, Arm B (baseline) gets that combined string (plus, for
Q_ERGO, the two PDFs) and nothing else — **no loop framing**; Arm L (loop) gets the same combined string (and same PDFs)
inside the loop's Frame phase. The machine-readable copies are in `questions.json`.

## Why word-identical matters
The whole experiment is "same question, two ways" — the only permitted difference between Arm B and Arm L is the loop,
never the question. Any wording drift confounds the result.
