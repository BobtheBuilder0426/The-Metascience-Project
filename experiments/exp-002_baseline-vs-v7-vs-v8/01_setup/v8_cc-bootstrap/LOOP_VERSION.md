# LOOP VERSION — v8_cc-bootstrap

- **Version name:** `v8_cc-bootstrap`
- **Content hash (sha256, first 16 hex, all 27 files concatenated in sorted path order, excl. LOOP_VERSION.md):** `331d802b219b4e69`
  - *(prior hashes: `24b364b1f22a1040` = Gate-2 figure add-on, before the pilot-design composer block (LB-089). This hash `331d802b219b4e69` = after adding the `pilot_design` conditional block to the context-composer (UPGRADE 1b, exp-002 output-format/pilot improvements — see the exp-002 improvements labbook entry). `92ea3b4abcae5794` = v8 with OPT-1 only, before the panel — LB-080. `2192548d3c253472` = panel wired
    in, before cold-read hardening — LB-084. `8b789842bd02f8e2` = after the cold-read verification fixes (blind-safety
    relay split, presentation standalone guard, deterministic Codex capture, Gate-2 fairness strip, per-lens retry,
    degrade↔Re-Act coupling, template freshness) — LB-085. This hash `24b364b1f22a1040` = after the Gate-2 artifact/
    figure-quality add-on (reviewer now sees CS's deliverables + figures and gives non-dominant design feedback) —
    LB-089.)*
- **Base:** built from `v7_cc-bootstrap` (content hash `6bbd94a13d13e462`, maintained source
  `experiments/exp-000_pilot_ergo-disease/01_setup/v7_cc-bootstrap/`), copied clean (23 files) and extended.
- **This copy:** the loop under test in `exp-002_baseline-vs-v7-vs-v8` (Arm L8). v7 is unmodified and still the
  Arm L7 loop.
- **⚠ v8 carries MORE THAN ONE upgrade over v7 (operator ruling 2026-07-12, LB-081).** Due to the time-box, changes were
  not made one-variable-at-a-time. So the exp-002 **L7→L8 delta is the cumulative v8 loop vs v7 — NOT a clean isolation
  of any single optimization.** Any write-up must state this. The two upgrades are:

  **UPGRADE 1 — OPT-1: per-question composed CS project Agent Context.** Instead of pasting the bare safety preamble,
  the bootstrap runs the shipped **`context-composer` skill** (`bootstrap/skills/context-composer/`) at project-creation
  (PART B step 10) to build `[safety preamble, verbatim] + [a performance block tuned to the question's shape]`. The
  performance block sharpens **how** CS works as a scientist (capability activation, citation discipline, reasoning
  transparency, completeness, honest uncertainty, anchored self-critique, novelty-paired-with-plausibility, and —
  when the task asks for an experiment — **pilot-design discipline** (smallest cheapest falsifying test; model-system
  before whole-animal; honest feasibility) — selected from a frozen, fairness-checked block library (principles
  P1–P12 / sources S-054..S-070 + the exp-001-feedback pilot block). It never prescribes **what** to conclude or
  reveals the domain; a fairness firewall (question-content-overlap) is asserted clean before use. *(The `pilot_design`
  block was added for exp-002 from exp-001 feedback — the operator: proposed pilots were overengineered, "not a pilot"; it is
  a conditional block gated on `asks_experiment`, firewall-clean, does not fire on hypothesis-only questions.)*

  **UPGRADE 2 — Codex multi-lens critique panel (C3): external cross-vendor review at two driver gates.** The driver no
  longer lets CS review its own plan/draft alone. Two gates, run by **GPT-5.6-sol agents via Codex on the host** (a
  different vendor from the Claude producer — the anti-self-enhancement mechanism): **Gate 1 (plan stage)** = a 4-lens
  panel (ambitious postdoc / experienced PI / anti-hallucination correctness / red-team) → a chairman qualitative
  synthesis → CS reflects + revises its plan; **Gate 2 (result stage)** = one journal-referee reviewer (plan-vs-
  implementation, bounded polish feedback) → a new **RE-ACT** phase where CS triages the feedback (accept/reject/defer),
  decides re-runs, and applies only quality-raising changes → INTEGRATE. **The Gate-2 reviewer also receives CS's actual
  deliverables + rendered figures (attached as images — Codex is multimodal) and adds a small, explicitly non-dominant
  4th output item: figure/artifact-quality feedback toward Nature/Science/Cell + professional-designer standards (KEEP-
  first, ≤2–3 concrete fixes, design-craft-only so it carries no domain WHAT) — added LB-089, sources S-077..S-082,
  research base `exp-002/01_setup/figure-quality-standards.md`.** Every critic gets web+literature (`codex-run.ps1
  -Search`) and a HOW-not-WHAT fairness firewall; all panel machinery lives in `run_log/panel/` and never enters the
  evaluated `presentation/` (blind-safety). Full spec + prompts: **`driver/CODEX_PANEL.md`**. If the Codex wrapper is
  unavailable/fails, both gates **degrade to self-review** (logged), so the loop still runs.

  Everything else (dedicated per-run folders, bridge, digest, isolation, blinding, presentation contract) is identical
  to v7.
- **New files vs v7 (4):** `bootstrap/skills/context-composer/{SKILL.md, blocks.json, kernel.py}` (UPGRADE 1),
  `driver/CODEX_PANEL.md` (UPGRADE 2).
- **Edited vs v7 (4):** `bootstrap/CLAUDE.md` (PART B step 10 → compose+firewall+paste [U1]; PART A pre-flight step 2b →
  detect+verify the Codex panel, record to CONNECTION.md [U2]; prepared-run status line), `bootstrap/skills/README.md`
  (context-composer section [U1]), `driver/CLAUDE.md` (Phase 3 → Gate 1; new Phase 6 Gate 2 + Phase 7 Re-Act; flow line;
  output tree adds `run_log/panel/` [U2]), `bootstrap/CONNECTION_TEMPLATE.md` (Codex-panel capability block [U2]).
- **Research + test provenance:** UPGRADE 1 — `loop-design/current/opt1-*.md`, `loop-design/current/opt1-context-composer-test/`
  (offline A/B: +0.060 overall, all 5 dims positive, firewall clean), `loop-design/future/context-composer-module/SPEC.md`.
  UPGRADE 2 — `experiments/exp-002_baseline-vs-v7-vs-v8/01_setup/codex-multilens-panel-design.md` (design + A/B/C decisions,
  sources S-071..S-076 + S-004/S-008/S-042/S-069 etc.). Labbook: LB-079 (context skill), LB-080 (v8 w/ OPT-1),
  LB-081 (panel workstream lock + multi-variable ruling), LB-082 [CS2] (panel research + design), LB-084 [CS2] (panel wired into v8).

To recompute the hash:
`find v8_cc-bootstrap -type f -not -name 'LOOP_VERSION.md' | sort | xargs cat | sha256sum | cut -c1-16`
