# Reasoning: how I arrived at D10

This document traces the actual line of thought — including the branch points, the checks that changed my mind, and the two construction bugs I caught and fixed. The goal is that a reader can reconstruct *why* each decision was made, not just what the final answer is.

---

## 1. Framing the problem

"Exercise mimetic for age-related muscle loss / sarcopenia" is ambiguous between two strategies:

- **(A) Broad exercise-mimetic** — hit a master metabolic switch (AMPK, PGC-1α, PPARδ, SIRT1) that reproduces the transcriptional program of endurance exercise. This is the classic "exercise in a pill" idea (e.g. GW501516).
- **(B) Mechanism-matched exerkine mimetic** — identify a *specific* secreted exercise factor whose decline is causal in sarcopenia, and pharmacologically restore its signalling.

I chose **(B)**. Reasoning: the broad-switch approach is crowded, and its master regulators are transcription factors / nuclear receptors with broad pleiotropy and safety baggage; the task explicitly says "starting from publicly available datasets," which rewards a data-driven *target* choice rather than a mechanism I assert up front. Strategy (B) turns the problem into a tractable, evidence-rankable target-selection exercise, which is where public data (Open Targets, GTEx, ChEMBL) are strongest.

## 2. Why apelin/APJ became the hypothesis to test

A quick literature orientation surfaced apelin as the strongest exerkine candidate for muscle aging specifically: it is secreted by contracting muscle, **declines with age**, and its restoration **reverses sarcopenia** in mice (Vinel et al., *Nature Medicine* 2018). Crucially for a *small-molecule* proposal, apelin signals through a **GPCR (APJ/APLNR)** — the most druggable target class — and small-molecule agonists already exist.

But I deliberately did **not** stop at "apelin sounds good." A single compelling paper is a hypothesis, not a decision. I built a scoring matrix to test it against alternatives.

## 3. Target selection as a scored decision (not a hunch)

I assembled **eight** candidate targets spanning the plausible mechanisms:

- **APLNR** (apelin receptor — exerkine agonism)
- **MSTN** (myostatin — the obvious anti-sarcopenia target, but an *antagonism* mechanism and a biologics-dominated space)
- **GHSR** (ghrelin receptor), **MC4R**, **LEPR** (appetite/metabolic GPCRs)
- **ADRB2** (β2-adrenergic — muscle anabolism, but heavy cardiovascular safety load)
- **NTRK2**, **FGFR1** (growth-factor receptors)

For each I pulled, from public APIs:
- **Open Targets** — disease-association score for sarcopenia (EFO_1000653) and muscle atrophy (EFO_0009851); small-molecule **tractability**; and the **count of recorded safety events**.
- **ChEMBL** — the amount and quality of existing chemical matter (agonist EC50/Ki counts).
- **GTEx** — median expression in skeletal muscle (a target you want to modulate in muscle should be expressed there or in the relevant secretory/vascular compartment).

I scored each target 0–5 on seven criteria and applied weights emphasizing exerkine evidence (0.22), safety (0.15), age-direction (0.15), and druggability (0.15). **APLNR won at 4.90/5**, far ahead of MSTN (3.26) and ADRB2 (3.15) — see Figure 1. The decisive differentiators:

- **Safety**: APLNR has **0** Open Targets safety events; ADRB2 has 26, GHSR 10, FGFR1 14. For a *chronic geriatric* indication, safety dominates.
- **Chemical matter + structure**: APLNR has both rich agonist SAR (CHEMBL1628481, ~4,900 potent measurements) *and* ligand-bound crystal structures — I can both learn from known agonists and dock into a real pocket.
- **Age-direction**: agonism *restores a declining protective signal* — mechanistically cleaner than antagonizing myostatin, and better precedented pharmacologically than the appetite GPCRs.

MSTN is the "obvious" answer and scored second, but it loses on druggability (myostatin inhibition is dominated by antibodies/ligand traps; small-molecule direct inhibition is hard) and on chemical matter — so it's a weaker fit for a *small-molecule* proposal.

## 4. Why a small molecule, and why *biased* agonism

Apelin peptide is not a drug: proteolytically unstable, renally cleared, short half-life. The genuine white space is a small molecule. Reading the APJ pharmacology, one nuance is central: **signalling bias**. APJ couples to both Gαi (therapeutic: inotropy, metabolic benefit) and β-arrestin (desensitization; linked to unwanted effects). **CMF-019** is the canonical **G-protein-biased** small-molecule APJ agonist. AMG 986 and BMS-986224 are the clinical-stage benchmarks (heart failure). So the design target crystallized as: *a novel, drug-like, G-protein-biased APJ agonist.* Building on the CMF-019 scaffold is the principled way to inherit the structural determinants of bias rather than gamble on predicting it de novo.

## 5. Building the pharmacophore from a real structure

I chose **PDB 7SUS** (X-ray, 2.7 Å, bound to agonist 8EH) as the docking template and derived the orthosteric pocket computationally (residues within 4.5 Å of the co-crystal ligand). The pocket gives a clean 4-feature pharmacophore:

