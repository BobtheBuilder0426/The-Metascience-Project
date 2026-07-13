# Sources & identifiers

All sources drawn on, with stable identifiers. Grouped by type. Databases were queried programmatically on 2026-07-11 via their public APIs/MCP connectors.

## Key primary literature (biological rationale)

| Claim it supports | Reference | Identifier |
|---|---|---|
| Apelin is a muscle exerkine that declines with age and its restoration reverses sarcopenia | Vinel C. et al. "The exerkine apelin reverses age-associated sarcopenia." *Nature Medicine* 24, 1360–1371 (2018) | DOI **10.1038/s41591-018-0131-6**; PMID **30061698** |
| CMF-019 is the first G-protein-biased small-molecule APJ agonist (Gαi bias ~400-fold over β-arrestin); its key receptor contacts are a carboxylate↔Arg168 ionic bond and a thiophene↔Tyr88 π-stack | Read C., Fitzpatrick C.M., Yang P., Kuc R.E., Maguire J.J., Glen R.C., Foster R.E., Davenport A.P. "Cardiac action of the first G protein biased small molecule apelin agonist." *Biochem. Pharmacol.* 116, 63–72 (2016) | DOI **10.1016/j.bcp.2016.07.018**; PMID **27475715**; PMCID **PMC5012889** |
| CMF-019 structure/IUPAC name & synthesis — independently confirms the C5-carboxamide benzimidazole regiochemistry used in this work | Trifonov L., Afri M., Palczewski K., Korshin E.E., Gruzman A. "An Expedient Synthesis of CMF-019: (S)-5-Methyl-3-{1-(pentan-3-yl)-2-(thiophen-2-ylmethyl)-1H-benzo[d]imidazole-**5**-carboxamido}hexanoic Acid, a Potent Apelin Receptor (APJ) Agonist." *Med. Chem. (Bentham)* 14(7), 688–694 (2018) | PMID **29651942**; PMCID **PMC6993063** |
| Apelin peptide unsuitable for exogenous administration (proteolytic instability, renal clearance); CMF-019 disease-modifying without desensitisation | Read C. et al. "The G Protein Biased Small Molecule Apelin Agonist CMF-019 is Disease Modifying in Endothelial Cell Apoptosis In Vitro and Induces Vasodilatation Without Desensitisation In Vivo." *Front. Pharmacol.* 11:588669 (2020) | DOI **10.3389/fphar.2020.588669**; PMCID **PMC7944139** |

> Note: literature was used for biological framing only. Every quantitative value in the deliverables comes from the databases and computations below, not from these papers. All literature identifiers above were verified against PubMed / PubMed Central on 2026-07-11 (PMIDs/PMCIDs listed); the Frontiers article carries the 2020 volume year matching its DOI token.

## Target (protein & gene)

| Resource | Identifier |
|---|---|
| Gene symbol | **APLNR** |
| Ensembl gene | **ENSG00000134817** |
| UniProt (protein) | **P35414** (APJ_HUMAN, apelin receptor) |
| ChEMBL target | **CHEMBL1628481** |
| Protein class | Class A (rhodopsin-like) GPCR |

## Disease ontology (Open Targets / EFO / MONDO)

| Disease | Identifier |
|---|---|
| Sarcopenia | **EFO_1000653** |
| Muscle atrophy | **EFO_0009851** |
| Muscular atrophy | **MONDO_0004323** |
| Cachexia (phenotype) | **HP_0004326** |

## PDB structures (docking template & cross-validation)

| PDB ID | Description | Method / resolution | Ligand |
|---|---|---|---|
| **7SUS** | APJ + agonist — **docking template used** | X-ray, 2.7 Å | 8EH |
| **8S4D** | APJ + CMF-019 (+ oleic acid) — identity cross-check | X-ray, 2.58 Å | A1D5N (= CMF-019) + OLA |
| **9JH3** | CMF-019–APLNR–Gi complex | cryo-EM, 2.93 Å | CMF-019 |
| **9VPM / 9VPN** | AMG 986-bound APJ | cryo-EM | AMG 986 |

## Reference / benchmark compounds (PubChem)

| Compound | Role | PubChem CID | InChIKey |
|---|---|---|---|
| **CMF-019** | G-protein-biased tool agonist (parent scaffold) | **73442763** | `VCQKKZXFASLXAH-SFHVURJKSA-N` |
| **AMG 986** | clinical-stage APJ agonist (heart failure) | **122702529** | `DOMQFIFVDIAOOT-ROUUACIJSA-N` |
| **BMS-986224** | clinical-stage APJ agonist | **137106310** | `AGZKELPIAJYRDT-UHFFFAOYSA-N` |
| **8EH** | 7SUS co-crystal agonist (triazole-sulfonamide chemotype) | — | `HNGYVRSMVVCWGF-KKSFZXQISA-N` |

## Chemical-matter & novelty databases

| Resource | Use | Identifier / scope |
|---|---|---|
| **ChEMBL** | APJ agonist SAR mining; novelty similarity search | target CHEMBL1628481; ~4,889 potent (pChEMBL ≥ 7) EC50 agonist measurements |
| **BindingDB** | orthogonal APJ ligand set | UniProt P35414; 5,105 ligands |
| **ZINC22** | commercial/known-space novelty check | exact + distance search |
| **PubChem** | registration/novelty check | InChIKey exact + 2D-flat CID lookup |

## Expression data

| Resource | Use | Value |
|---|---|---|
| **GTEx v8** | tissue expression of candidate targets | APLNR skeletal muscle median **2.63 TPM**; heart LV **8.77 TPM** |

## Databases for target triage

| Resource | Use |
|---|---|
| **Open Targets Platform** | disease-target association scores, small-molecule tractability, safety-event counts |
| **GTEx** | skeletal-muscle expression |
| **ChEMBL** | chemical-matter richness per target |

## Software / methods

| Tool | Version | Use |
|---|---|---|
| **RDKit** | 2025.03.6 | descriptors, QED, PAINS/Brenk alerts, SA score, 3D embedding, InChIKey |
| **smina** | AutoDock Vina 1.1.2 base | rigid-receptor docking & scoring |
| **Open Babel** | 3.1.0 | file conversion, protonation (pH 7.4), PDBQT prep |
| **PyMOL** (open-source) | — | binding-pose rendering |

## The proposed compound (this work)

| Field | Value |
|---|---|
| ID | **D10** (`D10_aza7_pyz_cPent_cPr`) |
| SMILES | `Cn1cc(Cc2nc3cc(C(=O)N[C@H](CC(=O)O)CC4CC4)cnc3n2C2CCCC2)cn1` |
| InChIKey | `HBARLOFZGWXLCB-SFHVURJKSA-N` |
| Formula / MW | C₂₄H₃₀N₆O₃ / 450.5 Da |

*D10 is a novel structure generated in this work; it has no external database identifier (that is the point of the novelty check).*
