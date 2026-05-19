---
title: "NASA NEPP — Reliability of Multilayer Ceramic Capacitors with Base-Metal Electrodes"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-nepp-bme-mlcc-reliability.md
tags:
  - paper
status: complete
importance: high
---

# NASA NEPP — Reliability of Multilayer Ceramic Capacitors with Base-Metal Electrodes

**Source:** `resources/literature/nasa-nepp-bme-mlcc-reliability.md` (PDF: `resources/literature/pdf/nasa-nepp-bme-mlcc-reliability.pdf`)
**Author:** David (Donhang) Liu ([[donhang-liu]]), NASA Goddard
**Publication:** EEE Parts Bulletin, April–May 2013, Vol. 5 Issue 2 (Special Issue)

## Summary

The single most useful synthesis for an MLCC reliability simulator. Liu builds an explicit three-factor model `R(t) = φ(N,d,r̄,S) · AF(V,T) · γ(t)`, deriving each factor from first principles and back-fitting to NEPP-funded test data. The structural factor `φ = (1 − (r̄/d)^α)^N` makes the **N amplifier** quantitative: per-layer reliability of 0.999 collapses to 0.13 at N=200. Distinguishes PME single-mode Prokopowicz–Vaskas acceleration from the BME-specific **two-mode** picture (catastrophic power-law + slow exponential degradation) driven by oxygen-vacancy electromigration. Closes with chip-size scaling (Table II — exact dimensions and end/side margin values for 0402 through 2220, plus a derived overlap-area scaling factor up to 102.55× from 0402 to 2220) and shows that chip-size reliability is roughly invariant because thicker `d` compensates for larger `S`.

## Key equations
1. `C = εr·ε₀·N·S/d` (Eq. 1)
2. `C/V ≈ ε₀·εr/d²` (Eq. 2) — volumetric efficiency
3. `R(t) = φ(N,d,r̄,S) · AF(V,T) · γ(t)` (Eq. 3)
4. Weibull `γ(t) = exp(−(t/η)^β)`, MTTF = η·Γ(1+1/β) (Eqs. 4–5)
5. PME P-V: `t₁/t₂ = (V₂/V₁)^n · exp((Ea/k)·(1/T₁ − 1/T₂))` (Eq. 6); n ≈ 3, Ea ≈ 1–2 eV.
6. BME two-mode acceleration (Table I).
7. MTTF ∝ (d/r̄)^n at fixed V and r̄ (Eq. 11). Reliability invariant when "voltage per grain boundary" is fixed (data courtesy of Murata).
8. Structural reliability `φ = (1 − (r̄/d)^α)^N`, α ≈ 6 (V≤50V), 5 (V>50V) (Eqs. 12–14).
9. Chip-scaling: `R_i(xy) = R_i(0402)^S` where S is the area scaling factor from Table II.

## Reference table (Table II — chip dimensions)
| Chip | L (µm) | W (µm) | End margin (µm) | Side margin (µm) | A (mm²) | Scale S |
|---|---|---|---|---|---|---|
| 0402 | 1000±100 | 500±100  | 125 | 100 | 0.225 | 1.00 |
| 0603 | 1600±150 | 810±150  | 175 | 100 | 0.763 | 3.39 |
| 0805 | 2010±200 | 1250±200 | 250 | 150 | 1.520 | 6.76 |
| 1206 | 3200±200 | 1600±200 | 250 | 150 | 3.510 | 15.60 |
| 1210 | 3200±200 | 2500±200 | 250 | 150 | 5.940 | 26.40 |
| 1812 | 4500±300 | 3200±200 | 300 | 200 | 10.920 | 48.53 |
| 2220 | 5700±400 | 5000±400 | 320 | 220 | 23.074 | 102.55 |

## Entities mentioned
- [[donhang-liu]] — author
- [[nasa-nepp]] — funding program
- [[murata]] — provided HALT data for grain-size analysis
- [[intel]] — 2010 report of BaTiO₃ MLCC life degradation as `d` shrinks

## Concepts discussed
- [[mlcc-capacitance-equation]]
- [[bme-reliability-model]] — this paper IS the source of the framework
- [[bme-vs-pme]]
- [[case-size-geometry]]
- [[core-shell-batio3]]

## References
_Original source: `resources/literature/nasa-nepp-bme-mlcc-reliability.md`_