1. **Anionic anchor** — the ligand carboxylate salt-bridges basic residues **Arg168 / Lys268** (mimicking the C-terminal Phe carboxylate of apelin-13).
2. **Aromatic core** — into a cage of Trp85, Tyr88, Tyr264, Tyr271, Phe110, Phe291.
3. **Aryl wing** — toward Ser106/Glu198/Thr295/Ser298.
4. **Lipophilic tail** — into Met288/Leu287/Val267.

I cross-validated identities by InChIKey: the 8S4D co-crystal ligand A1D5N is **exactly CMF-019** (identical InChIKey), which confirms the pocket and the reference chemistry are consistent. (One caution I recorded: 7SUS's ligand 8EH is the *same chemotype family* as AMG 986 — a triazole-sulfonamide — but a **distinct molecule**, confirmed by non-matching InChIKey; I corrected an earlier note that implied identity.)

## 6. Design: single-change, pharmacophore-preserving

Rather than generate random analogs, I made **individually-justified single-point changes** to CMF-019, each targeting one liability:

| Step | Change | Rationale |
|---|---|---|
| D01 | *(= CMF-019 exactly)* | construction control — verified identical InChIKey |
| D02 | +7-aza core | lower logP, remove a metabolic soft spot |
| D04 | thiophene → N-Me-pyrazole | remove toxicophore, add H-bond |
| D06 | pentyl → cyclopentyl | cut rotatable bonds & logP |
| D10 | leucine → cyclopropyl-β-homoleucine | cap flexibility, keep acid anchor |

Fifteen analogs (D01–D15) explored the combinations. The **single-point SAR ladder D01→D02→D04→D06→D10** shows monotonic QED improvement (0.39→0.52) with falling logP — evidence the optimization is systematic, not lucky.

## 7. Two bugs I caught and fixed (part of the honest record)

Good process includes the errors:

- **Regiochemistry bug.** My first scaffold builder placed the carboxamide at the wrong benzimidazole position, so "D01" was a *regioisomer* of CMF-019, not CMF-019 (different InChIKey connectivity block), even though MW/logP/QED coincidentally matched. An audit flagged that the "reproduces CMF-019 exactly" claim was false. **Fix:** I rebuilt the whole series on the correct C5-carboxamide core and verified D01 ≡ CMF-019 by identical InChIKey (`VCQKKZXFASLXAH-SFHVURJKSA-N`).
- **SMILES ring-closure collision.** My string-concatenation reused ring-closure digits, so two analogs (including an interim "lead") silently became **macrocyclic artifacts** (11-membered rings) instead of open-chain azabenzimidazoles. I caught this from the 2D depiction (tangled bridged ring) and a ring-size audit. **Fix:** rebuilt every SMILES with collision-free ring numbering, re-verified all 15 as clean cores with intact acids, and **re-ran properties, novelty, and docking on the corrected structures.** This mattered: the artifact had spuriously inflated the interim lead's QED (0.72 vs the true 0.52); correcting it changed the lead selection.

Both fixes are why the final lead (D10) rests on verified structures.

## 8. Selecting the lead: integrated, not single-metric

After correction, several designs were close on drug-likeness. Rather than pick by QED alone (which would have chosen D13), I scored the shortlist with a **transparent integrated function**: drug-likeness 0.40 + docking 0.35 + pose quality 0.25. **D10 won at 0.834** (D06 0.659, D13 0.528) because it is the only design that is simultaneously (a) near-top on QED, (b) best on docking (−9.4), and (c) the only one whose **top-ranked** pose already makes the full pharmacophore (K268 salt bridge 2.96 Å + 6/7 aromatic cage). That triple-alignment is what makes D10 the defensible choice.

## 9. Validation and what I deliberately did *not* claim

- I validated the docking protocol (redock control, 1.36 Å) before trusting comparative scores.
- I confirmed novelty against three databases with a working positive control.
- I did **not** claim measured affinity, potency, or bias — docking rank-orders, it does not quantitate, and bias is inherited-by-design, not predicted. These are explicitly listed as wet-lab next steps.

The strength of the proposal is the *alignment* of independent public-data signals — target genetics/safety, tissue expression, existing chemistry, structural pharmacophore, and multiparameter design — all pointing at the same mechanism and a single novel molecule that fits it better than the current tool compound.

## 10. If I had more resources

Next steps, in order: (1) free-energy / induced-fit refinement of the D10 pose; (2) synthesize D10 and D06 and run APJ cAMP + β-arrestin assays to confirm agonism and bias; (3) microsomal stability and permeability; (4) a mouse sarcopenia model (grip strength, fiber CSA, mitochondrial markers). GPU structure-prediction (AlphaFold/Boltz co-folding) and MD were unavailable in this environment (CPU-only), so all structural work used rigid-receptor docking, which is why I treat the binding evidence as triage-grade.
