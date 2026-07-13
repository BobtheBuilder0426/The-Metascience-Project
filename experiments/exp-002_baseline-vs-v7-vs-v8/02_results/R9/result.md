# A causal, aging-anchored method nominates an L-Carnitine + L-Ergothioneine cocktail for aged-muscle rejuvenation

> ## Bottom line
> Instead of asking *which metabolites recur as cells differentiate in a dish* (the source paper's forward, correlative RPC screen), we ask the **backward, causal** question: *which circulating metabolites does human genetics say protect aging muscle, which does aging deplete, and which pair converges on one repairable bottleneck in aged satellite cells?* Triangulating human muscle GWAS at metabolite-handling loci, metabolite-QTL colocalization, aging-depletion literature, and satellite-cell mechanism, the top-ranked, non-1C cocktail is **L-carnitine + L-ergothioneine** — the substrates of two adjacent 5q31 transporters (OCTN2/*SLC22A5*, OCTN1/*SLC22A4*) whose muscle-raising alleles reach genome-wide significance. Predicted synergy acts on the **mitochondrial fatty-acid-oxidation (FAO) bottleneck** in aged satellite cells: carnitine restores FAO flux (acetyl-CoA → Pax7 acetylation), ergothioneine protects the mitochondria carrying that flux. First pilot: a 2×2 factorial in aged mice with Bliss/HSA synergy decomposition, scramble control, and a head-to-head 1C-MIM benchmark.

## The method — CAMT (Causal, Aging-anchored Muscle-metabolite Triangulation)

The source paper (Hernandez-Benitez et al., *Cell Reports Medicine* 2024, DOI 10.1016/j.xcrm.2024.101449) discovered **1C-MIM** — methionine, threonine, glycine, putrescine, cysteine, SAM — by time-resolving *in-vitro* cell-fate transitions (myoblast→myofiber, NSC→astrocyte, MSC→chondrocyte), running untargeted metabolomics, and using a custom **Recurrent Pattern Classification (RPC)** to isolate transiently-spiking metabolites, then intersecting pathways to a one-carbon/polyamine signature. That pipeline is **forward** (start from a cell transition, see what moves) and **correlative** (a metabolite that rises during differentiation is a marker, not a proven cause of repair). Its own stated limitations: a metabolomic snapshot, cell lines rather than aged *in-vivo* muscle, and no human anchor.

CAMT inverts every one of those choices (Figure 1, `figures/fig1_pipeline.png`):

1. **Anchor on human aged-muscle phenotypes, not a dish.** We start from GWAS Catalog traits that *define* the endpoint we care about: hand-grip strength (EFO_0006941), appendicular lean mass (EFO_0004980), lean body mass (EFO_0004995), sarcopenia (EFO_1000653).
2. **Causal triangulation at metabolite-handling loci.** For each candidate metabolite we ask whether its **handling gene** (biosynthesis / transporter / catabolism) carries a genome-wide muscle-phenotype association with a **consistent effect direction**, then whether the same locus is the metabolite's own **QTL** (colocalization). A muscle association *at the gene that sets a metabolite's tissue level*, coinciding with that metabolite's mQTL, is a locus-level causal statement — the opposite epistemic direction from "it spiked in a dish."
3. **Aging-depletion + satellite-cell mechanism filter.** Advance only metabolites that are (a) causally protective, (b) documented to decline with age, and (c) mechanistically wired to satellite-cell (MuSC) function via muscle expression of their transporters/enzymes.
4. **Orthogonality guard.** Exclude the six 1C-MIM members and *any* candidate whose mechanism reduces to a histone-acetylation/methylation methyl-donor (1C-MIM's axis), so a win is a new mechanism, not a relabeling.
5. **Transparent composite score → ranked shortlist → cocktail** with a falsifiable synergy hypothesis.

Why this is quantitative, not correlational: each advancement gate is a retrieved number (a GWAS p-value with signed β; a median TPM; a lifespan/velocity effect size), and the orthogonality guard is a hard exclusion rule applied before scoring.

## The ranked shortlist (actual data-driven output)

Running the pipeline over an endogenous, orally-dosable, non-1C candidate universe produced this ranking (Figure 2, `figures/fig2_evidence.png`; full table in `figures/scoring_table.csv`):

| Rank | Metabolite | Handling gene | Best muscle-GWAS p (dir.) | Composite |
|------|------------|---------------|---------------------------|-----------|
| 1 | **L-Carnitine** | *SLC22A5*/OCTN2 | 3×10⁻²¹ (＋) | 14 |
| 2 | **L-Ergothioneine** | *SLC22A4*/OCTN1 | 2×10⁻²¹ (＋) | 12 |
| 3 | BCAA (Leu/Ile/Val) | *BCKDHB* | 2×10⁻⁴³ (**mixed**) | 8 |
| — | Spermidine | *SRM* | 2×10⁻¹² | excluded (1C polyamine arm) |
| — | Glutathione | *GSS* | 6×10⁻⁴⁵ | excluded (Cys/Gly, 1C-adjacent) |

Two honesty checks the method passed:
- **It rejects the "obvious" longevity metabolites.** NAD⁺ (*NAMPT*), creatine (*GATM/CKM*), taurine (*SLC6A6*), β-hydroxybutyrate (*BDH1/OXCT1*), α-ketoglutarate (*OGDH*), and lactate (*SLC16A1*) have **zero** muscle-phenotype associations at their handling loci at full catalog depth — they did not enter the cocktail despite their popularity.
- **It demotes the strongest raw hits when they fail a gate.** *GSS* and *BCKDHB* have larger −log₁₀p than the winners, but glutathione is Cys/Gly-based (orthogonality-excluded) and *BCKDHB*'s muscle alleles point in **inconsistent directions**, so BCAA is reported but kept out of the cocktail.

## The cocktail and its synergy hypothesis

**L-Carnitine + L-Ergothioneine.** They are the substrates of two *distinct but adjacent* 5q31 transporters, both muscle-expressed, both with positive-signed muscle-GWAS alleles.

- **L-Carnitine (OCTN2/*SLC22A5*, 50 TPM in muscle)** is the obligate carrier that loads fatty acids into mitochondria. The keystone mechanism paper (*EMBO J* 2025, PMID 40065099) shows **mitochondrial FAO is required for satellite-cell function**: deleting *Cpt2* (the FAO rate-limiting step carnitine feeds) drops acetyl-CoA, reduces **Pax7 acetylation**, and delays regeneration — and acetate rescues it. Aging depletes muscle carnitine and blunts FAO.
- **L-Ergothioneine (OCTN1/*SLC22A4*)** is a diet-derived mitochondrial-protective antioxidant that concentrates in oxidative (soleus) muscle via OCTN1 (PMID 40543223) and whose oral supplementation extends lifespan and preserves movement velocity in aged **male** mice (PMID 38446314; sex-specific — a caveat carried into the pilot's both-sexes design). Its plasma level falls with age.

**Synergy of mechanism (not of dose):** aged satellite cells fail to re-enter the cycle partly because their FAO machinery is both *under-fueled* (low carnitine) and *oxidatively damaged* (low ergothioneine). Carnitine restores the **flux** through the FAO→acetyl-CoA→Pax7-acetylation axis; ergothioneine protects the **mitochondria** that must sustain that flux under the ROS load of activation. Neither alone fully rescues the bottleneck; together they should super-additively restore aged-MuSC-driven regeneration. Notably, this axis reaches the *same downstream node the source paper found (protein acetylation)* but through **metabolic flux**, not methyl/acetyl-donor supplementation — satisfying the orthogonality guard.

**Honest caveats (retrieved, not hidden):** the **free-carnitine** mQTL did **not** close — the L-carnitine trait (EFO_0021612) is under-powered (maps only *SLC22A16*), so carnitine's causal weight rests on OCTN2 substrate identity + the FAO mechanism + RCTs, not a formal colocalization. (What the OCTN2 muscle SNP *does* colocalize with, same effect allele, is several **acyl**carnitine levels — palmitoyl-/acetyl-/hexanoyl-carnitine — i.e. a carnitine-transport QTL.) OCTN1 muscle expression is low (3.5 TPM, highest in blood) — ergothioneine's muscle effect may be indirect/systemic; both 5q31 loci are pleiotropic (platelet/immune traits), so the muscle association is real and positive but not muscle-exclusive; lifelong genetic level ≠ acute supplementation, which is exactly why a pilot, not the genetics, is the test.

## First pilot experiment

**Model:** aged (22–24 mo) C57BL/6, both sexes; acute tibialis-anterior injury (BaCl₂ or cardiotoxin); metabolites delivered in drinking water (both are oral; levocarnitine is an FDA-approved oral drug, CHEMBL1149, and ergothioneine is a GRAS micronutrient with a completed human oral RCT, NCT06846827).

**Arms (2×2 factorial + controls; Figure 3a, `figures/fig3_pilot.png`):** vehicle · L-carnitine (A) · L-ergothioneine (B) · A+B — enabling **Bliss/HSA synergy decomposition**; plus a **scramble** control (specificity), a head-to-head **1C-MIM** arm (the paper's mix), and a young-injured ceiling.

**Readouts:** *primary* — ex-vivo tetanic force and myofiber cross-sectional-area recovery at a fixed post-injury day; *secondary* — Pax7⁺/MyoD⁺ counts, EdU incorporation, single-fiber/transplant MuSC-intrinsic FAO flux, grip/treadmill, and intake/palatability/weight.

**Sample size (Figure 3b):** powered to the demanding synergy contrast (A+B vs best single); simulation at CV=25%, α=0.05 gives ~80% power at n≈12–15/arm/sex for a 30% Bliss excess (the efficacy contrast A+B-vs-vehicle is over-powered at that n).

**Pre-registered go/no-go:**
- *Synergy* — A+B exceeds the best single arm with a Bliss/HSA excess whose CI excludes 0 (**else synergy falsified**).
- *Efficacy* — ≥1 active arm beats vehicle on the primary (**else the nomination is falsified**).
- *Specificity* — scramble ≈ vehicle.
- *Win condition* — **A+B ≥ 1C-MIM** on the primary endpoint.

*Full identifiers are in `sources.md`; the query log is in `process_trace.json`.*
