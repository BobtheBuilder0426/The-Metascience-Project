# A new compound for complex-I mitochondrial disease: repurpose **edaravone** as a brain-penetrant lipid-peroxidation blocker

> ## Bottom line
> Starting from public data, I nominate **edaravone** (PubChem CID 4021; InChIKey QELUYTUMUWHWMC-UHFFFAOYSA-N; ChEMBL CHEMBL290916) — an approved oral free-radical scavenger — as a **repositioning candidate for primary complex-I (CI) deficiency**. Three independent public datasets converge on one druggable vulnerability: CI-deficient cells are sensitised to **lipid peroxidation / ferroptosis driven by reductive stress**, not ATP shortage alone. A cross-lab RNA-seq signature shows loss of NADPH-dependent reactive-aldehyde detox; a genome-wide CRISPR screen makes GPX4 synthetic-lethal with CI inhibition; patient fibroblasts mount an Nrf2/selenoprotein response. Edaravone blocks this chemistry, has proven CNS exposure, and has **zero publications in primary CI disease**. A related antioxidant (vatiquinone) rescued cells but failed in vivo — so this is a testable, high-bar hypothesis, not a validated therapy.

*Labels used throughout: **[FACT]** = supported by a cited source/accession I queried; **[INFERENCE]** = my reasoning from those facts; **[SPECULATION]** = plausible but unproven.*

---

## 1. The gap in the current landscape

Complex-I deficiency is the most common OXPHOS disorder, caused by lesions in nuclear structural subunits (NDUFS1/S4/V1/S2), assembly factors (ACAD9, NDUFAF5, FOXRED1, NUBPL) or mtDNA ND genes — all three classes confirmed in ClinVar/gnomAD (pathogenic/likely-pathogenic variant counts: NDUFV1 68, NDUFS1 50, NDUFS4 47; assembly factors ACAD9 184, NDUFAF5 118, FOXRED1 62, NUBPL 20; mtDNA MT-ND5 1711 variants; release 2026-06-06). **[FACT]** Open Targets returns 2420 targets associated with MONDO:0100133 but **zero approved or candidate drugs for the disease** (drugAndClinicalCandidates count = 0). **[FACT]**

The clinical/experimental landscape clusters into three mechanistic bets (Fig. 3, top): **(i) raise the NAD⁺ pool** (nicotinamide riboside/NMN; PMID 24711540); **(ii) shuttle/relieve electrons and ROS** (idebenone 27798429, MitoQ 37454529, methylene blue 19384599, elamipretide 34572131, sonlicromanol 35477351); **(iii) reprogram metabolism/signalling** (rapamycin 24231806, bezafibrate 18762025, DCA 18411236, hypoxia 26917594). Idebenone is the only broadly approved agent (for LHON) and its benefit is partial. **[FACT]**

**My gap hypothesis [INFERENCE]:** the field mostly treats *energy supply*. But the most rigorous mechanistic work says the acute liability of a failing respiratory chain is **reductive stress** — an inability to reoxidise NADH — and its lipid-chemistry consequence. That consequence, **ferroptosis**, is a specific, druggable node that no approved mitochondrial-disease drug directly targets.

## 2. What the public data actually say

**Mechanistic root — reductive stress. [FACT]** Titov et al. (2016, *Science*; PMID 27124460) expressed a water-forming NADH oxidase (LbNOX) to raise the NAD⁺/NADH ratio and *ameliorated* defects caused by an impaired ETC, explicitly "underscoring the role of reductive stress." Sullivan et al. (2015, *Cell*; PMID 26232225) showed a major function of respiration is to supply **electron acceptors** for aspartate synthesis, substitutable by α-ketobutyrate. Together these say the failing variable is electron-acceptor/NAD⁺ *regeneration*, not NAD⁺ *pool size*.

