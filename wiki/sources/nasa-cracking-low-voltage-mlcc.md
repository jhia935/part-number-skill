---
title: "NASA / Teverovsky — Cracking Problems in Low-Voltage Chip Ceramic Capacitors (NEPP 2018)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-cracking-low-voltage-mlcc.md
tags:
  - paper
status: complete
importance: high
---

# NASA / Teverovsky — Cracking Problems in Low-Voltage Chip Ceramic Capacitors

**Source:** `resources/literature/nasa-cracking-low-voltage-mlcc.md` (PDF: `resources/literature/pdf/nasa-cracking-low-voltage-mlcc.pdf`, 3 900 lines)
**Author:** Alexander Teverovsky, ASRC Federal Space and Defense, NASA Goddard
**Year:** 2018
**Type:** NEPP Task Report — a near-encyclopedic survey

## Summary

A 200+-page NEPP report covering the entire MLCC technology stack from the **cracking-and-reliability** lens. The companion piece to [[donhang-liu]]'s reliability framework — where Liu focuses on intrinsic IR degradation, Teverovsky focuses on **mechanical** failure paths. Useful even outside the cracking topic for its broad, systematic survey style.

## What it covers (TOC at a glance)

1. Manufacturing processes & types of MLCCs — including detailed materials sections on **dielectric, electrode, and termination materials**, plus design topics (flexible terminations, laser marking).
2. Testing & QA — comparative analysis across MIL-PRF-123, NASA/GSFC specs, ESA / JAXA, automotive (AEC-Q200) qualification procedures.
3. Characteristics of MLCCs — rated voltage, capacitance and DF, **insulation resistance and leakage** (specified IR, absorption, intrinsic leakage, effect of cracking on IR), breakdown voltage, mechanical characteristics (flexural strength, Vickers hardness, indentation fracture toughness).
4. **Failure mechanisms in MLCCs with cracks** — degradation in moisture (both PME and BME), degradation in dry environments.
5. Special cases — **hydrogen-related cracking** (a unique BME issue), pick-and-place damage, electro-mechanical resonance.
6. Revealing cracks — optical (vicinal illumination, delamination by discoloration), electrical measurements.
7. Screening & qualification recommendations.

## Useful as
- A go-to reference for any MLCC mechanical / cracking question.
- An overview of **non-AEC-Q200** qualification frameworks (NASA GSFC EEE-INST-002, ESA ECSS, JAXA, MIL-PRF-49467 for high reliability).
- Documentation that hydrogen-related cracking is a real BME-specific phenomenon (Pd hydrogen-absorption in older PME could cause cracks; analogous mechanisms in BME flexible-termination layers).

## Concepts discussed
- [[failure-modes-mlcc]]
- [[bme-vs-pme]]
- [[mlcc-manufacturing-process]]
- [[termination-and-plating]]
- [[oxygen-vacancy-migration]]

## Entities mentioned
- [[nasa-nepp]]
- [[aec-council]]
- [[donhang-liu]]
- [[murata]], [[tdk]], [[samsung-electro-mechanics]] (manufacturer survey)

## References
_Original source: `resources/literature/nasa-cracking-low-voltage-mlcc.md`_
