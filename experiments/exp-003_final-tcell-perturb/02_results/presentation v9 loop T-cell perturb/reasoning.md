# Scientific reasoning: from a genome-scale CD4⁺ screen to micheliolide for multiple sclerosis

This document lays out the scientific line of thought that connects the evidence to the prediction — **micheliolide, acting on the PKM2 metabolic switch, to disarm encephalitogenic CD4⁺ T cells in multiple sclerosis** — and explains why the central idea is not obvious.

## 1. Why multiple sclerosis, and why the CD4⁺ compartment specifically

Autoimmune diseases differ in how cleanly their genetics point at one cell type. Multiple sclerosis (MS) is unusual: its single strongest heritable risk factor is an MHC class II allele, *HLA-DRB1\*15:01*. MHC class II presents antigen to CD4⁺ T cells and to essentially nothing else. The dominant genetic signal in MS therefore points, mechanistically, at the CD4⁺ T-cell compartment. This makes MS an unusually well-posed setting for a CD4⁺-cell-intrinsic intervention: if we can change what CD4⁺ T cells do, we are acting on a compartment the human genetics already implicate. Diseases whose genetics implicate epithelium or innate cells (for example inflammatory bowel disease) do not offer this clean a line from cause to a single manipulable cell type.

## 2. Why the GM-CSF / IFN-γ effector program is the right thing to move

Within CD4⁺ T cells, pathogenicity in CNS autoimmunity is not carried by "activation" in general but by a specific effector output. In the animal model, a discrete GM-CSF-producing (*CSF2*) T-helper state is the proximate driver of tissue damage, and removing that output interrupts the disease cascade; IFN-γ marks the parallel Th1 arm. The therapeutic goal is thus sharply defined: **suppress the GM-CSF/IFN-γ effector program without globally shutting down T-cell activation** — because a global shutdown is just immunosuppression, with its infection and malignancy costs. This reframing — target the effector *program*, spare activation — is the criterion that everything downstream is measured against.

## 3. Why a genome-scale causal screen changes what "target nomination" can be

Most target ideas come from association: a gene is differentially expressed, or sits under a GWAS peak, in disease. Association does not tell you what happens if you *remove* the gene, nor in which direction a drug should act. A genome-scale CRISPRi Perturb-seq atlas of primary human CD4⁺ T cells is different in kind: it reports, for each of >11,000 knockdowns, the causal consequence for the transcriptome and cytokine output in the relevant human cell type. That lets target nomination be a causal question — *which single knockdown moves the effector program the way we want* — rather than a correlational one.

## 4. The selectivity filter is what separates a real target from an artefact

Ranking knockdowns purely by "lowers GM-CSF and IFN-γ" returns, at the top, exactly what one would predict from first principles: the TCR-proximal signalling machinery (*LCP2*, *CD3G*, *ZAP70*, *LAT*) and the general transcriptional apparatus. These lower effector cytokines only because they shut activation down wholesale — the immunosuppression we are trying to avoid. The decisive analytic step is therefore to score each knockdown on **two axes at once**: effect on the effector program (GM-CSF + IFN-γ) *and* effect on activation (IL-2). Plotting one against the other, the pan-activation genes lie on the diagonal (they move both equally), and a small group falls off it — lowering effector cytokines while leaving IL-2 essentially untouched. That off-diagonal group is where a genuinely disease-modifying, non-immunosuppressive target must live.

## 5. Why PKM (PKM2) is the nomination

*PKM* sits in the effector-selective group: its knockdown lowers GM-CSF (z = −3.66), IFN-γ (z = −3.30) and TNF while leaving IL-2 unchanged (z = −0.05), at the early (8 h) activation window, with strong on-target knockdown and cross-donor reproducibility. Three features make it the nomination rather than merely a hit:

1. **It is selective, not a saturation artefact.** Among glycolytic genes, only *PKM* and its immediate neighbour *PGK1* produce the effect; upstream glycolytic enzymes (*HK1/2*, *GAPDH*) do not. So this is not "cells starved of ATP make fewer cytokines" — it is a specific node in lower glycolysis.
2. **It is druggable in a way the more-selective hits are not.** A few genes score even higher on selectivity, but they are either pan-activation/general-transcription factors excluded by rule (*STAT5B*, *DR1*), or enzymes with no natural-product ligand and no direction-matched pharmacology (*RFT1*, *DARS1*). PKM2 is an established druggable enzyme with defined allosteric pockets and, crucially, a *natural* ligand that moves it the right way.
3. **Its biology explains the selectivity.** PKM2 is not only a glycolytic enzyme.

## 6. The direction-of-effect problem, and how the mechanism solves it

