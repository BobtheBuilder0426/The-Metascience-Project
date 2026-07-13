# Proposed compound for Complex I disease

> ## Bottom line
> I propose **repurposing deuterated docosahexaenoic acid (D-DHA)** — DHA with its
> oxidation-prone *bis*-allylic C–H sites replaced by C–D, given orally as the ethyl ester —
> as a treatment for mitochondrial **Complex I disease**, above all **LHON** and **Leigh
> syndrome**. **Mechanism:** the C–D bond breaks far more slowly than C–H at the rate-limiting
> step of lipid peroxidation, so deuterium-reinforced membrane lipids resist the
> self-propagating radical chain that kills Complex-I-deficient neurons and retinal ganglion
> cells. Unlike every antioxidant tried (idebenone, vatiquinone, MitoQ), it **hardens the lipid
> substrate itself** — needing no glutathione, NADPH, or intact electron-transport chain.
> **First experiment:** treat patient MT-ND4 LHON iPSC-derived retinal ganglion cells with
> D-DHA vs normal DHA; read out lipid peroxidation (C11-BODIPY) and survival. **Disproof:**
> incorporation without a drop in peroxidation or death.

---

## The problem, and why the obvious fixes underperform

Complex I (NADH:ubiquinone oxidoreductase) disease is the largest genetic class of
mitochondrial disease, from mtDNA mutations in core subunits (*MT-ND1/4/6* in LHON and MELAS)
or nuclear mutations in subunits/assembly factors (*NDUFS/NDUFV/NDUFA/NDUFAF*; the commonest
cause of Leigh syndrome). The shared lesion is failure to oxidise NADH, collapsing ATP output
and raising electron leak and reactive oxygen species (ROS) in the least-tolerant tissues —
retinal ganglion cells (RGCs), basal-ganglia/brainstem neurons, heart, skeletal muscle.

Essentially every therapy tried attacks the **energy/redox deficit**: electron carriers and
antioxidants (idebenone — approved for LHON [PMID 38428428]; CoQ10; MitoQ; the
α-tocotrienol-quinone **vatiquinone/EPI-743**, tested in Leigh and GPX4-deficiency models
[PMID 39930437]); NAD⁺ precursors (nicotinamide riboside, KL1333); gene therapy (rAAV2-ND4/
GS010, *MT-ND4*-specific); mTOR inhibition (rapamycin rescues the *Ndufs4* Leigh mouse
[PMID 24231806]); hypoxia/HIF activation [PMID 26917594]. I enumerated this prior art from
ClinicalTrials.gov (Placebo 28 trials; idebenone/GS010/vatiquinone/KH176/NR each 2–6) across
Leigh, LHON, MELAS and Complex-I-deficiency conditions.

These share a hidden dependency: **the antioxidant strategies are regenerable radical traps
that must themselves be reduced** — by glutathione (GSH), NAD(P)H, or a working respiratory
chain, the very pools that fail here. The clearest illustration is the only approved LHON
drug: **idebenone must be reduced by the NAD(P)H-dependent enzyme NQO1** to shuttle electrons
past Complex I, it benefits up to ~50% of patients, and NQO1 variants explain part of the
non-response [PMID 38272025]. A therapy needing no cofactor or enzyme sidesteps this failure
mode — the weakness this proposal exploits.

## Dataset-grounded rationale — the evidence chain (Fig. 3)

I grade each causal rung honestly as **PASSED / PARTIAL / UNRESOLVED / UNTESTED**.

**Rung 1 — genetic screen names the death axis · PARTIAL.** The compendium of genetic
modifiers of mitochondrial dysfunction (To et al., *Cell* 2019; genome-wide CRISPR in K562/
HAP1 under OXPHOS inhibitors, galactose vs glucose; 191 modifiers) reports verbatim that loss
of **GPX4** — the phospholipid-hydroperoxide-detoxifying glutathione peroxidase — "scored as
one of the strongest hits among our synthetic sick/lethal interactions," enhancing toxicity of
**antimycin, oligomycin and ethidium bromide**; the death is rescued by α-tocopherol/
ferrostatin-1 but **not** by caspase inhibition — i.e. **ferroptosis**, not apoptosis
[PMID 31730859]. *Why only PARTIAL:* isolated Complex I inhibition (piericidin) is **not**
itself in GPX4's synthetic-lethal set here; GPX4's partners are the CIII/CV/mtDNA lesions, and
the Complex-I-specific hit is the **NADPH-supply arm (G6PD/pentose-phosphate) feeding the same
defence** [PMID 31730859]. The anchor is a growth-*worsening* (synthetic-lethal) interaction,
not a rescue, and the proposed compound was never screened — so this rung names a *druggable
axis*, it does not prove a rescue.

