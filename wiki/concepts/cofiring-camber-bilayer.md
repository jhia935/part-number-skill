---
title: Co-firing Camber in Bilayer Ceramics
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - hagymasi-ltcc-ferrite-dielectric-cofiring.md
  - shi-2023-jecs-sovs-bilayer-modeling.md
tags:
  - paper
status: complete
importance: medium
---

# Co-firing Camber in Bilayer Ceramics

When two ceramic green tapes with **different shrinkage rates** are laminated and cofired, the differential shrinkage generates **in-plane stresses** and causes the bilayer to **bow out of plane** (camber). The same physics that causes camber in LTCC bilayers and bimetal strips also causes:
- Camber-free but stressed MLCC stacks (symmetric layers cancel camber but residual stress remains)
- Delamination at internal interfaces
- Channel cracks in the layer under tensile stress
- Warpage of large-area MLCC arrays before dicing

For symmetric MLCC stacks (electrodes top + bottom), camber cancels by symmetry — but the **internal stress field is exactly the same** as in the unsymmetric bilayer.

## The Jean-Chang framework

J.-H. Jean and C.-R. Chang (*J. Am. Ceram. Soc.* 80 (1997) 2401) gave the canonical camber-prediction equation for a bilayer sintering with differential shrinkage rate `\Delta\dot{\varepsilon}`:

$$
\kappa(t) = 6 \cdot \Delta\dot{\varepsilon} \cdot t \cdot \frac{h_1 h_2 (h_1 + h_2)}{(h_1 + h_2)^3 \cdot f(\eta_1/\eta_2, h_1/h_2)}
$$

where:
- `κ` = curvature (1/m)
- `h_1, h_2` = layer thicknesses
- `η_1, η_2` = layer viscosities
- `f` = a dimensionless function of the viscosity and thickness ratios

For equal-thickness, equal-viscosity layers, camber scales **linearly with the time-integrated differential strain** and **inversely with bilayer thickness**.

## Bordia-Green-Hsueh viscoelastic continuum theory

A more general formulation:
1. Each layer is a viscous body with its own free-sintering strain rate `\dot{\varepsilon}_s` and viscosity `η`.
2. The bilayer geometry constrains the in-plane strain rate to be uniform across the cross-section.
3. The bilayer must satisfy zero net axial force and zero net bending moment about its neutral axis.
4. Solving the resulting beam-bending equations gives the **stress profile** and the curvature.

Result: the faster-shrinking layer is put in **tension** (its preferred contraction is held back by the slower layer), and the slower-shrinking layer is put in **compression** (it's stretched by the faster layer). Cooling-stage TEC mismatch superposes another stress field; the two can add or partially cancel.

## Two camber-generation stages

In real cofiring, camber accumulates in two distinct windows:

### Stage 1: Binder burnout (200–600 °C)
**Mechanism**: inhomogeneous binder distribution through the tape thickness. The top side often has more binder (capillary segregation during drying). When binder volatilizes, the top side contracts more than the bottom side, generating bow.

Data point from [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási LTCC ferrite tape]]:
- Single FT laminate, BBO at 2 K/min → **convex camber peaks at 300 °C**, persists through subsequent sintering.
- BBO at **0.5 K/min** → no camber, flat sample.

The fix is **always** a slower BBO ramp through the 200–400 °C window. See [[binder-burnout-debinding]].

### Stage 2: Differential sintering (peak T range)
**Mechanism**: the two layers have different `(\dot{\varepsilon}_s, η)` curves, so when one is densifying and the other is rigid (or vice versa), tensile/compressive stress accumulates.

Data point from [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási]]:
- DT (DuPont 951): onset 650-700 °C, done by 840 °C, max-rate ~780 °C.
- FT (BaFe₁₂O₁₉): onset 740-760 °C, requires 5 h hold at 900 °C, max-rate at 900 °C.
- Net: at 700-760 °C, DT shrinks while FT is rigid → DT is in tensile stress, cavitation forms (2 vol% pores).
- At 760-840 °C, both shrink but DT dominates → FT is in compressive stress.
- At 840-900 °C, FT shrinks alone → FT is in tensile stress → channel cracks.

Symmetric DT/FT/DT sandwich: camber cancels but **all three stress states are still present locally**, producing cavitation in DT and channel cracks in FT.

## Camber from SOVS

The [[skorohod-olevsky-viscous-sintering|SOVS framework]] predicts bilayer curvature directly. Its main observable is `κ(t)`, the curvature evolution. Validated against Garino's bilayer benchmarks ([[shi-2023-jecs-sovs-bilayer-modeling]]):
- Bilayer bar (ZnO with different ρ₀): **4 % curvature error**.
- Bilayer disc (ZnO with different ρ₀): **8 % curvature error**.

This level of accuracy on a laptop is sufficient for **shrinkage matching during MLCC paste design** — you can sweep BT-additive content in Ni paste, predict the resulting `η(T)`, and find the recipe that minimizes the stress integral.

## Mitigation hierarchy (in order of cost)

1. **Match the shrinkage curves**: add nano-BT additive to Ni paste so its `η(T)` overlaps the dielectric's. See [[ni-batio3-cosintering-interface]].
2. **Match the layer thicknesses and lay-ups**: symmetric stacks zero out camber even with mismatch.
3. **Slow the BBO ramp**: 0.5 K/min through 200–400 °C cures the binder-gradient stage 1 camber.
4. **Add sintering aids to the dielectric**: glass aids lower the dielectric `T_onset` to match Ni — see [[sintering-aids-glass]].
5. **Constrained sintering with sacrificial layers**: force lateral shrinkage to zero from outside — see [[zero-shrinkage-ltcc]].
6. **Pressure-assisted sintering** (HIP / SPS): expensive, but eliminates the camber problem entirely. See [[spark-plasma-sintering]].

## Implications for the MLCC simulator

A camber/warpage predictor should:
- Take `η_dielectric(T)`, `η_Ni-paste(T)`, layer thicknesses, and the sintering profile as inputs.
- Implement the Jean-Chang formula for a quick first-pass camber estimate.
- For high-fidelity, fall back to a 1D SOVS solver (which is the same equations integrated through the stack thickness).
- Flag camber > 10 µm / cm as a probable delamination risk in symmetric stacks.

## References

- J.-H. Jean & C.-R. Chang, "Effect of Densification Mismatch on Camber Development during Cofiring of Nickel-Based Multilayer Ceramic Capacitors", *J. Am. Ceram. Soc.* 80 (1997) 2401–2406.
- R. K. Bordia, R. Raj, "Sintering behavior of ceramic films constrained by a rigid substrate", *J. Am. Ceram. Soc.* 68 (1985) 287–292.
- C. H. Hsueh, "Sintering of a ceramic film on a rigid substrate", *Scripta Metall.* 19 (1985) 1213–1217.
- D. J. Green, O. Guillon, J. Rödel, "Constrained sintering: A delicate balance of scales", *J. Eur. Ceram. Soc.* 28 (2008) 1451–1466.
- [[hagymasi-ltcc-ferrite-dielectric-cofiring]] — LTCC dielectric+ferrite experimental case study.
- [[shi-2023-jecs-sovs-bilayer-modeling]] — SOVS-FE prediction of bilayer warpage.
- [[lester-2017-sandia-sovs-verification]] — Sandia SOVS bilayer bar verification.
