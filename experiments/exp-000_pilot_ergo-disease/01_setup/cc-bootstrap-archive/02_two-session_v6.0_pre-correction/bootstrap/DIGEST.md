<!-- METHOD file, referenced by CLAUDE.md INTAKE step 14. This is HOW the bootstrap turns each input file into an
     agent-optimized digest. The heavy reading is done INSIDE Claude Science (it reads PDFs + figures well over the
     mounted folder); the CC orchestrates and saves the result to driver/context/<filename>.digest.md. -->

# DIGEST.md — turn an input file into an agent-optimized digest (every page, every figure)

## Why this exists
If the human hands the run a paper, the loop must **fully understand it** — not skim the abstract. In a
mechanism/methods paper the **figures and schematics often ARE the result** (pathways, dose-responses, knockout
comparisons), so a digest that ignores them is useless. This step produces, for each input file, a structured,
information-complete **digest** the driver can read in seconds instead of re-reading the PDF — and every claim in the
digest is anchored to a location in the source, so it stays checkable (not a free-form summary that can drift; see the
faithfulness evidence in the research note, S-032/S-033).

## Who does the reading
**Claude Science does the heavy reading, the CC orchestrates.** CS natively opens the mounted PDF and can view its
figures (verified in setup step 9 — CS returned the real page count + internal title). The CC does **not** need a local
PDF renderer (that was the v5 blocker). The CC's job here is to (1) tell CS exactly how to read + what to emit, (2)
enforce whole-document coverage, and (3) save CS's output verbatim into `driver/context/`. For a large file, run this as
a **dedicated pass** (a focused CS request, or a subagent) so the full-read discipline isn't interrupted by other work.

## The method (per input file)
1. **Confirm CS can open the file** from the attached folder (it was verified for the channel-check file; confirm for
   each real input): ask CS for the file's page count + title and sanity-check it's the right document.
2. **Force whole-document coverage.** Instruct CS to read **every page in order, start to finish** — not the abstract,
   not a skim. For a long paper, have it work in page ranges and report per range, so nothing is skipped. The digest
   must state the page count and confirm all pages were covered.
3. **Analyze EVERY figure and schematic explicitly.** For each figure/scheme/table: what it shows, the underlying
   data or mechanism it encodes, the key quantitative result (direction + magnitude if given), and why it matters to the
   paper's argument. A figure entry that just repeats the caption is not acceptable — CS must interpret it.
4. **Emit the digest in the schema below** (markdown). Every non-trivial claim carries a **location anchor**
   `(p.N)` or `(Fig.N)` so it can be traced back. Keep it information-DENSE but readable; a digest of a 30-page paper is
   typically 1.5–3 pages.
5. **Save** CS's output verbatim to `driver/context/<original-filename>.digest.md`. Record it in `run_log.md`.

## The prompt to send CS (fill ⟨filename⟩)
> *"Read the file ⟨filename⟩ in the attached workspace folder, cover to cover — every page in order, and every figure,
> scheme, and table. Do not skim or work from the abstract. Then produce a DIGEST in exactly this structure:*
> *1) **Identity** — title, authors, venue, year, DOI, page count, and 'pages covered: 1–N'.*
> *2) **One-paragraph synopsis** — what the paper establishes, in plain language.*
> *3) **Objective / question** the paper addresses.*
> *4) **Methods** — the key experimental systems/assays (models, techniques), 3–8 bullets.*
> *5) **Key findings** — the main results as bullets, each with a location anchor (p.N); include direction + magnitude
>    of effects where stated.*
> *6) **Figures & schematics** — one entry PER figure/scheme/table: 'Fig N: <what it shows> — <the data/mechanism> —
>    <key result> — <why it matters>'. Interpret them; do not just restate captions.*
> *7) **Mechanism / model** — the causal chain the paper argues (A → B → C), stated explicitly.*
> *8) **Limitations & open questions** the paper itself notes or that are evident.*
> *9) **Claims-with-citations** — any claim the paper makes that rests on a specific reference, as
>    {claim → cited ref}, so the driver knows what is this-paper's-result vs borrowed.*
> *Anchor every non-trivial statement with (p.N) or (Fig.N). Be dense and complete; this is the only thing a downstream
> agent will read instead of the paper, so it must lose no load-bearing information. End with `PHASE_COMPLETE` on its own
> line."*

## Digest file schema (what lands in driver/context/<filename>.digest.md)
```
# Digest: <filename>
**Identity:** <title> · <authors> · <venue> <year> · DOI <…> · <N> pages · pages covered: 1–<N>
## Synopsis
<one paragraph>
## Objective
<the question>
## Methods
- <assay/model> …
## Key findings
- <finding> (p.N)
## Figures & schematics
- **Fig 1:** <what> — <data/mechanism> — <result> — <why it matters>
- **Fig 2:** …  (one per figure/scheme/table)
## Mechanism / model
<A → B → C causal chain>
## Limitations & open questions
- <…>
## Claims resting on cited references
- "<claim>" → <ref>
```

## Quality bar / self-check before saving
- **Coverage:** does the digest state the page count and confirm all pages read? Is there a figures section with an
  entry for **every** figure/scheme (count them against the paper)?
- **Interpretation, not transcription:** do figure entries explain the data/mechanism, or just echo captions? (echo = redo)
- **Anchored:** does each key finding carry a (p.N)/(Fig.N)? Unanchored claims are the drift risk — fix them.
- **Honesty:** every detail must come from the actual file. If CS couldn't read a page/figure, the digest says so — it
  never invents a figure that wasn't seen. A fabricated digest is worse than a short honest one.

*(See `context_worked_example.digest.md` in this folder for a filled example on a real paper.)*
