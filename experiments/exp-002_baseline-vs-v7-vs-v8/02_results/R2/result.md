# Why does biological aging occur?

> ## Bottom line
>
> Life encodes a detailed program for **how to build a body**, but no target for **how to hold a finished one**. Growth is a controlled trajectory with a goal; adulthood has no encoded goal, because selection fades after reproduction and never "pays" to specify one. So the growth-control system (insulin/IGF-1 → mTOR) keeps running past maturity with no target to settle into — overshooting some tissues, under-maintaining others — and the body drifts from its youthful state at a rate set by how hard that system still runs. This one missing "adult set-point" explains both why nearly all complex life ages and why slower-developing species, and diet/drug-slowed animals, age slower.
>
> **First experiment:** in mice, shift the growth controller toward maintenance *while holding its overall activity and the damage load fixed*; if the aging clock slows anyway, the cause is the missing set-point, not the signal level.

---

## 1. The unifying principle — one sentence

**Aging occurs because the genome encodes a developmental *reference trajectory* for building a body but no stationary *adult set-point* for holding one, so after growth the shared nutrient-growth controller has no target state to regulate toward and the organism drifts along the extrapolated tail of its own growth program — at a rate set by how hard that controller keeps running.**

The causal variable is **the absence of a held reference**, not the *level* of any signal and not the *quantity* of any resource.

## 2. What the principle says

A feedback controller needs two things to hold a state: a **set-point** (the target) and an **error signal** (distance from target). Development supplies a *moving* reference — the growth trajectory from zygote to adult — and the insulin/IGF-1 → AKT → mTORC1 network executes it. In real pathway data these genes are not scattered; they form one connected insulin/IGF → AKT → mTOR/autophagy/FOXO axis (Reactome v97). At maturity the trajectory ends, but nothing defines "the adult state to be maintained indefinitely," because the force of natural selection falls after reproduction and never encodes a maintenance target (the classical evolutionary theories).

The result is a controller with a reference but **no terminal hold-state**. Two consequences follow from the *same* missing set-point:

- **Commission (over-run).** Growth-type signalling continues into adulthood — the "quasi-program" that hyperfunction theory *observes*.
- **Omission (under-repair).** The high-mTORC1 state suppresses autophagy and repair, so maintenance stays under-resourced — what disposable-soma theory *observes*.

These are not two problems; they are two faces of one absent target. That is the reframing: hyperfunction sees the commission arm, disposable soma sees the omission arm, and the set-point principle says both exist because there is no adult reference to correct toward.

## 3. Why almost all complex life ages (universality)

Universality falls out of the architecture, not from accumulated damage. Any organism that (i) grows to an adult form using a nutrient-responsive controller and (ii) has a post-reproductive selection shadow will lack an encoded adult set-point — this is structural, so it applies across complex life. The controller itself is ancient and ubiquitous:

- Its proteins are conserved metazoa-wide (UniProt: MTOR = P42345, 2549 aa; the twelve-node controller set all confirmed at the protein level), with the loss-of-function longevity phenotype traceable from *C. elegans* daf-2 (Kenyon 1993) through flies and mice.
- The network is expressed in **all 54 human tissues** above 1 TPM (GTEx v8; MTOR median 14.1 TPM, AKT1 50.2, FOXO3 29.8) — a shared, body-wide system, not a tissue quirk.

## 4. Why aging *rate* varies >100-fold and is tunable (the quantitative test)

If aging rate is set by *how hard the growth controller runs after maturity*, then species that run it more slowly — mature later, grow slower — should age more slowly, **independent of body size**. I tested this on AnAge (4,645 species; HAGR), using life-history proxies measured independently of lifespan, and correcting for the body-mass allometry. (**Figure 1**, **Figure 2**.)

- Maximum lifespan spans **100-fold across mammals** (Northern red-backed vole 2.1 yr → bowhead whale 211 yr, n=1,003) and **2,450-fold across vertebrates** (pygmy goby 0.16 yr → Greenland shark 392 yr). Body mass explains only ~50% of the mammalian variance (allometric r=0.705).
- **After removing the mass allometry**, developmental tempo still predicts lifespan: age-at-maturity **partial r = +0.65 [95% CI +0.61, +0.69], n=801, p≈10⁻⁹⁷**; growth-rate constant **partial r = −0.37 [−0.48, −0.25], n=215**.
- The **direct** aging-rate measure — mortality-rate doubling time (MRDT) — tracks age-at-maturity even harder: **partial r = +0.85 [+0.62, +0.94], n=17, p≈10⁻⁵**, surviving order-level aggregation (r=+0.53, 20 orders, p=0.017) to partly address phylogeny.
- **Naked mole-rat vs mouse** is the cleanest natural experiment (**Figure 2b**): near-matched mass (35 g vs 20 g, 1.7×) but **5.4× later maturity and 7.8× longer life**; the mole-rat lives 3.7× longer than its mass predicts, the mouse 0.5×, and mole-rat mortality does not rise with age (Ruby 2018).

**Tunability is the same variable moved by hand.** Rapamycin lowers mTORC1 and extends mouse lifespan by **+14% (F) / +9% (M)** at standard dose and **+23% (M) / +26% (F)** at 3× dose in the Interventions Testing Program. Growth-hormone-receptor knockout abolishes any *further* benefit of dietary restriction — the two act through **one pathway**, exactly as a single-controller model requires (Bonkowski & Bartke 2009). Human genetics agrees the controller's set-point governs growth: GHR → Laron syndrome / short stature (score 0.83), IGF1R → growth delay, INSR → growth-resistance, MTOR → overgrowth syndromes (Open Targets).

