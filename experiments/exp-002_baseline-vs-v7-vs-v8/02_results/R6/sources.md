# Sources

**Verification.** Every PMID below was confirmed to exist and to match the claim it supports via PubMed `get_article_metadata`, which returns each record's own PMID, DOI, and title together — titles checked for all cited PMIDs, abstracts read for the scope-critical ITP, plateau, reprogramming, and resilience claims. DOI-only classic works (Williams 1957, Gladyshev 2013, Yang 2023 and its 2024 erratum) were confirmed via OpenAlex `openalex_get_work`. PMIDs are confirmed through PubMed rather than OpenAlex, since OpenAlex returns DOIs, not PMIDs. Sources are grouped by the constraint each primarily supports; several support more than one.

## C1 — Evolutionary theory

- Hamilton WD 1966, J Theor Biol — moulding of senescence by natural selection  
  PMID 6015424 · DOI 10.1016/0022-5193(66)90184-6 — confirmed via PubMed metadata (title + abstract)
- Williams GC 1957, Evolution — pleiotropy & senescence  
  DOI 10.1111/j.1558-5646.1957.tb02911.x — confirmed via OpenAlex (DOI)
- Kirkwood TBL 1977, Nature — disposable soma / evolution of ageing  
  PMID 593350 · DOI 10.1038/270301a0 — confirmed via PubMed metadata (title + abstract)
- Medawar PB 1952, An Unsolved Problem of Biology (Lewis, London)  
  (no PMID/DOI) — monograph — no PMID/DOI (identity by title)

## C2 — Mortality kinetics

- Carey JR et al 1992, Science — slowing of mortality at older ages (medfly)  
  PMID 1411540 · DOI 10.1126/science.1411540 — confirmed via PubMed metadata (title + abstract)
- Curtsinger JW et al 1992, Science — Drosophila mortality plateau  
  PMID 1411541 · DOI 10.1126/science.1411541 — confirmed via PubMed metadata (title + abstract)
- Barbi E et al 2018, Science — human mortality plateau  
  PMID 29954979 · DOI 10.1126/science.aat3119 — confirmed via PubMed metadata (title + abstract)
- Comment on Barbi 2018  
  PMID 30262471 · DOI 10.1126/science.aav1200 — confirmed via PubMed metadata (title + abstract)
- Response to comment on Barbi 2018  
  PMID 30337380 · DOI 10.1126/science.aav3229 — confirmed via PubMed metadata (title + abstract)
- Gavrilov & Gavrilova 2001, J Theor Biol — reliability theory of aging  
  PMID 11742523 · DOI 10.1006/jtbi.2001.2430 — confirmed via PubMed metadata (title + abstract)

## C3 — Cross-species variation

- Ruby JG et al 2018, eLife — naked mole-rat mortality defies Gompertz  
  PMID 29364116 · DOI 10.7554/eLife.31157 — confirmed via PubMed metadata (title + abstract)
- Comment on Ruby 2018  
  PMID 31287058 · DOI 10.7554/eLife.45415 — confirmed via PubMed metadata (title + abstract)
- 2024 follow-up — NMR mortality with doubled data; conclusion holds  
  PMID 38773057 · DOI 10.1007/s11357-024-01201-4 — confirmed via PubMed metadata (title + abstract)
- Jones OR et al 2014, Nature — diversity of ageing across the tree of life  
  PMID 24317695 · DOI 10.1038/nature12789 — confirmed via PubMed metadata (title + abstract)
- Abegglen LM et al 2015, JAMA — elephant TP53 & Peto's paradox  
  PMID 26447779 · DOI 10.1001/jama.2015.13134 — confirmed via PubMed metadata (title + abstract)

## C4 — Conserved hallmarks

- López-Otín C et al 2013, Cell — hallmarks of aging  
  PMID 23746838 · DOI 10.1016/j.cell.2013.05.039 — confirmed via PubMed metadata (title + abstract)
