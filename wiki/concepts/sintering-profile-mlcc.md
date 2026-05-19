---
title: MLCC Sintering Profile (Heating Rate, Peak, Multi-Stage)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - escies-bme-mlcc-high-reliability.md
tags:
  - paper
---

# MLCC Sintering Profile (Heating Rate, Peak T, Multi-Stage)

The time-temperature recipe used to fire green MLCC chips into dense, electrically-functional ceramic monoliths. Modern BME profiles are **not** simple "ramp up, hold, ramp down" — they're engineered multi-segment programs that **trade off densification, grain-growth control, and Ni-electrode continuity**. The single biggest knob is **heating rate**.

## Typical commercial BME profile (0805, 300-layer)

A representative profile assembled from Polotai et al. *JACerS* 2007 and similar published recipes:

```
Stage 1: Binder burnout         200 → 600 °C        @ 1–3 °C/min,  Ar + ~1 vol% O2
Stage 2: Pre-sintering          600 → 1100 °C       @ 10–30 °C/min, transition to N2/H2 reducing
Stage 3: Approach peak          1100 → 1250 °C      @ 30–60 °C/min, fast through liquid-alloy window
Stage 4: Peak hold              1250 °C            for 1–2 h,    PO2 ≈ 10⁻¹⁰ to 10⁻¹² atm
Stage 5: Slow cooldown          1250 → 1000 °C      @ 5–10 °C/min, controlled atmosphere
Stage 6: Re-oxidation anneal    900–1100 °C        for 1–2 h,    PO2 ≈ 10⁻⁸ to 10⁻⁹ atm
Stage 7: Final cooldown         1000 → 25 °C        @ 5 °C/min
```

Total cycle time: **6–18 hours**. Pusher furnace throughput: ~10⁶ chips/day per chamber.

## Heating-rate effect on Ni electrode continuity

Polotai *et al.* (JACerS 2007, "Utilization of Multiple-Stage Sintering to Control Ni Electrode Continuity in Ultrathin Ni–BaTiO₃ Multilayer Capacitors") tested heating rates from **200 to 3000 °C/h** on 0805 / 300-layer parts. Key findings:

| Heating rate | Ni electrode continuity | Cause |
|---|---|---|
| Low (200 °C/h ≈ 3.3 °C/min) | **Poor** (extensive break-up) | Long dwell in the 1000–1100 °C window where the [[ni-batio3-cosintering-interface\|(Ni,Ba,Ti) liquid alloy]] forms — Rayleigh-Plateau instability has time to play out |
| Medium (10–30 °C/min) | Moderate | |
| **Fast (60 °C/min)** | **Best** at 1250 °C peak — sweet spot in their study | Kinetically suppresses interfacial liquid formation |
| Very fast (>100 °C/min) | Risk of cracking from thermal-shock stress | Thermal expansion not uniform across chip |

**The standard "fast heating rate" prescription** in modern BME MLCC literature is ~30–60 °C/min through the danger zone (1000–1250 °C), achieved by short, dense, high-velocity pusher-furnace zones.

## Peak temperature trade-off

Higher peak T → faster densification, fuller pore elimination, but:
- More [[grain-growth-dopant-pinning|grain growth]] → larger `r̄` → worse [[bme-reliability-model|reliability `(r̄/d)^α`]] factor
- More [[oxygen-vacancy-migration|oxygen vacancy formation]] → more reoxidation needed
- More [[ni-batio3-cosintering-interface|interfacial liquid alloy formation]] → worse electrode continuity
- Higher Ni-electrode grain coarsening → break-up risk

Lower peak T → less densification, residual porosity → mechanical weakness, lower BDV, higher leakage.

Modern commercial BME formulations tune **dopants and sintering aids** to hit full density at **1100–1250 °C** (the lower end of the historical 1200–1350 °C window). Some Cu-electrode systems hit density at **900–960 °C** (below Cu's 1085 °C melting point) using [[sintering-aids-glass|glass aids]].

## Atmosphere transitions
See [[bme-sintering-atmosphere]] for the PO₂ profile. Critical transitions:
- **Stage 1 → 2**: oxidizing (binder burnout) → reducing (sinter). Inhabits a narrow Ar + low-O₂ window.
- **Stage 5 → 6**: reducing (sinter) → slightly less reducing (reoxidation). PO₂ raised 1–2 decades.

## Why multi-stage matters
A flat single-stage profile (ramp + hold + cool) can't satisfy all the competing constraints:
- Stage 1 must be slow enough for clean binder removal without cracking
- Stages 2–3 must be **fast** through the electrode-instability window
- Stage 4 must be long enough at peak T for densification
- Stage 5 must be slow enough to allow [[cubic-tetragonal-transition|tetragonal phase transition]] domain formation without thermal shock
- Stage 6 must be at the right PO₂ to refill O-vacancies without oxidizing Ni

## Cross-references
- [[sintering-kinetics-batio3]]
- [[bme-sintering-atmosphere]]
- [[re-oxidation-anneal]]
- [[ni-batio3-cosintering-interface]]
- [[grain-growth-dopant-pinning]]
- [[two-step-sintering]]
- [[mlcc-manufacturing-process]]

## References
- Polotai, Yang, Dickey, Randall, "Utilization of Multiple-Stage Sintering to Control Ni Electrode Continuity in Ultrathin Ni–BaTiO₃ Multilayer Capacitors", *J. Am. Ceram. Soc.* 90:12 (2007) 3811–3817.
- Yoon, Shin et al., "Control of Connectivity of Ni Electrode with Heating Rates During Sintering and Electrical Properties in BaTiO₃-Based MLCCs" (Semantic Scholar)
- [[escies-bme-mlcc-high-reliability]]
- ScienceDirect "Oxidation of Ni electrode in BaTiO₃ based MLCC"
