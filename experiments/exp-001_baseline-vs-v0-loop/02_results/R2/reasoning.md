# Reasoning: how this rationale was reached

This document traces the line of thought from the two papers to the winning hypothesis and the pilot, and states for each novel claim why it is novel and not obvious.

## Step 1 — Extract each paper's exact causal chain, not its headline

Both papers say "EGT → H₂S → better endurance," but through different enzymes in different compartments. Reading each mechanism to the level of transporter → enzyme → chemical product → downstream effector → metabolic output made three things precise:

- In the mouse/MPST axis, EGT is a **sulfur-acceptor that is not consumed** (no hercynine accumulates), and there is **no H₂S from EGT alone** — it needs 3-mercaptopyruvate. So MPST is an *activator target*, not a route that desulfurates EGT.
- In the CSE axis, EGT **is** desulfurated (to hercynine + H₂S), and the benefit runs through persulfidation of cytosolic GPDH-Cys243 → glycerophosphate shuttle → cytosolic NAD⁺.
- Each paper's discovery screen was blind to the other's enzyme (CSE unchanged in the mouse thermal screen; MPST not a target in the worm/rat persulfidation screen).

That last point is the crux: a genuine unifying mechanism cannot be *either* enzyme; it has to be something both screens would have missed.

## Step 2 — Put both enzymes' affinities for EGT on one axis

The decisive move was to compare the two enzymes' affinity for the *same* molecule. This comparison had never been made because the two constants live in two papers, in two different units. Pinning the units down mattered more than any single database query:

- The automatic text layer of the mouse-paper PDF renders the micro sign "µ" as "m". I confirmed this by cropping the individual page glyphs, where the binding constant reads **3.2 µM** and the kinetic constant **2.1 µM**, and where a sentence the text layer gives as "500 mM EGT" visibly reads "500 µM EGT" on the page.
- I did not rely on the glyph read alone. The calorimetry titrated EGT into **27.5 µM** enzyme; that measurement is only physically informative when the ratio [enzyme]/K_D sits between about 1 and 1000. At K_D = 3.2 µM the ratio is ~8.6 (measurable); at 3.2 mM it is ~0.009 (impossible). The biophysics alone rules out the millimolar reading.
- The CSE Km for EGT, **6.6 mM**, is printed in a figure table header and on a plot axis (not corruptible running text) and is internally arithmetic-consistent, so it stands as genuinely millimolar.

The result: **the two effector enzymes read EGT with affinities ~3,000× apart.** Computing fractional velocity at measured muscle EGT concentrations then showed MPST is ~95 % saturated at rest (a switch, +4 % on the diet) while CSE runs at <1 % and scales +255 % with the dietary EGT rise (a rheostat).

**Why this is novel and not obvious:** neither paper reports the other's constant, and neither expresses its own in a way that invites the comparison. The "one molecule, two enzymes, two operating regimes ~3,000× apart" picture is not stated or implied in either paper; it emerges only from placing a micromolar number from one paper next to a millimolar number from the other — after correcting a unit-rendering artifact that would have made both look millimolar and collapsed the partition to ~2×.

## Step 3 — Let the affinity split raise a puzzle, then look for the node that resolves it

If muscle EGT already saturates MPST at rest, why does *more* dietary EGT help? Either free intramitochondrial EGT is far below the whole-tissue average (so MPST is not really saturated), or the dose-responsive benefit is carried by something with lower affinity — CSE, or a node further downstream. This reframed the search: the unifying mechanism should be **downstream** of both enzymes and should be **dose-responsive** even when the high-affinity enzyme is saturated.

## Step 4 — Use expression data to choose the node, and accept the surprise

Both axes terminate in H₂S/sulfane-sulfur. The enzyme that disposes of and harvests H₂S — routing its electrons into the respiratory chain — is SQOR. Rather than assume SQOR mattered in muscle, I pulled GTEx expression for every sulfide-handling enzyme. The result reshaped the hypothesis:

- **SQOR is the only sulfide-handling enzyme more abundant in muscle than in liver** (1.96×).
- **CSE is nearly absent from muscle** (0.04× liver), while MPST is well expressed.

So in muscle the producer is MPST and the disposer/harvester is SQOR; CSE's role is probably systemic, not muscle-intrinsic. Network (STRING) and pathway (Reactome) data confirmed the producer→oxidiser topology, and the H₂S→SQOR→CoQ biochemistry (with its bell-shaped respiration dose-response) supplied the mechanism by which low-level sulfide *raises* respiration.

**Why this is novel and not obvious:** the "obvious" reading of two H₂S-producing papers is that CSE and MPST are the interesting enzymes and H₂S is the shared currency. The expression data invert that intuition — the muscle-relevant enzyme is neither producer but the *oxidiser*, and the cytosolic producer that one paper is built around is barely present in muscle. That is a specific, data-driven constraint that an expert reasoning from the papers alone would not reach.

## Step 5 — State the winning claim so that it is bolder than the easy version

The easy version of a unifying story is "it's all H₂S → SQOR." That is the first thing an expert guesses, and on its own it does not explain the cytosolic NAD⁺ rise or the dietary dose-response (SQOR acts on H₂S, not EGT). The claim was therefore sharpened: SQOR is the muscle node where **both** sulfide axes converge **and** where the parallel glycerophosphate-shuttle route (which persulfidated cGPDH feeds) dumps its electrons — the CoQ pool is the shared sink. The dose-response is supplied upstream by the low-affinity arm and by free-EGT-gated MPST flux. EGT becomes, functionally, a **sulfide-fuel charger for the CoQ pool**.

**Why this is novel and not obvious:** a literature search returned zero reports connecting EGT to SQOR in muscle, zero connecting the MPST and CSE axes into one mechanism, and zero on EGT and the NADH shuttles — against an otherwise active field (dozens of recent EGT-exercise and SQOR-muscle papers). The idea also explains the paradox that stumps the single-enzyme readings: each discovery screen missed the true node because SQOR neither binds EGT (so it is invisible to a binding/thermal screen) nor is a primary persulfidation target (so it is invisible to a persulfidation screen) — it is a downstream electron-transfer enzyme.

## Step 6 — Design the experiment around the one manipulation that separates the ideas

A convergence claim is decisively tested by removing the convergence point. Knocking down SQOR should blunt the EGT benefit regardless of which upstream axis supplied the sulfide, whereas inhibiting MPST or CSE individually should each remove only part of it. That asymmetry — a full block at SQOR, partial blocks at each producer, no effect from inert hercynine, and a rescue by a downstream sulfide donor only when SQOR is present — is the signature that distinguishes the new mechanism from the two published ones. The primary statistical object is the EGT × SQOR interaction, and a pre-stated result (equal EGT benefit with and without SQOR) falsifies the hypothesis outright.

**Why this design is not obvious:** both papers established causality by removing the *producer* (MPST or CSE). Testing the *shared oxidiser* is a different manipulation that neither paper performed, and it is the one that can tell "two independent mechanisms" apart from "two feeds into one node." The isolated-mitochondria EGT-quantitation arm additionally settles the free-vs-total saturation question that the affinity partition raised but cannot itself answer.

## What is proposed vs. established
- **Established (retrieved):** the affinity partition (both constants glyph- and biophysics-verified); the muscle expression pattern; the network/pathway topology; the H₂S→SQOR→CoQ biochemistry and SQOR's activation by H₂S.
- **Proposed (to be tested):** that SQOR is the operative convergence node for the endurance phenotype, and that it is co-loaded with the glycerophosphate shuttle on a shared CoQ sink. These are exactly what the pilot's SQOR-knockdown, CoQ-redox, and cGPDH-persulfidation arms are built to confirm or kill.
