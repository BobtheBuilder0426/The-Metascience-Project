# Sources

These sources fall into the theory families the Reference-Decay hypothesis
unifies, plus the empirical results the generative model was checked against.

**Provenance of identifiers (July 2026).** The correctness of every identifier
below rests on one thing only: a **programmatic confirmation pass against the
Crossref API — 14/14 DOIs resolved**, matching title, journal, and year, with
the raw API responses saved as `doi_verification.json` in this folder. That pass
is fully reproducible and is the sole basis on which these citations should be
trusted. It also *corrected* reference #3, whose DOI had been recorded
incorrectly in an earlier draft; the value below (10.1016/j.cell.2024.01.013) is
the one present and confirmed in `doi_verification.json`.

The papers were originally located during a web-search survey of the aging
literature (queries listed under "Search provenance" below). I am **not** citing
those searches as evidence of identifier correctness — that evidence is the
Crossref file. PMIDs are as transcribed from PubMed during the survey and were
not independently re-resolved; treat the DOIs (Crossref-confirmed) as the
authoritative identifiers. Where a reference represents a *family* of work, one
representative primary source is cited.

## Foundational theory landscape (what is unified)

1. **López-Otín C, Blasco MA, Partridge L, Serrano M, Kroemer G.** Hallmarks of
   aging: an expanding universe. *Cell* 186(2):243–278 (2023).
   DOI: 10.1016/j.cell.2022.11.001 · PMID: 36599349.
   — The symptom catalogue (now 12 hallmarks) that a cause-level theory must sit beneath.

2. **Yang JH, Hayano M, … Sinclair DA.** Loss of epigenetic information as a
   cause of mammalian aging. *Cell* 186(2):305–326 (2023).
   DOI: 10.1016/j.cell.2022.12.027 · PMID: 36638792.
   — Information theory of aging + the ICE mouse (inducible changes to the epigenome).

3. **(Matters Arising):** The information theory of aging has not been tested.
   *Cell* 187(5) (2024). DOI: 10.1016/j.cell.2024.01.013 (verified on Crossref;
   supersedes an incorrect DOI recorded in the first draft).
   — Included to represent the live debate over the information theory; Reference-Decay
     specifies *what* information (set-point calibration) and gives a falsifier.

4. **Blagosklonny MV.** Aging and immortality: quasi-programmed senescence and
   its pharmacologic inhibition. *Cell Cycle* 5(18):2087–2102 (2006).
   DOI: 10.4161/cc.5.18.3288 · PMID: 17012837.
   — Hyperfunction / quasi-program theory (source of the directional-drift term).

5. **Gems D & de Magalhães JP.** The hoverfly and the wasp / hyperfunction theory
   reviews. Representative: *The hyperfunction theory: an emerging paradigm for
   the biology of aging.* Ageing Res Rev (2021). PMC7612201.

6. **Kirkwood TBL.** Evolution of ageing (disposable soma theory). *Nature*
   270:301–304 (1977). DOI: 10.1038/270301a0.
   — Somatic-maintenance trade-off; Reference-Decay reframes as "no external reference."

7. **Gladyshev VN.** Aging: progressive decline in fitness due to the rising
   deleteriome adjusted by genetic, environmental, and stochastic processes.
   *Aging Cell* 15(4):594–602 (2016). DOI: 10.1111/acel.12480 · PMID: 27060562.
   — The deleteriome (cumulative deleterious change).

8. **Nelson P & Masel J.** Intercellular competition and the inevitability of
   multicellular aging. *PNAS* 114(49):12982–12987 (2017).
   DOI: 10.1073/pnas.1618854114 · PMID: 29087299.
   — Inevitability argument; needs a fitness reference to define decline.

## Control- / systems-theoretic framings (nearest neighbours — differentiated from)

9. **Kriete A.** Robustness and aging — a systems-level perspective / "Toward a
   control theory analysis of aging." *Biosystems* / systems-biology work (2013);
   see also PMC4335186. PMID: 18318658 (early control-theory framing).
   — Treats homeostasis as control but focuses on robustness/which-parameters, **not
     observability**. This is the closest prior framing; the observability argument is new.

10. **Dissipation theory of aging** (arXiv:2504.13044, 2025) and recent
    **"control theory of aging" for gerotherapeutics** (arXiv:2605.16781, 2025).
    — Thermodynamic and state-space framings respectively; neither invokes the
      unobservable-subspace / common-mode-drift mechanism.

11. **Novoseltsev VN, Yashin AI, et al.** Homeostasis and health: analysis from a
    standpoint of control theory. *Automation and Remote Control* 73(5) (2012).
    DOI: 10.1134/S0005117912050086.
    — Set-point / homeostatic-drift framing that predates and motivates this work.

