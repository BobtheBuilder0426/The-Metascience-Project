# Sources

All identifiers were verified against the retrieved record. Each entry notes the exact claim it supports and whether it grounds a **[fact]** (directly supported) or an **[inference]/prior**.

## Inspiration / baseline
- **Hernández-Benítez et al., 2024** — *One-carbon metabolites cocktail for muscle reprogramming.* Cell Reports Medicine 5, 101449. **DOI 10.1016/j.xcrm.2024.101449.** The one-carbon cocktail (methionine, threonine, glycine, putrescine, cysteine at 5 mM + SAM 0.5 mM); the method and baseline this work differs from.

## Primary literature (PubMed)
- **PMID 37289866** — *Taurine deficiency as a driver of aging.* Science, 2023. DOI 10.1126/science.abn9257. **[fact]** Circulating taurine declines with age in mice/monkeys/humans; restoration increases healthspan (and lifespan in mice), reduces cellular senescence, suppresses mitochondrial dysfunction, decreases DNA damage, attenuates inflammaging. Grounds taurine's causal direction (E2) and mechanism (E3).
- **PMID 31412242** — *Nicotinamide Riboside Augments the Aged Human Skeletal Muscle NAD Metabolome and Induces Transcriptomic and Anti-inflammatory Signatures.* Cell Rep, 2019. DOI 10.1016/j.celrep.2019.07.043. **[fact]** Oral NR (1 g/day) raised the muscle NAD metabolome and produced an anti-inflammatory signature in aged men; explicitly reports **no change in mitochondrial bioenergetics**. Grounds NR's mechanism (E3) and the removal of NR's mitochondrial-quality coverage.
- **PMID 35584623** — *Urolithin A improves muscle strength, exercise performance, and biomarkers of mitochondrial health in a randomized trial in middle-aged adults.* Cell Rep Med, 2022. DOI 10.1016/j.xcrm.2022.100633 (trial NCT03464500). **[fact, qualified]** ~12% strength gain and improved mitochondrial biomarkers in **middle-aged** adults; the pre-registered **primary endpoint (peak power) was not met**. Grounds urolithin A's mechanism (E3) with its stated caveat.
- **PMID 33783984** — *GlyNAC supplementation in older adults improves glutathione deficiency, oxidative stress, mitochondrial dysfunction, inflammation, ... muscle strength, and cognition: a pilot clinical trial.* Clin Transl Med, 2021. DOI 10.1002/ctm2.372. **[fact]** Grounds GlyNAC redox/glutathione mechanism (E3) and target-fit to the computed redox-decline axis (E1).
- **PMID 35975308** — *Supplementing GlyNAC in Older Adults Improves Glutathione Deficiency, Oxidative Stress, Mitochondrial Dysfunction, Inflammation, Physical Function, and Aging Hallmarks: A Randomized Clinical Trial.* J Gerontol A Biol Sci Med Sci, 2022. DOI 10.1093/gerona/glac135. **[fact]** Randomized confirmation of the above.
- **PMID 37004845** — *Glycine and aging: Evidence and mechanisms.* Ageing Res Rev, 2023. DOI 10.1016/j.arr.2023.101922. **[fact]** Glycine as a pro-longevity molecule; mechanistic context for the glycine component of GlyNAC.
- **PMID 34518687** — *Molecular mechanisms of dietary restriction promoting health and longevity.* Nat Rev Mol Cell Biol, 2021. DOI 10.1038/s41580-021-00411-4. **[fact]** Names methionine (and BCAA) restriction as longevity levers — grounds the direction-of-causality argument (supplementing "what rises in youth" can be backwards).
- **PMID 27841876** — *Cardioprotection and lifespan extension by the natural polyamine spermidine.* Nat Med, 2016. DOI 10.1038/nm.4222. **[fact]** Spermidine induces autophagy/mitophagy, is cardioprotective, extends lifespan — cardiac/organismal, not muscle-aging-specific; grounds spermidine's E3 and the note that its evidence is not muscle-aging-specific.

