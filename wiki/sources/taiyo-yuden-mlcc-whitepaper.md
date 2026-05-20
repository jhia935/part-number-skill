---
title: "Taiyo Yuden — Advances in Material Technology Enable Game-Changing MLCC Performance (Whitepaper)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/market/taiyo-yuden-mlcc-whitepaper.md
tags:
  - paper
status: complete
importance: high
---

# Taiyo Yuden — Advances in Material Technology Enable Game-Changing MLCC Performance

**Source:** `resources/market/taiyo-yuden-mlcc-whitepaper.md` (PDF: `resources/market/pdf/taiyo-yuden-mlcc-whitepaper.pdf`)
**Publisher:** [[taiyo-yuden]]
**Type:** Vendor technical whitepaper (mid-2010s, mass-production milestones)

## Summary

Taiyo Yuden's positioning paper for **high-value MLCCs (100–470 µF) as polymer-capacitor replacements**. Documents the company's manufacturing roadmap: 330 µF MLCC commercialized 2013, 470 µF in 2014, 1000 µF target 2016. Demonstrated **MTTF 10 000 to >1 000 000 years** for the high-value products (consistent with [[bme-reliability-model|Liu's framework]] applied to well-engineered BME). The dense-case + low-ESR/ESL combination beats polymer capacitors on every electrical metric except cost-at-very-low-cap.

## Key quantitative anchors

### Product capability ceiling (mass production, as of paper)
- 470 µF in EIA 1812 case — using **1200+ layers**
- 100 µF achievable in 0805
- 220 µF in 1206
- 1000 µF target (2016 roadmap)

### Reliability claim
**Demonstrated MTTF: 10 000 to over 1 000 000 years** for high-value MLCCs (manufactured by Taiyo Yuden's process). Compare to polymer capacitor field-failure rates of 0.1–1 %/1000 h typical (MTTF ~ 100 000 h ≈ 11 years).

### ESR / ESL advantage over polymer
- 100 / 220 / 330 µF Taiyo Yuden MLCCs have **lower ESR and ESL** than 330 µF polymer, in a smaller case.
- εr stability over frequency: 4 MLCCs varied **only 8–12 %** from 100 Hz to 100 MHz, vs 18–80 % for 6 polymer devices.

### Process technology
Sub-µm dielectric thickness — "regions less than one-micron thick" — confirmed for production. Built around:
- Super-fine BaTiO₃ powder
- [[core-shell-batio3|Core-shell structure]]
- Thin-layer technology
- Printing technology
- Multilayer assembly
- Simulation technology

### Acoustic noise suppression
TY commercializes a proprietary [[batio3|BaTiO₃]]-based dielectric specifically engineered to **suppress piezoelectric "singing"** at high AC drive — the audible defect in standard high-CV X5R / X7R parts. Slight DC-bias-derating tradeoff in exchange.

### Soft termination
TY soft-termination variants provide **heat-cycle resistance and substrate-bending resistance** (analogous to [[kemet-arcshield|KEMET ArcShield]] flex termination and [[tdk-cga-series|TDK CGA soft-termination]]).

## Taiyo Yuden product family naming

| Prefix | Typical V_r | Use |
|---|---|---|
| **AMK** | 4 V | high-cap consumer |
| **JMK** | 6.3 V | high-cap consumer / industrial |
| **LMK** | 10 V | bulk decoupling |
| **PMK** | 2.5 V | sub-V supply rails |
| **GMK** | 25 V | mid-voltage automotive |
| **EMK** | 10 V | high-cap industrial |
| **TMK** | 50 V | industrial |
| **HMK** | 100 V+ | high-voltage |

Plus suffix `HT` for AEC-Q200 automotive grade (e.g., AMK316ABJ107MLHT = 100 µF / 4 V / 1206 / X5R / AEC-Q200).

## High-value product specs (Table 1 selected)
| Capacitance | Case | V_r | Class | Part Number |
|---|---|---|---|---|
| 100 µF | 0805 | 2.5 V | X5R | PMK212BBJ107MG-T |
| 100 µF | 1206 | 4 V | X5R | AMK316ABJ107ML-T |
| 100 µF | 1206 | 4 V | X6S | AMK316AC6107ML-T |
| 100 µF | 1210 | 10 V | X5R | LMK325ABJ107MM-T |
| 220 µF | 1210 | 6.3 V | X5R | JMK325ABJ227MM-T |
| 330 µF | 1210 | 4 V | X5R | AMK325ABJ337MM-T |
| **470 µF** | **1812** | **4 V** | X5R | AMK432ABJ477MM-T |

## Concepts discussed
- [[batio3]]
- [[core-shell-batio3]]
- [[termination-and-plating]]
- [[esr-esl-srf]]
- [[bme-reliability-model]]
- [[failure-modes-mlcc]] — soft termination
- [[x5r-dielectric]]
- [[dielectric-class-comparison]]

## Entities mentioned
- [[taiyo-yuden]] — author / vendor

## References
_Original source: `resources/market/taiyo-yuden-mlcc-whitepaper.md`_
