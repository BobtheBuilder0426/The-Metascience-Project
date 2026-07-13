"""citation_quality.py — citation QUALITY scoring (operator: this is CS's job, not the operator's).

Existence + support live in citations.py. This module scores the *quality* of the citations
an answer leans on, on axes the operator named (LB-029 point 5):
  - amount        : how many distinct citations (too few = thin; contextual, not scored alone)
  - usage         : citations-per-major-claim proxy (are claims actually cited?)
  - venue quality : are sources from strong venues?
  - primary>review: ratio of primary research over reviews (primary preferred)
  - retractions   : any cited work retracted? (hard red flag)

All outputs are numeric so they plot directly for the submission. `metadata_fn` is injected
(dry-run stub / real PubMed+OpenAlex) so this runs offline in tests.

metadata_fn(citation) -> {
   "venue": str|None, "type": "primary"|"review"|"preprint"|"other"|None,
   "retracted": bool, "year": int|None, "venue_rank": float|None  # 0..1 optional prior
}
"""
import re

# A small, transparent venue-quality prior (0..1). Extend as needed; unknown venues -> None
# (scored as neutral, never fabricated). Names matched case-insensitively as substrings.
VENUE_PRIOR = {
    "nature": 1.0, "science": 1.0, "cell": 1.0, "cell metabolism": 0.95,
    "nature medicine": 0.98, "nature aging": 0.95, "nature communications": 0.85,
    "the lancet": 0.98, "new england journal": 1.0, "pnas": 0.9, "elife": 0.85,
    "embo": 0.85, "journal of clinical investigation": 0.9, "aging cell": 0.85,
    "geroscience": 0.8, "plos biology": 0.82, "plos one": 0.6,
    "biorxiv": 0.4, "medrxiv": 0.4, "arxiv": 0.4, "preprint": 0.4,
    "scientific reports": 0.6, "frontiers": 0.55, "mdpi": 0.45,
}


def venue_prior(venue: str):
    if not venue:
        return None
    v = venue.lower()
    best = None
    for name, score in VENUE_PRIOR.items():
        if name in v:
            best = score if best is None else max(best, score)
    return best


def score_citation_quality(citation_records, metadata_fn, n_major_claims=None) -> dict:
    """
    citation_records: the `records` list from citations.verify_citations (each has ["citation"]).
    metadata_fn: injected; returns venue/type/retracted per citation.
    n_major_claims: optional int; if given, usage = min(1, n_cited / n_major_claims).
    """
    per = []
    venues_scored = []
    n_primary = n_review = n_preprint = n_other = n_retracted = 0
    for rec in citation_records:
        c = rec.get("citation", rec)
        md = metadata_fn(c) or {}
        vq = md.get("venue_rank")
        if vq is None:
            vq = venue_prior(md.get("venue"))
        typ = md.get("type")
        if typ == "primary":
            n_primary += 1
        elif typ == "review":
            n_review += 1
        elif typ == "preprint":
            n_preprint += 1
        elif typ:
            n_other += 1
        if md.get("retracted"):
            n_retracted += 1
        if vq is not None:
            venues_scored.append(vq)
        per.append({"citation": c, "venue": md.get("venue"), "type": typ,
                    "retracted": bool(md.get("retracted")), "venue_quality": vq, "year": md.get("year")})

    total = len(per)
    typed = n_primary + n_review + n_preprint + n_other
    primary_ratio = (n_primary / typed) if typed else None
    mean_venue = (round(sum(venues_scored) / len(venues_scored), 3) if venues_scored else None)
    usage = None
    if n_major_claims:
        usage = round(min(1.0, total / max(1, n_major_claims)), 3)

    flags = []
    if n_retracted:
        flags.append(f"cites_{n_retracted}_retracted_work")
    if total and primary_ratio is not None and primary_ratio < 0.34:
        flags.append("mostly_reviews_few_primary")
    if total == 0:
        flags.append("no_citations")

    # A single 0..1 quality composite for convenience (transparent, plottable):
    #   0.5*mean_venue + 0.3*primary_ratio + 0.2*(no retractions) — only over available parts.
    parts, wsum = 0.0, 0.0
    if mean_venue is not None:
        parts += 0.5 * mean_venue; wsum += 0.5
    if primary_ratio is not None:
        parts += 0.3 * primary_ratio; wsum += 0.3
    parts += 0.2 * (0.0 if n_retracted else 1.0); wsum += 0.2
    quality_composite = round(parts / wsum, 3) if wsum else None

    return {
        "n_citations": total,
        "n_primary": n_primary, "n_review": n_review, "n_preprint": n_preprint, "n_other": n_other,
        "n_retracted": n_retracted,
        "primary_ratio": (round(primary_ratio, 3) if primary_ratio is not None else None),
        "mean_venue_quality": mean_venue,
        "usage": usage,
        "quality_composite": quality_composite,
        "flags": flags,
        "per_citation": per,
    }
