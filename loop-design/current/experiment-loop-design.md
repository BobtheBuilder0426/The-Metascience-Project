<!-- WHAT THIS FILE IS: D1 — Claude Science's design of the EXPERIMENT LOOP: how CS runs the experiments to discover
     the best Agentic Loop, and the controls that make the comparison credible. It is the methods backbone of the
     submission. HOW TO USE: read with method-foundations.md (the cited basis) and quantification.md + creativity-metric.md
     (the measurement specs). This doc = the experimental design + strategy; those two = the metrics. Update via a new
     labbook entry; promote changes into loop-design/CHANGELOG.md. -->

# D1 — The Experiment-Loop design  [CS] — 2026-07-09  (v0)

**One sentence.** We run an outer **Experiment Loop** (a controlled, metric-driven search) to discover the inner
**Agentic Loop** (a blank Claude Code that drives Claude Science) that turns a research question into the most
**credible** and most **novel** science — proven against a raw blank-CS baseline on **word-identical** questions.

This is, in the language of the harness survey (S-005), a **Meta-Harness outer loop**: an agentic proposer (CS)
iterates *loop* designs, evaluates each on a benchmark (our test set + quantification), and feeds results back into
the next design. The survey's central evidence — that **harness-level changes with the model held fixed drive large
performance gains** — is exactly the bet this project makes.

---

## 1. The two loops (what we run vs. what we build)

- **Experiment Loop (OUTER, what CS runs):** hypothesis → setup → run → analyse → repeat. Each turn is an
  `experiments/exp-NNN/`. The manipulated thing is the **Agentic-Loop design**.
- **Agentic Loop (INNER, the product):** a blank Claude Code that bootstraps a workspace and **drives a Claude Science
  session** (via Chrome control) through a research task, exploiting the full CS capability stack, then self-reports.
  Its evolving design lives in `loop-design/current/`; the final version ships self-bootstrapping in `final-run/`.

```
        ┌───────────────────────── EXPERIMENT LOOP (CS runs this) ─────────────────────────┐
        │  00 hypothesis → 01 setup → [run] → 02 results → 03 report → 04 eval → 05 analysis │
        │        ▲                                                                    │      │
        │        └──────────────── next hypothesis (promote if improved) ◄───────────┘      │
        └───────────────────────────────────────────────────────────────────────────────────┘
                                        the "[run]" expands to ↓
        ┌───────────────────────── AGENTIC LOOP (the product under test) ──────────────────┐
        │  blank CC  ──drives──▶  Claude Science session  ──uses──▶  connectors+skills+      │
        │  (isolated)  ◀─reads─   (hypothesis, analysis, figures)     Reviewer, code, data   │
        └───────────────────────────────────────────────────────────────────────────────────┘
```

## 2. Roles & the isolation boundary (LOCKED)

| Agent | Runs where | May touch the shared repo? |
|---|---|---|
| **CS** (designs + analyses) | Linux/WSL (this) | YES — authors setups, analyses, promotes loop versions |
| **blank CC** (executes one setup, drives CS) | **isolated runtime area** (own laptop / possibly different Claude account) | **NO — never reads or writes the shared repo or labbook.** It stays "blank". |
| **the assistant** (Mission-Control CC) | bridges | YES — the **ONLY** agent that carries blank-CC outputs back into the repo, analyses, reports to CS |
| **the operator** (human expert) | — | evaluates (scores + qualitative), contributes test questions |
| **blank CS baseline** | fresh raw CS project | the control arm; empty, memory-free |

**Why the blank CC is walled off (operator-locked):** a CC that reads our GOAL/labbook/loop-design is no longer a
*blank* CC — it would be contaminated by the very design we're testing, and the "a downloader gets a working loop"
claim (D3) would be unfalsifiable. So the setup package it receives (`01_setup/`) is **fully self-contained with zero
references to the rest of the repo**, and everything the run produces is pulled back **by the assistant**, not by the CC.

## 3. The unit of the experiment (controlled design)

Classical design-of-experiments discipline (method-foundations §D):

- **One manipulated variable per experiment** = the **improvement category** under test (see §7). Everything else is
  held fixed. This is what lets D2 attribute "which improvement helped most, and by how much".
