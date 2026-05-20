---
title: "Sugimura & Hirao — BaTiO₃ Nanoparticle Additive Effect on Ni Electrode Quality (J. Ceram. Soc. Jpn. 2009)"
type: source
created: 2026-05-21
updated: 2026-05-21
sources:
  - resources/literature/sugimura-hirao-2009-batio3-additive-ni-electrode.md
tags:
  - paper
status: complete
importance: high
---

# Sugimura & Hirao — BaTiO₃ Nanoparticle Additive Effect on Ni Electrode Quality (2009)

**Source:** `resources/literature/sugimura-hirao-2009-batio3-additive-ni-electrode.md` (WebFetch citation + key data from J-STAGE; full PDF behind registration)
**Authors:** Ken-ichi Sugimura (Noritake Kizai Co., Ltd.), Kazuhisa Hirao (Noritake Co., Ltd.)
**Journal:** *Journal of the Ceramic Society of Japan* 117 (2009) 1039–1043
**DOI:** 10.2109/jcersj2.117.1039

## Summary

A Noritake-industry paper that quantifies the **size and loading sensitivity of the nano-BT-in-Ni-paste additive** for MLCC inner electrodes. Establishes the industry-standard recipe of **~10 mass% BaTiO₃ additive at 30 nm particle size** for ~0.2 µm Ni powder, achieving > 75 % Ni film coverage on the dielectric.

This is the **"size matters more than mass"** result: smaller additive particles dramatically outperform larger ones at the same loading.

## Key quantitative data

| Parameter | Value |
|---|---|
| Ni powder size | ~0.2 µm (industry-typical sub-µm BME Ni) |
| BaTiO₃ additive sizes tested | 30, 50, 100 nm |
| BaTiO₃ loadings tested | 10–20 mass% |
| **Optimal additive size** | **30 nm** |
| **Optimal additive loading** | **10 mass%** |
| **Achieved Ni film coverage** | **> 75 %** |

## Headline findings

1. **The BaTiO₃ additive plays two roles**:
   - Mechanically retards Ni sintering ([[bordia-scherer-composite-sintering|rigid-inclusion retardation]]).
   - **Protects Ni from oxidation** by physically coating the Ni surface.

2. **Onset-temperature shift**: a polycrystalline BT coating on Ni raises the Ni shrinkage onset temperature, narrowing the Ni-vs-BT-dielectric onset gap from ~450 °C to ~250–350 °C in well-formulated pastes. This pulls the Ni shrinkage curve closer to the dielectric's so cofiring tensile stress drops.

3. **Particle-size scaling**: at the same 10 mass% loading, **30 nm BT achieves >75 % coverage while 50 and 100 nm BT do not**. To reach the same coverage with 50 nm BT, mass% must be increased — and increasing loading hurts electrode conductivity.

## Connection to other sources

This paper provides the **empirical industry validation** of the DEM-predicted retardation curves from [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis]] (Ch. 6):
- Yan predicted (DEM, 60 nm BT in 180 nm Ni, D = 0.70): retardation factor 7× at 20 vol%.
- Sugimura-Hirao measured (real paste, 30 nm BT in 200 nm Ni): > 75 % coverage at 10 mass%.

Both point at the same conclusion: **small + well-dispersed + ~5–15 vol% is the sweet spot**.

## Implications for MLCC paste design

| Loading (mass%) | Particle size (nm) | Result |
|---|---|---|
| 0 | — | Ni shrinks uncontrolled → catastrophic break-up at 1200 °C |
| 5 | 30 | Marginal retardation; some discontinuity |
| **10** | **30** | **Industry sweet spot: > 75 % coverage** |
| 15 | 30 | Diminishing returns on coverage; conductivity drops |
| 20+ | 30 | Electrode percolation threshold approached; resistance rises |
| 10 | 50 or 100 | Insufficient retardation; need higher mass% |

## Concepts discussed

- [[ni-electrode-paste-formulation]] — primary topic of this paper.
- [[ni-batio3-cosintering-interface]] — BT additive narrows the Ni / BT shrinkage gap.
- [[metal-electrode-shrinkage-effect]] — additive content is the main shrinkage knob on the Ni side.
- [[bordia-scherer-composite-sintering]] — theoretical framework for the inclusion-retardation effect.

## References

_J-STAGE link: https://www.jstage.jst.go.jp/article/jcersj2/117/1369/117_1369_1039/_article_

Related and confirmatory:
- Kang, Joo, Cha, Jung, Paik, "Shrinkage behavior and interfacial diffusion in Ni-based internal electrodes with BaTiO₃ additive", *Ceram. Int.* 34 (2008) 1487 — independent confirmation of the additive-size effect on Ni shrinkage.
- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — DEM simulation that predicts the same retardation curves.
