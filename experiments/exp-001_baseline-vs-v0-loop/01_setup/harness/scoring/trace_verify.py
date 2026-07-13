"""trace_verify.py — verify a run bundle's process_trace.json (LB-029 point 4: "did it really happen").

CS badges each provenance step ✓ (verified) or ⚠ (could not verify) in the blinded eval site.
A step is verifiable when it names a checkable action (a connector query with an entity/count,
a cited dataset) that CS can independently re-run. This module produces the per-step verdicts
that make_eval_site.py renders as the CS ✓/⚠ badges.

`recheck_fn` is injected: recheck_fn(step) -> {"ok": bool, "evidence": str} — in real mode it
re-runs the connector query (host.mcp) and compares; dry-run stubs it. Steps that are pure
reasoning are marked "asserted" (not independently checkable, not a failure) unless they claim
a factual lookup.
"""
import re

_CHECKABLE = re.compile(r"connector|pubmed|openalex|uniprot|pdb|geo|ensembl|open targets|dataset|query", re.I)


def verify_trace(trace, recheck_fn=None) -> dict:
    """trace: list of {phase, action, detail, evidence, verified?}.
    Returns per-step verdicts + a summary. Does NOT trust a step's own 'verified' field —
    CS re-derives it (a fabricated self-claim must be caught)."""
    steps = []
    n_ok = n_warn = n_asserted = 0
    for s in (trace or []):
        blob = f"{s.get('action','')} {s.get('detail','')} {s.get('evidence','')}"
        checkable = bool(_CHECKABLE.search(blob))
        verdict, evidence = "asserted", ""
        if checkable:
            if recheck_fn:
                r = recheck_fn(s) or {}
                if r.get("ok"):
                    verdict, evidence = "verified", r.get("evidence", "")
                    n_ok += 1
                else:
                    verdict, evidence = "unverified", r.get("evidence", "could not reproduce")
                    n_warn += 1
            else:
                # no recheck available: a checkable step with concrete evidence is provisionally
                # verified; one with none is unverified.
                if (s.get("evidence") or "").strip():
                    verdict = "verified"; n_ok += 1
                else:
                    verdict = "unverified"; n_warn += 1
        else:
            n_asserted += 1
        steps.append({"phase": s.get("phase"), "action": s.get("action"), "detail": s.get("detail"),
                      "claimed_evidence": s.get("evidence"), "verdict": verdict,
                      "recheck_evidence": evidence, "verified": verdict == "verified"})
    total = len(steps)
    return {"n_steps": total, "n_verified": n_ok, "n_unverified": n_warn, "n_asserted": n_asserted,
            "verified_fraction": (round(n_ok / total, 3) if total else None),
            "any_unverified": n_warn > 0, "steps": steps}
