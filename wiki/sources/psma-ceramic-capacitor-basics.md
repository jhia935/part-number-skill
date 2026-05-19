---
title: "PSMA / KEMET — Ceramic Capacitor Basics (MLCCs Design and Characteristics)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/psma-ceramic-capacitor-basics.md
tags:
  - paper
status: complete
importance: high
---

# PSMA / KEMET — Ceramic Capacitor Basics

**Source:** `resources/design-rules/psma-ceramic-capacitor-basics.md` (PDF: `resources/design-rules/pdf/psma-ceramic-capacitor-basics.pdf`)
**Publisher:** [[kemet]] / PSMA, © 2017
**Type:** Industry training deck

## Summary

The most quantitatively dense of the foundational sources. Covers the full MLCC stack from outer construction (Cu termination on BME, Ag on PME; Ni barrier; Sn plating) through dielectric classes (with full EIA RS-198 tables for Class I and Class II/III), DC bias derating physics (BaTiO₃ tetragonal-vs-cubic), AC coupling and signal distortion, X7R aging at 1.5 %/decade-hour, and the full taxonomy of failure modes (crack types, surface arcing). Also contains a critical historical chart of BME dielectric thickness and layer count progression (1988 → today): from `0.1 µF/50V` at 12 µm × 30 layers to `47 µF/4V` at 1 µm × 600 layers. Closes with a section on RF MLCC construction (low-loss C0G, short/wide geometry, Cu-BME for lowest ESR).

## Key points

- Full Class I letter-code table: 1st letter = TCC significant figure, digit = multiplier, 3rd letter = tolerance. Examples: C0G, P2H, U2J.
- Full Class II/III letter-code table including X8L (industry, non-EIA, +15/−40 %).
- DC bias example: 1210 vs 0805, X7R, 10 µF, 6.3 V — the smaller case loses ~60 % at rated, the larger only ~10 %. Field, not voltage, is the driver.
- BaTiO₃: cubic above 130 °C (no dipole, no ferroelectricity); tetragonal below (dipole, ferroelectricity).
- Aging law: X7R loses 1.5 %/decade-hour (industry max). Reversible above Curie.
- Four-level flex-crack mitigation hierarchy:
  - L0: standard, 2 mm, fail-short
  - L1: open-mode / floating electrode, 2 mm, fail-open
  - L2: flexible termination, 5 mm, fail-short
  - L3: hybrid (L1 + L2), 5 mm, fail-open
- RF MLCC: Cu-BME has lower resistivity than Ni-BME, Pd-PME, Ag-PME — chosen for lowest ESR.

## Entities mentioned
- [[kemet]]

## Concepts discussed
- [[mlcc-capacitance-equation]]
- [[eia-rs-198-dielectric-classes]]
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[failure-modes-mlcc]]
- [[bme-vs-pme]]
- [[batio3]]

## References
_Original source: `resources/design-rules/psma-ceramic-capacitor-basics.md`_
