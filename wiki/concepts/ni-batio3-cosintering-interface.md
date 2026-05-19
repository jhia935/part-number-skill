---
title: Ni-BaTiO₃ Co-Sintering Interface
type: concept
created: 2026-05-19
updated: 2026-05-19
sources: []
tags:
  - paper
---

# Ni-BaTiO₃ Co-Sintering Interface

Where it goes wrong in BME MLCC manufacturing. Co-sintering Ni inner electrodes with BaTiO₃ dielectric at 1100–1300 °C produces a chemically reactive interface whose dynamics determine whether you end up with a clean, continuous electrode layer or a broken, beaded-up Ni stripe that destroys the active area.

## The interfacial liquid alloy
At 1000–1100 °C under tension, a **thin (~10 nm) liquid (Ni, Ba, Ti) alloy film** forms at every Ni / BaTiO₃ interface. The high-T liquid film:
- Drastically lowers interfacial free energy
- Provides a fast kinetic pathway for mass transport along the interface
- **Accelerates Ni grain coarsening + Rayleigh-instability driven break-up of the Ni layer**

This liquid is the **single biggest driver of electrode discontinuity** in modern thin-layer MLCCs.

## Discontinuity formation (Rayleigh-Plateau in reverse)
Stress-induced instability promotes diffusion **from thinner Ni regions toward thicker ones** (uphill in thickness, downhill in chemical potential because thinner regions are under more tension). The thinning regions accelerate until they break — leaving holes. Holes coalesce, ligaments collapse, and a once-continuous electrode becomes a patchwork.

Loss of electrode continuity reduces the **effective overlap area `A`** in the [[mlcc-capacitance-equation|capacitance equation]] — capacitance drops below spec.

## NiO inhibition of BaTiO₃ grain growth
Conversely, residual NiO (from partial oxidation of the Ni electrode or NiO-doped paste formulations) **inhibits BaTiO₃ grain growth**:
- NiO solubility in BaTiO₃: ~ 0.13 wt% at 1250–1330 °C (ScienceDirect, "Effect of NiO addition on the sintering and grain growth behaviour of BaTiO₃").
- Above this limit, NiO precipitates at GBs → Zener pinning of GB motion → finer BaTiO₃ grains.
- The Ni/NiO ratio in the electrode/dielectric system thus has a **tight, two-sided design window**.

## Shrinkage matching (the other interfacial problem)
Even before any chemical reaction, the two layers shrink at different rates during sintering:
- Pure Ni paste: shrinks ~ 25–35 % linearly between 600 and 1100 °C
- BaTiO₃ green: shrinks ~ 15–20 % over the same range, with the bulk of shrinkage in a narrow 1100–1300 °C window

Mismatch → in-plane tensile stress on the layer that shrinks more (typically Ni at intermediate T, BaTiO₃ at peak T) → cracks, delamination, **or** the Rayleigh-Plateau electrode break-up.

## Process counter-measures
1. **Add 50 nm BaTiO₃ powder to the Ni paste** (typical 5–20 vol%): delays Ni sintering / shrinkage until the dielectric catches up.
2. **Bimodal Ni powder** size distribution: tighter shrinkage profile than monomodal.
3. **Multiple-stage sintering** (Yan et al., "Multiple Stage Sintering to Control Ni Electrode Continuity in Ultra-Thin Ni–BaTiO₃ MLC"): a low-T hold ~1000 °C lets the (Ni, Ba, Ti) liquid drain off before reaching peak T, suppressing Rayleigh-Plateau break-up.
4. **Fast heating** through the 1000–1100 °C window: kinetically suppresses the interfacial liquid film formation.
5. **Sintering aids** in the dielectric (BaO-B₂O₃-SiO₂ glass): lowers dielectric sintering T to match Ni shrinkage curve.

## Synchrotron X-ray nano-CT observations
[Nano-CT studies (Acta Mater. 2021)](https://www.sciencedirect.com/science/article/pii/S1359645420310429) image the Ni electrode 3D morphology evolution in-situ during sintering. Confirms that:
- Layer breakup initiates as nm-scale undulation along the Ni/BaTiO₃ interface
- Hole nucleation precedes hole growth (no critical hole size; everywhere is statistically vulnerable)
- Adjacent Ni layers can "sympathetically" break at correlated locations due to coupled stress fields

## Implications for the simulator
- The simulator's effective overlap area `A` should be discounted by an **electrode-continuity factor** (vendor-quality dependent, typically 0.85–0.98 for modern Tier-1, lower for second-tier).
- Sub-µm dielectric parts have **much narrower process windows** because the Ni layer is also sub-µm and Rayleigh-Plateau scales with thickness.
- A simulator option could surface "electrode quality" as an input (0 = pristine, 1 = highly broken) for sensitivity analysis.

## Cross-references
- [[bme-sintering-atmosphere]]
- [[grain-growth-dopant-pinning]]
- [[sintering-kinetics-batio3]]
- [[mlcc-capacitance-equation]]
- [[bme-vs-pme]]
- [[mlcc-manufacturing-process]]

## References (web)
- ScienceDirect "Microstructure evolution during the co-sintering of Ni/BaTiO₃ multilayer ceramic capacitors modeled by discrete element simulations" (J. Eur. Ceram. Soc. 2014)
- Yan et al. "Utilization of Multiple Stage Sintering to Control Ni Electrode Continuity in Ultra-Thin Ni–BaTiO₃ Multilayer Capacitors"
- ScienceDirect "Shrinkage behavior and interfacial diffusion in Ni-based internal electrodes with BaTiO₃ additive"
- Penn State, "Stability of Ni electrodes and Ni-BaTiO₃ interface evolution in ultrathin BME MLCCs"
- ScienceDirect "Effect of NiO addition on the sintering and grain growth behaviour of BaTiO₃"
- ScienceDirect "Microstructural evolution of electrodes in sintering of multi-layer ceramic capacitors (MLCC) observed by synchrotron X-ray nano-CT" (Acta Mater. 2021)
