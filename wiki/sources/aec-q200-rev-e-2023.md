---
title: "AEC-Q200 Rev E — Stress Test Qualification for Passive Electrical Components"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/aec-q200-rev-e-2023.md
tags:
  - paper
status: complete
importance: high
---

# AEC-Q200 Rev E — Stress Test Qualification for Passive Electrical Components

**Source:** `resources/design-rules/aec-q200-rev-e-2023.md` (PDF: `resources/design-rules/pdf/aec-q200-rev-e-2023.pdf`)
**Publisher:** Automotive Electronics Council ([[aec-council]])
**Date:** Rev E, March 20 2023 — supersedes Rev D (June 2010)
**License:** Free download; AEC retains copyright; reprintable with notice.

## Summary

The de-facto industry qualification standard for any passive component used in automotive applications. AEC-Q200 defines, per component family, the **stress sequence**, test conditions, and parametric acceptance criteria a part must pass before it can be marketed as automotive-grade. For ceramic capacitors specifically, Table 2 enumerates 14 stresses (temperature cycling, humidity bias, operating life, mechanical shock, vibration, board flex, terminal strength, ESD, etc.), each with explicit MIL-STD or JESD reference test method and **additional requirements** that tighten the underlying spec. Acceptance criteria for Class I (Table 2B-1) and Class II/III (Table 2B-2) parts are specified per measured parameter (capacitance, Q or DF, IR).

## Key conditions for ceramic capacitors (Table 2)

| Test | Standard | Key parameters |
|---|---|---|
| Temperature cycling | JESD22-A104 | 1000 cycles, −55 °C to T_max (≤+125 °C), 15 min dwell, 1 min transition |
| Humidity bias | MIL-STD-202 Method 103 | 1000 h, **85 °C / 85 % RH**, rated V + 1.3–1.5 V offset (100 kΩ resistor) |
| High-temp operating life | MIL-STD-202 Method 108 | 1000 h, **rated voltage**, T_max ≤ +150 °C |
| Mechanical shock | MIL-STD-202 Method 213 | Condition C, SMD |
| Vibration | MIL-STD-202 Method 204 | 5 g, 10 Hz–2000 Hz, 20 min × 12 cycles × 3 axes |
| Resistance to soldering heat | MIL-STD-202 Method 210 | SMD Condition K, ≥217 °C for 60–150 s |
| Withstanding voltage | (in Table 2B) | **250 % rated voltage** at 25 °C |
| Board flex | AEC-Q200-005 | (separate spec document) |
| Terminal strength SMD | AEC-Q200-006 | (separate spec document) |
| ESD | AEC-Q200-002 | (separate spec document) |

## Notably different from older revisions
- **Operating life uses rated voltage** for ceramics (not 2× rated as for tantalum/polymer in Table 1). The ceramic spec is deliberately conservative on voltage acceleration because of Class II DC-bias-aging risk.
- Rev E added Jump Start Endurance and Load Dump Endurance (Tests 35–36) for fuses; ceramic table unchanged in conditions but acceptance-criteria tables 2B-1 / 2B-2 fully restructured.

## Implications for the simulator
- AEC-Q200 grade doesn't change the **equations** in the simulator — it constrains the **margin**. A part passing Q200 endurance at rated V + T_max is implicitly OK for ≥10 yr at 80 % V_rated / (T_max − 20 °C) (Murata's published rule of thumb).
- Acceptance criterion `ΔC ≤ ±x %` over 1000 h endurance is what the supplier guarantees — typical X7R automotive limits are ±15 % over the test for Class II.

## Concepts discussed
- [[dc-bias-aging]]
- [[aging-class-2]]
- [[failure-modes-mlcc]]
- [[bme-reliability-model]]

## Entities mentioned
- [[aec-council]] — Automotive Electronics Council, publisher
- [[murata]] — co-author affiliation (Christian Merkel, Alex Yanez)
- [[tdk]] — co-author affiliations
- [[vishay]] — co-author affiliations
- [[yageo]] — co-author affiliations (LeAnna Weakley, Alfred Chen)

## References
_Original source: `resources/design-rules/aec-q200-rev-e-2023.md`_
