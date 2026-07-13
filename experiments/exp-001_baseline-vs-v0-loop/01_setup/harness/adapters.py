"""adapters.py — bind the pure scoring core to the outside world.

TWO adapter sets:
  * dry-run  : deterministic, offline stubs (for CI / dry-run verification)
  * real     : wrap host.llm (Claude reviewer personas) + host.mcp (PubMed/OpenAlex)

The runner picks a set by name. This is the ONLY file that talks to host.* — the
scoring core stays pure + testable.
"""
import re


# ─────────────────────────── DRY-RUN (offline) ───────────────────────────
class DryRunAdapters:
    """Deterministic stubs. No network, no host.*. Same interface as real mode."""

    def __init__(self, canned=None):
        # canned: optional dict to force specific behaviours per answer id
        self.canned = canned or {}

    def retrieval_fn(self, query):
        # deterministic 'hits' from a hash of the query -> stable across runs
        h = abs(hash(query)) % 3000
        neighbours = [f"Prior work on {query.split()[0] if query.split() else 'topic'} ({i})." for i in range(3)]
        return {"hits": h, "neighbours": neighbours}

    def resolver_fn(self, citation):
        # PMIDs of >=8 digits "exist"; author-year "exist"; obviously-fake flagged
        if citation["kind"] == "pmid":
            exists = len(citation["value"]) >= 7 and not citation["value"].startswith("0000")
        elif citation["kind"] == "doi":
            exists = "fake" not in citation["value"].lower()
        else:
            exists = True
        return {"exists": exists,
                "title": f"Stub title for {citation['value']}" if exists else None,
                "abstract": f"Stub abstract mentioning {citation['value']}." if exists else None}

    def entailment_fn(self, claim, abstract):
        # deterministic: 'supports' unless the claim contains 'cure'; 'overclaim' if it contains 'core driver'
        # (lets the dry-run exercise the C2 scope-inflation path, exp-002 C2).
        cl = (claim or "").lower()
        supports = "cure" not in cl
        overclaim = "core driver" in cl
        return {"supports": supports, "overclaim": overclaim, "reason": "stub entailment"}

    def metadata_fn(self, citation):
        # deterministic quality metadata for offline tests.
        val = (citation.get("value") or "").lower()
        kind = citation.get("kind")
        if kind == "pmid" and val.startswith("0000"):
            # the fabricated-PMID trap: nonexistent -> treat as retracted-quality-unknown
            return {"venue": None, "type": None, "retracted": False, "year": None}
        # stable pseudo-assignment from a hash so tests are reproducible
        h = abs(hash(val))
        venue = ["Cell Metabolism", "Nature Aging", "bioRxiv", "PLOS ONE", "Aging Cell"][h % 5]
        typ = ["primary", "primary", "preprint", "primary", "review"][h % 5]
        retracted = (h % 23 == 0)  # rare
        return {"venue": venue, "type": typ, "retracted": retracted, "year": 2020 + (h % 6)}

    def make_judge_fn(self):
        """ONE judge callable jf(prompt, system) used by both panels. Detects whether the
        system prompt asks for the creativity form or the rubric form, and — for the rubric —
        varies scores by which reviewer persona's system prompt it received, so the 3-persona
        jury produces realistic inter-reviewer spread (deterministic, offline)."""
        def jf(prompt, system):
            sys_l = (system or "").lower()
            # creativity form?
            if "plausibility" in sys_l and "reasoning_trace" in sys_l:
                has_chain = bool(re.search(r"premise|prediction|because|therefore|mechanism", prompt, re.I))
                trace = 4 if has_chain else 2
                plaus = 3 + (1 if "established" in prompt.lower() else 0)
                chain = "quoted: premises->mechanism->prediction" if has_chain else None
                rf = '[]' if has_chain else '["no derivable reasoning chain"]'
                return ('{"plausibility": %d, "plausibility_reason": "stub", "reasoning_trace": %d, '
                        '"reasoning_trace_reason": "stub", "reasoning_chain_quote": %s, "redflags": %s}') % (
                            plaus, trace, ('"%s"' % chain) if chain else 'null', rf)
            # rubric form — persona-dependent bias for inter-reviewer spread
            if "rigor" in sys_l or "methods referee" in sys_l:
                bias = -1        # R1 is the hard marker on reasoning/grounding
            elif "significance" in sys_l or "so what" in sys_l:
                bias = 0         # R2 middle
            else:
                bias = 1         # R3 novelty reviewer rewards creative leaps
            n = len(prompt)
            base = 2 + (n // 400) % 3  # 2..4 from answer length
            def s(off):
                return max(1, min(5, base + off + bias))
            return ('{"grounding": %d, "grounding_reason": "stub", "reasoning": %d, '
                    '"reasoning_reason": "stub", "completeness": %d, "completeness_reason": "stub", '
                    '"usefulness": %d, "usefulness_reason": "stub", "creativity": %d, '
                    '"creativity_reason": "stub"}') % (s(0), s(0), s(-1), s(0), s(-1))
        return jf

    def make_compare_fn(self):
        def cf(a_text, b_text, question):
            # longer + more entity-rich answer wins (deterministic)
            from scoring.extract import extract_entities
            na = extract_entities(a_text)["counts"]["total"] + len(a_text) / 500
            nb = extract_entities(b_text)["counts"]["total"] + len(b_text) / 500
            if abs(na - nb) < 0.5:
                return "tie"
            return "A" if na > nb else "B"
        return cf


# ─────────────────────────── REAL (host.llm + host.mcp) ───────────────────────────
class RealAdapters:
    """Wraps host.llm (Claude reviewer personas) and host.mcp connectors.

    NOTE: host.mcp is only callable from the repl tool, and host.llm from the analysis
    kernel — in a real CS run the runner is invoked where `host` is available. `host` is
    injected here. This class contains NO host-specific imports so the module loads
    anywhere; it only CALLS the injected `host`. CS's side is Claude-only by design
    (reviewer-panel-design.md): no cross-vendor judge — self-enhancement is measured vs the operator.
    """

    def __init__(self, host, reasoning_model=None):
        self.host = host
        self.reasoning_model = reasoning_model

    # --- connectors ---
    def retrieval_fn(self, query):
        # count via PubMed search; neighbours via nearest abstracts.
        r = self.host.mcp("pubmed", "search_articles", query=query, max_results=6)
        pmids = [str(p) for p in (r.get("pmids") or [])[:6]]
        neighbours = []
        if pmids:
            det = self.host.mcp("pubmed", "get_article_metadata", pmids=pmids)
            for a in det.get("articles", []):
                t = (a.get("title") or "") + ". " + (a.get("abstract") or "")
                if t.strip():
                    neighbours.append(t[:1200])
        return {"hits": r.get("total_count", 0), "neighbours": neighbours}

    def resolver_fn(self, citation):
        try:
            if citation["kind"] == "pmid":
                det = self.host.mcp("pubmed", "get_article_metadata", pmids=[citation["value"]])
                arts = det.get("articles", [])
                if arts:
                    a = arts[0]
                    return {"exists": True, "title": a.get("title"), "abstract": a.get("abstract")}
                return {"exists": False, "title": None, "abstract": None}
            # DOI / author-year: search OpenAlex by the raw string
            # (kept minimal; real impl can widen). Fall back to 'unresolved'.
            return {"exists": None, "title": None, "abstract": None}
        except Exception as e:
            return {"exists": None, "title": None, "abstract": None, "error": str(e)[:100]}

    def metadata_fn(self, citation):
        """Quality metadata via PubMed (venue/type/pubtypes) with OpenAlex fallback. Best-effort;
        returns None-filled dict on failure (never fabricates)."""
        out = {"venue": None, "type": None, "retracted": False, "year": None, "venue_rank": None}
        try:
            if citation.get("kind") == "pmid":
                det = self.host.mcp("pubmed", "get_article_metadata", pmids=[citation["value"]])
                arts = det.get("articles", [])
                if not arts:
                    return out
                a = arts[0]
                out["venue"] = a.get("journal") or a.get("venue")
                out["year"] = a.get("year") or a.get("pub_year")
                ptypes = [str(p).lower() for p in (a.get("publication_types") or a.get("pubtypes") or [])]
                if any("review" in p for p in ptypes):
                    out["type"] = "review"
                elif any(("journal article" in p or "research" in p) for p in ptypes):
                    out["type"] = "primary"
                if any("retract" in p for p in ptypes):
                    out["retracted"] = True
            elif citation.get("kind") == "doi":
                # OpenAlex by DOI (requires api_key in real runs; injected via env in the CS kernel)
                pass
        except Exception as e:
            out["error"] = str(e)[:100]
        return out

    def entailment_fn(self, claim, abstract):
        # C2 (exp-002 overclaim improvement): also detect OVERCLAIM — the abstract is topical but the claim states MORE than it
        # shows (correlation asserted as causation; a minor/associative finding asserted as a core driver;
        # a single study asserted as established consensus). overclaim is reported independently of supports.
        sys = ("You check scientific citation support. Given a CLAIM and a cited ABSTRACT, answer STRICT "
               "JSON {supports: true|false, overclaim: true|false, reason: one sentence}. supports=true only "
               "if the abstract provides evidence for the specific claim. overclaim=true if the abstract is "
               "on-topic but the claim OVERSTATES its strength or scope (e.g. correlation stated as causation, "
               "a minor/associative finding stated as a core/causal driver, one study stated as consensus). "
               "A faithful, appropriately-hedged claim has overclaim=false. Non-angle delimiters.")
        out = self.host.llm({"prompt": f"CLAIM:\n{claim}\n\nABSTRACT:\n{abstract}", "system": sys,
                             "max_tokens": 200})
        import json
        m = re.search(r"\{.*\}", out.get("text", ""), re.S)
        try:
            return json.loads(m.group(0)) if m else {"supports": False, "overclaim": False, "reason": "unparseable"}
        except Exception:
            return {"supports": False, "overclaim": False, "reason": "unparseable"}

    def make_judge_fn(self):
        """ONE Claude judge callable jf(prompt, system) used by both panels. The persona
        diversity comes from the system prompt judge.py passes (REVIEWER_PERSONAS), not from
        different vendors — CS's side is Claude-only (host.list_models). Self-enhancement is
        measured vs the the operator anchor, not removed by a non-Claude judge."""
        def jf(prompt, system):
            kw = {"prompt": prompt, "system": system, "max_tokens": 500}
            if self.reasoning_model:
                kw["model"] = self.reasoning_model
            return self.host.llm(kw).get("text", "")
        return jf

    def make_compare_fn(self):
        def cf(a_text, b_text, question):
            sys = ("Compare two answers to a research question. Which is the more novel-yet-sound, "
                   "better-reasoned hypothesis? Answer STRICT JSON {winner: 'A'|'B'|'tie', reason: one sentence}. "
                   "Non-angle delimiters.")
            out = self.host.llm({"prompt": f"QUESTION:\n{question}\n\nANSWER A:\n{a_text}\n\nANSWER B:\n{b_text}",
                                 "system": sys, "max_tokens": 150})
            import json
            m = re.search(r"\{.*\}", out.get("text", ""), re.S)
            try:
                v = json.loads(m.group(0)).get("winner", "tie") if m else "tie"
                return v if v in ("A", "B", "tie") else "tie"
            except Exception:
                return "tie"
        return cf