- **Controls held fixed:** the test-set questions (word-identical across arms), the quantification rubric, the judge
  panel configuration, and the blank-CS baseline procedure.
- **No memory / no drift:** every baseline runs in a **fresh, empty CS project** with memory off; every CC run
  bootstraps a clean workspace. Nothing carries state between runs that shouldn't.
- **Replication:** **≥2 runs per setup, report the mean** (and spread), because agentic outputs vary run-to-run
  (S-003, S-004). Use 3 when cost allows; the scoring is cheap (API/DB), the CC runs are the cost.

## 4. The comparison arms (what is measured against what)

Two arms answer the **same word-identical question**:
- **Arm B (baseline):** a **raw blank Claude Science** project — no loop, no specialists, no project context — given
  the question directly. The control the loop must beat (GOAL success-dim 2, central).
- **Arm L (loop):** a **blank Claude Code running the current Agentic Loop**, which drives a CS session through the
  same question, exploiting the full CS stack.

Outputs from both arms are **normalized to a common answer template** and **blinded** (arm identity + tell-tale style
stripped) before scoring, so neither the judge panel nor the operator knows which arm produced which — the confounder control
from Si et al. (S-006). Arm order is randomized (S-008 position-bias control).

## 5. Test & baseline strategy (CS decision)

GOAL S4 offers two strategies; **we choose a hybrid, and here is the reasoning:**

- **Primary = constant tests vs. a fixed baseline.** The 4 test-set questions (`test-sets/2026-07-09_testset_aging-v1/`)
  stay **constant** across iterations; the blank-CS baseline is **drawn once per question and reused** (re-run for
  variance, but same procedure). This gives a clean, comparable **loop-to-loop improvement curve** — the D2 headline —
  because the yardstick never moves. It is the cheaper, lower-variance choice, which matters under our compute bound.
- **Secondary = an escalation check at the end.** Once the loop stops improving on the constant set, we run **one
  harder tier** (T3 questions) with the baseline **re-drawn**, to test the GOAL's hypothesis that *a stronger loop on
  harder tasks widens the gap*. If the gap widens, that is a strong result; if not, we report that too.
- **Why not escalate every round:** moving the test and the baseline simultaneously every iteration confounds
  "loop got better" with "test got harder" — you can't read the improvement curve. Keeping the test constant is the
  control-variable choice; the escalation is a separate, deliberate stress test.

**Runs-per-setup:** ≥2 + mean (see §3). **Iterations:** target ≥3 improvement experiments, 2 tests (questions) each,
per ROADMAP — adjustable as variance/compute dictate.

## 6. One turn of the loop (the relay, with hand-offs)

Per DOCUMENTATION §4b, hand-offs are **few + explicit + human-relayed** (the operator triggers between the isolated systems):

1. **CS** finalises `exp-NNN/01_setup/` (self-contained) → STATUS "Next: run exp-NNN" + labbook.
2. **the operator** starts the blank-CC run on the pulled setup (human trigger CS→CC).
3. **blank CC** bootstraps in its isolated area, drives a CS session through each test question, self-documents +
   self-reports **in its own area** (never the repo).
