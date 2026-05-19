---
title: "NASA / CARTS 2012 — Failure Mechanisms in BaTiO₃-Based MLCCs"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-batio3-mlcc-failure-mechanisms.md
tags:
  - paper
status: complete
importance: high
---

# NASA / CARTS 2012 — Failure Mechanisms in BaTiO₃-Based MLCCs

**Source:** `resources/literature/nasa-batio3-mlcc-failure-mechanisms.md` (PDF: `resources/literature/pdf/nasa-batio3-mlcc-failure-mechanisms.pdf`)
**Authors:** David (Donhang) Liu ([[donhang-liu]]) and Michael J. Sampson, NASA Goddard
**Venue:** CARTS International, Las Vegas NV, March 26–29 2012 — **CARTS Outstanding Paper Award**

## Summary

The companion paper to [[nasa-nepp-bme-mlcc-reliability]], focused on **why thinner dielectric layers reduce MLCC lifetime**. Triggered by an Intel 2010 report that MLCC usable life had dropped from "thousands of years" (model prediction) to as low as 5 years as volumetric efficiency increased. Develops the volumetric-efficiency limit (`C/V ≈ ε₀·εr/d²`) and proves it saturates around 3000–4000 µF/cm³ because `εr` collapses with grain size below ~200 nm. Introduces the "early failures" failure mode (β > 1, distinct from infant mortality), identifies them as **extrinsic defect-driven** (avalanche-like breakdown leakage current), and proposes the geometric reliability factor `(1 − (r̄/d)^α)^N`.

## Key tables / numerical results

- **Table I (5-year reliability as function of `Ri` and `N`)**:
  | Ri (5 yr) | N=20 | N=200 | N=500 |
  |---|---|---|---|
  | 0.99999 | 0.99980 | 0.99800 | 0.99501 |
  | 0.99990 | 0.99800 | 0.98020 | 0.95123 |
  | 0.99900 | 0.98019 | 0.81865 | 0.60638 |
  | 0.99000 | 0.81791 | 0.13398 | 0.00657 |
- Figure 2: Volumetric efficiency saturates ~3000 µF/cm³ as `d → 0.5 µm` because `εr` drops with shrinking grain size.

## Implications captured

1. The Intel-reported degradation is real and structural: thinner `d` reduces the margin against defect-feature-size `r`.
2. Reliability per layer must be **astronomically high** to survive the N-amplifier.
3. Modern thin-layer parts (sub-µm `d`, N > 500) need very tight defect control + small `r̄` + careful core-shell engineering.

## Entities mentioned
- [[donhang-liu]]
- [[nasa-nepp]]
- [[intel]] — reported the field issue triggering this study

## Concepts discussed
- [[bme-reliability-model]]
- [[core-shell-batio3]]
- [[mlcc-capacitance-equation]]
- [[batio3]]

## References
_Original source: `resources/literature/nasa-batio3-mlcc-failure-mechanisms.md`_
