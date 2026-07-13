<!-- Authored by [CS]. Literature-grounded design for CS's OWN scoring judge panel (the "ruler" that measures
     loop-vs-baseline output). Mimics journal/hackathon reviewers per operator instruction (LB-032). ACCEPTED by the
     operator 2026-07-09 (LB-034): the 3-persona jury as proposed. NOT the loop-under-test's lenses (those are a separate
     improvement category). -->

# CS Scoring — Reviewer-Panel Design (literature-grounded)  [CS] — ACCEPTED (3-persona jury, LB-034)

## 0. Scope (the locked distinction — LB-032)
This document designs **set (B): CS's own scoring panel** — the instrument CS uses to judge the quality/creativity/
usefulness of what each arm produced. It is **NOT set (A)**, the lenses *inside* the CC/CS agent-loop under test
(multi-model Codex + ambitious-postdoc-vs-mentoring-PI), which are an improvement category CS builds and tests. Using the
loop's creative-tension lenses as the ruler would confound the thing-optimized with the thing-measuring; they stay
separate. **CS's side has Claude-family models only** (`host.list_models()` → claude-sonnet-5 / opus-4-8 / …; no GPT/
Codex), so this panel is Claude-based reviewer *personas*, diversified by system-prompt + sampling, honestly labeled
within-vendor.

## 1. What the evidence says (grounded)
- **A panel beats a single judge.** Verga et al. 2024 ("Panel of LLM evaluators", PoLL) show a *panel of diverse models*
  outscores a single large judge, at lower cost, while reducing the intra-model bias a lone judge injects
  (10.48550/arXiv.2404.18796). We adopt the panel principle; our diversity axis is persona+sampling (not vendor), since
  CS is single-vendor.
- **Distinct reviewer ROLES, made to deliberate, improve agreement with humans.** Chan et al. 2023 (ChatEval) show
  multiple judges with *different role prompts* that communicate/debate track human judgement better than one judge
  (10.48550/arXiv.2308.07201). This is the direct license for reviewer *personas* + a synthesis step.
- **LLM judges carry systematic biases that must be engineered out.** Wang et al. 2023 document *position bias* and give
  mitigations — swap/randomize order, multi-evidence calibration, voting (10.48550/arXiv.2305.17926). Zheng et al. 2023
  (MT-Bench) add *verbosity* and *self-enhancement* bias and validate agreement-with-humans + pairwise Elo
  (10.48550/arXiv.2306.05685). Self-enhancement is our sharpest risk (Claude judging Claude) and — since we can't cross
  vendors — is mitigated by **blinding + the the operator human anchor**, stated honestly, not by a non-Claude judge.
- **Fine-grained scores need explicit per-criterion rubrics.** Kim et al. 2023 (Prometheus) show 1–5 scoring aligns with
  humans only when each criterion has explicit score descriptions (10.48550/arXiv.2310.08491). Our rubric is already
  anchored this way; the panel must be *conditioned on the anchored rubric*, not free-scoring.
- **Chain-of-thought + form-filling raises human correlation.** Liu et al. 2023 (G-Eval) — judges reason step-by-step,
  then fill the score form (10.18653/v1/2023.emnlp-main.153). We keep G-Eval-style scoring.
- **For research-idea judging specifically, the gold standard is a blinded expert panel over novelty + feasibility.**
  Si, Yang & Hashimoto 2024 ran 100+ NLP researchers, blinded, scoring AI-vs-human ideas (10.48550/arXiv.2409.04109) —
  the template for our reviewer axes and for pairing the machine panel with the operator's blinded human read.
- A 2025 survey (Li et al., "From Generation to Judgment", 10.18653/v1/2025.emnlp-main.138) consolidates the above into
  the standard bias-controls + panel-aggregation playbook we follow.

## 2. Proposed panel — "mimic 2–3 journal/hackathon reviewers" (operator's instruction)
Three reviewer *personas*, each a Claude call with its own system prompt, scoring **blinded** + **rubric-conditioned** +
**G-Eval style** (reason, then fill the form). Personas mirror a real review committee — they judge the SAME anchored
rubric, but weight what they scrutinize differently (this is role-diversity per ChatEval, not different rubrics):

