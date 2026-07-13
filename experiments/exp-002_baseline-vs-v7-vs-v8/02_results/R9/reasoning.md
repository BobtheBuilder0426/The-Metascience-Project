# Reasoning trace — how CAMT reached L-carnitine + L-ergothioneine

## Why a new method was needed (what RPC can and can't do)
- The source paper's RPC is **forward + correlative**: it finds metabolites that *move during an in-vitro transition*. A mover is a marker; it is not shown to *cause* repair, and it is not anchored to *aging* or to *human* muscle.
- Re-running RPC on a new cell type would inherit all three limits → not novel. To beat it, the method must change the **question direction** (causal, not correlational) and the **anchor** (human aging phenotype, not a dish).

## The inversion (CAMT)
- Start from **human aged-muscle phenotypes** (grip, lean mass, sarcopenia) and ask which metabolites' **handling genes** carry directionally-consistent muscle-GWAS signal → a locus-level causal claim.
- Require **≥1 independent corroborating line** (mQTL colocalization, aging-depletion literature, MuSC mechanism) before a metabolite advances.
- Apply an **orthogonality guard** *before* scoring: exclude the six 1C-MIM members and any acetyl/methyl-donor-only mechanism, so the answer cannot be a relabeling of 1C-MIM.

## What the connector queries actually returned
- **EFO resolution (GWAS Catalog):** grip=EFO_0006941, ALM=EFO_0004980, LBM=EFO_0004995, sarcopenia=EFO_1000653. "muscle mass"/"fat-free mass" returned **no** EFO term → used the four above.
- **997 mapped genes** across the muscle traits; **255** supported by ≥2 traits. I did **not** pre-pick metabolites — I intersected the muscle-GWAS gene set with the handling genes of a broad endogenous-metabolite universe.
- **Positive intersections (locus-level causal support):**
  - *SLC22A5*/OCTN2 (carnitine transporter) — best muscle p=3×10⁻²¹ (LBM), 2×10⁻¹⁶ (grip); **positive β** (rs2631367-G, rs2631360-G, rs11242109-T).
  - *SLC22A4*/OCTN1 (ergothioneine transporter) — muscle p=2×10⁻²¹ (LBM, rs11242109-T, positive β).
  - *BCKDHB* (BCAA) — p=2×10⁻⁴³ but **direction mixed** across SNPs.
  - *GSS* (glutathione) p=6×10⁻⁴⁵; *SRM* (spermidine) p=2×10⁻¹².
- **Full-depth re-test of the "nulls" (guard against truncation):** at gene-level query depth (not truncated), NAMPT, NMRK2, SLC6A6, CSAD, CKM, GATM, GAMT, BDH1, OXCT1, OGDH, SLC16A1, AMD1 returned **0 muscle-trait rows** → the popular longevity metabolites are genuinely unsupported here, not just below a cut.

## How the shortlist collapsed to a cocktail
- **Excluded by orthogonality guard:** glutathione (built from cysteine+glycine — 1C-adjacent) and spermidine (putrescine→spermidine *is* 1C-MIM's polyamine arm). Both excluded *despite* strong/likely signal — the guard is doing real work.
- **Demoted for evidence quality:** BCAA — its *BCKDHB* muscle alleles point in inconsistent directions (β both + and − across rs6931421/rs9350850/rs2322633), so causal direction is unclear; reported but not put in the cocktail.
- **Winners:** carnitine (14) and ergothioneine (12) — top of the transparent composite; both non-1C; both feasible.

## Closing the causal triangle
- **Substrate identity (UniProt):** SLC22A5 = O76082 = high-affinity **carnitine** transporter OCTN2; SLC22A4 = Q9H015 = **ergothioneine** transporter OCTN1. So the muscle loci sit on the genes that set these two metabolites' tissue levels.
- **mQTL colocalization:** the ergothioneine measurement trait (EFO_0021163) maps to **SLC22A4** — same gene as the muscle locus → metabolite-level, not just gene-level, causal support.
- **Carnitine mQTL — kept honest:** the *free*-L-carnitine trait (EFO_0021612) is under-powered (maps only *SLC22A16*), so a formal free-carnitine colocalization **did not close**. However, the OCTN2 muscle lead SNPs are genome-wide mQTLs for the *transported cargo*: rs2631367-**G** raises palmitoylcarnitine (p=4×10⁻¹⁶), acetylcarnitine (8×10⁻¹⁴) and hexanoylcarnitine (2×10⁻¹²); rs11242109-**T** raises cerotoylcarnitine (5×10⁻¹⁹) — **same effect alleles as the muscle associations**. So carnitine's causal support is: OCTN2 substrate identity (UniProt) + a carnitine-*transport* QTL at the muscle locus + FAO mechanism + RCTs — but *not* a free-carnitine colocalization, which I do not claim.
- **Variant pleiotropy (honest):** rs11242109 / rs2631367 also associate with platelet/leukocyte/monocyte traits (5q31 immune region). The muscle association is real and positive-signed but the locus is not muscle-exclusive — a reason to triangulate, and a caveat carried into the pilot.

## Why these two work together (mechanistic synergy)
- **Same bottleneck, two failures:** aged satellite cells have FAO that is under-fueled (low carnitine) *and* oxidatively damaged (low ergothioneine).
- **Carnitine = flux:** obligate FAO cofactor; FAO→acetyl-CoA→**Pax7 acetylation** is required for MuSC function; *Cpt2*-KO delays regeneration and acetate rescues (PMID 40065099). Muscle is carnitine-dependent — CPT1B (100 TPM), CRAT (120), CACT/SLC25A20 (49), OCTN2 (50) all abundant (GTEx v8).
- **Ergothioneine = protection:** concentrates via OCTN1 in oxidative soleus (PMID 40543223); lifespan/velocity benefit in aged mice at 4–5 mg/kg/d oral (PMID 38446314).
- **Orthogonality satisfied:** the axis lands on protein acetylation (like the paper) but arrives via **metabolic flux + mitochondrial protection**, not methyl/acetyl-donor supplementation.

## Pilot logic
- **2×2 factorial** is the minimum design that decomposes synergy (Bliss/HSA) rather than just testing the combo.
- **Scramble** isolates specificity; **1C-MIM head-to-head** makes the benchmark explicit and sets the win condition (A+B ≥ 1C-MIM).
- **Power** is set by the *synergy* contrast (harder than efficacy): simulation → n≈12–15/arm/sex for ~80% power at a 30% Bliss excess (CV=25%).
- **Falsification is pre-registered** on all three axes (synergy / efficacy / specificity) so a null is interpretable, not salvageable.

## What would change the answer
- If OCTN1 muscle action proves purely systemic, ergothioneine could be swapped for a second FAO-axis metabolite (e.g. an acyl-carnitine or a mitochondrial-quality metabolite) while keeping carnitine as the anchor.
- If the L-carnitine mQTL were properly powered and did *not* colocalize with OCTN2, carnitine's causal weight would drop from "triangulated" to "mechanism + RCT."
- A stronger, single-direction MR instrument for either metabolite would upgrade the causal grade from locus-level to formal Mendelian-randomization.
