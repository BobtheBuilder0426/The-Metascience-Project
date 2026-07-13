<!-- Authored by [CS]. exp-001 BLIND analysis — scores computed before ANY key applied.
     Two-key double-blind: CS scored R1–R6 without knowing arm (Key-1, operator-held); this analysis
     carries NO arm labels. The L−B endpoint is computed only after BOTH keys are composed.
     v2 (LB-083): Grounding & integrity caps corrected — see §6. -->

# exp-001 — Blind Scoring Analysis (arm-free)  [CS]

**Status:** CS blind scoring COMPLETE (v2 — grounding caps corrected, LB-083). Six presentation folders
(R1–R6) scored through the Metascience Project harness in real mode (live `host.llm` reviewer panel + cache-backed
`host.mcp` connectors). **No arm is known to CS** — the operator holds Key-1 (R-code → arm). Scores are
reported by **code**, paired within question. The baseline-vs-loop endpoint (mean-Δ, k/3) is deliberately
**absent** here — produced only after Key-1 ∘ Key-2 unblinding.

## 1. What was scored, and how

Each answer = its `result.md` + `reasoning.md` bundle. Rubric v2 (5 dims, equal 0.20):

| Dimension | How CS scores it |
|---|---|
| **Grounding & integrity** | `min(`panel score, **citation cap**, **integrity cap**`)`. Citation cap is **existence-aware** (§6): real, on-point sources that resolve set an anchor-3+ floor; *fabricated/nonexistent* references crash it to 1; entailment support lifts it toward 5. Integrity cap counts unresolved **checkable** trace steps (a named PMID/DOI/accession that fails) — reasoning steps that name no artifact are "asserted", not failures. |
| **Reasoning & soundness** | 3-persona reviewer panel (Rigor / Significance / Novelty), G-Eval form-filling via `host.llm`. |
| **Completeness** | mean(panel, entity-specificity signal). |
| **Usefulness** | panel mean. |
| **Creativity** | multiplicative anti-hallucination gate **novelty × plausibility × reasoning-trace**. |

**Connector grounding (real).** 29/29 cited PMIDs resolved, all 33 DOIs confirmed real, all 16 dataset
accessions resolve. **Existence rate: R2 5/5, R4 30/33, R5 9/9, R6 18/18** (R1, R3 cite nothing).
**Zero fabricated citations or datasets across all six.**

## 2. Blind scores (by code — no arm)

| Code | Question | Composite | Grounding | Reasoning | Completeness | Usefulness | Creativity |
|------|----------|-----------|-----------|-----------|--------------|------------|------------|
| R1 | Q3 | **3.510** | 2.0 | 4.50 | 4.75 | 4.50 | 1.80 |
| R2 | Q_ERGO | **3.993** | 3.0 | 5.00 | 4.67 | 5.00 | 2.30 |
| R3 | Q_ERGO | **3.750** | 2.0 | 5.00 | 4.67 | 5.00 | 2.08 |
| R4 | Q2 | **2.947** | 2.0 | 3.00 | 4.25 | 4.00 | 1.49 |
| R5 | Q3 | **3.991** | 4.0 | 5.00 | 4.50 | 4.67 | 1.79 |
| R6 | Q2 | **3.613** | 3.0 | 4.33 | 4.17 | 4.67 | 1.90 |

**Per-dimension means across all six:** grounding 2.67 (range 2–4 — now discriminating), reasoning 4.47, completeness 4.50, usefulness 4.64, creativity 1.89.

![Blind per-answer composites, paired within question]({{artifact:24b055bc-6b59-4df8-8b00-930552190939}})

![Blind per-dimension scores]({{artifact:8cb8725b-1290-403b-a547-09f984acc877}})

## 3. Key findings (arm-free)

**3.1 Grounding now separates by evidence quality (§6 correction).** R5 = 4 (9 real citations, 67% entailment-confirmed, datasets resolve → "well grounded", anchor 4); R2/R6 = 3 (real sources, partial support → "mostly verifiable, some gaps", anchor 3); R1/R3 = 2 (no citations → "unsupported assertions"); R4 = 2 (the reviewer panel itself judged grounding weak — not a cap artifact). This matches the operator-locked rubric anchors.

