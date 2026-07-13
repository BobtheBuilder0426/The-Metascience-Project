"""citations.py — citation verification (quantification.md §2a).

The credibility backbone. For every citation:
  1. resolve existence (does the reference exist?)         -> resolver_fn
  2. check support   (does it actually back the claim?)    -> entailment_fn (LLM)
  3. rate = supported / total ; caps the Grounding dimension.

Both fns are injected so this runs offline in dry-run and against
PubMed/OpenAlex + host.llm in real mode.
"""
from .extract import extract_citations


def verify_citations(answer_text: str, claims_map, resolver_fn, entailment_fn) -> dict:
    """
    claims_map: callable(citation_raw) -> the claim sentence the citation is attached to
                (or None). Kept simple: nearest preceding sentence.
    resolver_fn(citation) -> {"exists": bool, "title": str|None, "abstract": str|None}
    entailment_fn(claim, abstract) -> {"supports": bool, "reason": str}
    """
    cites = extract_citations(answer_text)
    results = []
    for c in cites:
        claim = claims_map(c["raw"]) if claims_map else None
        res = resolver_fn(c)
        rec = {"citation": c, "claim": claim, "exists": bool(res.get("exists")),
               "title": res.get("title"), "flags": []}
        if not res.get("exists"):
            rec["flags"].append("nonexistent_reference")
            rec["supported"] = False
        else:
            if claim and res.get("abstract"):
                ent = entailment_fn(claim, res["abstract"])
                rec["supported"] = bool(ent.get("supports"))
                rec["entailment_reason"] = ent.get("reason")
                # C2 (exp-002 overclaim improvement): overclaim = the source is real and topical but the answer states MORE
                # than it shows (correlation cited as causation, a minor/associative finding cited as a
                # core driver, a single study cited as established consensus). Distinct from "unsupported":
                # the citation is not fabricated, but its strength is inflated. entailment_fn MAY return
                # `overclaim` (bool); absent -> False, so this degrades safely on older adapters.
                rec["overclaim"] = bool(ent.get("overclaim"))
                if not rec["supported"]:
                    rec["flags"].append("claim_not_supported_by_cited_source")
                if rec["overclaim"]:
                    rec["flags"].append("overclaim_source_overstated")
            else:
                # exists but we can't check support -> counts as unverified, not supported
                rec["supported"] = False
                rec["flags"].append("reference_exists_but_support_unchecked")
        results.append(rec)

    total = len(results)
    supported = sum(1 for r in results if r["supported"])
    exists_n = sum(1 for r in results if r["exists"])
    overclaim_n = sum(1 for r in results if r.get("overclaim"))
    rate = (supported / total) if total else None
    return {"n_citations": total, "n_exist": exists_n, "n_supported": supported,
            "overclaim_count": overclaim_n,
            "verification_rate": (round(rate, 3) if rate is not None else None),
            "records": results,
            "n_uncited_answer": total == 0}


def grounding_cap(verification: dict) -> int:
    """Map citation evidence -> a MAX Grounding score (1..5), aligned to the LOCKED rubric anchors
    (rubric.json dimensions[0]): 5 = every claim traced to a verifiable on-point source; 4 = real,
    on-point sources; 3 = main claims cited to real sources and MOSTLY VERIFIABLE, some gaps/loose links;
    2 = few citations, some don't support / can't be verified; 1 = fabricated/nonexistent sources.

    Two distinct signals, NOT collapsed (LB-082 fix):
      * EXISTENCE  (n_exist/total) = the fabrication check. Nonexistent references are what earns cap 1.
      * SUPPORT    (n_supported/total, entailment) = does the real source back the claim.
    A reference that RESOLVES but whose abstract could not be fetched is 'exists but support-unchecked' —
    that is 'mostly verifiable with gaps' (anchor 3), NOT a fabrication (anchor 1). The earlier ladder used
    support alone, so DOI-only citations (no abstract to entail against) scored identically to fabrications
    and pinned real, well-cited answers to cap 2."""
    n = verification["n_citations"]
    if n == 0:
        return 2  # unsupported assertions — nothing to ground against
    exist_rate = (verification.get("n_exist", 0) / n) if n else 0.0
    support_rate = verification.get("verification_rate") or 0.0  # supported / total

    # Fabrication gate first: if references largely DO NOT resolve, this is anchor 1-2 (fabricated/unreal).
    if exist_rate < 0.5:
        return 1
    if exist_rate < 0.8:
        return 2  # a meaningful share don't resolve -> "some can't be verified" (weak)

    # Sources are real (exist_rate >= 0.8). Support (entailment) now lifts the cap within the "real" band.
    # Real + strongly claim-supported -> 5/4; real + partial support -> 3 (anchor: mostly verifiable, gaps);
    # real but little/none of the support could be confirmed (e.g. abstracts unavailable) -> 3 floor, never 1.
    for thr, cap in [(0.9, 5), (0.6, 4), (0.3, 3)]:
        if support_rate >= thr:
            return cap
    return 3  # real on-point sources, support largely unconfirmable -> "partially grounded", not fabricated
