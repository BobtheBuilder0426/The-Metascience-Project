# Reasoning — how I got here

*A scannable trace of the line of thought. Numbers are exact; full detail in `process_trace.json`.*

## The reframing
- The paper works **forward**: differentiation dynamics → enriched pathways → hand-picked 1C cocktail.
- To be genuinely *novel*, invert the arrow: **aging state → cofactor-limited enzymes → feedable metabolites → combinatorial cocktail.**
- Anchor the inversion on a mechanism, not a pathway list: **cofactors** gate the chromatin/metabolic enzymes that maintain muscle, and cofactors have **feedable precursors**.

## What I had to be honest about
- **Naive premise ("reverse the whole transcriptome") is wrong.** Tested it: the 1C-MIM effect is *positively* correlated with the aging axis (r = +0.27 on age-significant genes), not anti-correlated.
- This is not a failure — it **matches the paper's own conclusion**: methylation-clock reversal was "minor"; the mechanism is **regenerative competence** (acetylation + cell-cycle re-entry).
- Course-correction: optimize the **enzyme layer that gates regeneration**, and score reversal **per module**, not globally.

## Evidence the pieces are real
- **Aging axis validated** — dominated by the canonical aged-muscle program: denervation/NMJ (*Chrng* +3.6, *Sln* +2.6), embryonic myosin re-expression (*Myh3* +1.3), stress (*Gadd45a, Runx1, Ampd3*). 1,813 genes at padj < 0.05.
- **1C-MIM re-analysis reproduces the paper exactly** — *Saa3, Timp1, Clu, Mt1, Mt2* down; *Lep, Gdf5* up. So my pipeline is trustworthy.
- **Module decomposition** — 1C-MIM reverses oxidative-stress/metallothionein (+0.42) and drives satellite/regeneration (+0.34); doesn't touch mito/senescence. Selective, not global.

## The ranking, and why I trust it
- Composite lever score = 0.20·(transcriptomic dysregulation) + 0.30·(metabolite age-decline) + 0.25·(feedability) + 0.25·(regeneration gate).
- Order: **NAD⁺ 0.90 > spermidine 0.81 > α-KG 0.78 > acetyl-CoA 0.70 > SAM/methylation 0.68 > FAD 0.37.**
- **Positive control passed:** from an orthogonal direction the method ranks **acetylation above methylation** — recovering the paper's experimentally-proven mechanism, and its finding that methylation is not the lever.
- Cofactor *levels* aren't visible in transcriptomes (that's why the paper ran metabolomics), so the metabolite-decline and feedability components are literature-anchored — each with a primary source (see `sources.md`).

## Why this exact cocktail
- Submodular optimizer: maximize total lever score, **penalize redundant axes** (λ = 1.2). Objective saturates at 4, elbow after 3.
- **The methionine/SAM route is never selected**, even when allowed to compete — redundant/antagonistic with α-KG demethylation (overlap 0.60) and acetyl-CoA acetylation (0.55). The method *spontaneously* walks away from 1C-MIM's defining axis.
- Output: **NR + spermidine + Ca-AKG** (core) **+ acetate** (optional 4th, reconstitutes acetylation via a non-methionine precursor).
- **Zero shared metabolites** with 1C-MIM. Nuance: their *putrescine* is the precursor of my *spermidine* (same family, precursor vs active product); NAD⁺/α-KG/acetate are wholly new.

## The pilot, and its logic
- Use the paper's **own CTX-injury regeneration assay** in **aged** mice so results are directly comparable to 1C-MIM.
- 4 arms: vehicle / CoRe / **1C-MIM benchmark** / scramble. Primary = day-7 myofiber CSA; secondary = central nuclei, Pax7⁺/Ki67⁺, motor recovery.
- **Target engagement is the differentiator:** measure muscle NAD⁺, spermidine, α-KG + histone acetylation + 5hmC. CoRe should raise these *without* flooding methylation — the fingerprint of cofactor restoration vs the paper's methyl-donor route.
- **Power:** n = 12/arm → 80% for CoRe-vs-vehicle at the paper's effect size (d ≈ 1.2). Superiority-vs-1C-MIM (d ≈ 0.8 → n ≈ 26) deferred to a follow-on. Honest about what the first experiment can and can't settle.
- **Go/no-go** ties phenotype to mechanism: advance only if regeneration improves *and* ≥ 2 of 3 cofactors engage.

## What would change the answer
- A measured metabolomic aging panel would replace the literature-anchored components and let the lever weights be *fit* rather than set.
- If the pilot shows cofactor engagement without phenotype, the enzyme-layer premise is insufficient and the method should fold in non-cofactor levers.
- Pharmacokinetic interactions between co-fed metabolites are not modeled by the axis-coverage objective — the pilot's engagement arm is the first place they'd show up.
