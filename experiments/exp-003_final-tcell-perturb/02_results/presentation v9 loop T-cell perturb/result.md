# A metabolite-sensitive glycolytic switch (PKM2) nominated from genome-scale CD4⁺ T-cell Perturb-seq as a natural-product target in multiple sclerosis

**Running title:** Micheliolide engagement of PKM2 to disarm encephalitogenic CD4⁺ T cells

---

## Abstract

Multiple sclerosis is driven by CD4⁺ T cells secreting the encephalitogenic cytokines GM-CSF and IFN-γ. Mining a genome-scale CRISPRi Perturb-seq atlas of primary human CD4⁺ T cells, we sought one knockdown that suppresses this effector program while sparing activation. Knockdown of *PKM* (pyruvate kinase M2) lowered GM-CSF (z = −3.66, FDR = 0.005) and IFN-γ (z = −3.30) at 8 h while leaving IL-2 unchanged (z = −0.05). Nuclear PKM2 potentiates STAT3-driven differentiation, and PKM2 deletion or activation ameliorates autoimmune encephalomyelitis; a 2026 human study shows PKM2 targeting curbs MS T-cell cytokines. The corrective direction — stabilize the PKM2 tetramer to block nuclear entry — is matched by one natural metabolite, **micheliolide**, which engages PKM2 covalently at Cys424, a distinct chemotype from the reversible tool compound used to date. We propose a decisive compound × CRISPRi epistasis pilot testing whether PKM2 is micheliolide's mediator in human CD4⁺ T cells.

---

## 1. Introduction

Multiple sclerosis is a chronic demyelinating CNS disease in which autoreactive CD4⁺ T cells are central to pathogenesis. Its dominant genetic risk factor is the MHC class II allele *HLA-DRB1\*15:01*, and the largest MS GWAS implicated peripheral immune cells in susceptibility [1]. Because MHC class II presents antigen to CD4⁺ T cells, this points specifically to the CD4⁺ compartment as causal — an unusually clean setting for a CD4⁺-intrinsic intervention.

The pathogenic activity of these cells is carried by defined effector cytokines. In the animal model of MS, a discrete GM-CSF-producing (*CSF2*) T-helper state mediates immunopathology and tissue destruction, and specific ablation of it interrupts the inflammatory cascade [2]; IFN-γ marks the Th1 arm. A therapeutic that shifts CD4⁺ T cells away from this GM-CSF/IFN-γ program without globally ablating T-cell function would be disease-modifying in principle.

Two problems have kept this from natural-product medicine: target nomination is rarely done at causal genome scale in the relevant human cell type, and the *direction* a compound must act is usually guessed rather than derived. We address both by mining a genome-scale CRISPRi Perturb-seq atlas of primary human CD4⁺ T cells [3] — deriving target and direction from data, then matching a natural metabolite whose measured pharmacology moves the target correctly.

---

## 2. Methods

**Belief ledgers.** We separate *DATASET* (derived here from the Perturb-seq resource), *LITERATURE* (an external published finding with an identifier), and *INFERENCE* (our reasoning connecting them). Every non-trivial claim carries a PMID/DOI/accession.

**Dataset.** We used the processed differential-expression (DE) estimates from the CD4⁺ T-cell Perturb-seq study [3] (bioRxiv 2025.12.23.696273; GEO GSE314342; SRA SRP643211; processed matrices at CZI Virtual Cell Models; code at github.com/emdann/GWT_perturbseq_analysis_2025). The screen used CRISPRi (partial **knockdown**, not knockout) in CD4⁺ T cells from four donors, profiled at rest, 8 h and 48 h after CD3/CD28 stimulation. Honouring a compute-light mandate, we did not download raw counts; we read only the pseudobulk DE tensor (`GWCD4i.DE_stats.h5ad`; 33,983 perturbation-conditions × 10,282 genes) by HTTP byte-range, extracting columns for the eight measured cytokines. IL-17 is not measured here (the stimulation is not Th17-polarizing), so the encephalitogenic readout is GM-CSF plus IFN-γ.

