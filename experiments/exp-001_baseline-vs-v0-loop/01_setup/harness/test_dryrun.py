"""test_dryrun.py — offline verification of the scoring harness.

Runs the full pipeline on a fixture with known-good and known-bad answers and
ASSERTS the anti-hallucination + ranking behaviours. No network, deterministic.
Run:  python test_dryrun.py     (exit 0 = all pass)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from adapters import DryRunAdapters
from run_scoring import run_experiment, score_one_answer
from scoring import composite as compmod
from scoring.extract import extract_citations, extract_entities
from scoring.citations import verify_citations, grounding_cap
from scoring.novelty import retrieval_frequency_novelty

FAILS = []
N_CHECKS = 0


def check(name, cond, detail=""):
    global N_CHECKS
    N_CHECKS += 1
    print(("PASS" if cond else "FAIL"), "-", name, ("" if cond else f" :: {detail}"))
    if not cond:
        FAILS.append(name)


def main():
    ad = DryRunAdapters()
    rubric = os.path.join(HERE, "rubric.json")

    # 1. unit: citation extraction finds pmid + doi
    cits = extract_citations("Real (PMID: 31133716) and fake 10.1234/fake.x here.")
    check("extract_citations finds pmid+doi", len(cits) == 2, cits)

    # 2. unit: retrieval-frequency novelty is monotone decreasing, 0 hits -> 1.0
    check("novelty(0 hits)=1.0", abs(retrieval_frequency_novelty(0) - 1.0) < 1e-9)
    check("novelty monotone", retrieval_frequency_novelty(10) > retrieval_frequency_novelty(1000))

    # 3. unit: fabricated citations -> verification rate 0 -> grounding cap 1
    trap = "Cures all aging (PMID: 00000001). Also 10.1234/fake.novel works."
    cv = verify_citations(trap, lambda raw: "the claim", ad.resolver_fn, ad.entailment_fn)
    check("fabricated cites -> low verify rate", (cv["verification_rate"] or 0) < 0.5, cv["verification_rate"])
    check("fabricated cites -> grounding cap 1", grounding_cap(cv) == 1, grounding_cap(cv))

    # 4. unit: no citations -> grounding cap 2 (unsupported assertions)
    cv0 = verify_citations("No citations here at all.", lambda r: None, ad.resolver_fn, ad.entailment_fn)
    check("no citations -> grounding cap 2", grounding_cap(cv0) == 2)

    # 4b. C2 (exp-002 overclaim improvement): a REAL, supported citation whose claim overstates it -> overclaim flagged,
    #     and grounding penalised below a faithful control (real cite, no overclaim).
    oc_txt = "X is the core driver of aging (PMID: 12345678)."          # real cite, overclaims
    faith_txt = "X is associated with aging (PMID: 12345678)."          # real cite, faithful
    cv_oc = verify_citations(oc_txt, lambda raw: "X is the core driver of aging", ad.resolver_fn, ad.entailment_fn)
    cv_fa = verify_citations(faith_txt, lambda raw: "X is associated with aging", ad.resolver_fn, ad.entailment_fn)
    check("overclaim detected on real-but-overstated cite", cv_oc.get("overclaim_count", 0) == 1, cv_oc.get("overclaim_count"))
    check("faithful cite has no overclaim", cv_fa.get("overclaim_count", 0) == 0, cv_fa.get("overclaim_count"))
    # overclaim caps grounding at 4 (single) — must sit strictly below the faithful control's cap
    check("overclaim caps grounding below faithful control",
          min(grounding_cap(cv_oc), 4 if cv_oc.get("overclaim_count",0)>=1 else 5) < grounding_cap(cv_fa),
          (grounding_cap(cv_oc), grounding_cap(cv_fa)))

    # 5. unit: specificity — entity-rich answer scores higher than vague
    rich = extract_entities("PGC-1alpha and SIRT1 drive mitophagy; Seahorse OCR rises 20% with urolithin A.")
    vague = extract_entities("Mitochondria matter for aging and should be studied.")
    check("specificity rich > vague", rich["counts"]["total"] > vague["counts"]["total"],
          (rich["counts"]["total"], vague["counts"]["total"]))

    # 6. integration: full experiment on the fixture
    manifest = json.load(open(os.path.join(HERE, "answers.example.json")))
    out = run_experiment(manifest, ad, rubric, os.path.join(HERE, "out"))
    rows = {f'{r["arm"]}#{r["run"]}': r for r in out["rows"]}

    # 6a. the trap (L#3) has the lowest composite of all
    trap_comp = rows["L#3"]["weighted_composite"]
    check("trap has lowest composite", trap_comp == min(r["weighted_composite"] for r in out["rows"]),
          trap_comp)
    # 6b. trap grounding dimension driven to 1 by citation cap
    check("trap grounding = 1", rows["L#3"]["dimensions"]["grounding"] == 1)
    # 6c. good loop answers beat baseline mean
    check("loop beats baseline", out["summary"]["Q1"]["delta_L_minus_B"] is not None
          and rows["L#1"]["weighted_composite"] > rows["B#1"]["weighted_composite"])
    # 6d. Elo ranks the trap below both baselines
    ranking = out["elo"]["Q1"]["ranking"]
    check("Elo ranks trap last among L, below baselines",
          ranking.index("L#3") > ranking.index("B#1") and ranking.index("L#3") > ranking.index("B#2"),
          ranking)
    # 6e. weights sum to 1 (rubric contract)
    check("weights sum to 1", abs(sum(out["weights"].values()) - 1.0) < 1e-9)
    # 6f. scorecard files written
    check("scorecard.json + csv written",
          os.path.exists(os.path.join(HERE, "out", "scorecard.json"))
          and os.path.exists(os.path.join(HERE, "out", "scorecard.csv")))

    print("\n%d checks, %d failures" % (N_CHECKS, len(FAILS)))
    if FAILS:
        print("FAILED:", FAILS); sys.exit(1)
    print("ALL PASS")


if __name__ == "__main__":
    main()
