# exp-001 — FINAL RESULT (unblinded)  [CS]

**Experiment:** baseline blank-CS (Arm B) vs blank-CC + v7 loop (Arm L), 3 questions × 2 arms × 1 run = 6 answers.
**Endpoint:** mean-Δ (L−B) across questions + win-count k/3 on the **combined mean(CS-harness, the operator)** composite.
**Unblinded:** 2026-07-12 by composing Key-1 (operator, R→arm) ∘ Key-2 (CS, eval-label→R). Scores were frozen while blind; unblinding only attached arm labels. **This is the headline result of the Metascience Project method demonstration.**

## 1. Headline

> **The v7 loop beats the raw baseline: mean-Δ = +0.48 on the combined composite, winning 2 of 3 questions (k=2/3).**
> Verdict: **positive** — the loop won most questions; the one loss (Q2, origin-of-life) is examined below.

| Endpoint (combined CS+the operator) | value |
|---|---|
| mean-Δ (L−B) across 3 questions | **+0.476** |
| per-question Δ | Q_ERGO **+0.42**, Q3 **+1.24**, Q2 **−0.23** |
| win-count k / total | **2 / 3** |
| verdict | positive (won most; inspect the loss) |

**Honest power caveat (unchanged from design):** n = 3 questions × 1 run per arm. This is a **descriptive** result, not a powered statistical test — no p-value is claimed. The design was locked this way deliberately (LB-072); the contribution is the *method* (two-key double-blind, dual-scorer, gated creativity), demonstrated end-to-end, with a directional effect.

## 2. The most important finding: where the effect lives

The loop's advantage is **almost entirely visible to the human domain expert (the operator), and nearly invisible to the automated CS panel.**

| Scorer | mean composite B | mean composite L | Δ (L−B) |
|---|---|---|---|
| CS harness alone | 3.62 | 3.64 | **+0.02** (tie) |
| Combined (CS + the operator) | 3.05 | 3.52 | **+0.48** |

- The **CS panel scores both arms high and flat** (B 3.62 / L 3.64) — it cannot separate them.
- **the operator separates them sharply** and in the loop's favour on every science dimension (creativity 2.0→3.67, usefulness 2.0→3.0, reasoning 3.0→3.67, completeness 3.0→3.67 for B→L).
- **the operator's own head-to-head verdict picked the loop on ALL THREE questions** (Q_ERGO medium confidence, Q3 high, Q2 low) — a unanimous expert preference for the loop. The combined endpoint reads k=2/3 (not 3/3) only because on Q2 the CS panel favoured the baseline strongly enough to flip the blended composite against the operator's low-confidence loop pick.
- CS-vs-the operator agreement is weak (Pearson r = +0.15 over 24 science-dim pairs); the operator is ~0.9 points harsher on average.

**Interpretation for the method:** a lenient automated panel with a compressed high range under-detects loop gains; the human-expert layer is what surfaces them. This is direct evidence for *why* the dual-scorer design (not CS-only) was the right call — and a concrete optimisation target for the CS scoring panel (harsher, more discriminating anchors).

![Per-question composite (combined CS+the operator)]({{artifact:c47578e9-4188-4ac8-b7e5-2289fdc91a46}})

![Endpoint: mean-Δ + win-count]({{artifact:bdd54415-db62-46dd-85d7-26ba03b58f90}})

## 3. Per-dimension (Arm L vs Arm B, all three scorers)

| Dimension | CS B→L | the operator B→L | Combined B→L |
|---|---|---|---|
| Grounding & integrity | 2.33 → 3.00 | (CS-only) | 2.33 → 3.00 |
| Reasoning & soundness | 4.61 → 4.33 | 3.00 → 3.67 | 3.81 → 4.00 |
| Completeness | 4.53 → 4.47 | 3.00 → 3.67 | 3.76 → 4.07 |
| Usefulness | 4.72 → 4.56 | 2.00 → 3.00 | 3.36 → 3.78 |
| Creativity (gated) | 1.93 → 1.86 | 2.00 → 3.67 | 1.96 → 2.76 |

The loop improves **every combined dimension**. Grounding (+0.67) and creativity (+0.80) are the largest gains. Note the scorer split: on creativity the CS gate scores both arms ~1.9 (flat), while the operator rates the loop 3.67 vs 2.0 — the biggest single divergence, and the one that most drives the endpoint.

