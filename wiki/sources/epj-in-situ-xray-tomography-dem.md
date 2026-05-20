---
title: "Yan, Martin et al. — Coupling In-Situ X-Ray Tomography and DEM for High-T Sintering (EPJ Web Conf 2017)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/epj-in-situ-xray-tomography-dem.md
tags:
  - paper
status: complete
importance: medium
---

# Yan, Martin et al. — Coupling X-Ray Tomography and DEM for High-T Sintering

**Source:** `resources/literature/epj-in-situ-xray-tomography-dem.md` (PDF: `resources/literature/pdf/epj-in-situ-xray-tomography-dem.pdf`)
**Authors:** Zilin Yan, Christophe L. Martin, Didier Bouvard, David Jauffrès, Pierre Lhuissier, Luc Salvo (Univ. Grenoble Alpes / CNRS SIMAP); Luis Olmos (Univ. Michoacana); Julie Villanova (ESRF); Olivier Guillon (Forschungszentrum Jülich)
**Venue:** *EPJ Web of Conferences* 140, 13006 (2017) — Powders & Grains 2017 conference
**DOI:** 10.1051/epjconf/201714013006
**Access:** Open access (CC-BY 4.0)

## Summary

A methodological / case-study paper presenting **synchrotron X-ray tomography + Discrete Element Method (DEM)** as a coupled framework for studying high-temperature sintering. Demonstrated on two systems: (1) copper powder with artificial pores, sintered in-situ at the ESRF synchrotron, and (2) **Ni-BaTiO₃ multilayer ceramic capacitors observed at Argonne National Laboratory** with 10–50 nm spatial resolution. Companion / precursor methodology to the later Okuma et al. *Acta Mater.* 2021 MLCC nano-CT paper.

This paper is the open-access entry point into the Grenoble + Argonne + Jülich collaboration that produced most of the recent in-situ MLCC sintering imaging literature.

## Key technical contributions

### 1. DEM model for high-T sintering
Particles modeled as spheres that **indent each other** under surface-energy-driven sintering forces. Mass-transport via **grain-boundary diffusion and surface diffusion** (Parhami-McMeeking model). Normal contact force:
$$
N_s = \frac{\pi a_s^4}{8 \Delta_b} \frac{d\delta}{dt} - \pi \gamma_s \cdot 8 R^* \cdot (1 - \cos(\psi/2)) + a_s \sin(\psi/2)
$$
- `a_s` = contact radius, `δ` = indentation
- `Δ_b` = T-dependent diffusion coefficient
- `γ_s` = surface energy
- `ψ` = dihedral angle (equilibrium contact shape)
- The first term is viscous; the second is the sintering driving force.

A tangential force opposes relative motion at the contact. The combined model captures particle rearrangement + neck growth + densification kinetics.

### 2. Validation with Cu / artificial-pore experiment
Cu sample with controlled large pores sintered in-situ at ESRF.
- **Resolution**: 1.5 µm (microtomography), several scans over the sintering cycle.
- Comparison of **measured particle-center displacements** vs **mean-field DEM predictions** reveals significant local rearrangement that mean-field theory misses.
- DEM produced **less rearrangement** than experiment (suggests model under-constrains some friction parameter) but accurately predicted bulk densification kinetics.

### 3. MLCC application
Ni-BaTiO₃ MLCCs observed by **synchrotron nano-tomography at Argonne** with 10–50 nm spatial resolution.
- Confirmed that **Ni layer heterogeneity** (the [[ni-batio3-cosintering-interface|interfacial liquid alloy + Rayleigh-Plateau breakup]] phenomenon) is set early in the sintering process by **initial powder packing heterogeneities**.
- DEM simulations confirmed that fast heating rate and electrode-additive content reduce defect formation — consistent with [[sintering-profile-mlcc|Polotai 2007]] empirical findings.

## Relevance to MLCC engineering

Two practical lessons:
1. **Initial powder packing** in the green-printed electrode layer is at least as important as the firing profile for determining the final Ni-layer continuity. Print uniformity and dispersion control matter more than people credit.
2. **DEM simulation** is now a mature tool that vendors use internally to optimize sintering recipes per part. The published literature shows the methodology; the proprietary parameter sets are vendor IP.

The Acta Mater 2021 paper (Okuma et al.) extends this work to **smaller-scale Ni-layer dynamics during break-up** in actual production-style MLCCs.

## Concepts discussed
- [[sintering-kinetics-batio3]]
- [[ni-batio3-cosintering-interface]]
- [[constrained-sintering-mlcc]]
- [[grain-growth-dopant-pinning]]
- [[mlcc-manufacturing-process]]
- [[sintering-profile-mlcc]]

## Entities mentioned
- Univ. Grenoble Alpes / CNRS SIMAP — primary research group (Yan, Martin, Bouvard)
- ESRF (European Synchrotron Radiation Facility) — Cu sample imaging
- Argonne National Laboratory — MLCC nano-CT imaging
- Forschungszentrum Jülich (Guillon group)

## References
_Original source: `resources/literature/epj-in-situ-xray-tomography-dem.md`_
