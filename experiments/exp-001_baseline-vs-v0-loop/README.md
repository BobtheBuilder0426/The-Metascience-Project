# exp-001 — baseline (blank CS) vs the v7 Agentic Loop  [CS]

<!-- WHAT THIS FOLDER IS: the FIRST comparison experiment. Measures whether the CC-driven v7 loop beats a raw blank-CS
     baseline on the same questions. Crash-recovery-proof: every state is a file + a labbook entry; STATUS.md "Next
     action" is the baton. Canonical end-to-end spec = ../../loop-design/current/dataflow-and-handoffs.md (if anything
     here disagrees, that doc + the labbook win). -->

## What this experiment measures
Does a blank Claude Code **driving Claude Science through the v7 Agentic Loop** (Arm L) produce better answers than a
**raw blank Claude Science** given the identical question (Arm B)? Same start prompt to both; the only difference is the
loop. **Loop of record = `01_setup/v7_cc-bootstrap/`** (content hash `1b94b20a94245fae`, LB-074).

## Design (locked, LB-072/074/076)
- **3 questions, one per category:** Q_ERGO (cat-1 day-in-lab, ships 2 PDFs) · Q2 (cat-2 big-think origin-of-life) ·
  Q3 (cat-3 translational). Each = naive text **+** the appended presentation-folder output-format instruction,
  byte-identical between arms.
- **6 answer-runs** = 3 questions × 2 arms (B, L) × 1 run.
- **Scoring:** 5-dimension rubric v2 at **equal 0.20** (grounding & integrity · reasoning & soundness · completeness ·
  usefulness · creativity), scored by the CS harness **and** the operator; `combined = mean(CS, the operator)` per answer × dimension.
- **Primary endpoint:** mean-Δ (Arm L − Arm B) across the 3 questions **and** win-count k/3, on the combined composite.
  n=3×1 is descriptive, not inferential.
- **Two-key double-blind:** operator-held Key-1 (`Rn→question,arm`) blinds CS; CS-held Key-2 (`Em→Rn`) blinds the operator.
  Full spec: `../../loop-design/current/blinding-protocol.md`.

## Who does what (LB-032 override)
**CS** owns the critical path — designs the setup, **captures + scores** answers, prepares the operator's blinded eval, writes
the final report, prepares exp-002. **Blank CC** drives CS through the loop in an isolated runtime (never touches this
repo). **Operator/the operator** is the human bridge (moves folders) + the independent science evaluator. **the assistant** appears
ONLY if a run crashes (blackbox forensic report) — not in the normal flow.

## Folder map
```
exp-001_baseline-vs-v0-loop/
├── 00_hypothesis.md         [CS]  hypothesis + endpoint + what it changes vs loop-design/current
├── 01_setup/                [CS]  everything the run needs:
│   ├── v7_cc-bootstrap/           the loop of record (+ LOOP_VERSION.md); Arm L runs from this
│   ├── bootstrap.md              CS/operator-facing explainer of the CC start package + fairness model
│   ├── protocol.md               operator-facing run protocol (two-session model, 6 runs, two-key blind)
│   ├── test-set/                 questions.json (3 Qs + output-format) + README + materials/ (Q_ERGO PDFs)
│   ├── harness/                  the CS scoring harness (rubric v2; scores blinded R1…R6)
│   ├── for-the operator/               eval-site + final-report generators + specs (CS-run; "for-the operator" is legacy naming)
│   └── _superseded/              archived earlier-model files (v0 single-folder loop, done Tier-3 marker)
├── 02_results/              [operator copies coded answers R1…R6 here; CS scores from them]
│   └── scoring/                  CS harness output: scorecard.csv + scorecard_long.csv + scorecard.json
├── 03_final-report.md       [CS]  post-unblind per-arm report (embeds 05_analysis figures)
├── 04_evaluation/           [CS]  eval site (E1…E6), Key-2, the operator's filled JSON, full blinding key
├── 05_analysis/             [CS]  per-dimension × per-scorer × per-category plots + analysis_tables.csv
└── 05_v8-improvement-input.md [CS] per-arm qualitative (the operator free-text + red-flags + CS notes), post-unblind
```
> **Slug note:** the folder is named `…_baseline-vs-v0-loop`; "v0-loop" = "the first loop version under test", whose
> concrete implementation is **v7_cc-bootstrap**. Kept as-is to avoid churning dozens of cross-references (see
> `01_setup/v7_cc-bootstrap/LOOP_VERSION.md`).

See `../../DOCUMENTATION.md` §4 + §7 for the loop flow, and `../../loop-design/current/dataflow-and-handoffs.md` for the
authoritative start→finish→next walkthrough.
