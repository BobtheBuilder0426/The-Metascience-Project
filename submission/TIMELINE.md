# Project timeline (reconstructed from the labbook)

**What this is.** A step-by-step reconstruction of the project from the append-only
`LABBOOK.md` (LB-001 → LB-106), oldest to newest. Each entry cites its labbook anchor so
the story can be checked against ground truth. Dates are CEST; the project ran
**2026-07-08 → 2026-07-13** (a six-day sprint to the deadline).

**How to read it.** Two intertwined threads run throughout:
the **Experiment Loop** (the outer scientific-method cycle: exp-000 → exp-001 → exp-002 →
exp-003) and the **Agentic Loop** (the inner product being optimized, versioned v0 → v6 →
v7 → v8 → v9). Major **pivots** are marked ◆.

---

## Day 1 — 2026-07-08 · Scaffold and lock the goal (LB-001 → LB-011)

- Repository scaffolded; roles, read-order, and the append-only labbook discipline
  established. (LB-001 → LB-005)
- ◆ **The research goal is formulated and locked** — the Northstar (use Claude Science to
  discover the best self-improving Agentic Loop and prove, measurably, that it beats a
  blank-CS baseline) plus Sections 1–6. (LB-006)
- ROADMAP, STATUS, and the resource pack assembled (machine specs, the Claude Science
  handbook, the 4 starter papers). The drive channel is fixed: a blank Claude Code controls
  the Claude Science browser tab. Domain = life science. (LB-007 → LB-011)

## Day 2 — 2026-07-09 · Design the method; the big architecture pivot; pilot begins (LB-012 → LB-048)

- **Phase-1 design work.** The 4 starter papers are read in full; the environment is
  self-checked; a literature-grounded evaluation methodology is written. (LB-012 → LB-014)
- **Quantification fixed *before* any run:** a 5-dimension rubric (grounding, correctness,
  completeness, usefulness, creativity) and — for the open creativity question — a
  multiplicative metric `Novelty × Plausibility-gate × ReasoningTrace-gate`. The scoring
  harness is built and dry-run clean (13/13). (LB-016, LB-018, LB-020)
- The v0 loop is specified as a flat single-session cycle
  (FRAME→PLAN→PLAN-REVIEW→ACT→RESULT-REVIEW→INTEGRATE). (LB-021 → LB-022)
- ◆ **Architecture pivot (operator override).** The workflow is simplified: **Claude Science
  owns the whole critical path** (capture → scoring → eval-prep → report → next); the
  operator is the A→B bridge; **the auxiliary analysis agent is removed from the critical path**
  (crash-fallback only, does not evaluate). (LB-031, LB-032)
- exp-001's two questions are locked (ergothioneine exercise-performance mechanism; and an
  exercise-mimetic repurposing question); the reviewer jury and blinded HTML eval site are
  designed. (LB-024 → LB-028, LB-033 → LB-038)
- **The pilot (exp-000) begins** to harden the CC bootstrap. (LB-039 → LB-042)
- ◆ **Safety incident.** During pilot bootstrap the blank Claude Code, running in the
  operator's logged-in Chrome, could read personal chats. A hard account-privacy block and
  an own-tab / own-project isolation rule are added — a real finding that shaped the loop's
  safety design. (LB-043 → LB-047)

## Day 3 — 2026-07-10 · The self-attach breakthrough; v5 → v6 (LB-049 → LB-065)

- The data channel is solved: browser upload is rejected, but a **shared host-folder mount**
  works. (LB-049)
- ◆ **v5 breakthrough** — the blank Claude Code self-attaches its own workspace folder and
  a real-file transport is verified end-to-end (it reads a 30-page PDF). (LB-050, LB-051)
- A 6-part redesign for v6 follows (persistent bridge, CC-side PDF digest, bootstrap/driver
  session split, structured intake); one module (multi-model literature synthesis) is
  **deferred** and shelved as future work. (LB-052 → LB-060)
- ◆ **v6 correction** — the missing local PDF renderer is fixed with a CC-side pypdfium2
  digest subagent (verified on 30 pages); a versioned bootstrap **archive** is created
  (9 CLAUDE.md versions recovered), and the current package is surfaced at repo top level.
  (LB-061, LB-062)

## Day 4 — 2026-07-11 · v7 is built; exp-001 runs (LB-063 → LB-077)

- The versioned-folder workflow is locked around `v6.1_cc-bootstrap`; the first real run
  reaches the driver START PROMPT and surfaces 4 issues. (LB-063, LB-064)
- ◆ **Fairness model updated (operator ruling):** the loop arm *may* optimize the CS project
  context — that counts as a measured loop gain, not cheating (this decision later becomes
  the v8 "OPT-1" upgrade). (LB-065)
- ◆ **`v7_cc-bootstrap` is built** (promoted from v6.1 with 5 fixes) and refined in place:
  publication-intake, a safety-only CS preamble, arm-blind neutrality, demo-data fidelity.
  Content hash `6bbd94a13d13e462`, 23 files. (LB-066 → LB-068)
- **exp-001 runs and is analyzed:** baseline vs the v7 loop, 3 questions, two-key
  double-blind, CS-panel + human-expert scoring. **Result — the loop wins the primary
  endpoint** (combined-composite mean within-question Δ = **+0.476**, winning **2 of 3**
  questions; the loss was on the open-ended question). The human expert preferred the loop
  answer on the ergothioneine question and flagged that the proposed pilots were
  overengineered — feedback that directly seeds a v8 upgrade. (LB-069 → LB-077)
  *(Note: the exp-001 folder is slugged `v0-loop`, but the loop under test was v7 — LB-077.)*

