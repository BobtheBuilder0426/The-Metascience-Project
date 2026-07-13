#!/usr/bin/env python
"""
run_opus_scoring.py  --  exp-002 blind harness scoring, ALL LLM judges pinned to claude-opus-4-8.

WHY THIS SCRIPT EXISTS (operator ruling 2026-07-12): the CS scoring panel MUST run on Opus, never
Sonnet/Haiku. A first pass mistakenly ran the rubric/creativity/Elo panels on host.reasoning_model()
(= claude-sonnet-5) and the citation-entailment on the kernel default (Haiku-class). Those scores were
discarded. This script re-runs the FULL panel on Opus and bakes in the reliability lessons from that
first pass as hard gates.

RUN IT IN A FRESH CS SESSION (new frame). The first frame hit its 2.0M host.llm per-frame token ceiling
during the wasted Sonnet runs, so no host.llm call can succeed there. A fresh frame = fresh ceiling.
Nothing else needs redoing: the integrity scan + connector_cache.json (0 fabricated citations) are
deterministic API results and are reused as-is, so this script makes ZERO connector calls — every
host.llm call is an Opus judge.

Reliability gates learned from the Sonnet pass (all three failure modes it hit):
  1. reasoning dim came back as PROSE not an integer -> None for 8/9. FIX: strict integer-format coda.
  2. max_tokens empty responses on long answers. FIX: token escalation 8k->16k + retry.
  3. no validation before write. FIX: per-answer parse-gate; a persona that fails to yield 5 integer
     dims is RE-CALLED (up to 3x); nothing is written to disk unless all 5 rubric dims + both
     creativity gates are numeric. Bad answers are reported, never silently Nulled.

Usage (inside a fresh CS python kernel where `host` is available):
    exec(open("run_opus_scoring.py").read())      # then: main(host)
"""
import os, re, json, time, traceback, statistics as stats

OPUS = "claude-opus-4-8"
HERE = os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() else "."
HARNESS = os.path.abspath(os.path.join(HERE, "../../..", "exp-001_baseline-vs-v0-loop/01_setup/harness"))
DIMS5 = ["grounding", "reasoning", "completeness", "usefulness", "creativity"]

_FORMAT_CODA = (
    "\n\nSTRICT OUTPUT CONTRACT (formatting only, does not change what you assess): return ONE JSON object. "
    "The five dimension keys -- grounding, reasoning, completeness, usefulness, creativity -- MUST each be an "
    "INTEGER 1-5 (the SCORE, not prose). Put every justification in the matching *_reason string key "
    "(grounding_reason, reasoning_reason, completeness_reason, usefulness_reason, creativity_reason). "
    "'reasoning' is the integer score for reasoning-quality; 'reasoning_reason' is its sentence. Non-angle delimiters."
)

# LB-098: the creativity panel (run_creativity_panel / _CREATIVITY_SYSTEM) has a DIFFERENT schema than
# the 5-dim rubric panel — it must return plausibility + reasoning_trace (1-5), NOT the rubric dims.
# Appending _FORMAT_CODA to it forced the model to emit the rubric keys instead, so plausibility/
# reasoning_trace came back None -> gates 0.0 -> creativity floored to 1.0 for all 9. This panel-specific
# coda restores the correct contract. Format-only; no rubric/anchor/criterion/model change.
_CREATIVITY_CODA = (
    "\n\nSTRICT OUTPUT CONTRACT (formatting only, does not change what you assess): return ONE JSON object. "
    "The two axis keys -- plausibility, reasoning_trace -- MUST each be an INTEGER 1-5 (the SCORE, not prose). "
    "Put every justification in the matching *_reason string key (plausibility_reason, reasoning_trace_reason). "
    "Also return reasoning_chain_quote (string) and redflags (a JSON list of strings). Do NOT return the rubric "
    "keys grounding/reasoning/completeness/usefulness/creativity here -- this panel scores ONLY plausibility and "
    "reasoning_trace. Non-angle delimiters."
)


