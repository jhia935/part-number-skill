---
title: Grain Growth & Dopant Pinning in BaTiO₃
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - epfl-ceramics-sintering-microstructure.md
tags:
  - paper
---

# Grain Growth & Dopant Pinning in BaTiO₃

During sintering, grain boundaries (GBs) move so that larger grains consume smaller ones — driven by GB-energy reduction. Without intervention, BaTiO₃ would coarsen well past the [[core-shell-batio3|200–260 nm sweet spot]] needed for thin-layer X7R/X5R parts. Modern BME MLCCs achieve fine-grain microstructure through **chemical pinning**: dopants segregate to GBs and slow their motion.

## Normal vs abnormal grain growth
- **Normal grain growth** (NGG): mean grain size grows monotonically with hold time `t^(1/n)`; size distribution stays self-similar; controlled by GB curvature.
- **Abnormal / discontinuous grain growth** (AGG): a few "runaway" grains grow disproportionately fast, breaking the unimodal distribution. The runaway grains are usually surrounded by a liquid film (transient liquid-phase) or by anisotropic-step-energy facets. For BaTiO₃, AGG is triggered by:
  - Excess TiO₂ (Ti-rich green body) → Ba₆Ti₁₇O₄₀ low-melting eutectic
  - Excess Ba (TiO₂-poor) → BaO·TiO₂ unstable phases
  - Hot spots in furnace
  - Single-crystal seeds in the powder

Abnormal grains are death for MLCC reliability — they collapse the [[bme-reliability-model|(r̄/d)^α structural factor]] locally.

## Pinning mechanisms (slow GB motion)
1. **Solute drag (Cahn-Lücke)**: dissolved dopant atoms diffuse with the moving GB, dragging it. Mobility reduction up to 50× at 0.75 at% [aliovalent cation doping](https://www.sciencedirect.com/science/article/abs/pii/S095522199700215X) with Nb⁵⁺, La³⁺, or Co²⁺.
2. **Second-phase pinning (Zener)**: precipitates at GBs pin them mechanically. Force scales as `F_Zener = 4π·γ_GB·r·f_v / 3` where `r` is precipitate radius, `f_v` volume fraction. Used in MLCCs by exceeding rare-earth solubility slightly so RE-rich oxide pockets form at GB triple junctions.
3. **Pore pinning**: residual pores at GBs (the late-sintering regime) pin GBs unless pore-mobility (surface diffusion) is faster than GB mobility. Why high-density / final-stage sintering must avoid coarsening.

## Dopant landscape for MLCC
[Studies of aliovalent cation doping at 1300 °C / O₂ atmosphere](https://www.sciencedirect.com/science/article/abs/pii/S095522199700215X) show:
- **Lanthanides as single dopants** (La, Ce, Nd, Sm) → **rapid grain growth**. They sit on Ba-sites as donors and create electron carriers that suppress the GB band-bending — paradoxically accelerating GB motion.
- **Divalent / trivalent acceptor cations** (Mg²⁺, Ni²⁺, Mn²⁺, Fe³⁺) → strong **grain-growth inhibition** via solute-drag + GB-charge compensation.
- **Heavy rare earths** (Y, Ho, Dy, Er, Yb, Tb) **co-doped with Mg** → grain growth slowed enough for sub-300-nm grain BaTiO₃ to survive 1200–1300 °C BME firing; this is the [[core-shell-batio3|core-shell]] formation chemistry.
- **Mg²⁺ segregation** at GBs slows diffusion (similar effect documented in other ceramic systems).

## Liquid-phase grain growth
When low-melting eutectic forms (BaO-B₂O₃-SiO₂ glass aid or Ba₆Ti₁₇O₄₀ from TiO₂ excess), grain growth proceeds by **dissolution-reprecipitation** through the liquid — far faster than solid-state diffusion. Carefully controlled, this gives uniform fine grain; poorly controlled, it gives runaway AGG.

## Quantitative anchor for the simulator
Final grain size `r̄(after sintering)` is set by:
- Starting particle size (hydrothermal 100 nm vs solid-state 500 nm)
- Dopant identity and concentration (Mg + RE doping → keep r̄ ≤ 300 nm)
- Sintering temperature and hold time (lower T, shorter hold → smaller r̄)
- Atmosphere (reducing accelerates per [[arxiv-electron-localization-cation-diffusion]])

The simulator's reliability factor `(r̄/d)^α` is set by this final r̄. **Process engineers tune dopants to keep r̄ low**.

## Cross-references
- [[sintering-kinetics-batio3]]
- [[core-shell-batio3]]
- [[bme-reliability-model]]
- [[bme-sintering-atmosphere]]
- [[batio3-powder-synthesis]]

## References
- [[epfl-ceramics-sintering-microstructure]]
- ScienceDirect: "Grain boundary mobility of BaTiO₃ doped with aliovalent cations" (Acta Mater. 1997)
- ScienceDirect: "Interface structure dependent step free energy and grain growth behavior of core/shell grains in (Y, Mg)-doped BaTiO₃" (J. Eur. Ceram. Soc. 2022)
