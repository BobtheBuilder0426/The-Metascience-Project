# Sources

Every source used, with its identifier, mapped to the exact claim it supports. Identifiers were resolved through NCBI (PMID→DOI), ClinicalTrials.gov, ChEMBL, the GWAS Catalog, and the dataset's own deposition records.

## Primary dataset

**[D1] Genome-scale Perturb-seq in primary human CD4⁺ T cells.** *bioRxiv* 2025; **doi:10.64898/2025.12.23.696273**. Data: **GEO GSE314342**, **SRA SRP643211**; processed differential-expression tensor `GWCD4i.DE_stats.h5ad` (CZI Virtual Cell Models); code github.com/emdann/GWT_perturbseq_analysis_2025.
- Supports: the screen design (genome-scale CRISPRi knockdown in primary human CD4⁺ T cells; four donors; rest / 8 h / 48 h CD3/CD28 stimulation).
- Supports (DATASET, derived here): PKM knockdown lowers GM-CSF (z = −3.66, FDR = 0.005), IFN-γ (z = −3.30, FDR = 0.013), TNF (z = −4.65, FDR = 1.6×10⁻⁴), IL-2 unchanged (z = −0.05), IL-10 (z = −3.11); on-target effect −32.2, cross-donor 0.78, two concordant guides; effect specific to 8 h; among glycolytic genes only PKM and PGK1 show it; effector-vs-activation selectivity 3.4; 11,526 knockdowns with usable cytokine estimates. (Read by HTTP byte-range from the deposited tensor; no raw counts downloaded.)

## Disease genetics and effector biology

**[1] International Multiple Sclerosis Genetics Consortium.** Multiple sclerosis genomic map implicates peripheral immune cells and microglia in susceptibility. *Science* 2019. **PMID 31604244; doi:10.1126/science.aav7188.**
- Supports: the largest MS GWAS implicates peripheral immune cells in susceptibility; the CD4⁺ compartment is implicated broadly by the MS genetic map.

**[2] Komuczki J, et al.** Fate-mapping of GM-CSF expression identifies a discrete subset of inflammation-driving T helper cells regulated by IL-23 and IL-1β. *Immunity* 2019. **PMID 31079916; doi:10.1016/j.immuni.2019.04.006.**
- Supports: in the animal model, a discrete GM-CSF (*CSF2*)-producing T-helper state mediates immunopathology, and ablating it interrupts the inflammatory cascade. (Cited as animal-model evidence only.)

## PKM2 mechanism and direction-of-effect

**[4] Damasceno LEA, et al.** PKM2 promotes Th17 cell differentiation and autoimmune inflammation by fine-tuning STAT3 activation. *J Exp Med* 2020. **PMID 32697823; doi:10.1084/jem.20190613.**
- Supports: nuclear PKM2 binds STAT3 and amplifies effector-cytokine transcription; T-cell-specific *Pkm2* deletion impairs Th17 differentiation and ameliorates EAE; PKM2 is **not** required for metabolic reprogramming or proliferation (the basis for the observed effector-selectivity).

**[5] Kono M, et al.** Pyruvate kinase M2 is requisite for Th1 and Th17 differentiation. *JCI Insight* 2019. **PMID 31217348; doi:10.1172/jci.insight.127395.**
- Supports: PKM2 is required for Th1 and Th17 differentiation; the TCR-activated kinase CaMK4 binds and activates PKM2; a PKM2 inhibitor ameliorates EAE — placing PKM2 downstream of antigen-receptor signalling in the effector program. (Abstract confirms "CaMK4 interacts directly with PKM2" and "a PKM2 inhibitor ameliorated experimental autoimmune encephalomyelitis.")

**[6] Angiari S, et al.** Pharmacological activation of pyruvate kinase M2 inhibits CD4⁺ T cell pathogenicity and suppresses autoimmunity. *Cell Metab* 2020 (online 2019). **PMID 31761564; doi:10.1016/j.cmet.2019.10.015.**
- Supports the *direction* keystone: the tetramer activator **TEPP-46** (which forces tetramerisation and blocks nuclear translocation) limits Th1/Th17 development and suppresses EAE in vivo; PKM2 is upregulated/phosphorylated/nuclear in activated murine and human CD4⁺ T cells. Establishes that pushing PKM2 toward the tetramer is disease-modifying.

## Compound identity, pharmacology, and exposure

