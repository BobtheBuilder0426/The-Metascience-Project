# Reasoning — why D-DHA follows from the data (and why it is novel, not obvious)

This document is the scientific argument: why the evidence forces this conclusion, and why
the novel step is justified rather than a guess. It is not a narrative of workflow.

## 1. The question, sharpened
- Complex I disease = failure to oxidise NADH → ATP deficit + electron leak/ROS, striking
  RGCs, basal-ganglia/brainstem neurons, heart, muscle.
- Genetically heterogeneous (mtDNA *MT-ND\** ; nuclear *NDUFS/NDUFV/NDUFA/NDUFAF*).
  ⇒ A therapy acting on a **shared downstream death mechanism** beats one tied to a single
  gene (unless gene-replacement), *if* such a mechanism exists and is druggable.

## 2. What the data say (established facts, each cited)
- **F1.** Unbiased genome-wide CRISPR screens under OXPHOS inhibition (galactose vs glucose)
  name genetic modifiers of mitochondrial dysfunction; GPX4 loss "scored as one of the
  strongest hits among our synthetic sick/lethal interactions," enhancing toxicity of
  antimycin/oligomycin/ethidium bromide (To 2019, *Cell*, PMID 31730859; 191 modifiers). GPX4
  detoxifies phospholipid hydroperoxides. *Caveat, stated for rigour:* isolated Complex I
  inhibition (piericidin) is not itself in GPX4's synthetic-lethal set in this proliferating-
  cell screen; the Complex-I-specific hit is the NADPH-supply arm (G6PD/pentose-phosphate) the
  same paper ties to ferroptosis, and ethidium bromide (a GPX4 partner) depletes the mtDNA-
  encoded Complex I subunits mutated in LHON/MELAS. The disease-cell bridge is F3.
- **F2.** That death is **ferroptosis**: rescued by ferrostatin-1 / α-tocopherol, **not** by
  the caspase inhibitor zVAD-fmk (To 2019). GPX4 needs selenium + reduced glutathione
  (Ingold 2017, *Cell*, PMID 29290465).
- **F3.** Complex I inhibition causes **oxidative damage in retinal ganglion cells**, the
  LHON-vulnerable type (Beretta 2006, PMID 16959493). Patient models exist: *MT-ND4* LHON
  iPSC-RGCs (GSE103619/PMID 29366807), iPSC OXPHOS neurons (GSE152915), *Ndufs4* Leigh mouse
  (GSE208530).
- **F4.** LHON penetrance is **not** explained by bioenergetic compensation
  (GSE144914/PMID 32687992) ⇒ a non-bioenergetic susceptibility is unexplained.
- **F5.** Lipid-peroxidation autoxidation is rate-limited by **bis-allylic H-abstraction**;
  replacing those H with D slows it via a kinetic isotope effect, and a **sub-stoichiometric**
  D-PUFA fraction suffices (Firsov et al., threshold effect, FEBS J 2019, PMID 30851224).
- **F6.** **Bis-allylic D-DHA incorporates and resists peroxidation in living brain in vivo**
  (JACS 2025, PMID 40408349). RT001 (D-linoleate ester) is orally bioavailable and membrane-
  incorporating in patients (PMID 32871154).
- **F7.** D-PUFAs give **functional rescue** in Friedreich (PMID 25499576), Parkinson-α-syn
  (PMID 33308320), AMD-like retinal degeneration (D-DHA, PMID 35257475).
- **F8.** GTEx v8: GPX4 highly expressed in all affected tissues; **SLC7A11 near-absent in
  nerve/muscle/heart** (median TPM 0.05–0.20).

## 3. The inference chain (fact → claim), with the surprising steps spelled out
1. F1+F2 ⇒ **a leading druggable death axis under respiratory-chain failure is ferroptotic
   lipid peroxidation** — nominated by a genome-wide screen, not assumed. (Top-ranked on a
   frozen composite metric over a literature-and-data-informed candidate shortlist — *not* an
   exhaustive enumeration of the eligible universe; scores are qualitative judgments and the
   winner is an inferred substrate intervention, not a node measured in the screen; nulls/
   discordant retained — Fig. 1.)
2. F3 ⇒ the same peroxidative death occurs in the **actual patient cell types**, so the
   cancer-line screen result plausibly transfers to disease neurons (the weakest transfer;
   addressed by the pilot).
3. **Surprising step A — direction choice.** The screen says "boost peroxidation defence."
   The obvious reading (activate GPX4 / add antioxidant) is a trap: GPX4 has no drug-like
   activator, and F2 shows the defence is **cofactor-limited** (GSH/selenium), while F8 shows
   the GSH-supply arm (SLC7A11) is barely expressed in the very tissues that die. In Complex I
   disease the reductant pools (GSH, NAD(P)H) and the ETC are exactly what is broken — so any
   *regenerable* antioxidant is throttled by the disease itself. ⇒ The correct move is to make
   the **substrate** unoxidizable, which needs no cofactor.
