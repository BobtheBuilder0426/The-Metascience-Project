<!-- WHAT THIS FILE IS: the literature-grounded methodological basis for the Metascience Project's Experiment Loop, quantification, and
     creativity metric. It records WHICH established methods we adopt and WHY, with citations (S-NNN), so every design
     choice downstream is traceable to prior work rather than asserted. HOW TO USE: read before the design docs
     (experiment-loop-design.md, quantification.md, creativity-metric.md); each of those cites back here. Append-safe. -->

# Methodological foundations (literature-grounded)  [CS] — 2026-07-09

This project is scientific, so its *measurement* methods must themselves be defensible. Below: the established
methods we adopt for (A) evaluating AI-generated science, (B) LLM-as-judge scoring, (C) novelty/creativity, and
(D) the outer experiment loop — each with the prior work it rests on.

## A. How to evaluate AI-generated scientific hypotheses (the eval design)
- **Blinded, confounder-controlled, head-to-head** is the gold standard. Si, Yang & Hashimoto (S-006) recruited 100+
  experts to write and *blind-review* AI vs. human research ideas, standardizing format/style so reviewers could not
  tell arms apart. **We adopt:** (i) both arms (baseline blank-CS vs. CC-driven loop) answer **word-identical**
  questions; (ii) outputs are **normalized to a common template** before scoring so judges are blind to which arm
  produced them; (iii) each item is scored on the **same rubric**.
- **Key empirical finding we design around:** AI ideas were judged **more novel but slightly less feasible** than human
  ideas (S-006). This is why novelty must **not** be scored alone — it must be paired with a feasibility/plausibility
  dimension (see C). It also sets a realistic expectation for our own results.
- **Expert + automated in combination.** The three starter systems all pair an automatic score with expert judgment:
  ERA a leaderboard metric (S-002), Co-Scientist Elo self-evaluation **plus** blinded expert novelty/impact Likert
  (S-004). **We adopt** the same two-track shape: cheap automated scoring for every iteration + the operator's expert eval as
  the human-grounded check.

## B. LLM-as-judge (the scalable scoring engine for iteration)
- **G-Eval** (S-007): LLMs judge best with **chain-of-thought + a form-filling paradigm** (fill a structured score
  form, with reasoning), which correlates with human judgment better than raw prompting. **We adopt** a rubric form
  the judge fills field-by-field with brief justification.
- **Judge reliability + biases** (S-008, MT-Bench/Chatbot Arena): LLM judges show **position, verbosity, and
  self-enhancement** biases; mitigations include **pairwise comparison, randomized order, and a panel/aggregate**.
  **We adopt:** (i) a **panel of judges** (multiple `host.llm` calls / models incl. Codex on the CC side — the
  "council" idea) and aggregate; (ii) **randomize arm order** and strip identifying style; (iii) for cross-iteration
  ranking use **pairwise Elo**, which is drift-robust (a relative signal that does not depend on absolute scale).
- **Self-enhancement caveat (important for us):** a Claude judge scoring Claude output can inflate. **Mitigation:**
  include a non-Claude judge (Codex is available per the CC pre-check), report inter-judge agreement, and treat the operator's
  expert eval as the tie-breaking ground truth.

## C. Novelty, usefulness, creativity (the open GOAL question)
- **Creativity = novelty AND usefulness** is the standard definition in the creativity literature (S-009, meta-theory).
  A hypothesis that is novel but useless is not creative; nor is a useful but obvious one. **We adopt** a **product
  form: creativity = novelty × plausibility** (a plausibility gate), so "surprising but nonsense" cannot score high —
  directly targeting the GOAL's "break the AI recombine-old-stuff bias, but sensibly".
- **Novelty as distance from prior art.** Science-of-science work measures novelty as **atypical/distant combinations
  of prior references** and documents a **systematic bias against novelty** with delayed recognition (S-010). **We
  adopt** a computable **literature-distance novelty**: embed the hypothesis, retrieve nearest prior art via
  OpenAlex/PubMed, and score novelty as *inverse* semantic similarity to the closest existing work — with the aging
  domain's dense literature (S-011: 8,596 "hallmarks of aging"; 3,951 mito-dysfunction) giving a real baseline.
- **Expert novelty rating** (S-004, S-006): a **5-point Likert on novelty + impact**, blinded, remains the human
  anchor. **We adopt** it for the operator, plus a qualitative "is this surprisingly good / does it break recombination bias?"
  prompt to capture what a number cannot.
- **Composite (proposed, validated empirically not asserted):**
  creativity_score = plausibility_gate × [ w1·literature_distance_novelty + w2·expert_novelty ] , with Elo as the
  drift-robust cross-arm/cross-iteration ranking. Weights + gate calibrated on worked examples (step 4).

## D. The outer Experiment Loop (how we run the search)
- **Metric-driven iterative search** is the shared skeleton of the prior art: ERA = LLM code-mutation + **tree search
  against an automatic quality metric** with idea injection/recombination (S-002); Co-Scientist = **tournament +
  evolution** with meta-review feedback (S-004); the harness survey frames exactly our situation — a **Meta-Harness
  outer loop** where an agentic proposer iterates *harness* (= loop) designs against a benchmark, and shows
  **harness-level changes alone (fixed model) drive large gains** (S-005). **We adopt** this framing: our Experiment
  Loop is a Meta-Harness outer loop searching Agentic-Loop designs against our quantification metric.
- **Controlled experiment discipline** (classical DoE): **one manipulated variable per experiment** (the improvement
  category), **fixed controls** (word-identical tests; the blank-CS baseline always in a fresh, memory-free project;
  no drift), and **replication** — Co-Scientist/Robin variance motivates **≥2 runs + mean** per setup (S-003, S-004).
- **Inter-rater reliability** for the human eval: report agreement (e.g. weighted κ / ICC) when >1 rater or across
  repeated items, per standard practice (S-008 for judges; κ methodology noted for the operator-vs-panel agreement).

## What this buys us (credibility)
Every measurement choice above is anchored in named prior work, so a Gladstone judge sees a **methods section**, not
asserted numbers: blinded head-to-head (S-006), CoT form-filling judges with bias controls + panel (S-007, S-008),
creativity as novelty×usefulness (S-009) with distance-based novelty (S-010), and a Meta-Harness outer loop (S-005).