**[7] Li J, et al.** Natural product micheliolide irreversibly activates pyruvate kinase M2. *J Med Chem* 2018. **PMID 29641204; doi:10.1021/acs.jmedchem.8b00241.**
- Supports: micheliolide **covalently binds PKM2 at Cys424** (absent in PKM1), promotes tetramer formation, inhibits K433 acetylation that licenses nuclear import, and reduces nuclear translocation; effects are PKM2-dependent in knockdown-controlled assays. Basis for the direction-matched, covalent-natural-product claim.

**[8] (Micheliolide–PKM2–p65).** Micheliolide interferes with the PKM2–NF-κB(p65) interaction / inflammasome activation. *Int Immunopharmacol* 2025. **PMID 40690808; doi:10.1016/j.intimp.2025.115231.**
- Supports: in inflammatory cells, micheliolide disrupts the PKM2–NF-κB(p65) interaction to suppress inflammation. (Cited as macrophage/non-T-cell context, correctly not as T-cell evidence.)

**[9] Zhang Q, et al.** Parthenolide suppresses Th17 and alleviates experimental autoimmune encephalomyelitis. *Front Immunol* 2022. **PMID 35514960; doi:10.3389/fimmu.2022.856694.**
- Supports: the parent sesquiterpene-lactone class (parthenolide) suppresses Th17 and alleviates EAE. (Cited as class-level EAE efficacy, distinct from micheliolide's own PKM2 engagement.)

**[10] Viennois E, et al.** Micheliolide, a new sesquiterpene lactone that inhibits intestinal inflammation and colitis-associated cancer. *Lab Invest* 2014. **PMID 25068660; doi:10.1038/labinvest.2014.89.**
- Supports: micheliolide is substantially more stable in vivo than parthenolide.

**[11] Xi J, et al.** Pharmacokinetics, tissue distribution and excretion of ACT001 in rats. *J Chromatogr B* 2018. **PMID 30423524; doi:10.1016/j.jchromb.2018.11.004.**
- Supports (attainable-exposure appraisal): the oral prodrug ACT001 (dimethylaminomicheliolide) has ~51% oral bioavailability, distributes widely, and crosses the blood–brain barrier in rats.

**[C1] Parthenolide chemical record.** ChEMBL **CHEMBL540445** (parthenolide; natural product; max clinical phase 2; C15H20O3).
- Supports: the feverfew parent of micheliolide is a natural product that reached clinical Phase 2; anchors the α-methylene-γ-butyrolactone covalent chemistry.

## Human translation and clinical status

**[13] Ellmeier E, et al. (Angiari S, senior author).** Targeting pyruvate kinase M2 (PKM2) reduces T cell pathogenicity in multiple sclerosis. *EBioMedicine* 2026. **PMID 42208151; doi:10.1016/j.ebiom.2026.106314.**
- Supports the human disease-side claim: in MS-patient T cells, effector/memory subsets (highest Th17/Tc17) over-express PKM2, MS PBMCs carry a higher PKM2 monomer fraction, and pharmacological PKM2 targeting (with TEPP-46) preferentially inhibits IFN-γ, IL-5, IL-13 and IL-17. (Full text confirms the compound used is TEPP-46, a reversible synthetic activator — not micheliolide, not covalent — which is why the natural-product covalent chemotype remains the distinct contribution here.)

**[12] ClinicalTrials.gov (status July 2026).**
- **NCT05053880** — ACT001 Phase 1b/2a in recurrent glioblastoma (± anti-PD-1); ACTIVE, NOT RECRUITING; no results posted.
- **NCT06894225** — ACT001 proof-of-concept in STAT3-high recurrent glioblastoma; Phase 2; **SUSPENDED**; no results posted.
- Supports: the prodrug has entered human early-phase trials (tolerability context only; not efficacy evidence for any mechanism).

## Genetics null (stated honestly)

**[G1] GWAS Catalog — *PKM* gene associations.**
- Supports the stated null: no genome-wide-significant *PKM*-locus association with MS or CNS autoimmunity (reported *PKM* hits are metabolic/anthropometric traits — e.g. bone mineral density, height, aspartate aminotransferase, colorectal cancer). Basis for the explicit statement that the nomination is functional/mechanistic, not genetically anchored.

## Structural/druggability

**[S1] Protein Data Bank / ChEMBL — PKM2.**
- Supports: PKM2 is an established druggable enzyme with defined allosteric pockets and co-crystallised small-molecule ligands (tractability is not the bottleneck).
