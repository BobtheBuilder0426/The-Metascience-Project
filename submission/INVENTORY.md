# Repository inventory

**What this is.** An annotated map of the whole repository: for every top-level item —
what it is, why it exists, and whether it should **ship** in the public submission. Trash
and duplicates are flagged with paths so the maintainer can remove them in the final
scrub. Sizes and counts are measured from the working tree (see
`submission/evidence/checksums.sha256` for hashes of the authoritative data files).

**Ship legend:** ✅ ships · ➖ optional / provenance (ship if space) · ❌ trash — remove ·
🔁 duplicate — keep one copy.

**Scale:** ~727 files, ~183 MB in the working tree. The bulk is (a) staged literature PDFs
(~73 MB in `resources/`, re-staged per experiment) and (b) two large offline eval-site HTML
files with base64-embedded figures (~17 MB). Neither is needed to *read* the result; both
are provenance. The scientific record is small and text-first.

---

## Root files

| Path | What / why | Ships |
|---|---|---|
| `README.md` | The judge entry point (D-F): what this is, what happened, and a table routing to every deliverable. | ✅ |
| `LICENSE` | Clean OSI MIT text (D-E), copyright "The Metascience Project", 2026. | ✅ |
| `LABBOOK.md` | Append-only ground-truth log, LB-001→LB-106 (425 KB). The central source of truth; every claim traces here. | ✅ |
| `SOURCES.md` | Registered source spine S-001→S-085 (PMIDs/DOIs/accessions). Cited by number throughout. | ✅ |
| `GOAL.md` | Locked research goal (Northstar + Sections 1–6). | ✅ |
| `DOCUMENTATION.md` | How the repo is organized (file-map + documentation-duty matrix). | ✅ |
| `ROADMAP.md` | Phase plan. | ➖ |
| `STATUS.md` | Live working-state baton (44 KB). Internal handoff notes; not a judge deliverable. | ➖ |
| `CLAUDE.md` | Start-here / read-order pointer for the driving agent. | ➖ |
| `Hackathon.md` | The competition brief (deadline, judging weights, prizes). Contains submission-platform details. | ➖ (internal reference) |

## `submission/` — the judge-facing deliverables (this build)

| Path | What / why | Ships |
|---|---|---|
| `submission/ACCEPTANCE_MATRIX.md` | The 7-deliverable contract + canonical layout + conflict-precedence rule. | ✅ |
| `submission/INVENTORY.md` | This file (D-A.1). | ✅ |
| `submission/TIMELINE.md` | Labbook-anchored timeline (D-A.2). | ✅ |
| `submission/EVAL_DESIGN_AUDIT.md` | Evaluation-design audit grounding Methods/Results. | ✅ |
| `submission/summary.md` | 100–200 word summary (D-C). | ✅ |
| `submission/evidence/` | Frozen evidence spine: `checksums.sha256`, `build_spine.py`, `evidence_spine.csv`, `derived_numbers.json`. Single source of truth for every number. | ✅ |
| `submission/report/report.pdf` | The report (D-B). | ✅ |
| `submission/report/verification_ledger.csv` | Every shipping claim → source ID, live-checked (D-B). | ✅ |
| `submission/report/figures/` | Paper figures (SVG masters + PNG/PDF). | ✅ |
| `submission/report/src/` | Report source + build. | ➖ (provenance) |
| `submission/talk-figures/` | Five talk figures (D-D). | ✅ |
| `submission/submission-checklist.md` | Pre-existing build-time checklist. Working file, not a deliverable. | ➖ |

## `experiments/` — the scientific record (108 MB, 646 files)

One folder per experiment, stages `00_hypothesis` → `05_analysis`. **This is the core of the
submission.**

| Path | What / why | Ships |
|---|---|---|
| `experiments/_TEMPLATE/` | The stage-00→05 skeleton every experiment follows. | ✅ (shows method) |
| `experiments/exp-000_pilot_ergo-disease/` | The pilot that hardened the CC bootstrap (v1→v6). Holds `cc-bootstrap-archive/` (**35 MB** — 9 CLAUDE.md loop versions + history snapshots, incl. triple-staged PDFs). | ✅ folder; ➖ the 35 MB archive (provenance — keep compressed or trim staged PDFs) |
| `experiments/exp-001_baseline-vs-v0-loop/` | First controlled comparison: baseline vs **v7** loop (folder slug says `v0-loop` — **naming drift**; the loop under test was `v7_cc-bootstrap`). `05_analysis/` holds the frozen result. | ✅ |
| `experiments/exp-002_baseline-vs-v7-vs-v8/` | The headline 3-arm experiment (B/v7/v8). `05_analysis/figs_final/` + `FINAL_RESULT.md` are the result of record. | ✅ |
| `experiments/exp-003_final-tcell-perturb/` | The final showcase (baseline vs v9) on the T-cell Perturb-seq dataset; two side-by-side PDF reports. | ✅ |

