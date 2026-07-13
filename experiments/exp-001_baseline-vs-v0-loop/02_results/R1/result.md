# A novel small-molecule exercise mimetic for sarcopenia: **D10**, a G-protein–biased apelin-receptor (APJ) agonist

## The proposal in one line

I propose **D10**, a novel, drug-like small molecule designed to act as a **G-protein–biased agonist of the apelin receptor (APLNR / APJ)** — pharmacologically mimicking *apelin*, the muscle-secreted exerkine whose age-related decline drives sarcopenia and whose restoration reverses age-associated muscle loss in animal models.

| Property | Value |
|---|---|
| **Compound ID** | D10 (`D10_aza7_pyz_cPent_cPr`) |
| **SMILES** | `Cn1cc(Cc2nc3cc(C(=O)N[C@H](CC(=O)O)CC4CC4)cnc3n2C2CCCC2)cn1` |
| **InChIKey** | `HBARLOFZGWXLCB-SFHVURJKSA-N` |
| **Molecular formula** | C₂₄H₃₀N₆O₃ |
| **Molecular weight** | 450.5 Da |
| **cLogP / TPSA / QED** | 3.24 / 114.9 Å² / **0.52** |
| **Target** | APLNR / APJ (UniProt P35414), class A GPCR |
| **Docking score (7SUS)** | **−9.4 kcal/mol** (vs CMF-019 −8.3, AMG 986 −8.8) |
| **Novelty** | 0 hits in PubChem, ChEMBL (≤70 % similarity), ZINC22 |

The compound, its 3D conformer, and its docked pose are provided in `structures/` (`D10_lead.smi`, `D10_3D.sdf`, `D10_docked_pose_7SUS.pdb`, `D10_properties.json`).

---

## Why this is a credible answer

### 1. The target is the single best-supported exerkine axis for muscle aging

Exercise protects muscle largely through **exerkines** — factors secreted by contracting muscle. Among these, **apelin** stands out: it is released by skeletal muscle during contraction, its circulating level and muscle expression **decline with age**, and in mice, restoring apelin–APJ signalling **reverses age-associated sarcopenia** (Vinel et al., *Nature Medicine* 2018). Apelin acts through **APJ**, a class A GPCR, stimulating muscle mitochondrial biogenesis, protein synthesis, and satellite-cell function.

I did not assume this target — I **scored eight candidate targets** (APLNR, MSTN, GHSR, MC4R, ADRB2, NTRK2, FGFR1, LEPR) across seven weighted criteria using public data (Open Targets associations & tractability & safety, ChEMBL chemical matter, GTEx muscle expression). **APLNR won decisively** (composite 4.90 / 5; next best MSTN 3.26). It uniquely combines: strong exerkine evidence, the correct age-direction (agonism restores a declining signal), small-molecule druggability with a ligand-bound crystal structure, the richest agonist SAR in ChEMBL (target CHEMBL1628481; ~4,900 potent agonist measurements), and **zero recorded safety liabilities** in Open Targets. See **Figure 1**.

### 2. The peptide can't be a drug — a small molecule is the real opportunity

Apelin itself is a peptide: rapidly degraded, renally cleared, and unsuitable for oral chronic dosing in a geriatric population. The therapeutic gap is precisely a **stable, orally-viable small molecule** that reproduces apelin's *beneficial* signalling. Two features matter:

- **Small-molecule APJ agonists exist and are clinically precedented** — CMF-019 (a G-protein-biased tool compound), and AMG 986 / BMS-986224 (which reached clinical trials for heart failure) — establishing that the receptor is druggable by small molecules.
- **G-protein bias is desirable**: β-arrestin recruitment at APJ drives receptor desensitization and is linked to unwanted cardiovascular effects, whereas the therapeutic (inotropic / metabolic) actions are Gαi-mediated. CMF-019 is the archetypal G-protein-biased APJ agonist. **D10 is built on the CMF-019 biased scaffold**, so it inherits the structural basis of that bias by design.

### 3. D10 is a *rational, single-change* optimization of a biased agonist — not a random hit

