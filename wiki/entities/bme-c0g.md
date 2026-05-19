---
title: BME C0G (KEMET)
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - escies-bme-mlcc-high-reliability.md
tags:
  - series
status: complete
importance: medium
---

# BME C0G (KEMET)

[[kemet]]'s line of **Class I C0G / NP0** MLCCs built with **base-metal** ([[bme-vs-pme|BME]]) Ni inner electrodes and [[cazro3|CaZrO₃]]-based dielectric — directly challenging the historical PME C0G stronghold (BNT dielectric + Ag/Pd electrodes) on both cost and reliability.

## Why it matters
For 25–30 years C0G/NP0 was the **PME holdout** even as Class II went BME: the legacy BNT (BaNd-titanate) dielectric had εr ≈ 70 and worked with Pd/Pt electrodes air-fired. BME C0G with CaZrO₃ has lower εr (~31) but allows much thinner dielectric layers in BME process, yielding **higher cap per case + dramatically longer life** than legacy PME C0G:

| Metric | PME C0G (BNT) | BME C0G (CaZrO₃) |
|---|---|---|
| Dielectric constant | ~70 | ~31 |
| Dielectric layer thickness (1206 / 10 nF) | 11.6 µm | 7.0 µm |
| HALT MTTF (175 °C, 400 V) | 62.6 min | **869.6 min** |
| BDV at 150 °C | (lower) | > 200 V/µm |
| IR @ 200 °C | typical drop | rises (CaZrO₃ wide-bandgap) |

Source: [[escies-bme-mlcc-high-reliability]] Figures 1–2.

## Lineup highlights
- Standard case sizes 0402 through 1812.
- Available in stacks (Case Code 4 per MIL-PRF-49470, 2.5 µF / 50 V at 5-chip stacks) for higher-cap military / energy-storage applications.
- Passed 4000-h life test at **2× rated V, 125 °C** with zero failures across many part types.
- Operating envelope extended to 200 °C (and 225 °C in custom stacks) — meets EIA X9G spec (TCC ≤ ±30 ppm/°C from −196 °C to +200 °C).

## See also
- [[kemet]]
- [[cazro3]]
- [[bme-vs-pme]]
- [[escies-bme-mlcc-high-reliability]]