4. **the assistant** pulls the outputs back → `02_results/`, writes `03_final-report.md` (to CS's spec), runs the automated
   scoring harness, presents to the operator → STATUS "Next: the operator eval".
5. **the operator** evaluates via the assistant's present-to-operator skill → `04_evaluation.md` (scores + qualitative) → STATUS "Next: CS analyse".
6. **CS** writes `05_analysis.md` + next hypothesis; if improved, promotes to `loop-design/current/` (+ CHANGELOG) →
   STATUS "Next: run exp-(N+1)". Repeat.

### 6a. Autonomy & the permission watchdog (from the CC pre-check)
The drive channel is operator-attested working; the residual risk for **unattended** running is CS **permission cards**
and **turn-completion detection** (CC report B/Q7-Q8). Design answer (two layers):
- **Pre-clear predictable scopes** in the bootstrap's pre-flight: CS code-execution = **Always**; featured connectors =
  **Always-allow / per-project**; folder grants persisted; compute jobs = **all-jobs-in-project** (CS permission scopes,
  handbook §1/§7). Most cards then never appear.
- **A watchdog/monitor sub-agent** in the CC session polls the CS tab for (i) a residual permission card → signals the
  driver to click approve, and (ii) **turn-completion** via a **stable-text + button-state debounce** (not a one-shot
  read). Where full autonomy can't be guaranteed, the loop degrades gracefully to an **explicit human-relayed approval
  point** rather than stalling silently.

## 7. Improvement categories to test (the D2 search space)

Each is a candidate manipulated variable (GOAL S5; examples, extendable). Ordered by expected benefit ÷ cost:

Reordered + expanded after the operator's prior-experience input (S-014, LB-019); axes now match what real runs
suggest matters. Each is a candidate manipulated variable (GOAL S5; extendable). Ordered by expected benefit ÷ cost:

| # | Category | What changes in the Agentic Loop | Cost | Rests on |
|---|---|---|---|---|
| C1 | **Mission-Control vs flat driver** | orchestrator MC + fresh substep-worker CC sessions + CS integration, vs one flat CC | structural | **S-014 A** (context = binding); S-004 Supervisor+worker; S-005 context isolation |
| C2 | **Plan-stage review gate** | inject creativity/ambition after the PLAN (before expensive results) | low | **S-014 D** (cheapest leverage); much cheaper than re-running results |
| C3 | **KEEP-first 2-lens × 2-brain panel** | correctness-checker → postdoc/PI lenses × Claude+Codex → comparator → chairman | med | **S-014 E/F**; Karpathy council; S-008 (2 brains vs self-enhancement) |
| C4 | **CS project-context prompt / Specialist** | give the driven CS session a standing domain brief / a named Specialist profile | low-med | CS `customize`; **S-014 G**; exploits the full stack |
| C5 | **Connector/skill exploitation depth** | explicitly enable + chain more CS connectors + enforce citations | med | **S-014 G**; "most out of CS"; S-005 (V-component) |
| C6 | **Poll cadence + permission pre-grant** | ≥5-min (default 10) polling; one project-wide permission grant up front | low | **S-014 B** (saves context + cuts stalls) |
| C7 | **Recombination / idea injection** | inject literature ideas + recombine partial substep answers | med | S-002 (ERA idea injection/recombination) |

C1/C3 are structural (the Mission-Control shape + the panel are the loop's backbone); C2/C6 are cheap tunables tested
early; C5/C7 exploit CS depth. **We test them one at a time**, cumulatively promoting winners into
`loop-design/current/`, so D2 can report each
category's marginal contribution. C5 is RAM-risky and gated behind the footprint budget (≤2-3 light agents).

## 8. What "an experiment" measures (pointer)

The dependent variable is the **quality + creativity** of each arm's output, scored by:
- the **automated harness** (rubric + citation-verification + literature-distance novelty + judge panel + Elo) — see
  `quantification.md` and `creativity-metric.md`, and
- **the operator's expert eval** (blinded scores + qualitative) — the human ground truth (GOAL success-dim 5).

An experiment **succeeds** when Arm L beats Arm B on the composite, the gain is **larger than run-to-run spread**, and
the operator's expert judgment concurs. Improvement across iterations (the D2 curve) is the story.

## 9. Constraints folded in (so the design is runnable)
- **GPU-free iteration** (no local/remote GPU); the €15 GPU budget is reserved for **one final-task step** only.
- **Lean footprint** (~2.3 GB realistic free RAM): scoring is API/DB-driven; bounded concurrency; no heavy local ML.
- **Crash-recovery:** every turn logged in the labbook (highest truth), STATUS updated, sources registered.
- **Self-contained repo:** the blank CC's `01_setup/` references nothing outside itself.

## 10. Threats to validity (named, so the write-up is honest)
- **Self-enhancement bias** (a Claude judge favouring Claude output) → mitigate with a non-Claude judge (Codex),
  inter-judge agreement reporting, and the operator as tie-break (S-008).
- **Novelty ≠ correctness** → plausibility gate + expert check; never score novelty alone (S-006, S-009).
- **Small n** (few questions × few runs) → report spread, don't over-claim significance; use the escalation check as
  corroboration, not a second bite.
- **Drive-channel variance** → watchdog + human-relayed fallback; log every run's reliability.
- **Overfitting the loop to the test set** → the **final** comparison question is chosen **later**, by the operator, and is
  distinct from the test set (GOAL S4).