def _build_adapter(host, cache):
    import sys
    if HARNESS not in sys.path:
        sys.path.insert(0, HARNESS)
    from adapters import RealAdapters

    class OpusAdapters(RealAdapters):
        MODEL = OPUS
        def __init__(self, host, cache):
            super().__init__(host, reasoning_model=OPUS)
            self.cache = cache; self._qkey = None
        def _llm(self, prompt, system, max_tokens):
            for cap in (max_tokens, max_tokens * 2):
                try:
                    out = self.host.llm({"prompt": prompt, "system": system, "model": OPUS, "max_tokens": cap})
                    txt = out.get("text", "") or ""
                    if txt.strip():
                        return txt
                except Exception as e:
                    if "max_tokens" in str(e) or "empty response" in str(e):
                        continue
                    time.sleep(2)
                    try:
                        out = self.host.llm({"prompt": prompt, "system": system, "model": OPUS, "max_tokens": cap})
                        if (out.get("text") or "").strip():
                            return out["text"]
                    except Exception:
                        pass
            return ""
        # connectors from cache (no LLM)
        def retrieval_fn(self, query):
            nv = self.cache["novelty"].get(self._qkey) if self._qkey else None
            return {"hits": nv["hits"], "neighbours": nv.get("neighbours", [])} if nv else {"hits": 0, "neighbours": []}
        def resolver_fn(self, citation):
            kind = citation.get("kind"); val = str(citation.get("value", "")).strip()
            if kind == "pmid":
                m = self.cache["pmid_meta"].get(val)
                return {"exists": bool(m["exists"]), "title": m.get("title"), "abstract": m.get("abstract")} if m else {"exists": None, "title": None, "abstract": None}
            if kind == "doi":
                m = self.cache["doi_crossref"].get(val) or self.cache["doi_crossref"].get(val.rstrip(').,;]}'))
                return {"exists": m["exists"], "title": m.get("title"), "abstract": m.get("abstract")} if m else {"exists": None, "title": None, "abstract": None}
            return {"exists": None, "title": None, "abstract": None}
        def metadata_fn(self, citation):
            out = {"venue": None, "type": None, "retracted": False, "year": None, "venue_rank": None}
            kind = citation.get("kind"); val = str(citation.get("value", "")).strip(); m = None
            if kind == "pmid": m = self.cache["pmid_meta"].get(val)
            elif kind == "doi": m = self.cache["doi_crossref"].get(val) or self.cache["doi_crossref"].get(val.rstrip(').,;]}'))
            if m and m.get("exists"):
                out.update({"venue": m.get("venue"), "year": m.get("year"), "type": m.get("type"), "retracted": bool(m.get("retracted"))})
            return out
        def dataset_resolver_fn(self, acc, db):
            r = self.cache["dataset"].get(acc)
            return {"exists": None, "used": True} if r is None else {"exists": bool(r.get("exists")), "used": True}
        def trace_recheck_fn(self, step):
            return None
        # LLM judges -- ALL OPUS
        def entailment_fn(self, claim, abstract):
            sys = ("You check scientific citation support. Given a CLAIM and a cited ABSTRACT, answer STRICT "
                   "JSON {supports: true|false, overclaim: true|false, reason: one sentence}. supports=true only "
                   "if the abstract provides evidence for the specific claim. overclaim=true if the abstract is "
                   "on-topic but the claim OVERSTATES its strength or scope (e.g. correlation stated as causation, "
                   "a minor/associative finding stated as a core/causal driver, one study stated as consensus). "
                   "A faithful, appropriately-hedged claim has overclaim=false. Non-angle delimiters.")
            txt = self._llm(f"CLAIM:\n{claim}\n\nABSTRACT:\n{abstract}", sys, 400)
            m = re.search(r"\{.*\}", txt, re.S)
            try:
                return json.loads(m.group(0)) if m else {"supports": False, "overclaim": False, "reason": "unparseable"}
            except Exception:
                return {"supports": False, "overclaim": False, "reason": "unparseable"}
        def make_judge_fn(self):
            # LB-098: route the coda by panel. The creativity panel passes the literal _CREATIVITY_SYSTEM
            # string; the rubric panel passes a persona system. Exact-match so the creativity panel gets the
            # plausibility/reasoning_trace contract, not the 5-rubric-dim one.
            from scoring.judge import _CREATIVITY_SYSTEM
            def jf(prompt, system):
                coda = _CREATIVITY_CODA if system == _CREATIVITY_SYSTEM else _FORMAT_CODA
                return self._llm(prompt + coda, system, 8000)
            return jf
        def make_compare_fn(self):
            def cf(a_text, b_text, question):
                sys = ("Compare two answers to a research question. Which is the more novel-yet-sound, "
                       "better-reasoned hypothesis? Answer STRICT JSON {winner: 'A'|'B'|'tie', reason: one sentence}. "
                       "Non-angle delimiters.")
                txt = self._llm(f"QUESTION:\n{question}\n\nANSWER A:\n{a_text}\n\nANSWER B:\n{b_text}", sys, 2000)
                m = re.search(r"\{.*\}", txt, re.S)
                try:
                    v = json.loads(m.group(0)).get("winner", "tie") if m else "tie"
                    return v if v in ("A", "B", "tie") else "tie"
                except Exception:
                    return "tie"
            return cf
    return OpusAdapters(host, cache)


