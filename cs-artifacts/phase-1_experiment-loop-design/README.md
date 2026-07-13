<!-- WHAT THIS FOLDER IS: the Phase-1 provenance folder (ROADMAP Phase 1 = "CS designs the Experiment Loop"). It holds
     dated CS exports/snapshots for this phase AND this MANIFEST, which is the master index of EVERY file CS generated
     in Phase 1 across the repo, with generation times. HOW TO USE: this is the single "where is everything from Phase 1"
     view. Canonical living design specs stay in loop-design/current/ (the evolving product, per DOCUMENTATION §3 file map);
     this folder keeps dated provenance. The labbook (LB-012..LB-017) is the ground-truth history. Never edit a dated
     snapshot after saving. -->

# Phase 1 — CS designs the Experiment Loop — file manifest  [CS]

**Phase:** ROADMAP Phase 1. **Compiled:** 2026-07-09 (updated as Phase-1 files are added).
**Convention:** loose/provenance files = `YYYY-MM-DD_HHMM_<category>_<short-description>.<ext>` (DOCUMENTATION §6);
structural design specs keep their fixed names in `loop-design/current/`.

## A. Provenance exports held IN this folder (dated snapshots)
| File | Category | Generated | What it is |
|---|---|---|---|
| `2026-07-09_0130_report_cs-env-selfcheck.md` | report | 2026-07-09 01:30 (rev 08:46) | CS environment self-check (probed kernel: 8 CPU / 3.78 GiB / 2.72 GiB avail / no GPU / WSL2; full connector suite; €15 GPU final-only) |
| `2026-07-09_0130_protocol_cc-env-precheck.md` | protocol | 2026-07-09 01:30 | the paste-ready pre-check prompt handed to a blank Claude Code (Chrome control + Codex + runtime) |
| `2026-07-09_0826_report_cc-env-precheck.md` | report | 2026-07-09 08:26 | the blank-CC pre-check report (operator-relayed; CC kept isolated from the repo) |
| `2026-07-09_0914_artifact_experiment-loop-schematic.png` | artifact | 2026-07-09 09:14 | snapshot of the two-loop schematic (canonical: loop-design/current/experiment_loop.png) |
| `2026-07-09_0917_artifact_scorecard-mock.png` | artifact | 2026-07-09 09:17 | snapshot of the quantification scorecard mock (canonical: loop-design/current/scorecard_mock.png) |
| `2026-07-09_1030_artifact_creativity-worked-example.png` | artifact | 2026-07-09 10:30 | snapshot of the creativity worked-example figure (canonical: loop-design/current/creativity_worked_example.png) |
| `2026-07-09_1030_result_creativity-priorart-neighbors.json` | result | 2026-07-09 10:30 | REAL PubMed prior-art neighbours retrieved for the 4 worked-example hypotheses (provenance for novelty) |
| `2026-07-09_1030_result_creativity-reasoning-assessment.json` | result | 2026-07-09 10:30 | REAL panel plausibility + reasoning-trace scores for the worked-example hypotheses |
| `2026-07-09_1030_result_creativity-worked-scores.json` | result | 2026-07-09 10:30 | REAL composite creativity indices (N × plaus × reason) for the worked example |
| `2026-07-09_1140_note_operator-design-input.md` | note | 2026-07-09 11:40 | operator prior-experience findings A–G + CS design response (canonical: loop-design/current/operator-design-input.md; S-014) |
| `2026-07-09_1205_harness_the Metascience Project-scoring-harness.tar.gz` | harness | 2026-07-09 12:05 | the full scoring harness package (source: experiments/exp-001_.../01_setup/workspace/harness/); 13/13 dry-run asserts pass |
| `2026-07-09_1205_readme_harness.md` | readme | 2026-07-09 12:05 | harness README (design, dry-run, real-mode usage, entailment caveat) |
| `2026-07-09_1205_result_harness-dryrun-scorecard.csv` | result | 2026-07-09 12:05 | dry-run scorecard: trap answer scored lowest + Elo-last; good loop answers beat baseline Δ+1.28, arm-level (incl. trap) Δ+0.77 |

## B. Canonical living design specs (home = loop-design/current/, referenced here)
| File | Category | Generated | What it is |
|---|---|---|---|
| `loop-design/current/method-foundations.md` | note (methods) | 2026-07-09 09:02 | literature-grounded basis for every measurement choice (cites S-006..S-012) |
| `loop-design/current/experiment-loop-design.md` | note (design=D1) | 2026-07-09 09:06 | D1 — the Experiment-Loop design (arms, controls, test/baseline strategy, C1-C6, threats) |
| `loop-design/current/experiment_loop.png` | artifact | 2026-07-09 09:14 | the two-loop schematic figure |
| `loop-design/current/quantification.md` | note (methods) | 2026-07-09 09:17 | the 5-dimension quality metric + auto checks + judge panel |
| `loop-design/current/rubric.json` | note (machine spec) | 2026-07-09 09:17 | machine-readable rubric the scoring harness loads (5 anchored dims, weights sum 1.0) |
| `loop-design/current/scorecard_mock.png` | artifact | 2026-07-09 09:17 | illustrative scorecard the harness emits |
| `loop-design/current/creativity-metric.md` | note (methods) | 2026-07-09 10:30 | creativity = novelty × plausibility × reasoning-trace; anti-hallucination gate + REAL worked example |
| `loop-design/current/creativity_worked_example.png` | artifact | 2026-07-09 10:30 | the worked-example figure (H3 vs H3+: same novel idea, 3× apart on reasoning) |
| `loop-design/current/operator-design-input.md` | note (methods) | 2026-07-09 11:40 | operator findings A–G → Mission-Control architecture (S-014) |
| `experiments/exp-001_baseline-vs-v0-loop/01_setup/workspace/harness/` | harness | 2026-07-09 12:05 | the runnable + dry-run-verified scoring harness (canonical source location) |

## C. Test-set (home = test-sets/, control variable)
| File | Category | Generated | What it is |
|---|---|---|---|
| `test-sets/2026-07-09_testset_aging-v1/README.md` | testset | 2026-07-09 09:02 | 4 tiered seed questions (aging/metabolism/mito) + design rationale |
| `test-sets/2026-07-09_testset_aging-v1/request-to-operator.md` | note | 2026-07-09 09:03 | the concrete domain-input request to the operator (confirm/replace questions) |

## D. Still to come this phase (exp-001 package)
`experiments/exp-001_<slug>/00_hypothesis.md` + `01_setup/` (bootstrap, workspace incl. the runnable scoring harness,
protocol, test-set pin, for-the operator specs). Will be indexed here + logged in the labbook when produced.

---
*Sources registered for Phase 1: S-006..S-012 (see SOURCES.md). Labbook coverage: LB-012 (pre-check), LB-013
(constraints), LB-014 (methodology+test-set), LB-015 (D1), LB-016 (quantification), LB-017 (this manifest).*
