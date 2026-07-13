<!-- WORKED EXAMPLE — the file a pdf-digest subagent produces. This one was made by the real pipeline: render_pdf.py
     rendered all 30 pages, then a reader viewed every page IMAGE (not memory) + the text. Figure entries below are
     interpreted from the rendered figures. This is the quality bar for driver/context/<file>.digest.md. -->

# Digest: Ergothioneine_CSE_Petrovic_2025_CellMetab.pdf
**Identity:** Ergothioneine improves healthspan of aged animals by enhancing cGPDH activity through CSE-dependent
persulfidation · Petrovic, Filipović et al. · *Cell Metabolism* 37, 542–556 · 2025 (Feb 4) · DOI 10.1016/j.cmet.2024.12.008 ·
30 pages · pages covered: 1–30 (all figures viewed as rendered images).

## Synopsis
Ergothioneine (ET) extends lifespan/healthspan in *C. elegans* and improves aged-rat muscle. The paper shows this is
NOT generic antioxidant action: ET is an **alternative substrate for cystathionine-γ-lyase (CSE / CTH)**, which
desulfurates it to produce **H₂S**; H₂S **persulfidates** proteins, and persulfidation of **cytosolic
glycerol-3-phosphate dehydrogenase (cGPDH)** raises its activity, increasing **NAD⁺** and improving mitochondrial/muscle
function. Benefits are abolished in CSE-null systems and are not reproduced by hercynine (the desulfuration product).

## Objective
Is ET's healthspan benefit antioxidant-only, or a defined enzymatic mechanism — and what is the pathway from dietary ET
to improved aging phenotypes?

## Methods
- *C. elegans* lifespan (Kaplan-Meier, Mantel-Cox) + healthspan (thrashing, H₂O₂ stress survival), N ≥ 460 / ≥ 180.
- Multi-omics on D10 worms: transcriptome, total proteome, and persulfidome (dimedone-switch, PSSH).
- Genetic dependence: cth-1 (CSE) mutants; hercynine controls; mpst-3 mutants.
- Biochemistry: human recombinant CSE + ET → H₂S (lead-acetate assay); competitive two-substrate kinetics (Vmax, Km);
  SeamDock in-silico docking of ET into CSE (PDB 2NMP); PLP-catalysed mechanism by NMR/ESI-MS/UV-vis; MALDI imaging MS.
- MEF mitochondrial respiration (Seahorse OCR) in WT vs CSE⁻ᐟ⁻; HUVEC proliferation/sprouting.
- Aged rats (9-mo, 20 mg/kg ET in drinking water, 3 wk): running-to-exhaustion, gastrocnemius mass, NAD⁺/NADH, PAX7
  stem cells, TOM20, TEM; purified cGPDH persulfidation + activity; cGPDH structure PDB 1wpq (catalytic K204/C243).

## Key findings
- ET extends lifespan (median +6.8%, p<0.0001) and improves thrashing + H₂O₂-stress survival in worms (p.3, Fig.1B–D).
- ET treatment raises protein persulfidation (>300 of 2,737 persulfidated proteins up), enriched for mitochondrial
  ATP-synthase, redox, and G3P-metabolism proteins (p.3/p.6, Fig.1I–J).
- ET is an alternative CSE substrate producing H₂S, with **lower Km than cysteine**; docking shows ET in the CSE active
  site with affinity similar to cystathionine (5.8 vs 5.5 kcal/mol) (p.6, Fig.2C–E).
- Benefits are **CSE-dependent**: hercynine gives no lifespan/healthspan gain, and ET does not rescue cth-1 mutants;
  MPST is dispensable (mpst-3 still benefits) (p.8, Fig.3A–G).
- ET increases mitochondrial respiration (maximal, basal, ATP production; reserve capacity tripled) in WT but not
  CSE⁻ᐟ⁻ MEFs (p.8/p.10, Fig.3H–L).
- In aged rats ET improves running endurance, gastrocnemius mass, and raises NAD⁺/NADH; effect runs through
  persulfidation of cGPDH at C243 boosting its activity → NAD⁺ via the G3P shuttle (p.10, Fig.4C–R).

## Figures & schematics
- **Fig 1 (p.3) — ET improves lifespan/healthspan of *C. elegans*.** (A) ET chemical structure; (B) lifespan survival
  curves ET vs vehicle, p<0.0001; (C) thrashing (movement) at D4/D8/D10, ET > vehicle *–***; (D) survival under 100 µM
  H₂O₂, ET protects (p=0.002); (E) blue/green/red autofluorescence lower with ET (less age pigment); (F) mito
  morphology (Pmyo-3::mitoGFP) roundness distributions + confocal; (G–I) D10 volcano plots — transcriptome, total
  proteome, and PSSH persulfidome (I is strongly one-sided → ET drives a unidirectional INCREASE in persulfidation);
  (J) GO semantic-space bubble plot of persulfidated targets (metabolic processes incl. glycerol-3-phosphate, mito
  electron transport, translation). *Why it matters:* establishes the phenotype + points at persulfidation of
  mito/G3P proteins as the mechanism to chase.