## Day 5 — 2026-07-12 · v7 → v8; exp-002 designed and executed (LB-078 → LB-094)

- v7 is redesigned to **bootstrap-once → drive-many** with dedicated, isolated per-run CS
  workspaces. (LB-078)
- ◆ **v8 upgrade 1 — OPT-1 context-composer.** A shipped skill composes a per-question CS
  project context (safety preamble + a fairness-checked "how to work as a scientist" block,
  including the pilot-design discipline learned from exp-001). Offline A/B: +0.060 overall,
  all 5 dimensions positive, firewall clean. (LB-079)
- **exp-002 created** (baseline vs v7 vs v8); `v8_cc-bootstrap` assembled. (LB-080)
- ◆ **Operator ruling (multi-variable):** under the time-box, v8 bundles **more than one**
  upgrade, so the L7→L8 delta will be the **cumulative v8 effect, not a clean single-variable
  isolation** — to be stated in any write-up. (LB-081)
- ◆ **v8 upgrade 2 — Codex cross-vendor critique panel.** The driver no longer lets Claude
  Science review its own work alone: a GPT-5.6-sol (Codex) panel critiques at two gates
  (a 4-lens plan panel + chairman; a single journal-referee result reviewer), followed by a
  new RE-ACT phase where CS keeps final agency. A Gate-2 figure-quality add-on is added later
  the same day. v8 content hash `331d802b219b4e69`, 27 files. (LB-082 → LB-090)
- The append-only discipline is reaffirmed after a correction; **v9** is branched from v8
  (content hash `c92973d8a3bbc5e9`, 28 files: Codex reasoning-effort high/xhigh, a hard
  multimodal Gate-2 precondition, and a CS-reconnect procedure). (LB-091 → LB-094)

## Day 6 — 2026-07-13 · exp-002 scored; exp-003 showcase; deadline (LB-095 → LB-106)

- **exp-002 is scored and unblinded.** CS blind-scores all 9 answers (rerun on
  claude-opus-4-8); a 0-fabrication certification passes (121/121 PMID, 112/112 DOI,
  36/36 GEO); the human expert completes the blind eval; the two-key unblind is composed.
  (LB-095 → LB-102)
- ◆ **exp-002 result (headline).** v8 wins **every** aggregate metric and every scorer; the
  **primary endpoint Δ(L8−L7) is positive on 3/3 questions for all scorers**. Honest
  secondaries: **v7 did *not* reliably beat baseline** (the gain is v8-specific); the
  open-ended "why does aging happen" question (Q2) was won by baseline unanimously; the
  Friedman omnibus is underpowered by construction (n=3). Gains concentrate in creativity and
  human-scored reasoning. (LB-103)
- **exp-003 — the final showcase.** Baseline vs the v9 loop on a genome-scale CD4⁺ T-cell
  Perturb-seq dataset, one shared question (find a natural metabolite to treat an autoimmune
  disease + design a pilot), byte-identical prompt, DOI-only data pointer + compute-caution.
  ◆ **Not scored — a showcase for the judges.** The two arms diverged: **baseline →
  IMPDH2 / mycophenolic acid / eosinophilic asthma**; **v9 loop → PKM2 / micheliolide /
  multiple sclerosis**. The v9 report carries visibly more epistemic-hygiene scaffolding
  (belief-ledger, perturbation-modality table, self-novelty check, falsifiable-interaction
  pilot). Claims are as reported by each arm — not re-verified by CS. (LB-104)
- exp-003 setup files are filled to the as-run state; sources S-084 (dataset) and S-085
  (preprint) are registered; the **GEO (GSE314342) and SRA (SRP643211) accessions are
  verified live via NCBI** (BioProject PRJNA1359008). (LB-105, LB-106)

---

## The two version threads at a glance

| Thread | Progression | Anchor(s) |
|---|---|---|
| **Experiment Loop** | exp-000 pilot (bootstrap hardening) → exp-001 (baseline vs v7) → exp-002 (baseline vs v7 vs v8) → exp-003 (baseline vs v9, showcase) | LB-039, LB-069→077, LB-103, LB-104 |
| **Agentic Loop** | v0 (flat) → v5 (self-attach) → v6 (two-session + PDF digest) → **v7** (drive-many, isolated workspaces; hash `6bbd94a1…`) → **v8** (+OPT-1 context-composer +Codex panel; hash `331d802b…`) → **v9** (+effort/multimodal/reconnect; hash `c92973d8…`) | LB-022, LB-051, LB-061, LB-066, LB-080, LB-094 |

## The pivots that mattered

1. **Operator override (LB-032)** — CS owns the whole critical path; the auxiliary analysis
   agent drops to crash-fallback. Simplified the workflow to a single accountable scientist.
2. **Safety incident → isolation rules (LB-043–047)** — a real privacy finding that made the
   loop's own-tab / own-project isolation non-negotiable.
3. **v5 self-attach breakthrough (LB-051)** — the moment the blank CC could actually reach a
   real-file data channel; everything downstream depends on it.
4. **Fairness ruling → OPT-1 (LB-065, LB-079)** — permitting the loop to optimize the CS
   project context turned a fairness question into the single measurable v8 upgrade.
5. **Multi-variable ruling (LB-081)** — the honest admission that v8 bundles >1 change, so
   its win is cumulative, not an isolation. Kept the analysis truthful.
6. **exp-003 as a showcase, not a score (LB-104)** — the final experiment is offered as an
   open, symmetric comparison for the judges rather than a measured claim.