4. **Surprising step B — the compound.** F5+F6 ⇒ **bis-allylic-deuterated DHA** achieves
   substrate-level, cofactor-independent peroxidation resistance, is oral, crosses into brain,
   and is proven on-target *in the correct tissue in vivo*. F7 ⇒ the mechanism yields
   functional rescue in adjacent lipid-peroxidation diseases.
5. F4 ⇒ this fits the one susceptibility LHON genetics leaves unexplained (non-bioenergetic).
6. ∴ **D-DHA is the simplest compound that satisfies the whole chain**: it targets the
   screen-nominated death axis, in the right direction the failing cell can sustain, in the
   right tissue, genotype-agnostically.

## 4. Why this beats the obvious alternatives (decision, not opinion)
- **Antioxidants / electron carriers (idebenone, vatiquinone, MitoQ, CoQ10):** regenerable
  traps dependent on GSH/NAD(P)H/ETC — the failing pools (F2, F8). D-DHA removes the substrate,
  no cofactor needed. **Direct evidence this matters:** idebenone, the only approved LHON drug,
  must be reduced by the NAD(P)H-dependent enzyme NQO1; it helps only ~50% of patients and NQO1
  variants explain part of the non-response (PMID 38272025). A cofactor-free mechanism
  removes exactly this dependency. Also: these carriers are **active prior art** (novelty fails).
- **GPX4 activation:** no drug-like activator; still cofactor-dependent (score 0, Fig. 1).
- **NAD⁺ precursors:** correlative, cofactor-dependent, active prior art.
- **Gene therapy (rAAV2-ND4):** genotype-specific (*MT-ND4*); D-DHA is genotype-agnostic.
- **mTOR inhibition / hypoxia:** strong causal support (score 8–12) but **active prior art**
  and systemically risky; not novel.
- **ISR / OMA1-DELE1-HRI:** direction is **discordant** across models (protective in Ahola
  cardiomyopathy vs ISRIB-benefit reports) — flagged, not built on (score 2).

## 5. What is novel — separated into three honest questions
- **Mechanistic novelty: LOW, not claimed.** Substrate-level cofactor-independent peroxidation
  resistance by bis-allylic deuteration is established prior art — isotope-reinforced PUFAs
  protect mitochondria and preserve respiration (Andreyev 2015, PMID 25578654), and reviews
  already nominate D-PUFAs for "neurological, mitochondrial and retinal diseases" as a class
  (Shchepinov 2020, PMID 32113652). I did not invent the mechanism.
- **Patent novelty: LOW.** The class is patented (Retrotope US10052299B2, deuterated-PUFA
  derivatives for oxidative-stress disorders, invoking cardiolipin's role in Complex I); a
  bis-allylic D-PUFA method-of-use patent covers a named neuromuscular disease (US10154983);
  D-DHA synthesis is patented (US10730821). A "mitochondrial disease" genus claim plausibly
  reads on this use. This is therefore a **repurposing** proposal, not a composition claim.
- **Indication + rationale novelty: the real contribution.** Full search at execution time —
  PubMed, ClinicalTrials.gov, ChEMBL, OpenAlex **and** patents/preprints (Google Patents/
  Justia/USPTO): **no deuterated PUFA proposed, trialled, or patented by name for LHON, Leigh,
  or primary Complex I deficiency.** Every D-PUFA program is a different indication (FRDA/INAD/
  ALS/PSP trials; AMD/Parkinson preclinical), and the LHON patents that exist are AAV gene
  therapy (Wuhan Neurophth US11352645) or the elamipretide peptide (Stealth) — not D-PUFA. What
  is new is the **data-grounded repurposing rationale**: a CRISPR modifier screen nominates the
  ferroptotic lipid-peroxidation axis under respiratory-chain failure, and tissue-expression
  logic argues a cofactor-independent substrate approach should beat the cofactor-dependent
  antioxidants already tried in these patients.
- Framing kept honest: "**no prior proposal of D-DHA for Complex I disease found under the
  documented search**."

## 6. Scope, predictions, and the line we will not cross
- **Predicted to help:** LHON (*MT-ND1/4/6*), Leigh (*NDUFS4* etc.), Complex-I-predominant
  MELAS; DHA-rich GSH-limited post-mitotic tissue (retina/optic nerve, CNS, then heart/muscle).
- **Predicted NOT to help:** acute bioenergetic crises, fixed structural lesions; genotypes/
  tissues where death is not peroxidation-driven. D-DHA does **not** restore ATP synthesis.

## 7. Weakest link and falsification (pre-registered)
- **Weakest link:** functional rescue is cross-disease (Rung 5), not yet shown in a Complex I
  model. The pilot targets exactly this.
- **Falsify if:** in patient *MT-ND4* iPSC-RGCs, verified D-DHA membrane incorporation produces
  **no** reduction in C11-BODIPY lipid peroxidation and **no** survival benefit vs H-DHA; or
  benefit is non-selective (generic proliferation only); or worsens an independent phenotype.
- **Confidence movers:** (up) peroxidation drop + RGC/neuronal rescue in patient cells and the
  *Ndufs4* mouse; (down) incorporation-without-rescue, or ferroptosis shown not to be the
  operative death mode in patient neurons.