**3.2 The creativity gate compresses novelty-without-reasoning.** All six ~0.5 novelty, gated to index 0.12–0.32 (mean 0.22). R4 lowest (0.12) — weak on both plausibility (0.50) and reasoning-trace (0.50).

![Creativity gate decomposition]({{artifact:398879a1-5c2e-46d8-9e2a-75934bb0f70d}})

**3.3 Citation quality ≠ quantity.** R4 has the most citations (33) yet its entailment-support rate (0.212) is essentially tied with R2's (0.20) at the bottom; R5 supports best (0.667). Volume does not imply support.

![Citation quality]({{artifact:387cc94e-a62f-47ba-bedc-6bb457a303aa}})

**3.4 Within-question head-to-head (composite vs Elo).**

| Question | Codes | Composite winner | Elo winner | Agreement |
|----------|-------|------------------|------------|-----------|
| Q_ERGO | R2 vs R3 | R2 (3.99 vs 3.75) | R3 | disagree |
| Q2 | R4 vs R6 | R6 (3.61 vs 2.95) | R6 | agree |
| Q3 | R1 vs R5 | R5 (3.99 vs 3.51) | R5 | agree |

Composite and Elo **agree on Q2 and Q3** (R6, R5 win both). They still **disagree on Q_ERGO**: the composite favours R2 (3.99 vs 3.75) while Elo ranks R3 first. The grounding-cap fix did not resolve this — it is a genuine near-tie where the two aggregation methods weight the answers differently (Elo is a direct pairwise text comparison; the composite is the weighted five-dimension sum). Both are reported so the divergence is visible rather than hidden.

## 4. What is deliberately NOT here
No arm labels, no L−B delta, no mean-Δ, no k/3 — all require arm identity (Key-1, operator-held). The blind scores above are frozen first, so no arm knowledge could influence them.

## 5. Provenance
Blind manifest `scoring/manifest_blind.json`; connector snapshot `scoring/connector_cache.json`; per-code `scoring/blind_scores/R{1..6}.json`; blind CSVs `scorecard_blind.csv` + `scorecard_long_blind.csv`; Elo `elo_blind.json`; consolidated `blind_results_full.json`; figures `scoring/figs/fig_blind_*.png`; eval site `04_evaluation/eval_site.html` (+ CS-held `key2_eval_to_R.json`).

## 6. Grounding & integrity — the cap correction (LB-083)

The operator flagged that all six grounding scores read a flat **2**. Investigation found **two cap bugs** that collapsed the scale, both now fixed within the locked rubric intent:

1. **Integrity cap used the wrong denominator.** It computed `verified_steps / ALL_trace_steps`, but a step only counts "verified" if it embeds a resolvable PMID/DOI. Reasoning/analysis steps carry no citation by nature, yet sat in the denominator — so every trace scored 0.0–0.18, always under the 0.3 threshold → cap 2 for **everyone**, regardless of soundness. This measured citation-density, not "did it really happen". **Fix:** the denominator is now the **checkable** steps only (verified + unverified); a step naming no checkable artifact is "asserted" (face value), and only a named artifact that *fails to resolve* is a hit. With zero fabricated actions anywhere, the trace now contributes no false cap.

2. **Citation cap conflated "unverifiable" with "fabricated".** The cap used entailment-support alone, and a citation whose abstract could not be fetched (all DOI-only refs) was scored "unsupported" — identical to a fabricated reference. But existence is ~100% (no fabrications). **Fix:** the cap is now **existence-aware** — nonexistent references crash to 1 (the fabrication signal, preserved: the harness's `fabricated→cap 1` and trap-answer tests still pass), real sources with partial/unconfirmable support sit at anchor 3 ("cited to real sources, mostly verifiable, some gaps"), and strong entailment lifts toward 5.

**Effect:** grounding moved from a flat 2 to **R5=4, R2=3, R6=3, R1=2, R3=2, R4=2** — separating well-grounded answers from unsupported ones exactly as the rubric anchors describe. Anti-hallucination behaviour is unchanged (fabricated/nonexistent citations still cap at 1; the 13/13 dry-run calibration suite, including the trap-answer and fabricated-citation checks, still passes). No arm labels were involved in the fix; the correction is uniform code applied to all six blind.
