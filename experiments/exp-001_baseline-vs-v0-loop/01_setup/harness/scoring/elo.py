"""elo.py — drift-robust pairwise ranking (quantification.md §3, creativity-metric.md §6).

Absolute rubric scores can drift as the judge/model changes across iterations. Elo is
a RELATIVE signal from head-to-head comparisons that survives absolute-scale drift.
`compare_fn(a_text, b_text, question) -> "A" | "B" | "tie"` is injected (a judge call
in real mode, deterministic in dry-run). Order randomized per pair (position-bias, S-008).
"""
import itertools
import random


def _expected(ra, rb):
    return 1.0 / (1.0 + 10 ** ((rb - ra) / 400.0))


def run_tournament(entries: dict, compare_fn, question: str, k: float = 24.0,
                   rounds: int = 1, seed: int = 0) -> dict:
    """
    entries: {name: answer_text}. Round-robin, `rounds` passes, K-factor Elo.
    Returns {ratings, history, n_comparisons}.
    """
    rng = random.Random(seed)
    ratings = {n: 1000.0 for n in entries}
    history = []
    names = list(entries)
    pairs = list(itertools.combinations(names, 2)) * rounds
    rng.shuffle(pairs)
    for a, b in pairs:
        # randomize presentation order to control position bias
        left, right = (a, b) if rng.random() < 0.5 else (b, a)
        verdict = compare_fn(entries[left], entries[right], question)
        if verdict == "A":
            winner, loser = left, right
        elif verdict == "B":
            winner, loser = right, left
        else:
            winner = loser = None
        ra_a, ra_b = ratings[a], ratings[b]
        if winner is None:  # tie
            sa = 0.5
        else:
            sa = 1.0 if winner == a else 0.0
        ea = _expected(ra_a, ra_b)
        ratings[a] = ra_a + k * (sa - ea)
        ratings[b] = ra_b + k * ((1.0 - sa) - (1.0 - ea))
        history.append({"a": a, "b": b, "shown": [left, right], "verdict": verdict})
    return {"ratings": {n: round(r, 1) for n, r in ratings.items()},
            "ranking": sorted(ratings, key=ratings.get, reverse=True),
            "n_comparisons": len(pairs)}
