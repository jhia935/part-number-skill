---
title: BME vs PME Electrode Technology
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - psma-ceramic-capacitor-basics.md
  - nasa-nepp-bme-mlcc-reliability.md
tags:
  - paper
---

# BME vs PME Electrode Technology

MLCC inner electrodes can be either **PME** (precious-metal electrode — Pd, Pd-Ag, Ag) or **BME** (base-metal electrode — Ni for the inner electrode, Cu for the termination). The choice cascades into atmosphere, dielectric chemistry, cost, and reliability.

## Why the split exists
Precious metals don't oxidize in air during co-firing at ~1350 °C — straightforward process, but **expensive**. Base metals (Ni, Cu) oxidize in air. To use them, the dielectric must be **co-fired in a reducing atmosphere** (very low PO₂), which:
1. Avoids oxidizing the electrode.
2. **Creates oxygen vacancies** in the dielectric.
3. Those oxygen vacancies migrate under DC bias and degrade the insulation resistance — the central reliability challenge of BME.

[[murata]] commercialized Ni-BME in **1982** ([Engineering and Technology History Wiki milestone](https://ethw.org/Milestones:Commercialization_of_Multilayer_Ceramic_Capacitors_with_Nickel_Electrodes,_1982)).

## Mitigation of oxygen-vacancy IR degradation
Two paths, both used in modern BME:
1. **Re-oxidation anneal** — a low-temperature firing in O₂-rich atmosphere after sintering, refilling vacancies near grain boundaries.
2. **Rare-earth doping** — Y, Ho, Dy, Er, Tb etc. dopants pin or slow vacancy migration. This is the basis of the [[core-shell-batio3]] microstructure that dominates X7R-grade BME today.

## Cost & application split
| Property | PME | BME |
|---|---|---|
| Inner electrode | Pd or Pd-Ag | **Ni** |
| Termination | Ag | **Cu** |
| Firing atmosphere | air | reducing |
| Metal cost | high | low |
| Achievable N | limited (~30–100 historically) | high (250–1000+ today) |
| Volumetric efficiency | low | high |
| IR degradation risk | low | non-trivial, mitigated |
| Mil/space spec heritage | MIL-PRF-123 default | qualifying for high-rel |

Most commercial Class II MLCCs since the 1990s are BME. PME survives in high-reliability (space, military), high-Q RF (where higher conductivity of Ag matters), and some Class I parts.

## Electrical-resistance ordering
For RF capacitors, [[psma-ceramic-capacitor-basics]] shows Cu-BME has **lower bulk resistivity than Ni-BME, Pd-PME, or Ag-PME** — counterintuitively, the BME option using Cu beats the Ag option once you account for the alloying needed to make the inner-Pd-electrode paste sinter-compatible. This is why Cu-BME is the basis of [[kemet-arcshield]] and most low-loss RF MLCCs.

## Cross-references
- [[bme-reliability-model]] — the two-mode reliability framework that's specific to BME
- [[core-shell-batio3]] — rare-earth-doped microstructure that makes BME work
- [[murata]] — BME pioneer

## References
- [[psma-ceramic-capacitor-basics]]
- [[nasa-nepp-bme-mlcc-reliability]]
