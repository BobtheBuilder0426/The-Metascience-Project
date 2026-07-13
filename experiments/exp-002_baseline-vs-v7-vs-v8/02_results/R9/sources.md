# Sources — identifier ↔ claim ledger

Every non-trivial factual claim below is tied to a real retrieved identifier (DOI / PMID / GWAS EFO or study accession / rsID / UniProt / GTEx / NCT / ChEMBL). Retrieved facts and my inferences are separated explicitly. Query log with timestamps: `process_trace.json`.

## Source paper (the method/cocktail to beat)
- **DOI 10.1016/j.xcrm.2024.101449** — Hernandez-Benitez et al., *Cell Reports Medicine* 5:101449 (2024). 1C-MIM (Met, Thr, Gly, putrescine, Cys, SAM); RPC discovery method; drinking-water delivery; cardiotoxin injury; young + aged mice; mechanism via histone acetylation. *[read from `inputs/` PDF + main-text extraction]*

## Human genetic causal anchor (GWAS Catalog, via human-genetics connector)
| Claim | Identifier(s) | Type |
|-------|---------------|------|
| Grip-strength trait | EFO_0006941 | retrieved (EFO) |
| Appendicular lean mass trait | EFO_0004980 | retrieved (EFO) |
| Lean body mass trait | EFO_0004995 | retrieved (EFO) |
| Sarcopenia trait | EFO_1000653 | retrieved (EFO) |
| *SLC22A5*/OCTN2 assoc. w/ lean body mass, positive β | rs2631367 (β=+0.0125, p=3×10⁻²¹), study GCST90428120, PMID 38538606 | retrieved |
| *SLC22A5*/OCTN2 assoc. w/ grip strength, positive β | rs2631360 (β=+0.0117, p=2×10⁻¹⁶), study GCST90565845, PMID 40374629 | retrieved |
| *SLC22A4*/OCTN1 assoc. w/ lean body mass, positive β | rs11242109 (β=+0.0125, p=2×10⁻²¹), study GCST90428120, PMID 38538606 | retrieved |
| *BCKDHB* muscle assoc. strong but **direction mixed** | p=2×10⁻⁴³; rs6931421(+)/rs9350850(±)/rs2322633(−); PMID 33097823, 38538606 | retrieved |
| *GSS* muscle assoc. (excluded: 1C-adjacent) | p=6×10⁻⁴⁵; PMID 38538606, 40374629 | retrieved |
| *SRM* muscle assoc. (excluded: 1C polyamine arm) | p=2×10⁻¹²; | retrieved |
| Ergothioneine mQTL colocalizes with *SLC22A4* | EFO_0021163 → mapped gene SLC22A4 | retrieved (colocalization closed) |
| **Free** L-carnitine trait under-powered → **no formal colocalization at OCTN2** | EFO_0021612 (api_total=2, maps only *SLC22A16*) | retrieved (stated gap — carnitine mQTL did NOT close) |
| BUT multiple **acyl**carnitine species are mQTLs at the OCTN2 muscle SNP, same effect allele | rs2631367-**G**: palmitoylcarnitine p=4×10⁻¹⁶ (GCST90199666), acetylcarnitine p=8×10⁻¹⁴ (GCST90199669), hexanoylcarnitine p=2×10⁻¹² (GCST90199668); rs11242109-**T**: cerotoylcarnitine p=5×10⁻¹⁹ (GCST90200136) | retrieved (carnitine-*transport* QTL, not free-carnitine colocalization) |
| rs11242109 / rs2631367 also platelet/leukocyte/monocyte associated (5q31 pleiotropy) | variant lookups, api_total 25 / 39 | retrieved (caveat) |
| NAD⁺/NAMPT, creatine/GATM-CKM, taurine/SLC6A6, β-HB/BDH1-OXCT1, α-KG/OGDH, lactate/SLC16A1 have **0 muscle-trait rows** at full depth | gene-level queries (api_total 9/54/18/10/32/61/8; 0 muscle) | retrieved |

