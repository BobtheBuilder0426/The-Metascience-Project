"""composite.py — assemble one answer's full score (quantification.md §1, creativity-metric.md §1).

Ties together: judge rubric panel + citation cap (Grounding) + entity specificity
(Completeness) + the multiplicative creativity index (novelty x plausibility_gate x
reasoning_trace_gate). Loads weights from rubric.json. Pure — inputs are the dicts
produced by the other modules.
"""
import json
import os

RUBRIC_DIMS = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]


def load_weights(rubric_path: str) -> dict:
    with open(rubric_path) as f:
        rub = json.load(f)
    w = {d["key"]: d["weight"] for d in rub["dimensions"]}
    assert abs(sum(w.values()) - 1.0) < 1e-9, f"weights must sum to 1, got {sum(w.values())}"
    return w


def gate(score) -> float:
    """1..5 Likert -> [0,1] gate = (s-1)/4."""
    if score is None:
        return 0.0
    return max(0.0, min(1.0, (float(score) - 1.0) / 4.0))


def creativity_index(novelty: float, plausibility, reasoning_trace) -> dict:
    """The multiplicative anti-hallucination composite (creativity-metric.md §1)."""
    pg = gate(plausibility)
    rg = gate(reasoning_trace)
    idx = round(novelty * pg * rg, 4)
    # map the [0,1] index back onto the 1..5 rubric scale for the creativity dimension
    dim_score = round(1.0 + 4.0 * idx, 3)
    return {"creativity_index": idx, "novelty": round(novelty, 3),
            "plausibility_gate": round(pg, 3), "reasoning_trace_gate": round(rg, 3),
            "creativity_dim_score_1to5": dim_score,
            "hallucination_flag": (novelty >= 0.6 and rg <= 0.25)}


def integrity_cap(dataset_result=None, trace_result=None) -> dict:
    """LB-075: 'Grounding & integrity' folds in dataset-ID resolution + the did-it-really-happen
    action check. Returns {cap, reasons} — a HARD cap on Grounding (1..5). A fabricated action or a
    named-but-unresolvable/unused dataset drags Grounding down exactly like a fabricated citation.
    Both args optional (None = signal absent, no cap contribution)."""
    cap, reasons = 5, []
    if trace_result:
        # A process_trace step that NAMES a checkable artifact (PMID/DOI/accession/calculation) that then
        # fails to resolve = an integrity hit (fabricated/erroneous action). But a reasoning/analysis step
        # that names no checkable artifact is "asserted", NOT a failure — it is taken at face value and must
        # NOT drag Grounding down (LB-082 fix: the earlier code divided verified steps by ALL steps, so the
        # reasoning steps every good trace contains guaranteed a <0.3 fraction and pinned Grounding to 2 for
        # every answer). The honest denominator is the CHECKABLE steps only: verified + unverified.
        if trace_result.get("any_unverified"):
            cap = min(cap, 1); reasons.append("process_trace names a checkable action that did not resolve -> cap 1")
        n_ver = trace_result.get("n_verified")
        n_unver = trace_result.get("n_unverified")
        n_check = (n_ver or 0) + (n_unver or 0)
        if n_check > 0 and not trace_result.get("any_unverified"):
            vf = n_ver / n_check  # fraction of *checkable* steps that resolved
            for thr, c in [(0.9, 5), (0.6, 4), (0.3, 3)]:
                if vf >= thr:
                    cap = min(cap, c); break
            else:
                cap = min(cap, 2); reasons.append(f"checkable trace steps mostly unresolved ({vf:.0%}) -> cap 2")
        # else: no checkable steps in the trace (all reasoning/asserted) -> trace contributes NO cap;
        # Grounding is then governed by the citation + dataset evidence, which is the correct behaviour.
    if dataset_result:
        n = dataset_result.get("n_dataset_ids", 0)
        if n:
            rate = dataset_result.get("used_and_resolved_rate", 0.0) or 0.0
            if rate < 0.5:
                cap = min(cap, 2); reasons.append(f"dataset IDs cited but {rate:.0%} used+resolved -> cap 2")
            elif rate < 0.9:
                cap = min(cap, 4); reasons.append(f"dataset use partial ({rate:.0%}) -> cap 4")
    return {"cap": cap, "reasons": reasons}


def score_answer(*, question, rubric_result, citation_result, entity_result,
                 novelty_result, creativity_panel, weights,
                 dataset_result=None, trace_result=None) -> dict:
    """Produce the final per-answer scorecard row. All args are module outputs.
    dataset_result / trace_result (LB-075) widen Grounding into 'Grounding & integrity'."""
    from .citations import grounding_cap
    from .extract import specificity_score

    dims = dict(rubric_result["aggregate"])  # judge means, may be None

    # --- Grounding & integrity: min(judge, citation cap, integrity cap, overclaim cap) ---
    gcap = grounding_cap(citation_result)
    icap = integrity_cap(dataset_result, trace_result)
    # C2 (exp-002 overclaim improvement): scope-inflation / overclaim penalty. An answer that cites REAL sources but overstates
    # what they show (correlation->causation, minor finding->core driver) is not fabrication (that caps to 1),
    # so this is a softer, graduated hit: any overclaim caps grounding at 4, several (>=2) cap at 3. It stacks
    # via min() with the other caps. Mirrors the human catch (exp-001: the operator flagged the baseline apelin overclaim).
    oc = (citation_result or {}).get("overclaim_count", 0) or 0
    overclaim_cap = 5
    if oc >= 2:
        overclaim_cap = 3
    elif oc == 1:
        overclaim_cap = 4
    eff_cap = min(gcap, icap["cap"], overclaim_cap)
    if dims.get("grounding") is not None:
        dims["grounding"] = min(dims["grounding"], eff_cap)
    else:
        dims["grounding"] = eff_cap

    # --- Completeness: blend judge + entity-specificity signal (mean) ---
    spec = specificity_score(entity_result)
    if dims.get("completeness") is not None:
        dims["completeness"] = round((dims["completeness"] + spec) / 2.0, 3)
    else:
        dims["completeness"] = spec

    # --- Creativity: OVERRIDE judge with the multiplicative gated index ---
    crea = creativity_index(novelty_result["novelty"],
                            creativity_panel.get("plausibility"),
                            creativity_panel.get("reasoning_trace"))
    dims["creativity"] = crea["creativity_dim_score_1to5"]

    # --- weighted composite ---
    composite = 0.0
    for d in RUBRIC_DIMS:
        composite += (dims[d] or 0.0) * weights[d]
    composite = round(composite, 3)

    return {
        "question": question,
        "dimensions": {d: dims[d] for d in RUBRIC_DIMS},
        "weighted_composite": composite,
        "grounding_cap": gcap,
        "integrity_cap": icap["cap"],
        "integrity_reasons": icap["reasons"],
        "overclaim_count": oc,
        "overclaim_cap": overclaim_cap,
        "effective_grounding_cap": eff_cap,
        "dataset_resolution": dataset_result,
        "trace_verification": ({k: trace_result[k] for k in
                                ("n_steps", "n_verified", "n_unverified", "verified_fraction", "any_unverified")}
                               if trace_result else None),
        "specificity_signal": spec,
        "creativity_detail": crea,
        "citation_verification_rate": citation_result["verification_rate"],
        "n_citations": citation_result["n_citations"],
        "entity_counts": entity_result["counts"],
        "redflags": creativity_panel.get("redflags", []),
        "inter_judge_absdiff": rubric_result.get("inter_judge_absdiff", {}),
    }
