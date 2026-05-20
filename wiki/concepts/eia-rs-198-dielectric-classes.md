---
title: EIA RS-198 Dielectric Classes
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - psma-ceramic-capacitor-basics.md
  - samsung-cl-series-mlcc-ds.md
tags:
  - paper
---

# EIA RS-198 Dielectric Classes

The EIA RS-198 standard (also tracked by IEC 60384-9/-22) names MLCC dielectric materials with three-character codes that fully specify temperature behavior. The code differs between **Class I** (linear) and **Class II/III** (ferroelectric).

## Class I — significant figure × multiplier × tolerance
Used for **paraelectric** dielectrics (e.g., CaZrO₃-based). Linear, low-loss, no aging, no DC-bias derating. Trade-off: low `εr` (20–100), low capacitance density.

| 1st (figure) | TCC sig. fig. | 2nd (digit) | TCC multiplier | 3rd (letter) | TCC tolerance (ppm/°C) |
|---|---|---|---|---|---|
| C | 0.0 | 0 | −1     | G | ±30 |
| B | 0.3 | 1 | −10    | H | ±60 |
| L | 0.8 | 2 | −100   | J | ±120 |
| A | 0.9 | 3 | −1000  | K | ±250 |
| M | 1.0 | 4 | −10 000 | L | ±500 |
| P | 1.5 | 5 | +1     | M | ±1000 |
| R | 2.2 | 6 | +10    | N | ±2500 |
| S | 3.3 | 7 | +100   |   |  |
| T | 4.7 | 8 | +1000  |   |  |
| U | 7.5 | 9 | +10 000 |   |  |

Examples:
- `C0G` = 0 ppm/°C × −1, ±30 ppm/°C — the canonical ultra-stable C0G / NP0 ([[cazro3]]-based in modern BME)
- `U2J` = 7.5 × −100 = −750 ppm/°C, ±120
- `P2H` = 1.5 × −100 = −150 ppm/°C, ±60

Temperature range: **−55 °C to +125 °C**.

## Class II / III — temperature range + max ΔC
Used for **ferroelectric** [[batio3]]-based dielectrics. High `εr` (600–18 000), but nonlinear (DC-bias derating, [[aging-class-2]], TCC bigger than ppm).

| 1st letter (T_low) | 2nd digit (T_high) | 3rd letter (max ΔC%) |
|---|---|---|
| X = −55 °C | 4 = +65 °C  | A = ±1.0 |
| Y = −30 °C | 5 = +85 °C  | B = ±1.5 |
| Z = +10 °C | 6 = +105 °C | C = ±2.2 |
|            | 7 = +125 °C | D = ±3.3 |
|            | 8 = +150 °C | E = ±4.7 |
|            | 9 = +200 °C | F = ±7.5 |
|            |             | P = ±10 |
|            |             | R = ±15 ← X5R, **X7R**, X8R |
|            |             | S = ±22 ← X6S, X7S |
|            |             | T = +22/−33 |
|            |             | U = +22/−56 |
|            |             | V = +22/−82 ← **Y5V**, Z5U |
|            |             | L = +15/−40 (industry, non-EIA) ← **X8L** |

## Typical `εr` ranges by class
| Class | `εr` at 25 °C, low field | Typical use |
|---|---|---|
| Class I (C0G/NP0) | 20–100 | RF tuning, filters, timing |
| Class II "stable mid-K" (X7R, X5R, X8R) | 600–4000 | bypass, decoupling, general purpose |
| Class II "high-K" (X6S, X7S, X7T) | 4000–8000 | high-cap miniaturization |
| Class III (Y5V, Z5U) | 4000–18 000 | bulk decoupling, where stability isn't critical |

(Source: [Knowles "Capacitor Fundamentals Part 8 — Dielectric Classifications"](https://blog.knowlescapacitors.com/blog/capacitor-fundamentals-part-8-dielectric-classifications) aggregated with [[psma-ceramic-capacitor-basics]].)

## Cross-references
- [[mlcc-capacitance-equation]] — how class enters as `εr`
- [[dc-bias-derating]] — Class II only
- [[aging-class-2]] — Class II/III only
- [[temperature-coefficient-of-capacitance]] — TCC physics
- [[batio3]] — the dominant Class II/III dielectric base

## References
- [[psma-ceramic-capacitor-basics]]
- [[samsung-cl-series-mlcc-ds]]
- Knowles Capacitor Fundamentals Part 8 (Knowles blog)
