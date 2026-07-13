# ReCAST — reasoning trace

Compact, scannable logic behind each step. Labels: **[computed]** = my own analysis here; **[fact]** = directly supported by a cited retrieved source; **[inference]** = reasoned from established facts; **[proposed]** = design choice.

**Status of this document:** ReCAST is presented as a discovery *method*; the run below is a **retrospective proof-of-concept instantiation** on real data, not a prospectively-frozen, blinded discovery run. Where a stage was executed below its full specification (curated panel vs transcriptome-wide; literature score vs quantitative reversal; hand-curated shortlist vs metabolome-wide universe; consistency check vs blinded benchmark), that is stated explicitly. No hashed frozen protocol or timestamped coded ledger was created prospectively, so no blinding is claimed.

## A. Why a new method is needed
- Existing metabolite-cocktail discovery tends to nominate from what *changes* in a youthful/plastic/regenerative state, then supplement it.
- **Direction failure** [inference]: one-carbon flux (incl. methionine) rises in early cell-identity transitions, but methionine *restriction* extends healthspan/lifespan **[fact: PMID 34518687]**. Supplementing "what rises" can invert the intended effect.
- **Rejuvenation vs regeneration** [inference]: satellite-cell / central-nucleated-fiber / Pax7⁺ readouts are injury-repair markers; an agent that causes low-grade damage-and-repair scores as "recovery" without reversing aging.
- ReCAST's two design commitments: (1) nominate by **signed causal direction**, not abundance change; (2) target **uninjured** aged muscle with a function-first, confound-gated readout.

## B. S1 — the target signature (computed, curated panel)
- **Scope:** a **curated 56-gene panel** across 9 mechanistic categories, NOT a transcriptome-wide/deconvolved/replicated signature. All "strongest/cleanest" statements are **panel-internal**. Gene-**expression** associations are not metabolite abundance or pathway flux.
- Source: GTEx v8 skeletal muscle, 803 RNA-seq donors. **[computed]**
- **Age encoding** [computed]: GTEx public age is released as decade brackets (20–29 … 70–79); mapped to midpoints and treated as continuous. Bracket counts: 20s=67, 30s=65, 40s=124, 50s=255, 60s=264, 70s=28.
- **Alignment check** [computed]: per-gene TPM arrays carry no sample IDs → verified index-alignment to metadata via sex probes. Expression-based sex call matched the label for **543/543 samples called male**; the strict two-marker gate (XIST>100 & RPS4Y1<5 for female; XIST<20 & RPS4Y1>20 for male) left the 260 labelled-female samples **uncalled**, so female precision is not asserted — but zero discordance was observed among called samples.
- **Sample-flow audit** [computed]: **803 → 716 kept; 87 excluded** = 82 pathology-flagged (fibrosis/atrophy/inflammation/necrosis) + 5 QC-only (RIN<6), where 80 are pathology-only, 5 QC-only, 2 both. Age 24–74. Pathology gating **attenuates but does not deconvolve** within-cell aging from composition change.
- **Model** [computed]: partial correlation of log2(TPM+1) with age, adjusting sex, RIN, ischemic time; BH-FDR. 95% CIs via Fisher z.
- **Positive controls confirm a real aging axis** [computed]: CDKN2A/p16 r=+0.291 (95% CI +0.222..+0.357, FDR=1.3e-13, strongest up); IL6 +0.139; CDKN1A +0.100; GLB1 +0.107.
- **Composition confound is visible** [computed]: COL1A1 +0.129, COL1A2 +0.116, PDGFRA +0.145 → justifies (but is not fully resolved by) the pathology gate.
- **Most consistent declining cluster = redox/glutathione** [computed]: GCLM −0.145, GSR −0.145, SOD2 −0.142 (FDR≈8e-4); plus NAD biosynthesis NMNAT1 −0.104 (FDR=0.019) and ESRRA −0.214 (FDR=2e-7).
- **Direction-aware kill shot** [computed]: polyamine-synthesis genes DHPS +0.195 (FDR=3e-6), SMS +0.147, SRM +0.092 all INCREASE with age → contradicts a spermidine "restore" rationale.

