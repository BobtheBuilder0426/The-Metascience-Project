# Reasoning: from public data to a novel exercise mimetic for sarcopenia

This document records the full line of thought — how the candidate was found, why competing options were set aside, and why the final claim is novel and defensible. Inference and hypothesis are labelled distinctly from cited fact throughout.

---

## 1. The framing problem

An "exercise mimetic for sarcopenia" is only interesting if it is *not* one of the already-crowded metabolic mimetics. The well-trodden axes — AMPK (AICAR, metformin), PPARδ (GW501516), the sirtuin–NAD⁺ arm (resveratrol, NR, NMN), PGC-1α, and the exerkines (irisin/FNDC5, MOTS-c, apelin, BAIBA, GDF15) — were treated as prior art to go *beyond*, not to rediscover. The goal was set explicitly: find the axis with the best **joint** novelty × mechanistic tractability × real-data support, and name a compound that is novel *as an exercise mimetic for sarcopenia*, not a known muscle-aging target relabelled.

**[inference]** The most defensible way to be novel here is not to find an unknown molecule, but to find an axis that the exercise-mimetic field has structurally overlooked. The entire prior-art list is metabolic/energetic. A conceptually orthogonal axis — if it is also the strongest signal in the data — is both more novel and more honest than another metabolite-sensing GPCR.

## 2. Building two comparable signatures from real data

Rather than reason from memory, two signatures were computed on a shared 60-gene anchor panel (eight axes: OXPHOS/mitochondrial biogenesis, angiogenesis, satellite-cell/regeneration, NMJ/neural, anabolic–catabolic/FoxO, senescence/inflammation, mechanotransduction, proteostasis/autophagy), so that "exercise up" and "aging down" could be read on the same ruler:

- **Exercise-trained signature** [data]: computed from human vastus lateralis RNA-seq across endurance (GSE151066), HIIT (GSE163356) and resistance (GSE157585) training, anchored to the MetaMEx meta-analysis (PMID 31980607) for direction.
- **Aged/sarcopenic signature** [data]: computed from GSE167186 (Young n=19 / Old n=29 / Sarcopenic n=24 bulk RNA-seq; PMID 36516485), with log2FC and BH-FDR calculated here from processed counts, cross-checked against Open Targets disease associations and GTEx muscle baseline.

**[data] The decisive observation:** the NMJ/denervation axis is the *strongest* aging signal in the panel — MYH8 +3.85 (FDR 9.3×10⁻⁶), CHRNA1 +1.51, MUSK +0.73 — larger than the OXPHOS decline (PPARGC1A −0.49, CKMT2 −0.53). The OXPHOS axis shows the textbook clean reversal (exercise up / aging down), but it is precisely the PGC-1α-adjacent prior-art axis. The NMJ axis is both the biggest effect and the orthogonal one.

**[cited]** This is consistent with, but stronger than, the standing view that NMJ degeneration is a hallmark of muscle wasting (PMID 26870889) and tracks sarcopenia stage in humans (PMID 39236304).

## 3. Interpreting the NMJ axis correctly (a subtlety that matters)

The NMJ axis does **not** reverse by naive per-gene sign-flip: several denervation markers (MYH8, CHRNA1) go *up* in both aging and exercise. **[inference]** The resolution is mechanistic, not arithmetic. In aging, the denervation/reinnervation program is a *failing compensation* — chronic cycles of synapse loss. In exercise, the same machinery is engaged as *successful maintenance*, and the pro-stability ligand agrin (AGRN +0.60, p=6×10⁻³) is sustained. The therapeutic goal is therefore not to suppress denervation genes but to **restore the agrin→MuSK stabilizing signal** so that compensation succeeds. This reframing is what makes MuSK *agonism* (not inhibition) the correct direction.

## 4. Scoring the candidate nodes transparently

Eleven druggable nodes across the eight axes were scored with a self-contained weighted composite, written from scratch for this task. Four criteria, each normalized to 0–1, with weights stated up front:

- **novelty (0.30)** — is the node unclaimed as an exercise mimetic for sarcopenia?
- **druggability (0.25)** — is there a real, correct-direction compound and a tractable target?
- **sarcopenia_reversal (0.25)** — strength of dysregulation in aged/sarcopenic muscle (my data + Open Targets)
- **exercise_up (0.20)** — strength of engagement in the beneficial direction by training (my data)

`composite = 0.30·novelty + 0.25·druggability + 0.25·sarcopenia_reversal + 0.20·exercise_up`

**[data/inference]** Result: MUSK 0.754 > NTRK2 0.715 > PIEZO1 0.693 > TFEB 0.615 > … The top three are all on orthogonal, under-drugged arms (NMJ, neurotrophic, mechanotransduction), and the top two both sit on the neuromuscular axis — the same axis the aging data flagged hardest. That convergence (independent data signal + independent scoring) is why the NMJ axis was chosen.

