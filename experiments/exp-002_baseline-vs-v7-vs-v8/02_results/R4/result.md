# Why does biological aging occur?
### The Reference-Decay Hypothesis — aging as a control-*observability* failure

---

> ## Bottom line
>
> Every somatic cell and tissue runs feedback loops that hold the body at
> "normal." But a loop can only measure the **error between its current state and
> a reference it stores internally** — it has no independent sensor for the *true*
> physiological optimum. So when those stored references slowly drift (from noisy
> turnover of the chromatin/network state that encodes them, plus a directional
> push from growth programs never switched off), the drift is a **common-mode
> error that feedback cannot see** — and is therefore *defended*, not corrected.
> **Aging is the accumulation of confidently-defended reference error.** The
> germline and early embryo escape only because they undergo an external
> re-calibration ("ground-zero" reset). **First experiment:** in a cell where a
> set-point is measurable (e.g. a hypothalamic thermostat or a stem-cell niche),
> show old cells defend a *shifted* reference and that a transient partial reset —
> not a full one — restores youthful function without erasing identity.

---

## The claim in one paragraph

Biological aging is not primarily the accumulation of *damage*, nor the
execution of a *program*. It is the accumulation of **calibration error in
self-referential control loops**. Homeostatic regulation keeps physiological
variables near stored set-points, but the soma has no way to measure whether
those set-points are still *correct* — only whether the current state matches
them. The true optimum is **unobservable** to the machinery that defends it.
Any process that slowly moves the stored reference away from the optimum
therefore produces an error the loop cannot detect and actively protects.
Damage, epigenetic noise, and hyperfunction are the *causes of drift*; the
reason drift becomes permanent decline is that the control system is blind to
it by construction. This reframes aging from "the body wears out / runs a death
program" to "**the body keeps working perfectly — toward a target that is
quietly wrong, and it has no way to know.**"

