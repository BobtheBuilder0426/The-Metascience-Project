<!-- Authored by [CS2] for exp-002 / v8. Research note + the Gate-2 figure-quality checklist. -->
<!-- Feeds the Gate-2 RESULT-PANEL reviewer add-on in driver/CODEX_PANEL.md. Sources S-077..S-082. -->

# Figure & artifact quality — research note + Gate-2 reviewer checklist  [CS2]

**Why this exists.** Operator observation: CS's figures/artifacts read as "AI-sloppy" — overlapping labels, default
look, weak colour, poor readability — not top-journal quality. Task: give the **Gate-2 RESULT-PANEL reviewer** a small,
**non-dominant** add-on so it also critiques figure/artifact *design quality* and tells CS how to lift artifacts to
Nature/Science/Cell + human-designer standards. This note is the research base; Part 3 is the checklist the reviewer
applies. It does **not** replace the `figure-style` skill CS already has — it is the *reviewer's* yardstick for whether
CS applied that craft.

---

## Part 1 — What "top-journal quality" concretely means (the hard specs)

Synthesised from the Nature (S-077), Cell Press (S-078) and Science/AAAS (S-079) author figure guidelines. These are
the *measurable* things a reviewer can check. Where journals differ, the difference is noted — the reviewer should
apply the **spirit** (legible, consistent, accessible), not force one house style, since exp-002 answers aren't being
submitted to a specific journal.

| Dimension | Nature (S-077) | Cell Press (S-078) | Science (S-079) | Reviewer takeaway |
|---|---|---|---|---|
| **Column width** | 89 mm single · 120–136 mm 1.5 · 180–183 mm double (max h 247 mm) | 85 mm single · 174 mm double | 5.5 cm / 1.5 / 18.4 cm | Figures sized to a real print column, not arbitrary; compact, not tall-and-narrow |
| **Body text** | 5–7 pt | ~5–8 pt | (legible at print size) | Text stays legible when the figure is shrunk to column width; nothing microscopic |
| **Panel letters** | 8 pt **bold, lowercase** a,b,c | **UPPERCASE** bold | **UPPERCASE** A,B,C 9 pt bold, upper-left | Panels are labelled, bold, top-left, one consistent case across the figure set |
| **Font** | sans-serif (Helvetica/Arial), same throughout | Avenir (Arial fallback), sans-serif | sans-serif (Myriad) | ONE sans-serif family everywhere; no serif, no font-salad |
| **Colour mode / res** | RGB, 300+ dpi; vector for line art | RGB; 300 colour / 500 b&w / 1000 line-art dpi | 300+ dpi at print size | Crisp at print size; vector (PDF/SVG) preferred for plots/schematics, not blurry PNG |
| **Colour choice** | distinct, comparable visibility; **avoid red/green**; **avoid rainbow**; green+magenta for fluor. | gray fills ≥20% apart (10–80%) | **avoid hues close together**; avoid grayscale + light lines | CVD-safe, few hues, strong value contrast; no red/green pairing, no jet/rainbow |
| **Axes / units** | error bars + exact n in legend | plot **individual data points**, not just mean±error; scale bars | axis = quantity+units+scale; units in parens; SI; powers of 10 | Axes fully labelled with units; show the data distribution, not just a summary bar |
| **Line weights** | — | 0.5–1.5 pt | avoid light lines / screen shading | Strokes heavy enough to survive reduction (≈0.5–1.5 pt) |

**The one-line version:** *sized to a real column · one sans-serif font, nothing below ~5–7 pt · panels labelled bold
top-left · few CVD-safe hues with real contrast (no red/green, no rainbow) · axes labelled with units · data points
shown, not just bars · crisp/vector output · nothing overlapping.*

---

## Part 2 — The design principles behind the specs (why, not just what)

From the two canonical design references + the CVD-palette standard. This is what lets the reviewer explain *why* a fix
helps, in CS's own goal-language (clarity + credibility), rather than reciting rules.

**Bang Wong, *Points of View* (Nature Methods, S-080)** — the practising-designer canon:
- **Salience:** make the ONE important element stand out by varying a single primary feature (colour, size, or
  orientation). If everything is emphasised, nothing is. AI figures often over-emphasise everything.
- **Gestalt + alignment:** group related items by proximity/similarity/enclosure; align elements to invisible guides.
  "Our eyes are acutely aware of small misalignments; compositions that use guides look clean and professional."
- **Negative space is a resource, not waste.** Overcrowded figures are taxing to read. Don't fill every pixel.
- **Simplify:** pull words repeated across labels into a header; use the fewest examples that convey the concept.

**Rougier et al., *Ten Simple Rules for Better Figures* (PLOS Comp Biol, S-081):**
1 know your audience · 2 **one figure = one message** · 3 adapt to the medium · 4 captions are not optional · 5 **do NOT
trust the tool defaults** · 6 use colour effectively (avoid rainbow) · 7 don't mislead (e.g. don't force bar-height
guessing) · 8 avoid chartjunk / maximise data-ink (Tufte) · 9 message trumps beauty · 10 use the right tool.

