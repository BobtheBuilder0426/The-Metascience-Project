# LOOP VERSION — v9_cc-bootstrap

- **Version name:** `v9_cc-bootstrap`
- **Content hash (sha256, first 16 hex, all 28 files concatenated in sorted path order, excl. LOOP_VERSION.md):** `c92973d8a3bbc5e9`
  - *(prior hashes: `331d802b219b4e69` = **v8** final (Gate-2 figure add-on + the `pilot_design` composer block) — the
    clean base this v9 was copied from. Earlier v8 chain: `24b364b1f22a1040` = Gate-2 figure add-on before the
    pilot-design block (LB-089); `92ea3b4abcae5794` = v8 with OPT-1 only, before the panel (LB-080); `2192548d3c253472`
    = panel wired in, before cold-read hardening (LB-084); `8b789842bd02f8e2` = after cold-read verification fixes
    (LB-085).)*
- **Base:** built from **`v8_cc-bootstrap`** (content hash `331d802b219b4e69`, source
  `experiments/exp-002_baseline-vs-v7-vs-v8/01_setup/v8_cc-bootstrap/`), copied **clean (27 files)** and extended with
  the three v9 edits below. v8 (and its own base v7, `6bbd94a13d13e462`) are unmodified and remain the exp-002 L8 / L7
  loops of record.
- **This copy:** the loop under test in `exp-003_final-tcell-perturb` (the FINAL experiment — T-cell perturbation data
  test).

## v9 — what changed vs v8 (four edits, from three operator-requested changes; 2026-07-12)
The operator asked for three surgical changes; the Codex model/effort change splits cleanly across the two gates, so it
is documented below as EDIT 1 (Gate 1) + EDIT 2 (Gate 2) — four edits in total. All four are **loop machinery** (HOW the
loop's critics run + how a dead CS session is recovered), never science content, and are applied identically to every
arm that runs this loop — so they carry no fairness cost; the HOW-not-WHAT firewall + blind-safety rules in
`driver/CODEX_PANEL.md` are unchanged.

  **EDIT 1 — Gate-1 Codex critics fixed to `gpt-5.6-sol`, reasoning effort `high`.** All four Gate-1 lenses AND the
  chairman now run at reasoning effort **high** (was: model named, effort unspecified). A per-gate "Model + reasoning
  effort" section is the single source of truth; the invocation shape carries a `-Effort <lvl>` flag (with a
  `-c model_reasoning_effort="<lvl>"` native passthrough fallback), and the pre-flight verifies + records the working
  effort-flag form (`codex_effort_flag` in CONNECTION.md).

  **EDIT 2 — Gate-2 Codex reviewer fixed to `gpt-5.6-sol`, reasoning effort `xhigh`.** The single result-stage journal
  reviewer runs at the **deepest** reasoning budget (`xhigh`) — the highest-stakes critique gets the most reasoning.

  **EDIT 3 — Gate-2 becomes a HARD MULTIMODAL precondition: the reviewer MUST see CS's figures and read CS's files.**
  v8 attached figures "if the `-i` build is available" with a soft text-only fallback. v9 makes multimodal a
  **pre-flight-verified requirement**: bootstrap **step 2c** runs a combined probe — a token painted into a PNG
  (`IMAGE_TOKEN`), a labelled/coloured box set (`BOXES`), and a token read from a file (`FILE_TOKEN`) — and only on a
  fully-correct, unhallucinated round-trip records `panel_multimodal: yes` (+ the exact tokens + the working `-i`
  invocation) in CONNECTION.md. When `yes` (the v9 default), Gate 2 **must** attach every rendered figure with `-i`
  (`codex exec -i <file.png>`) at `-Effort xhigh` and give the reviewer the deliverable text files. The honest text-only
  path survives **only** when the probe fails (`panel_multimodal: no`) and then the run **logs Gate 2 as degraded**.

  **EDIT 4 — CS reconnect procedure for both CC roles.** A new `bootstrap/RECONNECT_CLAUDE_SCIENCE.md` documents how a
  bootstrap OR driver session recovers a dead/expired Claude Science session on its own: the login link is single-use +
  expires in ~3 min (and a daemon restart kills the session), so always mint a **fresh** link — PowerShell
  `wsl -- bash -lc "claude-science url"` → paste the `http://localhost:8000/?nonce=…` into Chrome → Sign in;
  "login no longer valid"/"reconnecting" = expired (same fix); daemon auto-starts (`ClaudeScience-EnsureUp`) or is
  forced with `claude-science serve --port 8000 --no-browser --detached`. Folded into CONNECTION.md's "How to resume"
  (replacing the old ask-the-human dead-end) + one-line pointers in `bootstrap/CLAUDE.md` and `driver/CLAUDE.md`.

- **New files vs v8 (1):** `bootstrap/RECONNECT_CLAUDE_SCIENCE.md` (EDIT 4). → 28 files total (v8 had 27).
- **Edited vs v8 (4):** `driver/CODEX_PANEL.md` (EDITs 1–3: Model+effort section, Gate-1/Gate-2 effort, `-Effort`
  invocation + native passthrough, Gate-2 hard multimodal precondition + degrade-only-on-probe-fail + done criterion),
  `bootstrap/CLAUDE.md` (pre-flight 2b verifies `-Effort` + records `codex_effort_flag`; new pre-flight **2c**
  multimodal probe; step-4 CS-reconnect pointer), `bootstrap/CONNECTION_TEMPLATE.md` (adds `codex_effort_flag` +
  `panel_multimodal` block with `image_token_seen`/`boxes_read`/`file_token_read`/`multimodal_invocation`; reconnect
  procedure in "How to resume"), `driver/CLAUDE.md` (STEP −1 CS-reconnect pointer).
## Inherited history — what v8 already carried over v7 (v9 keeps ALL of it)
- **⚠ v8 carries MORE THAN ONE upgrade over v7 (operator ruling 2026-07-12, LB-081).** Due to the time-box, changes were
  not made one-variable-at-a-time. So the exp-002 **L7→L8 delta is the cumulative v8 loop vs v7 — NOT a clean isolation
  of any single optimization.** v9 inherits this entire bundle unchanged, so **any exp-003 write-up that compares v9 to
  v7 or to baseline must state that the v9-vs-earlier delta is cumulative** (v8's OPT-1 context + Codex panel + the v9
  effort/multimodal/reconnect edits together), not a single-variable isolation. The two inherited v8 upgrades are:

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
`find v9_cc-bootstrap -type f -not -name 'LOOP_VERSION.md' -not -name '*.pyc' -not -path '*/__pycache__/*' | sort | xargs cat | sha256sum | cut -c1-16`
