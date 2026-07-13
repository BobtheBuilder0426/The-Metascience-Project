# Reasoning: the line of thought from two papers to one new hypothesis

This document records *how* I arrived at the cytosolic-redox / lactate-threshold hypothesis, including the alternatives I considered and why I set them aside. It is deliberately more exploratory than `result.md`.

## Step 1 — Read both papers for what they actually prove, not what their titles claim

I parsed both PDFs in full (Results + Discussion + Methods outline + reference lists). The essential extracted facts:

**Sprenger (EGT–MPST), young mice**
- Exercise concentrates EGT ~2× in *muscle mitochondria* specifically (not liver/heart), via PGC‑1α → SLC22A4.
- EGT binds mitochondrial MPST (K_D ≈ 3.2 mM by ITC; confirmed by NMR, PISA thermal shift, docking near active-site Cys248 persulfide).
- Mechanistically EGT acts as a persulfide **acceptor** — MPST releases H₂S only with EGT **plus** its substrate 3‑MP; EGT alone yields no H₂S, and no hercynine accumulates → **EGT is recycled, not consumed**.
- EGT diet: +19% distance/h, +28% peak speed, +14% cumulative distance — **all abolished in *Mpst*⁻/⁻**.
- They explicitly *did not* nail down which persulfide acceptor operates in vivo, and note H₂S is hormetic (boosts respiration at low dose, inhibits at high).

**Petrovic (EGT–CSE), worms + rats**
- EGT is an alternative **substrate** for cytosolic CSE (low K_m; consumed → hercynine + H₂S). Opposite chemical fate to Sprenger.
- H₂S drives persulfidation of >300 proteins; the decisive one is **cytosolic GPDH at Cys243**, which raises cGPDH activity ~2×.
- cGPDH is the NAD⁺-generating arm of the G3P shuttle → **muscle NAD⁺/NADH rises**, and **serum + muscle lactate fall** after exercise.
- Aged rats: ~2× time and distance to exhaustion; +muscle mass, +vascularization, +MuSCs. Effects abolished in CSE-null and cGPDH-null models. A 5-day treatment already boosted endurance and serum NAD⁺.

## Step 2 — Notice the tension, and the shared core

The papers look like rivals: different enzyme, different compartment, opposite fate for the EGT molecule, different "headline" output (OXPHOS vs NAD⁺). But they **agree on the effector**: low-level H₂S / sulfane sulfur, acting through the electron transport chain and/or persulfidation. Sprenger even checked CSE thermostability (unchanged in their cells) and Petrovic checked MPST (not a hit in their cells) — so in each system one enzyme dominates, but the *class of mechanism is identical.*

That told me the productive move was **not** to pick a winner between MPST and CSE. It was to ask: *what single physiological quantity would both mechanisms move in the same direction?*

## Step 3 — Find the physiological variable neither paper measured

Here I brought in exercise physiology that sits outside both molecular papers. Endurance running speed at the whole-animal level is governed less by VO₂max alone than by the **lactate threshold** (a.k.a. lactate/anaerobic threshold, OBLA) and running economy. The lactate threshold is set by the balance between pyruvate production and the cell's ability to **re-oxidise cytosolic NADH** so that pyruvate keeps entering mitochondria instead of being reduced to lactate by LDH.

Both EGT mechanisms converge precisely on that balance:
- **CSE route:** persulfidation-activated cGPDH is *literally the cytosolic NAD⁺-regenerating enzyme of the G3P shuttle.* Speeding it clears cytosolic NADH → less substrate for LDH → less lactate.
- **MPST route:** mitochondrial H₂S → SQR donates electrons into CoQ and keeps the matrix NADH sink open, which is what allows the shuttles to keep exporting cytosolic reducing equivalents.

So the *same* running-relevant quantity — the speed at which lactate starts to accumulate — is pushed up by both. And Petrovic's own data (lower lactate at 2× the distance) is a direct, if unremarked, footprint of a lactate-threshold shift.