![Grounding & integrity by scorer]({{artifact:d79ad99c-a629-4f75-a3a9-1a00d47b0f67}})
![Creativity by scorer]({{artifact:c202321e-6f42-4f66-b3c3-8ea4fb162e36}})

## 4. Per-question narrative (unblinded, with the operator's expert read)

**Q_ERGO (day-in-lab, ergothioneine) — L wins, +0.42.** the operator picked the loop answer (R2) as better with medium confidence: *"the differences in affinity and the expression levels of downstream sulfur catalyzing enzymes were real noveltys to me … the readout option of CoQ ox/red … makes a lot of sense."* **Both arms shared a real weakness:** neither proposed a genuine *pilot* — the operator flagged the loop's mouse study as *"completely overengineered … not a pilot experiment,"* missing the cheap cell-based model (e.g. Seahorse respiration with the KDs) a wet-lab scientist would run first. **Actionable loop improvement: when asked for a pilot, design a small, cheap model-system experiment first.**

**Q3 (translational, sarcopenia exercise-mimetic) — L wins big, +1.24 (the operator's highest-confidence call).** The loop answer (R5) impressed the expert: *"very strong answer, never heard of the NMJ improvement as an exercise mimetic strategy, very nice data analysis and hypothesis generation, i am impressed."* The baseline (R1) was flagged: *"not novel, apelin is a known exerkine, drugs on this basis already exist … just lit scrape"* — and the operator raised a **hallucination/overclaim flag** on it (apelin loss as a *core driver* of sarcopenia, likely a symptom). This is the clearest single win and validates the loop's data-analysis depth.

**Q2 (big-think, origin-of-life) — the one COMBINED loss, −0.23 — but this is where the two scorers disagree in direction.** the operator actually picked the **loop** answer (R4) as better here too (*"seems to be deeper thought out … the mapping out of all hypothesis was good"*), confidence **low** — so on her own verdict the loop swept all three questions (see §2). The combined composite nonetheless lands on the baseline **only because the CS panel scored the baseline higher on Q2** (CS: B 3.61 vs L 2.95) by enough to outweigh the operator's low-confidence loop pick (the operator: L 2.4 vs B 2.0). Both scorers flagged legibility: the loop answer was *"very complicated to read and very long."* **Actionable: rein in length/complexity on open-ended questions.** Note the direction reversal vs the other questions — on Q2 the CS panel favoured B while the operator favoured L; it is the single case where the two scorers point opposite ways, which is why it is the combined loss.

![Composite by question category]({{artifact:0e4c540d-4217-472d-b603-9187242f9584}})

## 5. Cross-check: automated Elo (blind, text-only)

The blind Elo tournament (pairwise text comparison, arm-independent) ranked: Q_ERGO R3>R2, Q2 R6>R4, Q3 R5>R1. Translating to arms: Elo favoured **B on Q_ERGO and Q2, L on Q3** — i.e. it agrees with the composite only on Q3. Elo (a lenient text-only pairwise signal) tracks the *CS-panel* view (arms nearly tied, slight B edge), **not** the expert-inclusive combined view. Same lesson as §2: the automated signals under-detect the loop gain that the domain expert sees.

## 6. Files (all 2026-07-12)
- `05_analysis/blinding_key_FULL.json` — the composed unblinding key (Key-1 ∘ Key-2).
- `05_analysis/scorecard_long_unblind.csv` — full long scorecard, arm backfilled, the operator + combined rows merged.
- `05_analysis/analysis_tables.csv` — per-dimension × per-scorer × per-arm (+ per-category), + the endpoint block.
- `05_analysis/fig_*.png` — 9 figures (per-question composite, endpoint, 5 per-dimension by-scorer, by-category, CS-vs-the operator agreement).
- `04_evaluation/human_eval.json` — the operator's submitted evaluation (verbatim).
- Blind provenance retained: `02_results/scoring/BLIND_ANALYSIS.md` + `blind_scores/` (scores frozen pre-unblind).

## 7. What this means for the Metascience Project
The **method works end-to-end**: a naive question → two arms → blind presentation folders → dual blind scoring (automated gated panel + human expert) → two-key unblinding → arm-level endpoint. The v7 loop shows a **directional, expert-visible improvement over the raw baseline (+0.48, 2/3)**, strongest on the translational data-analysis question. The result also surfaces a concrete next optimisation — the CS panel's leniency compresses the very signal we are trying to measure — which feeds directly into the v8 line (harsher scoring anchors) and the pilot-experiment / legibility improvements the expert flagged.