## 5. Ordering the hallmarks of aging (Figure 3)

The principle generates a **causal hierarchy**, not a list. Upstream sits *deregulated nutrient sensing* — the unheld reference itself. The **commission** arm generates cellular senescence, mitochondrial dysfunction, and stem-cell exhaustion; the **omission** arm (mTORC1 ⊣ autophagy) generates loss of proteostasis and *permits* genomic instability, telomere attrition, and epigenetic drift to accumulate uncorrected; altered intercellular communication / inflammaging is terminal.

**A pre-registered null keeps this honest.** I asked whether nutrient-sensing genes are more *network-central* (STRING betweenness) than the other hallmark genes. **They are not** (ratio 0.83×; 10,000× permutation p=0.45; the top hub is TP53, a senescence gene). So the controller's primacy is a claim about **intervention and developmental causation, not static network topology** — and I do not claim the latter.

## 6. What this adds to each existing theory (Figure 4)

- **Mutation accumulation** (Medawar) — supplies the shared proximate mechanism that makes aging *stereotyped*, not idiosyncratic.
- **Antagonistic pleiotropy** (Williams 1957) — names the pleiotropic locus: the controller with no adult set-point *is* the early-good/late-bad gene, mechanized.
- **Disposable soma** (Kirkwood 1977) — reframes dietary restriction from resource *amount* to reference *level*, resolving the "less food → longer life" paradox.
- **Free-radical / oxidative** (Harman 1956) — demotes ROS to a *permitted* downstream hallmark, not the driver.
- **Hyperfunction / mTOR** (Blagosklonny 2010) — adds the control variable: rate = unheld-reference error, tunable *at constant mTOR* (the discriminator below).
- **Telomere attrition** — subsumes it as one permitted clock among several, not primary or universal.
- **Information / epigenetic noise** (Yang & Sinclair 2023) — specifies the *governor* of the noise rate: the running growth reference sets how fast information degrades.

The principle also **unifies the evolutionary "why"** (mutation accumulation / antagonistic pleiotropy / disposable soma) **with the mechanistic "how"** (hyperfunction / nutrient-sensing) under one statement about control-reference structure.

## 7. Is this just hyperfunction restated? — the discriminator

No. Hyperfunction predicts aging rate ∝ **absolute** mTOR activity. The set-point principle predicts rate ∝ **reference error** — the mismatch between the running program and an absent held target. These diverge under one manipulation: **hold absolute mTOR fixed and supply a competing stationary reference / error-correction** while holding damage load fixed. Hyperfunction predicts no change; the set-point principle predicts the aging rate slows.

## 8. Falsification — the first experiment

- **System:** mouse (or *C. elegans* for throughput), tissue/time-gated.
- **Intervention:** decouple mTORC1 *level* from maintenance *allocation* — e.g. co-manipulate Rptor/Rictor balance ± an orthogonally induced constitutive autophagy/proteostasis "hold" signal — tuned so that **bulk mTORC1 activity (p-S6K, p-4E-BP1) and a damage marker (8-oxo-dG, γH2AX) are held constant** across arms while maintenance allocation shifts.
- **Readout:** rate of change of a transcriptomic/epigenetic clock (Horvath 2013; Tabula Muris Senis GSE132040 as the mouse reference), autophagic flux, and a functional frailty index.
- **Discriminating prediction:** the clock *rate* falls when a stationary reference is supplied **at constant mTOR and constant damage**.
- **Refuting result:** if clock rate and frailty are invariant to the allocation/reference shift when mTOR and damage are clamped, the principle is falsified (and hyperfunction or damage theories stand). A second refutation: if, across a larger phylogenetically-corrected species set, lifespan is *independent* of developmental tempo after mass correction, the quantitative wager fails.

## 9. Honest limitations

1. **Mammal-strong, bird-partial.** The developmental-tempo law is strong and directional in mammals and for age-at-maturity broadly, but the **growth-rate channel vanishes in birds** after mass correction (partial r = −0.04 [−0.16, +0.07], n=298, p=0.46). It is not a clean universal scaling law; the growth-rate proxy is confounded or differently structured outside mammals.
2. **Phylogenetic non-independence** is only *partly* addressed. Species are not independent data points; I mitigated with order-level aggregation (r=+0.53, 20 orders) but a formal phylogenetic generalised least-squares analysis with a dated tree is the proper next step and is not performed here.

## Figures

- **figures/fig1_developmental_rate_scaling.png** — mass-corrected developmental tempo vs aging rate (mammals, birds, and MRDT), with 95% CIs.
- **figures/fig2_allometry_residual_nmr.png** — body-mass allometry of lifespan with residual highlights, and the naked-mole-rat-vs-mouse dissociation.
- **figures/fig3_causal_dag.png** — the causal hierarchy: one unheld set-point generates some hallmarks, permits others.
- **figures/fig4_differential_table.png** — what the set-point principle adds to each of the seven existing theories.

*Evidence tags in the full text: cited facts are backed by the identifiers in `sources.md`; the cross-species correlations are my own analysis of the cited AnAge dataset. Full provenance in `citation_ledger.csv` and `process_trace.json`.*
