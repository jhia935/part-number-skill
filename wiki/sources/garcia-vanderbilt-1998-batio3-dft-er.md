---
title: "García & Vanderbilt — Temperature-Dependent Dielectric Response of BaTiO₃ from First Principles (arXiv 1998)"
type: source
created: 2026-05-21
updated: 2026-05-21
sources:
  - resources/literature/zhong-vanderbilt-1998-batio3-dft-er.md
tags:
  - paper
status: complete
importance: high
---

# García & Vanderbilt — εr(T) of BaTiO₃ from First Principles (arXiv 1998)

**Source:** `resources/literature/zhong-vanderbilt-1998-batio3-dft-er.md` (PDF: `resources/literature/pdf/zhong-vanderbilt-1998-batio3-dft-er.pdf`, 8 pages)
**Authors:** Alberto García (Universidad del País Vasco, Bilbao); David Vanderbilt (Rutgers)
**Reference:** arXiv:cond-mat/9802208v1, February 19, 1998 (Ferroelectrics 220 (1999) 87)

## Summary

The first **first-principles calculation of the dielectric response of BaTiO₃ as a function of temperature**. The authors use a Vanderbilt-Rabe effective Hamiltonian constructed from LDA-DFT, then evaluate the dielectric tensor via Monte Carlo simulations on a 14³ supercell. The result reproduces — without empirical adjustment beyond a linear T-rescaling that fixes the cubic-tetragonal transition temperature — **the experimental low-frequency dielectric response of BaTiO₃ across the cubic and tetragonal phases**, including the divergence at T_C and the strong dielectric anisotropy of the tetragonal phase.

This paper is the methodological foundation for predicting `ε_r` from first-principles. The same effective-Hamiltonian + MC framework underwrites essentially every subsequent DFT-based BaTiO₃ permittivity prediction.

## Key technical content

### Effective Hamiltonian

Contains:
- **Local soft-mode degrees of freedom** at each unit cell (15 per cell)
- **Displacement variables** for acoustic modes
- **Six components of homogeneous strain** η

Parameters fit from LDA-DFT calculations with Vanderbilt ultrasoft pseudopotentials. The full Hamiltonian is the Zhong-Vanderbilt-Rabe model (PRL 73 (1994) 1861; PRB 52 (1995) 6301).

### Monte Carlo evaluation

Extended Metropolis MC including electric field:
$$
\text{accept } j \leftarrow \exp\left[-\beta(U_j - V_0\sigma_\nu\eta_\nu^j - E_i P_i^j)\right]
$$

For each (T, σ, E), 14×14×14 = 2744 unit cell supercell, 3×10⁵ MC sweeps. Dielectric susceptibility extracted from:
$$
\chi_{ij} = \frac{1}{V\varepsilon_0}\beta(\langle P_i P_j\rangle - \langle P_i\rangle\langle P_j\rangle)
$$

### Validation

Reproduces measured `ε_r(T)` of BaTiO₃ across both the tetragonal phase (278–403 K) and the cubic phase (above 403 K):
- **Curie-Weiss form** `χ⁻¹ = C(T − T₀)` reproduced on both sides of T_C.
- **`|C_below| / 2C_above ≈ 4`** (vs 1.0 expected for a purely displacive second-order transition under mean-field theory) — indicates the cubic-tetragonal transition has substantial **order-disorder character**, not pure displacive.
- **Tetragonal dielectric anisotropy** (χ₁₁ ≫ χ₃₃ near T_C) reproduced — a signature of the in-plane soft-mode dispersion.

### Theoretical-to-experimental temperature rescaling

The effective Hamiltonian (finite Taylor expansion of energy in mode amplitude) systematically **underestimates transition temperatures**:
- Theoretical T (rhombohedral → orthorhombic → tetragonal → cubic): 197 K, 230 K, 295 K
- Experimental: 187 K, 278 K, 403 K

The authors apply a **linear T-rescaling** to align the tetragonal-phase endpoints with experiment before comparing ε_r. The mismatch is a known limitation of fixed-polynomial effective Hamiltonians and is the primary obstacle to absolute prediction of T_C from first-principles for arbitrary doped BaTiO₃ compositions.

## Implications for an ε_r-from-dopant simulator

The García-Vanderbilt method is the **gold standard for predicting ε_r(T) of undoped BaTiO₃** and the methodological basis for doped extensions. For an MLCC simulator that needs to predict ε_r as a function of dopant composition, the path is:

1. **Re-parametrize the effective Hamiltonian** for each Ba-site or Ti-site substitution (Y, La, Sm, Nd, Yb, Lu, Mg, Mn, etc.). Computationally expensive but tractable.
2. **Run MC** on the dopant-parametrized Hamiltonian for each (T, composition, V_DC) combination.
3. **Calibrate T-rescaling** to anchor T_C to experimental data — empirically necessary.

This is currently a research workflow, not a production simulator. Practical recipe-aware ε_r prediction relies on **empirical correlations** (per [[epsilon-r-from-dopant-composition]]) calibrated against experimental data like [[liu-2019-sm-mn-codoped-batio3-permittivity|Liu 2019]].

## Entities mentioned

- David Vanderbilt — co-author; key contributor to DFT methodology (ultrasoft pseudopotentials).
- Karin Rabe — methodological collaborator (Zhong-Vanderbilt-Rabe effective Hamiltonian).

## Concepts discussed

- [[cubic-tetragonal-transition]] — the transition this paper computes ε_r across.
- [[curie-temperature]] — the divergence near T_C is the central result.
- [[ferroelectric-domain-wall]] — order-disorder character implies fluctuating local dipoles.
- [[epsilon-r-from-dopant-composition]] — methodological foundation.

## Notable quote

> "The agreement [between simulation and experiment] is excellent, with the simulations reproducing in detail all the features of the observed behavior, including the large anisotropy of the dielectric tensor in the tetragonal phase."

> "The fitted values of the Curie temperature T₀ extracted from the tetragonal and cubic phases are very similar, reflecting the fact that the transition is only weakly first-order... |C_below|/2C_above ≃ 4 ... would be consistent with the analysis [...] pointing to a relatively strong order-disorder character of the cubic-tetragonal transition in BaTiO₃."

## References

_arXiv full text: `resources/literature/pdf/zhong-vanderbilt-1998-batio3-dft-er.pdf`_

Key cited references that this paper builds on:
- Zhong, Vanderbilt, Rabe, *Phys. Rev. Lett.* 73 (1994) 1861; *Phys. Rev. B* 52 (1995) 6301 — the foundational effective-Hamiltonian paper.
- Padilla, Zhong, Vanderbilt, *Phys. Rev. B* 53 (1996) R5969 — BaTiO₃ ferroelectric domain walls.
- Waghmare, Rabe, *Phys. Rev. B* 55 (1997) 6161 — PbTiO₃ ferroelectric transition.
- Vanderbilt, *Phys. Rev. B* 41 (1990) 7892 — ultrasoft pseudopotentials method.
