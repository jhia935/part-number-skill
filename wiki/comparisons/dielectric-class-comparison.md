---
title: MLCC Dielectric Class Comparison (Full Family)
type: comparison
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: high
sources:
  - psma-ceramic-capacitor-basics.md
  - samsung-cl-series-mlcc-ds.md
  - escies-bme-mlcc-high-reliability.md
  - rohm-ceramic-cap-app-note.md
tags:
  - paper
---

# MLCC Dielectric Class Comparison (Full Family)

The complete EIA RS-198 letter-code taxonomy with quantitative specs for every commercially significant temperature characteristic. **The choice of dielectric class is the single biggest design decision** that drives every other tradeoff: εr range, voltage rating, aging, DC-bias derating, IR/reliability, and cost. This comparison is keyed to the simulator's `f_T(T)` block.

## Master table — Class I (paraelectric, linear)

| Code | TCC (ppm/°C) | Tolerance (ppm/°C) | εr range | Aging | DF max | Material basis | Notes / use |
|---|---|---|---|---|---|---|---|
| **C0G / NP0** | 0 | ±30 | 20–100 | ~0 | 0.15 % | CaZrO₃ (modern BME) or MgTiO₃ / CaTiO₃ blends (PME) | Workhorse Class I; RF tuning, timing, AC coupling |
| BO / BP | +0.3 | ±10 to ±60 | similar to C0G | ~0 | <0.1 % | TiO₂ + MgTiO₃ | Slight positive TCC |
| **P2H** | −150 | ±60 | 50–150 | ~0 | <0.1 % | CaTiO₃ + neutralizers | RF resonators |
| **R2H** | −220 | ±60 | 50–200 | ~0 | <0.15 % | CaTiO₃-rich | Tuning RF |
| **S2H** | −330 | ±60 | 100–250 | ~0 | <0.15 % | CaTiO₃ + TiO₂ | RF |
| **T2H** | −470 | ±60 | 150–300 | ~0 | <0.2 % | TiO₂-dominant | Linear-T-coefficient resonators |
| **U2J** | −750 | ±120 | 250–500 | ~0 | <0.2 % | Nd-doped TiO₂ | Highest-εr Class I; band-pass filters |
| **S2L** | +350 to −1000 | (industry, non-EIA) | varies | ~0 | <0.3 % | mixed | Asymmetric TCC |
| **X8G** | (Class I, ±30 ppm/°C) | over −55…+150 °C | low εr | ~0 | <0.15 % | high-T Class I | Rare; high-T temperature-compensating; mostly replaced by extended-range PME |

## Master table — Class II (ferroelectric, "stable mid-K")

| Code | Temp range | Max ΔC | εr range | Aging %/decade | DF max | Material basis | Notes |
|---|---|---|---|---|---|---|---|
| **X5R** | −55 to +85 °C | ±15 % | 1000–3000 | ~ 5 % | 2.5 % | BaTiO₃ + Y/Mg co-dope | Smartphone bulk decoupling; lower DC-bias tol than X7R |
| **X6S** | −55 to +105 °C | ±22 % | 2000–4000 | ~ 4 % | 2.5 % | BaTiO₃ doped | Industrial bridging X5R-X7R range |
| **X7R** | −55 to +125 °C | ±15 % | 600–4000 | **1–2 %** | 2.5 % | BaTiO₃ core-shell Y/Mg/Mn | **Most common** — automotive / industrial baseline |
| **X7S** | −55 to +125 °C | ±22 % | up to 5000 | ~ 3 % | 3.0 % | BaTiO₃, higher dopant | Larger range than X7R, **better effective C under DC bias** than X7R |
| **X7T** | −55 to +125 °C | +22/−33 % | up to 6000 | ~ 4 % | 3.5 % | BaTiO₃, even higher dopant | **Higher CV per case** than X7R; asymmetric tolerance acceptable |
| **X7U** | −55 to +125 °C | +22/−56 % | up to 8000 | ~ 5 % | 4 % | BaTiO₃ relaxor-ish | High-CV; bulk decoupling where stability not critical |
| **X8R** | −55 to +150 °C | ±15 % | 1500–3500 | ~ 2 % | 2.5 % | BaTiO₃ + Sr/Zr/Bi shift (Curie raised) | Automotive under-hood standard |
| **X8L** | −55 to +150 °C | ±15 % (−55…+125), +15/−40 % (+125…+150) | ~3000 | ~ 2 % | 2.5 % | BaTiO₃ wider Curie peak | Most common automotive — "X7R-class behavior to 125, controlled drift to 150" |
| **X0U** | −55 to +175 °C | ±15 % (−55…+125), +22/−56 % (+125…+175) | ~2000–3000 | 3–4 % | 3 % | BaTiO₃ + Bi₂O₃ / NaNbO₃ dopants | **New** automotive-extreme code for 175 °C |
| **X9R** | −55 to +200 °C | ±15 % | research-grade | TBD | TBD | NaNbO₃-modified BaTiO₃-BiMg₁/₂Ti₁/₂O₃ | Research; not yet a major commercial line |
| **X9V** | −55 to +200 °C | +22/−82 % | varies | high | high | BaTiO₃ relaxor + dopants | Vishay HOTcap — high-T but with relaxed tolerance |

## Master table — Class III (high-K, "Y/Z" codes)

