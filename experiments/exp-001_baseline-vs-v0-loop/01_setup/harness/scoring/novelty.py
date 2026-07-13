"""novelty.py — literature-distance novelty (creativity-metric.md §2).

Novelty = distance from prior art, computed two ways:
  (1) retrieval-frequency  N_freq = 1/(1+log10(1+hits))   [PRIMARY — robust]
  (2) semantic distance    1 - max_cosine(hyp, nearest neighbours)  [model-dependent]

The worked example (LB-018) showed naive TF-IDF cosine under-discriminates, so the
composite leans on retrieval-frequency and reports semantic distance as a flagged
secondary signal. `retrieval_fn` is injected: real mode wraps a PubMed/OpenAlex
count query; dry-run passes a deterministic stub.
"""
import math


def retrieval_frequency_novelty(hits: int) -> float:
    """0 hits -> 1.0 (nothing like it); thousands -> ~0.2. Monotone decreasing."""
    hits = max(0, int(hits))
    return 1.0 / (1.0 + math.log10(1.0 + hits))


def semantic_distance_novelty(hypothesis: str, neighbours: list) -> dict:
    """1 - max cosine similarity to nearest neighbour. Uses TF-IDF if sklearn is
    present; otherwise a lexical Jaccard fallback. Flagged model-dependent."""
    texts = [t for t in neighbours if t and t.strip()]
    if not texts:
        return {"value": None, "method": "none", "note": "no neighbours"}
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)
        X = vec.fit_transform([hypothesis] + texts)
        sims = cosine_similarity(X[0:1], X[1:]).ravel()
        return {"value": round(1.0 - float(sims.max()), 3), "method": "tfidf_cosine",
                "max_sim": round(float(sims.max()), 3),
                "note": "model-dependent; under-discriminates on shared domain vocab (LB-018)"}
    except Exception:
        def toks(s):
            return set(w for w in "".join(c.lower() if c.isalnum() else " " for c in s).split() if len(w) > 3)
        h = toks(hypothesis)
        best = max((len(h & toks(t)) / max(1, len(h | toks(t))) for t in texts), default=0.0)
        return {"value": round(1.0 - best, 3), "method": "jaccard_fallback",
                "max_sim": round(best, 3), "note": "sklearn unavailable; lexical fallback"}


def novelty_score(hypothesis: str, retrieval_fn, tight_query: str = None) -> dict:
    """Combine retrieval-frequency (primary) + semantic distance (secondary).

    retrieval_fn(query) -> {"hits": int, "neighbours": [str, ...]}
    Returns {novelty, N_freq, hits, semantic, nearest, method}.
    """
    q = tight_query or hypothesis
    r = retrieval_fn(q)
    hits = r.get("hits", 0)
    neigh = r.get("neighbours", []) or []
    nfreq = retrieval_frequency_novelty(hits)
    sem = semantic_distance_novelty(hypothesis, neigh)
    # PRIMARY = retrieval-frequency. Semantic nudges only when it AGREES it's far
    # (both-high => confident-novel); we take a weighted blend favouring N_freq.
    if sem["value"] is None:
        novelty = nfreq
    else:
        novelty = round(0.75 * nfreq + 0.25 * sem["value"], 3)
    return {"novelty": novelty, "N_freq": round(nfreq, 3), "hits": hits,
            "semantic": sem, "n_neighbours": len(neigh),
            "method": "0.75*retrieval_freq + 0.25*semantic_distance"}
