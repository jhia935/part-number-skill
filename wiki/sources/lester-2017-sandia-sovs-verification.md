---
title: "Lester — Verification of the Skorohod-Olevsky Viscous Sintering (SOVS) Model (Sandia SAND2017-12933R)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/sandia-sovs-verification-2017.md
tags:
  - report
status: complete
importance: medium
---

# Lester — Verification of the SOVS Model (Sandia 2017)

**Source:** `resources/literature/sandia-sovs-verification-2017.md` (PDF: `resources/literature/pdf/sandia-sovs-verification-2017.pdf`, 6 pages)
**Author:** Brian T. Lester
**Report number:** SAND2017-12933R, November 16, 2017
**Organization:** Sandia National Laboratories (Albuquerque, NM)
**Access:** Public-domain US government technical report (DOI: 10.2172/1411315)

## Summary

A short Sandia tech-memo presenting **a new fully implicit integration scheme** for the SOVS sintering model and verifying it against the legacy McHugh-Riedel semi-implicit scheme. The motivation is the prior observation by Argüello et al. (Sandia) that resolving curvature/warpage in SOVS bilayer simulations required impractically fine meshes; this report shows that the new implicit scheme **mitigates the spatial-resolution requirement** and converges to the same answer with order-of-magnitude less mesh refinement.

Companion document to the Shi et al. 2023 JECS paper ([[shi-2023-jecs-sovs-bilayer-modeling]]) which extends the same approach with solid-like shell elements and validates on a broader range of materials.

## Key content

### Model statement (Eq. 1)

The SOVS inelastic strain rate, in the linear-viscous form:
$$
\dot{\varepsilon}^{in}_{ij} = \frac{\sigma'_{ij}}{2\eta_0(\theta)\phi(\rho)} + \frac{\sigma_{kk} - 3\sigma_s(\rho)}{18\eta_0(\theta)\psi(\rho)}\,\delta_{ij}
$$

- `σ_ij` = Cauchy stress; `σ'_ij` = deviatoric part; `(1/3)σ_kk` = pressure
- `η₀(θ)` = shear viscosity of the fully dense skeleton (temperature-dependent)
- `φ(ρ)` = normalized shear viscosity
- `ψ(ρ)` = normalized bulk viscosity
- `σ_s(ρ)` = sintering stress (the "thermodynamic driving force" for densification)
- `ρ = ρ_t / ρ_T` = relative density

This is the same equation as in [[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]] — Lester writes it in indicial / tensor-component form whereas Shi writes it in matrix form, but the physics is identical.

### Verification cases

1. **Constitutive verification**: free isothermal sintering of a single solid element. Implicit and McHugh-Riedel schemes converge to the same densification trajectory.
2. **Bilayer bar verification** (Argüello-Garino reference): two stacked viscous sintering layers with different starting `ρ₀`. The implicit scheme reproduces the warpage with the same mesh that gave incorrect answers in the legacy code.

The paper's central engineering message:

> "Difficulties in appropriately resolving temporal and spatial fields have been noted... the investigation of Argüello et al. used both a legacy finite element code (JAS3D) and the legacy constitutive implementation scheme of McHugh and Riedel. Here, the possibility of mitigating these issues have been addressed by (i) proposing and implementing a new, fully implicit integration scheme..."

Practically: the SOVS framework is good; previous bad results were a numerical-scheme problem, not a model-fidelity problem.

## Why this matters for MLCC

Confirms that **the SOVS model has the resolution to predict MLCC bilayer/multilayer warpage** at modern industrial scales, given the right integration scheme. Combined with [[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]]'s solid-like shell elements, you can run **the full sintering trajectory of an MLCC stack on a laptop**, including:
- In-plane shrinkage as a function of green density and sintering profile
- Thickness shrinkage absorbing the lateral suppression
- Camber from intra-tape green-density gradients
- Stress concentrations at the electrode/dielectric interfaces

## Concepts discussed

- [[skorohod-olevsky-viscous-sintering]] — direct topic.
- [[constrained-sintering-mlcc]] — bilayer bar is the canonical constrained case.
- [[cofiring-camber-bilayer]] — verification cases include camber/curvature evolution.

## Notable quote

> "It is important to note that the investigation of Argüello et al. used both a legacy finite element code (JAS3D) and the legacy constitutive implementation scheme of McHugh and Riedel."

## References

_Sandia public-domain report: `resources/literature/pdf/sandia-sovs-verification-2017.pdf`_
- Olevsky, *Mater. Sci. Eng. R* 23 (1998) 41–100 — the foundational SOVS paper.
- Argüello, Ewsuk, Reiterer — earlier Sandia SOVS verification work.
- Garino — bilayer reference experiment data.
