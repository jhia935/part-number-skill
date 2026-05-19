---
title: "NASA / Liu — Time-Dependent IR Degradation in Ni-BaTiO₃ MLCCs (PRB 2013 manuscript)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-time-dependent-ir-2013-prb.md
tags:
  - paper
status: complete
importance: high
---

# NASA / Liu — Time-Dependent IR Degradation in Ni-BaTiO₃ MLCCs (PRB 2013)

**Source:** `resources/literature/nasa-time-dependent-ir-2013-prb.md` (PDF: `resources/literature/pdf/nasa-time-dependent-ir-2013-prb.pdf`)
**Author:** Donhang (David) Liu ([[donhang-liu]]), NASA Goddard / NEPP
**Venue:** Physical Review B manuscript, n275, 2013

## Summary

The **mechanistic foundation paper** for Liu's BME reliability framework. Where the 2013 EEE Parts Bulletin packages the model for engineers, this PRB manuscript derives the **exponential-in-time IR degradation law** from first principles (Heywang-Jonker Schottky double-depletion + oxygen-vacancy electromigration kinetics + first-order reaction theory). Provides explicit experimental fits for two commercial BME MLCCs (BME A automotive-grade, BME B commercial-grade).

## Core derivation

Starting from oxygen vacancy migration rate `dΔn_O/dt = K(t) · [n_s(0) − Δn_O(t)]` (first-order Langmuir-style):
$$
\Delta n_O(t) = n_s(0)\,(1 - e^{-Kt}), \quad K = K_0 \, e^{-E_k/kT}
$$
Substituted into the Schottky barrier:
$$
\phi(t) = \frac{e^2 \, [n_s(0) - \Delta n_O(t)]^2}{8 \varepsilon_0 \varepsilon_r N_d} = \phi(0)\, e^{-2 K t}
$$
And the leakage current grows exponentially with time constant `τ_SD`:
$$
I(t) = I(t_0)\, e^{(t-t_0)/\tau_{SD}}
$$
**Final reduction to Prokopowicz-Vaskas** under constant voltage:
$$
\frac{1}{\text{MTTF}} \approx K_0\, e^{-E_k/kT}
$$

## Measured parameters

Two commercial BME 0.47 µF / 50 V / 0805 parts at constant voltage, varying T:

| Sample | E_k (slope) | Implied E_k (eV) | At T=165°C: MTTF |
|---|---|---|---|
| BME A (automotive) | y = −32.616/T·1000 + 69.53 | **~2.81 eV** | predicts ≥1000 h at rated stress |
| BME B (commercial) | y = −18.727/T·1000 + 39.92 | **~1.61 eV** | 50.5 h at 165°C/72V |

(Both R² > 0.99.)

The automotive-grade part has a **higher activation energy** and thus much slower degradation rate constant K — it's not just faster die qualification, the underlying chemistry is genuinely different.

## τ_SD (exponential growth time of leakage current)
For BME B at 165 °C / 72 V (Table II):
- Range across 20 samples: 1705–2279 min
- Average: ~1850 min
- TTF range: 377–1235 min
- τ_SD / TTF ≈ 1.5–2× (i.e., leakage doubles in about half the time-to-failure)

At first catastrophic failure:
- BME A: 70 % barrier-height reduction (φ(0) → 0.3·φ(0)) at 367 h, 155 °C
- BME B: 55 % barrier-height reduction at 6.3 h, 165 °C

## Implications for the simulator
1. The "exponential growth of leakage" model gives a clean prediction equation: `I(t) = I_0 · exp((t-t_0)/τ_SD)`. Once `τ_SD` is known for a part (or estimated from material activation energy), the time-to-100-µA-leakage failure is predictable.
2. The activation energy **E_k = 1.6–2.8 eV** spread across BME parts of nominally identical spec is the most direct empirical anchor for the "slow degradation" branch of `simulator-model.md` §5.2. For conservative design, use **E_k ≈ 1.6 eV** (the commercial-grade endpoint).
3. The Liu reduction to P-V (Eq. 15) means the same model parameters apply whether you measure τ_SD directly or fit a P-V MTTF curve.

## Concepts discussed
- [[oxygen-vacancy-migration]]
- [[bme-reliability-model]]
- [[core-shell-batio3]]
- [[heywang-jonker-model]]

## Entities mentioned
- [[donhang-liu]]
- [[nasa-nepp]]

## References
_Original source: `resources/literature/nasa-time-dependent-ir-2013-prb.md`_
