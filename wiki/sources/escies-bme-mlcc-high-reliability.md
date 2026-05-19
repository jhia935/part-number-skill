---
title: "KEMET / Gurav et al. — Base-Metal Electrode (BME) Ceramic Capacitors for High Reliability Applications (ESA)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/escies-bme-mlcc-high-reliability.md
tags:
  - paper
status: complete
importance: high
---

# KEMET / Gurav et al. — BME Ceramic Capacitors for High Reliability Applications

**Source:** `resources/literature/escies-bme-mlcc-high-reliability.md` (PDF: `resources/literature/pdf/escies-bme-mlcc-high-reliability.pdf`)
**Authors:** Abhijit Gurav, Craig Scruggs, Richard Turner, Travis Ashburn ([[kemet]] Electronics Corporation)
**Venue:** Hosted on ESCIES (European Space Components Information Exchange System); ESA-affiliated open archive

## Summary

The most useful single-source comparison of **BME C0G** (CaZrO₃-based, Class I BME) vs traditional **PME C0G** (BaNdTi-based, Class I PME), grounded in measured HALT data. Establishes that modern [[bme-vs-pme|BME]] technology has surpassed PME on reliability **even for Class I parts** — historically the last preserve of PME.

## Key quantitative findings

**Dielectric constants:**
- PME C0G (BaNdTi): k ≈ 70
- BME C0G ([[cazro3|CaZrO₃-based]]): k ≈ 31

**Yet BME C0G achieves higher capacitance / smaller size** because much thinner dielectric layers are achievable:
- PME C0G 1206 / 10 nF: dielectric thickness 11.6 µm
- BME C0G 1206 / 10 nF: dielectric thickness 7.0 µm

**HALT reliability (175 °C / 400 V):**
| Type | MTTF |
|---|---|
| PME C0G 1206 / 10 nF | 62.6 minutes |
| BME C0G 1206 / 10 nF | **869.6 minutes** (13.9× longer) |

**Insulation resistance & temperature:**
BME C0G IR **increases** beyond 120 °C (uncommon — most ceramic IR drops with T), giving >2 orders of magnitude higher IR than PME at 200 °C. Mechanism: CaZrO₃'s wide-band-gap + reduction-resistant lattice + tight perovskite O-binding.

**Breakdown voltage:**
BME C0G 1206/100nF: BDV > 200 V/µm at 150 °C and above. Crucial for HV and pulse apps.

**4000-hour life test at 2× rated V, 125 °C:**
Both BME C0G and BME X7R portfolios passed with zero failures across multiple part types (Tables 1–2). Only one outlier: X7R 0805 / 2.2 µF at 20V life-test stress failed between 2000–3000 h.

## Process & microstructure notes
- BME C0G fires in reducing atmosphere, then **optimized re-oxidation anneal** — but the CaZrO₃ formulation is so reduction-resistant that the reoxidation step is more of a refinement than a necessity.
- BME X7R uses **BaTiO₃ powder available at 150 / 200 / 250 nm** sizes.
- "[[core-shell-batio3]] type microstructure" with high-crystallinity BaTiO₃ core and dopant-rich shell, with **uniform grain size** after firing.

## Production scale
> World-wide production: **~2 trillion MLCC pieces per year**

## Concepts discussed
- [[bme-vs-pme]]
- [[bme-reliability-model]]
- [[cazro3]]
- [[core-shell-batio3]]
- [[bme-sintering-atmosphere]]
- [[re-oxidation-anneal]]

## Entities mentioned
- [[kemet]] — authors
- [[bme-c0g]] — KEMET's flagship Class I BME product family (the subject of this paper)

## References
_Original source: `resources/literature/escies-bme-mlcc-high-reliability.md`_