Starting from CMF-019 (which I rebuilt exactly as design control **D01**, verified by identical InChIKey), I made four chemically-motivated, individually-justified modifications, each fixing a specific liability while **preserving all four pharmacophore features** (anionic anchor, aromatic core, aryl wing, lipophilic tail):

1. **7-aza-benzimidazole** core (imidazo[4,5-b]pyridine) — lowers cLogP and adds a metabolic-soft-spot–free H-bond acceptor.
2. **thiophene → N-methylpyrazole** — removes a known toxicophore/metabolic liability and adds a polar contact.
3. **N1 pentan-3-yl → cyclopentyl** — trims rotatable bonds and lipophilicity.
4. **leucine → cyclopropyl-β-homoleucine tail** — retains the acid anchor while capping flexibility.

Across this **true single-point SAR ladder** (D01→D02→D04→D06→D10), QED rises monotonically **0.39 → 0.52** and cLogP falls **5.67 → 3.24** (**Figure 2c**). The result: D10 fixes CMF-019's two worst drug-likeness problems (cLogP 5.67 and 11 rotatable bonds, which fail Veber and Lipinski) while keeping the pharmacophore intact.

### 4. Every computational line of evidence favours D10

- **Docking (Figure 3, Figure 5).** In the APJ orthosteric site (crystal structure 7SUS), D10 scores **−9.4 kcal/mol**, better than both reference agonists (CMF-019 −8.3, AMG 986 −8.8). Critically, **D10 is the only design whose top-ranked pose already satisfies the key pharmacophore** — a salt bridge from its carboxylate to **Lys268 (2.96 Å)** plus **6/7 aromatic-cage contacts** (Trp85, Tyr88, Phe291…). The docking setup was validated by redocking the co-crystal ligand, recovering the crystal pose at **1.36 Å RMSD**.
- **Drug-likeness / ADMET (Figure 6).** D10 **passes all five** rule sets (Lipinski, Veber, Egan, Ghose, Muegge) — the reference agonists each fail two to four. Synthetic accessibility (SA 3.32) is comparable to the references; predicted absorption is high; predicted CNS penetration is low, which is **favourable** for a peripherally-acting muscle/cardiovascular target.
- **Novelty.** D10 returns **zero matches** in PubChem (exact + 2D), ChEMBL (≤70 % similarity), and ZINC22 (exact) — it is a genuinely new chemical entity, not a known compound. (Control: the same search correctly retrieves near-neighbours for CMF-019.)

### 5. The honest bottom line

D10 is a **computationally-validated design hypothesis**, not a validated drug. Docking is a rank-ordering triage, not an affinity measurement; predicted agonism, G-protein bias, and ADMET are hypotheses that require wet-lab confirmation (calcium/cAMP and β-arrestin functional assays, microsomal stability, in-vivo muscle endpoints). What the public data *do* support strongly is the **choice of target and mechanism**, and what the computational chemistry supports is that **D10 is a novel, synthetically-accessible, drug-like molecule that fits the APJ agonist pharmacophore better than the current biased tool compound while fixing its developability liabilities.** That combination is the proposal.

---

## What "exercise mimetic" means here, concretely

D10 is intended to reproduce the *muscle-anabolic arm of exercise signalling* by agonizing the receptor for a contraction-induced exerkine (apelin) whose decline is a driver of sarcopenia. It is a mechanism-matched mimetic: rather than broadly mimicking exercise, it targets the specific, age-declining, druggable, safety-clean pathway that the public evidence most strongly ties to reversible muscle aging.

## Deliverables map

- **`result.md`** — this file (final answer + case)
- **`reasoning.md`** — the full line of thought, including dead-ends and self-corrections
- **`figures/`** — Figures 1–6, each labelled
- **`sources.md`** — all sources with identifiers (DOI, PDB, ChEMBL, UniProt, GTEx, EFO)
- **`process_trace.json`** — step-by-step machine-readable record
- **`structures/`** — D10 as SMILES, 3D SDF, docked-pose PDB, and a property sheet
- **`data/`** — all underlying tables (scoring, properties, docking, ADMET, novelty)