**Okabe–Ito / Wong CVD-safe palette (S-082)** — the concrete colour fix, matches the `figure-style` skill palette:
`#000000 black · #E69F00 orange · #56B4E9 sky-blue · #009E73 bluish-green · #F0E442 yellow · #0072B2 blue ·
#D55E00 vermillion · #CC79A7 reddish-purple`. Cap categorical hues at ~6; pair colour with shape/position/label (never
colour alone); use perceptually-uniform **viridis/cividis** for continuous data, never jet/rainbow.

**The recurring AI-figure failure modes** (from the matplotlib "why do charts look bad" literature) and their fixes —
this is the "AI slop" the operator flagged, made concrete:

| AI-slop symptom | Fix the reviewer points CS to |
|---|---|
| Dated default look, heavy chartjunk (full box frame, gridlines everywhere) | strip top/right spines, minimal grid, more whitespace, less ink |
| **Overlapping labels / tick text** | rotate/stagger ticks, direct-label lines at their end, `adjustText` or manual offset, widen figure |
| **Overplotted scatter** (dense blob) | transparency (alpha), smaller markers, jitter, 2D-density/hexbin, or facet |
| **Legend covering data / 12-entry legend** | move legend to whitespace or direct-label; cap series; not every line needs a legend row |
| Rainbow/jet colormap; red+green categories | viridis for continuous; Okabe-Ito for categorical; never red/green as the only distinction |
| Too many saturated primary colours | few muted hues, one saturated focal series, comparators desaturated |
| Blurry raster / wrong size | vector (PDF/SVG) or 300+ dpi; set an explicit figure size to a column width |
| Title restates axis; unlabelled units | title = the takeaway; axis carries quantity + units |
| Gratuitous 3D / pie for part-to-whole | 2D with position encoding; bar/dot over pie |

---

## Part 3 — THE GATE-2 FIGURE-QUALITY CHECKLIST (what the reviewer applies)

A compact, actionable yardstick — deliberately short so it stays an **add-on**, not a new dominant axis. The reviewer
walks CS's actual artifacts against these, names what already works (KEEP), then gives **at most 2–3** highest-leverage
fixes, each phrased as a concrete instruction CS can act on. If the artifacts are already clean, the reviewer says so
and moves on — no manufactured nitpicks.

**A. Readability (does it survive being shrunk to a journal column?)**
- [ ] All text legible at print size (nothing below ~5–7 pt equivalent); axis labels, ticks, annotations readable.
- [ ] **No overlapping** text/labels/markers/legend-over-data. Nothing collides or is clipped at the figure edge.
- [ ] One sans-serif font throughout; ≤3 sizes mapped to role (title/label/tick).

**B. Colour & accessibility**
- [ ] CVD-safe: no red/green as the only contrast; no rainbow/jet colormap; viridis/cividis for continuous.
- [ ] Few hues (≤~6 categorical); a clear focal series; comparators lower visual weight; colour reused consistently
      for the same entity across panels.
- [ ] Colour is not the *only* channel — paired with shape/position/label where it carries meaning.

**C. Data integrity & clarity (the science, shown honestly)**
- [ ] Axes labelled with quantity **and units**; sensible scale (powers of 10 / SI for big/small numbers).
- [ ] Distribution shown where relevant (individual points, not just a mean±error bar); n stated; error bars defined.
- [ ] One clear message per figure; title states the takeaway, doesn't just restate the axis.
- [ ] No chartjunk / no misleading encoding (no truncated-axis distortion, no pie for precise comparison, no 3D-for-decoration).

**D. Composition & professionalism**
- [ ] Panels labelled (bold, top-left, consistent case); logical reading order; aligned to a grid; balanced whitespace.
- [ ] Multi-panel figures share axes/scale where comparable; consistent styling across the whole artifact set.
- [ ] Output crisp — vector (PDF/SVG) or ≥300 dpi; sized to a real column width, not arbitrarily tall/narrow.
- [ ] Tables/other artifacts (not just plots): aligned columns, consistent decimals/units, clear headers, no truncation.

**Reviewer discipline (keeps it non-dominant + fair):**
- Figure quality is **ONE small dimension** of the Gate-2 review, after the scientific substance (rigor, completeness,
  correctness). It must never dominate or dilute the science critique.
- **KEEP-first:** name what the artifacts already do well before any fix.
- **Cap at 2–3 fixes**, highest-leverage first; each a concrete, actionable instruction ("move the legend into the
  empty upper-right; switch the 5-colour rainbow to Okabe-Ito; the two overlapping x-labels need rotation"), not vague
  ("make it prettier").
- **Fairness (HOW not WHAT):** critique *presentation/craft only* — never use the figure critique to smuggle a
  different scientific conclusion, a specific number, or a mechanism into CS. Design feedback changes how the result is
  shown, never what the result *is*.
- **Blind-safety:** the improved figure must still read as first-authored — CS applies fixes silently, never captions
  "figure revised after review".

---

## Sources
S-077 Nature figure guidelines · S-078 Cell Press figure guidelines · S-079 Science/AAAS figure guidelines ·
S-080 Wong *Points of View* (Nature Methods) · S-081 Rougier et al. *Ten Simple Rules for Better Figures* (PLOS Comp
Biol, 10.1371/journal.pcbi.1003833) · S-082 Okabe–Ito / Wong CVD-safe palette. Full entries in `/SOURCES.md`.
Complements the loaded `figure-style` skill (the craft CS applies; this note is the reviewer's yardstick for it).