- **Fig 2 (p.6) — ET is a substrate for CSE to produce H₂S.** (A) thermal proteome profiling melt curves identifying
  CSE as the ET target; (B) SF7-AM H₂S imaging in WT vs CSE⁻ᐟ⁻ MEFs; (C) **SeamDock docking of ET into human CSE
  (PDB 2NMP)** active site (hydrophobicity surface + H-bonds); (D) recombinant-CSE H₂S generation (lead acetate) —
  faster/greater with ET, ET alone produces H₂S; (E) competitive two-substrate kinetics: Vmax like cysteine but Km
  lower; (F) proposed PLP-catalysed desulfuration mechanism (NMR/MS/UV-vis annotated); (G) ¹H NMR of ET in WT vs
  CSE⁻ᐟ⁻ cells; (H) intracellular HCys/cystathionine/cysteine. *Why it matters:* proves the first mechanistic step,
  ET→(CSE)→H₂S, with structural + kinetic + spectroscopic evidence.
- **Fig 3 (p.8) — benefits are CSE-dependent.** (A–C) hercynine (the desulfuration product) gives NO lifespan/thrash/
  stress benefit; (D–G) ET does NOT rescue cth-1 (CSE) mutants (lifespan, motility, arsenite + H₂O₂ stress); (H–L)
  Seahorse OCR in WT vs CSE⁻ᐟ⁻ MEFs — ET raises maximal/mito respiration, ATP production, and triples reserve capacity
  in WT only; (M) ECAR unchanged (not glycolytic); (N–P) ET promotes HUVEC proliferation + sprouting, abolished by
  CSE siRNA. *Why it matters:* the causal linchpin — removes the antioxidant-only explanation; the effect REQUIRES CSE.
- **Fig 4 (p.10) — ET raises NAD⁺ and improves muscle via cGPDH persulfidation.** (A) NAD⁺ up in aged worms; (B)
  NAD⁺/NADH up dose-dependently in MEFs; (C) **aged rats (20 mg/kg ET, 3 wk) run longer/further to exhaustion**;
  (D) higher gastrocnemius mass; (E) lactate; (F) muscle NAD⁺/NADH up; (G) WGA vessel density; (H) more PAX7⁺
  satellite cells; (I) TOM20 up; (J) TEM of mitochondria; (K) schematic of the cytosolic G3P shuttle (cGPDH→mGPDH→ETC)
  regenerating NAD⁺; (L) cGPDH persulfidation up in rat muscle; (M) G3P levels; (N) purified-cGPDH activity rises with
  persulfidation; (O) MS spectrum localising the persulfidated **C243**; (P) **human cGPDH structure (PDB 1wpq)** with
  catalytic **K204/C243** highlighted; (Q–R) cGPDH activity in control vs ET rat-muscle lysates. *Why it matters:*
  closes the chain to the aging phenotype and pins the effector residue (C243) — cross-species (worm→rat).

## Mechanism / model
Dietary **ET** → alternative substrate for **CSE (CTH)** → **H₂S** → **persulfidation of cGPDH at C243** → ↑cGPDH
activity → G3P shuttle regenerates cytosolic **NAD⁺** → improved mitochondrial respiration + muscle health → extended
healthspan (worms) and better aged-muscle endurance (rats). Gated by CSE (Fig.3); hercynine-independent; MPST-independent.

## Limitations & open questions
- Mammalian tissue ET bioavailability/dosing for a performance effect not fully mapped (rat dosing shown, human absent).
- Whether persulfidation targets beyond cGPDH contribute to the phenotype.
- Relationship to the parallel ET→MPST→mitochondria axis (companion paper) not integrated here — the two papers
  center different effectors (a strong place for a discriminating experiment).
- Long-term mammalian lifespan (vs healthspan/muscle) not tested.

## Claims resting on cited references
- "ET is diet-derived, taken up via OCTN1/SLC22A4" → transporter literature (background).
- "Persulfidation is a functional redox PTM" → prior persulfidation refs (method basis).
- "H₂S can act as ETC electron donor or complex-IV inhibitor depending on dose" → ref 38 (framing).
- "H₂S stimulates NAD⁺ in endothelial cells akin to NMN" → ref 40 (parallel to the NAD⁺ result).
