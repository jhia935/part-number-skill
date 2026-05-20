---
title: "AEC-Q104 Rev A — Failure Mechanism Based Stress Tests for Multichip Modules (Nov 2025)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/design-rules/aec-q104-rev-a-2025.md
tags:
  - paper
status: complete
importance: medium
---

# AEC-Q104 Rev A — Multichip Module Qualification

**Source:** `resources/design-rules/aec-q104-rev-a-2025.md` (PDF: `resources/design-rules/pdf/aec-q104-rev-a-2025.pdf`)
**Publisher:** Automotive Electronics Council ([[aec-council]])
**Date:** Rev A, November 28, 2025

## Summary

The AEC qualification standard for **multichip modules (MCMs)** in automotive electronics — i.e., packages containing multiple electronic components (ICs + passives + sensors + etc.) inside a single enclosure designed to be soldered directly to a PCB. Companion document to [[aec-q200-rev-e-2023|AEC-Q200]] (passive components) and AEC-Q100 (ICs). Relevant to the MLCC space when capacitors are integrated **inside** a power-stage module, sensor fusion package, or system-in-package (SiP) device rather than discrete on the PCB.

## Scope

AEC-Q104 applies to MCMs designed for **direct PCB soldering**. Out of scope:
- Two-or-more-assembly-component "modules" assembled by Tier-1 OEM (treated as separate components)
- Discrete optoelectronic devices (those are covered by AEC-Q102)
- MEMS devices included **as a separate part** (those are AEC-Q103)

But: Optoelectronic and MEMS devices that are **embedded inside** a larger MCM are covered by Q104.

For MLCC engineers: Q104 governs **automotive power modules with integrated decoupling caps**, **integrated voltage regulators with built-in input/output caps**, **smart sensor packages with onboard MLCCs**, etc.

## Key differences from AEC-Q200 (passive single component)

| Aspect | AEC-Q200 (passives) | AEC-Q104 (MCM) |
|---|---|---|
| Sample size per lot | 77 pieces × 3 lots | **30 pieces × 3 lots** (reduced due to MCM cost) |
| Testing categories | A through G (passive types) | A through G **plus H** (MCM-specific) |
| ESD HBM minimum | per Q200 acceptance | down to **1 kV** (from 2 kV in Q100) |
| ESD CDM | per Q100 (750 V corner / 500 V rest) | **500 V on all pins** regardless of position |
| Thermal shock | passive component test | thermal shock + **VISM** (Visual Inspection for Migration) |
| Operating life | rated V at T_max, 1000 h | also rated V at T_max but **with MCM-specific endurance** |

## MCM-specific tests added

The "H" category in Rev A includes:
- **Thermal Shock Migration**: visual inspection for ion migration / dendrite formation after thermal cycling at humidity
- **MCM-level Electrical Characterization**: full-system measurement, not just per-component
- **MCM Early Life Failure Rate (ELFR)** appendix: framework for predicting and bounding the early-life-failure tail of MCMs (relevant because MCMs have many serial failure modes)

## Implications for MLCC embedded in modules

When an MLCC is qualified at component level (AEC-Q200), it's tested as a free-standing chip. When that same MLCC is **embedded in an MCM** (e.g., as a sensor-fusion module's decoupling cap), the MCM as a whole must additionally pass AEC-Q104:
1. MLCC's individual reliability number propagates into MCM reliability via series-product (`R_MCM = R_MLCC × R_other_components × …`).
2. Thermal-shock and humidity tests at MCM level apply different ΔT profiles than at component level (because the MCM thermal mass changes the rate).
3. Visual inspection requirements at MCM level are stricter; surface flaws on the encapsulant that wouldn't matter for a discrete cap can fail VISM.

## For the simulator

Most MLCC simulators target discrete-component analysis. AEC-Q104 mostly affects the simulator at two boundaries:
1. **Output**: simulator should flag "this part is integrated inside an MCM → MCM-level qualification (Q104) applies in addition to Q200."
2. **Input**: when simulating power modules / SiPs, the simulator should accept Q104-qualified-part inputs even if the cap is technically a Q200-qualified MLCC.

## Concepts discussed
- [[aec-q200-rev-e-2023]]
- [[failure-modes-mlcc]]
- [[bme-reliability-model]]
- [[weibull-distribution]]

## Entities mentioned
- [[aec-council]]

## References
_Original source: `resources/design-rules/aec-q104-rev-a-2025.md`_
