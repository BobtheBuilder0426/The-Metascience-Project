# Best-practice research: PDF→agent-digest capability + multi-model literature-synthesis context
**Date:** 2026-07-10 · **Author:** Claude Science (CS) · **For:** v6 bootstrap redesign (LB-051/052)
**Scope:** Grounded findings for two v6 capabilities, (B) turning a media-heavy PDF into an agent-optimized,
information-complete digest including figures/schematics; and (E) multi-model literature research + fusion into a
concise, high-quality, citation-grounded context report. **E is being researched now but DEFERRED out of the next
tested bootstrap** (operator decision LB-052), it is prepared and shelved as a post-first-success loop optimization.

All DOIs below resolve and were retraction-checked. Citations are inline as clickable links.

---

## Part B, PDF → agent-optimized digest (incl. figure/schematic analysis)

### The problem, concretely
In the v5 pilot the driving CC had **no local PDF renderer** (poppler missing on the Windows/WSL side), so it could not
read the input papers itself and had to lean on Claude Science to read them. For a research loop whose whole premise is
"start from a paper and understand it fully," the agent that plans the work must be able to **ingest the entire
document, every page, every figure and schematic, not just its metadata.** This is a document-understanding problem,
and the field has converged on a few reliable patterns.

### Reading order and figure priority
General-purpose extraction of body text and tables from scientific PDFs is now close to solved by
layout-aware models. [Blecher 2023 (Nougat)](https://doi.org/10.48550/arXiv.2308.13418) converts a scanned or
born-digital academic PDF directly into structured markdown (including math and table structure) with a single
vision encoder–decoder, and open pipelines such as [Wang 2024 (MinerU)](https://doi.org/10.48550/arXiv.2409.18839)
package layout detection, formula and table recognition, and reading-order reconstruction into an end-to-end
"PDF→machine-readable" tool. Layout-aware generative models like
[Wang 2024 (DocLLM)](https://doi.org/10.18653/v1/2024.acl-long.463) show that jointly modelling text **and** spatial
layout beats text-only ingestion for documents where position carries meaning. The practical lesson: **do not scrape
raw text out of a PDF and hope**, use a layout-aware step that preserves structure, or hand the whole document to a
model that natively reads document images.

The harder and more valuable half is **figures and schematics**, which in a methods/mechanism paper often *are* the result. Chart- and figure-understanding is its own active subfield: [Masry 2023
(UniChart)](https://doi.org/10.18653/v1/2023.emnlp-main.906) and [Liu 2023
(MatCha)](https://doi.org/10.18653/v1/2023.acl-long.714) pretrain vision–language models specifically to *read* charts
(recover the underlying data, answer questions, summarize), and the broader problem is surveyed in [Huang 2023,
Automatic Chart Understanding](https://doi.org/10.1109/access.2023.3298050). General multimodal foundation models —
[Alayrac 2022 (Flamingo)](https://doi.org/10.48550/arXiv.2204.14198) and long-context multimodal models like
[Gemini 1.5](https://doi.org/10.48550/arXiv.2403.05530), can interpret an interleaved stream of page images and text,
which is exactly the shape of a scientific paper. For biomedical figures specifically, domain VLMs such as
[Li 2023 (LLaVA-Med)](https://doi.org/10.48550/arXiv.2306.00890) exist, but a strong general multimodal model is
sufficient for our purpose and simpler to rely on.

### The known failure mode to design against
Long-document ingestion + summarization is where models quietly fabricate. Faithfulness, not fluency, is the metric:
[Zhang 2024](https://doi.org/10.1162/tacl_a_00632) benchmarks summarization quality and shows how much
model output can drift from the source, and hallucination is detectable but real at scale
([Farquhar 2024, Nature](https://doi.org/10.1038/s41586-024-07421-0)). The mitigation the literature keeps landing on
is **structured, source-anchored extraction** rather than free-form summary: e.g.
[Dagdelen 2024, Nat Commun](https://doi.org/10.1038/s41467-024-45563-x) extract structured records from scientific text
with an explicit schema. So a digest should be organized around **claims tied to their location in the paper**, not a
prose recap the driver has to trust blindly.

### Recommendation for v6 (given our actual constraints)
Our situation is favourable: **Claude Science already reads PDFs and their figures well** (v5 proved it, CS returned a
paper's true internal title and page count, flagging encoding artifacts, i.e. a genuine full read), the CC/CS channel is a mounted folder, and Codex is available on the CC side. Therefore:

1. **Do the heavy document reading inside Claude Science, driven by the CC**, CS is the component that natively reads
   the mounted PDF end-to-end and can view figures. Don't require a local renderer on the CC/Windows side (that was the v5 blocker).
2. **Force whole-document coverage, page by page and figure by figure.** The digest step must iterate the entire file
   (not "read the abstract + skim"), and must analyze **every figure/schematic**, what it shows, the mechanism/data it
   encodes, and why it matters, because in mechanism papers the figures carry the argument.
3. **Emit a structured, agent-optimized digest file** whose entries are anchored to the source (section/page/figure
   number + the claim), so the driver can use it as fast, trustworthy context without re-reading the PDF, so any claim is checkable. A reader **subagent per document** (spawned by the CC, or run as a dedicated CS session) keeps the
   full-read discipline isolated and repeatable.
4. **Prefer schema-anchored content over free prose** (per the faithfulness evidence): objective/methods/key
   results/figures/limitations/claims-with-locations, plus a short human-readable synopsis.

This becomes the v6 "PDF→digest" capability (plan step 4) and feeds the structured-intake step (plan step 5).

---

## Part E, multi-model literature-synthesis context (DEFERRED; prepared now, shelved for after first success)

### Rationale and the quality bar
Giving the driver a concise, grounded background brief before it starts is a legitimate loop advantage (the AI
Co-Scientist and Robin systems in our starter papers both bootstrap reasoning from a literature-grounded context), and
using two different models (Claude + Codex, or whatever a future user has) exploits genuine diversity: multi-agent
debate/collaboration improves factuality over any single model
([multi-agent LLM agents survey, Wang 2024](https://doi.org/10.1007/s11704-024-40231-1)). **But the operator's quality
bar is the crux:** the brief must not be "old papers all repeating the same tired consensus," or the driver will anchor
on stale, low-quality hypotheses. So the design is dominated by *source selection and grounding*, not by the fusion
step.

### The dominating risk: ungrounded context
LLMs fabricate citations at high rates when unconstrained
([Chelli 2023, Sci Rep](https://doi.org/10.1038/s41598-023-41032-5)), and hallucination in generated text is a
well-catalogued failure ([Zhang 2023, Siren's Song survey](https://doi.org/10.48550/arXiv.2309.01219)). A background
report that invents or misattributes findings injects confident fiction directly into the driver's context, strictly worse than giving it nothing. Two mitigations are established:
- **Retrieval-grounding.** Build the brief from *actually retrieved* sources rather than model memory, the RAG pattern
  ([Gao 2023, RAG survey](https://doi.org/10.48550/arXiv.2312.10997)), which for scientific/medical QA measurably
  improves grounding ([Xiong 2024, benchmarking RAG for medicine](https://doi.org/10.18653/v1/2024.findings-acl.372)).
- **Inline attribution + verification.** Force every claim to carry a citation and verify those citations resolve and
  support the claim, the attributed-generation approach of
  [Gao 2023 (ALCE)](https://doi.org/10.18653/v1/2023.emnlp-main.398), plus a hard DOI-resolution/retraction check (the
  same `verify_dois` discipline used here).

### Source-quality selection (the part the operator emphasized)
To avoid the "countless low-quality journal papers" trap, the retrieval layer must **rank and filter for quality and
recency, not just keyword match**, before any synthesis:
- **Recency-weighted:** bias toward the last ~3–5 years, and always fold in the newest work that extends or contests the
  older anchors (forward citation walk), so the brief reflects the current front rather than the founding consensus.
- **Primary + high-signal venues:** prefer primary research in reputable venues over review-of-reviews; use citation
  velocity and venue as signals but not as the sole filter (highly-cited-only surfaces old generic papers, exactly the
  failure seen in an unfiltered `cited_by_count:desc` sort during this very research session).
- **Diversity/contrarian inclusion:** deliberately include well-supported minority/contrarian findings and flag
  disagreement rather than blending everything into a false consensus (the value of model/source diversity per the
  multi-agent evidence above).
- **Retraction screen:** drop retracted/heavily-corrected papers up front.

### Proposed module shape (to shelve)
1. **Retrieve** a quality-and-recency-filtered source set from the question + input digests (PubMed/OpenAlex/web).
2. **Two independent model passes** (Claude + Codex/other) each write a grounded mini-background from that shared source
   set, each claim cited.
3. **Synthesis agent** fuses the two into **one concise report (~2–4 pages)**, keeping only source-supported claims,
   **flagging where the two models disagree**, and running a citation-verification + retraction pass.
4. **Fairness bookkeeping:** the report is a loop-only advantage the baseline never receives, documented as part of the
   loop method and recorded in the run bundle, so any later "loop beat baseline" claim honestly accounts for it.
5. **Modular + optional + length-capped:** it must never be able to break the core handoff; if it fails or is disabled,
   the driver still runs.

### Decision
**Build and shelve** under `loop-design/future/multimodel-context-module/` (spec + worked example), explicitly **excluded
from the v6 driver handoff package** until one clean end-to-end loop has run (LB-052). Revisit as a measured improvement
category, comparing driver-with-brief vs driver-without against the fixed baseline.

---

## Sources registered (see SOURCES.md for S-numbers)
Nougat; MinerU; DocLLM; UniChart; MatCha; Automatic Chart Understanding review; Flamingo; Gemini 1.5; LLaVA-Med;
structured info extraction (Dagdelen); semantic-entropy hallucination detection (Farquhar); news-summarization
benchmark (Zhang); RAG survey (Gao); RAG-for-medicine benchmark (Xiong); ALCE attributed generation (Gao);
ChatGPT citation fabrication (Chelli); Siren's Song hallucination survey (Zhang); multi-agent LLM agents survey (Wang).
