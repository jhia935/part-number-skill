---
title: X7R (Class II Workhorse Dielectric)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - psma-ceramic-capacitor-basics.md
  - escies-bme-mlcc-high-reliability.md
  - vishay-x7r-cap-drift-dc-bias.md
tags:
  - paper
---

# X7R (Class II Workhorse Dielectric)

The default Class II dielectric for **general-purpose decoupling, bypass, and bulk capacitance**. Operating range **−55 to +125 °C** with ΔC ≤ ±15 %. εr typically **600–4000** depending on formulation and grain size. Built from [[batio3|BaTiO₃]] with [[core-shell-batio3|core-shell]] microstructure and rare-earth + Mg + Mn co-doping. Almost every consumer / industrial / automotive PCB uses thousands of X7R MLCCs.

## Spec envelope
- **EIA code**: X = T_low −55 °C, 7 = T_high +125 °C, R = ΔC ±15 % across the range.
- **Aging rate**: industry spec **≤ 1.5 %/decade-hour** ([[aging-class-2]]).
- **DF max**: 2.5 % (at 25 °C, 1 kHz, low V_AC; rises at low V_r and high V_AC).
- **Withstand voltage**: 250 % rated V for 1–5 s per AEC-Q200.
- **Operating temp envelope**: full −55 to +125 °C.

## Why X7R is the workhorse
- **Good balance** of capacitance density (much higher than [[c0g-npo-dielectric|C0G]]) and stability (much better than [[y5v-z5u-class-iii-dielectric|Y5V]]).
- **Widest cap range** of any Class II — from sub-pF to 22 µF in case sizes 0201–2220.
- **Highest BDV per µm** among Class II.
- **Most predictable aging** (1–2 %/decade, low scatter) — vendor data is trustworthy.

## Material engineering
X7R formulations are not just "BaTiO₃" — they're engineered solid solutions of:
- BaTiO₃ (the high-εr ferroelectric core)
- Sr or Zr substitution at A or B sites to **shift T_C just outside the −55 to +125 °C window** (or smear it across the upper end)
- Rare-earth dopants (Y, Ho, Dy, Er) on A and/or B sites for [[core-shell-batio3|core-shell shell]] formation
- Mg + Mn acceptors for V_O compensation and grain-growth control
- Sometimes a small fraction of relaxor-like materials (BNT, BiScO₃) for additional Curie-peak broadening

The resulting **flattened Curie peak**, combined with the core-shell shell's paraelectric response, keeps εr within ±15 % of the 25 °C value across the full operating range.

## Where X7R falls short
1. **DC bias derating** is severe at high field. A 10 µF / 6.3 V / 0805 X7R can drop −35 % to −65 % at rated voltage ([[epci-high-cv-mlcc-bias-aging|EPCI 2019]]). The simulator must use field-not-voltage logic for sensible prediction.
2. **AC-bias drift**: −5 % to −15 % at small (10 mV) AC drive vs the 1 V_rms test standard.
3. **DC-bias-aging slow tail**: −7 % to −10 %/decade at rated V in BME competitors ([[vishay-x7r-cap-drift-dc-bias|Vishay 2021]]).
4. **Piezo / microphonic noise** at high AC drive (audible "singing" caps). For audio paths, switch to C0G.
5. **Temperature limit at 125 °C** — above this, εr drops sharply past ±15 % and the part no longer meets EIA X7R spec. Use [[x8r-x8l-x9r-high-temperature-dielectrics|X8R/X8L]] for automotive under-hood.

## Cousins within "X7-something"
The X7-prefix family is engineered for the **same** −55 to +125 °C range but with different ΔC tolerance / εr trade-offs:
- **X7R** (ΔC ±15 %): the baseline
- **X7S** (ΔC ±22 %, higher εr): more cap density at relaxed tolerance — Murata recommends X7S over X7R for some CPU-decoupling cases because under actual DC-bias / AC-drive operating conditions, X7S delivers more effective capacitance.
- **X7T** (ΔC +22/−33 %, higher εr still): asymmetric tolerance; allows greater positive drift; even more CV per case.
- **X7U** (ΔC +22/−56 %): relaxor-leaning; high εr; bulk decoupling only.
- **X7P** (ΔC ±10 %): tightest tolerance in the X7 family; for tighter-spec apps.

The choice depends on whether the application tolerates the bigger negative drift in exchange for higher initial εr.

## Vendor variation
Per [[electrical-integrity-dce11-200|Novak DesignCon 2011]], **same nominal 1 µF / 0603 / 16 V / X7R from different vendors** shows **0 % to −80 %** DC-bias drift at +20 V. Within-vendor "X7R" can also vary depending on internal sub-grade. The lesson: **specify by part number, not just by class code**, especially for safety-critical apps.

## Implications for the simulator
- `f_T(T)` for X7R: piecewise sigmoid centered on the broadened Curie peak (~75–100 °C in modern X7R, shifted from bulk BaTiO₃'s 120 °C by Zr/Sr doping). The ±15 % envelope is the worst-case bound; actual curves can be ~±5 % for premium parts and full ±15 % for high-CV grades.
- `f_VCC(E)`: sigmoid with **E₀ ≈ 5 V/µm, p ≈ 1.3** for typical X7R. Vendor / grade specific.
- `A_age`: 1–2 %/decade typical; 1.5 % industry limit.
- Reliability `E_k`: 1.6 eV commercial, 2.8 eV automotive grade ([[nasa-time-dependent-ir-2013-prb]]).

## Cross-references
- [[eia-rs-198-dielectric-classes]]
- [[dielectric-class-comparison]]
- [[core-shell-batio3]]
- [[batio3]]
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[dc-bias-aging]]
- [[curie-temperature]]
- [[temperature-coefficient-of-capacitance]]

## References
- [[psma-ceramic-capacitor-basics]]
- [[escies-bme-mlcc-high-reliability]]
- [[vishay-x7r-cap-drift-dc-bias]]
- [[epci-high-cv-mlcc-bias-aging]]
- [[electrical-integrity-dce11-200]]
- Murata FAQ: X7R vs X7S vs X7T