## Empirical signatures the model was checked against

12. **Pyrkov TV, Avchaciov K, … Fedichev PO.** Longitudinal analysis of blood
    markers reveals progressive loss of resilience and predicts human lifespan
    limit. *Nature Communications* 12:2765 (2021).
    DOI: 10.1038/s41467-021-23014-1 · PMID: 34035236.
    — Critical slowing down: rising recovery time + autocorrelation with age (Fig 2c).

13. **Martinez-Jimenez CP, … Marioni JC, Odom DT.** Aging increases cell-to-cell
    transcriptional variability upon immune stimulation. *Science*
    355(6332):1433–1436 (2017). DOI: 10.1126/science.aah4115 · PMID: 28360329.
    — Rising cell-to-cell transcriptional variability with age (Fig 2b).

14. **Enge M, et al.** (single-cell pancreas) and **Hernando-Herraez I, et al.**
    Ageing affects DNA methylation drift and transcriptional cell-to-cell
    variability in mouse muscle stem cells. *Nature Communications* 10:4361 (2019).
    DOI: 10.1038/s41467-019-12293-4.
    — Methylation drift as microscopic origin of reference drift.

## The decisive prediction — reprogramming (partial vs full reset)

15. **Ocampo A, … Izpisua Belmonte JC.** In vivo amelioration of age-associated
    hallmarks by partial reprogramming. *Cell* 167(7):1719–1733 (2016).
    DOI: 10.1016/j.cell.2016.11.052 · PMID: 27984723.
    — *Transient/cyclic* OSKM rejuvenates; continuous expression is lethal → the
      non-monotonic dose–response the model predicts (Fig 3).

16. **Lu Y, Brommer B, Tian X, … Sinclair DA.** Reprogramming to recover youthful
    epigenetic information and restore vision. *Nature* 588(7836):124–129 (2020).
    DOI: 10.1038/s41586-020-2975-4 · PMID: 33268865.
    — Rejuvenation of function via re-referencing the epigenome, without genome repair.

17. **Kerepesi C, Zhang B, Lee SG, Trapp A, Gladyshev VN.** Epigenetic clocks
    reveal a rejuvenation event during embryogenesis followed by aging.
    *Science Advances* 7(26):eabg6082 (2021). DOI: 10.1126/sciadv.abg6082 ·
    PMID: 34172448. (See also Kerepesi et al., *Aging Cell*, 2023, intersection clock.)
    — "Ground zero": the germline/embryo re-derives the reference — the external
      re-calibration the soma lacks.

## Methods / tools

- Model, figures, and analysis: NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.0 (Python 3.11).
- Stochastic reference dynamics integrated by Euler–Maruyama; mortality by
  Gillespie-style hazard sampling; all code and parameters recorded in
  `process_trace.json` and reproducible from `model_outputs.npz` / `intervention.npz`.

*Note on identifiers:* every DOI above was confirmed against the Crossref API
(14/14 resolved; see `doi_verification.json`). Where a reference represents a
*family* of work (e.g. hyperfunction reviews, dissipation/control-theory
preprints), a representative primary source is cited rather than an exhaustive list.

## Search provenance

The papers were located through a web-search survey of the aging literature. I
list the survey queries below for transparency about how the landscape was
mapped, but I make **no claim about the exact number of underlying tool calls or
their individual identifiers** — that record is not something I can enumerate
reliably here, and it is not what the citations rest on. The queries were
approximately:

- "control theory setpoint homeostasis theory of aging"
- "loss of resilience critical slowing down aging recovery time Pyrkov"
- "increased cell-to-cell transcriptional variability with age"
- "information theory of aging Sinclair ICE mouse epigenetic"
- "Nelson Masel intercellular competition aging mathematically inevitable PNAS"
- "Gladyshev deleteriome aging accumulation deleterious changes"
- "hallmarks of aging expanding universe Lopez-Otin 2023"
- "epigenetic clock rejuvenation embryogenesis ground zero Kerepesi Gladyshev"
- "Ocampo 2016 in vivo partial reprogramming amelioration aging hallmarks Cell"
- "Kriete Toward a control theory analysis of aging 2013 systems biology"
- "Blagosklonny hyperfunction theory quasi-programmed aging mTOR Cell Cycle 2006"
- "Lu Sinclair 2020 reprogramming restore youthful epigenome vision Nature DOI"

Identifier *correctness* does not rest on those searches: it rests on the
Crossref confirmation pass documented above and in `doi_verification.json`.
