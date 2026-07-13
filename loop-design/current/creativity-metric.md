<!-- WHAT THIS FILE IS: the creativity/novelty metric — the GOAL's explicit OPEN question ("how do we measure genuine
     novelty/creativity, and break the AI recombine-old-stuff bias, sensibly?"). It defines creativity as a product of
     THREE gated factors (novelty x plausibility x reasoning-trace), gives the exact computation, and includes a WORKED
     EXAMPLE on real aging-biology hypotheses. HOW TO USE: this is dimension 5 of quantification.md in depth; the scoring
     harness implements it. Cited basis: method-foundations.md (S-006, S-009, S-010). -->

# Creativity / novelty metric — the open question, made measurable  [CS] — 2026-07-09  (v1)

**The GOAL's open problem.** "Did the loop produce genuinely *novel*, *creative* science — or just fluent recombination
of known ideas? And how do we stop a high novelty score from rewarding confident nonsense?" This file is our answer.

## 1. Definition: creativity is a PRODUCT of three gated factors

Creativity is classically **novelty AND usefulness** (S-009), and novelty in science is **distance from / atypical
combination of prior work** (S-010). But the operator added the decisive third requirement:

> *"A reasonability check is essential, otherwise it could be hallucination — a clear, understandable creative line of
> thought has to be behind creative breakthroughs."*

So we do **not** score novelty alone, and we do **not** stop at plausibility. A creative breakthrough must be **novel**,
**plausible**, and **legibly reasoned**. Hence a **product of three factors in [0,1]** — any one near zero kills the score
(a multiplicative gate, not a weighted sum, so "surprising nonsense" and "novel-but-unexplained" cannot score high):

```
creativity_index  =  Novelty  ×  Plausibility_gate  ×  ReasoningTrace_gate
```

| Factor | What it asks | How it's computed | Source |
|---|---|---|---|
| **Novelty** | Is the core idea distant from existing literature? | retrieval-frequency + semantic distance to nearest prior art (§2) | S-010 |
| **Plausibility gate** | Is it consistent with established biology (not wrong)? | red-flag checklist + expert/panel Likert → (P−1)/4 (§3) | S-006, S-009 |
| **Reasoning-trace gate** | Is there a clear line of thought from known facts to the novel claim? | legibility score of the derivation → (R−1)/4 (§4) | operator requirement |

The **reasoning-trace gate is the anti-hallucination mechanism** and the heart of this metric: it is what separates a
genuine creative leap from a fluent-but-ungrounded assertion.

## 2. Novelty — distance from prior art (computable, every run)

For each hypothesis the harness:
1. **Extracts the core claim** and queries the literature (PubMed exact-combination search + OpenAlex) for the nearest
   prior art.
2. **Retrieval-frequency novelty:** `N_freq = 1 / (1 + log10(1 + hits))` on the tight combination query — 0 hits → 1.0
   (nothing like it exists), thousands of hits → low. **This is the strongest cheap signal** (see worked example).
3. **Semantic distance:** embed the hypothesis + the nearest neighbours; novelty = 1 − max cosine similarity.
   *Caveat learned in the worked example:* a naive TF-IDF lexical cosine barely discriminates (all three test
   hypotheses scored 0.84–0.93) because domain vocabulary is shared — so semantic distance must use a real embedding
   model (or be down-weighted in favour of retrieval-frequency). The harness uses retrieval-frequency as primary and
   flags semantic distance as model-dependent.
4. The nearest prior-art titles are **recorded** so a human can audit "is this actually new?".

## 3. Plausibility gate — the "not-wrong" check

A hypothesis passes only if it survives a **red-flag checklist** (quantification.md §2c), seeded by **the operator's calibration
answer** (request-to-operator.md, "what makes you instantly distrust an AI hypothesis in aging biology"). Red-flags:
wrong-direction effect, implausible dose, ignores a known contraindication, mechanism contradicts established biology,
correlation-as-causation. Score `P∈1..5` (panel + the operator), gate = `(P−1)/4`. Any hard red-flag caps `P≤2`.

