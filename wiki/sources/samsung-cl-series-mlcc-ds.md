---
title: "Samsung Electro-Mechanics — CL Series General-Purpose MLCC Datasheet"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/market/samsung-cl-series-mlcc-ds.md
tags:
  - paper
status: complete
importance: high
---

# Samsung Electro-Mechanics — CL Series General-Purpose MLCC Datasheet

**Source:** `resources/market/samsung-cl-series-mlcc-ds.md` (PDF: `resources/market/pdf/samsung-cl-series-mlcc-ds.pdf`)
**Publisher:** [[samsung-electro-mechanics]] (SEMCO)
**Type:** Series-level technical specification for the [[samsung-cl-series]]

## Summary

A comprehensive series datasheet that doubles as a vocabulary reference. Contains:
- Full part-numbering decoder (11 fields): size, TCC, nominal cap, tolerance, rated V, thickness option, electrode/termination/plating, control code, packaging.
- Size code table mapping SEMCO codes (03/05/10/21/31/32/43/55) to EIA codes (0201/0402/0603/0805/1206/1210/1812/2220) and L × W dimensions in mm.
- Full TCC code table for Class I (C0G, P2H, R2H, S2H, T2H, U2J, S2L) with ppm/°C values, plus Class II (X5R/A, X7R/B, X6S/X) and Class III (Y5V/F) with allowed ΔC%.
- Capacitance-tolerance letter codes (A through Z, ±0.05 pF to +80/−20 %).
- Rated voltage codes (R, Q, P, O, A, L, B, C, D, E, G, H, I, J, K) for 4.0 V through 3000 V.
- Thickness option codes per case size (e.g., 1206 has 0.85, 1.25, 1.6 mm options).
- Electrode/termination combinations: A = Pd/Ag/Sn (PME); N = Ni/Cu/Sn (BME); G = Cu/Cu/Sn.
- Outer dimensions table with tolerances and bandwidth (BW) — the lateral termination dimension.
- Full reliability test conditions: insulation resistance limit (10⁴ MΩ or 500 MΩ·µF, whichever is smaller; reduces to 10⁴ or 100 MΩ·µF below 16 V); withstanding voltage (300 % rated, Class I; 250 % rated, Class II) for 1–5 s.
- Test currents & frequencies for capacitance measurement (1 MHz for ≤ 1000 pF; 1 kHz for > 1000 pF up to 10 µF; 120 Hz for > 10 µF).
- Tan δ limits as function of rated voltage and capacitance.
- TCC measurement procedure for Class I (vs 25 °C, normalized by formula).
- Mechanical: 1 mm bending limit, 500 gf adhesive strength (200 gf for 0201), capacitance change limits during bending (±5 % Class I, ±12.5 % Class II X5R/X7R/X6S, ±30 % Y5V).
- Solderability and resistance to soldering heat conditions.
- Humidity (steady-state) and moisture-resistance tests with capacitance / Q / tan δ / IR limits.

## Why this source is high-importance
1. It is the only vendor source we have with **explicit dimensional and thickness-option tables** — needed to derive `H_max` and `m_end / m_side` for the simulator.
2. Letter-code tables are a Rosetta Stone for parsing other vendor part numbers.
3. Test conditions (250 % withstand, 1 mm flex, etc.) are the verbatim AEC-Q200 / IEC 60384-style limits the simulator should mirror.

## Concepts discussed
- [[mlcc-capacitance-equation]] (implicit)
- [[eia-rs-198-dielectric-classes]]
- [[case-size-geometry]]
- [[failure-modes-mlcc]] (mechanical test conditions)

## Entities mentioned
- [[samsung-electro-mechanics]]
- [[samsung-cl-series]]

## References
_Original source: `resources/market/samsung-cl-series-mlcc-ds.md`_
