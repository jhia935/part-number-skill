---
title: Prokopowicz-Vaskas Equation
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - nasa-nepp-bme-mlcc-reliability.md
  - nasa-time-dependent-ir-2013-prb.md
tags:
  - paper
---

# Prokopowicz-Vaskas Equation

The classic single-failure-mode acceleration equation for predicting MLCC time-to-failure (TTF) under temperature + voltage stress. Originally derived by Prokopowicz and Vaskas (1969) for [[bme-vs-pme|PME (precious-metal electrode)]] MLCCs; widely used as a starting point for BME analysis with the caveat that **BME parts have two failure modes** (catastrophic + slow degradation) so single-mode P-V over-predicts lifetime.

## The equation
$$
\text{AVT} \;=\; \frac{t_1}{t_2} \;=\; \left(\frac{V_2}{V_1}\right)^n \exp\!\left[\frac{E_a}{k}\!\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right]
$$
where:
- `t_1, t_2` = times to failure at stress conditions (V_1, T_1) and (V_2, T_2)
- `n` = voltage acceleration exponent (typical ~ 3 for PME; **measured 4.5 for BME single-mode fits**)
- `E_a` = activation energy (1–2 eV typical PME; **1.6 eV commercial BME, 2.8 eV automotive BME** per [[nasa-time-dependent-ir-2013-prb|Liu PRB 2013]])
- `k` = Boltzmann constant

## Equivalent Weibull-scale form
The same physics expressed as a parameterization of the Weibull scale parameter `η(V, T)`:
$$
\eta(V, T) \;=\; \frac{C}{V^n}\, e^{E_a/kT}
$$

## Derivation sketch (Liu reduction)
[[nasa-time-dependent-ir-2013-prb|Liu (2013 PRB)]] derives P-V from first principles for BaTiO₃ MLCCs:
1. Start from Schottky GB barrier `φ(t) = φ(0)·exp(-2Kt)` with `K = K_0·exp(-E_k/kT)`
2. Combine with the resistivity-current-barrier relationship `ρ(t) ∝ exp(φ(t)/kT)` and the empirical exponential leakage growth `j(t) = j(0)·exp((t-t_0)/τ_SD)`
3. Solve for MTTF under constant applied V
4. Result: `1/MTTF ≈ K_0·exp(-E_k/kT)` — **exactly the temperature-acceleration part of P-V**

So P-V is the **temperature-only Arrhenius reduction** of the full Heywang-Jonker + O-vacancy electromigration model. The voltage acceleration exponent `n` is an empirical fit (because the relationship between V and the kinetic constants K and τ_SD is not pure-Arrhenius at high field).

## Use cases
1. **Lifetime prediction at use level** from accelerated life-test (HALT) data:
   $$
   t_\text{use} \;=\; t_\text{HALT} \cdot \left(\frac{V_\text{HALT}}{V_\text{use}}\right)^n \exp\!\left[\frac{E_a}{k}\!\left(\frac{1}{T_\text{HALT}} - \frac{1}{T_\text{use}}\right)\right]
   $$
2. **Comparing parts**: a part with lower `n` or `E_a` will fail relatively faster at high stress and relatively slower at low stress vs a part with higher exponents (= overall more sensitive to acceleration).
3. **Production screening**: HALT at 2× rated V × max T for 1000 h is the AEC-Q200 operational-life test ([[aec-q200-rev-e-2023]]).

## Failure: BME mixed-mode parts
For modern BME parts, the single-mode P-V **over-predicts** MTTF because the catastrophic mode (defect-driven, exponential in field) and the slow-degradation mode (vacancy-electromigration, exponential in 1/T) have different acceleration factors. Liu's measured discrepancy: predicted 2111 h vs measured 318 h = **6.6× over-prediction** at one specific BME sample condition.

The fix: **two-mode acceleration** ([[bme-reliability-model]] § 5.2):
- Catastrophic (power-law): `η = C/V^n · exp(Ea₁/kT)` — the P-V-style branch
- Slow degradation (exponential): `η = C'·exp(-bE)·exp(Ea₂/kT)`

## Implications for the simulator
- For PME parts, P-V with `n = 3`, `E_a = 1.5 eV` is a reasonable first cut.
- For BME parts, single-mode P-V is only **a conservative upper bound** on MTTF (real lifetime is shorter due to the slow-degradation tail). For accurate prediction, use the two-mode model from `simulator-model.md` § 5.2.

## Cross-references
- [[bme-reliability-model]]
- [[nasa-nepp-bme-mlcc-reliability]]
- [[nasa-time-dependent-ir-2013-prb]]
- [[oxygen-vacancy-migration]]
- [[weibull-distribution]]
- [[bme-vs-pme]]
- [[aec-q200-rev-e-2023]]
