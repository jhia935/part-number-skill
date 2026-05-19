---
title: BME MLCC Reliability Model
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - nasa-nepp-bme-mlcc-reliability.md
  - nasa-batio3-mlcc-failure-mechanisms.md
tags:
  - paper
---

# BME MLCC Reliability Model

The state-of-the-art reliability model for base-metal-electrode ([[bme-vs-pme]]) MLCCs is the framework synthesized by David (Donhang) Liu at NASA Goddard NEPP, summarized in [[nasa-nepp-bme-mlcc-reliability]]. It cleanly separates structure, stress acceleration, and statistical distribution.

## General form
$$
R(t) \;=\; \underbrace{\varphi(N, d, \bar r, S)}_{\text{structure}} \,\times\, \underbrace{AF(V, T)}_{\text{acceleration}} \,\times\, \underbrace{\gamma(t)}_{\text{Weibull}}
$$

### Structure factor `φ(N, d, r̄, S)`
$$
P \;=\; 1 - \left(\tfrac{\bar r}{d}\right)^\alpha \qquad \varphi \;=\; P^N
$$
where `r̄` is the average BaTiO₃ grain size, `d` the dielectric thickness, `N` the active layer count. `α ≈ 6` for V ≤ 50 V, `α ≈ 5` for V > 50 V — fitted from accelerated life-test data on commercial BMEs.

**Key insight — the N amplifier**: Whole-chip reliability is the per-layer reliability raised to the N-th power. Even tiny defects in per-layer reliability are devastating at modern N > 250.

| Per-layer reliability `Ri` (5 yr) | Whole-chip `Rt` at N=20 | N=200 | N=500 |
|---|---|---|---|
| 0.99999 | 0.99980 | 0.99800 | 0.99501 |
| 0.99990 | 0.99800 | 0.98020 | 0.95123 |
| 0.99900 | 0.98019 | 0.81865 | 0.60638 |
| 0.99000 | 0.81791 | 0.13398 | 0.00657 |

(Source: [[nasa-batio3-mlcc-failure-mechanisms]] Table I.)

### Acceleration factor `AF(V, T)`
**PME — single-mode** Prokopowicz–Vaskas:
$$
\frac{t_1}{t_2} = \left(\frac{V_2}{V_1}\right)^n \exp\!\left[\frac{E_a}{k}\!\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]
$$
With `n ≈ 3` and `1 < E_a < 2` eV typical.

**BME — two-mode**: oxygen-vacancy electromigration creates a slow-degradation tail that the PME single-mode model misses.
- **Catastrophic** (power-law): `η(V,T) = C / V^n · exp(Ea₁/kT)`
- **Slow degradation** (exponential field dependence): `η(E,T) = C' · exp(−b·E) · exp(Ea₂/kT)`

### Distribution `γ(t)`
Two-parameter Weibull:
$$
\gamma(t) = e^{-(t/\eta)^\beta} \qquad \text{MTTF} = \eta \cdot \Gamma(1 + 1/\beta)
$$
For β > 3, MTTF ≈ 0.9 η.

## Why grain size matters
Liu shows that MTTF scales as `(d/r̄)^n` when voltage and grain size are both fixed (Eq. 11). The "voltage per grain boundary" is the truly invariant quantity: parts with the same `V/(d/r̄)` have nearly identical MTTF regardless of total `d`. This experimental finding (data courtesy of Murata) is the foundation of the structural factor `(r̄/d)^α`.

## Chip-size effect (small)
Effective single-dielectric-layer area scales by **6.76×** going from 0402 to 0805, and **103×** going to 2220 — see table in [[case-size-geometry]]. The single-layer reliability degrades only modestly: `R_i(xy) = R_i(0402)^S`. Larger chips also use thicker `d`, which compensates for the area increase, so **overall MLCC reliability is roughly chip-size independent**.

## Implications for the simulator
1. The structure factor `(1 − (r̄/d)^α)^N` is a sharp cliff: as `d` approaches `r̄`, reliability falls off precipitously. This sets a hard floor on the achievable `d`.
2. For BME, MTTF projections via P-V alone over-predict lifetime at low voltages. The two-mode model is necessary for accurate consumer-rated parts.
3. The simulator should expose `(N, d, r̄)` as user inputs and surface `R_t(t)` and MTTF as outputs.

## References
- [[nasa-nepp-bme-mlcc-reliability]] (Liu, EEE Parts Bulletin, 2013)
- [[nasa-batio3-mlcc-failure-mechanisms]] (Liu & Sampson, CARTS 2012, Outstanding Paper)
