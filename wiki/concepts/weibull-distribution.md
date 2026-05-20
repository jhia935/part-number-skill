---
title: Weibull Distribution (Reliability)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - nasa-nepp-bme-mlcc-reliability.md
tags:
  - paper
---

# Weibull Distribution

The default statistical distribution for MLCC time-to-failure (TTF) data. Two-parameter form:
$$
R(t) \;=\; \exp\!\left[ - \left(\tfrac{t}{\eta}\right)^{\beta} \right]
$$
- `R(t)` = reliability (probability of survival past time t)
- `η` = **scale parameter** = time at which 63.2 % of the population has failed (related to MTTF)
- `β` = **shape parameter** (dimensionless) — characterizes the **type** of failure mode

## What β tells you
| β | Failure mode interpretation |
|---|---|
| < 1 | **Infant mortality** — failure rate decreases with time. Manufacturing defects screened out. |
| = 1 | **Random / memoryless** failures (exponential distribution). External cause, e.g., ESD. |
| > 1 | **Wear-out** failures. Failure rate increases with time. Intrinsic degradation. |
| 3–7 | Typical for MLCC catastrophic breakdown. |
| > 10 | Very tight failure-time distribution; usually one dominant deterministic mechanism. |

## MTTF (mean time to failure)
$$
\text{MTTF} \;=\; \eta \cdot \Gamma\!\left(1 + \tfrac{1}{\beta}\right) \;\approx\; 0.9\,\eta \quad (\text{for } \beta > 3)
$$
where Γ is the gamma function. For most MLCC analyses, MTTF ≈ η to within 10 %.

## Standard fitting approach
1. Run N samples under stress, record TTF for each (the time leakage exceeds 100 µA, or insulation resistance drops below threshold).
2. Sort TTF ascending, assign cumulative probability `F_i = (i − 0.3)/(N + 0.4)` (median rank approximation).
3. Plot `ln(ln(1/(1 − F)))` vs `ln(TTF)`. A straight line indicates Weibull-distributed data.
4. Slope of the line = β; intercept gives η.

For BME parts with [[bme-reliability-model|mixed failure modes]], the data don't fit a single straight line — you have to classify each unit's failure mode (catastrophic vs slow degradation) and fit each subset separately.

## Why Weibull (and not exponential or normal)
- Failure of an MLCC happens when **any** of N dielectric layers fails (weakest-link statistics). Weibull is the natural distribution for weakest-link extreme-value problems.
- Empirically, BME MLCC TTF data fit Weibull better than log-normal or normal.
- The shape parameter β has a direct physical interpretation that other distributions lack.

## "Early failures" with β > 1
A counterintuitive observation by [[donhang-liu|Liu]]: in modern thin-layer BME parts, **some failures appear early** (well before the expected wear-out time) but have **β > 1** when isolated and replotted. These are **not** infant-mortality defects — they're **extrinsic-defect-driven** catastrophic failures (a pore or impurity right at the wrong place) but the population is large enough to support a Weibull fit. This is why [[nasa-batio3-mlcc-failure-mechanisms|the 2012 CARTS paper]] argued for the structural reliability factor `(1 − (r̄/d)^α)^N`.

## Implications for the simulator
- Reliability output: simulator gives `R(t)` curve (or equivalently the Weibull η and β).
- MTTF from η is the headline number for system-level lifetime estimates.
- For BME mixed-mode predictions, output **two** Weibull pairs (catastrophic, slow-degradation) and a mixing fraction `p` — the full form in `simulator-model.md` § 5.2.

## Cross-references
- [[bme-reliability-model]]
- [[prokopowicz-vaskas-equation]]
- [[nasa-nepp-bme-mlcc-reliability]]
- [[nasa-batio3-mlcc-failure-mechanisms]]
- [[insulation-resistance]]
