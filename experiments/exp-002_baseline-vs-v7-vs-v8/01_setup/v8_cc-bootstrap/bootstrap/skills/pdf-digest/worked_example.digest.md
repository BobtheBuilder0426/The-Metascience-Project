<!-- WORKED EXAMPLE — the file a pdf-digest subagent produces. This one was made by the real pipeline: render_pdf.py
     rendered all pages, then a reader viewed every page IMAGE (not memory) + the extracted text. Figure entries below
     are interpreted from the rendered figures. This is the quality bar for driver/AL-<name>/context/<file>.digest.md.
     The subject is a NEUTRAL, illustrative demo document (no connection to any real run) so this example can ship in a
     generic bootstrap folder without biasing any research question. -->

# Digest: example_paper.pdf
**Identity:** "Thermal cycling stability of a layered oxide cathode for grid-scale storage" · Demo Author A, Demo Author B ·
*Journal of Illustrative Materials* 12, 88-101 · 2024 · DOI 10.0000/demo.illustrative.2024.0012 · 4 rendered pages
(document states "6 pages"; the shipped render is a 4-page excerpt) · all pages read; both figures viewed as rendered images.
**NOTE:** illustrative demo document — the numbers and citation are fictional, used only to show digest quality.

## Synopsis
Ni-rich layered oxide cathodes (LiNi0.8Mn0.1Co0.1O2) fade under repeated thermal cycling. The paper tests whether a 3 nm
Al2O3 atomic-layer-deposition (ALD) coating suppresses that fade. Coated half-cells retain **92%** capacity after 500
cycles in a 15-45 C window vs **71%** uncoated (Fig. 2a). The benefit tracks a ~4x reduction in post-mortem surface
crack density (Fig. 2b), not a bulk structural change, and is **lost above 60 C** — consistent with ALD-film breakdown.

## Objective
Is thermal-cycling capacity fade in a Ni-rich cathode reducible by a thin protective surface coating, and if so, is the
mechanism surface (crack suppression) rather than bulk, and over what temperature range does it hold?

## Methods
- Cathode LiNi0.8Mn0.1Co0.1O2, 10 mg/cm2 loading; half-cells vs Li metal.
- Coating: 3 nm Al2O3 by ALD (50 cycles); uncoated controls processed identically.
- Cycling: 1C rate; three conditions — 15-45 C window, 15-60 C window, 25 C isothermal control; 500 cycles; n=6 cells/arm.
- Readouts: capacity retention (%), Coulombic efficiency, post-mortem SEM crack density (cracks/100 um2).

## Key results (with anchors)
- Retention @500 cycles, 15-45 C: coated 92 +/- 1.5% vs uncoated 71 +/- 2.2% (Fig. 2a, p.3; abstract p.1; Results p.4).
- Coulombic efficiency >99.5% in both arms → loss is capacity fade, not shuttling (Results p.4).
- Crack density (15-45 C): coated 3.1 vs uncoated 11.8 /100 um2 (~4x); (15-60 C): 9.4 vs 14.2 (Fig. 2b, p.3).
- 25 C isothermal control: both arms behave similarly → benefit is specific to thermal CYCLING, not temperature alone (p.4).
- Benefit abolished >60 C (abstract p.1; Discussion p.4).

## Figures (interpreted from the rendered images)
- **Figure 1 (p.2) — mechanism schematic.** Two cathode particles side by side. LEFT "Uncoated": three dark-red radial
  lines from the centre = grain-boundary cracks; caption "fresh surface exposed". An arrow labelled "ALD coating" points
  right. RIGHT "Al2O3-coated": same particle with an intact red shell ring, no cracks; caption "coating intact / surface
  protected". Message: the coating mechanically constrains the surface and suppresses crack nucleation. Schematic, not to scale.
- **Figure 2 (p.3) — two panels.** (a) Capacity-retention vs cycle number (0-500), two error-bar curves: green circles
  "Al2O3-coated" stay high (100% down to ~92% by cycle 500); orange squares "Uncoated" decline steeply to ~71% by 500 cycles;
  y-axis 60-102%. (b) Bar chart, crack density (/100 um2) for four arms: Coated-15/45C ~3.1 (lowest), Uncoated-15/45C
  ~11.8, Coated-15/60C ~9.4, Uncoated-15/60C ~14.2 (highest); green=coated, orange=uncoated, SD error bars. Together:
  coating raises retention and lowers cracking, with the gap narrowing in the hotter window.

## Limitations (stated by the authors, p.4)
- Half-cell (vs Li) data only; full-cell behaviour may differ.
- n=6 per arm; no independent replication cohort.
- Coating integrity after cycling inferred from crack density, not imaged directly.
- Single coating thickness (3 nm) tested.

## Claims to treat with care
- The >60 C breakdown is attributed to Al2O3 ALD-film failure but film integrity was not measured directly (authors flag this).
- "~4x lower cracking" is the 15-45 C window; the effect is smaller (1.5x) at 15-60 C — don't over-generalise the 4x figure.

## One-line handoff
A 3 nm ALD Al2O3 coating improves Ni-rich cathode thermal-cycling retention (92% vs 71% at 500 cycles) by suppressing
surface cracking in a 15-45 C window, with the benefit lost above 60 C — demonstrated in half-cells, n=6, single thickness.
