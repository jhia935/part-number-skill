---
title: C0G / NP0 (Class I Ultra-Stable Dielectric)
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: high
sources:
  - escies-bme-mlcc-high-reliability.md
  - psma-ceramic-capacitor-basics.md
tags:
  - paper
---

# C0G / NP0 (Class I Ultra-Stable Dielectric)

The reference for "perfect" MLCC behavior: **TCC = 0 ± 30 ppm/°C** over −55 °C to +125 °C (and often to +200 °C with grade extensions), **no aging**, **no DC-bias derating**, **no piezoelectric / microphonic effects**, **DF ≤ 0.15 %**. C0G and NP0 ("Negative-Positive-zero") are the same thing — different naming conventions. C0G is the EIA RS-198 letter code, NP0 is the historical industry code.

## Why C0G is special
Built from **paraelectric** materials, not ferroelectric. No ferroelectric domains → no [[ferroelectric-domain-wall|domain-wall effects]] → no DC-bias derating, no aging, no piezo. The trade-off is **modest εr** (20–100 typical; up to 500 with extended-range Class I formulations).

C0G is the **only** ceramic dielectric class that behaves like a "textbook ideal capacitor" across the operating range. Use it whenever spec accuracy matters more than capacitance density.

## Material chemistry

### Modern BME C0G ([[bme-c0g]])
Base: **[[cazro3|CaZrO₃]]**, εr ≈ 31. Compatible with Ni inner electrodes + reducing-atmosphere firing. Replaces legacy PME C0G in most commercial production since the late 2000s.

### Legacy PME C0G
Base: **BaNd-titanate (BNT, Ba₆Ti₁₇O₄₀-based)**, εr ≈ 70. Fired in air with Pd or Ag/Pd inner electrodes. Still used in some high-rel / mil-spec applications. Now largely superseded by BME C0G on cost and reliability ([[escies-bme-mlcc-high-reliability]]: 13.9× HALT MTTF advantage for BME).

### Extended-range Class I (Negative-TCC variants)
Adds a tunable negative TCC by introducing small amounts of **CaTiO₃, SrTiO₃, or TiO₂** to the C0G base. These are mildly ferroelectric ions that shift the Curie peak just outside the operating range, producing **near-linear, predictable temperature characteristics** with εr up to ~500.

Codes for the negative-TCC extended-range Class I:
- **P2H**: −150 ppm/°C ±60 ppm/°C
- **R2H**: −220 ± 60
- **S2H**: −330 ± 60
- **T2H**: −470 ± 60
- **U2J**: −750 ± 120 (highest εr in the Class I family, ~250–500)

These codes are designed to **temperature-compensate** other circuit elements (e.g., compensate an inductor's positive TCC to make an LC resonator temperature-stable).

## Quantitative spec envelope

| Parameter | C0G typical | Extended Class I (e.g., U2J) |
|---|---|---|
| TCC | 0 ± 30 ppm/°C | −750 ± 120 ppm/°C |
| Operating T | −55 to +125 °C (some to +200) | −55 to +125 °C |
| εr | 20–100 (CaZrO₃ ~31) | 250–500 |
| DF max (1 MHz) | 0.15 % (0.0015) | 0.2 % (0.002) |
| Aging | ~0 (no measurable) | ~0 |
| DC-bias derating | ~0 (paraelectric — no domains to pin) | ~0 |
| AC drive sensitivity | none | none |
| Piezoelectric output | none | none |
| IR @ 25 °C | very high (10¹³ Ω cm grain) | very high |

## Applications
1. **RF tuning and filtering**: the εr stability and zero aging means an LC filter holds its center frequency for the life of the part.
2. **Audio coupling / mic bias**: zero piezo / microphonic effects → no signal distortion (in contrast to Class II BaTiO₃ parts which sing when AC-driven).
3. **High-Q resonator capacitors**: low DF means high quality factor Q (typically Q > 1000 for C0G).
4. **Precision timing**: zero TCC means RC time constants are temperature-stable.
5. **Energy-storage with low loss**: pulse-power, high-voltage applications where BDV / current capability matters more than CV.
6. **High-temperature (≥ 150 °C)**: extended BME C0G survives 200 °C with rising IR (per [[escies-bme-mlcc-high-reliability]]).

## Why not always use C0G?
- **Low εr** → low CV per case. A 1 µF C0G in 1206 takes more layers and thicker dielectric than a 10 µF X7R in the same case.
- **Higher cost per µF** (because of lower volumetric efficiency).
- **Limited capacitance range**: typical commercial C0G tops out at hundreds of nF in 1210 size; multi-µF requires large case sizes or stacks.

## Class I vs Class II decision flow
- Need stability (RF, timing, mic, signal-path)? → **C0G**.
- Need high CV (bulk decoupling)? → **X7R** (or X8R for auto). Don't use C0G — wastes space and money.
- Need both stability and high CV? → mix and match: C0G for the precision rail, X7R for bulk capacitance in parallel.

## Cross-references
- [[eia-rs-198-dielectric-classes]]
- [[dielectric-class-comparison]]
- [[cazro3]]
- [[bme-c0g]]
- [[bme-vs-pme]]
- [[temperature-coefficient-of-capacitance]]
- [[ferroelectric-domain-wall]] — what C0G doesn't have

## References
- [[psma-ceramic-capacitor-basics]]
- [[escies-bme-mlcc-high-reliability]] — BME vs PME C0G comparison
- [[samsung-cl-series-mlcc-ds]] — TCC code table for Class I extended range
- KYOCERA AVX C0G/NP0 product page
- doEEEt.com "Class 1 Ceramic Dielectrics"