- López-Otín C et al 2023, Cell — hallmarks of aging: an expanding universe  
  PMID 36599349 · DOI 10.1016/j.cell.2022.11.001 — confirmed via PubMed metadata (title + abstract)
- Kennedy BK et al 2014, Cell — geroscience: linking aging to chronic disease  
  PMID 25417146 · DOI 10.1016/j.cell.2014.10.039 — confirmed via PubMed metadata (title + abstract)

## C5 — Interventions (incl. NIA ITP)

- McCay CM et al 1935 (J Nutr; PMID 2520283 = 1989 reprint) — caloric restriction extends life  
  PMID 2520283 — confirmed via PubMed metadata (title + abstract)
- Kenyon C et al 1993, Nature — daf-2 mutants live twice as long  
  PMID 8247153 · DOI 10.1038/366461a0 — confirmed via PubMed metadata (title + abstract)
- Harrison DE et al 2009, Nature — rapamycin extends lifespan (ITP)  
  PMID 19587680 · DOI 10.1038/nature08221 — confirmed via PubMed metadata (title + abstract)
- Strong R et al 2008, Aging Cell — NDGA & aspirin extend male lifespan (ITP)  
  PMID 18631321 · DOI 10.1111/j.1474-9726.2008.00414.x — confirmed via PubMed metadata (title + abstract)
- Harrison DE et al 2014, Aging Cell — acarbose/17aE2/NDGA/methylene blue (ITP)  
  PMID 24245565 · DOI 10.1111/acel.12170 — confirmed via PubMed metadata (title + abstract)
- Strong R et al 2016, Aging Cell — 17aE2/NDGA/Protandim; metformin-alone null; metformin+rapa (ITP)  
  PMID 27312235 · DOI 10.1111/acel.12496 — confirmed via PubMed metadata (title + abstract)
- Strong R et al 2013 (J Gerontol; publ. 2012) — resveratrol, GTE, curcumin, oxaloacetate, MCT null (ITP)  
  PMID 22451473 · DOI 10.1093/gerona/gls070 — confirmed via PubMed metadata (title + abstract)
- Miller RA et al 2020, JCI Insight — canagliflozin extends male lifespan (ITP)  
  PMID 32990681 · DOI 10.1172/jci.insight.140019 — confirmed via PubMed metadata (title + abstract)
- Miller RA et al 2019, Aging Cell — glycine extends lifespan (ITP)  
  PMID 30916479 · DOI 10.1111/acel.12953 — confirmed via PubMed metadata (title + abstract)
- Miller RA et al 2007, Aging Cell — ITP study design  
  PMID 17578509 · DOI 10.1111/j.1474-9726.2007.00311.x — confirmed via PubMed metadata (title + abstract)
- Baker DJ et al 2011, Nature — clearing p16 senescent cells delays aging  
  PMID 22048312 · DOI 10.1038/nature10600 — confirmed via PubMed metadata (title + abstract)
- Baker DJ et al 2016, Nature — naturally-occurring p16 clearance extends lifespan  
  PMID 26840489 · DOI 10.1038/nature16932 — confirmed via PubMed metadata (title + abstract)
- Conboy IM et al 2005, Nature — heterochronic parabiosis rejuvenates  
  PMID 15716955 · DOI 10.1038/nature03260 — confirmed via PubMed metadata (title + abstract)

## C6 — Reset / rejuvenation

- Horvath S 2013, Genome Biol — DNA methylation age clock  
  PMID 24138928 · DOI 10.1186/gb-2013-14-10-r115 — confirmed via PubMed metadata (title + abstract)
- Lu Y et al 2020, Nature — reprogramming restores youthful vision  
  PMID 33268865 · DOI 10.1038/s41586-020-2975-4 — confirmed via PubMed metadata (title + abstract)
- Gill D et al 2022, eLife — transient reprogramming (maturation phase) rejuvenates  
  PMID 35390271 · DOI 10.7554/eLife.71624 — confirmed via PubMed metadata (title + abstract)
