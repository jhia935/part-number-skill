---
title: Skorohod-Olevsky Viscous Sintering (SOVS) Model
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - shi-2023-jecs-sovs-bilayer-modeling.md
  - lester-2017-sandia-sovs-verification.md
tags:
  - paper
status: complete
importance: high
---

# Skorohod–Olevsky Viscous Sintering (SOVS) Model

The **continuum-mechanics constitutive model** for predicting the shrinkage, densification, and stress state of a sintering ceramic body. SOVS treats the densifying porous compact as a **non-linear viscous medium** whose flow is driven by a hydrostatic sintering stress and resisted by shear and bulk viscosities. It is the dominant framework for FE-based simulation of MLCC and LTCC sintering, ceramic membranes, and bilayer / multilayer parts.

Originally formulated by Skorohod (1972) and Olevsky (1998 *MSE-R*). The 2017 Sandia ([[lester-2017-sandia-sovs-verification]]) and 2023 Eindhoven/Hamburg ([[shi-2023-jecs-sovs-bilayer-modeling]]) papers represent the current best-practice numerical implementation.

## Constitutive equation

Inelastic (sintering) strain rate tensor:
$$
\dot{\boldsymbol{\varepsilon}}_i = \frac{\boldsymbol{\sigma}'}{2\eta\phi(\rho)} + \frac{\text{tr}(\boldsymbol{\sigma}) - 3P_L(\rho)}{18\eta\psi(\rho)}\,\mathbf{I}
$$

| Symbol | Meaning |
|---|---|
| `σ'` | Deviatoric Cauchy stress |
| `tr(σ)` | Hydrostatic pressure × 3 |
| `η(T)` | Shear viscosity of the fully dense skeleton phase (Arrhenius-type T dependence) |
| `φ(ρ)` | Normalized shear viscosity, typically **`ρ²`** |
| `ψ(ρ)` | Normalized bulk viscosity, typically **`(2/3) ρ³ / (1 − ρ)`** — diverges as ρ → 1 |
| `P_L(ρ)` | Sintering stress, **`(3α / r_p) ρ²`** |
| `α` | Surface tension of the powder material (J/m²) |
| `r_p` | Particle radius |

The **sintering stress `P_L` is a hydrostatic compressive stress** that drives densification. A tensile external stress of equal magnitude (e.g., from a constraining layer) **stops the shrinkage**. This is the continuum-mechanics origin of the in-plane suppression / thickness enhancement seen in [[constrained-sintering-mlcc|constrained MLCC sintering]].

**Continuity equation:**
$$
\dot{\rho} = -\rho\,\text{tr}(\dot{\boldsymbol{\varepsilon}}_i)
$$

## Material-parameter sources

| Parameter | How to get it |
|---|---|
| `α` (surface tension) | Literature (~2 J/m² for Ni; 0.5–0.9 J/m² for BT) |
| `r_p` (particle radius) | SEM / laser diffraction |
| `η(T)` | **Free-sintering dilatometry** of a single tape — inverted via `\dot{\rho} = (P_L / η ψ) ρ` (Shi 2023 method) |
| `ρ₀` (initial relative density) | Geometric or Archimedes density |

The killer-app aspect of SOVS for MLCC: **a single free-tape dilatometry run gives you `η(T)`, which combined with `α / r_p` predicts the entire sintering trajectory of an arbitrarily complex multilayer**.

## Three viscosity functional forms

Different authors use different `η(T)` parametrizations:

| Form | Where used | Strength |
|---|---|---|
| Quadratic (Olevsky 1998) | Narrow T window | Empirical fit; lowest model risk |
| **Arrhenius** (Reiterer-Ewsuk-Argüello 2006) | Standard for FEM codes | Physical activation-energy interpretation |
| **Deformed Arrhenius (Aquilanti-Mundim)** | Shi 2023; wide T window | Captures both heat-up and cooldown viscosity branches |
| Density-decorated `η(ρ)·η(T)` | Shi 2023 final-stage holding | Lets viscosity rise with ρ during isothermal hold |

## Numerical implementation

Historically the SOVS model was implemented with the **McHugh-Riedel semi-implicit integration scheme** (1995), which Sandia reported as needing impractically fine meshes to resolve bilayer warpage ([[lester-2017-sandia-sovs-verification]] quoting Argüello et al.).

The current state of the art ([[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]]) uses:
- **Fully implicit time integration** — single state variable `Δe = tr(Δε_i)` to solve per integration point per timestep.
- **Solid-like shell (SSC / SLS) elements** — avoid Poisson thickness locking when `ψ` is large.
- A reduction factor of **50× to 1000× in CPU cost** over McHugh-Riedel.

Result: bilayer-bar MLCC-like simulations run on a laptop in minutes.

## Free vs constrained sintering predictions (SOVS)

For **free isotropic sintering** (zero external stress), the inelastic strain rate is purely hydrostatic:
$$
\dot{\boldsymbol{\varepsilon}}_i = -\frac{P_L}{6\eta\psi}\,\mathbf{I}
$$

so `dε_x/dt = dε_y/dt = dε_z/dt`. **Isotropic linear shrinkage.**

For a **constrained film** (lateral strain rate = 0 via a rigid substrate or matched lateral layer):
$$
\dot{\varepsilon}_z = -\frac{P_L}{2\eta\psi} \cdot \frac{1}{1 - 2\nu_v}
$$

where `ν_v` is the viscous Poisson's ratio (= `(3ψ − 2φ) / (6ψ + 2φ)` in SOVS). The thickness strain rate is amplified by the factor `1 / (1 − 2ν_v)`, which **drives the lateral-to-thickness shrinkage exchange** observed in [[constrained-sintering-mlcc]] and [[hagymasi-ltcc-ferrite-dielectric-cofiring|LTCC sandwich experiments]] (3% lateral / 33% thickness).

## Validated benchmarks

| System | Geometry | Result |
|---|---|---|
| ZnO (Garino) | Bilayer bar | Curvature error 4 % ([[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]]) |
| ZnO (Garino) | Bilayer disc | Curvature error 8 % |
| LaWO₅₄ | Free pellet | Shrinkage error 1.5–3 %, density error 0.4 % |
| Sandia v&v | Solid bar | Implicit converges to McHugh-Riedel at coarser mesh ([[lester-2017-sandia-sovs-verification]]) |

## How to use SOVS for an MLCC simulator

1. **Measure `η(T)` for each component**: dilatometry of free dielectric tape and free Ni-paste pellet.
2. **Measure `ρ₀` for each component**: green density of the tape; calculated from compact mass + dimensions.
3. **Look up `α, r_p`** for the powder.
4. **Build a 1D / 2D / 3D mesh** of the stack (Ni layer + BT layers, alternating).
5. **Run the FE simulation** with the planned temperature profile and the new implicit scheme.
6. Output: fired-chip dimensions, internal stress field, electrode discontinuity probability, residual stress for ferroelectric domain calculation.

The Shi 2023 + Lester 2017 contributions make this **practical at MLCC time-scales**: a full 4–6 h sintering profile on a million-element MLCC stack now fits in a tractable simulation.

## Limitations

- **Solid-state sintering only** — not designed for liquid-phase sintering with reactive glass phases (BME parts at peak T have a [[ni-batio3-cosintering-interface|liquid Ni-Ba-Ti alloy film]] that violates the viscous-skeleton assumption).
- **Surface diffusion not explicitly modeled** — for sub-µm powders surface diffusion can compete with bulk densification; SOVS lumps it into `η(T)`.
- **Grain growth coupled only via η(ρ)** — full Hansen-Su-Johnson [[master-sintering-curve]] coupling requires additional terms.
- **Large rotations** in bilayer warpage need a co-rotational finite-strain extension.

## Cross-references

- [[constrained-sintering-mlcc]] — the bilayer / multilayer constraint problem SOVS predicts.
- [[cofiring-camber-bilayer]] — warpage geometry from differential SOVS predictions.
- [[green-density-vs-shrinkage]] — `ρ₀` is the initial condition for the SOVS integration.
- [[green-tape-shrinkage-anisotropy]] — anisotropic-microstructure extensions of SOVS use anisotropic `φ`, `ψ`.
- [[master-sintering-curve]] — alternative density-only formulation; SOVS adds the stress field.
- [[bordia-scherer-composite-sintering]] — inclusion-retardation model that complements SOVS for composite electrodes.

## References

- Olevsky, "Theory of sintering: from discrete to continuum", *Mater. Sci. Eng. R* 23 (1998) 41–100 — the foundational paper.
- Reiterer, Ewsuk, Argüello, "Arrhenius-Type Viscosity Function for SOVS in FEM", *J. Am. Ceram. Soc.* 89 (2006) 1930–1935.
- [[lester-2017-sandia-sovs-verification]] — implicit scheme, Sandia SAND2017-12933R.
- [[shi-2023-jecs-sovs-bilayer-modeling]] — solid-like shell + implicit SOVS, JECS 2023.
- Olevsky, *J. Am. Ceram. Soc.* 96 (2013) 2295 — multilayer / constrained extensions.
