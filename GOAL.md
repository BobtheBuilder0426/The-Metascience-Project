# the Metascience Project GOAL -- [FINAL -- locked 2026-07-08]

<!-- WHAT THIS FILE IS: the locked research GOAL for the project + competition. HOW TO USE: right now it holds the
     CAPTURED INPUTS (raw material + decisions) for the GOAL, NOT the final formulation. We formulate the real GOAL
     from these next, step by step, then lock it. Everything below is crash-recovery-preserved so nothing is lost. -->

**Status:** FINAL -- Northstar + Sections 1-6 locked 2026-07-08 (operator-approved). Next: the ROADMAP. (Appendix below = original raw inputs, kept for provenance.)

---

## Northstar (LOCKED)

> **1.** Use Claude Science to scientifically discover the best automated, self-improving research loop for **agentic
> hypothesis generation** -- an **Agentic Loop** in which Claude Code drives Claude Science in a closed cycle -- that a
> blank Claude Code can bootstrap and run to turn any research question into **credible, genuinely novel** science, with
> each iteration's gain **measured, not asserted**.
> **2.** Prove it at **high-impact-journal standard** in a publication-style report: given the **exact same real
> question** as a raw, blank Claude Science baseline, the optimized Agentic Loop delivers the more credible and more
> creative science -- everything packaged **submission-ready** for *Built with Claude: Life Sciences*.

## 1. What this is & the plan (LOCKED)

This project runs inside *Built with Claude: Life Sciences* (Researcher Track); every output must end presentation- and
submission-ready.

Working systems now show agent teams can do real science -- **ERA** writes expert-level scientific software against a
metric, **Robin** runs a multi-agent lab-in-the-loop, **Co-Scientist** evolves hypotheses in a tournament (S-002..S-004).
Our contribution is not another such system, but the **method for reaching the best one**: we **use Claude Science to
scientifically discover the best automated, self-improving research loop** -- the **Agentic Loop**, in which Claude Code
drives Claude Science in a closed cycle -- and prove, measurably, that it works.

