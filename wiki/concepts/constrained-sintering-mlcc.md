---
title: Constrained Sintering in MLCC Multilayer Stack
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: medium
sources:
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
tags:
  - paper
---

# Constrained Sintering in MLCC Multilayer Stack

When a dielectric green tape is **constrained** by an adjacent layer (Ni electrode, or another tape that shrinks differently), its sintering becomes **anisotropic**: in-plane shrinkage is suppressed while thickness (out-of-plane) shrinkage absorbs most of the volume reduction. This is the geometric origin of camber/warpage in cofired multilayer structures and a key mechanical-stress source in MLCC.

## The phenomenon

In an unconstrained free body, sintering shrinks isotropically: same percent linear shrinkage in x, y, z. In a constrained body, the in-plane direction can't shrink (held by the constraining layer) and the **same volumetric shrinkage has to happen entirely in the z (thickness) direction**.

Typical MLCC values (LTCC-style measurements, similar physics):
- Casting direction (x): 12.7 %
- Cross direction (y): 13.9 %
- **Thickness direction (z): 12.8 %** (close to free; the case-size lateral is more constrained than the cross direction because of substrate constraints)

Compared to the **free sintering** expectation of ~17 % linear in all three directions, lateral shrinkage is suppressed ~30 % and thickness absorbs the slack.

## Camber and warpage
If a bilayer has two materials with different sintering kinetics (e.g., dielectric tape vs Ni-electrode tape, or two tapes with different shrinkage onset temperatures), they tension each other in plane during sintering. The faster-shrinking layer pulls the slower into tension; the slower layer pushes the faster into compression. The bilayer bows ("camber") to balance the resulting moment.

For MLCC stacks (3-D alternating dielectric/electrode), the camber is suppressed by symmetry (electrodes on both sides) **but** local stress accumulates, leading to:
- Delamination at Ni/dielectric interfaces
- Electrode discontinuity ([[ni-batio3-cosintering-interface|Rayleigh-Plateau break-up]] driven partly by in-plane tension on the Ni layer)
- Residual stresses that show up post-sintering as bow, twist, or built-in stress fields that modify [[cubic-tetragonal-transition|tetragonal domain formation]]

## Constitutive model
The continuum-mechanics framework for constrained sintering ([Olevsky JACerS 2013](https://ceramics.onlinelibrary.wiley.com/doi/10.1111/jace.12375)):
- Uniaxial viscosity `η_a` (resistance to deformation in the constrained direction)
- Viscous Poisson's ratio `ν_v` (coupling between in-plane and thickness deformation)
- Free sintering strain rate `\dot{\varepsilon}_s` (the would-be isotropic shrinkage)

For an anisotropic microstructure that develops during constrained sintering (elongated pores, aligned grain boundaries), both `η_a` and `ν_v` become anisotropic — the material remembers its own constraint history.

## Composite-sintering retardation (Bordia-Scherer)

The classical model for a sintering matrix with **rigid (or slow-sintering) inclusions** ([[rahaman-ceramic-processing-sintering-textbook|Rahaman]] Ch. 10, [[mistler-twiname-tape-casting-textbook|Mistler-Twiname]] for the tape-casting side, originally Bordia & Scherer 1988 and Scherer 1987):

$$
\frac{\dot{\varepsilon}_c}{\dot{\varepsilon}_{m,\text{free}}} \;=\; 1 \,-\, v_i
$$

where `v_i` is the inclusion volume fraction. The composite shrinks **at most** by the factor (1 − v_i) of the free matrix rate. In practice, **inclusions retard far more strongly** than this linear bound predicts, because they substitute matrix-matrix contacts (which sinter) by matrix-inclusion contacts (which don't).

Quantitative numbers from [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan 2013, DEM Ch. 6]] for Ni-matrix + nano-BT-inclusion composites at relative density D = 0.70:

| BT inclusion vol% | BT particle size | Retarding factor (free / composite) |
|---|---|---|
| 5 | 60 nm | ~1.5 |
| 20 | 300 nm | 2 |
| 20 | 100 nm | ~4 |
| 20 | 60 nm | **7** |

Smaller inclusions and better dispersion dramatically amplify the retardation. This is the engineering basis for **nano-BT-doped Ni paste** in MLCC: 5–15 vol% well-dispersed nano-BT slows the Ni shrinkage enough to align with the dielectric's shrinkage curve.

## Mitigation strategies for MLCC
1. **Shrinkage-matched paste**: add ~5–20 vol% nano-BaTiO₃ (10–30 nm) to the Ni paste so the Ni shrinkage curve overlaps the dielectric's (see [[ni-batio3-cosintering-interface]] for the quantified retardation table).
2. **Sintering-aid tuning**: lower the dielectric sintering T with [[sintering-aids-glass|glass aids]] to bring it into the Ni shrinkage window.
3. **Pre-sintered powder**: use pre-calcined dielectric powder with reduced shrinkage on firing.
4. **Symmetric stack design**: keep electrode/dielectric symmetric top-to-bottom so the part doesn't bow.
5. **External constraint** (substrate): for LTCC, sintering against a sacrificial constraining layer gives "zero shrinkage" laterally and forces all volume shrinkage into thickness — useful when in-plane dimensional accuracy is critical.

## Implications for the simulator
- Effective overlap area `A` and active layer count `N` are set **post-sintering**, after constrained shrinkage has rearranged the geometry.
- Sub-µm dielectric layer parts have lateral constraints stronger than thicker-d parts because the Ni electrode coverage is a larger fraction of the chip's in-plane stiffness.
- Residual stress from constrained sintering interacts with [[cubic-tetragonal-transition|cooldown stress]] — the two superpose and can either cancel or add depending on geometry.

## Cross-references
- [[ni-batio3-cosintering-interface]]
- [[sintering-profile-mlcc]]
- [[sintering-kinetics-batio3]]
- [[mlcc-manufacturing-process]]
- [[case-size-geometry]]
- [[failure-modes-mlcc]]
- [[green-tape-shrinkage-anisotropy]]
- [[yan-thesis-2013-mlcc-sintering-nanotomography]]
- [[rahaman-ceramic-processing-sintering-textbook]]

## References
- Olevsky, "Sintering of Multilayered Porous Structures: Part I — Constitutive Models", *J. Am. Ceram. Soc.* 96 (2013) 2295–2304.
- Frandsen, Bjørk, "Modeling Sintering of Multilayers Under Influence of Gravity", *J. Am. Ceram. Soc.* 96 (2013) 80–86.
- Schoenitz et al., "Distortion of an LTCC Bilayer during Constrained Sintering: Comparison between Ombroscopic Imaging and Modeling", *Materials* 15:18 (2022) 6405.
- ScienceDirect: "Microstructural evolution of electrodes in sintering of MLCC observed by synchrotron X-ray nano-CT", *Acta Materialia* 2021.
