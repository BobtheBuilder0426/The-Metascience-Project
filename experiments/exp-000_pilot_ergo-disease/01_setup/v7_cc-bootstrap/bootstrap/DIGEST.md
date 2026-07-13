<!-- Referenced by CLAUDE.md INTAKE. The digest CAPABILITY now lives in skills/pdf-digest/ (a CC-side subagent that
     reads the whole PDF itself — every page + every figure — with no dependency on Claude Science or system poppler).
     This file is a short pointer + the digest schema. The full method is skills/pdf-digest/SKILL.md. -->

# DIGEST — turn an input file into an agent-optimized digest (CC-side subagent, every page + every figure)

## The capability lives in the skill
**Use `skills/pdf-digest/SKILL.md`.** At INTAKE, for every PDF the human provides, the blank Claude Code:
1. Runs `skills/pdf-digest/render_pdf.py <file.pdf> <out>` → one PNG per page + full text + manifest. It uses
   **pypdfium2** (a pip wheel with the PDFium engine bundled — NO system poppler; that missing dependency was the v5
   blocker). It pip-installs itself on first use if absent.
2. **Spawns a dedicated reading subagent** whose only job is to open EVERY page image + text, interpret EVERY figure/
   scheme, and write the digest to `driver/AL-<name>/context/<file>.digest.md`. Isolating it in a subagent forces a complete read.

**The reading is done by the CC itself (via its subagent), not by Claude Science.** This is what lets the DRIVER hold
full paper context BEFORE it ever prompts CS. See SKILL.md for the exact subagent brief + fallbacks.

## Why figures are mandatory, not optional
In a mechanism/methods paper the figures and schematics often ARE the result (pathways, dose-responses, knockouts,
structures). A digest that ignores them is useless. The subagent must LOOK at each rendered figure image and interpret
it (data/mechanism/result/why-it-matters), never just echo the caption.

## Digest schema (what the subagent writes to driver/AL-<name>/context/<file>.digest.md)
```
# Digest: <file>
**Identity:** <title> · <authors> · <venue> <year> · DOI <…> · <N> pages · pages covered: 1–<N>
## Synopsis            (one paragraph — what the paper establishes)
## Objective           (the question it addresses)
## Methods             (key systems/assays, 3–8 bullets)
## Key findings        (bullets, each with a (p.N) anchor; direction+magnitude where stated)
## Figures & schematics(one entry PER figure/scheme/table: "Fig N: what — data/mechanism — result — why it matters")
## Mechanism / model   (the causal chain A → B → C, explicit)
## Limitations & open questions
## Claims resting on cited references   ({claim → cited ref})
```
Anchor every non-trivial statement with (p.N) or (Fig.N). Be dense + complete — the digest REPLACES the paper for every
downstream agent. Never invent a figure that wasn't seen; flag any unreadable page.

*(Worked example: `skills/pdf-digest/worked_example.digest.md` — a real digest of a neutral demo paper
(`skills/pdf-digest/example_paper.pdf`, shipped alongside), produced by this exact render→subagent pipeline. It is the
quality bar: every page read, both figures interpreted from the rendered images.)*
