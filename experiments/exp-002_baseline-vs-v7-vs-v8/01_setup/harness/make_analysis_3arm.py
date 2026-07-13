#!/usr/bin/env python3
"""make_analysis_3arm.py — exp-002 THREE-ARM analysis extension.  [CS-authored]

exp-001's `make_analysis.py` (shared, in ../../exp-001_baseline-vs-v0-loop/01_setup/harness/) computes ONE
pairwise delta (L-B). exp-002 has THREE arms (B / L7 / L8), so the endpoint needs the three pairwise deltas:
  Delta(L8-L7) = the v8-upgrade-bundle effect (PRIMARY: did optimizing the loop help?)
  Delta(L8-B)  = the full v8 loop vs raw baseline
  Delta(L7-B)  = the v7 loop vs raw baseline (reproduces the exp-001 finding on the new questions)

This module does NOT fork the shared harness. It imports its arm-generic building blocks
(load_long, aggregate, write_tables, render_all, DIMS, _verdict) and only REPLACES the 2-arm endpoint
with a 3-way one. Everything upstream (by_dim_scorer_arm, per_question composite, per-category, the operator merge,
two-key unblinding) is already arm-generic and reused unchanged.

Usage (after unblinding backfills the arm column with B/L7/L8):
  python make_analysis_3arm.py --long <scorecard_long_unblind.csv> --harness <exp-001 harness path> --out 05_analysis
"""
import argparse, json, os, sys
import statistics as st


def three_arm_endpoint(comp, arms=("B", "L7", "L8")):
    """comp: {(scorer, qid, arm): composite}. Returns the 3 pairwise deltas + per-question detail.
    Prefers the COMBINED composite (mean of CS+the operator); falls back to CS-only interim (flagged)."""
    scorer = "combined" if any(sc == "combined" for (sc, _, _) in comp) else "cs"
    qids = sorted({qid for (sc, qid, _) in comp if sc == scorer})
    # the pairs we report; PRIMARY first
    pairs = [("L8", "L7"), ("L8", "B"), ("L7", "B")]
    out = {"scorer": scorer, "is_interim_cs_only": scorer == "cs", "arms": list(arms),
           "primary": "L8_minus_L7", "pairwise": {}}
    for hi, lo in pairs:
        per_q, wins = [], 0
        for qid in qids:
            a = comp.get((scorer, qid, hi)); b = comp.get((scorer, qid, lo))
            if a is not None and b is not None:
                d = round(a - b, 3); per_q.append({"question_id": qid, "delta": d})
                wins += 1 if d > 0 else 0
        md = round(st.mean([d["delta"] for d in per_q]), 3) if per_q else None
        out["pairwise"][f"{hi}_minus_{lo}"] = {
            "per_question_delta": per_q, "mean_delta": md,
            "delta_min": min([d["delta"] for d in per_q]) if per_q else None,
            "delta_max": max([d["delta"] for d in per_q]) if per_q else None,
            "k_wins": wins, "k_total": len(per_q),
        }
    # per-arm mean composite (across questions) — the level each arm sits at
    out["arm_mean_composite"] = {}
    for arm in arms:
        vals = [comp[(scorer, q, arm)] for q in qids if (scorer, q, arm) in comp]
        out["arm_mean_composite"][arm] = round(st.mean(vals), 3) if vals else None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--long", required=True, help="scorecard_long with arm in {B,L7,L8}")
    ap.add_argument("--harness", required=True, help="path to exp-001 shared harness (for the reused functions)")
    ap.add_argument("--out", default="05_analysis")
    ap.add_argument("--key_full", default=None, help="optional blinding_key_FULL.json to backfill arm")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sys.path.insert(0, a.harness)
    import make_analysis as MA

    key_full = json.load(open(a.key_full)) if a.key_full else None
    rows = MA.load_long(a.long, key_full)
    agg, comp = MA.aggregate(rows)                 # arm-generic upstream — reused unchanged
    ep3 = three_arm_endpoint(comp)                 # REPLACE the 2-arm endpoint with the 3-way one
    agg["endpoint_3arm"] = ep3
    MA.write_tables(agg, a.out)                     # shared tables (by-dim/-cat/-question)
    # write the 3-arm endpoint separately (write_tables only knows the 2-arm 'endpoint')
    json.dump(ep3, open(os.path.join(a.out, "endpoint_3arm.json"), "w"), indent=1)
    print("3-ARM ENDPOINT:", json.dumps(ep3, indent=1))
    try:
        import make_analysis_figs as F
        F.render_all(rows, agg, comp, a.out)        # per-dim/-arm/-category bars already handle >2 arms
        print("shared figures rendered to", a.out)
    except Exception as e:
        print("shared figs skipped:", e)
    print("NOTE: 3-bar pairwise-delta figure is rendered by make_3arm_figs.py (separate, run after this).")


if __name__ == "__main__":
    main()
