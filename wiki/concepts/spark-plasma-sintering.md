---
title: Spark Plasma Sintering (SPS / FAST)
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: medium
sources: []
tags:
  - paper
---

# Spark Plasma Sintering (SPS / FAST)

Field-assisted sintering technology (FAST), commonly called **spark plasma sintering (SPS)**, uses pulsed DC current through a graphite die to heat a powder compact at extreme rates (up to **1000 °C/min**) while applying uniaxial pressure (~ 50–200 MPa). Achieves >99 % density at much lower temperature and shorter time than conventional sintering — and **largely freezes grain size** at the powder value, ideal for nanocrystalline ceramics.

## Process
- Powder is loaded into a graphite die between two graphite punches.
- Vacuum or inert gas (Ar) chamber.
- Pulsed DC current (a few volts, kA-class amperage) passes through the die + powder.
- Joule heating ramps up to peak temperature (typically 1000–1300 °C for BaTiO₃) in **3–10 minutes**.
- Uniaxial pressure applied throughout — promotes mechanical particle rearrangement, contributes to densification.
- Hold at peak for **a few minutes** typically.
- Cool down (faster than conventional — no constraint from large thermal mass).

Total cycle time: **15–60 minutes** (vs 6–18 hours for conventional pusher furnace).

## BaTiO₃ SPS results (literature consensus)

| Parameter | Value |
|---|---|
| Peak temperature | 900–1200 °C |
| Pressure | 50–100 MPa |
| Hold time | 1–10 min |
| Final density | 97–99.5 % |
| Grain size | similar to starting powder (e.g., 0.6 µm) |
| **εr at room T, 1 kHz** | **~3500** (vs ~2000 for conventional sintering at the same grain size) |
| **Sub-µm grain SPS BaTiO₃ (20 nm grains)** | densities > 97 % achievable |

The **doubled εr vs conventional** comes from reduced GB defect density and tighter microstructure control.

## Why εr is higher in SPS BaTiO₃
1. Less oxygen-vacancy accumulation: short time at peak T means less reduction → higher [[heywang-jonker-model|Schottky barrier]] uniformity, less [[insulation-resistance|IR scatter]].
2. Less surface contamination on grain boundaries (no long-duration atmosphere exposure).
3. Fine-grain, dense microstructure means more [[ferroelectric-domain-wall|domain walls]] per volume contributing to εr.
4. SPS-grown grains have anisotropic / textured crystallographic alignment in some cases — favorable for εr.

## Disadvantages for MLCC manufacturing
SPS has not displaced conventional pusher-furnace BME sintering for production MLCC because:
- **Geometry**: SPS dies are cylindrical or rectangular billet — not compatible with millions of tiny ~mm² chips per batch.
- **Throughput**: even though each cycle is fast, batch size is limited to die area. A pusher furnace processes millions of chips per shift.
- **Co-firing with internal electrodes**: SPS pressure can deform thin (sub-µm) Ni electrode tapes; precise PO₂ control is harder in graphite-die environment.
- **Cost**: SPS equipment is more capital-intensive than belt or pusher furnaces.

## Research-scale applications
- Nanostructured BaTiO₃ ceramics (20 nm grain) for academic studies of finite-size effects on ferroelectricity.
- High-εr energy-storage capacitors (single-monolith, not MLCC) — colossal-εr BaTiO₃ × CaCu₃Ti₄O₁₂ composites.
- BME C0G research where lower processing T enables BaTiO₃ × MgO core-shell composites.

## Cross-references
- [[sintering-kinetics-batio3]]
- [[mlcc-manufacturing-process]]
- [[batio3]]
- [[cold-sintering]]
- [[ferroelectric-domain-wall]]

## References
- Anselmi-Tamburini et al., "Field-Assisted Sintering Technology / Spark Plasma Sintering: Mechanisms, Materials, and Technology Developments".
- Multiple ScienceDirect / J. Am. Ceram. Soc. papers on SPS BaTiO₃ — see web search for current state of the art.
- Paper "From core–shell BaTiO₃@MgO to nanostructured low dielectric loss ceramics by spark plasma sintering".
