<!-- WHAT THIS IS: test-set v1 for the Metascience Project Experiment Loop. Domain = aging biology / metabolism / mitochondria
     (the operator's core expertise, so his novelty/plausibility judgment is authoritative). These are the research questions
     BOTH arms answer word-identically: the raw blank-CS baseline and the CC-driven Agentic Loop. HOW TO USE: an
     experiment PINS this version in its protocol.md. Never edit a question after an experiment used it — make v2.
     Seed questions are CS-drafted for the operator to confirm/replace (see request-to-operator.md). Register externally-pinned
     data in ../../SOURCES.md. -->

# Test-set v1 — aging / metabolism / mitochondria  [CS-drafted, the operator-confirmed pending]

**Status:** DRAFT — seed questions below are CS proposals grounded in the live prior-art landscape (S-011). Awaiting
the operator's confirm/replace via `request-to-operator.md`. Do not run an experiment on this set until it is marked CONFIRMED.

## Design principles (why these questions, methodologically)
Each question is chosen to satisfy four constraints derived from the method foundations (`../../loop-design/current/method-foundations.md`):
1. **Open hypothesis-generation** (not a lookup) — so "novel + sensible" is meaningful and the loop's reasoning shows.
2. **Word-identical across arms** — the question text is fixed; both baseline and loop get exactly this string.
3. **Has a prior-art baseline** — answerable/gradeable against real literature via CS connectors (PubMed, OpenAlex,
   Open Targets, UniProt, Reactome, STRING, GTEx, ChEMBL, gnomAD/ClinVar) so **literature-distance novelty** is computable.
4. **Rewards exploiting CS** — a good answer benefits from multiple connectors + skills (so the loop that uses more of
   CS should visibly win), and the operator can judge novelty+plausibility from expertise.

## Difficulty tiers (test/baseline strategy hook)
Tagged so we can run **constant tests vs. a fixed baseline** OR **escalate difficulty with the baseline re-drawn**
(decided in the design doc). T1 = focused; T2 = integrative; T3 = cross-domain / mechanism-level.

## Seed questions (CS draft — the operator to confirm/replace/tune)

| ID | Tier | Question (draft — the word-identical prompt) | Novelty baseline (prior-art anchor) | CS connectors it invites |
|----|------|----------------------------------------------|--------------------------------------|--------------------------|
| Q1 | T1 | "Propose a novel, testable hypothesis for a mechanism by which enhancing mitochondrial quality control (mitophagy) could be pharmacologically induced to slow skeletal-muscle aging, and name a concrete candidate intervention and the assay that would test it." | mitophagy + sarcopenia is active (urolithin A etc.); ~3,951 mito-dysfunction papers (S-011) — moderate density, room for novelty | PubMed, Open Targets, ChEMBL, UniProt, Reactome, GTEx |
| Q2 | T2 | "Identify an under-explored metabolic pathway linking NAD+ decline to a specific age-related tissue dysfunction, and propose a hypothesis + intervention that would distinguish causation from correlation." | NAD+ is crowded (high prior art) → harder novelty; good stress test of recombination bias | PubMed, Reactome, KEGG-via-connectors, STRING, GTEx, ChEMBL |
| Q3 | T2 | "Propose a repurposing hypothesis: an approved drug (not currently used for aging) that could act as an exercise mimetic on mitochondrial biogenesis, with the molecular rationale and a falsifiable prediction." | exercise-mimetic is sparse (~87 papers, S-011) → high novelty headroom + strong the operator fit | ChEMBL, openFDA/Drugs@FDA, Open Targets, PubMed, ClinicalTrials |
| Q4 | T3 | "Given the hallmarks of aging, propose a single upstream node whose modulation would plausibly affect ≥3 hallmarks simultaneously in a specific cell type, with mechanism and the experiment to test the multi-hallmark effect." | "hallmarks" is very dense (~8,596, S-011) → hardest novelty; rewards cross-connector integration | PubMed, STRING, Reactome, Open Targets, GTEx, UniProt, gnomAD |

**Note:** these are *drafts to react to*. the operator may (a) confirm as-is, (b) tune wording, (c) swap in questions closer to
his current bench work, or (d) tell us which tier depth is right. His input makes his later evaluation more meaningful
(GOAL S4 "the operator's test input").

## Files in this folder
- `README.md` (this) — the question specs + design rationale.
- `request-to-operator.md` — the concrete, idiot-safe request for the operator to confirm/replace the questions.
- (after CONFIRM) `questions.json` — the machine-readable frozen question set the harness + protocol consume.
