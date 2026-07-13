# Sources

Each identifier is tied to the single claim sentence it supports. All PMIDs, UniProt/PDB/PRIDE/Reactome accessions and expression values below were checked against their databases in the course of this work. Kinetic constants and dose values were read from the source PDFs' page glyphs (the automatic text layer corrupts the micro sign).

## The two starting papers

| Identifier | Claim it supports |
|---|---|
| DOI 10.1016/j.cmet.2025.01.024 (Sprenger et al. 2025, *Cell Metab* 37:857–869) | Exercise-induced EGT uptake via SLC22A4 makes EGT bind and activate mitochondrial MPST, raising respiration and voluntary-wheel-running performance (+19% distance, +28% peak speed), abolished in *Mpst⁻/⁻*. |
| DOI 10.1016/j.cmet.2024.12.008 (Petrovic et al. 2025, *Cell Metab* 37:542–556) | EGT is an alternative substrate for cytosolic CSE, producing H₂S that persulfidates cGPDH-Cys243 → glycerophosphate shuttle → cytosolic NAD⁺, roughly doubling time/distance to exhaustion in aged rats; abolished in CSE⁻/⁻ and *gpdh* mutants. |

## Kinetic constants and concentrations (read from source-paper figure glyphs)

| Source | Claim it supports |
|---|---|
| Sprenger Fig 3E (glyph `figures/glyph_MPST_KD.png`) | MPST binds EGT with K_D = 3.2 µM. |
| Sprenger Fig 3G (glyph `figures/glyph_MPST_Km.png`) | MPST releases H₂S with Km = 2.1 µM (95% CI 1.0–3.8 µM). |
| Sprenger text, glyph `figures/glyph_unit_corruption.png` | The PDF text layer renders "µ" as "m" (it prints "500 µM EGT" as "500 mM EGT"), so kinetic units must be read from the glyph. |
| Sprenger ITC methods (glyph `figures/glyph_ITC_concentration.png`) | Calorimetry titrated EGT into 27.5 µM MPST, giving a c-value of ≈8.6 that is only measurable if K_D is micromolar, independently confirming the µM reading. |
| Sprenger text (glyph `figures/glyph_physiological_dose.png`) | The paper's "physiologically relevant dose" of EGT is 10 µM, consistent with a micromolar-affinity target. |
| Petrovic Fig 2E (table header "Km (mM)" and plot axis) | CSE uses EGT with Km = 6.6 mM (vs 17 mM for cysteine), i.e. ~3,000× lower affinity than MPST. |
| Sprenger muscle EGT quantitation (8.89 ng/mg sedentary; ~3.6× on EGT diet) | Whole-muscle EGT ≈ 39 µM at rest and ≈ 140 µM on the EGT diet — the concentrations at which MPST is ~95% saturated and CSE runs at <1% and scales +255%. |

## Gene/protein identities (UniProt / Ensembl via MyGene)

| Identifier | Claim it supports |
|---|---|
| SQOR — UniProt Q9Y6N5 (Ensembl ENSG00000137767) | Sulfide:quinone oxidoreductase, the proposed muscle convergence node. |
| MPST — UniProt P25325 | The mitochondrial effector enzyme of the Sprenger axis. |
| CTH (CSE) — UniProt P32929 | The cytosolic effector enzyme of the Petrovic axis. |
| GPD1 — UniProt P21695 | Cytosolic glycerophosphate dehydrogenase persulfidated at Cys243. |
| GPD2 — UniProt P43304 | Mitochondrial glycerophosphate dehydrogenase feeding the CoQ pool. |
| ETHE1 — UniProt O95571 | Persulfide dioxygenase in the sulfide-oxidation pathway downstream of SQOR. |
| TST — UniProt Q16762 | Thiosulfate sulfurtransferase in the same sulfide-oxidation pathway. |
| SLC22A4 (OCTN1) — UniProt Q9H015 | The ergothioneine transporter through which EGT enters muscle. |
| CBS — UniProt P35520 | H₂S-producing enzyme included in the expression panel. |
| PPARGC1A — UniProt Q9UBK2 | PGC-1α1, which induces SLC22A4 with training in the Sprenger axis. |
| PPARA — UniProt Q07869 | PPARα co-activator partner in the transporter-induction step. |

## Expression (GTEx v8 median TPM, skeletal muscle vs liver)

