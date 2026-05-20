---
title: ESR, ESL, and Self-Resonant Frequency
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - kyocera-avx-esr-esl-decoupling.md
  - psma-ceramic-capacitor-basics.md
  - murata-grm-series-tcc-data.md
tags:
  - paper
---

# ESR, ESL, and Self-Resonant Frequency

A real MLCC is an RLC series network — capacitance with parasitic resistance (ESR) and inductance (ESL). The equivalent circuit and its magnitude:

$$
Z(\omega) \;=\; \sqrt{\text{ESR}^2 + \big(\omega L_\text{ESL} - 1/\omega C\big)^2}
$$

(Source: [[kyocera-avx-esr-esl-decoupling]] Eq. 1.)

## Self-resonant frequency (SRF)
At SRF the capacitive and inductive reactances cancel; total impedance equals ESR (its minimum).
$$
f_\text{SRF} \;=\; \frac{1}{2\pi\sqrt{L_\text{ESL}\cdot C}}
$$
Above SRF the part behaves as an **inductor**.

| Part | Typical SRF |
|---|---|
| 10 µF · 0.5 nH ESL MLCC | ~7 MHz |
| 100 nF · 0.5 nH ESL MLCC | ~22 MHz |
| 10 nF · 0.5 nH ESL MLCC | ~70 MHz |
| 100 µF aluminum electrolytic · 15 nH | ~400 kHz |

## ESR breakdown
Two contributions, dominant in different frequency bands:
- **Dielectric loss** (below SRF): `R_d = tan δ / (ω·C)`. For X7R, `tan δ` ≈ 0.025; for C0G, ≤ 0.0015.
- **Electrode resistance** (above SRF and around minimum): determined by inner-electrode metallurgy, electrode thickness, current path length.

[[psma-ceramic-capacitor-basics]] shows the bulk resistivity ordering: **Cu-BME < Ni-BME < Pd-PME < Ag-PME** for inner electrodes — which is why high-Q RF MLCCs use Cu-BME ([[bme-vs-pme]]).

## ESL geometry
ESL is the inductance of the current loop through the part, terminations, and PCB pads. It depends mostly on **geometry**, weakly on material.

| Construction | Typical ESL |
|---|---|
| Standard 0402 X7R | 0.5–1.0 nH |
| Reverse-geometry (0306, 0204 — long side at the terminal) | 0.2–0.5 nH |
| LICC (low-inductance chip caps, interdigitated 8-terminal) | 0.1–0.3 nH |
| Through-hole leaded ceramic | 5–10 nH |

## Decoupling design rule of thumb
For a digital decoupling cap to keep up with switching transients, [[kyocera-avx-esr-esl-decoupling]] recommends:
$$
\frac{1}{\text{ESR}\cdot C} \gtrsim f_\text{operating}
$$
i.e., the RC time constant must be **shorter** than the switching period.

Adding capacitance does not always reduce ripple — at fixed ESR, the ESR sets the floor. To beat ESR-limited ripple, parallel multiple lower-ESR parts.

## Implications for the simulator
1. The simulator outputs `Z(f)` over the full frequency range, with SRF marked.
2. ESR is decomposed into a frequency-dependent dielectric-loss term and a frequency-flat electrode term. Vendor curves are fit to a 4-element transmission-line-like model for better accuracy ([Equivalent-Circuit Model for High-Capacitance MLCC](https://www.researchgate.net/publication/254059571_Equivalent-Circuit_Model_for_High-Capacitance_MLCC_Based_on_Transmission-Line_Theory)).
3. ESL is mostly a function of case-size + termination geometry — the simulator gets it from a small lookup table keyed by case + construction (standard / reverse / LICC).

## References
- [[kyocera-avx-esr-esl-decoupling]]
- [[psma-ceramic-capacitor-basics]]
- [[murata-grm-series-tcc-data]]
