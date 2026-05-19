---
title: "EPFL — Ceramics: Sintering and Microstructure (TP3 lab guide)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/epfl-ceramics-sintering-microstructure.md
tags:
  - paper
status: complete
importance: high
---

# EPFL — Ceramics: Sintering and Microstructure (TP3)

**Source:** `resources/literature/epfl-ceramics-sintering-microstructure.md` (PDF: `resources/literature/pdf/epfl-ceramics-sintering-microstructure.pdf`)
**Authors:** Aslam Kunhi Mohamed et al., EPFL Laboratory of Construction Materials
**Type:** Educational lab manual (graduate / advanced undergraduate), 2016 edition

## Summary

A clean teaching reference for the physics of solid-state ceramic sintering. Covers the textbook framework (driving forces, four mass-transport mechanisms, activation-energy hierarchy, densification rate equations) and includes a worked-example dilatometry protocol for extracting `Q` from `dL/dt` vs `T` data. Probably the most accessible single document for understanding the **physics** that happens during MLCC firing without having to wade through a 1000-page textbook (Kingery / German / Rahaman).

## Key content for the MLCC simulator

### Three sintering modes
1. Solid-phase sintering (MLCC default)
2. Liquid-phase sintering (with [[sintering-aids-glass]])
3. Reactive sintering

### Four mass-transport mechanisms
| Mechanism | Densifies? |
|---|---|
| Surface diffusion | No (coarsens only) |
| Volume diffusion | Yes |
| Vapor transport | No |
| Grain-boundary diffusion | Yes |

### Activation energy hierarchy
`Q_surf < Q_GB < Q_volume`. Worked examples:
- α-Al₂O₃: 399 / 464 / 616 kJ/mol
- ZnO: 158 / 282 / 376 kJ/mol

### Densification rate equation
$$
\frac{d\rho}{dt} = \frac{A}{T} \cdot e^{-Q/RT} \cdot \frac{f(\rho)}{D^n}
$$
where `D` is grain size, `n` depends on mechanism (typically 3 for GB, 4 for volume diffusion).

### Driving force
- Global: reduce interfacial free energy (replace solid-vapor surfaces with grain boundaries).
- Local: Young-Laplace pressure / curvature difference drives vacancy gradients → mass transport.

### Dopant effects (3 mechanisms)
1. Precipitate pinning (Zener)
2. Point-defect concentration changes (charge compensation creates vacancies / interstitials)
3. Defect immobilization (dopant-defect pair binding reduces mobility)

## Concepts discussed
- [[sintering-kinetics-batio3]]
- [[grain-growth-dopant-pinning]]
- [[defect-chemistry-batio3]]
- [[sintering-aids-glass]]
- [[mlcc-manufacturing-process]]

## Entities mentioned
- EPFL Laboratory of Construction Materials (LMC)

## References
_Original source: `resources/literature/epfl-ceramics-sintering-microstructure.md`_
