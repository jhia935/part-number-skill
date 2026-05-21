---
title: "Liu, Liu, Lu, Li, Zheng — Dense Sm-Mn Co-Doped BaTiO₃ Ceramics with High Permittivity (Materials 2019)"
type: source
created: 2026-05-21
updated: 2026-05-21
sources:
  - resources/literature/liu-2019-sm-mn-codoped-batio3-permittivity.md
tags:
  - paper
status: complete
importance: high
---

# Liu et al. — Sm-Mn Co-Doped BaTiO₃ with High Permittivity (Materials 2019)

**Source:** `resources/literature/liu-2019-sm-mn-codoped-batio3-permittivity.md` (WebFetch extract from PMC)
**Authors:** Q. Liu, J. Liu, D. Lu, T. Li, W. Zheng
**Journal:** *Materials* 12 (4) (2019) 678
**DOI:** 10.3390/ma12040678 (open access, MDPI)

## Summary

A focused study of (Ba₁₋ₓSmₓ)(Ti₀.₉₉Mn₀.₀₁)O₃ ceramics with Sm donor content swept from 2 to 7 mol% at fixed Mn 1 mol% acceptor. The headline result: **peak permittivity climbs from ~5,500 to ~15,000 across the Sm sweep**, with the Curie temperature dropping from 105 °C to 20 °C. The mechanism is the **2 Sm_Ba• — Mn_Ti″ donor-acceptor defect complex**: a charge-compensated, electrically neutral defect cluster that suppresses space-charge polarization and lets ionic-displacement polarization dominate across 1 Hz–1 MHz.

This is a **directly recipe-actionable dataset** for the εr-from-dopant simulator: it gives the slope of ε' vs Sm mol% and T_C vs Sm mol% over a useful design range.

## Key quantitative findings

### Composition

| Species | Site | Loading |
|---|---|---|
| Sm³⁺ | A-site (substitutes Ba²⁺) | 2–7 mol% (the sweep variable) |
| Mn²⁺ | B-site (substitutes Ti⁴⁺) | 1 mol% (held constant) |

### Permittivity scaling with Sm

| Sm content (mol%) | Peak ε' (ε'_max) | RT ε' |
|---|---|---|
| 2 | **5,480** | — |
| 7 | **15,220** | **13,810** |

Linear interpolation slope: **+1,950 / mol% Sm** for peak ε'.

### Curie-temperature shift

| Sm content (mol%) | T_C (°C) |
|---|---|
| 2 | 105.5 |
| 7 | 20.4 |

Slope: **−17.0 °C / mol% Sm**.

### Dielectric loss

- tan δ < 0.03 across the temperature range tested. Meets typical MLCC dielectric-loss specs.

## Mechanism: 2 Sm_Ba• — Mn_Ti″ defect complex

Charge balance:
- Sm³⁺ at Ba²⁺ site: defect notation Sm_Ba• (one positive effective charge)
- Mn²⁺ at Ti⁴⁺ site: defect notation Mn_Ti″ (two negative effective charges)
- Stoichiometric ratio 2 Sm : 1 Mn for charge neutrality

The Sm doping also drives the **reduction of Mn**: in pure BaTiO₃ Mn would be Mn³⁺ or Mn⁴⁺, but Sm³⁺ donor doping shifts the equilibrium to **Mn²⁺**, stabilizing the tetragonal ferroelectric phase and preventing the otherwise problematic hexagonal phase from appearing.

The compensation is the critical feature: a charge-neutral defect complex **does not act as a space-charge polarization center**, so ε' stays high without losses across the Hz–MHz range.

## Implications for the simulator

This study, combined with similar single-RE / Mn co-doping studies, suggests a useful empirical model for ε_r:

$$
\varepsilon_r(\text{RE}_x, T_C^0) \approx \varepsilon_r^0 + \alpha_{\text{RE}} \cdot x
$$
$$
T_C(\text{RE}_x) \approx T_C^0 + \beta_{\text{RE}} \cdot x
$$

with `α_RE` and `β_RE` characteristic of each rare-earth species (depends on ionic radius and Pauling electronegativity). For Sm specifically:
- α_Sm ≈ +1,950 / mol% (at fixed 1 mol% Mn)
- β_Sm ≈ −17 °C / mol%

A simulator could load such (α, β) per RE species and predict ε_r and T_C for arbitrary multi-RE-doped recipes by superposition (to leading order). Validation against published datasheets from [[murata]] and [[samsung-electro-mechanics]] would close the loop.

## Caveats / open issues

- Only one Sm:Mn stoichiometry was tested (2:1). Off-stoichiometric ratios would reintroduce space-charge polarization.
- Grain size effects are not separated from composition effects — the ε' values include grain-boundary contributions that vary with sintering profile.
- T_C below room temperature (at x = 0.07) means the part is paraelectric at room temperature — the relevant operating range. ε' values come from soft-mode behavior approaching T_C from above; very temperature-sensitive.
- The Sm-Mn system is **not directly used in commercial X7R / X5R MLCC** — those use Y/Mn/Mg or Dy/Mn/Mg co-doping with finer grain size. But the mechanism is the same.

## Entities mentioned

- (Authors are at a Chinese institution; the paper does not name commercial partners.)

## Concepts discussed

- [[epsilon-r-from-dopant-composition]] — direct topic.
- [[dopant-site-occupancy-batio3]] — A-site vs B-site preference; Sm³⁺ goes to Ba²⁺ site for ionic-radius reasons.
- [[defect-chemistry-batio3]] — Kröger-Vink notation for the donor-acceptor complex.
- [[core-shell-batio3]] — Sm/Mn co-doping is one of many MLCC core-shell recipes.
- [[curie-temperature]] — the dopant shifts T_C dramatically.
- [[dopant-powder-coating]] — likely application route (Sm + Mn coated on BT powder before sintering).

## Notable quote

> "Formation of 2 Sm_Ba• — Mn_Ti″ donor-acceptor defect complexes prevents space charge polarization effects, enabling ionic displacement polarization to dominate across a broad frequency range (1–10⁶ Hz), thereby maintaining consistently high permittivity values."

## References

_Open-access via PMC: `resources/literature/liu-2019-sm-mn-codoped-batio3-permittivity.md`_
