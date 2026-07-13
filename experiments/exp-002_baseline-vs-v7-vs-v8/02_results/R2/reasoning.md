# Reasoning trace — how the answer was reached

## Starting constraints I set myself
- One **upstream cause**, stated in a single sentence, that *generates* the hallmarks rather than adding a new one.
- Must explain **two hard facts at once**: near-universality, and >100-fold rate variation that is tunable by diet / mTOR–IIS.
- Every non-trivial claim → a **connector-verified** PMID/DOI or a named dataset; my own synthesis tagged separately.
- A **falsifiable** prediction that the nearest rival (hyperfunction) does not make.

## The central problem to avoid
- Everyone already knows the *locus* is nutrient-growth signalling (mTOR/IIS). Naming it again = "mTOR hyperfunction, restated."
- So the answer had to be a new **causal variable on that locus**, not the locus.
- Candidate variables considered:
  - signal *level* → that is hyperfunction (Blagosklonny).
  - resource *amount* → that is disposable soma (Kirkwood).
  - **control-reference structure** → the gap none of them names: a controller with a developmental reference but **no encoded adult set-point**. ← chosen.

## Why the reference-structure framing is not a relabel
- It changes the predicted **experimental outcome**: decelerate aging *at constant mTOR* by supplying a stationary reference/error-correction. Hyperfunction predicts rate ∝ absolute signal only.
- It fixes a paradox disposable soma gets backwards: dietary restriction = *less* resource but *more* life → makes sense only if DR **lowers the reference**, not if it adds maintenance resource.
- It unifies the evolutionary "why" (selection shadow → no set-point encoded) with the mechanistic "how" (controller keeps running) in one statement.

## Prior-art audit (did someone already say this?)
- Checked "set-point / control-theory / quasi-programmed / developmental theory of aging."
- Found genuine antecedents — Blagosklonny quasi-program; de Magalhães programmatic-development; Kirkwood 2008 control-theory (damage-centric); developmental-drift/Wnt.
- Conclusion: the framing is **adjacent, not identical**; none casts aging as *set-point absence in a feedback controller*. So I claim an **increment**, cite the antecedents, and do not over-claim novelty.

## Evidence I went and got (not from memory)
- **Anchor papers + theory attributions** confirmed by matching returned title/year/journal (hallmarks, hyperfunction, epigenetic-information, rapamycin, clocks, disposable soma, free-radical, naked mole-rat).
- **Controller network**: confirmed 12 protein accessions (UniProt), one connected insulin/IGF→AKT→mTOR/autophagy/FOXO axis (Reactome), expressed in all 54 human tissues (GTEx).
- **Human genetics** (Open Targets): the controller's top disease associations are **growth/body-size phenotypes** (Laron, growth delay, overgrowth) — direct evidence the set-point governs growth.
- **Geroprotectors** (ChEMBL): rapamycin/metformin sit on the growth controller; senolytics sit on a *different* target class → informs the falsification contrast.
- **Aging omics** located for the experiment readout (Tabula Muris Senis GSE132040; 215 human aging series).

## The quantitative wager (the risky, discriminating prediction)
- Prediction rivals don't make: aging rate scales with a **growth-controller set-point proxy** (developmental tempo), *independent of body mass*.
- Used proxies measured **independently of lifespan** to avoid circularity: age-at-maturity, growth-rate constant.
- Data: AnAge, 4,645 species; quality-filtered; log-log **partial correlation** controlling body mass; Fisher-z CIs.
- Results:
  - Mammal age-at-maturity vs lifespan: **partial r +0.65 [+0.61,+0.69], n=801**.
  - Mammal growth-rate vs lifespan: **partial r −0.37 [−0.48,−0.25], n=215**.
  - Direct aging-rate (MRDT) vs age-at-maturity: **partial r +0.85 [+0.62,+0.94], n=17**.
  - Order-level aggregation: r +0.53, 20 orders → partial phylogeny check.
- Natural experiment: naked mole-rat vs mouse — 1.7× mass but 5.4× maturity, 7.8× lifespan.
- Tunability numbers verified: rapamycin +14%/+9% (std), +23%/+26% (3× dose); GHR-KO abolishes DR's extra benefit (one pathway).

## Where I made myself report against the hypothesis
- **Bird growth-rate signal vanishes** after mass correction (r −0.04 [−0.16,+0.07], n=298, p=0.46). Kept as a stated limitation, not hidden.
- **STRING centrality null**: pre-registered betweenness + 10,000× permutation → nutrient-sensing nodes are **not** more central (p=0.45; TP53 is the top hub). So I **dropped** any "topologically upstream" claim; controller primacy rests on intervention/genetics/comparative data instead.
- **Dietary-restriction magnitude**: found it is genotype-dependent and can even shorten life → removed the memorized "~40–50%," kept DR qualitative.

## Corrections made during verification
- daf-2 attribution fixed to **Kenyon 1993, Nature, PMID 8247153**.
- Williams 1957 and Medawar 1952 are pre-MEDLINE → verified via **Crossref**; Williams DOI 10.1111/j.1558-5646.1957.tb02911.x; Medawar original (1952 lecture) has no native DOI → flagged, reprint DOI given.
- A metadata **parser bug** (reading identifier under the wrong key) briefly made a re-check look empty; the underlying data were correct; fixed the reader, re-verified all 19 PMIDs.
- Figure 1 recomputed with strict complete-case partial correlation so the plotted r matches the ledger exactly (+0.85, not +0.83).

## How the principle orders the hallmarks
- Root: unheld adult set-point → controller runs past maturity.
- **Commission** arm (over-run): senescence, mitochondrial dysfunction, stem-cell exhaustion.
- **Omission** arm (mTORC1 ⊣ autophagy): loss of proteostasis; *permits* genomic instability, telomere attrition, epigenetic drift.
- Terminal: altered intercellular communication / inflammaging.
- This makes the hypothesis an **ordering principle**, not a 13th hallmark.

## What would refute the whole thing
- Clock rate invariant to a reference/allocation shift at **fixed mTOR and fixed damage** → principle falsified.
- Lifespan independent of developmental tempo after mass + phylogeny correction on a larger tree → quantitative wager fails.
