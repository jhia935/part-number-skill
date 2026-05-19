---
title: Murata Manufacturing Co., Ltd.
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - psma-ceramic-capacitor-basics.md
  - murata-grm-series-tcc-data.md
  - nasa-nepp-bme-mlcc-reliability.md
tags:
  - company
status: complete
importance: high
---

# Murata Manufacturing Co., Ltd.

The largest MLCC manufacturer in the world (Japan, HQ Nagaokakyo, Kyoto). The technological pacesetter for thin-layer dielectrics and BME firing.

## Why Murata leads
- **Vertical integration from BaTiO₃ powder**: produces own dielectric powder at ~100 nm particle size — Korean competitors (e.g., [[samsung-electro-mechanics]]) historically at 300–500 nm, a 3–5× gap in raw-material control.
- **Pioneer of Ni-BME** ([[bme-vs-pme]]): commercialized the world's first Ni internal-electrode MLCC in **1982** (IEEE/ETHW milestone). The required shift to reducing-atmosphere firing and the rare-earth-doped dielectric chemistry that compensates for oxygen vacancies is largely Murata IP.
- **Thin-layer state of the art**: published 0.7 µm and thinner dielectric layer technology; lab parts at <1 µm × 1000 layers.

## Product portfolio (MLCC)
- **GRM series** ([[murata-grm-series]]) — general-purpose, the workhorse line. Sub-families: GRM03 (0201), GRM15/18 (0402/0603), GRM21/22 (0805), GRM31/32 (1206/1210), GRM43/55 (1812/2220).
- **GCM / GCJ series** — AEC-Q200 automotive grade.
- **GJM series** — high-frequency / RF.
- **GRT series** — soft-termination flex mitigation.

## Patent activity
WO2024247128A1 (filed May 2023, published Dec 2024) — BaTiO₃ with rare-earth `Re` + first-additive `Me` minor components. Indicates active dopant engineering ([[core-shell-batio3]]) is still the competitive frontier.

## Role in the public reliability literature
Murata supplied the HALT data used by Donhang Liu ([[donhang-liu]]) to validate the `MTTF ∝ (d/r̄)^n` scaling — see [[nasa-nepp-bme-mlcc-reliability]] Figure 7. Strong public claim that "voltage per grain boundary" is the invariant reliability metric.

## See also
- [[murata-grm-series]]
- [[bme-vs-pme]]
- [[core-shell-batio3]]
