# The Metascience Project

**Can you use an AI research agent to discover how to make that same agent do better science — and *measure* that it worked?**

This repository is the complete, auditable record of a small meta-science project that treats
that question as an experiment rather than a hunch. A human operator ran an outer **experiment
loop** (hypothesise → test → analyse → repeat) to search for a good inner **agentic loop**: a
blank general-purpose coding agent that bootstraps and drives a research agent through a fixed,
memory-free cycle. Each candidate loop design was compared against a raw, unscaffolded baseline of
the *same* research agent, on word-identical questions, scored blind by two independent judges.

**Headline finding (stated honestly).** Across three iterations, the matured loop design (v8)
scored highest on every aggregate metric and for every scorer, and improved on its predecessor (v7)
on all three test questions. The effect is **modest and the sample is small** (n = 3 questions;
one open-ended question was won by the baseline), so we report a **consistent direction, not a
powered effect**. The durable contribution is the **reusable, auditable method** for measuring
whether an agent's configuration actually helps.

---

## Start here (for a judge)

| If you have… | Read this |
|---|---|
| **2 minutes** | [`submission/summary.md`](submission/summary.md) — 174-word plain-language summary |
| **15 minutes** | [`submission/report/report.pdf`](submission/report/report.pdf) — the full report (9 pp; Abstract + Intro + Results + Discussion = 7 pp, then Methods / Sources / Supplementary) |
| **a 3-minute talk** | [`submission/talk-figures/`](submission/talk-figures/) — five slide-ready figures (SVG + PNG + PDF) |
| **to check our work** | [`submission/report/verification_ledger.csv`](submission/report/verification_ledger.csv) and [`submission/evidence/`](submission/evidence/) |

---

## What happened (the arc)

Two intertwined threads, both reconstructed step-by-step from the project labbook in
[`submission/TIMELINE.md`](submission/TIMELINE.md):

- **The experiment loop** — a pilot (exp-000) to harden the setup, then three measured iterations:
  **exp-001** (baseline vs an early loop, on aging-biology questions), **exp-002** (the central
  three-arm comparison: baseline vs v7 vs v8), and **exp-003** (an open, unscored showcase on a
  genome-scale CD4⁺ T-cell perturbation dataset).
- **The agentic-loop design** — evolving from an early flat design through **v7 → v8 → v9**. Each
  version adds a *cumulative bundle* of changes to the previous one (so a version-to-version
  difference reflects the whole bundle, not a single variable — an explicit design decision, not a
  controlled ablation).

The central result lives in **exp-002**: nine answers (three arms × three questions) scored blind
under a two-key double-blind, by an automated reviewer panel and a single human domain expert.

---

## What's in this repository

### `submission/` — the judge-facing deliverables
- [`report/report.pdf`](submission/report/report.pdf) — the report. Source in
  [`report/src/`](submission/report/src/) (HTML + print CSS + a WeasyPrint build script);
  figures in [`report/figures/`](submission/report/figures/).
- [`report/verification_ledger.csv`](submission/report/verification_ledger.csv) — every non-trivial
  claim that ships, checked live against a source (PMID / DOI / accession), with the exact metadata
  seen and the date.
- [`talk-figures/`](submission/talk-figures/) — five talk figures + a note on how they were designed.
- [`summary.md`](submission/summary.md) — the 100–200 word summary.
- [`INVENTORY.md`](submission/INVENTORY.md) — annotated map of every file and directory: what it is,
  why it exists, and whether it ships.
- [`TIMELINE.md`](submission/TIMELINE.md) — the labbook-reconstructed timeline of both threads.
- [`EVAL_DESIGN_AUDIT.md`](submission/EVAL_DESIGN_AUDIT.md) — the evaluation design laid bare: unit
  of analysis, rubric, blinding keys, aggregation rules, and documented scorer disagreements.
- [`evidence/`](submission/evidence/) — the reproducible **evidence spine**: input checksums, a
  single derivation script (`build_spine.py`) that recomputes every headline number from the raw
  per-answer scores and asserts equality with the frozen tables, the resulting `derived_numbers.json`,
  and the per-claim evidence classification (`evidence_spine.csv`).

### The research record (the working repository)
- `LABBOOK.md` — the append-only ground truth; every step is logged here.
- `experiments/` — one folder per experiment (hypothesis → setup → results → analysis).
- `loop-design/` — the evolving design of the agentic loop.
- `SOURCES.md` — the numbered source registry the report cites.
- `GOAL.md`, `ROADMAP.md`, `STATUS.md` — the project's own charter and running state.

---

## Reproducing the numbers

Every quantitative claim in the report is regenerated from raw scores by one script:

```
python submission/evidence/build_spine.py
```

It checksums its authoritative inputs, recomputes the exp-001 and exp-002 aggregates and the
Friedman statistics, and **fails loudly** if any recomputed value disagrees with the frozen analysis
tables. All captions, tables, and figures inherit their numbers from its output. The report PDF is
rebuilt from source with `python submission/report/src/build_report.py report.html report.pdf`, which
also enforces the ≤10-page budget on the counted sections.

---

## Honest scope

- **n = 3 questions per arm, one answer per cell.** The study is underpowered by construction; we
  report direction and sign-consistency, not statistical significance.
- **The gain is specific to the v8 bundle.** The intermediate v7 design did not reliably beat the
  baseline.
- **One question favoured the baseline.** The open-ended "why does aging happen" question was won by
  the baseline, unanimously across scorers — shown, not smoothed away.
- **The "combined" score is a derived summary** — the per-dimension mean of the two judges, not a
  third independent scorer or a replicate.
- **exp-003 is a showcase, not a measured win** — a single answer per arm, not scored or blinded;
  each arm's scientific claims are reported as given and were not independently re-verified. The data
  accessions it relies on, however, were confirmed live (see the verification ledger).

---

## License

Released under the MIT License — see [`LICENSE`](LICENSE).
