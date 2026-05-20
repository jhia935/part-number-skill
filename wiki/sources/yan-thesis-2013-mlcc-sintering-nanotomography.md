---
title: "Yan, Z. — Microstructure Evolution during Sintering of MLCCs: Nanotomography and Discrete Simulations (PhD thesis 2013)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/tu-darmstadt-mlcc-sintering-thesis.md
tags:
  - thesis
status: complete
importance: high
---

# Yan — PhD thesis: MLCC Sintering Nanotomography + DEM (TU Darmstadt / Grenoble, 2013)

**Source:** `resources/literature/tu-darmstadt-mlcc-sintering-thesis.md` (PDF: `resources/literature/pdf/tu-darmstadt-mlcc-sintering-thesis.pdf`, ~11 MB, 235 pages)
**Author:** Zilin Yan (Hubei, P.R.China)
**Supervisors:** Christophe L. Martin (SIMaP/GPM2, U. Grenoble); Olivier Guillon, Jürgen Rödel (TU Darmstadt); Didier Bouvard (Grenoble)
**Date:** Defense 17 October 2013, published Darmstadt 2014. Erasmus Mundus IDS-FUNMAT joint PhD.
**Companion paper:** [[epj-in-situ-xray-tomography-dem]] — 2017 conference paper distilling part of this work.

## Summary

Full PhD thesis behind the Grenoble + Argonne + Jülich MLCC sintering studies. Combines **in-situ synchrotron X-ray nano-CT** (30 nm resolution, Advanced Photon Source / Argonne) and **FIB-SEM nanotomography** (5 nm voxel) with **discrete element simulations (dp3D code)** to track how Ni inner electrodes evolve from green to fired state inside a 0603/1206 SEMCO MLCC.

Central result: **electrode discontinuity originates from initial heterogeneity in the green compact, not from the peak-temperature mechanism.** The discontinuity is locked in below 1000 °C, at the stage where the Ni layer is sintering under tensile constraint from the surrounding (still-cold) BaTiO₃ matrix.

## Materials studied

- **Powders**: Ni powder (Shoei Chemical, PVD-grown, near-spherical, sub-µm) + X5R BT powder (NanoAmor, solid-state synthesis, irregular shape).
- **Ni paste recipe**: 55 vol% Ni + nano-BT additive (Ni:BT = 100:7 by weight) + 41 vol% terpineol + 4 vol% resin.
- **MLCC samples**: EIA 1206 (3.2 × 1.6 × 1.6 mm) and EIA 0603 (1.6 × 0.8 × 0.8 mm), fabricated at Samsung Electro-Mechanics. Dielectric sheets 2.5 µm thick; electrodes 1.2 µm thick by screen printing.
- **Sintering**: 2% H₂ in Ar, peak 1150–1200 °C, holding 30–60 min.

## Key quantitative findings (highly relevant to shrinkage)

### Bulk MLCC shrinkage curve (1206 chip)
| Stage | Linear shrinkage |
|---|---|
| 25 → 950 °C (Ni sinter only) | **~0%** — no macroscopic shrinkage; Ni densification of the thin electrode layer doesn't show at chip scale because it's geometrically constrained |
| 950 → 1150 °C (BT sinter window) | **6–7%** linear |
| 1150 °C hold, 0 → 30 min | additional ~5–6% → **~12% total linear shrinkage** |
| 1150 °C hold, > 30 min | **flat** — no further shrinkage |

The macroscopic shrinkage **belongs to the BT skeleton**, not the Ni. The Ni densifies between 450–950 °C but contributes negligibly because its volume fraction in the chip is small and it's geometrically constrained by the still-rigid BT.

### Ni vs BT shrinkage onset gap
| Material | Onset T | Max rate T | End-of-densification T |
|---|---|---|---|
| Ni electrode paste | ~450 °C | ~900 °C | ~1150 °C (rate ≈ 0) |
| BaTiO₃ X5R dielectric | ~900–950 °C | ~1150 °C | post-30 min hold |

**Ni starts sintering 450 °C below BT.** This shrinkage-onset offset is the entire engineering problem of [[ni-batio3-cosintering-interface|Ni/BT cofiring]] — the Ni wants to densify while the dielectric is still a cold rigid skeleton.

### BT-additive retardation effect on Ni sintering (DEM simulations, Ch. 6)
DEM was used to simulate Ni matrix (180 nm monosize particles) with rigid BT inclusions. Quantitative results at relative density `D` = 0.70:

| Inclusion vol % | Inclusion size (nm) | Dispersion | Retarding factor (free-Ni rate / composite rate) |
|---|---|---|---|
| 0 (pure Ni) | — | — | 1.0 (baseline) |
| 5 | 60 | random | ~1.5 (noticeable already with little additive) |
| 20 | 300 | random | **2** |
| 20 | 100 | random | ~4 |
| 20 | 60 | random | **7** |
| 20 | 60 | agglomerated (300 nm clusters) | weaker than random — clusters lose effectiveness |

**Two design knobs for retarding Ni sintering**: (1) increase inclusion **volume fraction**, (2) decrease inclusion **size**. Smaller is much more effective per vol%: at 20 vol%, going from 300 nm to 60 nm inclusions raises the retarding factor from 2 to 7. **Dispersion matters too** — agglomerated BT clusters of the same total mass do not retard nearly as well as well-dispersed nano-BT.

### Heterogeneity → discontinuity mechanism (Ch. 5 + Ch. 7)
1. After lamination there are inevitable heterogeneous (thin/thick) regions in the green electrode layer.
2. Below 950–1000 °C, Ni densifies everywhere except the thin/dilute heterogeneous zones where **desintering** is observed.
3. Tensile stress in thinner sections drives matter flow toward thicker sections.
4. Thinner sections rupture → electrode discontinuity.
5. After 1000 °C, when BT starts to densify and shrinks the matrix, Ni is put under **compressive stress** → viscous Ni contracts and forms further islands (Rayleigh-Plateau instability).
6. Final electrode discontinuity in published parts can reach **~40% uncovered area** at 1250 °C.

Discontinuity is *already* present at 800 °C and grows from there.

## Cited textbooks & papers (added to bibliography)

- Rahaman, *Ceramic Processing and Sintering*, 2nd ed., New York, 2003. — Yan's textbook reference.
- Kang, *Sintering — Densification, Grain Growth and Microstructure*, Elsevier Butterworth-Heinemann, 2005. — second textbook reference.
- Bordia & Scherer, "On constrained sintering I/II/III", *Acta Metall.* 36 (1988) 2393, 2399, 2411 — foundational constitutive framework.
- Green, Guillon, Rödel, "Constrained sintering: A delicate balance of scales", *J. Eur. Ceram. Soc.* 28 (2008) 1451–1466 — review.
- Kang, Joo, Cha, Jung, Paik, "Shrinkage behavior and interfacial diffusion in Ni-based internal electrodes with BaTiO₃ additive", *Ceram. Int.* 34 (2008) 1487 — directly on the user's binder/metal-ratio question.
- Sugimura, Hirao, "Effect of a BaTiO₃ nanoparticle additive on the quality of thin-film Ni electrodes in MLCC", *J. Ceram. Soc. Jpn.* 117 (2009) 1039.
- Polotai, Jeong, Yang, Dickey, Randall et al., "Effect of Cr additions on the microstructural stability of Ni electrodes in ultra-thin BaTiO₃ multilayer capacitors", *J. Electroceram.* 18 (2007).
- Jean & Chang, "Effect of Densification Mismatch on Camber Development during Cofiring of Ni-Based MLCC", *J. Am. Ceram. Soc.* 80 (1997) 2401.

## Entities mentioned
- [[samsung-electro-mechanics]] — supplied the MLCC samples and powders.
- Christophe Martin, Olivier Guillon, Didier Bouvard, Jürgen Rödel — supervisory team.
- Argonne National Laboratory APS (Beamline 32-ID), ESRF — synchrotron facilities.

## Concepts discussed
- [[constrained-sintering-mlcc]] — Ch. 2.2 reviews the Bordia-Scherer, Hsueh, Scherer-Garino framework.
- [[ni-batio3-cosintering-interface]] — Ch. 7 simulates BT/Ni/BT trilayer cofiring.
- [[green-tape-shrinkage-anisotropy]] — Ch. 3.3 dilatometry of Ni paste, dielectric, and full MLCC chip.
- [[binder-burnout-debinding]] — Ch. 3.1 / 3.2 debinding protocol (25 → 230 °C ramps).
- [[master-sintering-curve]] — Yan uses density-based formulations equivalent to Su-Johnson MSC for the matrix.
- [[failure-modes-mlcc]] — electrode discontinuity as a primary failure mode.

## Notable quotes

> "The final electrode discontinuity is linked to the initial heterogeneity in the electrode layers."

> "It is found that the densification rate of the matrix decreases with increasing volume fraction of inclusions and with decreasing size of inclusions."

> "Discontinuity occurs at the early stage of the sintering cycle. At this stage, the electrode starts to sinter while the dielectric material may be considered as a constraining substrate."

## References

_Original PDF: `resources/literature/pdf/tu-darmstadt-mlcc-sintering-thesis.pdf` (235 pages, CC-BY 4.0 via TUprints)_