Here is the trap that sinks naïve "the screen says knock it down, so inhibit it" reasoning. PKM2 is a glycolytic enzyme; inhibiting its enzymatic activity would impair the very metabolism that all activated T cells (including protective ones) need. If PKM2's therapeutic relevance were its enzyme activity, this would be a poor drug target.

The resolution is that **PKM2 has two physically distinct forms with opposite consequences**:
- a cytoplasmic **tetramer** that does housekeeping glycolysis, and
- a **dimer/monomer** that translocates to the nucleus and acts as a transcriptional co-activator, binding STAT3 (and NF-κB) to amplify effector-cytokine transcription.

The pathogenic function is the *nuclear moonlighting* form, not the glycolytic one. This is why CRISPRi knockdown is selective for the effector program: removing PKM2 protein preferentially removes the nuclear pool's transcriptional amplification, while glycolysis is buffered. And it dictates the **direction a drug must act**: not "inhibit the enzyme" but **"push the equilibrium toward the tetramer and keep PKM2 out of the nucleus."** Independent genetics and pharmacology confirm both halves — T-cell PKM2 deletion ameliorates EAE without impairing proliferation, and the synthetic tetramer-activator TEPP-46 (which forces the tetramer and blocks nuclear entry) limits Th1/Th17 and suppresses EAE in vivo. The screen gives the target; the mechanism gives the direction; they are derived independently and agree.

## 7. Why micheliolide is the matched natural metabolite

With the required direction defined — *tetramer-stabilising, nuclear-translocation-blocking* — the compound search is no longer "find a PKM2 binder" (many of which are inhibitors, i.e. the wrong direction) but "find a natural product that forces the tetramer." Micheliolide (MCL), a guaianolide sesquiterpene lactone from the feverfew lineage, does exactly this: it **covalently binds PKM2 at Cys424** — a cysteine present in PKM2 but absent from PKM1 — thereby promoting tetramer formation, blocking the K433 acetylation that licenses nuclear import, and reducing nuclear translocation. It is therefore predicted to *phenocopy the beneficial loss of nuclear PKM2* while leaving cytoplasmic glycolysis intact. It is a natural metabolite, its parent class (parthenolide) already alleviates EAE, and its stabilised oral prodrug crosses the blood–brain barrier — the right properties for a CNS disease.

## 8. Why this is not obvious

The non-obvious core is a **three-way match that each single field would miss on its own**:

- **A pure data-mining reading of the screen gets the direction wrong.** "Knockdown lowers the cytokine, therefore inhibit the enzyme" would nominate an enzyme inhibitor — the opposite of what helps, because it is the *non-enzymatic nuclear* form that is pathogenic. Only bringing in the moonlighting-function mechanism turns "knock it down" into the correct pharmacological instruction "stabilise the tetramer."
- **A pure pharmacology reading would never select this compound.** Micheliolide is known as an anti-leukemia / anti-inflammatory natural product; nothing in its usual description says "multiple sclerosis." Its Cys424 covalent chemistry — which happens to be an *activating*, tetramer-forcing modification rather than an inhibitory one — is precisely the rare direction the T-cell biology demands, and that alignment is only visible once the direction has been derived from the screen and the mechanism.
- **A pure genetics reading would drop PKM2 entirely.** There is no MS *PKM*-locus GWAS signal. Anchoring on human genetics — the default move — would never surface this target. It is nominated by *causal function* in the right cell type, not by association.

The novelty is thus the **specific conjunction**: an unbiased genome-scale causal screen nominates a metabolic enzyme; its moonlighting biology converts the screen's direction into a counter-intuitive "activate, don't inhibit" instruction; and a *natural* covalent metabolite happens to implement exactly that activating instruction, with CNS-penetrant chemistry, for a disease its literature never connected it to. Any one discipline, read alone, points elsewhere.

## 9. Why the proposed test is decisive

The prediction is mechanistic and therefore falsifiable in one experiment. If micheliolide acts *through* PKM2, then depleting PKM2 should abolish its effect — a statistical **interaction** in a compound × CRISPRi-PKM2 factorial. If micheliolide lowers effector cytokines just as much in PKM2-depleted cells as in intact cells, its action is off-target and the entire chain of reasoning is rejected for this indication. Making target-dependence the *primary* result — rather than a secondary confirmation of an efficacy endpoint — is what makes the pilot decisive rather than merely encouraging. The interaction is read alongside measured residual PKM2 and direct target engagement, because a partial-knockdown floor can mimic, and residual protein can mask, a true interaction. Isoform attribution (PKM2 vs PKM1, plus a complementation/rescue arm) closes the gap between perturbing the *gene* and implicating the *isoform*.
