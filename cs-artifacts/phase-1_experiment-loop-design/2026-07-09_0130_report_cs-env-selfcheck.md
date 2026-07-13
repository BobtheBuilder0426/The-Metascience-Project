<!-- WHAT THIS FILE IS: Claude Science's (CS) Phase-1 self-check of its OWN reachable environment, run 2026-07-09.
     It records what CS verified it can and cannot do, so the Experiment-Loop + Agentic-Loop design is grounded in the
     real environment (not assumptions). HOW TO USE: read alongside the CC-side report (2026-07-09_report_cc-env-precheck.md,
     produced by a blank Claude Code from 2026-07-09_0130_protocol_cc-env-precheck.md). Pair = the full picture. -->

# CS-side environment self-check (Phase 1)  [CS] — 2026-07-09

**Method:** two evidence classes, kept distinct. **(P) Probed live** = a tool/command returned this value in this
session (2026-07-09). **(D) Documented** = from the Claude Science handbook (S-001) / RESOURCES.md / the CC pre-check
report — capability that exists but was not exercised here. Read-only; nothing installed.

> **Correction (2026-07-09, supersedes v1):** v1 listed the local-kernel CPU/RAM/GPU row as "verified by direct probes"
> but no kernel probe had been run — the numbers were carried from RESOURCES.md (the Windows *host*). Now probed
> directly (values below). v1 also framed connectors as "only 6 available → limit the test set to 6"; that was wrong —
> the 6 are this **agent session's `host.mcp` bridge**, not a limit on Claude Science. A real CS session (what the loop
> drives) has the **full featured-connector suite pre-enabled**. Both fixed below.

## 1. Compute
| Item | Evidence | Finding | Consequence for design |
|---|---|---|---|
| **Local kernel (this CS sandbox)** | **(P)** `os.cpu_count()`=8, `sched_getaffinity`=8; `/proc/meminfo` MemTotal=3.78 GiB, MemAvailable=2.72 GiB; `uname`=`Linux 6.18…-microsoft-standard-WSL2 x86_64`; `nvidia-smi` absent | **8 logical CPUs, ~3.8 GiB total RAM (~2.7 GiB free at probe), no GPU, running in WSL2** | fine for parsing/stats/plots + connector/API-driven work; **no heavy local ML** (2.7 GiB is tight); bounded concurrency |
| Remote compute | **(P)** `list_compute` → `[]` | none configured now | no remote target for GPU skills unless one is added |
| GPU for the FINAL task | **(D)** operator approval 2026-07-09 | **up to €15 purchasable** GPU (external provider e.g. Modal, or Settings>Compute) — **final-run only, not iteration** | the final Agentic Loop MAY use one GPU step (e.g. a structure prediction) for the submission question; iteration stays GPU-free |
| Shared host machine | **(D)** RESOURCES + CC report | i5-1135G7 4C/8T, 7.7 GB total, ~2.3 GB free **after Chrome+CS+Claude are already running**, integrated GPU | the ~2.3 GB is the realistic steady state → keep everything lean; ≤2–3 light agents |

## 2. Connectors — how a CS session reaches the databases (corrected)
- **What CS actually has (D, handbook §5.1):** the **featured connector suite is *pre-enabled*** and works globally across projects, no auth, read-only — Ensembl, UCSC, MyGene, **UniProt**, **GO**, **Reactome**, OLS, **gnomAD/ClinVar/dbSNP**, GWAS Catalog, eQTL, FinnGen, **Open Targets**, **GTEx**, ENCODE/JASPAR, **InterPro/Pfam/HPA/STRING**, **PDB/AlphaFold**, EMDB, Rfam, **GEO/ArrayExpress/PRIDE/MetaboLights**, cBioPortal, **PubChem/ChEBI/Rhea/BindingDB**, openFDA, **OpenAlex/arXiv**, and more. The 4 **Directory** connectors (PubMed, ClinicalTrials, ChEMBL, bioRxiv) are separate and can need admin enabling on Team/Enterprise. **A blank or loop-driven CS session uses these as native tools once enabled in Settings.**
- **What *this agent session's* `host.mcp` bridge exposes (P):** 6 servers — `pubmed` (confirmed live: 14,216 hits for "mitochondrial dysfunction aging", 0.9 s), `chembl`, `clinical-trials`, `biorxiv`, `variants`, `biomart`. This is **my** design/testing surface, **not** a limit on CS.
- **Consequence for design:** the Agentic Loop must **enable + aggressively exploit the full CS connector suite + skills + the Reviewer** ("get the most out of CS" — GOAL). The aging/metabolism test-set domain is well covered (UniProt, Reactome, STRING, GTEx, Open Targets, gnomAD/ClinVar, GEO, PubMed, ChEMBL). My **dry-run scoring** uses the 6 I have + `host.llm`, which is enough to prove the harness runs; in production it runs inside a CS session with the full suite.

## 3. Literature & credentials (verified present)
- Contact email: **present** (usable for NCBI/EBI/Unpaywall-style services).
- OpenAlex API key: **present** (scholarly-graph queries available).
- Open-access full-text fetch: available (Unpaywall/PMC route).

## 4. Authoring / self-improvement capability (verified in catalog)
- 54 skills reachable. Key for this project: **`customize`** (create CS **Specialists** = named skills+connectors+instructions a session answers as; and author skills), **`skill-creator`**, **`figure-composer`**/`figure-style` (publication-grade figures), plus domain skills (structure prediction, dossiers).
- **Consequence:** the "CS Specialists" and "CS project-context prompt" improvement categories (GOAL D2) are **buildable on the CS side** without external tooling.

## 5. Net picture for the loop design
CS can: read/write the shared repo natively; query 6 live biomedical databases + scholarly literature; run Python/R/bash; author skills + Specialists; make publication-grade figures. CS cannot (here): run local GPU/heavy ML, or reach the un-attached connectors. **The one thing CS cannot self-verify is the CC side** — Chrome control of the CS tab (the drive channel), Codex, `claude -p`, and the local runtime area — which is exactly what the CC pre-check prompt covers.