| Code | Temp range | Max ΔC | εr range | Aging %/decade | DF max | Material basis | Notes |
|---|---|---|---|---|---|---|---|
| **Y5V** | −30 to +85 °C | +22/−82 % | **4000–18 000** | **5–7 %** | 16 % @ 6.3 V | High-K BaTiO₃ relaxor | High-cap bulk decoupling **only** in climate-controlled designs |
| **Z5U** | +10 to +85 °C | +22/−56 % | 4000–14 000 | ~ 5–7 % | 12 % | similar high-K BaTiO₃ | Legacy; mostly replaced by X5R |

## Master table — Military / Hi-rel codes (per MIL-C-55681 etc.)

| Code | Notes |
|---|---|
| **BP** | PME equivalent of C0G; legacy mil-spec |
| **BX** | PME X7R-like, "BX" = ±15/−25 % under V+T combined stress |
| **BR** | PME X7R-like, ±15 % at rated V (more aggressive than BX) |

These are largely superseded by AEC-Q200 (commercial-derived) and BME C0G/X7R for modern hi-rel applications.

## Reading the codes (EIA RS-198 Class II/III)
Three characters:
1. **Letter** = T_min: X = −55 °C, Y = −30 °C, Z = +10 °C
2. **Digit** = T_max: 4 = 65, 5 = 85, 6 = 105, **7 = 125**, **8 = 150**, **9 = 200**
3. **Letter** = max |ΔC|: A = ±1 %, B = ±1.5 %, C = ±2.2 %, D = ±3.3 %, E = ±4.7 %, F = ±7.5 %, P = ±10 %, **R = ±15 %**, **S = ±22 %**, T = +22/−33 %, **U = +22/−56 %**, **V = +22/−82 %**, L = +15/−40 % (industry, non-EIA).

Class I codes use a different scheme (significant-figure × multiplier × tolerance) — see [[temperature-coefficient-of-capacitance]].

## Sorted by application

### RF / timing / precision filters (need stability)
→ **C0G / NP0** (mandatory); other Class I extended codes for specific Curie compensation.

### Power supply decoupling (need high cap, moderate stability)
→ **X7R** (default), upgrade to **X8L** or **X8R** for automotive; downgrade to **X5R** for cost-sensitive consumer.

### Bulk decoupling, energy storage (need maximum CV)
→ **X7T / X7U** for engineered ones; **Y5V** for ultra-low-cost (with all the caveats).

### Automotive under-hood (need 125+ °C with stability)
→ **X8R** for ±15 % to 150 °C; **X8L** for moderate stability acceptable; **X0U** for 175 °C; **X9V** for 200 °C with relaxed tol.

### High-voltage (need thick d, high BDV)
→ **C0G** or **BME C0G** [[bme-c0g]] for ≥ 200 V/µm BDV; X7R serial / [[kemet-arcshield]] for ≥ 500 V applications.

### Audio / mic-bias / coupling (need low DF, no piezo)
→ **C0G** mandatory (no ferroelectric domains, no microphonic effect, no signal distortion).

## Cross-vendor naming quirks
- **Murata**: standard EIA codes (X7R, X5R, etc.) plus internal product-series codes (GRM18, GCM21, etc.). X7R can subdivide into X7R "stable" and X7R "high-CV" within the same EIA box.
- **Samsung CL series**: uses EIA codes directly in the part number (B = X7R, A = X5R, X = X6S, F = Y5V, C = C0G).
- **TDK**: C-series uses EIA codes; some specialty TDK part numbers use **X8M, X8P** internal designations beyond EIA.
- **KEMET**: occasional **B** suffix for "X7R Class II" in legacy MIL-C-55681 nomenclature.

## Why the proliferation of codes?
Each code exists because a specific application demands a specific trade-off:
- **X7R → X7S → X7T → X7U → Y5V**: progressively more εr but progressively worse temperature stability and aging — used when high CV is more important than precision.
- **X7R → X8R → X9R / X9V**: extends T_op upward; needs Curie-temperature engineering (Sr/Zr substitution to shift T_C, dopants to broaden it).
- **C0G → U2J**: increases εr in Class I by accepting larger (but linear) TCC — useful for **temperature compensation** of other circuit elements.

## Implications for the simulator
The simulator's `f_T(T)` block must implement different functional forms for each class:
- Class I (linear): `f_T = 1 + TCC × (T − 25)` with the right TCC value.
- Class II "boxed" (X7R, X8R, X8L): piecewise envelope ±15 % within range, +15/−40 % beyond X8L's range, etc.
- Class II asymmetric (X7T, X7U): use the wider negative range as worst-case.
- Class III (Y5V, Z5U): full +22/−82 % asymmetric box; do not extrapolate beyond range.

## Cross-references
- [[eia-rs-198-dielectric-classes]] — the underlying code system
- [[temperature-coefficient-of-capacitance]] — TCC primitive
- [[c0g-npo-dielectric]] — Class I deep-dive
- [[x7r-dielectric]] — Class II workhorse deep-dive
- [[x8r-x8l-x9r-high-temperature-dielectrics]] — high-T extensions
- [[y5v-z5u-class-iii-dielectric]] — Class III deep-dive
- [[curie-temperature]]
- [[core-shell-batio3]]

## References
- [[psma-ceramic-capacitor-basics]] — Class I/II/III tables
- [[samsung-cl-series-mlcc-ds]] — vendor code-to-EIA mapping
- [[escies-bme-mlcc-high-reliability]] — BME C0G vs PME C0G (CaZrO₃ vs BNT)
- [[rohm-ceramic-cap-app-note]] — Class II/III chart
- Knowles Capacitor Fundamentals Part 8
- KYOCERA AVX X8R/X8L product page
- Vishay HOTcap X9V documentation
- Passive-components.eu X8G/X8L/X8R article
