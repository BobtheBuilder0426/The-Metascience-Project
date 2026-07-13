<!-- WORKED EXAMPLE of the fused topic_brief.md the module would hand the driver. Demonstrates the quality bar:
     built from 7 quality/recency-filtered, DOI-verified, retraction-screened sources (see worked_example_sources.json),
     NOT stale high-cited consensus. Topic seeded from the ergothioneine question. Concise (~1.5 pp). -->

# Topic brief: ergothioneine → exercise performance, mitochondria, aging
*Built by the multi-model context module (worked example). Sources: 10 primary+review, 2022–2025, all DOI-verified, 0
retracted. The selection used a **novelty-aware quality filter** (recency + primary-vs-review + topical specificity +
citation-momentum, per S-047/S-049) — a generic 2,318-citation ROS review and two off-topic SIRT6 reviews were RETRIEVED
but DROPPED (q=0.24–0.39) **even though they had high citation momentum**, because the topical + primary signals
correctly override raw citation velocity for off-topic consolidation. The brief is built on recent primary mechanism
work (top sources q=0.97), not stale consensus — exactly the "no shitty old same-idea papers" bar.*

## What's established
- Ergothioneine (ET/EGT) is a diet-derived thione that **improves exercise/aerobic performance and mitochondrial
  function**, now with two independent 2025 mechanisms in *Cell Metabolism*: an **ET→CSE→H₂S→cGPDH-persulfidation→NAD⁺**
  axis improving aged-animal healthspan (DOI 10.1016/j.cmet.2024.12.008), and a direct **ET→MPST activation** axis
  controlling mitochondrial function + exercise performance (DOI 10.1016/j.cmet.2025.01.024). These are the two
  load-bearing primary papers and they converge on mitochondria via different effectors.
- Independent work reports **ET boosts mitochondrial respiration + exercise performance** (preprint
  10.1101/2024.04.10.588849), consistent with the two mechanisms above.
- ET's benefits extend across aging phenotypes: **age-related hearing loss** slowed (10.1016/j.heares.2024.109004) and
  **aerobic performance improved without negative effects** (review 10.3389/fphys.2022.834597).

## What's actively contested / emerging (where the two model passes flagged disagreement)
- **Which effector dominates in mammalian muscle** — CSE/H₂S/cGPDH vs direct MPST activation. The two 2025 papers each
  center a different node; whether they are parallel, sequential, or tissue-specific is unresolved. (Flagged as
  disagreement, not blended — the driver should treat this as an open mechanistic question, a strong place to propose a
  discriminating experiment.)
- **Antioxidant vs enzymatic framing** — older literature frames ET as an antioxidant; the recent primary work argues a
  defined enzymatic/persulfidation mechanism. The brief sides with the recent primary evidence and notes the antioxidant
  framing is the superseded prior.

## What's NOT known (gaps = opportunity for a landmark answer)
- Tissue-level ET bioavailability + dosing in mammals for a performance effect.
- Whether the CSE and MPST axes can be co-targeted or are redundant.
- Human exercise data (most mechanism data are worm/rodent/cell).
- Persulfidation targets beyond cGPDH that contribute to the phenotype.

## Highest-quality primary sources to build on
1. 10.1016/j.cmet.2024.12.008 — ET→CSE→cGPDH→NAD⁺, healthspan (Petrovic 2025, Cell Metab). [primary]
2. 10.1016/j.cmet.2025.01.024 — ET→MPST, mitochondria + exercise performance (Sprenger 2025, Cell Metab). [primary]
3. 10.1101/2024.04.10.588849 — ET boosts mito respiration + exercise (2024 preprint — flag as not-yet-peer-reviewed). [primary]
4. 10.1016/j.heares.2024.109004 — ET slows age-related hearing loss (2024). [primary]
5. 10.1186/s12917-023-03584-6 — docking + validation of an ET effect (2023). [primary]

*Reviews retained for framing only: 10.1002/1873-3468.14299 (ET decline in frailty/cognition), 10.3389/fphys.2022.834597
(ET + aerobic performance). Generic ROS/SIRT6 reviews were dropped.*

---
**Fairness note (for the run bundle):** this brief is a loop-only advantage; the baseline arm receives none of it. It
was built from the 7 sources listed in `worked_example_sources.json`. Any "loop beat baseline" comparison must record
that the driver was self-briefed from these sources.