def main(host, only=None):
    import sys
    if HARNESS not in sys.path:
        sys.path.insert(0, HARNESS)
    import run_scoring
    from scoring import composite as compmod
    W = compmod.load_weights(os.path.join(HARNESS, "rubric.json"))
    cache = json.load(open(os.path.join(HERE, "connector_cache.json")))
    data = json.load(open(os.path.join(HERE, "scoring_input.json")))
    qs = {q["id"]: q for q in data["questions"]}
    ADA = _build_adapter(host, cache)
    SCDIR = os.path.join(HERE, "blind_scores_opus"); os.makedirs(SCDIR, exist_ok=True)

    order = only or [a["code"] for a in data["answers"]]
    for code in order:
        a = [x for x in data["answers"] if x["code"] == code][0]
        q = qs[a["question_id"]]
        ADA._qkey = a["_qkey"]
        t0 = time.time()
        # GATE: score, then verify all 5 dims numeric AND both creativity gates numeric (LB-098);
        # recall the panel up to 3x if not. A None plausibility/reasoning_trace silently zeroes the
        # creativity gate (novelty x 0 x 0 = 0), so it must be caught here, not just the 5 rubric dims.
        attempt, row = 0, None
        while attempt < 3:
            attempt += 1
            row = run_scoring.score_one_answer(a["text"], q["text"], ADA, W,
                                               tight_query=q.get("tight_query"),
                                               process_trace=a["process_trace_normalized"])
            bad = [d for d in DIMS5 if not isinstance(row["dimensions"].get(d), (int, float))]
            cd = row.get("creativity_detail", {})
            crea_gates_bad = [g for g in ("plausibility_gate", "reasoning_trace_gate")
                              if not isinstance(cd.get(g), (int, float))]
            # a gate value of exactly 0.0 for BOTH gates is the schema-failure signature (LB-098):
            # a real answer is not simultaneously zero-plausible and zero-reasoning-trace.
            crea_gates_zeroed = (cd.get("plausibility_gate") == 0.0 and cd.get("reasoning_trace_gate") == 0.0)
            if not bad and not crea_gates_bad and not crea_gates_zeroed:
                break
            print(f"  {code} attempt {attempt}: bad dims {bad} crea_gates_bad={crea_gates_bad} "
                  f"crea_gates_zeroed={crea_gates_zeroed} -> re-scoring", flush=True)
        row["code"] = code; row["question_id"] = a["question_id"]; row["arm"] = code; row["run"] = 1
        row["_qgroup"] = a["_qkey"]; row["_model"] = OPUS; row["_attempts"] = attempt
        row["_dim_parse_bad"] = [d for d in DIMS5 if not isinstance(row["dimensions"].get(d), (int, float))]
        row["_dim_parse_ok"] = (len(row["_dim_parse_bad"]) == 0)
        json.dump(row, open(os.path.join(SCDIR, f"{code}.json"), "w"), indent=1)
        _dimstr = ", ".join("%s=%s" % (d, row["dimensions"].get(d)) for d in DIMS5)
        print(f"{code}: composite={round(row['weighted_composite'],3)} "
              f"dims={{{_dimstr}}} "
              f"ok={row['_dim_parse_ok']} ({time.time()-t0:.0f}s, {attempt} attempt(s))", flush=True)
    print("DONE. scores in", SCDIR)
