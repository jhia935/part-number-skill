---
title: "TDK MLCC Product Guide (CGA / C-Series, 2012 catalog via Octopart)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/market/octopart-tdk-cga8l3c0g.md
tags:
  - paper
status: complete
importance: high
---

# TDK MLCC Product Guide (CGA / C-Series, 2012)

**Source:** `resources/market/octopart-tdk-cga8l3c0g.md` (PDF: `resources/market/pdf/octopart-tdk-cga8l3c0g.pdf`, 62 pages, 7.5 MB)
**Publisher:** [[tdk]] (mirrored on Octopart from the 2012 TDK MLCC product line-up document)
**Type:** Vendor-wide product catalog: C-series (commercial), CGA-series (automotive), CKC-series (arrays), high-voltage variants

## Summary

TDK's 2012 full MLCC product line-up. The most comprehensive single TDK document obtained for this knowledge base — covers temperature characteristic series (C0G / NP0, X5R, X7R, X8R, X7T), automotive grades (CGA), high-voltage parts, soft-termination "CC-Cap" devices, and arrays (CKC). Provides lineup tables (cap value × case size × rated voltage) per series.

## Content coverage (62 pages)

- General-purpose **C-Series** with full case range C0402 (01005) – C5750 (2220)
- Automotive **CGA-Series** AEC-Q200 qualified
- **High-voltage** C-series (mid voltage, high voltage) — up to several kV
- **Conductive-resin (soft termination) CC-Cap** for flex / thermal-shock resistance
- **Array (CKC)** series — 4-element MLCC arrays
- **CKC** dimension example: CKCL22 (4-element 0805 array) — 2.00 × 1.25 × 0.85 mm, BW 0.45 / 1.00 mm

## Useful nuggets relevant to the simulator

- TDK's C-Series "uses advanced ceramic dielectric thin-layer and multi-layering technology" — generic but confirms ≤1 µm dielectric layer SOTA.
- Mid-voltage and high-voltage families explicitly call out "Excellent DC bias properties" as a marketing claim — i.e., engineered to flatten the VCC sigmoid for power-distribution use cases (plasma drivers, automotive battery).
- "Guaranteed TC Bias and Hot IR performance" for automotive-grade parts (CGA) is the explicit reliability commitment vs commercial-grade C-series — the AEC-Q200 envelope.
- High-temperature dielectric performance: C-series "Stable temperature characteristics (±7.5 %) up to 125 °C" for the X7T variant, "Stable temperature characteristics (±15 %) up to 150 °C" for X8R.
- Sintered Ni inner electrode, sintered Cu outer termination + Ni barrier + Sn plating — the standard BME stack.
- Soft-termination variants ("CC-Cap") add a conductive resin layer between Cu termination and Ni barrier to absorb board-flex stress — analogous to [[kemet]]'s FT-CAP.

## Implications for the lineup matrix

This source gives the TDK side of the [[case-size-geometry]] table:
| TDK code | EIA | L × W × T_max (mm) |
|---|---|---|
| C0402 | 01005 | 0.40 × 0.20 × 0.20 |
| C0603 | 0201 | 0.60 × 0.30 × 0.30 |
| C1005 | 0402 | 1.00 × 0.50 × 0.50 |
| C1608 | 0603 | 1.60 × 0.80 × 0.80 |
| C2012 | 0805 | 2.00 × 1.25 × 1.25 |
| C3216 | 1206 | 3.20 × 1.60 × 1.60 |
| C3225 | 1210 | 3.20 × 2.50 × 2.50 |
| C4532 | 1812 | 4.50 × 3.20 × 3.20 |
| C5750 | 2220 | 5.70 × 5.00 × 2.80 |

Note that TDK exposes **height = width** for square-cross-section families (≤ 1206), and reduced height for the larger 2220.

## Concepts discussed
- [[case-size-geometry]]
- [[eia-rs-198-dielectric-classes]]
- [[bme-vs-pme]]
- [[failure-modes-mlcc]]

## Entities mentioned
- [[tdk]]
- [[tdk-cga-series]]

## References
_Original source: `resources/market/octopart-tdk-cga8l3c0g.md`_
