#!/usr/bin/env python3
"""make_analysis_figs.py — the figure renderers for make_analysis.py (LB-077).  [CS-authored]

Kept separate so make_analysis.py can emit the tables with no matplotlib dependency (--tables-only).
Every figure is built from the tidy aggregates; every underlying number is in analysis_tables.csv.
Arm colors are threaded consistently: Arm B = comparator (muted), Arm L = focal (saturated).
"""
import os, statistics as st
from collections import defaultdict
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DIMS = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]
DIM_LABEL = {"grounding": "Grounding\n& integrity", "reasoning": "Reasoning\n& soundness",
             "completeness": "Completeness", "usefulness": "Usefulness", "creativity": "Creativity"}
SCORERS = ["cs", "operator", "combined"]
SCORER_LABEL = {"cs": "CS harness", "operator": "the operator (human)", "combined": "Combined mean"}
CAT_LABEL = {1: "Cat-1\nday-in-lab", 2: "Cat-2\nbig-think", 3: "Cat-3\ntranslational"}
ARM_COLOR = {"B": "#B0A58F", "L": "#2F6DB5"}   # B muted comparator, L focal
ARM_LABEL = {"B": "Arm B (baseline blank CS)", "L": "Arm L (v7 loop)"}


def _try_style():
    try:
        from kernel import apply_figure_style
        apply_figure_style()
        return True
    except Exception:
        plt.rcParams.update({"font.size": 8, "axes.spines.top": False, "axes.spines.right": False})
        return False


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return st.mean(xs) if xs else None


def fig_dim_by_scorer(rows, out_dir):
    """For EACH dimension: Arm L vs Arm B, three panels {CS, the operator, combined}. 5 files."""
    paths = []
    by = defaultdict(list)
    for r in rows:
        if r["score"] is not None:
            by[(r["dimension"], r["scorer"], r["arm"])].append(r["score"])
    for dim in DIMS:
        fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7), sharey=True)
        for ax, sc in zip(axes, SCORERS):
            vals = {arm: _mean(by.get((dim, sc, arm), [])) for arm in ("B", "L")}
            xs = [0, 1]; ys = [vals["B"] or 0, vals["L"] or 0]
            bars = ax.bar(xs, ys, color=[ARM_COLOR["B"], ARM_COLOR["L"]], width=0.62)
            for x, y in zip(xs, ys):
                if y:
                    ax.text(x, y + 0.08, f"{y:.2f}", ha="center", va="bottom", fontsize=7)
            ax.set_xticks(xs); ax.set_xticklabels(["B", "L"])
            ax.set_title(SCORER_LABEL[sc], fontsize=8)
            ax.set_ylim(0, 5.4)
            if sc == "cs":
                ax.set_ylabel("mean score (1–5)")
        fig.suptitle(f"{DIM_LABEL[dim].replace(chr(10),' ')} — Arm L vs Arm B", fontsize=9, y=1.02)
        fig.tight_layout()
        p = os.path.join(out_dir, f"fig_dim_{dim}_by_scorer.png")
        fig.savefig(p, dpi=150, bbox_inches="tight"); plt.close(fig); paths.append(p)
    return paths


def fig_by_category(rows, out_dir):
    """Composite by category x arm, one panel per scorer — the 'where does the loop help' view."""
    # weighted composite per (scorer, category, arm)
    perq = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r["score"] is not None and r.get("category") not in (None, ""):
            perq[(r["scorer"], int(r["category"]), r["arm"], r["question_id"])][r["dimension"]].append((r["score"], r["weight"]))
    comp = defaultdict(list)
    for (sc, cat, arm, qid), dm in perq.items():
        c = sum(_mean([v for v, _ in dm[d]]) * dm[d][0][1] for d in DIMS if dm.get(d))
        comp[(sc, cat, arm)].append(c)
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 2.9), sharey=True)
    cats = [1, 2, 3]
    for ax, sc in zip(axes, SCORERS):
        w = 0.36
        for i, arm in enumerate(("B", "L")):
            ys = [_mean(comp.get((sc, c, arm), [])) or 0 for c in cats]
            xs = [c + (i - 0.5) * w for c in cats]
            ax.bar(xs, ys, width=w, color=ARM_COLOR[arm], label=ARM_LABEL[arm] if sc == "cs" else None)
        ax.set_xticks(cats); ax.set_xticklabels([CAT_LABEL[c] for c in cats], fontsize=7)
        ax.set_title(SCORER_LABEL[sc], fontsize=8); ax.set_ylim(0, 5.4)
        if sc == "cs":
            ax.set_ylabel("weighted composite")
    axes[0].legend(fontsize=6.5, frameon=False, loc="upper left")
    fig.suptitle("Composite by question category — Arm L vs Arm B", fontsize=9, y=1.02)
    fig.tight_layout()
    p = os.path.join(out_dir, "fig_by_category.png")
    fig.savefig(p, dpi=150, bbox_inches="tight"); plt.close(fig); return [p]