![Figure 1. The soma controls to references it cannot re-calibrate; reference drift lives in the loop's unobservable subspace.]({{artifact:8d892dd4-7f42-4ad6-88d0-0f8d16a77474}})

## Why this is the right level of explanation

The field has a rich list of *mechanisms* — the twelve hallmarks and their
"expanding universe" (López-Otín et al. 2023) — but hallmarks are a symptom
catalogue, not a cause. The deeper theories each capture one facet: damage
theories name an input; hyperfunction (Blagosklonny; Gems) notes that
early-life programs run on unchecked; the information theory of aging (Yang,
Sinclair et al. 2023) says epigenetic *information* is lost; loss-of-resilience
work (Pyrkov, Fedichev et al. 2021) shows recovery slows with age; the
deleteriome (Gladyshev 2016) sums deleterious changes. **What unifies them is a
control-theoretic fact that none states directly: a feedback system cannot
regulate a quantity it cannot observe.** The optimum the soma "should" hold is
exactly such a quantity. Naming aging as an *observability* failure specifies
what the "lost information" *is* (the calibration of set-points to the true
optimum), why loss is *directional* (developmental bias + entropy both push one
way), and why it is *self-reinforcing* (the controller is built from the same
drifting substrate it defends). Table 1 lays out the unification.

![Table 1. How Reference-Decay unifies existing theories.]({{artifact:e3b76c4b-ea40-4a61-9bb8-d9b21a73b518}})

## The mechanism, precisely

Represent a somatic unit's regulated state as `x`, defended toward a stored
reference `r` by fast feedback, so `x ≈ r`. Fitness depends on the true optimum
`x*` (set by development and physics). The loop's only measurement is the error
`e = x − r`. Crucially, **`x*` never enters `e`.** Two forces move `r`:

1. **Stochastic drift.** The reference is physically stored — chromatin marks,
   transcription-factor network attractors, tissue architecture, matrix
   composition. That substrate turns over noisily, so `r` random-walks. This is
   the microscopic origin of age-related **DNA-methylation drift** and **rising
   cell-to-cell transcriptional variability** (Enge et al.; Martinez-Jimenez et
   al. 2017).
2. **Directional bias.** Growth, anabolic and developmental programs optimal in
   youth are never switched off (the hyperfunction insight), adding a *drift
   term* that pushes `r` consistently in one direction.

Because `e` is blind to `x*`, the loop nulls `x` to a reference that is itself
sliding away from optimal. The organism is **increasingly, confidently wrong.**
A control system with an *external* reference — the germline, checked every
generation against the brutally honest fitness filter of reproduction — does not
drift without bound. This is the formal reason the soma ages and the germline
does not, and why embryogenesis shows a **rejuvenation event to "ground zero"**
(Kerepesi et al. 2021): meiosis and early development *re-derive* the reference
from scratch rather than inheriting the parent's drifted copy.

## A generative model reproduces the core laws of aging

I built the smallest model that encodes the hypothesis and asked whether the
*known quantitative signatures of aging* fall out without being inserted by
hand. References evolve as `dr = b·dt + s·dW` (soma: biased random walk,
unbounded) versus an externally-anchored control `dr = −κ(r−x*)dt + s·dW`
(germline-like, bounded). Physiological deviation is `|r − x*|`; a unit "fails"
past a tolerance; organism hazard rises with the failed fraction. Nothing about
age enters the hazard except through accumulated reference error. Four
independent, non-tuned-for signatures emerge (Figure 2):

- **Gompertz mortality.** Log-hazard rises approximately linearly with age
  (fit R² = 0.94) — the exponential mortality acceleration is an *output*, not
  an assumption.
- **Rising cell-to-cell variance.** Cross-unit variance of the regulated state
  grows monotonically — matching observed transcriptional-noise increase with
  age — while the anchored control stays flat.
- **Loss of resilience / critical slowing down.** When the controller's gain is
  built from the *same* drifting substrate (`κ_eff = κ₀/(1+g·V)`), recovery
  half-time after perturbation grows ~2.3× and the AR(1) autocorrelation climbs
  from 0.75→0.90 across life — the exact resilience-collapse signature reported
  in human blood-marker trajectories, here emergent rather than posited.
- **Soma diverges, germline does not.** Only the self-referential loop's error
  grows without bound.

![Figure 2. Four quantitative signatures of aging emerge from reference decay: Gompertz mortality, rising variance, critical slowing down, and soma-vs-germline divergence.]({{artifact:ee803752-a9ad-4b22-9632-89f79d9d950a}})

## The decisive prediction: partial reset, not repair

Damage theories predict rejuvenation requires *removing damage*. Reference-Decay
predicts something sharper and stranger: because the fault is a *reference
error*, transiently re-anchoring references toward `x*` should rejuvenate — **but
over-resetting is self-defeating**, because a cell's reference is the *sum* of a
legitimate differentiated set-point (its identity) and the accumulated drift. A
reset of depth λ removes a fraction λ of the drift (good) but also a fraction λ
of the identity (bad). In the model I make identity loss a genuine mortality
driver: a unit pushed off its true set-point fails, and — as with a
dedifferentiated or senescent cell — that failure is *absorbing*. The total
deviation from optimum is then `√[(1−λ)²σ²_drift + λ²σ²_id]`, a convex function
with an interior minimum (Figure 3a). **Median lifespan peaks at partial reset
(λ*≈0.4 for well-differentiated cells) and then declines; at full erasure it
falls *below untreated* (66 vs 97 model units).** The optimum shifts toward
zero — and the penalty for over-reset grows — the more strongly differentiated
the cell (Figure 3b), which is exactly why the therapeutic window is narrow.

This is precisely the empirical signature of cellular reprogramming: *transient*
OSKM expression ameliorates aging hallmarks and extends life (Ocampo et al.
2016; Lu et al. 2020), whereas *sustained/complete* reprogramming causes loss of
cell identity, teratomas and death. Damage theories do not naturally predict
this non-monotonic dose–response; a *calibration* theory predicts it as a
theorem. That reprogramming resets **epigenetic age without repairing the
genome** is, under this view, the single most important clue about aging: it
shows the aged state is largely a *recoverable set-point error*, not an
*accumulated-damage floor*.

![Figure 3. Rejuvenation is re-calibration. (a) Reset trades residual drift for identity loss; total deviation from optimum is minimised at an interior depth. (b) Median lifespan peaks at partial reset and falls below untreated at full erasure, with the window narrowing as differentiation strength rises — mirroring transient vs. sustained reprogramming.]({{artifact:86646d75-8aed-436a-8bff-8c6ae42497fd}})

## What the hypothesis predicts (and how to break it)

1. **Old cells defend shifted set-points.** In any system with a measurable
   reference (hypothalamic temperature/energy set-points; stem-cell niche
   signaling; circadian amplitude), old cells should regulate *tightly* around a
   value displaced from young — high control *precision*, wrong *target*.
   **Falsifier:** if aged loops are simply noisier around the *correct* set-point
   (loss of precision, not accuracy), the hypothesis is wrong.
2. **Interventions that supply an external reference beat those that only reduce
   noise.** Heterochronic parabiosis, young-plasma factors, and reprogramming
   (all *re-reference* the cell) should outperform pure antioxidant/damage-repair
   strategies — as observed.
3. **Non-monotonic reprogramming dose–response** with an identity-loss cliff
   (Figure 3) — measurable today by titrating OSKM duration.
4. **Biological age = reference displacement.** Clocks should track *distance of
   the epigenetic state from the developmental optimum*, and partial
   reprogramming should reduce that distance without touching mutation load —
   consistent with epigenetic clocks reversing while genomic damage persists.
5. **Aging rate ∝ drift/anchoring ratio.** Species with stronger somatic
   re-referencing (planaria, hydra, some "negligibly senescent" species) should
   show flat variance-vs-age and non-Gompertz mortality.

## Honest limits

This is a *conceptual/organizing* hypothesis with a supporting toy model, not a
fitted account of any dataset; the model demonstrates *sufficiency* (these
assumptions can generate the laws), not proof. "Reference," "optimum" and
"observability" are defined operationally but will need system-specific
molecular identification to be tested. It does not deny damage — it reframes
damage as one driver of drift. And it inherits the hard measurement problem: `x*`
is unobservable to the soma *and*, for now, largely to us — the research program
is to make it observable. What Reference-Decay buys is a single, falsifiable
sentence that explains why damage isn't repaired, why the same programs persist,
what "lost information" means, why resilience collapses, and why *transient*
rejuvenation works: **the soma ages because it cannot see how far its own
definition of "normal" has drifted from what is actually optimal.**
