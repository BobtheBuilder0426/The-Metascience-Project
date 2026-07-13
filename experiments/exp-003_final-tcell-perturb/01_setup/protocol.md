<!-- Authored by [CS] (scaffold); FILLED by [CS2] to match the as-run experiment (LB-104, operator full permission
     2026-07-13). exp-003 RAN as a 2-arm showcase (B vs L9), DOI-only dataset + compute-caution, single-PDF output. -->

# exp-003 — Run Protocol (operator-facing)  [CS scaffold / CS2 filled]  — RUN COMPLETE

**Final experiment. Loop under test: `v9_cc-bootstrap`.** 2 arms (**B** blank CS vs **L9** v9 loop), 1 question, 1 run
per arm = **2 answer-runs**. Showcase comparison — both PDF reports feed the final submission for hackathon-judge
evaluation (no CS-side rubric scoring / no two-key blind; operator ruling 2026-07-13, LB-104).

## The arms — how each was run
- **Arm B (baseline blank CS).** A fresh Claude Science project; Agent Context = the **safety preamble only** (the
  byte-identical guardrail; v9's preamble == v8's, verified). The operator pastes the guardrail (see
  `run-packs/arm-B-baseline/…PROJECT-CONTEXT.md`), then pastes the question block into chat. One response; no loop.
- **Arm L9 (v9 loop).** The `v9_cc-bootstrap` START PACKAGE is handed to a blank Claude Code: `Read CLAUDE.md and
  bootstrap your workspace.` → answer one-time setup → paste the **identical** question block as the research question
  → give a run NAME → the bootstrap creates the CS project + prints a START PROMPT that a second blank CC runs to drive
  the loop. Shared v7/v8 machinery + the v9 edits: Gate-1 Codex critics on gpt-5.6-sol effort=HIGH; Gate-2 reviewer on
  gpt-5.6-sol effort=XHIGH with mandatory multimodal figure + file ingestion; CS reconnect procedure for both CC roles.

## Delivered prompt (fairness lock)
Both arms receive, **byte-identical**: `question.text + "\n\n" + dataset_pointer + "\n\n" + output_format_instruction`
(see `test-set/questions.json`). Concretely the shared block is:
1. **Question (verbatim):** *"Starting from this genome-scale CD4+ T-cell Perturb-seq dataset, identify a natural
   metabolite or nutraceutical that could be used to treat patients with an autoimmune disease of your choice. Present
   your results, methodology, scientific rationale, and an optimal pilot experiment to test your prediction."*
2. **Dataset pointer + compute-caution:** DOI https://doi.org/10.64898/2025.12.23.696273 (S-084/S-085) + "the full
   dataset is very large and you are running on a small laptop with limited compute — do not download/load the raw
   dataset; work from a tractable subset or the paper's processed / summary data."
3. **Output format:** a single **PDF**, publication-style report (title; ≤150-word abstract; rationale; methodology;
   results; pilot; embedded labelled figures/tables; references with PMID/DOI/accession).

## Dataset delivery — DOI-only (operator ruling 2026-07-13)
**No files staged** in `materials/`. Both arms receive the identical DOI + compute-caution inside the prompt; each
decides how to access a tractable slice (both, in fact, streamed the processed DE tensor `GWCD4i.DE_stats.h5ad` rather
than downloading the ~1.8 TB of raw cell-level data — LB-104). This keeps delivery byte-identical while respecting the
laptop's limits. (An alternative — staging the author CSV supp tables ~15 MB — was considered and set aside for DOI-only.)

## Output + collection
Each arm delivers a single **PDF** report into its own granted folder (baseline: its dedicated CS folder via the
delivery stanza; L9: its `AL-<name>` run folder via the bridge). Collected under `02_results/`:
- `presentation CS blank T-cell perturb/` — Arm B (`report.pdf` + HTML + 3 figs).
- `presentation v9 loop T-cell perturb/` — Arm L9 (`report.pdf` + `result.md`/`reasoning.md`/`sources.md`/`process_trace.json`/`figures/`).

## Evaluation — showcase (no rubric scoring)
exp-003 is judged **externally by the hackathon judges** from the two PDFs. There is deliberately **no** CS harness
scoring, no rubric composite, no two-key double-blind, and no the operator rubric pass here (that was exp-002). CS2's role was
to review + document the deliverables (LB-104), not to score them.

## Fairness invariants (carried, non-negotiable)
Question + dataset pointer (incl. compute-caution) + output-format delivered byte-identical to both arms; the loop
changes only HOW, never WHAT. Baseline gets the safety preamble only; the v9 loop may carry its composed context + Codex
panel (loop machinery — never enters the PDF deliverable, never seen by an evaluator). Blind-safety: no loop/process
vocabulary in the deliverable.

## Status
**RUN COMPLETE** (both arms delivered; LB-104). Deliverables in `02_results/`; both PDFs feed the final submission.