**A cross-lab transcriptomic signature (this work). [FACT]** I built a CI-deficiency signature from two independent mouse RNA-seq datasets — GSE149616 (cerebellum, CI cKO; PMID 32574562) and GSE242286 (cortex+hippocampus, Ndufs4-KO; PMID 40731203, which reports CI deficiency inducing Alzheimer's-disease-like signatures). Genome-wide log-fold-changes correlate across labs/regions (Spearman ρ = 0.29, p ≈ 10⁻²⁶⁵); of 605 genes significant in both, **466 (77%) agree in direction** (Fig. 1a). Scanning that robust signature against candidate nodes (Fig. 1b), the redox axis is the one that lights up, while NAD-salvage, HIF and aspartate-transport gene sets show **no** enrichment.

The clean, correctly-signed evidence is **down-regulation of NADPH-dependent reactive-aldehyde detox enzymes (AKR1B1, AKR1B10, AKR1E1)** — reduced capacity to clear the toxic aldehydes (e.g. 4-HNE) produced by lipid peroxidation. **[FACT]** The signature also shows down-regulation of lipid-remodelling genes including *ACSL4/ACSL6*. Because **ACSL4 is pro-ferroptotic** (it loads polyunsaturated fatty acids into membranes to sensitise ferroptosis), its *down*-regulation is best read as a **compensatory/adaptive** response that limits peroxidisable substrate — not as evidence of cells "losing" per se. **[INFERENCE]** I therefore anchor the vulnerability claim on the detox-loss signal, not on ACSL4/6.

**A genetic reversal arm — and an honest limit. [FACT]** GSE149616 uniquely includes a rescue arm expressing NDI1 (a single-subunit NADH:ubiquinone oxidoreductase that reoxidises NADH — a genetic proxy for the mechanism I propose). It rescues lifespan, but the CI-vs-NDI1-rescue contrast moved only **4 genes** in brain, and the dataset's own title states NAD⁺ regeneration "rescues lifespan but not ataxia." **[FACT]** Restoring NADH oxidation helps systemically but does not normalise the brain transcriptome — motivating a *downstream* intervention at the lipid-peroxidation step, in parallel. **[INFERENCE]**

**An unbiased screen names the node. [FACT]** To et al. (2019, *Cell*; PMID 31730859) performed genome-wide CRISPR screens under mitochondrial inhibition and found **GPX4** — the selenoenzyme that detoxifies lipid peroxides and is the master ferroptosis brake — scored as **synthetic sick/lethal**. CI-inhibited cells *depend* on GPX4 to survive. Jain et al. (2016, *Science*; PMID 26917594) independently showed the hypoxia response is protective and rescues the Ndufs4 Leigh mouse — consistent with lowering O₂-driven lipid peroxidation. **[INFERENCE]**

**A human line. [FACT]** The GSE27041 patient-fibroblast study (PMID 22033105) reports CI-deficiency transcriptional changes in the **Nrf2-Keap1 antioxidant pathway and selenoproteins** (GPX4 is a selenoprotein) — the same axis, in human patient cells.

**Convergence [INFERENCE]:** three independent public data types — my cross-lab signature (detox-capacity loss), an unbiased CRISPR dependency (GPX4), and a patient-cell antioxidant response — point to the *same* node: **lipid-peroxidation / ferroptosis vulnerability arising from reductive stress** (Fig. 3, middle).

## 3. Why edaravone, and why it is "not-thought-of-yet" here

**Mechanistic fit. [FACT/INFERENCE]** Edaravone (MCI-186) is a pyrazolone radical-trapping antioxidant that inhibits lipid peroxidation and the radical chain that drives ferroptosis; it attenuates ferroptosis and lipid peroxidation in a neuronal (HT22) model (PMID 36333599). It is also a hydroxyl-radical scavenger that protects cultured astrocytes against the complex-I poison MPP⁺ by inhibiting the mitochondrial *apoptotic* pathway (PMID 18643790) — a distinct death mode, but evidence of activity against complex-I toxicity. The anti-ferroptosis/lipid-peroxidation claim rests on PMID 36333599. **[FACT]** Acting at the lipid-peroxidation step places edaravone exactly where the three data lines converge. **[INFERENCE]**

**Drug-like, brain-penetrant, approved. [FACT]** Edaravone is an oral/IV drug approved for ALS and stroke (ChEMBL CHEMBL290916, max_phase 4, first approval 2017). Across an 8-compound panel it combines drug-like size, low lipophilicity (MW 174, TPSA 32.7 Å², HBD 0, XLogP 1.3; Fig. 2) and — unlike the research-tool ferroptosis inhibitors ferrostatin-1/liproxstatin-1 (not drugs) or the highly lipophilic comparators — **clinically established BBB penetration**. Safety is an approved-drug profile (GHS Warning/irritant only). **[FACT]**

**Novelty. [FACT]** A PubMed negative-search returns **0 papers** for edaravone with "complex I deficiency", **0** with "Ndufs4", and only 1 with "Leigh syndrome" — which on inspection concerns MELAS stroke-episode management (PMID 19780807), not primary CI disease. Edaravone is essentially **untested in primary complex-I disease**, despite a mechanism that matches the data.

**Honest differentiation and the strongest counter-argument. [FACT]** The ferroptosis *node* is not unprecedented: vatiquinone (EPI-743, α-tocotrienol quinone) targets the GPX4/15-lipoxygenase ferroptosis axis and is in mitochondrial-disease trials (PMID 30921410). Critically, a preclinical study (PMID 38883711, preprint) found that vatiquinone **robustly rescued patient cells from RSL3-induced ferroptosis but had no effect on survival in the Ndufs4 Leigh mouse in vivo** (it may have reduced seizures). This is the single strongest argument against my nomination: **a cell-assay rescue at this node has already failed to translate in the closest in-vivo model.** Edaravone is not a copy of vatiquinone — it is a broad radical-trapping antioxidant rather than a lipoxygenase-axis quinone, is far less lipophilic (XLogP 1.3 vs 7.4), and is an approved CNS drug with defined exposure — but the vatiquinone result raises the bar: edaravone must be judged in vivo, not on a cell rescue. **[FACT/INFERENCE]**

## 4. The compound (resolvable identifiers)

| Field | Value |
|---|---|
| Name | Edaravone (MCI-186, Radicava) |
| PubChem CID | 4021 |
| InChIKey | QELUYTUMUWHWMC-UHFFFAOYSA-N |
| SMILES | CC1=NN(C(=O)C1)C2=CC=CC=C2 |
| Formula / MW | C10H10N2O / 174.20 |
| ChEMBL | CHEMBL290916 (max_phase 4, 2017) |
| CAS | 89-25-8 |

Backup (different mechanism, iron chelation): **deferiprone** (CID 2972; CHEMBL70927) — carries a **black-box agranulocytosis warning**, so second-line.

## 5. First experiment (falsifiable, with a mandatory in-vivo step)

**[SPECULATION — proposed design]** Because vatiquinone passed the cell assay yet failed in vivo, a cell rescue alone is *not* an acceptable endpoint. The design must clear that bar.
1. **Cell tier (necessary, not sufficient):** in patient-derived CI-deficient fibroblasts (GTEx-validated model — NDUFS4 is highly expressed in cultured fibroblasts) and Ndufs4-KO neurons, challenge with the GPX4 inhibitor RSL3 ± edaravone dose-response; read C11-BODIPY lipid peroxidation and viability. **Prediction:** CI-deficient cells are hypersensitive to RSL3 (from To 2019); edaravone shifts the EC₅₀ more in CI-deficient than control cells. Include vatiquinone as a positive comparator so potency is benchmarked head-to-head.
2. **In-vivo tier (decisive):** dose the Ndufs4-KO Leigh mouse with edaravone (using its known CNS-exposure regimen) and measure survival, body weight/temperature, neuropathology and brain lipid-peroxidation markers — the same endpoints on which vatiquinone failed. **This is where the hypothesis lives or dies.**
3. **Mechanistic control:** confirm rescue is reversed/occluded by re-oxidising NADH (NDI1/LbNOX), tying any benefit to the reductive-stress→lipid-peroxidation axis.
4. **Kill criteria:** if edaravone does not preferentially shift the RSL3 EC₅₀ in CI-deficient cells, stop. If it passes the cell tier but does not improve in-vivo survival/neuropathology, it has failed exactly as vatiquinone did — report the negative result.

Why edaravone might succeed where vatiquinone did not is a genuine open question, not a promise: distinct radical-trapping mechanism, lower lipophilicity, and an established CNS-exposure profile are the differences the in-vivo tier is designed to test. **[SPECULATION]**

## 6. Key limitations (stated, not hidden)

- **In-vivo precedent is negative [FACT]:** the closest antioxidant at this node (vatiquinone) failed to extend survival in the Ndufs4 Leigh mouse. This is a real strike against the whole node, not just against one molecule.
- **Signature caveat [FACT]:** derived in mouse brain; bulk RNA-seq carries a cell-composition confound. Human validation rests on one fibroblast dataset (GSE27041).
- **NOT-RUN [FACT]:** the pharmacological L1000/CLUE.io connectivity-reversal line could not run — api.clue.io/clue.io are proxy-blocked and the raw L1000 matrices (~40 GB) exceed available memory. No connectivity scores were fabricated; the genetic NDI1 arm is the substitute, with its limits noted.
- **Efficacy is unproven [INFERENCE]:** edaravone's antioxidant benefit in other CNS diseases has been modest; brain lipid-peroxidation control at tolerated doses is the open question. Its own metabolism can generate reactive intermediates, and chronic paediatric dosing/formulation is undefined. **[SPECULATION]**

*Figures: `figures/fig1_signature_discovery.png` (signature + node); `figures/fig2_bbb_physchem.png` (candidate physicochemistry); `figures/fig3_evidence_chain.png` (evidence chain + counter-evidence). Full identifier list in `sources.md`; run log in `process_trace.json`.*
