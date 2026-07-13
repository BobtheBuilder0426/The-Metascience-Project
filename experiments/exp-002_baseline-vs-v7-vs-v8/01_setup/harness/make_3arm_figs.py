#!/usr/bin/env python3
"""make_3arm_figs.py — exp-002 THREE-ARM deliverable figures.  [CS-authored]

exp-001's make_analysis_figs.py hardcodes the pair ("B","L") and cannot render 3 arms. This module renders
the exp-002 figures for arms B / L7 / L8:
  fig_3arm_per_question_composite.png  — composite per question, 3 grouped bars
  fig_3arm_by_dimension.png            — 5 dims x 3 arms (combined scorer)
  fig_3arm_pairwise_delta.png          — the endpoint: 3 pairwise deltas (L8-L7 primary, L8-B, L7-B)

Colours: B muted comparator, L7 mid, L8 focal (colour-blind-safe, Okabe-Ito-derived).
Loads figure-style (apply_figure_style/set_frame) if the skill is present; degrades to a plain style otherwise.
Run AFTER make_analysis_3arm.py (reads endpoint_3arm.json + the shared analysis_tables.csv).
"""
import argparse, csv, json, os
from collections import defaultdict

ARM_ORDER = ["B", "L7", "L8"]
ARM_COLOR = {"B": "#B0A58F", "L7": "#7FA8C9", "L8": "#2F6DB5"}   # muted -> mid -> focal
ARM_LABEL = {"B": "B (baseline)", "L7": "L7 (v7 loop)", "L8": "L8 (v8 loop)"}
DIMS = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]
DIM_LABEL = {"grounding": "Grounding\n& integrity", "reasoning": "Reasoning\n& soundness",
             "completeness": "Completeness", "usefulness": "Usefulness", "creativity": "Creativity\n(gated)"}


def _style():
    try:
        import matplotlib; matplotlib.use("Agg")
        g = globals()
        if "apply_figure_style" in g:  # kernel-plugin form
            apply_figure_style()  # noqa
        return True
    except Exception:
        return False


def _frame(ax):
    g = globals()
    if "set_frame" in g:
        set_frame(ax)  # noqa
    else:
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)


def render(analysis_tables_csv, endpoint_3arm_json, out_dir, scorer="combined"):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    os.makedirs(out_dir, exist_ok=True)
    made = []

    # ---- parse the shared analysis_tables.csv blocks we need ----
    per_q = defaultdict(dict)      # (qid) -> {arm: composite}  for scorer
    by_dim = defaultdict(dict)     # (dim) -> {arm: mean_score} for scorer
    block = None
    for row in csv.reader(open(analysis_tables_csv)):
        if row and row[0] == "#":
            block = row[1]; continue
        if not row or row[0] in ("scorer",): continue
        if block == "per_question_composite" and len(row) >= 4 and row[0] == scorer:
            per_q[row[1]][row[2]] = float(row[3])
        elif block == "by_dimension_scorer_arm" and len(row) >= 4 and row[0] == scorer:
            by_dim[row[1]][row[2]] = float(row[3])

    # ---- FIG 1: per-question composite, 3 grouped bars ----
    qids = sorted(per_q.keys())
    if qids:
        fig, ax = plt.subplots(figsize=(7.6, 4.2)); w = 0.26; x = np.arange(len(qids))
        for i, arm in enumerate(ARM_ORDER):
            ys = [per_q[q].get(arm, 0) for q in qids]
            ax.bar(x + (i - 1) * w, ys, width=w, color=ARM_COLOR[arm], label=ARM_LABEL[arm],
                   edgecolor="#333", linewidth=0.6)
        _frame(ax); ax.set_xticks(x); ax.set_xticklabels(qids); ax.set_ylim(0, 5.3)
        ax.set_ylabel("Weighted composite (1-5)"); ax.legend(fontsize=7, framealpha=0.9)
        ax.set_title(f"exp-002 per-question composite by arm ({scorer})", fontsize=8, loc="left")
        fig.tight_layout(); p = os.path.join(out_dir, "fig_3arm_per_question_composite.png")
        fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig); made.append(p)

    # ---- FIG 2: 5 dims x 3 arms ----
    if by_dim:
        fig, ax = plt.subplots(figsize=(9, 4.0)); w = 0.26; x = np.arange(len(DIMS))
        for i, arm in enumerate(ARM_ORDER):
            ys = [by_dim.get(d, {}).get(arm, 0) for d in DIMS]
            ax.bar(x + (i - 1) * w, ys, width=w, color=ARM_COLOR[arm], label=ARM_LABEL[arm],
                   edgecolor="#333", linewidth=0.6)
        _frame(ax); ax.set_xticks(x); ax.set_xticklabels([DIM_LABEL[d] for d in DIMS], fontsize=7.5)
        ax.set_ylim(0, 5.3); ax.set_ylabel("Mean score (1-5)"); ax.legend(fontsize=7, framealpha=0.9)
        ax.set_title(f"exp-002 per-dimension by arm ({scorer})", fontsize=8, loc="left")
        fig.tight_layout(); p = os.path.join(out_dir, "fig_3arm_by_dimension.png")
        fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig); made.append(p)

    # ---- FIG 3: the endpoint — 3 pairwise deltas ----
    ep = json.load(open(endpoint_3arm_json))
    pw = ep["pairwise"]
    keys = ["L8_minus_L7", "L8_minus_B", "L7_minus_B"]     # primary first
    labels = {"L8_minus_L7": "L8 - L7\n(v8 upgrade effect)", "L8_minus_B": "L8 - B\n(full v8 vs baseline)",
              "L7_minus_B": "L7 - B\n(v7 vs baseline)"}
    vals = [pw[k]["mean_delta"] if pw[k]["mean_delta"] is not None else 0 for k in keys]
    kw = [f"k={pw[k]['k_wins']}/{pw[k]['k_total']}" for k in keys]
    fig, ax = plt.subplots(figsize=(7.2, 4.2)); x = np.arange(len(keys))
    colors = ["#2F6DB5" if v > 0 else "#C24A5E" for v in vals]
    bars = ax.bar(x, vals, width=0.6, color=colors, edgecolor="#333", linewidth=0.8)
    for xi, v, k in zip(x, vals, kw):
        ax.text(xi, v + (0.03 if v >= 0 else -0.03), f"{v:+.2f}\n{k}", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=7.5)
    _frame(ax); ax.axhline(0, color="#333", lw=0.8); ax.set_xticks(x)
    ax.set_xticklabels([labels[k] for k in keys], fontsize=7.5)
    ax.set_ylabel("mean-Δ composite (arms)"); pad = max(0.3, max(abs(v) for v in vals) * 0.25)
    ax.set_ylim(min(vals) - pad, max(vals) + pad)
    interim = " [CS-only INTERIM]" if ep.get("is_interim_cs_only") else ""
    ax.set_title(f"exp-002 endpoint: pairwise mean-Δ ({ep['scorer']}){interim}", fontsize=8, loc="left")
    fig.tight_layout(); p = os.path.join(out_dir, "fig_3arm_pairwise_delta.png")
    fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig); made.append(p)
    return made


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tables", required=True, help="analysis_tables.csv from make_analysis_3arm")
    ap.add_argument("--endpoint", required=True, help="endpoint_3arm.json")
    ap.add_argument("--out", default="05_analysis")
    ap.add_argument("--scorer", default="combined")
    a = ap.parse_args()
    _style()
    made = render(a.tables, a.endpoint, a.out, a.scorer)
    print("rendered:", made)


if __name__ == "__main__":
    main()
