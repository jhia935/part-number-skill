---
title: Insulation Resistance (IR)
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - samsung-cl-series-mlcc-ds.md
  - nasa-ir-degradation-ni-batio3-2015.md
tags:
  - paper
---

# Insulation Resistance (IR)

The DC resistance of an MLCC measured at rated voltage after a short stabilization time (typically 60–120 s). Specifies how well the dielectric blocks DC current. **Drops with temperature**, **drops over time under DC bias** ([[oxygen-vacancy-migration]]), and **drops with thinning dielectric**.

## Spec convention
Datasheets specify IR as the **smaller of two limits**:
$$
\text{IR}_\text{spec} \;=\; \min\bigl(R_\text{abs}, \;\; (RC)_\text{spec} / C\bigr)
$$
- `R_abs` = absolute resistance floor (e.g., 10 000 MΩ for V_r ≥ 16 V; 1000 MΩ for V_r < 16 V)
- `(RC)_spec` = time-constant floor (e.g., 500 MΩ·µF for V_r ≥ 16 V; 100 MΩ·µF for V_r < 16 V)

So a 10 µF / 25 V part has IR_spec = min(10 000 MΩ, 500 MΩ·µF / 10 µF) = min(10 000, 50) = **50 MΩ**. A 10 nF / 25 V part has IR_spec = min(10 000 MΩ, 500 MΩ·µF / 10 nF) = min(10 000, 50 000) = **10 000 MΩ**. Big caps have lower IR specs because the dielectric has more area (more parallel leakage paths) at the same thickness.

## Measurement
- Apply **rated voltage** for **60–120 s** (different vendors).
- Measure leakage current with high-impedance ammeter.
- IR = V / I.

For [[aec-q200-rev-e-2023|AEC-Q200]] humidity-bias test: rated V + 1.3–1.5 V offset, 100 kΩ series resistor, 1000 h at 85 °C / 85 % RH.

## Why IR matters
- **Standby current draw**: cap leakage adds to system idle current (a fraction of µA per µF for X7R at rated V at 25 °C).
- **Voltage sag / charge retention** for energy-storage or timing applications.
- **Reliability indicator**: rising leakage current is the **earliest sign** of [[oxygen-vacancy-migration|IR degradation]] (well before catastrophic breakdown). Liu uses leakage growth `I(t) = I₀·exp((t−t₀)/τ_SD)` as the primary failure signal in [[nasa-ir-degradation-ni-batio3-2015|HALST]] testing.

## Temperature dependence
Typical for BaTiO₃-based parts: IR **decreases** by ~ 3 orders of magnitude going from 25 °C to 150 °C (Arrhenius-activated thermionic emission over GB Schottky barriers — see [[heywang-jonker-model]]).

[[cazro3|CaZrO₃-based BME C0G]] is the exception: IR actually **rises** beyond 120 °C because the wide-band-gap perovskite has no Curie transition to weaken the GB barrier.

## DC-bias-aging effect on IR
Long-time DC bias gradually lowers IR even at constant T. Mechanism: [[oxygen-vacancy-migration|oxygen vacancies migrate to the cathode-side electrode/GB region]], reducing the Schottky barrier height, increasing leakage current.

## Failure threshold
For high-rel applications:
- **MIL-PRF-123**: failure when IR drops 3–4 orders of magnitude below initial (legacy thick-dielectric parts had high enough initial IR that this was conservative).
- **Modern thin-layer BME**: leakage current = 100 µA fixed threshold (Liu 2015 standard) — because thin-d parts have much lower initial IR, a 3-order drop can leave the cap nominally functional.

## Implications for the simulator
- IR(T, V_DC, t) is the simulator's reliability proxy:
  $$
  \text{IR}(T, V, t) \;=\; \text{IR}_0 \cdot e^{-2 K t} \cdot e^{-E_a/k T}
  $$
  with K from [[nasa-time-dependent-ir-2013-prb|Liu's 2013 PRB derivation]].
- TTF (time to 100 µA leakage) is the standard reliability output.

## Cross-references
- [[oxygen-vacancy-migration]]
- [[heywang-jonker-model]]
- [[bme-reliability-model]]
- [[dc-bias-aging]]
- [[batio3]]
- [[cazro3]]

## References
- [[samsung-cl-series-mlcc-ds]] — IR spec table format
- [[nasa-ir-degradation-ni-batio3-2015]]
- [[nasa-time-dependent-ir-2013-prb]]
- [[aec-q200-rev-e-2023]] — IR + humidity bias test conditions
