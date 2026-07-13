# Sources

All identifiers verified during the analysis (DOIs confirmed against CrossRef; GEO accessions confirmed via the GEO archive).

## Source publication (the attached paper)
- **Hernandez-Benitez R, et al.** "Intervention with metabolites emulating endogenous cell transitions accelerates muscle regeneration in old mice." *Cell Reports Medicine* **5**, 101449 (2024). DOI: **10.1016/j.xcrm.2024.101449**.
  - Cocktail (1C-MIM): methionine, threonine, glycine, putrescine, S-adenosylmethionine (SAM), cysteine.
  - Validated mechanism: increased histone acetylation + cell-cycle re-entry (regenerative competence); DNA-methylation-clock reversal reported as minor.

## Datasets analyzed (primary data, re-analyzed from counts)
- **GSE229533** — "Effect of metabolite intervention in mice muscle gene expression" (the paper's own in-vivo 1C-MIM RNA-seq; aged quadriceps; 5 control + 5 1C-MIM). Used for the premise test and 1C-MIM signature. NCBI GEO.
- **GSE132040** — "Tabula Muris Senis: Bulk sequencing" (mouse multi-organ bulk RNA-seq, ages 1–27 mo; 947 samples, 17 organs). Limb-muscle subset (54 samples) used to build the aging axis. NCBI GEO.
  - Companion analysis: **Schaum N, et al.** "Ageing hallmarks exhibit organ-specific temporal signatures." *Nature* **583**, 596–602 (2020). DOI: **10.1038/s41586-020-2499-y**.

## External references anchoring the cofactor axes (DOIs confirmed via CrossRef)
- **NAD⁺ / Sirtuin axis** — Zhang H, et al. "NAD⁺ repletion improves mitochondrial and stem cell function and enhances life span in mice." *Science* **352**, 1436–1443 (2016). DOI: **10.1126/science.aaf2693**. (NR rejuvenates aged muscle stem cells; dose basis.)
- **NAD⁺ feedability in aged human muscle** — Elhassan YS, et al. "Nicotinamide Riboside Augments the Aged Human Skeletal Muscle NAD⁺ Metabolome and Induces Transcriptomic and Anti-inflammatory Signatures." *Cell Reports* **28**, 1717–1728.e6 (2019). DOI: **10.1016/j.celrep.2019.07.043**.
- **Polyamine / spermidine axis** — Eisenberg T, et al. "Cardioprotection and lifespan extension by the natural polyamine spermidine." *Nature Medicine* **22**, 1428–1438 (2016). DOI: **10.1038/nm.4222**. (Spermidine declines with age; drinking-water dosing.)
- **α-Ketoglutarate axis** — Asadi Shahmirzadi A, et al. "Alpha-Ketoglutarate, an Endogenous Metabolite, Extends Lifespan and Compresses Morbidity in Aging Mice." *Cell Metabolism* **32**, 447–456.e6 (2020). DOI: **10.1016/j.cmet.2020.08.004**. (Ca-AKG healthspan/lifespan; dose basis.)

## Databases & ontologies queried
- **NCBI GEO** — series metadata and per-sample count matrices (GSE229533, GSE132040).
- **Reactome** — cofactor-metabolism pathway grounding for each enzyme axis (Coenzyme A biosynthesis; Nicotinate metabolism; Citric acid (TCA) cycle; Metabolism of polyamines; Vitamin B2/riboflavin metabolism; Methylation).
- **CrossRef** — DOI verification for all external references.

## Methods & tools
- **DESeq2** (via pydeseq2) — differential expression for the aging axis and the 1C-MIM signature.
- **statsmodels** — two-sample t-test power analysis (pilot sizing).
- **Composite lever score** and **submodular axis-coverage optimizer** — original to this analysis (defined in `process_trace.json` and the reasoning file).

## Note on provenance
Gene-level differential-expression values, module reversal scores, lever scores, the selection objective, and the power curves were all computed in this analysis from the primary count data above. The metabolite-age-decline and feedability score components are expert judgments anchored to the cited primary literature, not values extracted from the datasets; this is stated explicitly in the method because cofactor abundance is a metabolite-level property not directly observable in transcriptomes.