## C. S2 — signed causal prior (retrieved)
- Tier 1 (causal intervention): **taurine** declines with age and its restoration is causally protective in mice/monkeys **[fact: PMID 37289866]** — the only candidate with intervention-grade causal evidence.
- Tier 2 (Mendelian randomization): metabolome-wide MR of 452 blood metabolites vs handgrip strength + appendicular lean mass **[fact: PMID 38366876]**; lipid-metabolite MR **[fact: PMID 39285470]**; gut-microbiota-metabolite MR **[fact: PMID 38995073]**. Used as direction/risk prior only.
- GWAS instruments exist for the outcomes [computed via connector]: grip strength EFO_0006941 = 850 associations; appendicular lean mass EFO_0004980 = 1,740; sarcopenia EFO_1000653 = 13.
- **Guardrail** [proposed]: no candidate-specific MR is invented; where MR is thin the score reflects uncertainty. PMID 38366876 does **not** report an NAD-precursor hit, so it is *not* used to support NR's direction.

## D. S3 — mechanism / signature reversal (retrieved)
- Taurine: ↓senescence, ↓mito dysfunction, ↓DNA damage, ↓inflammaging **[fact: PMID 37289866]** → reverses the computed age-up axis.
- NR: ↑NAD metabolome + anti-inflammatory transcriptomic signature in aged human muscle **[fact: PMID 31412242]**; same study explicitly reports **no change in mitochondrial bioenergetics** → NR is NOT credited a mitochondrial-quality point.
- Urolithin A: ↑strength ~12%, ↑endurance, ↓acylcarnitines/CRP in middle-aged adults **[fact: PMID 35584623]**; caveat — pre-registered **primary endpoint (peak power) not met**.
- GlyNAC: ↑glutathione, ↓oxidative stress, ↓mito dysfunction, ↓inflammation, ↑strength in older adults **[fact: PMID 33783984, 35975308]**; glycine-aging mechanism review **[fact: PMID 37004845]**.
- Spermidine: autophagy/mitophagy induction, cardioprotection, lifespan extension **[fact: PMID 27841876]** — but cardiac/organismal, not muscle-aging-specific.