**Pre-specified scoring (fixed before ranking).** From independent references we fixed a pathogenic-effector set (core *CSF2*, *IFNG*) to lower and confound sets (activation/*IL2*, proliferation, stress) that must stay flat — pre-specified, i.e. fixed before ranking though not deposited as a public protocol. Sign convention was validated empirically: knockdown of canonical positive regulators (*TBX21*, *STAT3*, *LAT*/*LCP2*/*ZAP70*) gave negative cytokine z-scores, confirming **negative z = knockdown lowers the cytokine** (z = DE effect ÷ standard error; FDR = Benjamini–Hochberg). Of ~12,748 targeted genes, 11,526 had usable cytokine estimates and entered ranking; candidates required significant on-target knockdown, cross-donor/guide reproducibility, and a significant reduction (FDR < 0.05, |z| > 2) of ≥1 core cytokine under stimulation. They were ranked biology-first, filtered for confounds (pan-activation, general transcription/chromatin, essential genes, cytokines-themselves), scored for **effector-vs-activation selectivity** (GM-CSF/IFN-γ minus IL-2 suppression), then passed through a tractability filter (**Table 1**). Genetic association enters as supporting rather than gating evidence: the GWAS Catalog shows no *PKM* MS-locus signal (below), so nomination rests on the causal effector-selectivity and the direction-matched mechanism. Sources: GWAS Catalog (genetics); PDB/ChEMBL (druggability, identity); PubMed (mechanism, PK, current-literature check); ClinicalTrials.gov (trials); NCBI (PMID→DOI).

---

## 3. Results

### 3.1 One knockdown suppresses the encephalitogenic cytokines while sparing activation

Screening all 11,526 knockdowns for effect on GM-CSF and IFN-γ, the strongest hits were, as expected, TCR-proximal signaling genes (*LCP2*, *CD3G*, *ZAP70*, *LAT*) and general transcriptional machinery — nodes whose loss shuts down activation wholesale, causing broad immunosuppression rather than targeted correction. Plotting each knockdown's effect on the effector program against its effect on IL-2 separates these pan-activation hits from a smaller group that lowers effector cytokines *selectively* (**Figure 1a**).

**PKM** (pyruvate kinase M2) sits in this selective group. At 8 h — the window the resource's own autoimmune analysis emphasises — PKM knockdown lowered GM-CSF (z = −3.66, FDR = 0.005), IFN-γ (z = −3.30, FDR = 0.013) and TNF (z = −4.65, FDR = 1.6×10⁻⁴) while leaving IL-2 unchanged (z = −0.05) (**Figure 1b**; DATASET). Its selectivity (3.4) far exceeded the TCR-proximal nodes (LCP2 2.2, ZAP70 0.8), which suppress effector cytokines only by shutting down activation. PKM was not the single most selective knockdown — a few genes scored higher but were excluded as pan-activation (*STAT5B*) or general transcription (*DR1*), or, for *RFT1* and *DARS1*, retained through the biology filters yet deprioritized at the tractability stage for lack of a natural-product ligand and a direction-matched mechanism; PKM was nominated by the pre-specified biology-then-tractability walk-down (**Table 1**). Knockdown was strongly on-target (effect size −32.2; two concordant guides), reproducible across donors (0.78), and specific to early activation — at 48 h it faded and IL-2 rose (**Figure 1c**). Among glycolytic genes only *PKM* and its neighbour *PGK1* showed the effect (upstream *HK1/2*, *GAPDH* did not), arguing against generic energetic collapse and for a specific PKM2 node. One caveat: PKM knockdown also lowered the regulatory cytokine IL-10 (z = −3.11), so it damps a broad activated-effector module rather than a pure Treg-sparing switch.

### 3.2 The target and its required direction converge across genetics, mechanism, and pharmacology

PKM2 is a well-established druggable enzyme with defined allosteric pockets and multiple co-crystallised small-molecule ligands (structures in the PDB; ChEMBL small-molecule chemistry), so tractability is not the bottleneck. We note honestly what the genetics do *not* show: the GWAS Catalog reports no genome-wide-significant *PKM*-locus association with MS or CNS autoimmunity (its *PKM* hits are metabolic and anthropometric traits) (LITERATURE). The case for PKM2 therefore does not rest on genetic association — it rests on the causal, cell-intrinsic effector-selectivity we observe here and on the direction-of-effect mechanism below, in a compartment (CD4⁺ T cells) that the MS genetic map does implicate broadly [1].

The mechanism explains both the selectivity and the direction (**Figure 2a**). Beyond its cytoplasmic glycolytic role as a tetramer, the PKM2 dimer translocates to the nucleus and binds STAT3, amplifying effector-cytokine transcription. T-cell-specific *Pkm2* deletion impairs Th17 differentiation and **ameliorates EAE** by reducing inflammation and demyelination — and, crucially, PKM2 is *not* required for the metabolic reprogramming or proliferation of these cells [4]: precisely the phenotype we observe (effector cytokines drop, activation/IL-2 spared). PKM2 is likewise required for Th1 and Th17 differentiation in a parallel study, in which the TCR-activated kinase CaMK4 binds and activates PKM2 and a PKM2 inhibitor ameliorates EAE [5] — placing PKM2 downstream of antigen-receptor signalling in the effector program. Because the *nuclear dimer* is pathogenic, the corrective move is to **stabilise the PKM2 tetramer and block nuclear translocation**. The synthetic tetramer activator TEPP-46 does this, limiting Th1/Th17 development and suppressing EAE in vivo [6] — direct proof that pushing PKM2 toward the tetramer is disease-modifying (**Figure 2b**).

### 3.3 Micheliolide is a natural metabolite that moves PKM2 the correct way

The **natural metabolite micheliolide (MCL)** — a guaianolide sesquiterpene lactone, the stable derivative of the feverfew natural product parthenolide (ChEMBL CHEMBL540445, itself Phase 2) — matches this direction with direct-assay pharmacology. MCL **covalently binds PKM2 at Cys424** (absent from PKM1), promoting tetramer formation, inhibiting the K433 acetylation that licenses nuclear import, and reducing nuclear translocation; these effects are PKM2-dependent in knockdown-controlled assays [7]. In inflammatory cells MCL disrupts the PKM2–NF-κB(p65) interaction [8]; the parent parthenolide suppresses Th17 and alleviates EAE [9]; MCL is far more stable in vivo than parthenolide [10]. This makes MCL a mechanistically distinct probe from the reversible activator TEPP-46 [6]: covalent versus allosteric, natural product versus tool compound.

MCL is therefore predicted to **phenocopy the beneficial loss of nuclear PKM2** while preserving cytoplasmic glycolysis (INFERENCE, grounded in [4,6,7]). We flag an explicit gap: MCL's *own* engagement is documented in leukemia cells and the EAE efficacy is for parthenolide — MCL's direct activity in primary human CD4⁺ T cells is unshown, and is what the pilot tests.

**Direction-of-effect across modalities — an empirical bridge, not an identity (Table 2).** The evidence spans perturbations that are *not* interchangeable. CRISPRi knockdown and genetic deletion both remove the whole PKM2 protein — including its cytoplasmic glycolytic pool — and lower effector cytokines; genetic deletion does so with proliferation and glycolysis preserved [4] (this screen measured cytokines, not proliferation/glycolysis — Table 2, "?"). The reversible activator TEPP-46 also dampens activation, proliferation and glycolysis [6]. Micheliolide is distinct from all three: it biases PKM2 toward the tetramer and blocks nuclear entry while sparing the cytoplasmic enzyme — so "glycolysis intact" is a property the covalent activator is designed to have, not one inherited from removing the protein. **Table 2** resolves each modality against engagement, cytokines, activation, proliferation, glycolysis, context and exposure, making explicit what the pilot must still establish — that the covalent natural product reproduces the beneficial phenotype in human cells without a proliferation/glycolysis penalty.

**Current landscape.** A human study now establishes the disease side directly: MS-patient effector/memory T cells (highest in Th17/Tc17) over-express PKM2, MS PBMCs carry more PKM2 monomer (heightened moonlighting), and PKM2 targeting preferentially inhibits IFN-γ/IL-5/IL-13/IL-17 in MS T cells [13] (LITERATURE) — using the reversible activator TEPP-46. This de-risks the target in humans; what remains novel here is the *unbiased genome-scale nomination* from a causal CD4⁺ screen and the **natural-product covalent chemotype** (micheliolide, Cys424) with a CNS-penetrant prodrug — neither addressed by that study.

**Compound versus prodrug, and attainable exposure (honest appraisal).** The natural metabolite MCL and its *synthesized* clinical prodrug dimethylaminomicheliolide (DMAMCL / ACT001) are distinct entities, kept separate here. ACT001 has ~51 % oral bioavailability and crosses the blood–brain barrier in rats [11], and has entered human early-phase oncology trials — which support tolerability but are not efficacy evidence: a Phase 1b/2a glioblastoma study is active/not-recruiting and a STAT3-high glioblastoma study is currently *suspended*, both with no results posted (NCT05053880, NCT06894225) [12]. Two limitations bound any translational claim. First, published PKM2-engagement/Th17 activity is low-micromolar and the unbound CNS-available concentration at tolerated human doses is unestablished — so attainable immunomodulatory exposure is an unproven gate, not a passed one. Second, as a covalent α-methylene-γ-butyrolactone, MCL can react with other cysteine proteins, so target selectivity in human T cells must be tested (the epistasis design does this).

---

## 4. A decisive, falsifiable pilot

The single most important question is causal: **is PKM2 the protein through which micheliolide acts in human effector CD4⁺ T cells?** We therefore make target-dependence the primary result, not a secondary confirmation (**Figure 3**).

**Design (2 × 2 factorial epistasis).** Primary human CD4⁺ T cells from ≥6 donors (healthy, ideally paired MS) are activated (CD3/CD28) in a factorial cross of {vehicle, micheliolide} × {non-targeting sgRNA, CRISPRi-*PKM2*}, at a non-saturating dose range.

**Primary endpoint (pre-declared, acute 8 h arm).** Frequency of GM-CSF⁺IFN-γ⁺ CD4⁺ cells (intracellular staining). The mechanism-defining prediction is an **interaction**: micheliolide lowers the effector fraction in control cells but produces *no further reduction* in PKM2-depleted cells (drug × sgRNA p < 0.05). Interpretation is bounded honestly — a lost effect after partial knockdown can reflect floor/saturation, and a *persisting* effect can reflect residual PKM2 or non-linear pharmacology, so persistence weakens but does not alone prove off-target action — hence the interaction is read alongside measured residual PKM2 and direct engagement, not alone.

**Isoform attribution.** The screen perturbs the *gene*; assigning the effect to PKM2 specifically requires isoform-resolved PKM2/PKM1 expression and a **complementation/rescue** arm (re-expressing nuclear-competent vs tetramer-locked PKM2 in knockdown cells) before gene-level CRISPRi can establish isoform-specific mediation.

**Second arm + engagement + controls.** A separate Th1/Th17-skewing 3–5 day arm measures polarization and proliferation (CTV), which an 8 h readout cannot. Target engagement: PKM2 tetramer:dimer ratio, nuclear PKM2, pSTAT3(Y705). Controls: Annexin-V (death), IL-2 (spared-activation positive), TEPP-46 (mechanism-positive comparator), and a PKM1-insensitive control (Cys424 is PKM2-specific).

**Statistics / feasibility.** Donor is the experimental unit; the drug × genotype interaction is fit by a mixed-effects model (donor random effect), with power pre-computed from the pilot's own between-donor variance. One immunologist, ~6–8 weeks (multi-day arm +~2 weeks), BSL-2, all-commercial reagents, no animals — a positive result is immediately human-relevant and a negative one cleanly falsifies the hypothesis.

---

## 5. Discussion

Starting from a genome-scale causal map of human CD4⁺ T cells, we nominated a single natural-product target for MS by requiring that its knockdown suppress the encephalitogenic GM-CSF/IFN-γ program while sparing activation, and we then let mechanism define the direction a compound must act. The lines of evidence point the same way — an unbiased effector-selectivity screen, a loss-of-function mechanism (nuclear PKM2→STAT3, deletion ameliorating EAE), an in-vivo directional control (TEPP-46 in EAE), a natural covalent ligand (micheliolide), and now a 2026 human MS study showing PKM2 targeting curbs patient T-cell cytokines [13] — but they span non-identical perturbations, so we treat the modality bridge (Table 2) as an empirical question the pilot must close rather than a settled convergence. The argument deliberately does not lean on genetic association — there is no MS *PKM*-locus GWAS signal — which is why the causal screen and the direction-matched mechanism carry the weight. Against the 2026 human validation, the distinct contribution here is narrow and honest: the *genome-scale causal nomination* and the *natural-product covalent chemotype* (micheliolide/Cys424) with a CNS-penetrant prodrug, versus the reversible tool activator used to establish the target biology.

**Limitations.** (i) IL-17 is not measured in this atlas, so the effector axis is GM-CSF/IFN-γ, not the full Th17 program; (ii) PKM knockdown also lowers IL-10, so the intervention damps a broad activated-effector cytokine module rather than executing a pure effector→Treg switch; (iii) CRISPRi removes all PKM2 whereas micheliolide biases the tetramer — related but not identical perturbations, which is exactly why the pilot pairs them; (iv) the human unbound CNS exposure of ACT001 at immunomodulatory concentrations is unproven; (v) covalent reactivity demands the off-target-controlled epistasis test we specify; (vi) *PKM* carries no MS-specific GWAS signal, so this is a functional/mechanistic nomination rather than a genetically anchored one — the causal screen and direction-matched mechanism, not human genetics, are what support it. These are testable, not fatal, and the proposed pilot addresses the decisive one first.

If the epistasis test succeeds, micheliolide/ACT001 becomes a mechanistically-defined, orally available, BBB-penetrant candidate for repositioning trials in MS, acting not by broad immunosuppression but by disarming a metabolite-sensitive switch that CD4⁺ T cells use to become encephalitogenic.

---

## Figures

**Figure 1. A knockdown that selectively disarms the encephalitogenic cytokine program.** (a) Effect of each of 11,526 CD4⁺ T-cell knockdowns on the effector program (mean z of GM-CSF + IFN-γ, x-axis) versus on activation (z of IL-2, y-axis), 8 h post-stimulation; pan-activation TCR-proximal genes lie on the y = x diagonal (they lower effector cytokines and IL-2 equally), whereas effector-selective genes — which lower effector cytokines with IL-2 near zero — sit *above* the diagonal, toward the top-left. PKM (PKM2) is highlighted. z = DE effect ÷ standard error; points are per-perturbation estimates pooled across four donors and two guides. (b) PKM-knockdown cytokine "barcode": GM-CSF, IFN-γ and TNF fall significantly (FDR<0.05) while IL-2 and FOXP3 are unchanged. (c) The effect is specific to the early (8 h) activation window. All values are DATASET (this screen).

**Figure 2. Mechanism and direction-of-effect.** (a) PKM2's nuclear dimer potentiates STAT3/NF-κB-driven effector cytokines (pathogenic), whereas its cytoplasmic tetramer performs housekeeping glycolysis; micheliolide covalently promotes the tetramer and blocks nuclear translocation, phenocopying the beneficial loss of nuclear PKM2 seen on knockdown. (b) The independent lines of evidence — dataset effector-selectivity, loss-of-function mechanism, in-vivo direction (TEPP-46 in EAE), compound pharmacology, and human translation — all point the same way, each with its identifier. (The genetics row is shown as a stated null: no MS *PKM*-locus GWAS signal; the target rests on causal and mechanistic, not genetic-association, evidence.)

**Figure 3. A decisive, falsifiable pilot.** (a) 2×2 compound × CRISPRi-PKM2 factorial; the mechanism-defining result is a statistical interaction (micheliolide's effect disappears in PKM2-depleted cells). Cells show the *expected* outcome under the on-target hypothesis, not observed data. (b) System, endpoints, confound controls and feasibility.

---

## Tables

**Table 1. Shortlist with inclusions and exclusions (8 h effector-selectivity ranking; representative rows).** Selectivity = (−effector z) − (−IL-2 z); larger = more effector-specific. Full table (40 rows) in `Table1_shortlist.csv`.

| Gene | z GM-CSF | z IFN-γ | z IL-2 | Selectivity | Disposition | Reason |
|---|---|---|---|---|---|---|
| LCP2 | −10.6 | −6.0 | −6.1 | 2.2 | excluded | TCR-proximal (pan-activation) |
| ZAP70 | −5.5 | −5.5 | −4.7 | 0.8 | excluded | TCR-proximal (pan-activation) |
| MED24 | −6.9 | −5.4 | −4.9 | 1.3 | excluded | general transcription |
| CSF2 | −10.9 | 0.1 | −0.3 | 5.1 | excluded | cytokine itself (trivial) |
| STAT5B | −4.8 | −4.0 | +2.7 | 7.0 | excluded | pan-activation signalling TF |
| DR1 | −4.0 | −5.3 | −0.4 | 4.2 | excluded | general transcription |
| RFT1 | −4.1 | −4.5 | +0.9 | 5.2 | candidate (deprioritized) | no natural-product ligand / direction-matched mechanism |
| DARS1 | −3.7 | −4.0 | +1.3 | 5.1 | candidate (deprioritized) | no natural-product ligand / direction-matched mechanism |
| PGK1 | −5.3 | −4.8 | −2.8 | 2.2 | candidate | glycolytic; cuts IL-2 (less selective) |
| GNPNAT1 | −3.6 | −5.1 | −2.5 | 1.9 | candidate | metabolic enzyme |
| **PKM** | **−3.7** | **−3.3** | **−0.1** | **3.4** | **★ nominated** | **effector-selective, druggable metabolic switch, natural covalent ligand, direction-matched** |

*Attrition:* ~12,748 genes targeted → 11,526 with usable cytokine-effect estimates → 195 rows (166 genes) passing the significance+reproducibility gate → 143 surviving confound filters → PKM nominated on the biology-then-tractability walk-down. Genes more selective than PKM were excluded as pan-activation/general-transcription (STAT5B, DR1) or retained but deprioritized as undruggable essential enzymes (RFT1, DARS1).

**Table 2. Direction-of-effect resolved by perturbation modality (not an identity).** ✓ = reported/observed in the correct direction; ↓ = reduced; = spared/unchanged; ? = untested/unknown. Entries are what each modality is *documented* to do; the pilot's job is to fill the MCL row in human CD4⁺ T cells.

| Modality | Target engagement | Effector cytokines | Activation / IL-2 | Proliferation | Glycolysis | Cell context | Human exposure |
|---|---|---|---|---|---|---|---|
| Gene CRISPRi (this screen) | knockdown | ↓ | spared (IL-2 =) | ? | ? | human CD4⁺ | — |
| Genetic *Pkm2* deletion [4] | none (removed) | ↓ | ✓ effector-specific | spared | preserved | mouse Th17/EAE | — |
| Reversible activator TEPP-46 [6] | tetramer ✓ | ↓ | ↓ (also dampened) | ↓ | ↓ | mouse+human CD4⁺ | research tool |
| Human MS T cells, TEPP-46 [13] | tetramer ✓ | ↓ (IFN-γ/IL-17…) | ? | ? | ? | human MS T cells | research tool |
| Covalent activator **MCL** (proposed) | tetramer, Cys424 ✓ | ↓ (predicted) | ? (to test) | ? (to test) | preserved? (to test) | to test in human CD4⁺ | prodrug, BBB+ |
| Clinical prodrug ACT001 | via MCL | ? | ? | ? | ? | human (oncology) | oral F≈51 %, BBB+ |

---

## References

[1] International Multiple Sclerosis Genetics Consortium. Multiple sclerosis genomic map implicates peripheral immune cells and microglia in susceptibility. *Science* 2019. PMID 31604244; doi:10.1126/science.aav7188.

[2] Komuczki J, et al. Fate-mapping of GM-CSF expression identifies a discrete subset of inflammation-driving T helper cells regulated by cytokines IL-23 and IL-1β. *Immunity* 2019. PMID 31079916; doi:10.1016/j.immuni.2019.04.006.

[3] Genome-scale Perturb-seq in primary human CD4⁺ T cells maps context-specific regulators of T-cell programs and human immune traits. *bioRxiv* 2025; doi:10.64898/2025.12.23.696273. Data: GEO GSE314342; SRA SRP643211.

[4] Damasceno LEA, et al. PKM2 promotes Th17 cell differentiation and autoimmune inflammation by fine-tuning STAT3 activation. *J Exp Med* 2020. PMID 32697823; doi:10.1084/jem.20190613.

[5] Kono M, et al. Pyruvate kinase M2 is requisite for Th1 and Th17 differentiation. *JCI Insight* 2019. PMID 31217348; doi:10.1172/jci.insight.127395.

[6] Angiari S, et al. Pharmacological activation of pyruvate kinase M2 inhibits CD4⁺ T cell pathogenicity and suppresses autoimmunity. *Cell Metab* 2020 (online 2019). PMID 31761564; doi:10.1016/j.cmet.2019.10.015.

[7] Li J, et al. Natural product micheliolide (MCL) irreversibly activates pyruvate kinase M2 and suppresses leukemia. *J Med Chem* 2018. PMID 29641204; doi:10.1021/acs.jmedchem.8b00241.

[8] Micheliolide interferes with PKM2–p65 interaction and inhibits inflammasome activation in macrophages after ischemic stroke. *Int Immunopharmacol* 2025. PMID 40690808; doi:10.1016/j.intimp.2025.115231.

[9] Zhang Q, et al. Parthenolide suppresses T helper 17 and alleviates experimental autoimmune encephalomyelitis. *Front Immunol* 2022. PMID 35514960; doi:10.3389/fimmu.2022.856694.

[10] Viennois E, et al. Micheliolide, a new sesquiterpene lactone that inhibits intestinal inflammation and colitis-associated cancer. *Lab Invest* 2014. PMID 25068660; doi:10.1038/labinvest.2014.89.

[11] Xi J, et al. Pharmacokinetics, tissue distribution and excretion of ACT001 in Sprague-Dawley rats and metabolism of ACT001. *J Chromatogr B* 2018. PMID 30423524; doi:10.1016/j.jchromb.2018.11.004.

[12] ClinicalTrials.gov: ACT001 Phase 1b/2a in recurrent glioblastoma (NCT05053880, active/not-recruiting, no results posted); ACT001 proof-of-concept in STAT3-high recurrent glioblastoma (NCT06894225, suspended, no results posted). Status as of July 2026.

[13] Ellmeier E, et al. (Angiari S, senior author). Targeting pyruvate kinase M2 (PKM2) reduces T cell pathogenicity in multiple sclerosis. *EBioMedicine* 2026. PMID 42208151; doi:10.1016/j.ebiom.2026.106314.

---

*Belief-ledger note.* DATASET claims (Results 3.1, Figure 1) derive from the processed DE estimates of ref [3] and are reproducible from the deposited `GWCD4i.DE_stats.h5ad`. LITERATURE claims carry PMIDs/DOIs above. INFERENCE statements — that micheliolide's tetramer-stabilising, nuclear-blocking action phenocopies the beneficial PKM2 knockdown — are explicitly reasoned from refs [4,6,7] and are the hypothesis the pilot is designed to falsify.