- Kerepesi C et al 2021, Sci Adv — embryonic ground-zero / rejuvenation event  
  PMID 34172448 · DOI 10.1126/sciadv.abg6082 — confirmed via PubMed metadata (title + abstract)
- Ocampo A et al 2016, Cell — partial reprogramming ameliorates aging  
  PMID 27984723 · DOI 10.1016/j.cell.2016.11.052 — confirmed via PubMed metadata (title + abstract)

## C7 — Program vs damage placement

- Blagosklonny MV 2006, Cell Cycle — hyperfunction/quasi-program (TOR)  
  PMID 17012837 · DOI 10.4161/cc.5.18.3288 — confirmed via PubMed metadata (title + abstract)
- Harman D 1956, J Gerontol — free radical theory of aging  
  PMID 13332224 · DOI 10.1093/geronj/11.3.298 — confirmed via PubMed metadata (title + abstract)
- Yang JH et al 2023, Cell — loss of epigenetic information drives aging  
  PMID 36638792 · DOI 10.1016/j.cell.2022.12.027 — original article; PMID + DOI + title confirmed via PubMed and OpenAlex (623 citations, type "article")
- Yang JH et al 2024, Cell — author correction to Yang 2023  
  PMID 38428398 · DOI 10.1016/j.cell.2024.01.049 — erratum record; typed "erratum" via OpenAlex
- Gladyshev VN 2013, Trends Genet — origin of aging / imperfectness-driven damage  
  DOI 10.1016/j.tig.2013.05.004 — confirmed via OpenAlex (DOI)
- Gems D & Partridge L 2013, Annu Rev Physiol — genetics of longevity / program vs damage  
  PMID 23190075 · DOI 10.1146/annurev-physiol-030212-183712 — confirmed via PubMed metadata (title + abstract)

## Novelty positioning — resilience / recovery-rate prior art & rivals

- Pyrkov TV et al 2021, Nat Commun — progressive loss of resilience predicts lifespan  
  PMID 34035236 · DOI 10.1038/s41467-021-23014-1 — confirmed via PubMed metadata (title + abstract)
- Cohen AA et al 2018, J Gerontol — physiological dysregulation as robustness/resilience measure  
  PMID 29939206 · DOI 10.1093/gerona/gly136 — confirmed via PubMed metadata (title + abstract)
- Bhatt S / Cohen AA et al 2019, Aging Cell — conserved dysregulation signatures across primates  
  PMID 30746836 · DOI 10.1111/acel.12925 — confirmed via PubMed metadata (title + abstract)
- Olde Rikkert MGM et al 2016, Crit Care Med — slowing recovery as generic risk marker (critical slowing down)  
  PMID 26765499 · DOI 10.1097/CCM.0000000000001564 — confirmed via PubMed metadata (title + abstract)
- Cagan A et al 2022, Nature — somatic mutation rates scale with lifespan  
  PMID 35418684 · DOI 10.1038/s41586-022-04618-z — confirmed via PubMed metadata (title + abstract)
- Cohen AA group 2023, Sci Rep — "mallostatic" natural variables erode homeostasis (multivariate mean-reverting set-point model; closest formal precedent to set-point drift)  
  PMID 38092834 · DOI 10.1038/s41598-023-49129-7 — confirmed via PubMed metadata (title + abstract)
- Dilman VM 1971, — transformation of the developmental program / neuroendocrine "elevation" model (developmental program continues post-maturity via hypothalamic set-point loss; historical predecessor)  
  PMID 381162 — confirmed via PubMed metadata (title + abstract) (pre-DOI era, no DOI)
- Lagasse E & Levin M 2024, Ageing Res Rev — aging as loss of morphostatic information (developmental-bioelectricity set-point framing)  
  PMID 38636560 · DOI 10.1016/j.arr.2024.102310 — confirmed via PubMed metadata (title + abstract)

*Note: "cybernetic theory of aging" was searched but has no clean primary PubMed anchor (hits were unrelated reinforcement-learning/stroke papers); it is therefore mentioned in the text as an unanchored term, not cited.*
