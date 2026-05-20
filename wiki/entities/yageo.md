---
title: Yageo
type: entity
created: 2026-05-19
updated: 2026-05-20
sources:
  - aec-q200-rev-e-2023.md
tags:
  - company
status: complete
importance: medium
---

# Yageo

Taiwanese passive-component manufacturer (國巨), HQ Taipei. **Largest passive components company by revenue** since the 2018 capacitor shortage; broader portfolio than the Tier-1 Japanese MLCC houses. Owns [[kemet]] (acquired 2020) and Pulse Electronics; supplies its own Yageo-branded line plus KEMET legacy. Active participant in AEC-Q200 standardization ([[aec-q200-rev-e-2023]] sub-committee).

## Position in the MLCC market
Yageo + KEMET combined is the **third-largest MLCC supplier globally** by unit volume after [[murata]] and [[samsung-electro-mechanics]], ahead of [[tdk]] and [[taiyo-yuden]] in some segments. Strong in:
- Mid-volume automotive (AEC-Q200) — explicit "approach the goal of zero defects in field applications"
- Cost-sensitive consumer
- Specialty: anti-flex, EMI, safety-certified

## Automotive product portfolio
- **AC Series**: AEC-Q200 standard automotive grade; case 0201–1812; X5R, X6S, X7R, X8R.
- **AS Series**: Boardflex-sensitive — soft-termination variant of AC, for flex / vibration zones.
- **AQ Series**: Automotive High-Frequency (low-ESL reverse geometry, RF / wireless infrastructure).
- **AC Array**: 2-element and 4-element MLCC arrays for high-density automotive boards.
- **AC HiCap**: high-capacitance automotive (>1 µF).
- **AC HiTemp**: X8L / X8R high-temperature subline.

All AEC-Q200 qualified + MIL-STD-020D moisture-resistance tested. Operating envelope **−55 °C to +150 °C** for X8R parts. 1000 h at 85 °C / 85 % RH humidity-bias tested.

## KEMET-branded continuation
Within Yageo, the KEMET brand continues to sell:
- [[kemet-arcshield]] HV MLCC (X7R BME, 500/630/1000 V_dc)
- BME [[bme-c0g|C0G]] family (CaZrO₃-based)
- FT-CAP soft-termination
- High-T BME C0G (200 °C operation, X9G class)
- Specialty safety-certified (Y1/Y2 line-to-line, X1/X2 line-to-ground)

## Yageo public technical content
- Yageo AC MLCC whitepaper (TTI Europe / Mouser distribution — `Yageo_AS_whitepaper.pdf`, `AQ_whitepaper_final.pdf`, `yageo_AC_mlcc_whitepaper_en_final_20072217_349.pdf`). *Anti-bot blocked from direct download during this research pass — content summarized from search snippets.*
- KEMET datasheet library (content.kemet.com) — full technical doc access via direct URLs (e.g., `KEM_C1100_CAS_SMD.pdf` for safety-certified line).
- DigiKey product highlight pages for AC, AS, AQ series.

## Quality framework
Yageo cites the following in their AC-series literature:
- High-quality raw materials (BaTiO₃ powder qualification)
- Special construction design (electrode geometry)
- **Comprehensive Statistical Process Control (SPC)** across production lots
- Dedicated production line for AEC-Q200 vs commercial

## Sub-committee participation
Per [[aec-q200-rev-e-2023]] acknowledgments, Yageo Group representatives (LeAnna Weakley, Alfred Chen) sit on the AEC-Q200 Q200 Sub-Committee — direct contributor to the automotive passive qualification spec.

## See also
- [[kemet]] — Yageo subsidiary brand
- [[kemet-arcshield]]
- [[bme-c0g]]
- [[aec-q200-rev-e-2023]]
- [[mlcc-pcb-layout-rules]] — boardflex / soft-termination link
