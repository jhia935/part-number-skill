---
title: Sintering Aids & Liquid-Phase Sintering Glass Systems
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources: []
tags:
  - paper
---

# Sintering Aids & Liquid-Phase Sintering Glass Systems

A small fraction of low-melting glass added to the BaTiO₃ green body forms a **viscous liquid phase** during firing that dramatically lowers the achievable sintering temperature, accelerates densification, and (when properly designed) suppresses grain growth. Used in **low-temperature co-fired ceramic (LTCC)** MLCC variants, in [[bme-c0g|BME C0G]] formulations where the dielectric must fire below the Cu inner-electrode melting limit (1085 °C), and in standard X7R formulations as fine-tuning of densification kinetics.

## Why add a glass aid
1. **Lower sintering T** from ~1300 °C to 900–1100 °C — enables Cu inner electrodes (BME Cu C0G) and reduces furnace energy / Ni grain coarsening.
2. **Faster densification** through dissolution-reprecipitation: ceramic surface dissolves into the liquid at convex points and reprecipitates at concave necks.
3. **Eliminate residual porosity** by filling pores with viscous liquid.
4. **Control grain growth**: properly chosen glass pins grain boundaries (forms wetting film at GBs that resists motion).

## Common glass systems for BaTiO₃

| System | Eutectic T | BaTiO₃ sintering T achieved | Notes |
|---|---|---|---|
| **BaO – B₂O₃ – SiO₂** (BBS) | ~ 850 °C | 900–950 °C with ≥ 93 % density | Standard for low-T BaTiO₃; lattice-compatible with Ba site |
| **PbO – B₂O₃ – SiO₂** (PBS) | ~ 600 °C | 850 °C | Pb-containing; restricted by RoHS in commercial parts |
| **ZnO – B₂O₃ – SiO₂** (ZBS) | ~ 700 °C | 900 °C, 95 % density, εr ≈ 994 | Pb-free, popular alternative |
| **BaO – B₂O₃ – Bi₂O₃** | ~ 700 °C | research scale | Bi-based, low loss |
| **Mn – Si – O** | ~ 1000 °C | 1100 °C | Targets Mn-doped Class II dielectrics |
| **B₂O₃ alone, PbB₂O₄** | ~ 500–700 °C | early Pb-borate work | Affects DF, BDV negatively at high addition |

## Mechanism details
1. **Wetting**: glass viscosity at firing T must be low enough to **wet** BaTiO₃ grain surfaces (γ_sl < γ_sv). Dihedral angle θ at solid-liquid-vapor lines ≤ 60° → penetrates GB → liquid-phase sintering active.
2. **Solubility-driven mass transport**: BaTiO₃ dissolves in the glass at high-curvature (convex) regions, supersaturates the liquid locally, and re-precipitates at concave necks. Fast — orders of magnitude faster than solid-state GB diffusion.
3. **Grain coarsening control**: glass film at GB pins boundaries via solute drag (similar to dopant pinning, but with an entire liquid film). Carefully tuned glass composition gives fine-grain final microstructure.

## Trade-offs
- **εr penalty**: most glass aids have lower εr than BaTiO₃ (50–500 vs 1000+). Even 5 vol% glass reduces ceramic εr by ~10–20 %.
- **DF penalty**: glass contributes additional dielectric loss; tan δ rises.
- **Reliability**: glass-rich GBs are weaker — flexural strength drops; in moisture, alkaline glass can leach.
- **Reduction sensitivity**: many glass systems (especially PbO-, Bi₂O₃-containing) are reducible under BME atmosphere — must verify atmosphere compatibility.

## Modern engineering knob
For BME Cu C0G ([[bme-c0g|BME C0G]]), the dielectric must sinter below ~1080 °C (Cu melting point) — this is impossible for neat BaTiO₃ or CaZrO₃. Glass aids are essential. [[kemet]]'s CaZrO₃-based BME C0G dielectric uses proprietary low-T sintering chemistry to hit this window.

## Cross-references
- [[sintering-kinetics-batio3]]
- [[bme-c0g]]
- [[grain-growth-dopant-pinning]]
- [[ni-batio3-cosintering-interface]]
- [[cazro3]]

## References (web)
- ScienceDirect: "Effect of glass composition on the densification and dielectric properties of BaTiO₃ ceramics" (J. Eur. Ceram. Soc. 2000)
- ScienceDirect: "Liquid phase sintering of BaTiO₃ by boric oxide (B₂O₃) and lead borate (PbB₂O₄) glasses" (1989)
- ScienceDirect: "Exploration of BaO–B₂O₃–Bi₂O₃ glasses as sintering aids for BaTiO₃ ceramics" (2020)
- ScienceDirect: "Low temperature sintering and dielectric properties of BaTiO₃ with glass addition" (2008)
