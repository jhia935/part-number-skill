---
title: Nano-Grain BaTiO₃ εᵣ (50–150 nm Regime)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - srep-batio3-grain-size-unfolding.md
tags:
  - paper
---

# Nano-Grain BaTiO₃ εᵣ (50–150 nm Regime)

What happens to [[batio3|BaTiO₃]] dielectric constant as grain size drops below the ~200 nm sweet spot referenced in [[core-shell-batio3|core-shell engineering]]. The relevant regime for next-generation sub-µm dielectric MLCC where multiple grains per layer requires r̄ down to 100–150 nm. Quantitative anchors from peer-reviewed literature (Polotai 2009, Hennings & Schreinemacher 1992, Frey & Payne 1996, "Unfolding grain size effects" Sci. Rep. 2015).

## Quantitative εᵣ vs grain size

| Grain size r̄ | εᵣ at 25 °C, 1 kHz | Tetragonality c/a | Notes |
|---|---|---|---|
| 5 µm | ~ 1500–2000 | 1.011 | bulk coarse-grain |
| 2 µm | ~ 3000 | 1.010 | typical "normal" sintering |
| **1 µm** | **~ 5000–6000 (peak)** | 1.009 | the εᵣ maximum |
| 0.8 µm | ~ 5000 | 1.008 | still near peak |
| 0.5 µm | ~ 4000 | 1.006 | shoulder of peak |
| 0.3 µm | ~ 2500–3500 | 1.004 | core-shell sweet spot for X7R |
| **0.2 µm** | **~ 2000–3000** | 1.002 | thin-layer SOTA target |
| 0.15 µm | ~ 1500 | ~1.000 | approaching paraelectric |
| **0.10 µm (100 nm)** | **~ 1000** | 1.000 (essentially cubic) | tetragonal distortion suppressed |
| 0.05 µm (50 nm) | **< 1000** (some reports as low as 200) | 1.000 | "ferroelectric collapse" regime |
| 0.03 µm (30 nm) | (paraelectric) | n/a | below critical size |
| **0.01 µm (10 nm)** | **paraelectric only** | n/a | ferroelectricity disappears |

Sources synthesizing this table:
- Hennings & Schreinemacher (JJAP 1992): foundational coarse → fine BaTiO₃ data
- Frey & Payne (PRB 1996): nanocrystalline εᵣ depression mechanism
- "Unfolding grain size effects" Sci. Rep. 9953 (2015): cross-comparison of sintering methods on grain-size-vs-εᵣ dependence
- Polotai et al. (Acta Mat. 2009): nanocrystalline BaTiO₃ ceramics with d_avg 50 nm

## The critical size for ferroelectricity disappearance
Published critical-size estimates vary by method and material form:
- **Epitaxial thin films**: a few nm
- **Nanoparticles** (free-standing): 10–30 nm
- **Dense nanoceramics** (sintered bulk): 10–20 nm

Below this threshold, BaTiO₃ stays cubic even at room temperature — no spontaneous polarization. The "tetragonal distortion" c/a collapses to 1.000 and εᵣ saturates at a small ionic + electronic value (~ 100–300).

## Why εᵣ drops below 200 nm — the "dead layer" model

Two competing pictures explain the drop:

### Intrinsic size effect
At small grain size, ferroelectric long-range order is energetically unfavorable. The Landau-Ginzburg free energy minimum shifts from tetragonal to cubic when surface energy (proportional to surface area = 1/r) exceeds the bulk polarization free energy. Critical size emerges from `f_polar = f_surface`.

### "Dead layer" model
Each grain has a paraelectric **dead layer** (~ 1–2 nm thick) at its surface — a region where ferroelectric order is locally suppressed by surface termination effects. For a 1 µm grain, the dead layer is 0.1–0.2 % of the volume; for a 50 nm grain, it's 4–8 %. As grain shrinks, dead-layer "dilution" dominates → effective εᵣ drops.

Both mechanisms are real; they compound at small grain. Modern thinking: the dead layer is the **dominant** mechanism for the 50–200 nm range; intrinsic size effect kicks in only below ~ 30 nm.

## What this means for MLCC engineering

For thin-layer dielectric `d ≤ 1 µm`:
- The [[core-shell-batio3|3-grains-per-layer rule]] (d ≥ 3 r̄) forces r̄ ≤ d/3.
- For d = 1 µm: r̄ ≤ 333 nm. Use the 200–300 nm sweet spot — εᵣ ~ 2500–3500.
- For d = 0.5 µm: r̄ ≤ 167 nm. εᵣ drops to ~ 1500–2000.
- For d = 0.3 µm (state-of-the-art Murata): r̄ ≤ 100 nm. εᵣ ~ 1000. **Density penalty** vs nominal BaTiO₃.
- For d = 0.1 µm (research): r̄ ≤ 33 nm. Below critical size; ferroelectricity essentially gone; εᵣ ~ 300. **No longer X7R territory**.

This is the physical reason **thin-layer scaling has limits**: at some point, smaller grains reduce εᵣ faster than thinner layers increase volumetric efficiency.

The [[nasa-batio3-mlcc-failure-mechanisms|NASA volumetric-efficiency-ceiling]] (~ 3000–4000 µF/cm³ at d → 0.5 µm) is a direct consequence of this εᵣ(r̄) collapse.

## Mitigation: core-shell engineering
The [[core-shell-batio3|core-shell architecture]] partially **defeats** the εᵣ drop by:
1. Keeping the **core** at 100–200 nm crystalline diameter — well above critical size.
2. Adding a **paraelectric shell** (low εᵣ, ~ 100–300) at the grain boundary that effectively acts as the "dead layer" — but at engineered thickness and composition.
3. Net effect: composite εᵣ ~ 3000+ in a grain that would otherwise have εᵣ ~ 1500.

This is **why Tier-1 BME parts can still claim εᵣ ~ 3000 at d = 0.3 µm**: the core is large enough to retain ferroelectricity; the shell adds a controlled rather than uncontrolled paraelectric contribution.

## Implications for the simulator
The simulator's bulk-εᵣ input parameter should be modeled as:
$$
\varepsilon_r(\bar r) \;\approx\; \frac{\varepsilon_{r,\infty}}{1 + (r_\text{crit}/\bar r)^p}
$$
with empirical fits:
- `ε_{r,∞}` ≈ 5000 (peak at r̄ ~ 1 µm)
- `r_crit` ≈ 80–120 nm (the half-amplitude point)
- `p` ≈ 3–5

For sub-150 nm grain parts, the simulator should **not** use the bulk peak εᵣ — use a grain-size-derated value.

## Cross-references
- [[batio3]]
- [[core-shell-batio3]]
- [[permittivity]]
- [[curie-temperature]]
- [[cubic-tetragonal-transition]]
- [[ferroelectric-domain-wall]]
- [[srep-batio3-grain-size-unfolding]]

## References
- [[srep-batio3-grain-size-unfolding]] — *Scientific Reports* 9953 (2015), the cleanest cross-method comparison
- Hennings & Schreinemacher, *JJAP* (1992)
- Frey & Payne, *Phys. Rev. B* 54 (1996) 3158 — nanocrystalline εᵣ depression
- Polotai et al., *Acta Mater.* 57 (2009) — d_avg 50 nm BaTiO₃ ceramics
