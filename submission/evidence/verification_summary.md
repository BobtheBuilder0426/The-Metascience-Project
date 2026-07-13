# Verification summary — live-check of shipping claims

**Date checked:** 2026-07-13 (UTC). Databases queried live via connectors; NCBI/Crossref
timestamp 2026-07-13T20:00:13Z. GEO/SRA/BioProject are dynamic databases — results reflect
their state on this date.

**Connectors used:** `mcp-omics-archives` (GEO via NCBI E-utilities db=gds), NCBI E-utilities
directly for SRA/BioProject (not exposed by the omics connector), `mcp-literature`
(OpenAlex/arXiv), Crossref, `mcp-chembl`, `mcp-pubmed`.

## Counts by result (16 checked claims)

| Result | Count |
|---|---|
| CONFIRMED | 14 |
| CORROBORATED-EXTERNAL | 2 |
| PARTIAL | 0 |
| FAILED | 0 |

No claim FAILED and none is PARTIAL — nothing in the checked set forces a report adjustment.

## PRIORITY 1 — accession verdict (plain words)

**All four exp-003 data pointers are LIVE and publicly resolvable right now — not merely
author-stated or prospective.** The report may cite them as live public accessions.

- **GEO `GSE314342`** — LIVE. Publicly released **Feb 06 2026** (submitted Dec 18 2025, last
  updated Jun 02 2026). Title *"Genome-scale perturb-seq in primary human CD4+ T cells reveals
  genes regulating T cell programs and human immune traits."*; *Homo sapiens*; **577 samples**;
  platforms GPL34284 + GPL34762; summary states 22M cells / 4 donors / 3 stimulation conditions.
- **SRA `SRP643211`** — LIVE. **785** public SRA experiment records; study name matches; *Homo
  sapiens*; CRISPRi Perturb-seq on Illumina NovaSeq X Plus; submitter Gladstone Institutes;
  linked to BioProject PRJNA1359008; runs public (e.g. SRR38883358).
- **BioProject `PRJNA1359008`** — LIVE. Single record (uid 1359008), registered **2025-11-10**;
  title matches; description states 22M primary CD4+ T cells from 4 donors under three
  stimulation conditions.
- **Preprint DOI `10.64898/2025.12.23.696273`** — LIVE / resolvable. Crossref `status: ok`,
  posted-content, publisher openRxiv, posted **2025-12-24**, 10 authors Zhu…Marson; OpenAlex
  confirms bioRxiv (CSHL), 2025, not retracted.

*Note (not a defect):* the GEO/SRA/BioProject records use the title "…**reveals** genes
regulating…" while the preprint DOI uses "…**maps context-specific regulators** of…". Same
Marson-lab study, parallel titling — not a contradiction. Both cite the same 22M-cell / 4-donor
/ 3-condition design.

## PRIORITY 2 — shipping literature claims

All 10 DOIs resolve to the stated title/authors/year/venue, concern the claimed topic, and are
not retracted (**CONFIRMED**):

- **S-015** Petrovic 2025 *Cell Metab* — ergothioneine → CSE-dependent persulfidation (cGPDH). ✓
- **S-016** Sprenger 2025 *Cell Metab* — ergothioneine → direct MPST activation. ✓
- **S-083** Hernandez-Benitez 2024 *Cell Rep Med* — 1C-metabolite cocktail → muscle regeneration. ✓
- **S-085** Zhu/Marson perturb-seq preprint — authors/title/year/venue match. ✓
- **S-002 / S-003 / S-004** ERA / Robin / Co-Scientist — all *Nature* 2026 (published 2026-05-19),
  titles match the starter-system descriptions. ✓
- **S-006** Si et al. novel-ideas · **S-008** MT-Bench · **S-017** PoLL jury — arXiv, titles and
  authors match the evaluation-methodology roles. ✓

## PRIORITY 3 — external corroboration of exp-003 drug–target facts (labelled)

These corroborate **established drug–target facts only**. They do **NOT** verify the exp-003
arms' dataset-derived target nominations, effect sizes, or disease claims — per evidence-spine
E306 those remain "as reported by each arm, not CS-verified."

- **Mycophenolic acid → IMPDH/IMPDH2** — **CORROBORATED-EXTERNAL.** ChEMBL: MPA (CHEMBL866) and
  its prodrug mycophenolate mofetil (CHEMBL1456) both carry mechanism "IMPDH inhibitor"
  (direct interaction); PubMed 262 hits incl. PMID 31924555. (ChEMBL target is the IMPDH enzyme
  family id; IMPDH2-isoform preference is standard pharmacology, consistent with the claim.)
- **Micheliolide → PKM2 (covalent, Cys424); prodrug DMAMCL/ACT001** — **CORROBORATED-EXTERNAL.**
  PubMed PMID 29641204 (*J Med Chem* 2018) confirms micheliolide *irreversibly* (covalently)
  activates PKM2; ChEMBL indexes the clinical prodrug ACT-001 (CHEMBL2220079, Phase 1). Caveats:
  micheliolide has no ChEMBL compound record under that name (only ACT-001 is indexed), and the
  exact **Cys424** residue was not separately surfaced by connector keyword search this session
  (consistent with, but not independently pinned by, the "irreversible activation" literature).

## Bottom line

Every shipping identifier the report relies on resolves and matches its stated claim. The two
Priority-3 rows are external corroboration of textbook drug–target facts, explicitly not a
re-verification of the exp-003 arms. No FAILED or PARTIAL claims — no report adjustment required.