**Rung 2 — the axis in patient-relevant cells · UNRESOLVED.** Partial Complex I inhibition
(rotenone) induces oxidative damage in *rat* retinal ganglion cells in primary culture — an
LHON-relevant model, but oxidative damage is **not** identical to ferroptosis [Beretta et al.,
*Neurobiol Dis* 2006, PMID 16959493]. Human patient material exists but is thin: the *MT-ND4*
LHON iPSC-RGC set is one patient + one carrier + one control (GSE103619 / PMID 29366807), plus
iPSC OXPHOS neurons (GSE152915) and the *Ndufs4* Leigh mouse (GSE208530). LHON penetrance is
**not** explained by bioenergetic compensation (GSE144914 / PMID 32687992), leaving a
non-bioenergetic (lipid-peroxidation) susceptibility as the open variable. The pilot exists to
resolve this rung directly.

**Rung 3 — drug direction · MECHANISTIC ANALOGY (not "same operation").** The screen implies
"increase lipid-peroxidation defence." Activating GPX4 is undruggable and still GSH/selenium-
dependent; every regenerable antioxidant needs the failing reductant pools. The cofactor-
**independent** move is to harden the **substrate**. This is an *analogy* — I translate a
protective loss-of-function signal into a substrate modification, not the identical genetic
operation. Its physical basis is exact: PUFA autoxidation is rate-limited by **bis-allylic
H-abstraction**, and C–D substitution slows it ~an order of magnitude, so a sub-stoichiometric
D-PUFA fraction suffices [Firsov et al., *FEBS J* 2019, PMID 30851224; Andreyev et al., *Free
Radic Biol Med* 2015, PMID 25578654].

**Rung 4 — target engagement · PASSED.** Bis-allylic **D-DHA incorporates into membrane
phospholipids and resists peroxidation in living rat brain in vivo**, lowering DHA-oxidation
products [*JACS* 2025, PMID 40408349]; D-DHA reaches neural retina/RPE with oral dosing
[PMID 35870486]. DHA is the brain/retina's most abundant, most peroxidation-prone PUFA.

**Rung 5 — disease-relevant functional rescue · UNTESTED in Complex I disease.** D-PUFAs
rescue oxidative/neurodegenerative phenotypes in Friedreich ataxia [PMID 25499576], α-synuclein
Parkinson rats [PMID 33308320], and iron-overload AMD-like retinal degeneration [D-DHA,
PMID 35257475] — but **never in a Complex I model**. RT001 (D₂-linoleate ester) is orally
bioavailable and membrane-incorporating in patients [PMID 32871154]. This is the decisive open
rung, and exactly what the pilot tests.

**Tissue-access gate (Fig. 2).** In GTEx v8, GPX4 is highly expressed across affected tissues
(basal ganglia 188–225, tibial nerve 294, muscle 197, heart 118 TPM). **SLC7A11 (cystine
import for GSH) is low in nerve/muscle/heart (0.05–0.2 TPM)** — *suggestive* that GSH-based
defence has limited headroom there, but **not dispositive**: bulk mRNA does not capture
cysteine flux or alternative import (e.g. EAAT3), and GTEx compares affected tissues, not
vulnerable-vs-spared cells. A single-cell vulnerable-vs-spared contrast remains to be done.
(GTEx has no optic-nerve/RGC tissue; the RGC claim rests on the iPSC-RGC/primary-retina data.)

## What is new — and what is not (Fig. 4)

Novelty splits into three questions with different honest answers:

**Mechanistic novelty — LOW; not claimed.** Substrate-level, cofactor-independent suppression
of lipid peroxidation by bis-allylic deuteration is established: isotope-reinforced PUFAs
protect mitochondria and preserve respiratory function [PMID 25578654], and reviews already
nominate D-PUFAs for "neurological, mitochondrial and retinal diseases" as a class
[Shchepinov, *Trends Pharmacol Sci* 2020, PMID 32113652]. I did not invent the mechanism.