def fig_per_question_composite(agg, out_dir):
    rowsq = [r for r in agg["per_question"] if r["scorer"] == "combined"]
    qids = sorted({r["question_id"] for r in rowsq})
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    w = 0.36
    for i, arm in enumerate(("B", "L")):
        ys = [next((r["composite"] for r in rowsq if r["question_id"] == q and r["arm"] == arm), 0) for q in qids]
        xs = [j + (i - 0.5) * w for j in range(len(qids))]
        ax.bar(xs, ys, width=w, color=ARM_COLOR[arm], label=ARM_LABEL[arm])
    ax.set_xticks(range(len(qids))); ax.set_xticklabels(qids)
    ax.set_ylabel("combined composite"); ax.set_ylim(0, 5.4)
    ax.set_title("Per-question composite (combined mean CS+the operator)", fontsize=9)
    ax.legend(fontsize=7, frameon=False)
    fig.tight_layout()
    p = os.path.join(out_dir, "fig_per_question_composite.png")
    fig.savefig(p, dpi=150, bbox_inches="tight"); plt.close(fig); return [p]


def fig_endpoint(agg, out_dir):
    e = agg["endpoint"]; deltas = e["per_question_delta"]
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    qids = [d["question_id"] for d in deltas]; ds = [d["delta"] for d in deltas]
    cols = ["#2F6DB5" if d > 0 else "#C0603A" for d in ds]
    ax.bar(range(len(qids)), ds, color=cols, width=0.6)
    if e["mean_delta"] is not None:
        ax.axhline(e["mean_delta"], ls="--", lw=1.3, color="#333",
                   label=f"mean-Δ = {e['mean_delta']:+.2f}")
    ax.axhline(0, lw=0.8, color="#888")
    ax.set_xticks(range(len(qids))); ax.set_xticklabels(qids)
    ax.set_ylabel("Δ composite (Arm L − Arm B)")
    ax.set_title(f"Endpoint: mean-Δ + win-count  ·  k = {e['k_wins']}/{e['k_total']}", fontsize=9)
    ax.legend(fontsize=7, frameon=False, loc="best")
    ax.text(0.02, 0.02, e["verdict"], transform=ax.transAxes, fontsize=6.5, style="italic", va="bottom")
    fig.tight_layout()
    p = os.path.join(out_dir, "fig_endpoint_meanDelta_k.png")
    fig.savefig(p, dpi=150, bbox_inches="tight"); plt.close(fig); return [p]


def fig_cs_vs_human(rows, out_dir):
    """Calibration: CS score vs the operator score per (answer x dimension)."""
    pairs = defaultdict(dict)
    for r in rows:
        if r["scorer"] in ("cs", "operator") and r["score"] is not None:
            pairs[(r["code"], r["dimension"])][r["scorer"]] = r["score"]
    xs, ys, cs_only = [], [], 0
    for (code, dim), d in pairs.items():
        if "cs" in d and "operator" in d:
            xs.append(d["cs"]); ys.append(d["operator"])
        else:
            cs_only += 1
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    ax.plot([1, 5], [1, 5], ls=":", color="#999", lw=1)
    ax.scatter(xs, ys, s=26, color="#2F6DB5", alpha=0.75, edgecolor="white", linewidth=0.5)
    ax.set_xlabel("CS harness score"); ax.set_ylabel("the operator score")
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_aspect("equal")
    n = len(xs)
    sub = f"n={n} answer×dim pairs" + (f" · {cs_only} CS-only (grounding)" if cs_only else "")
    ax.set_title("CS vs the operator agreement\n" + sub, fontsize=8)
    fig.tight_layout()
    p = os.path.join(out_dir, "fig_cs_vs_human_agreement.png")
    fig.savefig(p, dpi=150, bbox_inches="tight"); plt.close(fig); return [p]


def render_all(rows, agg, comp, out_dir):
    _try_style()
    made = []
    made += fig_dim_by_scorer(rows, out_dir)
    made += fig_by_category(rows, out_dir)
    made += fig_per_question_composite(agg, out_dir)
    made += fig_endpoint(agg, out_dir)
    made += fig_cs_vs_human(rows, out_dir)
    print(f"figures -> {len(made)} PNGs in {out_dir}")
    return made
