---
title: Cold Sintering
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: medium
sources:
  - cold-sintering-annual-review-mse.md
tags:
  - paper
---

# Cold Sintering

A class of low-temperature densification processes (typically **room T to 300 °C**, far below the material's melting point) that use a **transient liquid transport phase** plus **uniaxial pressure** to densify ceramic powder compacts. Pioneered by Clive Randall's group at Penn State (2016+). Bears a strong family resemblance to [[sintering-aids-glass|liquid-phase sintering]], but with the "liquid" being a thin aqueous (or solvent-based) film at the particle surface rather than a fired glass.

## Process

```
1. Mix ceramic powder with a small amount of transient liquid (typ. water, acetic acid, ammonium salts).
2. Load into a die.
3. Apply uniaxial pressure (~200–500 MPa).
4. Heat to 100–300 °C while maintaining pressure.
5. Liquid promotes dissolution-reprecipitation at particle contacts → densification.
6. Liquid evaporates during the heating → leaves a dense ceramic.
```

Cycle time: minutes. Final density: 80–98 % typical, up to >99 % for the easiest systems.

## Mechanism (per Guo, Randall et al. 2019 Annual Review)
A multi-stage densification analogous to liquid-phase sintering but at much lower T:
1. **Particle rearrangement** under pressure (mechanical).
2. **Dissolution of high-curvature regions** into the transient liquid film.
3. **Reprecipitation at low-curvature regions** (necks between particles).
4. **Final pore closure** by Ostwald ripening of remaining pores in liquid film.

Grain growth follows classical kinetics (∝ t^(1/n)) but with **activation energies much lower** than thermally-driven solid-state diffusion — the liquid film provides a fast mass-transport shortcut.

## What it enables
- **Co-firing of ceramics with materials that can't survive 1000+ °C**: polymer composites, low-melting metals (Sn, Bi, In). Cold-sintered BaTiO₃ has been co-densified with polymer matrices to make mixed ceramic-polymer capacitors.
- **Multimaterial nanocomposites** with previously incompatible processing windows.
- **Sintering ceramics traditionally considered "unsinterable"** (e.g., Na-containing perovskites that volatilize Na at high T).

## BaTiO₃ cold sintering results (research scale)
- Density 90–95 % achievable at 180–250 °C with acetic acid + water + Ba(OH)₂ surface modifier.
- εr ≈ 1000–2000 — significantly lower than conventionally sintered BaTiO₃ (3000–5000) due to residual porosity and surface defects.
- Energy-storage density (vs breakdown V) **higher** than conventional BaTiO₃ because of finer grain and reduced GB defect density.

## Why not for MLCC manufacturing (yet)
- Pressure requirement (~ 200+ MPa) — incompatible with thin internal electrode tapes (would deform / break Ni stripes).
- Density not yet high enough for high-IR / long-life dielectric applications.
- Throughput limited (batch process).
- Co-firing with [[ni-batio3-cosintering-interface|Ni internal electrodes]] not yet demonstrated at production scale.

But the **research direction** is active. Future thin-layer flex MLCCs could plausibly use cold-sintered dielectric layers with conductive-polymer "electrodes" — an entire new manufacturing branch enabled by cold sintering.

## Cross-references
- [[sintering-kinetics-batio3]]
- [[sintering-aids-glass]]
- [[spark-plasma-sintering]]
- [[mlcc-manufacturing-process]]
- [[batio3]]

## References
- [[cold-sintering-annual-review-mse]] — Guo, Floyd, Lowum, Maria, Herisson de Beauvoir, Seo, Randall, "Cold Sintering: Progress, Challenges, and Future Opportunities", *Annu. Rev. Mater. Res.* 49 (2019) 275–295.
- ScienceDirect "Microstructure, dielectric, and energy storage properties of BaTiO₃ ceramics prepared via cold sintering" (2017).
