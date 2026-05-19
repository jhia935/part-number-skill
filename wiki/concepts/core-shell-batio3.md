---
title: Core-Shell BaTiO₃ Microstructure
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - adv-mater-2026-grain-boundary (search)
  - nasa-batio3-mlcc-failure-mechanisms.md
tags:
  - paper
---

# Core-Shell BaTiO₃ Microstructure

For ultra-thin dielectric layers (≤ 1 µm), each BaTiO₃ grain has to be small enough that 3–5 grains fit across the layer thickness, but **not so small that ferroelectricity collapses**. The industrial answer is the **core-shell** grain architecture: a ferroelectric core surrounded by a paraelectric shell, stabilized by rare-earth dopants.

## Why pure fine-grain BaTiO₃ fails for thin layers
Bulk BaTiO₃ has high `εr` (1500–6000 depending on grain size) because of ferroelectric domain motion. **Grain size scaling**:
- Grain ≈ 1 µm: peak `εr` ~6000
- Grain ≈ 200–260 nm: `εr` still ~3000–5000 — peak under DC fields > 4 V/µm
- Grain < 200 nm: `εr` collapses as the tetragonal-phase ferroelectricity loses to surface paraelectricity

A layer thinner than ~1 µm without compensation runs into this collapse.

## The core-shell architecture
1. **Core** (interior of each grain): ferroelectric BaTiO₃ tetragonal — high `εr`, the capacitance carrier.
2. **Shell** (outer rim of each grain): paraelectric, dopant-enriched — low `εr` but **temperature-flat** and **field-flat**. Stabilizes the temperature characteristic to meet X7R/X5R.

The shell is engineered by **rare-earth doping** (Y, Ho, Dy, Er, Yb) combined with Mg and Mn at the grain boundaries. Rare earths form a "donor + acceptor" co-doping system that pins oxygen vacancies (reliability) and creates the paraelectric shell (TCC).

[[adv-mater-2026-grain-boundary]] (An et al., *Advanced Materials* 2026) reports grain-boundary segregation as the controlling design lever for DC-bias performance — concentrating the rare-earth at the grain boundary rather than diffusing it through the grain core.

## Design rules for the simulator
- `d ≥ (3–5) · r̄` — at least 3 grains across the layer to retain shell-buffered behavior.
- `r̄ ≈ 200–260 nm` is the sweet spot for X5R/X7R under typical operating fields.
- Modern Murata and Samsung BME parts use 100–300 nm grain BaTiO₃ ([web research summary]) — Korean manufacturers historically lagged at 300–500 nm grains.
- Sub-µm `d` mandates core-shell + grain control + re-oxidation anneal.

## Active patent landscape
Recent patents observed:
- **WO2024247128A1** (Murata, May 2023 / Dec 2024 pub) — BaTiO₃ + rare earths Re + first-additive Me as minor components.
- Samsung Electro-Mechanics patents in this space (US 11,211,181 / 11,295,894 / 11,763,990 / 11,776,748 / 12,488,941) — Tb-Dy co-doped BaTiO₃ with specific molar ranges (Tb 1.2–3.0 mol%, Dy 2.5–3.4 mol% per 100 mol BaTiO₃).

The fact that the entire field is still **patenting dopant ratios** in 2024–2025 indicates this microstructure is the live competitive frontier.

## Related
- [[batio3]] — base material
- [[bme-reliability-model]] — uses `(r̄/d)^α` directly
- [[eia-rs-198-dielectric-classes]] — X7R / X5R is the spec the core-shell is engineered to meet
- [[bme-vs-pme]] — rare-earth doping is part of why BME works

## References
- [[nasa-batio3-mlcc-failure-mechanisms]]
- An et al., *Adv. Mater.* 2026, doi:10.1002/adma.202507233 — Microstructure Optimization via Grain-Boundary Segregation
- Various ScienceDirect papers on Y-Mg, Ho-Mg, Tb-Dy co-doped BME BaTiO₃
