---
title: Dissipation Factor (DF, tan δ)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - psma-ceramic-capacitor-basics.md
  - samsung-cl-series-mlcc-ds.md
tags:
  - paper
---

# Dissipation Factor (DF, tan δ)

The fraction of energy **dissipated as heat** per cycle, relative to the energy stored, when the dielectric is driven by an AC field. The standard datasheet spec for dielectric loss in a capacitor. A capacitor with DF = 0.025 (2.5 %, typical X7R) loses 2.5 % of the cycled energy each cycle.

## Definition
For a complex permittivity ε* = ε' − jε'':
$$
\tan \delta \;=\; \frac{\varepsilon''}{\varepsilon'} \;=\; \frac{1}{\omega R_p C}
$$
where R_p is the equivalent parallel resistance. Equivalent series-circuit form (used by LCR meters):
$$
\tan \delta \;=\; \omega \cdot R_s \cdot C
$$
where R_s is the equivalent series resistance ([[esr-esl-srf|ESR]]) at the measurement frequency.

The angle δ is the **phase difference** from perfect 90° between voltage and current; δ → 0 for an ideal capacitor.

## Typical DF values
| Dielectric | tan δ max (at 25 °C, low field, 1 kHz) |
|---|---|
| **C0G / NP0** | ≤ 0.0015 (0.15 %) |
| **X7R, X5R**: V_r ≥ 25 V | ≤ 0.025 (2.5 %) |
| X7R, X5R: V_r = 16 V | ≤ 0.035 |
| X7R, X5R: V_r = 10 V | ≤ 0.05 |
| X7R, X5R: V_r = 6.3 V | ≤ 0.05–0.10 (depending on capacitance — see [[samsung-cl-series-mlcc-ds]]) |
| **Y5V**: V_r = 6.3 V | ≤ 0.16 (16 %) |

For high-cap parts at low-V, the spec relaxes because DC bias derating already implicit in measurement isn't normalized.

## Measurement conditions
- **C ≤ 1000 pF**: 1 MHz, 0.5–5 V_rms
- **C > 1000 pF, ≤ 10 µF**: 1 kHz, 1.0 ± 0.2 V_rms
- **C > 10 µF**: 120 Hz, 0.5 ± 0.1 V_rms

Class I uses 1 MHz for the small-cap range; Class II uses 1 kHz / 120 Hz. The same part will show very different DF at different test frequencies — vendor datasheets always specify the measurement frequency.

## What drives DF up
1. **Dielectric loss in the bulk**: ferroelectric domain wall hysteresis (dominant in Class II)
2. **Conductive loss**: leakage current through grain interiors and electrodes
3. **Interfacial polarization loss**: space-charge buildup at GBs and electrode interfaces
4. **Mechanical loss**: piezoelectric coupling generating acoustic waves that absorb energy ("singing" capacitors)

## Why Class I has 30× lower DF
[[cazro3|Class I CaZrO₃-based dielectrics]] are paraelectric → no ferroelectric domains → no hysteresis loss. The DF is set only by intrinsic phonon loss and a tiny conductivity contribution. **This is the same reason C0G has no aging and no DC-bias derating** — all three are downstream of the absence of ferroelectric domains.

## Implications for the simulator
- ESR at low frequency: `ESR(f) ≈ tan δ / (ω·C)`
- High-DF parts (Y5V at low V_r) make poor RF / decoupling caps — convert input power to heat.
- DF rises with AC drive amplitude in Class II (domain-wall sweeping more area of the hysteresis loop) — at low-mV AC the DF you measure is the small-signal value; at Volt-range AC the effective DF is higher.

## Cross-references
- [[permittivity]]
- [[esr-esl-srf]]
- [[batio3]]
- [[cazro3]]
- [[ferroelectric-domain-wall]]
- [[eia-rs-198-dielectric-classes]]

## References
- [[psma-ceramic-capacitor-basics]]
- [[samsung-cl-series-mlcc-ds]] (full DF spec tables by V_r and dielectric class)
- [[murata-grm-series-tcc-data]]
