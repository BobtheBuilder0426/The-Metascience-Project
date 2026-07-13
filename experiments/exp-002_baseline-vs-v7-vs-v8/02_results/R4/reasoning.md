# Reasoning trace — how I got to the Reference-Decay hypothesis

## 1. Framing the target
- Question wants a **novel, plausible, unifying** hypothesis — not a review.
- So the bar is three-fold: (a) *unify* existing theories rather than add a 13th hallmark;
  (b) be *mechanistically precise* enough to model and falsify; (c) be genuinely *novel* — not
  a rename of an existing theory.
- Strategy: map the theory landscape first, find the gap that no existing theory names, build
  the hypothesis on that gap, then stress-test it with a generative model.

## 2. Landscape survey (what already exists)
- **Damage/wear theories** — aging = accumulated molecular damage. Gap: repair capacity
  demonstrably exists (embryo resets; germline is ageless), so *why isn't damage repaired?*
- **Programmed / hyperfunction** (Blagosklonny; Gems & de Magalhães) — early-life programs run
  on unchecked ("quasi-program"). Gap: names a *driver* but not why it's uncorrectable.
- **Disposable soma** (Kirkwood) — resource trade-off. Gap: fails even when resources abundant.
- **Information theory of aging** (Yang/Sinclair 2023; ICE mouse) — loss of *epigenetic
  information*. Strong and close, but "information" is underspecified: *information about what?*
- **Loss of resilience / critical slowing down** (Pyrkov & Fedichev 2021) — recovery time and
  variance diverge with age. Describes dynamics but not the *generating mechanism*.
- **Deleteriome** (Gladyshev 2016) — cumulative deleterious changes. Gap: causal vs bystander.
- **Intercellular competition inevitability** (Nelson & Masel 2017) — competition forces
  cancer-or-senescence. Needs a *fitness reference* to define "worse."
- **Control/systems framings** (Kriete 2013 "toward a control theory analysis"; recent 2025
  control-theory-of-aging & dissipation-theory arXiv preprints) — treat homeostasis as control,
  but focus on *which knobs* or *thermodynamics*, **not observability**.

## 3. The gap nobody names
- Recurring word across the strong theories: **set-point / reference / homeostasis** drifts.
  (Setpoint-drift is even an explicit older idea — Novoseltsev/Yashin.)
- But everyone treats the drift as the *thing to explain*. The unasked question: **why does a
  regulatory system that is *good at correcting errors* fail to correct this one?**
- Control-theory answer, and the core insight: **a feedback loop can only regulate what it can
  observe.** It measures `error = state − stored_reference`. It has **no independent sensor for
  the true optimum.** So drift of the reference itself is in the loop's **unobservable
  subspace** — structurally invisible, hence defended rather than corrected.
- This is the novel move: aging as a **control-*observability* failure**, not a damage,
  program, information, or resilience failure — and it *contains* all of those as facets.

## 4. Why this unifies (the payoff)
- Damage & epigenetic noise → the *stochastic drift* term on the reference.
- Hyperfunction → the *directional bias* term on the reference.
- "Lost information" → precisely the **calibration of set-points to the optimum** (observability).
- Loss of resilience → emerges if controller *gain is built from the drifting substrate*.
- Deleteriome causal subset → changes that hit the stored reference (vs correctable bystanders).
- Germline agelessness & embryonic "ground zero" reset → the germline keeps an **external
  reference** (fitness filter each generation); soma does not.

## 5. Building the model (sufficiency test)
- Minimal encoding: reference `r` per somatic unit; fast feedback makes state `x ≈ r`; fitness
  depends on true optimum `x*`; loop sees only `x − r`. WLOG `x* = 0`.
- Soma: `dr = b·dt + s·dW` (biased random walk → unbounded). Germline control: OU process
  `dr = −κ(r−x*)dt + s·dW` (bounded).
- **Design principle:** put in *only* the mechanism; let the *laws of aging* be outputs. If
  Gompertz, variance rise, and slowing-down have to be hand-tuned, the hypothesis is weak.

## 6. What the model showed (see figures/)
- **Gompertz:** hazard = h0·exp(α·failed_fraction); log-hazard vs age linear, R²=0.94, MRDT≈8 units.
  Exponential mortality *emerged* — never imposed on age.
- **Variance:** cross-unit variance grew linearly; anchored control stayed flat (~0.03 @ end).
- **Critical slowing down:** made gain depend on the drift, `κ_eff = κ₀/(1+g·V)`. Recovery
  half-time rose 2.3×; AR(1) 0.75→0.90. *Emergent*, matching Pyrkov/Fedichev.
- **Soma vs germline:** only self-referential loop diverged.
- Calibration note: first hazard params under-sampled deaths (4% dead); swept θ/α/h0 to a
  realistic regime (median≈105, 96% mortality) before trusting the Gompertz fit.

## 7. The decisive, differentiating prediction
- A *calibration* theory and a *damage* theory diverge sharply on **reprogramming**.
- Damage theory: rejuvenation needs damage removal; more reset = more benefit (monotone).
- Reference-Decay: reset re-anchors references → benefit; but a reset of depth λ also removes
  a fraction λ of the *legitimate* differentiated set-point → identity loss. Predict
  **non-monotonic** dose-response with a hard over-reset cliff.
- Model (honest version): reference = identity set-point + drift; reset removes fraction λ of
  *both*. Deviation from optimum = √[(1−λ)²σ²_drift + λ²σ²_id] (convex, interior minimum).
  Identity loss is made a real mortality driver and failure is **absorbing** (a dedifferentiated
  cell doesn't spontaneously re-specify). **Median lifespan peaks at interior λ*≈0.4 and
  declines; at full erasure it falls BELOW untreated (66 vs 97).** Window narrows as
  differentiation strength σ_id rises.
- Correction note: an earlier draft asserted "full erasure kills" while the then-model actually
  plateaued at the sim ceiling with still-positive benefit (an abstract λ² cost bolted on, later
  washed out by post-reset drift). Rebuilt so the decline is genuinely emergent from mortality;
  claim now matches the data.
- This matches the actual biology exactly: *transient* OSKM rejuvenates (Ocampo 2016; Lu 2020);
  *sustained/complete* reprogramming → teratoma/identity loss/death. Damage theory doesn't
  predict the cliff; calibration theory predicts it as a theorem. Strong novelty + testability.
- Memory note: long-horizon intervention run OOM-killed the kernel at 3000×200×221 float64;
  re-ran in float32 with a streaming failed-fraction computation (no 3-D copy) → clean.

## 8. Falsifiers I deliberately built in
- If aged loops are *noisier around the correct set-point* (lose precision, keep accuracy) →
  hypothesis wrong (it predicts tight control around a *displaced* set-point).
- If damage-repair-only interventions match re-referencing interventions → weakens it.
- If reprogramming dose-response is monotone with no identity cliff → weakens it.
- If negligibly-senescent species still show rising variance & Gompertz mortality → weakens it.

## 9. Honesty checks
- This is an organizing hypothesis + sufficiency model, not a data fit. Stated as such.
- `x*` unobservable to the soma *and* (currently) to us — flagged as the central hard problem
  and the actual research program (make the optimum observable).
- Does not deny damage; reframes its role.
