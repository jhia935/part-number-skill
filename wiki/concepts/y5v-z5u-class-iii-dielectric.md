---
title: Y5V / Z5U (Class III High-K Dielectrics)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - rohm-ceramic-cap-app-note.md
  - murata-grm-series-tcc-data.md
tags:
  - paper
---

# Y5V / Z5U (Class III High-K Dielectrics)

The **highest capacitance density per case size** at the cost of **wildly varying capacitance over temperature, DC bias, and time**. εr typically **4000–18 000**. Mostly being **phased out** in favor of [[x5r-dielectric|X5R]] (which has improved enough on εr in modern formulations to challenge Y5V on volumetric efficiency, at much better stability). Still found in legacy and ultra-cheap consumer designs.

## Spec envelope

| Code | T_op | ΔC envelope | εr range | Aging | DF max | Notes |
|---|---|---|---|---|---|---|
| **Y5V** | −30 to +85 °C | **+22 / −82 %** | 4000–18 000 | **5–7 %/decade** | up to **16 %** at 6.3 V | Legacy bulk decoupling |
| **Z5U** | **+10 to +85 °C** | +22 / −56 % | 4000–14 000 | 5–7 %/decade | up to 12 % | Even more restrictive T-range |

Note that **Z5U doesn't work below +10 °C** — quite literally outside its spec from a cold-morning startup. Y5V has a useful low-T floor of −30 °C, still poor compared to X-prefix Class II.

## Material chemistry
Y5V / Z5U are **relaxor-leaning** [[batio3|BaTiO₃]]-based formulations:
- Higher BaTiO₃ ratio (less dopant) → higher εr but narrower stability window
- Some compositions include **PbZrTiO₃ (PZT)** or **PbLaZrTiO₃ (PLZT)** relaxor materials — restricted by RoHS in most markets
- Heavy A-site or B-site cation substitution to create diffuse-phase-transition relaxor behavior
- Less rare-earth dopant → less [[core-shell-batio3|core-shell]] engineering → cheaper

## Why Y5V / Z5U **fail** in practical designs

### Temperature collapse
At +85 °C end: Y5V can be at **−82 %** of room-T value. A 10 µF nominal becomes 1.8 µF effective. At Murata GRM21 / Y5V / 50 V data ([[murata-grm-series-tcc-data]]), the temperature curve drops dramatically from +25 to +85.

### DC bias collapse
Even worse — a Y5V at rated voltage can lose **−90 %** of its nominal capacitance ([[murata-grm-series-tcc-data]] Fig. for 50 V / Y5V). Combined with temperature, the part is effectively **gone**.

### Aging
At 7 %/decade, a Y5V loses ~ 32 % of nominal over 10 years from aging alone, plus all the above.

### Combined operating-point loss
[[epci-high-cv-mlcc-bias-aging|Zednicek 2019]] multiplicative example: a Class II part can drop to 10 % of nominal CV under combined V_DC + V_AC + T + aging. **Class III is worse** because the individual factors are larger.

For Y5V: a typical operating-point CV could be 5–10 % of nameplate. The capacitor is essentially advertised but not delivered.

## When Y5V / Z5U are still defensible
1. **Climate-controlled consumer enclosures (laptops, indoor IoT)** at fixed-voltage rails with significant headroom.
2. **Supplementary bulk decoupling** in parallel with X7R or tantalum primary caps — the Y5V provides occasional extra storage but isn't relied on.
3. **Audio-frequency low-impedance bypass** where capacitance accuracy doesn't matter.
4. **Ultra-low-cost legacy designs** where bill-of-materials cost dominates everything else.

## Where they fail
1. **Power supply primary decoupling** — voltage sag during transients because actual CV is much lower than spec.
2. **Timing circuits, RC filters** — temperature drift will detune any design.
3. **Automotive** — temperature range alone disqualifies (T_max = 85 °C; auto demands ≥ 125 °C).
4. **Long-life industrial** — aging eats away too much over 10+ years.
5. **Anywhere ambient T can go below 0 °C** (excludes Z5U) or below −30 °C (excludes Y5V).

## The phase-out trend
Major vendors (Murata, [[samsung-electro-mechanics]], [[tdk]]) are gradually **deprecating Y5V / Z5U** lines in favor of improved X5R formulations. The argument:
- Modern X5R achieves εr ~ 3000–4000 in commercial production — within striking distance of legacy Y5V's "typical 6000–8000".
- X5R aging is ~ 5 %/decade vs Y5V's 7 %/decade.
- X5R operating range goes down to −55 °C (vs Y5V's −30 °C, Z5U's +10 °C).
- **Bottom line**: a modern X5R at the same case + V_r gets you 70 % of Y5V's nominal CV with 3× better stability — a much better deal.

[[rohm-ceramic-cap-app-note|ROHM]] explicitly warns: "Do not use Y5V, Z5U capacitors in power circuit as it may cause trouble." That's industry consensus by 2020.

## Implications for the simulator
- `f_T(T)` for Y5V: full +22/−82 % asymmetric box from −30 to +85 °C. Outside this range, **undefined** — the simulator should refuse to operate beyond spec.
- `f_VCC(E)`: sigmoid with E₀ ≈ 1.5 V/µm, p ≈ 1.0 — much sharper than X7R.
- Aging: A_age = 5–7 %/decade in the simulator.
- DF rises steeply with applied AC bias.

## Cross-references
- [[eia-rs-198-dielectric-classes]]
- [[dielectric-class-comparison]]
- [[x5r-dielectric]] — the modern replacement
- [[batio3]]
- [[core-shell-batio3]]
- [[dc-bias-derating]]
- [[aging-class-2]]

## References
- [[rohm-ceramic-cap-app-note]]
- [[murata-grm-series-tcc-data]] — Y5V graphs
- [[epci-high-cv-mlcc-bias-aging]] — multiplicative-factor loss
- [[psma-ceramic-capacitor-basics]]
- pcbsync.com Y5V Capacitor guide
- electronics-notes.com ceramic dielectric types
