---
title: Class II MLCC Aging
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - vishay-x7r-cap-drift-dc-bias.md
  - psma-ceramic-capacitor-basics.md
  - murata-grm-series-tcc-data.md
tags:
  - paper
---

# Class II MLCC Aging

Class II/III MLCCs lose capacitance **logarithmically** over time after they cool below the [[curie-temperature]] (~125 °C for [[batio3]]). The cause is gradual re-orientation of ferroelectric domains seeking a lower-energy configuration. Class I (paraelectric) parts do not exhibit this — no domains.

## The log law
$$
C(t) \;=\; C_0 \cdot \left[1 - \tfrac{A_\text{age}}{100} \cdot \log_{10}\left(\tfrac{t}{t_\text{ref}}\right)\right]
$$
With:
- `A_age` — aging rate constant in **% per decade-hour**
- `t_ref` — reference time after de-aging (typ. 1 h)

| Class | Typical A_age |
|---|---|
| C0G / NP0 | ≈ 0 |
| X7R       | 1–2 %/decade |
| X5R       | ~5 %/decade |
| Y5V       | 5–7 %/decade |

**Reading**: a 1.5 %/decade X7R loses 1.5 % between 1 h and 10 h, another 1.5 % between 10 h and 100 h, and so on. By 100 000 h (~11 years) that is ~7.5 % total.

[[psma-ceramic-capacitor-basics]] shows the X7R limit specified as **1.5 %/decade-hour** with the reference at 1 h post heat.

## De-aging
Aging is **fully reversible** by heating above `T_c` (typically 150 °C × 1 h). Cooling resets the domain ensemble to its randomized post-Curie state, and the aging clock restarts. This is also how datasheet-spec measurements are normalized (1 day or 24 h after last heat).

## What aging does NOT mean
- It is **not** chemical degradation or wear-out — the part is electrically healthy.
- It is **not** the same as [[dc-bias-aging]], which is a much larger, time-dependent drift caused by **continuous DC bias** and can be 5–10× faster than natural aging ([[vishay-x7r-cap-drift-dc-bias]]).
- It does **not** affect reliability (insulation resistance, lifetime).

## Implication for simulator
In `simulator-model.md` § 3.4, `f_age(t)` is the multiplicative correction on `C₀`. For Class II parts the simulator must know `A_age` per material (datasheet value). At any operating point with non-zero DC bias, the **effective** aging rate is the natural rate **plus** the [[dc-bias-aging]] component, which depends on field and temperature.

## References
- [[vishay-x7r-cap-drift-dc-bias]]
- [[psma-ceramic-capacitor-basics]]
- [[murata-grm-series-tcc-data]]
