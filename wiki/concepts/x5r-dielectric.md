---
title: X5R (Class II Lower-Temp Dielectric)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - rohm-ceramic-cap-app-note.md
  - epci-high-cv-mlcc-bias-aging.md
tags:
  - paper
---

# X5R (Class II Lower-Temp Dielectric)

The volume-dominant Class II dielectric for **consumer electronics** (smartphones, tablets, laptops). Operating range **−55 to +85 °C** with ΔC ≤ ±15 %. The "5" digit (T_max = +85 °C) is the **only** difference from [[x7r-dielectric|X7R]]; everything else — chemistry, εr range, voltage spec format — is essentially the same.

## Why X5R exists despite X7R being superior
- **Lower cost**: relaxed T_max → less stringent dopant engineering → ~ 10–20 % cheaper per µF than equivalent X7R.
- **Higher CV per case**: vendors can use slightly higher-εr (less heavily doped) BaTiO₃ because they don't have to maintain stability up to 125 °C → more cap in the same case size.
- **Consumer electronics rarely sees > 70 °C**: smartphone PCB ambient ~ 40–55 °C, server motherboards ~ 70 °C. The X7R extra 40 °C of stable range is unused.

## Spec envelope
- **EIA code**: X = T_low −55 °C, 5 = T_high **+85 °C**, R = ΔC ±15 %.
- **Aging rate**: typically ~ 5 %/decade-hour (higher than X7R because less doping → faster domain re-orientation).
- **DF max**: 2.5 % at 25 °C, 1 kHz, low V_AC.
- **εr range**: 1000–3000 typical for commercial X5R (vs 600–4000 for X7R).

## DC-bias derating
Generally **worse** than X7R for the same nominal cap and case size. [[epci-high-cv-mlcc-bias-aging|EPCI 2019]] data:
- 1 µF / 6.3 V / 0402 / X5R: drops ~ −70 % at 6.3 V_dc
- Same case / value as **X7R**: drops ~ −40 % at 6.3 V_dc

The mechanism: X5R formulations sit closer to the bulk BaTiO₃ Curie peak (no engineered shifting → higher peak εr at 25 °C → harder field-pinning behavior).

## When to use X5R
- **Smartphone / consumer**: low-cost, low-thermal-stress decoupling
- **High-cap bulk decoupling** (10 µF+) in 0805/1206 cases where X7R would be more expensive or unavailable
- **Battery-management** in handhelds (ambient < 60 °C)

## When NOT to use X5R
- Automotive (T_max routinely exceeds 85 °C)
- Industrial high-T (steel mill electronics, oil/gas)
- Anywhere ambient + self-heating could push the part past 85 °C
- **High-reliability** apps: the looser aging spec compounds with DC-bias-aging

## ROHM size/V_r comparison (10 µF / B-char ≈ X7R; lessons apply to X5R too)
- Same V_r, smaller case → thinner d → larger E → worse DC-bias derating
- Same case, lower V_r → thicker d for the same nominal cap → better DC-bias derating
- See [[rohm-ceramic-cap-app-note|ROHM 62AN089E]] for the concrete charts (1608 vs 2012 vs 3216 at 10 µF / 10 V).

## Cross-references
- [[x7r-dielectric]]
- [[dielectric-class-comparison]]
- [[eia-rs-198-dielectric-classes]]
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[core-shell-batio3]]

## References
- [[rohm-ceramic-cap-app-note]]
- [[epci-high-cv-mlcc-bias-aging]]
- [[psma-ceramic-capacitor-basics]]
- [[murata-grm-series-tcc-data]]