**Patent novelty — LOW.** The class is patented (Retrotope US10052299B2, deuterated-PUFA
derivatives for oxidative-stress disorders, itself invoking cardiolipin's role in Complex I),
a bis-allylic D-PUFA method-of-use patent covers a named neuromuscular disease (US10154983),
and D-DHA synthesis is patented (US10730821). A genus claim to "mitochondrial disease" would
plausibly read on this use. This is a **repurposing** proposal, not a composition claim.

**Indication + data-grounded-rationale novelty — the real contribution.** Across PubMed,
ClinicalTrials.gov, ChEMBL, OpenAlex (searched 2026-07-12) **and** patents/preprints (Google
Patents/Justia/USPTO), **no deuterated PUFA has been proposed, trialled, or patented *by name*
for LHON, Leigh syndrome, or primary Complex I deficiency.** Every D-PUFA program targets a
different indication (Friedreich NCT02445794, INAD NCT03570931, ALS NCT04762589, PSP
NCT04937530, dry AMD [PMID 35257475, 35870486]); the LHON patents that exist are AAV gene
therapy (Wuhan Neurophth US11352645) or the elamipretide peptide (Stealth), **not** D-PUFA.
What is new is the **repurposing rationale**: a CRISPR modifier screen [PMID 31730859]
nominates ferroptotic lipid peroxidation as a druggable death axis under respiratory-chain
failure, and tissue-expression logic argues a cofactor-independent substrate approach should
outperform the cofactor-dependent antioxidants already tried in these patients. Conclusion,
framed honestly: *"no prior proposal of D-DHA for Complex I disease found under the documented
search."*

## Predicted effect and scope

**Should help most:** genotypes whose neurons/RGCs die by ROS-driven lipid peroxidation
downstream of Complex I failure — **LHON (*MT-ND1/4/6*)**, **Leigh (nuclear *NDUFS4* and
related)**, plausibly Complex-I-predominant MELAS. **Tissues:** DHA-rich, post-mitotic —
retina/optic nerve and CNS first, then heart/muscle. **Genotype-agnostic within Complex I
disease**, acting on a shared downstream death mechanism, not a subunit — a contrast with
*MT-ND4*-only gene therapy. **Where it should NOT help:** it does **not** restore ATP
synthesis, so not acute bioenergetic crises or fixed structural lesions; benefit should be
preventive/disease-slowing, greatest before neuronal loss; little expected where death is not
peroxidation-driven.

## Falsifiable first experiment (pilot)

**System:** patient *MT-ND4* LHON iPSC-derived RGCs (GSE103619 model) with a **genuinely
isogenic mutation-corrected** control (CRISPR/cybrid). **Arms:** D-DHA ethyl ester vs equimolar
normal (H)-DHA vs vehicle. **Dose/duration:** 3–10 µM, 7–14 days, tied to the D-DHA membrane-
incorporation windows reported in retina and in patients [PMID 35870486, 32871154]; verify
incorporation by LC-MS/MS before reading efficacy. **Positive control (genetic recapitulation):**
GPX4 knockdown to force ferroptosis, expected rescued by ferrostatin-1. **On-mechanism test
(substrate-appropriate):** because only the isotope differs, D-DHA-vs-H-DHA *is* the on-target
contrast; benefit must track deuteration, and must shrink against a peroxidation-independent
stressor. **Primary readout:** C11-BODIPY 581/591 lipid peroxidation (the To 2019 probe) + RGC
survival; **selectivity/health:** MDA/4-HNE, and general viability/cytotoxicity to exclude
non-specific effects. **Expected:** D-DHA lowers peroxidation and improves survival vs H-DHA,
non-inferior to ferrostatin-1. **Reject the hypothesis if:** verified incorporation but no drop
in peroxidation/death; benefit not isotope-dependent; benefit only in the uncorrected line
(no selective rescue); or an independent phenotype worsens. Feasible in ~6–8 weeks for one
researcher with the published line and RT001-class material.

## Risks, caveats, and what would move confidence

**Weakest link:** Rung 5 is UNTESTED in Complex I disease — cross-disease rescue only; the
pilot closes exactly this. **Others:** (1) if death is ATP-failure- rather than peroxidation-
dominated in a genotype, effect is small; (2) dietary PUFAs dilute the deuterated pool —
sustained dosing needed; (3) the CRISPR anchor is proliferating cancer lines, not under
selective Complex I inhibition — the iPSC-RGC/Leigh-mouse work is the necessary post-mitotic
bridge; (4) the tissue-access argument rests on bulk mRNA and lacks a vulnerable-vs-spared
contrast; (5) GTEx has no optic-nerve coverage. **Most would raise confidence:** D-DHA lowering
peroxidation and rescuing survival in patient RGCs and the *Ndufs4* mouse; **lower it:** clean
incorporation-without-rescue, or ferroptosis shown not to be the operative death mode in
patient neurons.