**The hypothesis therefore is:** EGT's performance benefit is, mechanistically, a **lactate-threshold shift driven by faster cytosolic NADH re-oxidation**, and this is the common denominator of the MPST and CSE stories.

## Step 4 — Stress-test against prior art and against the obvious rival mechanism

A quick literature check confirmed the framing is new and the phenotype is real but mechanistically unsettled:
- EGT was already known to improve rodent aerobic performance / time-to-exhaustion, and earlier work attributed this to **antioxidant / NRF2** activity; a 2026 preprint attributes anti-fatigue to **AMPK/PGC‑1α** and reduced oxidative stress. None proposes a lactate-threshold / cytosolic-redox mechanism. Good — the idea is not already published.
- The **rival mechanism** is "EGT just makes more/better mitochondria (biogenesis, VO₂max)." Two facts argue against biogenesis being *sufficient*: (i) Sprenger showed EGT boosts respiration acutely in cell culture with **no change in OXPHOS subunit levels**, i.e. it is activity, not mass; (ii) Petrovic's 5-day effect and unchanged PGC‑1α/SIRT1 protein argue the fast benefit is **metabolic remodelling, not biogenesis**. My hypothesis is compatible with both observations and makes a *distinguishing* prediction (threshold shift with or without a VO₂max change).

I also had to handle the **hormesis paradox**: if H₂S is the effector, why doesn't more sulfide help without limit? Because high H₂S inhibits complex IV. This is not a weakness — it is a sharp prediction: the benefit should be **biphasic in EGT/H₂S dose**, and should differ between an endogenous enzyme-gated route (supplement) and an exogenous bolus (H₂S gas). Both molecular papers already report the low-dose/high-dose duality, so the caveat is grounded.

## Step 5 — Design the smallest experiment that could falsify it

I wanted one experiment that (a) measures the *specific new variable* (lactate threshold in a running mouse — absent from both papers), and (b) tests *causality through the proposed enzyme*, not just correlation. That yields the 2×2 (diet × enzyme-KO) treadmill lactate-threshold assay in `result.md`. The KO row is the linchpin: it separates the H₂S/persulfidation mechanism from a generic antioxidant explanation, and it connects directly to Sprenger's existing *Mpst*⁻/⁻ result (which showed the *performance* benefit is MPST-dependent but never measured lactate threshold).

I grounded the sample size in the effect sizes the papers themselves report (rather than guessing): even under a conservative assumption (15% threshold shift, 12% CV → d≈1.25), n≈12/group reaches 80% power, so the pilot is small and feasible.

## Alternatives I considered and did not choose as the primary hypothesis

- **"EGT raises VO₂max via mitochondrial biogenesis."** Rejected as *primary* because it doesn't explain the acute (5-day, no-biogenesis) effects or the activity-not-mass respiration data, and it's the incumbent view rather than a new idea.
- **"EGT is fundamentally an antioxidant that protects muscle."** Both papers argue against this (Petrovic shows CSE-dependence and no ferroptosis/4-HNE effect; EGT's redox potential is too mild). My design still tests it, via the KO control.
- **"It's all about NAD⁺ per se (like NR/NMN)."** Close, and Petrovic leans this way — but NAD⁺ is the intermediate, not the performance variable. Framing the endpoint as *cytosolic redox flux → lactate threshold* is more specific, is measurable in a running animal, and explains the lactate drop directly. I treat NAD⁺/NADH as a secondary (mechanistic-bridge) endpoint rather than the headline.
- **A muscle-only vs systemic (erythrocyte/CNS) origin.** Sprenger flags a possible CNS contribution. I kept the pilot muscle-focused for tractability but note this as a later dissection (tissue-specific KO), not the first experiment.

## What would make me abandon the hypothesis
- EGT shifts the lactate threshold *equally* in wild-type and enzyme-KO mice (→ mechanism is not H₂S/persulfidation).
- EGT improves endurance with *no* change in lactate threshold and a clear VO₂max rise instead (→ biogenesis/capacity model wins).
- Muscle NAD⁺/NADH and cGPDH-C243 persulfidation do not move with the performance change (→ the proposed node is not on the causal path).
