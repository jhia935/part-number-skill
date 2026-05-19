---
title: Two-Step Sintering (Chen-Wang Method)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources: []
tags:
  - paper
---

# Two-Step Sintering (Chen-Wang Method)

A two-stage sintering recipe that achieves **high density without grain growth** by exploiting the different temperature dependencies of densification and grain-boundary mobility. Proposed by I.-W. Chen and X.-H. Wang (Univ. of Penn., 2000–2006). The de-facto standard for producing **dense nanocrystalline BaTiO₃** and other oxide ceramics for applications where grain size must be kept small (modern thin-layer MLCC, transparent ceramics, structural ceramics).

## The recipe (Chen-Wang TSS)

```
Step 1:  ramp to T1 = 1300 °C, hold briefly (intermediate density ~75 %).
Step 2:  cool to T2 = 1100 °C, hold for 0–20 h (final density → 96+%, grain size frozen).
```

For BaTiO₃ specifically:
- **T1 = 1300 °C, short hold (~ minutes)**: ensures pore closure to "closed-pore" regime (~ 75 % density) where pores are isolated and densification can continue by GB diffusion alone, **without** surface-diffusion-driven coarsening.
- **T2 = 1100 °C, long hold (hours)**: kinetic window where GB diffusion (densification) is still active but **GB mobility (grain growth) is frozen** because surface diffusion (which controls pore-boundary mobility and thus grain growth in late-stage sintering) has higher activation energy than GB diffusion.

## The kinetic window
[[sintering-kinetics-batio3|Activation-energy hierarchy]] `Q_surf < Q_GB < Q_vol` means that **dropping T from T1 to T2 turns off surface diffusion proportionally more than GB diffusion**. By choosing T2 carefully — below the surface-diffusion threshold but above the GB-diffusion threshold — densification proceeds while grain growth halts.

This is the "kinetic window utilized in second-step sintering" cited in the Chen-Wang papers.

## Quantitative results for BaTiO₃

| Method | Final density | Final grain size |
|---|---|---|
| Conventional sintering, 1300 °C × 2 h | 96–98 % | 1–5 µm |
| Conventional sintering, 1100 °C × 2 h | 75–85 % | 100–300 nm |
| **Two-step (1300 °C ramp / 1100 °C hold)** | **96+ %** | **35 nm** (Chen-Wang JACerS 2006) |

The two-step path achieves the same density as the conventional 1300 °C hold but with **30× smaller grains**. Crucial for thin-layer (sub-µm) MLCC where the [[core-shell-batio3|3-grains-per-layer rule]] requires `r̄ < d/3`.

## Why it works (mechanism summary)
Conventional single-step sintering at 1300 °C: both densification and grain growth are active → high density but coarse grains.
Conventional single-step sintering at 1100 °C: too cold for full densification → low density.
Two-step: pre-densify quickly at 1300 °C (pore closure), then drop T to suppress grain growth while completing densification.

The "trick" is that **late-stage densification is GB-diffusion-limited**, while **grain growth is surface-diffusion-limited** (pore-boundary mobility). The two-step T schedule favors the former.

## Limitations
- Only works for the late stage of sintering (post-pore-closure). Useful for the final ~5–20 % of density.
- T1 must be high enough to reach closed-pore density but **not so high that grains coarsen excessively** during the brief hold.
- Requires precise temperature control of the second-step hold — too cold and densification stalls; too hot and grain growth restarts.
- Total cycle time longer than single-step (2–20 h second-step hold).

## Use in industrial MLCC?
Open question. Published commercial recipes resemble TSS in spirit (multi-stage profiles per [[sintering-profile-mlcc]]) but the exact T1 / T2 / hold times are proprietary. The Polotai 2007 multi-stage paper is the closest open-literature analogue applied to actual MLCC chips with electrodes.

## Cross-references
- [[sintering-kinetics-batio3]]
- [[grain-growth-dopant-pinning]]
- [[sintering-profile-mlcc]]
- [[core-shell-batio3]]
- [[mlcc-manufacturing-process]]

## References
- I.-W. Chen and X.-H. Wang, "Sintering dense nanocrystalline ceramics without final-stage grain growth," *Nature* 404 (2000) 168.
- X.-H. Wang and I.-W. Chen, "Two-Step Sintering of Ceramics with Constant Grain-Size, II: BaTiO₃ and Ni–Cu–Zn Ferrite", *J. Am. Ceram. Soc.* 89:2 (2006) 438–443.
- Mazaheri et al., "A review of two-step sintering for ceramics", *Ceramics International* 42 (2016) 8484–8505.