| # | Persona | What it scrutinizes (mimics…) | Emphasis |
|---|---|---|---|
| R1 | **Rigor / Methods reviewer** | a demanding journal methods referee | correctness, grounding, is the experiment/logic sound + falsifiable |
| R2 | **Significance / Impact reviewer** | a top-venue "so what?" referee | usefulness, completeness, would this matter to the field |
| R3 | **Novelty / Creativity reviewer** | a hackathon judge + idea-study rater (Si et al.) | creativity, is the idea genuinely new + non-obvious vs prior art |

- **Aggregation:** per-dimension = mean of the 3 personas; report **inter-reviewer spread** (disagreement = low
  confidence, flag it). No persona is the "decider"; this is a jury (PoLL), not a chair.
- **Why 3 and these 3:** they cover the rubric's load-bearing axes with the reviewer archetypes a journal/hackathon
  actually fields; odd number breaks ties in the Elo pairwise votes; 3 Claude calls × answers stays inside the laptop's
  bounded compute.

## 3. Bias controls (engineered in, from the evidence)
1. **Blinding** — arm identity + any "produced by a loop" cue stripped before judging (self-enhancement, halo).
2. **Order randomization / swap** — in every pairwise Elo comparison, present both orders (or randomize) and average →
   kills position bias (Wang et al.).
3. **Rubric-conditioned, anchored** — each 1–5 has an explicit descriptor (Prometheus); judges may not free-score.
4. **CoT + form-filling** — reason first, then emit the JSON score (G-Eval).
5. **Human anchor, not vendor-diversity** — self-enhancement can't be removed by a non-Claude judge here, so we *measure*
   it: report judge-vs-the operator agreement (weighted κ / correlation) on every item the operator scores; if the panel tracks the operator we
   trust it on un-scored items, else down-weight it. Honestly labeled within-vendor.
6. **Temperature/seed diversity** — the 3 personas run at modest temperature with different seeds so they are not 3
   identical samples.

## 4. Outputs (quantifiable + plottable for submission)
Per answer: 3× per-dimension reviewer scores + mean + spread; the weighted composite; the creativity index (separate
module). Per question: the Elo ranking. All numeric → bar charts (per-arm dimension means ± spread), an Elo table, and a
judge-vs-the operator agreement plot. These are D2/D4 submission figures.

## 5. Decision + remaining tuning
- **DECIDED (operator accept, LB-034):** the **3-persona jury** (R1 Rigor, R2 Significance, R3 Novelty/Creativity) as
  proposed. Persona system prompts drafted + frozen into the harness `judge.py` (REVIEWER_PERSONAS).
- **R3 vs the creativity index:** kept DISTINCT — R3 is a human-style creativity referee; the creativity index is the
  mechanical Novelty×Plausibility×ReasoningTrace metric. Overlap noted; both reported (they cross-check each other).
- **Minor, tunable without re-accept:** the the operator-agreement stat (weighted-κ vs correlation) — small-n, so report both +
  raw diffs. Persona sampling temperature to be set at first real run.

## 6. Provenance
Grounded in 8 papers: Verga 2024 (PoLL, S-017), Chan 2023 (ChatEval, S-018), Wang 2023 (unfair evaluators, S-019), Kim
2023 (Prometheus, S-020), Li 2025 (survey, S-021) — all new this session; plus Si 2024 (idea study, S-006), Liu 2023
(G-Eval, S-007), Zheng 2023 (MT-Bench, S-008) — existing. DOIs for the 6 arXiv/EMNLP works added this session were
title-confirmed (arXiv API / crossref); the two carried over from S-006/7/8 were verified when first registered (LB-014),
and MT-Bench's DOI returned only a weak existence flag this session (title not re-confirmed) — it stands on its LB-014
registration. Supersedes the "PI-vs-postdoc / non-Claude judge" framing that wrongly imported the loop's lenses into the
ruler (retracted, LB-032).
