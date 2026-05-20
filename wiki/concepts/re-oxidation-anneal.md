---
title: Re-oxidation Anneal (Post-Sinter)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - escies-bme-mlcc-high-reliability.md
  - nasa-ir-degradation-ni-batio3-2015.md
tags:
  - paper
---

# Re-oxidation Anneal

A controlled-atmosphere thermal step performed **after main sintering** to **partially refill the oxygen vacancies** created during the reducing-atmosphere co-firing of BME MLCCs ([[bme-sintering-atmosphere]]). Trades a small Ni oxidation risk for a major boost in insulation resistance and reliability.

## Process window
- Temperature: typically 900–1100 °C (well below the sintering peak of ~1300 °C).
- PO₂: somewhat higher than during sintering, but **still reducing relative to air**. Typical 10⁻⁸ to 10⁻⁹ atm — enough oxygen activity to react with O vacancies, not enough to oxidize Ni metal.
- Time: minutes to a few hours depending on dielectric thickness and grain size (limited by O-diffusion path length).

## What it does
1. **Refills O vacancies near grain boundaries** — the high-vacancy zones are where Schottky depletion layers form. Filling them raises the barrier height φ(0).
2. **Improves IR by 1–3 orders of magnitude** vs an as-fired-only part.
3. **Slows the [[oxygen-vacancy-migration]] electromigration** by reducing the carrier (vacancy) concentration.

## Limits
- Cannot fill all vacancies: penetration is O-diffusion-limited. Bulk grain interiors retain higher V_O concentrations.
- Modern thin-layer parts (sub-2 µm dielectric) have shorter diffusion paths and benefit more.
- CaZrO₃-based [[cazro3|Class I BME]] formulations are **inherently reduction-resistant** — the re-oxidation step is "for refinement, not necessity" ([[escies-bme-mlcc-high-reliability]]). BaTiO₃ Class II formulations require it.

## Defect / process pitfalls
- **Over-oxidation**: Ni inner electrode partially oxidizes → ESR rises, capacitance drops, in extreme cases electrode delaminates.
- **Under-oxidation**: residual V_O too high → IR scatter, accelerated DC-bias aging.
- **Non-uniform**: temperature or PO₂ gradient across the furnace produces electrical-parameter scatter across the lot.

## Implications for the simulator
- A part's post-reoxidation barrier height `φ(0)` (a key parameter in [[oxygen-vacancy-migration|Liu's IR-degradation model]]) is **set in this step**. For two BME parts with otherwise identical microstructure, the one with the better reoxidation has a higher `φ(0)` and slower `K = K₀·exp(-E_k/kT)`.
- The simulator should treat reoxidation efficacy as a vendor-quality knob — captured in the empirical `E_k` (1.6 eV commercial, 2.8 eV automotive — see [[nasa-time-dependent-ir-2013-prb]]).

## Cross-references
- [[bme-sintering-atmosphere]]
- [[oxygen-vacancy-migration]]
- [[mlcc-manufacturing-process]]
- [[bme-vs-pme]]
- [[cazro3]]

## References
- [[escies-bme-mlcc-high-reliability]]
- [[nasa-ir-degradation-ni-batio3-2015]]
- [[nasa-time-dependent-ir-2013-prb]]
