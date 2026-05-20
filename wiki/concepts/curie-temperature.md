---
title: Curie Temperature (T_C)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - vishay-x7r-cap-drift-dc-bias.md
  - arxiv-batio3-cubic-to-tetragonal-md.md
tags:
  - paper
---

# Curie Temperature (T_C)

The temperature above which a ferroelectric material loses its spontaneous polarization and transitions from the **tetragonal (or rhombohedral / orthorhombic) ferroelectric phase** to the **cubic paraelectric phase**. For [[batio3|bulk BaTiO₃]], `T_C ≈ 393 K = 120 °C` (some sources give 122–130 °C depending on dopants, grain size, and stress state).

## Why T_C matters for MLCC engineering
1. **Sets the operating envelope** for Class II / III dielectrics. Below T_C: ferroelectric, all the [[dc-bias-derating|VCC]], [[aging-class-2|aging]], piezoelectric effects apply. Above T_C: linear paraelectric, εr drops to the intra-domain value (~1500 vs 5000+ in the peak), but no aging.
2. **Causes the [[cubic-tetragonal-transition|εr peak]] at T_C** — εr can spike to 9000–15 000 right at T_C in undoped BaTiO₃ (the diverging soft-mode susceptibility). This is the **Curie-Weiss singularity**.
3. **Defines the "aging clock reset" temperature**: heating any Class II part above T_C for 1 h randomizes the domain structure, fully recovering all aging and DC-bias-aging losses. Reflow soldering does this for solder joints near 150 °C; deliberate "de-aging" anneals run at the same condition.

## Curie-Weiss law
For a ferroelectric above T_C:
$$
\varepsilon_r \;=\; \varepsilon_\infty \;+\; \frac{C}{T - T_0}
$$
- `C` = Curie constant (~10⁵ K for BaTiO₃ — explains the huge εr at high T)
- `T_0` = Curie-Weiss temperature (slightly below T_C; difference attributed to "dead-layer" effects in real ceramics)
- The (T − T_0)⁻¹ divergence at T → T_0 is why εr peaks near T_C.

Below T_C, a different temperature dependence governs (still hyperbolic but with different coefficients).

## T_C shifting by chemistry
T_C is **the** primary handle for tailoring temperature stability of a Class II dielectric:
- Substitute **Sr²⁺ for Ba²⁺** → T_C drops (BST formulations).
- Substitute **Zr⁴⁺ for Ti⁴⁺** → T_C drops dramatically (BZT formulations).
- Substitute **Pb²⁺ for Ba²⁺** → T_C rises (PbTiO₃ is ferroelectric to 490 °C; restricted by RoHS today).
- **Heavy rare-earth doping** flattens and shifts the Curie peak laterally — the basis of X8R / X8L / X9R high-temperature dielectrics.

## T_C vs grain size
In fine-grain ([[batio3|sub-200 nm grain]]) BaTiO₃, the **effective T_C drops** and the transition broadens — eventually disappearing below ~30 nm (the critical size for ferroelectricity). [[cubic-tetragonal-transition|Cooldown stress]] retained in fine grains suppresses tetragonal distortion → effective behavior is paraelectric even below the bulk T_C.

## Practical T_C numbers
| Material | T_C |
|---|---|
| BaTiO₃ (bulk, undoped) | 120 °C |
| BaTiO₃ (commercial X7R) | shifted to ~ 70–80 °C by Zr/Sr doping (so that ±15 % εr drift falls within −55 to +125 °C window) |
| X8R-grade BaTiO₃ | shifted to ~ 130–140 °C |
| X8L industry (KEMET) | broadened/shifted to stay within ±15 % to 150 °C, then +15/−40 % to 150 °C |
| PbTiO₃ | 490 °C (RoHS-restricted now) |
| SrTiO₃ | < 0 K (quantum paraelectric; no T_C in operating range) |
| CaZrO₃ | no ferroelectric T_C (paraelectric throughout) |

## Cross-references
- [[batio3]]
- [[cubic-tetragonal-transition]]
- [[ferroelectric-domain-wall]]
- [[aging-class-2]]
- [[dc-bias-derating]]
- [[srtio3]], [[cazro3]] — paraelectric counterparts
- [[arxiv-batio3-cubic-to-tetragonal-md]]
- [[vishay-x7r-cap-drift-dc-bias]] — aging/de-aging description
