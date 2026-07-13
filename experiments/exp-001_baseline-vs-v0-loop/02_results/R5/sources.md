# Sources

Every source below is tied to the specific claim it supports. Identifiers (PMID, DOI, GEO accession, ChEMBL ID, UniProt, PDB, NCT, EFO) were each verified to exist and to support the exact claim cited. Labels: **[data]** = a value computed here from the referenced public dataset; **[cited]** = a fact reported in the referenced work; **[db]** = a record retrieved from the named database.

---

## 1. The named compound: ARGX-119 (adimanebart), a MuSK agonist antibody

| Claim | Source | Type |
|---|---|---|
| ARGX-119 is a molecule record: humanized antibody, clinical phase 2 | ChEMBL **CHEMBL6068571** (molecule_type Antibody, max_phase 2.0); synonyms ARGX-119, adimanebart | [db] |
| ARGX-119 is a first-in-class agonist antibody for human MuSK that stabilizes the NMJ and reverses disease relapse | Vanhauwaert et al. (Oury), *Sci Transl Med* 2024. PMID **39292800**, DOI 10.1126/scitranslmed.ado7189 | [cited] |
| Patient-specific therapeutic benefit of ARGX-119 in MuSK myasthenia gravis models | Lim et al., *iScience* 2024. PMID **39898046**, DOI 10.1016/j.isci.2024.111684 | [cited] |
| ARGX-119 (adimanebart) first-in-human: 112 healthy adults, well tolerated, favorable safety, target-mediated PK, ADA comparable to placebo | van Bragt et al., *J Clin Pharmacol* 2026. PMID **42153453**, DOI 10.1002/jcph.70208 | [cited] |
| MuSK agonist antibody shows gene-specific benefit in congenital myasthenic syndromes | Ho et al., *Brain Commun* 2026. PMID **42146855**, DOI 10.1093/braincomms/fcag115 | [cited] |
| ARGX-119 clinical program (5 trials; none in sarcopenia/aging): Ph1 healthy volunteers (completed), Ph1b congenital myasthenic syndrome, Ph2a ALS, Ph2 SMA, Ph1 healthy volunteers | ClinicalTrials.gov **NCT05670704**, **NCT06436742**, **NCT06441682**, **NCT07287982**, **NCT07673601** | [db] |

## 2. The target: MuSK and the agrin-LRP4-MuSK-DOK7 axis

| Claim | Source | Type |
|---|---|---|
| MuSK target identity | ChEMBL **CHEMBL5684**; UniProt **O15146**; Ensembl **ENSG00000030304** | [db] |
| MuSK is druggable by small molecule (High-Quality Ligand, Druggable Family) and antibody; 0 recorded safety liabilities; disease-association landscape is dominated by NMJ disease (congenital myasthenic syndromes 0.79; the only non-neuromuscular top association is diabetes mellitus 0.28) with sarcopenia/aging absent | Open Targets Platform (GraphQL), DOI 10.1093/nar/gkac1046 | [db] |
| Structure of the 1:1:1 agrin/LRP4/MuSK signaling complex (cryo-EM, 3.8 Å) | PDB **8S9P**; Xie et al., *PNAS* 2023. PMID **37252960**, DOI 10.1073/pnas.2300453120 | [db]/[cited] |
| AlphaFold predicted models exist for all four pathway proteins (AGRN O00468, LRP4 O75096, MuSK O15146, DOK7 Q18PE1) | AlphaFold DB (via structures-interactions) | [db] |
| Specific proteolytic cleavage of agrin regulates NMJ maturation | Bolliger et al., *J Cell Sci* 2010. PMID **20980386**, DOI 10.1242/jcs.072090 | [cited] |
| Agrin-LRP4-MuSK signaling is a therapeutic target across NMJ disorders (incl. sarcopenia); enhancing postsynaptic signaling is desirable but "no currently available drug has this functionality" | Ohno et al., *Expert Opin Ther Targets* 2017. PMID **28825343**, DOI 10.1080/14728222.2017.1369960 | [cited] |

## 3. The aging lesion: neurotrypsin -> agrin cleavage -> NMJ loss -> sarcopenia

| Claim | Source | Type |
|---|---|---|
| Proteolytic cleavage of agrin (neurotrypsin overexpression) destabilizes the NMJ and causes precocious sarcopenia | Bütikofer et al., *FASEB J* 2011. PMID **21885656**, DOI 10.1096/fj.11-191262 | [cited] |
| Elevated C-terminal agrin fragment (CAF) identifies a subset of human sarcopenia patients | Hettwer et al., *Exp Gerontol* 2012. PMID **22433628**, DOI 10.1016/j.exger.2012.03.002 | [cited] |
| AGRN and neurotrypsin (PRSS12) genotypes associate with muscle mass, strength, and plasma CAF | Pratt et al., *GeroScience* 2023. PMID **36609795**, DOI 10.1007/s11357-022-00721-1 | [cited] |
| Failed reinnervation drives denervated-myofiber accumulation in aged muscle | Aare et al., *Skelet Muscle* 2016. PMID **27588166**, DOI 10.1186/s13395-016-0101-y | [cited] |
| NMJ degeneration is a hallmark mechanism of age-related muscle wasting | Rudolf et al., *Curr Opin Clin Nutr Metab Care* 2016. PMID **26870889**, DOI 10.1097/MCO.0000000000000267 | [cited] |
| Neuromuscular impairment tracks sarcopenia stage in humans | Sarto et al., *J Cachexia Sarcopenia Muscle* 2024. PMID **39236304**, DOI 10.1002/jcsm.13531 | [cited] |