**Disqualifications and near-misses handled up front:**
- **ESRRG (ERRγ)** was disqualified: its agonist SLU-PP-332 is already publicly described as an exercise mimetic — exactly the "known target relabelled" trap. [cited]
- **The metabolite-receptor candidates** (GPR35/kynurenic acid, HCAR1/lactate) were down-weighted as adjacent-to-prior-art: same "exercise-metabolite → GPCR" shape as the exerkine prior art, with indirect or non-muscle mechanisms and very low muscle expression.
- **Direction-mismatch nodes** (YAP1, PTK2/FAK, ULK1) were down-weighted: their only clinical-stage compounds are *inhibitors*, whereas the mimetic requires *activation*.

## 5. Choosing the compound on the winning axis

On the agrin–LRP4–MuSK–DOK7 axis, three real modalities exist. The choice among them was made on mechanism and stage, not convenience:

1. **Supply agrin (NT-1654 fragment)** [cited, PMID 24520420] — improves NMJ-disassembly pathology, but acts *upstream* and remains a neurotrypsin substrate; still only preclinical. **[inference]** Mechanistically it does not escape the aging lesion.
2. **Activate MuSK directly (agonist antibody, ARGX-119)** [cited] — acts *downstream* of the agrin-loss lesion, is in phase 2, and has a completed first-in-human safety study. **Chosen.**
3. **Small-molecule MuSK potentiator** — feasible (a screen has found 8–30× enhancers, PMID 39024975) but no correct-direction clinical molecule exists yet. Kept as a forward extension, not the primary claim, to honor the hard constraint that the named compound be real and verifiable.

**[cited] ARGX-119 (adimanebart) identity and status were each verified against primary databases:** CHEMBL6068571 (antibody, phase 2); MuSK = CHEMBL5684 / UniProt O15146; five ClinicalTrials.gov records (NCT05670704, NCT06436742, NCT06441682, NCT07287982, NCT07673601); first-in-human safety in *J Clin Pharmacol* 2026 (PMID 42153453). Every one of the drug's indications is a rare neuromuscular disease — none is sarcopenia.

## 6. The novelty argument

**The premise is not novel; the connection is.** That distinction is stated plainly because the near-misses are real and must be surpassed honestly rather than ignored.

**What already exists (the premise):**
- NMJ degeneration and disrupted agrin–MuSK signaling are recognized drivers of sarcopenia — including a 2026 review that surveys "therapeutic strategies" for exactly this (PMID 41619083). [cited]
- MuSK agonist antibodies exist and are in the clinic — for myasthenic and motor-neuron diseases. [cited]
- CAF is an established sarcopenia biomarker. [cited]

**What does not exist (the gap this fills):**
- **Zero** publications or trials propose a MuSK agonist — or ARGX-119 specifically — as an *exercise mimetic* for sarcopenia (PubMed: MuSK/NMJ + "exercise mimetic" + aging = 0; ARGX-119 + sarcopenia = 0. OpenAlex full-text over ~250M works: adimanebart/ARGX-119 + sarcopenia = 0). [db]
- The 2026 NMJ-sarcopenia review (PMID 41619083) names **no specific MuSK agonist** and frames exercise as an *adjunct to combine with* NMJ agents — the opposite of a pharmacological *mimic* of exercise. [cited]
- A 2017 review of the same pathway states the gap in its own words: enhancing postsynaptic NMJ signaling is desirable but "no currently available drug has this functionality" (PMID 28825343) — written before ARGX-119 existed. [cited]
- Independent database confirmation: MuSK's top target–disease associations in Open Targets are dominated by NMJ disease (congenital myasthenic syndromes, myasthenia gravis, fetal akinesia); the only non-neuromuscular entry among them is diabetes mellitus (0.280), and sarcopenia / age-related muscle loss are absent entirely. [db]

**[inference] The defensible novel increment**, therefore, is the actionable synthesis: *this real, clinically-safe, correct-direction molecule is a rational exercise mimetic for sarcopenia because it reconstitutes the specific NMJ-stabilizing signal that exercise sustains and that a defined aging lesion destroys.* It converts a general premise (NMJ matters) plus an existing tool (a MuSK agonist) into a specific, testable, previously-unmade therapeutic hypothesis.

## 7. Why this is tractable, not just novel

**[cited/inference]** The claim is unusually testable for a novel proposal because the reagent already exists in humans. The mechanism predicts specific, falsifiable readouts (muscle force, NMJ innervation, phospho-MuSK, serum CAF), and a human biomarker bridge (serum CAF, strength) can be measured in the ongoing ARGX-119 trials without any new molecule. The full experimental plan, with explicit falsifiers for each step, accompanies this report.

## 8. Honest limitations

- **[inference]** ARGX-119 is a biologic (parenteral), not an oral small molecule — hence the small-molecule extension is flagged as the natural next step.
- **[inference]** Denervation in aging is multifactorial and includes upstream motoneuron loss; NMJ stabilization may be necessary but not sufficient. The head-to-head exercise-mimicry experiment is designed to bound exactly this — how much of exercise's neuromuscular benefit a MuSK agonist can reproduce alone.
- **[data caveat]** The aging signature's strongest values come from one deep dataset (GSE167186); the direction is corroborated by a second aging dataset, GTEx baseline, and Open Targets, but a formal multi-cohort meta-analysis would strengthen the effect-size estimate.
