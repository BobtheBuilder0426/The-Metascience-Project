# Figure manifest — The Metascience Project

Complete figure set for the submission report (paper) and talk. Every figure
authored in **SVG** (master), exported to **PNG + PDF at ≥300 dpi**. Every mark
traces to `derived_numbers.json` / `exp002_master_3arm.csv`; claim IDs below
reference `evidence_spine.csv`.

## Locked visual code (learn once, reused in every figure)
| Encoding | Meaning |
|---|---|
| **black** | Baseline (blank Claude Science) — neutral reference |
| **sky-blue** | v7 loop (intermediate) |
| **blue** | v8 loop (focal / matured design) |
| **bluish-green** | v9 loop (exp-003) |
| **orange** | delta / win / highlight call-outs only |
| ● circle | CS-harness panel · ▲ triangle Human expert · ◆ diamond Combined (**derived**) |

Colour = arm (deeper blue = better loop). Scorer = marker **shape**, never a competing hue.
The **combined** score is the per-dimension mean of the two scorer streams — a *derived summary*,
never a third independent judge or replicate. The two streams are the automated CS-harness panel
and a single human expert; there are 3 questions per arm (n = 3).

## Paper schematics (conceptual — no data marks)
| Fig | Takeaway title | Evidence-spine claims |
|---|---|---|
| **P-S1** | A human uses one AI to discover how to make that AI do better science | P01, P03 |
| **P-S2** | exp-002 scores three loop versions blind: two scorer streams, two-key unblinding | E201, E213 |
| **P-S3** | Each loop version adds a cumulative bundle to the previous one — v7→v8→v9 | V01, V02, V03, V04 |

## Paper data figures
| Fig | Takeaway title | Evidence-spine claims | Key numbers |
|---|---|---|---|
| **P-D1** (KEY) | The v8 loop scores highest with every scorer stream | E202, E203, E204 | CS 3.85/4.00/4.17 · Human 2.75/2.67/3.25 · Combined 3.30/3.33/3.71 |
| **P-D2** | The v8 upgrade improved every question for every scorer; the v7 step did not | E205, E206 | Δ(v8−v7) positive 9/9 · Δ(v7−baseline) straddles 0 |
| **P-D3** (INCLUDED) | The v8 gain over v7 is most consistent in creativity and human-scored reasoning | E207 | CS creativity +0.43 (3/3) · human reasoning +1.00 (3/3) |

## exp-003 graphical abstract
| Fig | Takeaway title | Evidence-spine claims |
|---|---|---|
| **P-E1** | Identical data + question, two research paths — open comparison, no winner | E301, E302, E303, E305, E306, E307 |

## Talk figures (16:9, big type, one message per slide)
| Fig | Takeaway title | Source | Evidence-spine claims |
|---|---|---|---|
| **T1** | One AI is used to make that same AI do better science | P-S1 | P01, P03 |
| **T2** | Every answer is scored blind by two scorer streams | P-S2 | E201, E213 |
| **T3** | The v8 loop adds three review steps on top of v7 | new (v8 focus) | V02, V03 |
| **T4** | With every scorer stream, the v8 loop scores highest | P-D1 | E202, E203, E204 |
| **T5** | Same start, two different answers — an open comparison, no winner | P-E1 | E301, E302, E303, E305, E307 |

## Honest-scope notes (carried in captions, not hidden)
- **n = 3 questions → underpowered by construction.** Figures report direction and
  sign-consistency of within-question deltas, NOT powered significance. Friedman p is
  in `derived_numbers.json` for completeness only (E210).
- **The gain is v8-specific.** v7 did not reliably beat baseline (P-D2 right panel, E206).
- **Q2 ("why does aging happen") was won by baseline** — visible as the baseline outlier /
  negative v8−baseline point; not smoothed away (E209).
- **exp-003 is a showcase, not a measured win** — n=1 per arm, not scored, not blinded,
  claims as reported by each arm and not independently re-verified (E306, E307).
- **Combined is derived**, labelled as such everywhere it appears (E213).

## Files
Each figure ships as `<id>_<slug>.svg` + `.png` + `.pdf`. Companion notes:
`FIGURE_MANIFEST.csv` (this table, machine-readable) and `TALK_FIGURE_PRINCIPLES.md`.