## E. Scoring & the benchmark (consistency check)
- Rubric: four axes scored 0–2 — E1 target-fit (computed GTEx panel), E2 causal direction (×1.5, up-weighted because direction is the method's core commitment), E3 mechanism/reversal, E4 oral delivery+safety. **[proposed rubric]**. It was NOT hashed/frozen prospectively; this is a retrospective scoring.
- Weighted totals [computed]: taurine 9.0; GlyNAC 7.5; NR 6.5; urolithin A 6.5; spermidine 4.5.
- **Benchmark** [computed] — a **consistency check, not a blinded held-out validation**: nomination gate = (E1≥1 ∧ E3≥2 ∧ E4≥2); it deliberately does *not* require pre-existing muscle-aging genetics (or nothing novel could pass). Result: taurine/UroA/NR recovered (3/3); spermidine excluded (fails E1 on computed panel data).
- **Limits of the check (stated):** the three positives were scored from their own known literature (not truly held out); only one negative was tested; the planned differential-abundance-top-N and source-method (RPC) baselines were **not** run. So this shows the rubric is internally coherent and can reject a data-contradicted agent — it does **not** establish sensitivity/specificity.

## F. S4 — combination (complementarity, not synergy)
- Fact-level hallmark coverage [computed from cited mechanisms]:
  - Taurine → {mito-quality, senescence}
  - NR → {NAD, senescence}
  - Urolithin A → {mito-quality}
  - GlyNAC → {redox, mito-quality, senescence}
- Distinctness filter [proposed]: exclude agents sharing chemistry with the one-carbon cocktail (methionine/threonine/glycine/putrescine/cysteine/SAM). GlyNAC fails (glycine + cysteine-family) → held out of the primary cocktail.
- **Selected: Taurine + NR** — highest-evidence distinct pair; covers 3/4 hallmarks (senescence, mito-quality, NAD) at redundancy 1. **Redox/glutathione is the explicit residual gap.**
- GlyNAC becomes the pre-specified **redox add-on** arm (best redox agent, but non-distinct).
- Combination selection names *what to co-test*; it is NOT a synergy claim — interaction is learned in Stage 1.

## G. Pilot logic
- **One clean primary inference** [proposed]: cocktail vs vehicle on ex-vivo specific force of *uninjured* EDL; experimental unit = animal, treatment assigned at cage level (shared water/diet) with cage as a random effect; one endpoint, one timepoint, pre-declared analysis hierarchy.
- **Real power calculation** [computed]: target Δ=+30 kN/m² (≥50% of a 60 kN/m² young–old gap) vs SD≈30 → Cohen's d≈1.0; two-sided t at α=0.05 → **17/group** (80% power), **23/group** (90%). Adjusted for cage clustering (design effect 1.15 at ICC 0.05, 4 mice/cage) and 10% attrition → **~22/group**. Sex included as a stratification covariate. SD taken from published mouse-EDL specific-force ranges and re-confirmed in Stage 1 before registration.
- **Arms staged to protect power** [proposed]: *core* = vehicle, full cocktail, minus-taurine, minus-NR (the primary + necessity comparisons). *Context, gated behind a positive primary* = scramble (generic intake/osmolarity), 1C-MIM comparator, exercise, GlyNAC redox add-on. Multiplicity: primary at α=0.05; two drop-outs Holm-adjusted.
- Confound detectors built into readouts: central-nucleated fibers + fibrosis (regeneration/remodeling), body-composition/intake (generic effects), clock-without-function (aging-clock artifact).
- Interaction + exposure/target-engagement learned before the animal test (Stage 1) so the animal study stays powered, interpretable, and exposure-qualified.

## H. What is computed vs retrieved vs proposed
- **Computed here:** GTEx alignment verification; the aged→young uninjured muscle axis (n=716, all r/FDR values); the evidence scores and weighted ranking; the benchmark consistency check; the hallmark set-cover selection.
- **Retrieved from literature/connectors:** every PMID claim; the NCT trial precedents; the GWAS association counts; dataset existence/identity (GEO, GTEx).
- **Proposed (design):** the scoring rubric and weights; the distinctness filter; the entire pilot protocol and decision rules.

## I. Key limitations (stated, not hidden)
- **This is a retrospective prototype, not a frozen/blinded discovery run.** No hashed protocol or timestamped coded ledger was created prospectively; blinding, held-out recovery, and demonstrated sensitivity/specificity are therefore NOT claimed.
- **S1 is a curated 56-gene panel**, not transcriptome-wide/deconvolved/replicated. GTEx is *cross-sectional bulk* human muscle: an age association is not longitudinal and mixes cell-composition with within-cell change (attenuated, not eliminated, by the pathology gate). Single-cell aging data (GSE196554) and an independent aged-muscle cohort (GSE152558) are named for confirmation but not reanalyzed here.
- **The candidate set is a hand-curated shortlist** of literature-supported agents, not an enumeration of a metabolome-wide universe — so this ranks a shortlist rather than discovering across the full space (`candidate_universe_log.json`).
- **S2/S3/S4/S5 ran below full spec:** no de-novo MR (published MR used as prior; NR/UroA lack candidate-specific muscle genetics → E2=1); S3 qualitative not quantitative-reversal; S4 expert-coded not network set-cover; S5 oral-trial precedent only (no ADMET/exposure).
- Urolithin A's headline muscle RCT missed its pre-registered primary endpoint — E3 real but qualified.
- Doses are not asserted; fixed at protocol registration from each agent's established efficacious regimen.
