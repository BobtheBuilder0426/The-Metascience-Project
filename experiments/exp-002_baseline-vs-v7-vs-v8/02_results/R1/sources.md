# Sources

Database identifiers (ontology, target, compound, and trial IDs) were retrieved directly
via the MCP connector calls logged in `process_trace.json`. The three core papers
(1–3) were located by DOI and, for Meisel 2024, the full text was fetched and read.
Bibliographic details (volume/issue/pages, PMID/PMCID) and the supporting-context papers
(4) were confirmed against PubMed / publisher records via web search.

## Primary literature — the mechanistic foundation

1. **Meisel JD, Wozniak DC, et al. (Mootha lab). "Hypoxia and intra-complex genetic
   suppressors rescue complex I mutants by a shared mechanism." _Cell_ 187(3):659–675
   (2024).** DOI: **10.1016/j.cell.2023.12.010**. PMC10919891.
   — Full text retrieved and read (36 pp). Establishes that hypoxia and the intra-complex
   suppressor *nuo-3(G60D)* / NDUFA6 rescue complex I mutants by a **shared, HIF-independent,
   ROS-independent** mechanism: restoration of forward electron flow at the ubiquinone (CoQ)
   binding pocket; rescue is specific to matrix-arm (electron-conducting) mutants; residues
   within the Q-pocket are required. This is the direct genetic proof-of-concept for the
   proposed drug mechanism.

2. **Jain IH, Zazzeron L, … Zapol WM, Mootha VK. "Hypoxia as a therapy for mitochondrial
   disease." _Science_ 352(6281):54–61 (2016).** DOI: **10.1126/science.aad9642**. PMID 26917594.
   — 11% O₂ chronic hypoxia dramatically extends survival and reverses neuropathology in the
   *Ndufs4*-KO Leigh mouse; genome-wide CRISPR screen identifies the hypoxia response as a
   suppressor of respiratory-chain dysfunction.

3. **Jain IH, et al. "Leigh Syndrome Mouse Model Can Be Rescued by Interventions that
   Normalize Brain Hyperoxia, but Not HIF Activation." _Cell Metabolism_ 30(4):824–832.e3 (2019).**
   PII S1550-4131(19)30379-1 (ScienceDirect pii/S1550413119303791); PMC6903907.
   — Interventions that reduce O₂ delivery (hypoxic breathing, carbon monoxide, severe anemia)
   rescue disease; genetic/pharmacologic HIF activation does **not**. Identifies brain tissue
   **hyperoxia** ("unused oxygen") as the driver. This is why HIF-PH inhibitors (roxadustat
   etc.) are the wrong node.

4. Supporting context (located via web search, not exhaustively read):
   - Warwick AM, et al. "Hypoxia-mediated rescue of retinal ganglion cells deficient in
     mitochondrial complex I is independent of the hypoxia-inducible factor pathway."
     _Scientific Reports_ 14:24114 (2024). DOI 10.1038/s41598-024-75916-x. — Deletion of *vhl*
     in *ndufs4*-deficient RGCs fails to rescue under normoxia: HIF activation is not sufficient.
   - Garg A, … Jain IH, et al. "Hypoxia rescues complex 1-associated disease caused by
     proteostatic defects." _Nature Metabolism_ (2026), published 08 Jul 2026.
     DOI 10.1038/s42255-026-01566-0. — HTRA2/CLPB loss aggregates IMS-facing complex I subunits,
     causing secondary complex I dysfunction and pathological hyperoxia corrected by hypoxia;
     extends the "unused-oxygen" model to secondary complex I disease.

   (Both corroborate HIF-independence and the breadth of the hypoxia/hyperoxia rescue; neither is
   load-bearing for the proposal, which rests on sources 1–3.)

## Databases queried (via MCP connectors)

5. **Open Targets Platform** (clinical-genomics connector; GraphQL API v4).
   - Complex I deficiency = **MONDO:0100133** — 2,420 associated targets, **0 associated drugs**.
     Top targets: NDUFS1 (0.835), NDUFS4 (0.832), NDUFS2 (0.819), NDUFV1 (0.810), FOXRED1
     (0.809), NUBPL (0.806), NDUFS7 (0.795), NDUFS8 (0.791)… (Figure 4 data).
   - Leigh syndrome = **MONDO:0009723**; LHON = **MONDO:0010788**; MELAS = **Orphanet:550**.
   - Disease→drug lists (Leigh/LHON): idebenone, vatiquinone (EPI-743), sonlicromanol,
     ubidecarenone (CoQ10), elamipretide, niacinamide, cysteamine, sirolimus, cyclosporine,
     mannitol, curcumin.

6. **ChEMBL** (chembl connector).
   - Complex I targets: **CHEMBL2363065** (Mitochondrial complex I, PROTEIN COMPLEX),
     **CHEMBL3039** (NDUFS2). Mechanism annotations on these targets are **exclusively
     INHIBITORS** (e.g. rotenone CHEMBL1703); **no activator or positive allosteric
     modulator exists** in ChEMBL — the core novelty check.
   - HIF-PH inhibitors confirmed approved/clinical: roxadustat (CHEMBL2338329, phase 4),
     daprodustat (CHEMBL3544988, ph4), vadadustat (CHEMBL3646221, ph4), molidustat
     (CHEMBL3646118, ph2); target EGLN1 = **CHEMBL5697**.

7. **PubChem** (chemistry connector) — reference-drug structures & properties: methylene blue
   (CID 6099), idebenone (CID 3686), MitoQ (CID 11388331), EPI-743 (CID 46184405),
   sonlicromanol (CID 72710875), niacinamide (CID 936), nicotinamide riboside (CID 439924),
   rotenone (CID 6758), decylubiquinone (CID 2971), coenzyme Q10 (CID 5281915).

8. **UniProt / MyGene** (genes-ontologies connector) — subunit identities: NDUFA6 **P56556**
   (accessory subunit, LYR-motif, abuts Q-module), NDUFAB1/ACP **O14561**, NDUFS2 **O75306**,
   NDUFS7 **O75251** (core Q-module subunits lining the CoQ pocket).

9. **ClinicalTrials.gov** (clinical-trials connector) — novelty/prior-art audit.
   - Leigh syndrome: 20 trials (EPI-743/vatiquinone, cysteamine bitartrate, sirolimus/ABI-009,
     KH176/sonlicromanol). Mitochondrial complex I deficiency: 3 trials (elamipretide phase 3,
     NCT05162768). Mitochondrial disease overall: 893.
   - **"methylene blue" in mitochondrial disease = 0 interventional trials.** Tried mechanisms
     are downstream antioxidants/electron-carriers and NAD⁺ precursors; none is a complex I
     allosteric activator.

## Tools / methods

10. **RDKit 2026.03.4** — molecular property calculation, 2D depiction, substructure (SMARTS)
    classification of the quinone/chromanol redox class.
11. **Wager et al. CNS MPO desirability** (ACS Chem Neurosci 2010, 1:435–449) — 6-parameter
    CNS drug-likeness score used to rank candidates vs tried drugs (Figure 2).
    Lipinski Ro5 and Veber rules for oral/permeability sanity checks.