## Substrate identity (UniProt, via genes-ontologies connector)
- **O76082** — SLC22A5 = OCTN2 = "high-affinity sodium-dependent **carnitine** transporter." retrieved.
- **Q9H015** — SLC22A4 = OCTN1 = "**ergothioneine** transporter." retrieved.
- **P21953** — BCKDHB = branched-chain α-ketoacid dehydrogenase E1 β (BCAA catabolism). retrieved.

## Tissue expression (GTEx v8, via expression connector; median TPM, skeletal muscle)
- SLC22A5/OCTN2 = **50.3**; SLC22A4/OCTN1 = **3.5** (low; highest in blood — caveat); CPT1B = 100.5; CRAT = 120.5; SLC25A20/CACT = 49.1; CPT2 = 10.7; SLC22A16 ≈ 0. retrieved.
- SLC22A5 skeletal-muscle precomputed cis-eQTLs: **0 significant** (reported honestly — muscle GWAS signal need not act via steady-state expression). retrieved.

## Mechanism & aging-depletion (PubMed, via pubmed connector)
- **PMID 40065099** (DOI 10.1038/s44318-025-00397-1, *EMBO J* 2025, PMC12048568) — mitochondrial FAO required for satellite-cell function; *Cpt2* deletion ↓acetyl-CoA and **Pax7 acetylation**, delays regeneration; acetate rescues. **Keystone mechanism.** retrieved (full text).
- **PMID 38446314** (DOI 10.1007/s11357-024-01111-5, *GeroScience* 2024, PMC11226696) — oral ergothioneine 4–5 mg/kg/d extends male-mouse lifespan, preserves movement velocity in aging. retrieved (full text).
- **PMID 40543223** (DOI 10.1016/j.bbrc.2025.152210, *BBRC* 2025) — ergothioneine concentrates via OCTN1 in oxidative soleus muscle; 20 mg/kg oral. retrieved (abstract).
- **PMID 29534031** (DOI 10.3390/nu10030349) & **PMID 32958033** (DOI 10.1186/s12970-020-00377-2) — L-carnitine in muscle recovery / systematic review (dosing, tolerability, mixed effects). retrieved.

## Feasibility (ClinicalTrials.gov + ChEMBL connectors)
- **Levocarnitine = CHEMBL1149**, max_phase 4, **oral**, first approval **1985** (FDA-approved drug). Acetyl-L-carnitine = CHEMBL1697733, phase 3. retrieved.
- Ergothioneine — food-derived micronutrient / GRAS (not a ChEMBL drug); has human oral trials, **at least one completed** (see below). retrieved.
- Carnitine aging-muscle trials: **NCT05009654** COMPLETED, **NCT05009641** COMPLETED ("Carnitine Supplementation and Skeletal Muscle Function in Aging"); **NCT02124590** COMPLETED; **NCT03907592** COMPLETED (carnitine + resistance training); **NCT03180424** Phase 2/3, status **UNKNOWN** (functional status in older adults). retrieved.
- Ergothioneine human trials: **NCT06846827** **COMPLETED** (RCT, cognition/anti-inflammatory); **NCT06886061** **COMPLETED** (continuous ergothioneine intake); **NCT06487546** **RECRUITING** (repletion in kidney failure, Stanford). retrieved.

## Inference (mine, not retrieved — flagged as such)
- **FAO-bottleneck synergy hypothesis** (carnitine restores flux; ergothioneine protects the mitochondria carrying it) is my mechanistic synthesis linking the retrieved facts above. It is a **prediction to be tested**, not a published result.
- **Composite scores (0–3 per axis)** are my transparent weighting of the retrieved evidence, not an external metric.
- **Power-analysis CV (25%)** is a conservative assumption for per-animal mean CSA/force; the resulting n is an estimate, to be refined with pilot variance.
- The claim that carnitine/ergothioneine **decline with age in muscle** is supported in the cited literature at the level of plasma/tissue trends; exact aged-muscle depletion magnitudes should be confirmed against a targeted metabolomics dataset in a full study (no muscle-aging metabolomics accession was fabricated here).

## Tooling gaps (stated, not worked around)
- No MetaboLights / metabolomics-archive connector and no genome-scale-metabolic-model connector were available; aging-metabolome magnitudes therefore rest on cited literature, not a re-analyzed accession.
