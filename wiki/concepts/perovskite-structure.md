---
title: Perovskite Crystal Structure (ABO₃)
type: concept
created: 2026-05-19
updated: 2026-05-19
sources: []
tags:
  - paper
---

# Perovskite Crystal Structure (ABO₃)

The family of oxide crystal structures with formula **ABO₃**, where A is a large cation (Ba, Sr, Ca, Pb), B is a smaller cation (Ti, Zr, Nb, Ta), and O is oxygen. Named after the mineral perovskite (CaTiO₃). **Almost every important MLCC dielectric is a perovskite**: [[batio3]], [[cazro3]], [[srtio3]], [[nanbo3]], PbTiO₃, PbZrTiO₃ (PZT), etc.

## Ideal cubic structure
- **A cation** at the cube corners (8 positions, but each shared among 8 cells → 1 per cell).
- **B cation** at the cube center.
- **Oxygen** at the cube face centers (6 positions, each shared between 2 cells → 3 per cell).

Net stoichiometry: 1 A + 1 B + 3 O per unit cell.

Coordination:
- A is 12-coordinated by oxygen.
- B is 6-coordinated by oxygen (sits inside an O octahedron).

## Tolerance factor (Goldschmidt)
Defines the size compatibility of A, B, O for a stable perovskite:
$$
t \;=\; \frac{r_A + r_O}{\sqrt{2}\,(r_B + r_O)}
$$
- `t = 1.0`: ideal cubic (e.g., SrTiO₃)
- `0.9 < t < 1.0`: stable cubic or slight distortion (e.g., BaTiO₃ above T_C)
- `t < 0.9`: orthorhombic / hexagonal distortion (e.g., CaTiO₃, CaZrO₃)
- `t > 1.0`: tetragonal distortion (e.g., BaTiO₃ below T_C; if B is too small, it sits off-center → ferroelectric)

The off-center B cation in undersized octahedra is **the origin of ferroelectricity in BaTiO₃**.

## Distortions and phases relevant to MLCC
| Material | Room-T phase | Cause |
|---|---|---|
| [[batio3]] | tetragonal P4mm | Ti off-center; ferroelectric |
| [[batio3]] above T_C | cubic Pm3m | Ti centered; paraelectric |
| [[srtio3]] | cubic Pm3m | t ≈ 1.0, quantum paraelectric |
| [[cazro3]] | orthorhombic Pnma | t < 0.9, octahedral tilting (no ferroelectric distortion) |
| [[nanbo3]] | orthorhombic; complex polymorphism | antiferroelectric phase |

## Substitution flexibility = engineering knob
The ABO₃ framework tolerates a remarkable range of A and B substitutions (within the tolerance-factor window). This is what makes BaTiO₃-based MLCC formulations chemically rich:
- **A-site substitution**: Sr²⁺, Ca²⁺, Pb²⁺ for Ba²⁺ → shifts T_C
- **B-site substitution**: Zr⁴⁺, Sn⁴⁺ for Ti⁴⁺ → shifts T_C (Zr-rich → relaxor)
- **Aliovalent dopants** (different charge from host): Y³⁺ on Ba²⁺ site (donor), Mg²⁺ on Ti⁴⁺ site (acceptor) — drives [[defect-chemistry-batio3|Kröger-Vink defect chemistry]] for IR/reliability tuning.

## Cross-references
- [[batio3]]
- [[cazro3]]
- [[srtio3]]
- [[nanbo3]]
- [[curie-temperature]]
- [[cubic-tetragonal-transition]]
- [[defect-chemistry-batio3]]
