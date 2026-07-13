#!/usr/bin/env python3
"""unblind_and_analyze.py — exp-001 FINAL unblinding + arm-level analysis.  [CS-authored]

Run this ONLY after BOTH keys exist:
  Key-1 (operator-held): key1_R_to_arm.json  = {"R1":"B"|"L", ..., "R6":...}  (R-code -> arm)
  Key-2 (CS-held):       key2_eval_to_R.json = {..., "display_label_to_Rcode": {qid:{A|B: Rcode}}}

Composition:  eval-label --Key2--> R-code --Key1--> arm.
Produces blinding_key_FULL.json {code: {arm, question_id, category}}, backfills arm into the blind
scorecard_long, and runs make_analysis.py to emit the L-B endpoint (mean-delta, k/3) + per-dim/per-arm figures.

Usage:
  python unblind_and_analyze.py \
      --key1 key1_R_to_arm.json \
      --key2 04_evaluation/key2_eval_to_R.json \
      --long 02_results/scoring/blind_scores/scorecard_long_blind.csv \
      --harness 01_setup/harness \
      --out 05_analysis
Optionally --operator human_scores.json  ({code|label: {dimension: 1..5}}) to merge the operator's science scores first.
"""
import argparse, csv, json, os, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key1", required=True, help="operator Key-1: {Rcode: arm}")
    ap.add_argument("--key2", required=True, help="CS Key-2 json (has display_label_to_Rcode)")
    ap.add_argument("--long", required=True, help="scorecard_long_blind.csv (arm=code)")
    ap.add_argument("--harness", required=True, help="path to 01_setup/harness")
    ap.add_argument("--out", default="05_analysis")
    ap.add_argument("--operator", default=None, help="optional human_scores.json {code: {dim:1..5}}")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    sys.path.insert(0, a.harness)

    key1 = json.load(open(a.key1))                      # Rcode -> arm
    key2 = json.load(open(a.key2))
    lab2R = key2["display_label_to_Rcode"]              # {qid:{A|B:Rcode}}
    R2q   = key2.get("Rcode_to_question", {})

    # blinding_key_FULL: for each Rcode, its arm (from Key-1) + question (from Key-2)
    full = {}
    for qid, m in lab2R.items():
        for lab, rc in m.items():
            arm = key1.get(rc)
            if arm is None:
                raise SystemExit(f"Key-1 missing arm for {rc}")
            full[rc] = {"arm": arm, "question_id": qid, "eval_label": lab}
    json.dump({"note":"FULL unblind = Key-1 ∘ Key-2. code->arm+question.","key":full},
              open(os.path.join(a.out,"blinding_key_FULL.json"),"w"), indent=1)
    print("wrote blinding_key_FULL.json:", json.dumps(full, indent=1))

    # backfill arm into the long csv (was arm=code); write a post-unblind copy
    rows = list(csv.DictReader(open(a.long)))
    for r in rows:
        rc = r["code"]
        r["arm"] = full.get(rc, {}).get("arm", r.get("arm"))
    unblind_long = os.path.join(a.out, "scorecard_long_unblind.csv")
    with open(unblind_long, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print("wrote", unblind_long)

    # optional: merge the operator science scores BEFORE analysis (keyed by code)
    if a.operator and os.path.exists(a.operator):
        import run_scoring
        operator = json.load(open(a.operator))
        # allow operator keyed by eval-label -> remap to code
        label2code = {lab: rc for qid,m in lab2R.items() for lab,rc in m.items()}
        operator = {label2code.get(k, k): v for k, v in operator.items()}
        run_scoring.merge_human_scores(unblind_long, operator, unblind_long)
        print("merged the operator scores into", unblind_long)

    # run the arm-level analysis (make_analysis.py) with the full key
    import make_analysis as MA
    key_full = {rc: {"arm": v["arm"], "question_id": v["question_id"]} for rc, v in full.items()}
    tmp_key = os.path.join(a.out, "_key_for_analysis.json"); json.dump(key_full, open(tmp_key,"w"))
    rows2 = MA.load_long(unblind_long, key_full)
    agg, comp = MA.aggregate(rows2)
    MA.write_tables(agg, a.out)
    print("ENDPOINT:", json.dumps(agg["endpoint"], indent=1))
    try:
        import make_analysis_figs as F
        F.render_all(rows2, agg, comp, a.out)
        print("figures rendered to", a.out)
    except Exception as e:
        print("figs skipped:", e)

if __name__ == "__main__":
    main()
