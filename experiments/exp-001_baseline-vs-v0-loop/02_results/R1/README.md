# Presentation folder — novel exercise-mimetic for sarcopenia

**Answer in one line:** **D10**, a novel G-protein–biased apelin-receptor (APJ) small-molecule agonist that pharmacologically mimics the muscle exerkine *apelin* — whose age-related decline drives sarcopenia.

## Contents

| File | What it is |
|---|---|
| **`result.md`** | Final answer and the full case for it — start here |
| **`reasoning.md`** | The line of thought: target selection, design logic, self-corrections |
| **`sources.md`** | Every source with identifiers (DOI, PMID, PDB, ChEMBL, UniProt, GTEx, EFO, PubChem CID) |
| **`process_trace.json`** | Machine-readable step-by-step record of the whole workflow |
| **`figures/`** | Figures 1–6, each labelled (see below) |
| **`structures/`** | The proposed compound D10: SMILES, 2D mol, 3D SDF, docked-pose PDB, property sheet |
| **`data/`** | All underlying tables (target scoring, properties, docking, ADMET, novelty, poses) |

## Figures

1. **fig1_target_selection** — 8 candidate targets scored across 7 criteria; APLNR/APJ wins (4.90/5)
2. **fig2_property_triage** — drug-likeness landscape, lead-vs-reference, single-point SAR ladder
3. **fig3_docking** — predicted binding affinity to APJ and binding-vs-drug-likeness
4. **fig4_structures** — CMF-019 (parent) → D10 (proposed) 2D structures
5. **fig5_binding_pose** — D10 docked in the APJ orthosteric pocket (K268 salt bridge)
6. **fig6_admet** — drug-likeness rule compliance and synthetic accessibility

## The compound

```
D10   SMILES:  Cn1cc(Cc2nc3cc(C(=O)N[C@H](CC(=O)O)CC4CC4)cnc3n2C2CCCC2)cn1
      InChIKey: HBARLOFZGWXLCB-SFHVURJKSA-N
      Formula:  C24H30N6O3   MW 450.5   QED 0.52   cLogP 3.24
      Target:   APLNR / APJ (UniProt P35414)
      Docking:  -9.4 kcal/mol (PDB 7SUS); K268 salt bridge 2.96 Å; 6/7 aromatic cage
      Novelty:  0 hits in PubChem / ChEMBL (≤70%) / ZINC22
```

## Important caveat

D10 is a **computationally-validated design hypothesis**, not a validated drug. The public data strongly support the **target and mechanism**; the chemistry supports that D10 is a **novel, synthesizable, drug-like molecule that fits the APJ agonist pharmacophore better than the current biased tool compound**. Predicted agonism, G-protein bias, and ADMET require wet-lab confirmation. See the "honest bottom line" in `result.md` and limitations in `process_trace.json`.