### Mendelian-randomization prior (direction/risk only)
- **PMID 38366876** — *Metabolome-Wide Mendelian Randomization Assessing the Causal Relationship Between Blood Metabolites and Sarcopenia-Related Traits.* J Gerontol A Biol Sci Med Sci, 2024. DOI 10.1093/gerona/glae051. **[prior]** 452 metabolites vs handgrip strength + appendicular lean mass. Establishes that signed metabolite→muscle causal evidence exists; **does not** report an NAD-precursor hit (so it is not used for NR's direction).
- **PMID 39285470** — *Lipid metabolites and sarcopenia-related traits: a Mendelian randomization study.* Diabetol Metab Syndr, 2024. DOI 10.1186/s13098-024-01465-y. **[prior]**
- **PMID 38995073** — *Causal Relationship Between Gut Microbiota, Metabolites, and Sarcopenia: A Mendelian Randomization Study.* J Gerontol A Biol Sci Med Sci, 2024. DOI 10.1093/gerona/glae173. **[prior]**
- **PMID 29685734** — *Quantitative Analysis of NAD Synthesis-Breakdown Fluxes.* Cell Metab, 2018. DOI 10.1016/j.cmet.2018.03.018. **[fact]** Background on NAD flux/turnover.

## Datasets
- **GTEx v8, Muscle - Skeletal** (803 RNA-seq donors; 716 retained after the pathology/QC gate). Primary computed target signature. Accessed via the GTEx expression connector.
- **GSE152558** — *Ribosome profiling analysis of aging human skeletal muscle* (Homo sapiens, n=10). Named independent human aged-muscle cohort for confirmation.
- **GSE196554** — *Single cell RNA sequencing of human muscle stem cells in aging* (Homo sapiens, n=12). Named single-cell aging resource for compartment-aware confirmation.
- **GSE155193** — *One-carbon metabolites control cellular identity [Bulk RNA-seq myoblast]* (Mus musculus, n=15). Inspiration-paper deposit.
- **GSE229533** — *Effect of metabolite intervention in mice muscle gene expression* (Mus musculus, n=10). Inspiration-paper deposit.
- **GSE229534** — *Effect of metabolites supplementation on C2C12 gene expression* (Mus musculus, n=9). Inspiration-paper deposit.

## GWAS instruments (GWAS Catalog, via connector)
- **Handgrip strength** — EFO_0006941 — 850 associations.
- **Appendicular lean mass** — EFO_0004980 — 1,740 associations.
- **Sarcopenia** — EFO_1000653 — 13 associations.

## Clinical-trial precedent (ClinicalTrials.gov) — oral deliverability + safety
- **NCT05149716** — *Taurine as a Possible Anti-aging Therapy?* (taurine vs placebo; COMPLETED). Taurine E4.
- **NCT05483465** — *Effects of NAD Restoration on Neurovascular Coupling in Community-Dwelling Older Adults* (nicotinamide riboside vs placebo; PHASE 4). NR E4.
- **NCT03464500** — *Efficacy of AMAZ-02 (Urolithin A/Mitopure)* (Mitopure 500/1000 mg vs placebo; COMPLETED) — the PMID 35584623 trial. Urolithin A E3/E4.
- **NCT05735886** — *Impact of Urolithin A Supplementation on Mitochondrial Health of Immune Cells (MitoImmune)* (Urolithin A 250 mg vs placebo; COMPLETED). Urolithin A E4.
- **NCT03283462** — Urolithin A (Mitopure) daily-dose RCT (COMPLETED). Urolithin A E4.
- **NCT02348762** — *Energetics and Function in Older Humans* (glycine + N-acetylcysteine; PHASE 1; COMPLETED). GlyNAC E4 (oral, aging-relevant).
- **NCT01870193** — *Glutathione and Fuel Oxidation in Aging* (GlyNAC; EARLY PHASE 1; COMPLETED). GlyNAC E4 (oral, aging-relevant).

## Derived data files (this work)
- `figures/gtex_age_trend.csv` — curated 56-gene computed aged-muscle table (gene, category, partial-r-with-age, 95% CI, p, FDR, median TPM; n=716).
- `figures/recast_ledger.json` — full scored evidence ledger with per-axis bases and weights.
- `power_calculation.json` — variance-based power calculation for the pilot primary endpoint (n/group, design effect, attrition, multiplicity).
- `candidate_universe_log.json` — the hand-curated candidate set and explicit rejection log (spermidine on data; GlyNAC on distinctness).
- `process_trace.json` — step-by-step of what was executed vs each stage's full specification.
