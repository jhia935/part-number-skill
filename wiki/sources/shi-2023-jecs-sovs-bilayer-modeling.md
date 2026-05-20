---
title: "Shi, Giuntini et al. — Efficient SOVS Modelling of Ceramic Bilayers (JECS 2023)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/tuhh-jecs-2023-sintering.md
tags:
  - paper
status: complete
importance: high
---

# Shi, Giuntini et al. — Efficient SOVS Modelling of Ceramic Bilayers (JECS 2023)

**Source:** `resources/literature/tuhh-jecs-2023-sintering.md` (PDF: `resources/literature/pdf/tuhh-jecs-2023-sintering.pdf`, 29 pages, 3 MB)
**Authors:** Hao Shi, Diletta Giuntini, Hans van Dommelen, Marc G.D. Geers, Joris J.C. Remmers (Eindhoven UT + TU Hamburg)
**Journal:** *Journal of the European Ceramic Society* 43 (2023) 4939–4949
**DOI:** 10.1016/j.jeurceramsoc.2023.03.053
**Access:** Open access (CC BY)

## Summary

A continuum-mechanics paper presenting an efficient finite-element implementation of the **Skorohod–Olevsky Viscous Sintering (SOVS) model** for predicting **shrinkage and densification of bilayer / membrane geometries**. The authors combine three contributions:

1. **A novel implicit integration scheme** that reduces computational cost by 50× (regular solid elements) to 1000× (solid-like shell elements) compared with legacy McHugh-Riedel semi-implicit codes.
2. **Solid-like shell elements** (SSC / SLS) for thin geometries — avoids Poisson thickness locking when the SOVS bulk viscosity is large.
3. **A new viscosity-characterization method** using the Aquilanti–Mundim deformed Arrhenius function, validated on ZnO (0.2 µm) and lanthanum tungstate (LaWO₅₄, 1.1 µm) sintering experiments.

Direct application to MLCC and other multilayer ceramic systems: the model now predicts differential shrinkage in bilayers and trilayers (with errors of 4 % for Garino bilayer bars and 8 % for Garino bilayer discs) on a laptop in short timeframes.

## Key model equations

**SOVS constitutive relation** (linear viscous form, isothermal):
$$
\boldsymbol{\sigma} = 2\eta\left[\phi\dot{\boldsymbol{\varepsilon}}'_i + \psi\dot{e}\mathbf{I}\right] + P_L\mathbf{I}
$$

Equivalently, the inelastic strain rate:
$$
\dot{\boldsymbol{\varepsilon}}_i = \frac{\boldsymbol{\sigma}'}{2\eta\phi} + \frac{\text{tr}(\boldsymbol{\sigma}) - 3P_L}{18\eta\psi}\mathbf{I}
$$

Where:
- `η` = shear viscosity of the fully dense skeleton (powder) phase (T-dependent)
- `φ(ρ) = ρ²` — normalized shear viscosity
- `ψ(ρ) = (2/3)ρ³/(1−ρ)` — normalized bulk viscosity (diverges at ρ → 1)
- `P_L(ρ) = (3α/r_p) ρ²` — **sintering stress**: proportional to surface tension `α`, **inversely proportional to particle radius `r_p`**
- `ρ` = relative density (bulk / theoretical)

The sintering stress `P_L` is a **hydrostatic compressive stress** driving densification; an externally applied tensile stress of equal magnitude would stop shrinkage. This is the continuum-mechanics analog to the [[bordia-scherer-composite-sintering|Bordia-Scherer]] retardation by inclusions.

**Continuity equation** (mass conservation):
$$
\dot{\rho} = -\rho\,\text{tr}(\dot{\boldsymbol{\varepsilon}}_i)
$$

Volume shrinkage rate `\dot{e} = \text{tr}(\dot{\boldsymbol{\varepsilon}}_i)` directly gives the density evolution.

**Material viscosity functions** validated in this paper:

| Function | Form | Best for |
|---|---|---|
| Quadratic | `η(T) = a/T² + b/T + c` | Narrow T-window fits |
| Arrhenius (Reiterer 2006) | `η(T) = η₀ exp(Q/RT)` | Bilayer cerium oxide |
| **Deformed Arrhenius (Aquilanti-Mundim)** | with two-branch exponent | Wide T-window incl. heat-up + cooldown of LaWO₅₄ |
| Density-dependent (this paper) | `η(ρ) = η(T*) · 10^((ρ−ρ₀)/Δρ·β)` | Final-stage holding densification |

## Validation results

- **ZnO bilayer bar** (Garino reference experiment): max curvature error 4%
- **ZnO bilayer disc** (Garino reference experiment): max curvature error 8%
- **Lanthanum tungstate pellet (new experiment)**: radial shrinkage error 1.5%, thickness 3.0%; final relative density 95.2% (experiment) vs 95.7% (model) — **0.4% error**.

Computational cost reduction: Garino bilayer bar simulation cut by **3 orders of magnitude** vs the legacy McHugh-Riedel scheme.

## Why this matters for MLCC

The SOVS framework is the right level of abstraction for **predicting MLCC chip-scale dimensional changes from green-tape data**. Given:
- Particle radius `r_p` (e.g., 100 nm BT, 0.2 µm Ni)
- Surface tension `α` (~2 J/m² for Ni; ~0.5–0.9 J/m² for BT)
- Initial relative density `ρ₀` (e.g., 0.55–0.66 for tape-cast BT)
- A measured `η(T)` curve from dilatometry on a free tape

…the SOVS model gives the **shrinkage trajectory of the entire MLCC stack** for any sintering profile, **including the bilayer constraint** between dielectric and Ni electrode.

This paper makes that practical (FE solution on a laptop) for the first time — and Garino's verification benchmarks are now matched within single-digit percent.

## Entities mentioned
- TU Eindhoven, TU Hamburg, Hamburg University of Technology — institutions
- Olevsky (Berkeley/San Diego State) — model originator
- Reiterer, Ewsuk, Argüello (Sandia) — earlier SOVS-Arrhenius work
- Garino (Sandia) — bilayer verification benchmarks

## Concepts discussed
- [[skorohod-olevsky-viscous-sintering]] — direct topic.
- [[constrained-sintering-mlcc]] — bilayer / trilayer is the canonical constraint problem.
- [[cofiring-camber-bilayer]] — the bilayer-bar/disc verification cases are camber-shape tests.
- [[green-density-vs-shrinkage]] — initial ρ₀ is a free parameter of the SOVS model.

## Notable quotes

> "The sintering stress is defined as the hydrostatic (compressive) stress which can stop the shrinkage when it is imposed in the opposite direction."

> "The differential shrinkage during co-sintering of bilayer or even trilayer parts with different materials or porosity levels in each layer can now be smoothly simulated in virtual frameworks."

## References

_Original PDF: `resources/literature/pdf/tuhh-jecs-2023-sintering.pdf` (Shi et al., CC BY)_
- Olevsky, "Theory of sintering: from discrete to continuum", *Mater. Sci. Eng. R* 23 (1998) 41–100.
- Reiterer, Ewsuk, Argüello, "Arrhenius-Type Viscosity Function for SOVS in FEM", *J. Am. Ceram. Soc.* 89 (2006) 1930–1935.
- Garino, "On the Constrained Sintering of Bilayer Tapes", *Acta Metall. Mater.* (1988) — the bilayer benchmark.
