---
title: X8R / X8L / X8G / X9R / X0U / X9V — High-Temperature MLCC Dielectrics
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - escies-bme-mlcc-high-reliability.md
tags:
  - paper
---

# X8R / X8L / X8G / X9R / X0U / X9V — High-Temperature MLCC Dielectrics

Class II dielectrics engineered for operation **above the standard X7R 125 °C ceiling**. Driven primarily by **automotive under-hood electronics** (electric vehicles, hybrid drivetrains, on-board chargers), industrial sensors, downhole oil/gas, and aerospace. The chemistry challenge: keep [[batio3|BaTiO₃]]'s εr-spec window (typically ±15 %) intact while the operating T extends past the natural Curie peak.

## The high-T family at a glance

| Code | T_max | ΔC envelope | Class | Notes |
|---|---|---|---|---|
| **X7R** | +125 °C | ±15 % | II | baseline (for reference) |
| **X8R** | +150 °C | ±15 % | II | automotive standard; Sr/Zr-shifted BaTiO₃ |
| **X8L** | +150 °C | ±15 % to +125, +15/−40 % to +150 | II (industry, non-EIA) | "X7R-equivalent to 125, controlled drift to 150" |
| **X8G** | +150 °C | ±30 ppm/°C | **I** | rare Class I extension; very low εr |
| **X9R** | +200 °C | ±15 % | II | research-grade; NaNbO₃-BaTiO₃-BiMg₁/₂Ti₁/₂O₃ |
| **X0U** | +175 °C | ±15 % to +125, +22/−56 % to +175 | II | **new** automotive-extreme code |
| **X9V** | +200 °C | +22/−82 % (similar to Y5V's tolerance but to 200 °C) | II | Vishay HOTcap; relaxed tol, high T |

(See [[dielectric-class-comparison]] for the full master table.)

## Why high-T is hard
Bulk [[batio3|BaTiO₃]] has T_C ≈ 120 °C. Above T_C, εr drops sharply (cubic paraelectric phase). For a part to maintain ±15 % εr through 150 °C, the **Curie peak must be shifted to higher T or broadened wide enough to bridge the gap**. Compositional levers:

1. **A-site substitution**: Pb²⁺ for Ba²⁺ raises T_C (PbTiO₃ T_C = 490 °C) — but **RoHS-restricted** since the early 2000s.
2. **B-site substitution**: Zr⁴⁺ for Ti⁴⁺ lowers T_C and broadens the peak. Sn⁴⁺ has similar effect. **Wrong direction** for high-T extension if used alone.
3. **Bi₂O₃ + Bi-titanate solid solutions**: Bi³⁺ on A-site, complex but engineerable behavior; raises Curie or broadens it.
4. **NaNbO₃ (anti-ferroelectric)** in solid solution: shifts Curie up and creates relaxor-like flat εr(T).
5. **BiMg₁/₂Ti₁/₂O₃**: A-site Bi³⁺ + B-site mixed Mg/Ti — broadens Curie peak dramatically; used in X9R formulations.
6. **Sr²⁺ for Ba²⁺**: lowers T_C (wrong direction).

Most commercial X8R formulations combine **Sr-Zr substitution to lower the bulk Curie a bit** + **heavy [[core-shell-batio3|core-shell]] engineering to flatten the peak**, so that the resulting εr(T) is approximately box-like (±15 %) from −55 to +150 °C.

## X8R vs X8L vs X8G
All three operate to **150 °C**, but differ in dielectric class and tolerance:

- **X8G** (Class I, ±30 ppm/°C): ultra-stable, low εr (~ 100–500). Uses extended-range Class I chemistries (Bi-titanate, CaTiO₃-rich). Rare — most vendors don't stock; alternative Class I products are usually preferred.
- **X8L** (Class II, asymmetric tolerance): tight ±15 % up to 125 °C, controlled +15/−40 % drift from 125 to 150 °C. **The pragmatic engineering choice**: standard X7R-like behavior in the consumer T range, with predictable degradation in the auto-hot zone.
- **X8R** (Class II, ±15 % full range): the most expensive — true ±15 % across the full envelope. Higher BOM cost than X8L, used when system-level error budget can't tolerate the X8L upper-T drift.

## X9R / X0U / X9V — beyond 150 °C
- **X9R** (T_max = 200 °C, ΔC ±15 %): research-grade in 2020s; NaNbO₃-modified BaTiO₃-BiMg₁/₂Ti₁/₂O₃ ceramics demonstrated. Not yet a major commercial line.
- **X0U** (T_max = **175 °C**, ΔC asymmetric): introduced ~ 2020s for AEC-Q200 automotive grade. Behaves as X7R (±15 %) up to 125 °C, then drifts +22/−56 % up to 175 °C. Production by AVX, Vishay, others.
- **X9V** (T_max = 200 °C, ΔC +22/−82 %): Vishay HOTcap brand. Engineered for ultra-high-T (downhole, EV inverter cases) where ±82 % drift is acceptable.

## Material chemistry pattern
The high-T extensions all share one strategy:
> Replace the **single sharp Curie peak at 120 °C** with a **broad, flat εr "plateau"** stretching from −55 °C to T_max — at the cost of lower peak εr.

The flatter the plateau, the lower the maximum εr. X7R peak εr ~ 4000; X8R typical εr ~ 2500–3500; X9R research-scale εr ~ 1500–2500. The CV/case-size trade-off vs X7R is real.

## Trade-offs at higher T
- **DC-bias derating** is **better** in X8R than X7R for the same nominal V because the broadened Curie peak puts the part further from the steep ferroelectric-to-paraelectric transition.
- **DC-bias-aging** is **better** in X8R (and dramatically better in X8L) because the higher [[curie-temperature|effective T_C]] and more aggressive doping pin the [[ferroelectric-domain-wall|domain walls]] more strongly.
- **Aging at zero bias** is **similar** to X7R for X8L; **slightly better** for X8R.
- **Insulation resistance at high T**: X8R drops less per decade of T rise than X7R (formulation specifically reduces O-vacancy electromigration).
- **εr is lower** at room temperature (the trade-off for broader temperature stability).

## Use cases
- Automotive under-hood (EV motor controllers, OBC, BMS, ADAS sensors near the engine bay): **X8R** standard, **X0U** for the hottest spots.
- Industrial sensors near hot processes (steel mill, gas turbines): **X8R / X8L** depending on accuracy budget.
- Aerospace electronics (radar, navigation, near-engine): **X8L** standard; **X9V** in extreme cases.
- Downhole oil/gas instrumentation: **X9V** (200 °C) or stacked C0G arrays.

## Vendor availability
KYOCERA AVX, KEMET, [[murata]] (GCM AEC-Q200 series), [[tdk]] (CGA series), [[samsung-electro-mechanics]] (CL series automotive variant) all offer X8R and X8L lines. X8G is rare — only Knowles and a few specialty vendors. X0U is appearing in 2024–2026 product launches (AVX, Vishay).

## Implications for the simulator
- For X8R: same f_T form as X7R but with shifted T_C (~135 °C) and broader sigmoid.
- For X8L: piecewise — X7R-equivalent envelope to 125 °C, then asymmetric drift.
- For X9V: full +22/−82 % box throughout.
- DC-bias derating: high-T extensions are systematically **better** at the same nominal V, but the user-facing simulator should still use vendor-specific data.

## Cross-references
- [[eia-rs-198-dielectric-classes]]
- [[dielectric-class-comparison]]
- [[x7r-dielectric]]
- [[curie-temperature]]
- [[batio3]]
- [[nanbo3]]
- [[core-shell-batio3]]
- [[tdk-cga-series]]
- [[bme-c0g]]
- [[aec-q200-rev-e-2023]]

## References
- [[escies-bme-mlcc-high-reliability]] — X7R / X8R / X8L life-test data
- KYOCERA AVX X8R/X8L product page
- KEMET Ultra Stable X8R/X8L SMD MLCC datasheet (Digi-Key)
- TDK C-Series High Temperature X8R datasheet
- Passive-Components.eu "What is the Difference Between X8G, X8L and X8R Ceramic Capacitor Dielectrics?"
- MDPI Crystals 12:2 (2022) 141 — X9R NaNbO₃-modified BaTiO₃-BiMg₁/₂Ti₁/₂O₃ ceramics
- Vishay HOTcap X9V documentation
- ScienceDirect (1−x)(K0.8Na0.2)NbO3–xBaTiO3 for X9R MLCC
