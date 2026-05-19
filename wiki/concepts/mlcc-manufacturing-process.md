---
title: MLCC Manufacturing Process (End-to-End)
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - escies-bme-mlcc-high-reliability.md
  - nasa-cracking-low-voltage-mlcc.md
  - octopart-tdk-cga8l3c0g-product-guide.md
tags:
  - paper
---

# MLCC Manufacturing Process (End-to-End)

A multi-step ceramic-electronic packaging pipeline that takes powder + paste + green-tape inputs to a finished surface-mount chip with three sintered, plated terminations on a five-axis controlled chip body. End-to-end yield and quality depend on **shrinkage matching** and **atmosphere control** at multiple steps.

## Process map (BME stack, modern Tier-1 line)

```
1.  Dielectric powder synthesis (BaTiO₃ ~100–300 nm core-shell powder)
2.  Slurry preparation (solvent + binder + plasticizer + dispersant + powder)
3.  Tape casting (doctor blade → 0.5–10 µm green tape on PET carrier)
4.  Screen printing internal electrode (Ni paste + dielectric additive, 0.5–1 µm wet)
5.  Stacking + lamination (alternating dielectric/electrode → green block)
6.  Isostatic pressing (∼50–200 MPa to densify and pre-shape)
7.  Dicing (mechanical or laser → green chips)
8.  Binder burnout / debinding (200–600 °C, controlled atmosphere)
9.  Sintering (1100–1300 °C, reducing atmosphere PO₂ 10⁻¹⁰–10⁻¹²)
10. Re-oxidation anneal (~900–1100 °C, slightly higher PO₂)
11. Corner rounding (tumble polish or barrel rounding to expose internal electrodes)
12. Termination (Cu paste dip → sinter → forms outer electrode)
13. Ni barrier plating (electrolytic, 2–3 µm)
14. Sn finish plating (matte tin, 5–10 µm; SnPb option for legacy)
15. Electrical sort / test
16. Tape & reel
```

Each step has its own page (or planned page) covering parameters, defect modes, and yield-critical knobs.

## Key kinetic coupling: shrinkage matching
The dielectric and electrode layers must shrink **in lockstep** during sintering, or the part delaminates or develops electrode discontinuity. Modern BME does this by:
1. **Adding BaTiO₃ ceramic powder (≈50 nm)** to the Ni paste — slows the Ni shrinkage in the sintering window so it tracks the dielectric.
2. **Using bimodal Ni powders** for tighter shrinkage profile.
3. **Sintering aids** (glass formers, transient liquid-phase additives) in the dielectric to lower its sintering temperature.

## Atmosphere control — the BME-specific challenge
- **Debinding** in Ar + 1 vol % O₂ (a mild oxidizing window) — removes 74 % of binder while limiting Ni oxidation (∼1600 ppm O pickup).
- **Sintering** in N₂/H₂ reducing atmosphere with PO₂ in the 10⁻¹⁰ to 10⁻¹² atm range — keeps Ni metallic but creates oxygen vacancies in the dielectric.
- **Re-oxidation** at lower T with slightly higher PO₂ to refill some O vacancies near grain boundaries (improves IR) without oxidizing Ni.

Closed-loop O₂ control is now the state of the art in pusher furnaces ([[bme-sintering-atmosphere]]).

## Defect / failure modes per step
| Step | Defect | Symptom |
|---|---|---|
| Tape casting | non-uniform thickness | yield loss at thin spots, capacitance variation |
| Electrode print | misalignment, voids | electrode discontinuity, reduced effective area |
| Lamination | trapped air | post-sinter delamination |
| Dicing | edge chipping | reduced creepage distance |
| Debinding | too fast | bulk cracking, [[failure-modes-mlcc|parallel-plate cracks]] |
| Sintering | shrinkage mismatch | delamination, electrode breaks |
| Re-oxidation | over-oxidize | Ni inner electrode degradation, raised ESR |
| Termination | poor coverage | open termination, dropped chips |
| Plating | porosity | solderability fail, humidity ingress |

## Production scale
World-wide MLCC production: **~2 trillion pieces/year** ([[escies-bme-mlcc-high-reliability]]). A single Tier-1 fab can output billions of pieces/month.

## Cross-references
- [[bme-vs-pme]]
- [[bme-sintering-atmosphere]]
- [[re-oxidation-anneal]]
- [[case-size-geometry]]
- [[core-shell-batio3]]
- [[failure-modes-mlcc]]
- [[oxygen-vacancy-migration]]

## References
- [[escies-bme-mlcc-high-reliability]]
- [[nasa-cracking-low-voltage-mlcc]] — Section 2 has the most comprehensive open-literature process survey
- [[octopart-tdk-cga8l3c0g-product-guide]] — vendor side
