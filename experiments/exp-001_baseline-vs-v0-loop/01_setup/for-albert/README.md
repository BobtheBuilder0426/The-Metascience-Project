<!-- Authored by [CS]. Orientation for this folder AFTER the operator override (LB-032): the assistant is dropped from the
     critical path; CS owns capture→score→eval-prep→report→next; the operator is the A→B bridge. This folder is kept
     (name unchanged to avoid breaking references mid-experiment) but its tools are now CS-run, not the assistant-run. -->

# 01_setup/for-the operator/ — eval + report tooling  (now CS-run; the assistant = crash fallback only)

**Ownership change (operator override, LB-032 / dataflow-and-handoffs.md):** the assistant is no longer in the normal flow.
**CS** runs the scoring, generates the eval site, ingests the operator's result, and writes the final report. The **operator**
copies files between the isolated CC runtime and the repo. the assistant is summoned ONLY if the blank CC/CS loop crashes and CS
needs a blackbox forensic report. The files here keep their names so existing references don't break, but read them with
that ownership in mind.

| File | What it is | Now run by |
|---|---|---|
| `make_eval_site.py` | v2 generator: `answers.json` → blinded `eval_site.html` + `blinding_key.json` (per-answer science scores + honesty + red-flags + qualitative; markdown+figures+provenance timeline; copy-to-clipboard primary; retro-futuristic) | **CS** |
| `2026-07-09_1720_artifact_eval-site-DEMO-v2.html` | the DEMO the operator re-tests (open, score, click "Copy my evaluation", paste back) | operator tests |
| `demo_answers.json` / `demo_blinding_key.json` | demo inputs / true (hidden) A/B↔arm map | CS |
| `eval-sheet-template.md` | the eval categories/anchors, human-readable (the operator scores SCIENCE only; citations are CS's job) | CS ref |
| `final-report-spec.md` | the sections of the final scoring report — now **CS writes** `03_final-report.md` (was the assistant) | **CS** |
| `present-to-operator-skill.md` | how the eval is presented to the operator blinded — now the **CS** procedure (the operator evaluates in the CS tile / browser, copy-pastes back). Superseded framing: "the assistant-run CC skill." | **CS** |

**the operator ↔ CS split (locked, LB-032):** the operator judges the science (reasoning / completeness / usefulness / creativity +
per-answer honesty + red flags + qualitative "what's weak" + head-to-head). CS scores citations (amount / usage /
existence / QUALITY), provenance verification, the composite, the creativity index, and Elo.
