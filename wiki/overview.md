---
title: Overview
type: overview
created: 2026-05-19
updated: 2026-05-19
tags: []
---

# Overview

A synthesis of the MLCC knowledge base built around a single deliverable: a **design simulator** that predicts MLCC behavior from material, sheet thickness, layer count, overlap area, and chip size.

## Current state

The simulator specification lives at [`resources/design-rules/simulator-model.md`](../resources/design-rules/simulator-model.md) and is **v0 — sufficient to build a first-cut simulator**. It defines:

1. **Inputs**: dielectric class, εr₀, grain size r̄, layer thickness d, electrode thickness d_e, layer count N, case size, end/side margins, operating V_DC / V_AC / f / T / t_life.
2. **Capacitance**: `C₀ = εr · ε₀ · A · N / d` with effective area `A = (L − 2m_end)(W − 2m_side)` and an `N_max` budget from `H − 2 d_cover`.
3. **Stress factors**: multiplicative `f_VCC(E) · f_AC(V_AC) · f_T(T) · f_age(t,E,T)` corrections.
4. **Reliability**: Liu's structure × acceleration × Weibull, with two-mode BME acceleration (catastrophic power-law + slow exponential).
5. **Parasitics**: `Z(ω) = √(ESR² + (ωL − 1/ωC)²)` with case-size-keyed ESL.
6. **Voltage rating + arcing checks**.

A worked example (X7R BME 0805, 10 µF/6.3 V) reproduces published vendor envelopes. Open gaps are documented inline in the model file.

## Key themes that emerged

- **Field, not voltage**, is the right independent variable. `E = V/d` drives every Class-II non-ideality.
- **The N amplifier** ([[bme-reliability-model]]): tiny per-layer reliability defects multiply across hundreds of layers in modern BME parts, so dielectric quality at the grain scale is paramount.
- **Grain size is the new dimension**: state-of-the-art parts can no longer just thin the layer — they have to engineer [[core-shell-batio3]] microstructure with rare-earth doping ([[murata]] WO2024247128A1; [[samsung-electro-mechanics]] Tb-Dy patents). The patent activity here in 2024–2025 confirms this is the live competitive frontier.
- **BME vs PME** ([[bme-vs-pme]]) is largely settled (BME for cost / volumetric efficiency), but [[vishay]] still publishes the strongest case for PME on DC-bias-aging robustness.
- **Mechanical failure modes** ([[failure-modes-mlcc]]) — flex cracks, thermal shock, surface arcing — drive case-size and termination-style choices independently of the electrical model.

## What's intentionally absent

- TDK and Taiyo Yuden catalog data — the catalog PDFs were blocked by anti-bot during download. Their entity pages exist as drafts and pending catalogs should land in `resources/market/` next.
- Process-step deep dives. Manufacturing got light coverage relative to design rules because the simulator goal is operating-condition prediction; for a manufacturing-yield-prediction simulator we would deepen `resources/manufacturing/`.
- Empirical (E₀, p) fits for the VCC sigmoid against published Murata/Samsung curves. Vendor PDFs publish graphs only; digitization is a v1 task.

## Open questions

- Quantitative `εr(grain size)` data points below ~150 nm. The collapse region is reported qualitatively but not curve-fitted in the open literature we've found.
- BME catastrophic-mode voltage exponent `n` ranges from 2.5 to 6 across studies; need to understand whether this is method-dependent or material-dependent.
- AEC-Q200 derating — the simulator currently approximates auto-grade as commercial × 0.8; a proper qualification-curve mapping is pending.