| Identifier | Claim it supports |
|---|---|
| GTEx v8 — SQOR 53.2 (muscle) / 27.1 (liver) | Among sulfide-handling enzymes, SQOR is the only one more abundant in muscle than liver (1.96×). |
| GTEx v8 — CTH 1.6 (muscle) / 44.9 (liver) | CSE is nearly absent from skeletal muscle, so its role in the phenotype is likely systemic rather than muscle-intrinsic. |
| GTEx v8 — SQOR ranks 3rd of 18 tissues (muscle 53; whole blood ~87; lung ~63) | SQOR is muscle-enriched relative to other sulfide enzymes but not muscle-restricted. |
| GTEx v8 — GPD1 153.5 / 72.7 (2.11×), GPD2 11.2 / 1.5 (7.48×) | The glycerophosphate shuttle is genuinely muscle-enriched, supporting a muscle-loaded CoQ-feeding route. |

## Network and pathway

| Identifier | Claim it supports |
|---|---|
| STRING — ETHE1–SQOR 0.993, SQOR–TST 0.952, MPST–SQOR 0.762, CTH–SQOR 0.752 | SQOR is functionally wired to both H₂S producers (MPST, CSE) and to the downstream oxidation enzymes. |
| Reactome R-HSA-1614517 ("Sulfide oxidation to sulfate") | SQOR, ETHE1 and TST form the sulfide-oxidation pathway, with MPST and CSE one step upstream — the producer→oxidiser topology. |

## Biochemistry of the convergence node (PubMed)

| Identifier | Claim it supports |
|---|---|
| PMID 25725524 (*Methods Enzymol* 2015) | Mitochondrial SQOR oxidises H₂S and delivers the electrons into the coenzyme-Q pool. |
| PMID 23991830 (*Br J Pharmacol* 2014) | Low-level H₂S stimulates mitochondrial bioenergetic function. |
| PMID 35435014 (*Physiol Rev* 2022) | H₂S has a bell-shaped effect — stimulating respiration at low levels, inhibiting complex IV at high levels. |
| PMID 34884491 (*Int J Mol Sci* 2021) | H₂S modulates mitochondrial bioenergetics, supporting the low-vs-high dose window. |
| PMID 21699882 (*Biochim Biophys Acta* 2011) | Sulfide oxidation in rat mitochondria is a regulated, saturable process. |
| PMID 40912653 (*J Biol Chem* 2025) | Human SQOR is itself activated by H₂S, so it responds dynamically to the sulfide load the EGT axes generate. |
| PMID 36758466 (*Redox Biol* 2023) | Sulfur-oxidation flux and mitochondrial activity are under NRF2 regulation. |

## Ergothioneine transporter (PubMed)

| Identifier | Claim it supports |
|---|---|
| PMID 15795384 (*PNAS* 2005) | SLC22A4/OCTN1 is the ergothioneine transporter through which EGT enters cells. |
| PMID 34958679 (*FEBS Lett* 2022) | An inventory of the ergothioneine transporter's substrates and tissue locations. |

## Structures (PDB)

| Identifier | Claim it supports |
|---|---|
| PDB 4JGT | Human MPST crystal structure (2.16 Å), the mitochondrial effector. |
| PDB 2NMP | Human CSE crystal structure (2.6 Å), the cytosolic effector. |
| PDB 1WPQ | GPD1 ternary complex with NAD and DHAP (2.5 Å), the persulfidated shuttle enzyme. |
| PDB 6MO6, 6MP5, 6OI5, 6OI6, 6OIB, 6OIC, 6WH6, 8DHK | Eight experimental human SQOR structures, establishing SQOR as a well-characterised flavoenzyme. |

## Proteomics deposits (PRIDE)

| Identifier | Claim it supports |
|---|---|
| PRIDE PXD056181 | Sprenger muscle proteomics deposit (the paper's retrievable ProteomeXchange dataset). |
| PRIDE PXD051587 | Petrovic *C. elegans* persulfidation-proteomics deposit. |
| PRIDE PXD051609 | Petrovic mouse CSE thermal-proteomics deposit. |

## Novelty checks (searches that returned essentially nothing)

| Search (database) | Claim it supports |
|---|---|
| PubMed & OpenAlex — "ergothioneine" + "sulfide:quinone oxidoreductase / SQOR" | No prior work connects EGT to SQOR in muscle (the single PubMed hit, PMID 27005325, is a fission-yeast oxidative-stress study, a false match). |
| PubMed & OpenAlex — "ergothioneine" + "MPST" + "CSE" unified mechanism | No prior work unifies the two EGT axes into one mechanism. |
| PubMed — "ergothioneine" + "NADH shuttle" | No prior work links EGT to the NADH shuttles. |
