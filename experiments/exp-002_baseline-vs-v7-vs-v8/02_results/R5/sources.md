# Sources — every identifier queried live via connectors

## Disease / target (clinical-genomics, genes-ontologies)
- Disease ontology: **MONDO:0100133** "mitochondrial complex I deficiency" (also EFO). Nuclear-type-1 subtype MONDO:0100224.
- Open Targets (efo MONDO_0100133): 2420 associated targets; top by score NDUFS1 (0.835, ENSG00000023228), NDUFS4 (0.832, ENSG00000164258), NDUFS2 (0.819), NDUFV1 (0.810), FOXRED1 (0.809), NUBPL (0.806). **Approved/candidate disease drugs = 0** (drugAndClinicalCandidates count = 0).
- UniProt: NDUFS4 **O43181**, NDUFS1 P28331, NDUFV1 P49821, NDUFS2 O75306.
- Reactome (v97): **R-HSA-611105** Respiratory electron transport; **R-HSA-6799198** Complex I biogenesis.
- GTEx: NDUFS4 TPM — Muscle_Skeletal 120.3, Artery_Tibial 118.1, Cells_Cultured_fibroblasts 115.8, Nerve_Tibial 104.8.
- ClinVar (release 2026-06-06) pathogenic/likely-pathogenic counts (P + LP + P/LP; "Conflicting classifications" excluded): NDUFV1 68 (of 531 total), NDUFS1 50 (402), NDUFS4 47 (210); assembly ACAD9 184 (1100), NDUFAF5 118 (555), FOXRED1 62 (505), NUBPL 20 (199). mtDNA variant counts (mitochondrial_variants): MT-ND5 1711, MT-ND4 1373, MT-ND2 962, MT-ND1 942, MT-ND6 476, MT-ND3 311.

## Therapeutic landscape (PubMed, all PMIDs verified)
- Idebenone (LHON) — PMID 27798429
- Vatiquinone / EPI-743 — PMID 38883711 (preclinical eval; preprint); ferroptosis/15-LO mechanism PMID 30921410
- Elamipretide / SS-31 — PMID 34572131
- Sonlicromanol / KH176 — PMID 35477351
- MitoQ — PMID 37454529
- Nicotinamide riboside / NAD+ — PMID 24711540
- Rapamycin (Ndufs4 mouse) — PMID 24231806
- Dichloroacetate — PMID 18411236
- Bezafibrate / PGC-1α — PMID 18762025
- Methylene blue — PMID 19384599

## Mechanistic anchors (PubMed + PMC)
- **Titov 2016** LbNOX, NAD+/NADH ratio & reductive stress — PMID 27124460, doi 10.1126/science.aad4017, PMC4850741
- **Sullivan 2015** respiration supplies electron acceptors for aspartate — PMID 26232225, doi 10.1016/j.cell.2015.07.017, PMC4522278 (companion Birsoy 2015 PMID 26232224)
- **Jain 2016** hypoxia as therapy, genome-wide screen — PMID 26917594, doi 10.1126/science.aad9642, PMC4860742
- **To 2019** compendium of genetic modifiers; GPX4 synthetic sick/lethal — PMID 31730859, doi 10.1016/j.cell.2019.10.032, PMC7053407

## Discovery datasets (GEO, omics-archives) — opened and analysed
- **GSE149616** cerebellum RNA-seq, complex-I cKO + NDI1 rescue (24 samples) — PMID 32574562 ("NAD+ Regeneration Rescues Lifespan, but Not Ataxia..."). Count file GSE149616_htseq.all.counts.txt.gz.
- **GSE242286** Ndufs4-KO cortex+hippocampus (36 samples) — PMID 40731203 ("Mitochondrial complex I deficiency induces Alzheimer's disease-like signatures that are reversible by targeted therapy"; Alzheimer's & Dementia, 2025). GSE242286_Ndufs4_knockout_Rawcounts.txt.gz.
- **GSE27041** human complex-I-patient fibroblasts vs controls (20 samples) — PMID 22033105 (Nrf2-Keap1 / selenoprotein response).

## Candidate chemistry (PubChem, ChEMBL)
- **Edaravone** — CID 4021, InChIKey QELUYTUMUWHWMC-UHFFFAOYSA-N, C10H10N2O, MW 174.20, XLogP 1.3, TPSA 32.7, HBD 0, CAS 89-25-8, synonym MCI-186/Radicava; ChEMBL **CHEMBL290916**, max_phase 4, first_approval 2017, oral. GHS: Warning/Irritant only.
- Edaravone anti-ferroptosis / lipid-peroxidation: **PMID 36333599** (attenuates ferroptosis & lipid peroxidation, Aβ/HT22 neuronal model). Edaravone vs complex-I poison MPP⁺: PMID 18643790 (protects astrocytes via inhibition of the mitochondrial *apoptotic* pathway — a distinct death mode, not ferroptosis).
- Deferiprone (backup, iron chelation) — CID 2972, InChIKey TZXKOCQBRNJULO-UHFFFAOYSA-N, ChEMBL CHEMBL70927, phase 4, **black-box warning (agranulocytosis)**.
- Panel comparators: ferrostatin-1 (CID 4068248), liproxstatin-1 (CID 135735917), vatiquinone (CID 46184405), idebenone (CID 3686), alpha-tocopherol (CID 14985), methylene blue (CID 6099).

## Counter-evidence (verified, load-bearing)
- **Vatiquinone in vivo — PMID 38883711 (preprint):** vatiquinone robustly prevented RSL3- and BSO/iron-induced death in patient cells but **provided no survival benefit in the Ndufs4-KO Leigh mouse model** (may have reduced seizure risk). Cell-assay rescue at this node has already failed to translate in vivo — the closest available precedent for the proposed intervention.

## Novelty negative-search (PubMed)
- edaravone × "complex I deficiency": **0** results
- edaravone × Ndufs4: **0**
- edaravone × Leigh syndrome: 1 (PMID 19780807 — MELAS stroke-episode management, not primary CI)
- edaravone × mitochondrial disease: 9 (peripheral/liver/MPP+ contexts, none primary CI)

## NOT-RUN (declared, not fabricated)
- LINCS L1000 / CLUE.io signature-reversal: api.clue.io and clue.io proxy-blocked (403); GSE92742/GSE70138 matrices ~40 GB, infeasible in available memory; no connectivity scores generated. Genetic NDI1 reoxidation arm (GSE149616) used as substitute.