**Key result files (authoritative, checksummed):**
`exp-001/05_analysis/{FINAL_RESULT.md, analysis_tables.csv, scorecard_long_unblind.csv, blinding_key_FULL.json}`;
`exp-002/FINAL_RESULT.md` + `exp-002/05_analysis/{master_3arm.csv, final_3arm_summary.json, table_*_by_arm.csv, figs_final/fig{1..4}}` + `exp-002/04_evaluation/{blinding_key_FULL.json, human_eval.json}`;
`exp-003/02_results/{presentation CS blank…, presentation v9 loop…}` (the two reports).

## `loop-design/` — the Agentic Loop design record (764 KB, 40 files)

| Path | What / why | Ships |
|---|---|---|
| `loop-design/current/` | The current design docs: `experiment-loop-design.md`, `quantification.md`, `rubric.json`, `creativity-metric.md`, `reviewer-panel-design.md`, `dataflow-and-handoffs.md`, `blinding-protocol.md` + schematic PNGs. | ✅ |
| `loop-design/future/` | Deferred modules (e.g. multi-model lit-synthesis SPEC) — shelved, documented as future work. | ➖ |
| `loop-design/CHANGELOG.md` | **Empty template.** The real version story lives in each `LOOP_VERSION.md` + the labbook. | ❌ (empty — remove or fill) |

## `resources/` — inbound knowledge (73 MB, 14 files)

| Path | What / why | Ships |
|---|---|---|
| `resources/papers/` | The 4 starter papers + the exp-input papers (PDFs, ~73 MB). | 🔁 See duplication note below |
| `resources/RESOURCES.md`, `claude-science-handbook.md` | Machine/capability specs + CS handbook. | ➖ |

## `cs-artifacts/`, `final-run/`, `test-sets/`

| Path | What / why | Ships |
|---|---|---|
| `cs-artifacts/phase-1_experiment-loop-design/` | Early phase-1 design artifacts (488 KB). | ➖ (superseded by `loop-design/current/`) |
| `final-run/` | **Only a README (8 KB)** — the "final run" was realized as exp-003, not a separate folder. | ➖ (stub — README should point to exp-003) |
| `test-sets/2026-07-09_testset_aging-v1/` | The aging-v1 test-set definition. | ✅ |

---

## Trash to remove (final scrub)

| Pattern | Count | Action |
|---|---|---|
| `*:Zone.Identifier` (Windows mark-of-the-web stubs) | **56** | ❌ delete all |
| `__pycache__/`, `*.pyc`, `.DS_Store`, empty `.gitkeep` | **31** | ❌ delete all |
| `loop-design/CHANGELOG.md` (empty template) | 1 | ❌ remove or fill |

## Duplicates (keep one copy)

| Item | Copies | Keep |
|---|---|---|
| `exp-002/_view_001_fig1_arm_by_scorer.png` (121 KB) vs `exp-002/05_analysis/figs_final/fig1_arm_by_scorer.png` | 2 | 🔁 keep `figs_final/` (the canonical analysis output); the root `_view_*` is a scratch preview |
| Starter/input PDFs staged in `resources/papers/` **and** each experiment's `01_setup/test-set/materials/` **and** the `exp-000/…/cc-bootstrap-archive/` (v1–v5, v6.0, v6.1) | up to 4× each (e.g. the two ergothioneine PDFs at 5.7–5.8 MB appear 4 times) | 🔁 keep `resources/papers/` as the canonical library; the per-experiment `materials/` copies are the *as-run* staged inputs (legitimate provenance — keep if reproducibility matters, else symlink); the **archive triple-copies are removable** |
| `eval_site.html` — `exp-001` (5.0 MB) + `exp-002` (12 MB), base64-embedded figures | 2 large files | ➖ provenance only; not needed to read results — exclude from a size-limited archive |

**Net:** removing the 56 Zone.Identifier + 31 other trash files, the empty CHANGELOG, the
one scratch PNG, and the archive PDF triple-copies reclaims most of the avoidable weight
without touching the scientific record. The two `eval_site.html` files and the `resources/`
PDF library are the only remaining large items, both provenance.