We reach it through the **Experiment Loop** (hypothesis -> test -> analyse -> repeat). Each iteration: Claude Science
designs a setup (bootstrap + ready-to-use Claude Code workspace + protocol + test set); a blank Claude Code bootstraps
and runs it **independently**; **the assistant** (the operator's Claude Code personal agent) analyses the run and reports back to
Claude Science, and assists the operator's evaluation (Claude Science decides how the operator evaluates); the operator gives scores + real
qualitative feedback; Claude Science analyses and forms the next hypothesis. **Claude Science's first task** is to work
out *how* it will run these experiments under our constraints and to identify the **quantification methods** that make
"better" measurable -- the progress of the setups across runs is itself part of the story.

The **proof** is a controlled comparison: a raw, blank Claude Science (empty new project) vs. a blank Claude Code
running the **optimized, final** Agentic Loop, both given the **exact same, word-identical** real research question --
which comes from **the operator** and is deliberately left open **to avoid overfitting** the loop to a specific question.

Everything is written up as **one publication-style report** at high-impact-journal standard (measured data, clean
figures, correct methods + controls -- credible to a Gladstone judge), and the final Agentic Loop ships **downloadable
and self-bootstrapping**. Emphasis: **the loop-method is the main contribution (~70%), the real finding is the proof it
works (~30%)**.

## Two loops (naming, to avoid confusion)

- **Experiment Loop** = the OUTER loop we RUN to discover the best setup: the scientific-method cycle
  hypothesis -> test -> analyse -> repeat. Each turn is an "experiment" (`experiments/exp-NNN/`).
- **Agentic Loop** = the INNER product we are building: the automated, self-improving research loop in which Claude
  Code drives Claude Science, which a blank Claude Code bootstraps + runs. Its evolving design lives in `loop-design/`;
  the final version is applied in `final-run/` and must be **self-bootstrapping** (a downloader gets the working loop
  automatically).

## 2. Deliverables & weighting (LOCKED)

Built **step by step** (not all at once), all wrapped into **one publication-style report**.

- **D1 -- The Experiment-Loop approach** -- how Claude Science decides to run the experiments: its experimental design + the **quantification methods** that make "better" measurable. *(part of ~70%)*
- **D2 -- The improvement report** -- how the setups get better across runs, and **which improvement-category delivers the most benefit, and by how much** (quantified). Categories are examples + extendable (specialists, a Claude Code sub-agent panel, a 2nd model like Codex, a CS project-context prompt, ...). *(part of ~70%)*
- **D3 -- The final Agentic Loop** -- the optimized loop, explained + shipped **downloadable & self-bootstrapping**: anyone who has Claude Code on the desktop and Claude Science installed + running in Google Chrome, downloads this repo, and starts it in a blank Claude Code, gets the running loop. *(part of ~70%)*
- **D4 -- The real finding** -- a genuine scientific result on a real question, requiring the full arc: **hypothesis generation, method selection + optimization, data analysis, and correct interpretation + presentation of results**. Delivered as the controlled comparison: raw blank Claude Science vs. blank Claude Code running the **final** Agentic Loop, same word-identical question. *(~30%)*

**Weighting:** D1-D3 together **~70%** (loop-method = main contribution); D4 **~30%** (the proof it works).

The report is one high-impact-journal-standard write-up and also serves as the **basis for the demo and the summary**. The **entire shared folder is submitted as the repo**, with the **LABBOOK as the central source of truth** over everything that happened.

## 3. Success dimensions (LOCKED)

North-star criteria -- what "good" means. **Claude Science operationalizes the exact metrics + thresholds itself** (we set WHAT to verify, CS decides HOW to measure).

1. **Loop is real** -- bootstrap -> the full Agentic Loop builds + runs autonomously.
2. **Loop beats baseline** *(central)* -- the blank-CC+loop output beats the raw blank-CS output, judged by CS's own criteria; those comparison criteria must be **understandable and identical for every test**.
3. **Scientific credibility** -- all sources cited, correct methods, appropriate controls, no hallucination / AI-slop; the code is present and really runs; results presentable with **no errors in figures/units/values** -- a Gladstone judge takes it seriously as real science.
4. **Improvement across iterations** -- measurable gains loop-to-loop (CS must find HOW to make this measurable).
5. **Human evaluation (the operator)** -- the methodology + write-up are understandable and the outcome is genuinely useful to the operator; needs a CS-defined work-up/explain mechanism + a standardized eval (scores + real qualitative feedback), which the assistant helps run.
6. **Genuine novelty / creativity** *(key differentiator)* -- did a truly novel + sensible hypothesis emerge? something surprisingly brilliant that breaks the AI "recombine-old-stuff" bias? **Open question: how do we measure this?** -- one of the first things CS must work out.

*(Mapping to the judging: loop + creativity -> Claude-Use + Impact; credibility + iteration -> Depth; everything stays demo-able -> Demo.)*

## 4. Experiment & comparison principles (CS fixes these first) (LOCKED)

Before running, Claude Science must settle:

- **Quantification first** -- identify the quantification methods that make "better" measurable, before any run.
- **Data generation + quality** -- design how each run generates **high-quality data**, especially the CC loop setup running in a clean Claude Code from the bootstrap on: as much as possible through the run/session itself, and through **the assistant**, who can inspect every file a run created and build an analysis report for Claude Science.
- **Runs per setup** -- decide run-once vs. **>=2 runs + mean** (to handle variance).
- **Test & baseline strategy (CS decides)** -- CS works out what's best: constant tests checked against a fixed blank-CS baseline, OR tests that grow more complex over iterations with the baseline re-drawn each round (a stronger loop on harder tests should widen the gap). Either way, **no memory / drift** may contaminate a run.
- **Identical wording** -- every test between the CS baseline and the CC-CS loop uses **exactly the same wording**.
- **Final comparison is chosen later** -- the final comparison question is **not fixed at the start**; it comes once the optimized loop stands.
- **the operator's test input** -- the operator contributes test suggestions to make his evaluation more useful.
- **Constant criteria** -- evaluation criteria are understandable and identical for every test.

## 5. Roles & improvement categories (LOCKED)

**Roles:**
> **OPERATOR OVERRIDE (2026-07-09, LB-032):** the operator simplified the workflow — **CS owns the whole critical
> path** (capture-prep → scoring → eval-prep for the operator → final report → next experiment, locking the labbook throughout).
> The **operator is the A→B bridge** (copies setups/workspaces/outputs/eval-JSON under CS instruction). **the assistant is NO
> LONGER in the critical path** — used ONLY as a crash fallback (a blackbox forensic report if the blank CC/CS loop
> fails). The original the assistant role below is superseded to that extent. Canonical flow: `loop-design/current/dataflow-and-handoffs.md`.
- **Claude Science** -- designs the Experiment Loop + the Agentic Loop; runs the experiments; analyses; defines + operationalizes the criteria and metrics; **owns capture→scoring→eval-prep→report→next (operator override).**
- **the assistant** (the operator's Claude Code personal agent) -- **CRASH FALLBACK ONLY (operator override, LB-032):** if the blank CC/CS loop crashes, the assistant inspects the run's files + builds a blackbox forensic report for CS. Not in the normal critical path. **Does not evaluate.**
- **blank Claude Code (CC)** -- bootstraps + runs one setup independently in a clean session.
- **blank Claude Science (baseline)** -- runs the test in an empty, independent project as the raw control the loop is measured against.
- **the operator** -- evaluates (scores + real qualitative feedback, in a CS-defined format) and is a domain-expert resource.

**Improvement categories to evaluate** *(examples -- CS may change/extend)*: **CS Specialists** (a named set of skills, connectors + instructions a session answers as); a Claude Code sub-agent panel; a 2nd AI model (Codex) used by the blank CC session; a CS project-context prompt; ... -> find which delivers the most benefit, and by how much. *(Start angles: the 4 starter papers in `resources/papers/` (S-002..S-005), Karpathy's "LLM council", and OpenRouter model-fusion.)*

## 6. Operating scope, resources & constraints (LOCKED)

**The setup CS works in** (so it plans realistically): Claude Science runs on Linux; Claude Code runs on Windows; both share ONE folder (this repo) through a bridge. Heavy code is never run in-place from the shared mount -- it is pulled to a local runtime area, run, and results copied back. Full specs, topology, and the complete resource list are in **`resources/RESOURCES.md`** (read it). **Drive channel:** Claude Code drives Claude Science by **controlling the CS browser tab (Chrome control)** -- the Chrome extension + Codex live on the Claude Code side.

**What CS, the Experiment Loop, and the Agentic Loops may use** (they may all use every resource listed here; summary, full detail in `resources/`):
- **Compute:** one modest laptop (4C/8T, ~8 GB RAM shared, integrated GPU, ample disk) -- **bounded concurrency, no heavy local ML, do not crash it.**
- **Tools:** Claude Code (Max 20x), Claude Science, Claude Chrome plugin, full web access, Codex (2nd model), `claude -p` (free allowance only), $200 API credits. **Chrome control + Codex are part of the standard blank-CC setup** -- the bootstrap just checks its environment.
- **Knowledge:** the Claude Science handbook + the 4 starter papers (`resources/`), plus Claude Deep-Research on demand.
- **People/agents:** the operator (domain expert; can fetch allowed non-paywalled literature **+ supplementary datasets** when interesting -- for the Experiment Loop and the Agentic Loops -- + copy-paste on request); **the assistant** (the operator's Claude Code agent -- data prep + run analysis; assists the operator with his tasks).

**Cross-cutting rules:** the **LABBOOK is THE central document** -- it must hold all the information by the end and be **updated after every step**, so the whole research is reproducible and traceable. Everything is documented **crash-recovery-proof**. The repo stays **self-contained** (no private-workspace references; external knowledge enters only via `resources/`).

**Scope / non-goals:** the research **domain is life science** (matching the Researcher Track + the final question). The real research question is **deliberately open** (comes from the operator, chosen once the optimized loop stands, to avoid overfitting); **standalone** project; **New-Work-Only** (analysis happens during the event).

**Constraints:** deadline **Mon 2026-07-13 21:00 ET (= Tue 14 03:00 CEST)**; compute per above; `claude -p` free allowance only; $200 API.

**Open questions:** how to measure creativity/novelty; CS's quantification methods; runs-per-setup (once vs. mean-of-N); the final comparison question (chosen later, not at the start).

---

## Appendix -- original captured inputs (now formulated into Sections 1-6 above; kept for provenance)

### The plan / arc (context -- do not lose)
The whole thing runs inside the competition and must end presentation-/submission-ready. The arc: (1) CS first works
out HOW it will run experiments under these constraints + goals, and identifies the **quantification methods** to
measure progress; (2) CS runs the **Experiment Loop** -- designing setups, a blank Claude Code builds + runs each,
the assistant analyses + reports, the operator evaluates -- to discover the best **Agentic Loop**; (3) the improvement of the setups
across runs is measured + shown; (4) the final Agentic Loop is explained + made downloadable (self-bootstrapping); (5)
the real research finding is produced paper-ready and compared: a raw blank Claude Science vs a blank Claude Code
running the final Agentic Loop, on the **exact same (word-identical) question**. All of it is written up as one
publication-style report.

### Deliverables + weighting (built STEP BY STEP, not all at once)
- **D1** -- CS's approach to running the Experiment Loop (its experimental design). }
- **D2** -- report on how the setups get better across runs (incl. which improvement-category helps most, quantified). } = **70%**
- **D3** -- the final Agentic Loop: explained + downloadable + self-bootstrapping. }
- **D4** -- the real finding: blank CS vs blank CC+final-loop on the same word-identical question, paper-ready. = **30%**
- All wrapped in **one publication-style report** (high-impact-journal standard: figures + measured data, no errors in
  figures/units/values -- a Gladstone judge takes it seriously as real science).

### Success dimensions (north-star; CS operationalizes the exact metrics -- FB-013)
1. **Loop is real** -- bootstrap -> full Agentic Loop built + runs autonomously.
2. **Loop beats baseline** -- blank-CC+loop output > raw blank-CS output, by CS's criteria. **Central.** The comparison
   criteria must be **understandable and the SAME for every test.**
3. **Scientific credibility** -- all sources, correct methods, appropriate controls, no hallucination/AI-slop; code
   present + really runs; outcome presentable; convinces a critical reviewer / Gladstone judge.
4. **Improvement across iterations** -- measurable gains loop-to-loop (CS must find HOW to make it measurable).
5. **Human evaluation (the operator)** -- understandable methodology / write-up, real usefulness; needs a work-up/explain
   mechanism + a standardized eval. the assistant may run the eval WITH the operator using a CS-provided skill/format. Capture the operator's
   real qualitative input + feedback, not only scores.
6. **Genuine novelty / creativity** -- novel + sensible hypotheses, "surprisingly brilliant", breaking the AI
   recombination-bias. **Important -- OPEN QUESTION: how do we measure this?**

### Experiment / comparison principles CS must fix FIRST
- Identify **quantification methods** before running.
- Decide **run-once vs. >=2 runs + mean** per setup.
- **Tests stay the same** across iterations (control variable); ensure **no memory / drift** over time.
- The **blank-CS control always runs in an empty, new, raw project.**
- Compare on a **word-identical** question.
- **the operator contributes test suggestions** (to make his eval more useful).
- Evaluation criteria: **understandable + constant per test.**

### Improvement categories to evaluate (EXAMPLES -- CS may change/extend)
Create specialists; spawn a subagent panel in Claude Code; use a 2nd AI model (Codex); give CS a project-context
prompt; ... -> find which measure brings the most benefit, and by how much.

### Roles
- **CS** -- designs the Experiment Loop + the Agentic Loop; analyses; defines/operationalizes the criteria + metrics.
- **the assistant** -- analyses + writes the report to CS; on CS's request investigates the blank-CC run + pulls data back;
  may run the eval WITH the operator via a CS format. **Does NOT evaluate.**
- **blank Claude Code (CC)** -- bootstraps + executes one setup.
- **the operator** -- evaluates (scores + real qualitative feedback) and is a domain-expert resource.

### End artifact
- One **publication-style report** (high-impact standard, figures, measured data, credible to a Gladstone judge) that
  tells the whole story.
- The **final Agentic Loop** explained + **downloadable + self-bootstrapping** (someone who downloads the repo gets the
  working loop automatically; a blank CC can bootstrap it alone).
- The **real finding** written paper-ready, with the blank-vs-loop comparison.

### Cross-cutting rules
- **Crash-recovery documentation is central:** everything documented crash-recovery-proof, with the **labbook as the
  top ground truth.**
- **Self-containment / no overspill:** nothing from any private workspace enters this repo; external knowledge comes in
  only via `resources/` (e.g. the Claude Science handbook, the papers the operator provides).

### Scope / non-goals
- The real research question is **deliberately open** (chosen with/by the optimized loop).
- **Standalone** project; **New-Work-Only** (analysis must happen during the event).

### Constraints
- Deadline Mon 2026-07-13 21:00 ET (= Tue 2026-07-14 03:00 CEST).
- Compute per `resources/RESOURCES.md` (tight RAM, bounded concurrency, no heavy local ML, do not crash the machine).
- `claude -p` only within the subscription's free allowance; $200 API credits.

### Open questions
- How to measure creativity/novelty (dimension 6).
- CS's quantification methods (dimension 4 + progress measurement).
- Run-count per setup (once vs. mean-of-N).
