---
title: Barium Titanate (BaTiO₃)
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - psma-ceramic-capacitor-basics.md
  - vishay-x7r-cap-drift-dc-bias.md
  - nasa-batio3-mlcc-failure-mechanisms.md
tags:
  - material
status: complete
importance: high
---

# Barium Titanate (BaTiO₃)

A [[perovskite-structure|perovskite-structure]] ferroelectric oxide. The dominant base dielectric material for **Class II / Class III** MLCCs — essentially all X5R, X7R, X8R, X6S, Y5V, Z5U capacitors are BaTiO₃-based. Pure [[cazro3|CaZrO₃]] and similar paraelectric oxides serve Class I (C0G) instead.

## Crystal structure & ferroelectricity
- **Above ~125–130 °C (Curie temperature `T_c`)**: cubic, paraelectric, no permanent dipole. `εr` modest (a few hundred up to a peak near `T_c` of 10 000–15 000).
- **Below `T_c`**: tetragonal, ferroelectric, permanent off-center Ti displacement creates a permanent dipole. Domain walls; high `εr` (1500–6000 depending on grain size and chemistry); aging, DC-bias derating, piezoelectricity all enter here.

`T_c` can be shifted by doping (Sr → lower, Ca/Pb → higher).

## εr vs grain size (the modern central trade-off)
- Coarse grain (~1 µm): εr ≈ 1500–2000 at room temperature, 6000 with peak engineering.
- Sub-µm (200–500 nm): εr drops, then rebounds. At ~200–260 nm, εr can be 3000–5000 under DC bias > 4 V/µm — this is the sweet spot for thin-layer MLCCs (An et al., *Adv. Mater.* 2026, [doi:10.1002/adma.202507233](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202507233)).
- Below ~150 nm: εr collapses as grains lose ferroelectricity (insufficient long-range order).

## Powder synthesis
- **Solid-state reaction** (cheap, coarse): BaCO₃ + TiO₂ → BaTiO₃, large powder.
- **Hydrothermal** (modern fine-grain): low-temperature aqueous synthesis, sub-100 nm powder. [[murata]] uses ~100 nm powder; Korean competitors historically at 300–500 nm.
- **Oxalate route** (intermediate).

## Dopant chemistry for MLCCs
- **Rare-earth donors** (Y, Ho, Dy, Er, Yb, Tb): create the paraelectric shell of [[core-shell-batio3]]; pin oxygen vacancies; flatten TCC.
- **Mg / Mn acceptors**: charge compensation; stabilize against reduction during reducing-atmosphere BME firing.
- **Co-doping ratios** are the active patent space (see [[murata]], [[samsung-electro-mechanics]] patent activity).

## Why BaTiO₃ "moves" under DC bias and signal
- DC bias pins domain alignment → εr drops → [[dc-bias-derating]].
- Long-time DC bias drives slow domain redistribution → [[dc-bias-aging]].
- Time alone drives domain relaxation → [[aging-class-2]].
- AC signal can re-orient domain walls → piezoelectricity and electrostriction → audible "singing" cap problem at high AC fields.
- Heating above `T_c` randomizes domains → full de-aging reset.

## See also
- [[eia-rs-198-dielectric-classes]]
- [[core-shell-batio3]]
- [[bme-reliability-model]]
- [[dc-bias-derating]]