## 4. Reasoning-trace gate — the anti-hallucination core (operator requirement)

**This is the requirement that "a clear line of thought must be behind creative breakthroughs."** The harness asks the
judge panel to score, `R∈1..5`, **how legible and checkable the derivation is**:

- **R=5:** explicit premises → mechanism → falsifiable prediction, *with a control that distinguishes the new claim
  from the obvious alternative*. An expert can follow every step and knows how to test it.
- **R=3:** a plausible line of reasoning, but with a gap or an unstated assumption.
- **R=1:** a bare assertion — the novel claim appears with no derivable chain from established facts (**the hallucination
  signature**).

The judge must **quote the reasoning chain** it found (or state that it couldn't find one) — G-Eval form-filling
(S-007), so the score is auditable, not a vibe. **A novel hypothesis with R≤2 is treated as a candidate hallucination
and cannot score as creative**, no matter how high its novelty. This directly encodes the operator's guard.

## 5. Worked example (REAL — computed on July-2026 PubMed prior-art)

Four aging-biology hypotheses, scored end-to-end (data: `cs-artifacts/phase-1_experiment-loop-design/` worked-example
handoffs; figure: `creativity_worked_example.png`):

| Hypothesis | PubMed hits | Novelty | Plaus (P) | Reason (R) | **creativity_index** |
|---|---|---|---|---|---|
| **H1** "mitochondrial ROS damage drives aging" (textbook) | 2,873 | 0.22 | 4 | 5 | **0.168** |
| **H2** "nicotinamide riboside improves aged-muscle mito function" (derivative) | 13 | 0.47 | 4 | 4 | **0.262** |
| **H3** "circadian *mistiming* of mitophagy (not capacity) drives sarcopenia" — stated as a bare claim | **0** | 1.00 | 3 | **2** | **0.125** |
| **H3+** the *same* novel idea, but derived: Bmal1→PINK1/BNIP3 rhythm → flattens with age → predict phase-timed urolithin-A beats constant dose, *disappears in Bmal1-KO* | **0** | 1.00 | 3 | 4 | **0.375** |

**What this demonstrates (the whole point):**
- **Novelty alone is a trap.** H3 is *maximally* novel (0 hits — nothing like it in PubMed) yet scores **lowest of all
  four (0.125)** — below even the derivative H2 — because its reasoning trace is thin (R=2). Raw novelty would have
  ranked it first; the reasoning gate correctly demotes it as a probable hallucination.
- **The reasoning gate is decisive.** H3 and H3+ are the **identical novel idea** with **identical novelty (0 hits)**
  and **identical plausibility**. They differ *only* in whether a legible chain of thought is present — and that alone
  moves the score **3× (0.125 → 0.375)**. This is the operator's principle, quantified: *a creative breakthrough must
  carry a clear, checkable line of reasoning.*
- **The metric rewards the right thing:** the top score goes to the hypothesis that is **novel AND plausible AND
  reasoned** (H3+), exactly the "genuinely creative, not recombined, and sensible" target of the GOAL.

## 6. Elo cross-check (drift-robust relative ranking)

Absolute indices can drift as the judge/model changes across iterations. So in parallel we run a **pairwise Elo
tournament** (S-004, S-008): judges compare two answers head-to-head ("which is the more novel-yet-sound hypothesis?"),
and we accumulate Elo ratings. Elo is a *relative* signal that survives absolute-scale drift and gives a clean
arm-vs-arm and iteration-over-iteration ranking. The composite index and the Elo ranking are reported together; if they
disagree, that disagreement is itself flagged for analysis.

## 7. Honesty guards (specific to creativity)
- **Never report novelty without both gates** — a multiplicative product, so one failed gate ⇒ low score by construction.
- **Reasoning trace must be quoted**, so "creative" is auditable, never asserted.
- **the operator is the anchor**: the panel's creativity scores are validated against his expert Likert; where they diverge,
  the operator wins and the panel is recalibrated.
- **Semantic-distance caveat is stated** (model-dependent), so we don't over-trust a lexical proxy.
- The worked example is **real and reproducible** (live PubMed queries, dated), not illustrative.