## 4. The exercise leg: training engages and preserves the agrin-MuSK arm

| Claim | Source | Type |
|---|---|---|
| 2-year exercise training preserves neuromuscular-system health in older adults with low muscle function | Monti et al., *J Cachexia Sarcopenia Muscle* 2023. PMID **36708273**, DOI 10.1002/jcsm.13173 | [cited] |
| Trained-muscle anchor signature (AGRN +0.60, p=6e-3; OXPHOS up; MSTN down) computed from human vastus lateralis RNA-seq | GEO **GSE151066** (PMID 35068187, endurance), **GSE163356** (PMID 35482326, HIIT), **GSE157585** (PMID 33071237, resistance) | [data] |
| Direction/acute-vs-chronic reference for the exercise signature | MetaMEx meta-analysis (Pillon et al.), *Nat Commun* 2020. PMID **31980607**, DOI 10.1038/s41467-019-13869-w | [cited] |
| Multi-loading remodeling reference dataset | GEO **GSE155959** (PMID 32755574) | [db] |

## 5. The aging signature: dysregulation in aged/sarcopenic human muscle

| Claim | Source | Type |
|---|---|---|
| NMJ/denervation is the strongest aging axis: MYH8 +3.85 (FDR 9.3e-6), CHRNA1 +1.51 (FDR 4.1e-4), MUSK +0.73 (FDR 1.1e-2) up in sarcopenic vs young; OXPHOS down (PPARGC1A -0.49, CKMT2 -0.53, ATP5F1A -0.28) | GEO **GSE167186** — bulk RNA-seq arm used for differential expression (Young n=19 / Old n=29 / Sarcopenic n=24; 4 unclassified excluded); the study also includes single-nuclei RNA-seq. Perez et al., *Aging (Albany NY)* 2022. PMID **36516485**, DOI 10.18632/aging.204435; log2FC + Mann-Whitney + BH-FDR computed here from the processed count matrix | [data] |
| Secondary aging reference (biological aging of human skeletal muscle) | GEO **GSE174106** | [db] |
| Healthy-aging transcriptome reference (GESTALT) | Tumasian et al., *Nat Commun* 2021. PMID **33795677**, DOI 10.1038/s41467-021-22168-2 | [cited] |
| Sarcopenia / muscle-atrophy target landscapes (sarcopenia EFO_1000653; muscle atrophy EFO_0009851: AR>GHR>MSTN>ACVR2B) | Open Targets Platform, DOI 10.1093/nar/gkac1046 | [db] |
| Anchor-gene muscle expression baseline (all panel genes muscle-expressed) | GTEx v8 Muscle_Skeletal, DOI 10.1126/science.aaz1776 | [db] |

## 6. Novelty landscape and vetted near-misses

| Claim | Source | Type |
|---|---|---|
| A class of small molecules enhances MuSK phosphorylation / AChR clustering (8-30x, > disulfiram) — feasibility of small-molecule MuSK activation | Miyairi et al., *Biochem Biophys Res Commun* 2024. PMID **39024975**, DOI 10.1016/j.bbrc.2024.150400 | [cited] |
| NT-1654 soluble neural agrin fragment improves NMJ-disassembly muscle pathology (an upstream, ligand-supply approach; remains a neurotrypsin substrate) | Hettwer et al., *PLoS One* 2014. PMID **24520420**, DOI 10.1371/journal.pone.0088739 | [cited] |
| Zero-hit novelty queries (MuSK/NMJ + "exercise mimetic" + aging = 0; ARGX-119 + sarcopenia = 0) | PubMed E-utilities; OpenAlex (full-text, ~250M works) | [db] |

---

### Database and tool provenance
- **GEO / NCBI** (gene-expression accessions and processed count tables)
- **Open Targets Platform** GraphQL, DOI 10.1093/nar/gkac1046 (target-disease associations, tractability, safety)
- **ChEMBL**, DOI 10.1093/nar/gkad1004 (compound and target records)
- **GTEx v8**, DOI 10.1126/science.aaz1776 (tissue baseline expression)
- **RCSB PDB** and **AlphaFold DB** (structures)
- **ClinicalTrials.gov** (trial records)
- **PubMed / PMC** and **OpenAlex** (literature and novelty search)
