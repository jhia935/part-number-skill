---
title: "KEMET — Multilayer Ceramic Capacitors (MLCCs): Design and Characteristics"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/kemet-mlcc-design-and-characteristics.md
tags:
  - paper
status: complete
importance: high
---

# KEMET — Multilayer Ceramic Capacitors (MLCCs): Design and Characteristics

**Source:** `resources/design-rules/kemet-mlcc-design-and-characteristics.md` (PDF: `resources/design-rules/pdf/kemet-mlcc-design-and-characteristics.pdf`)
**Publisher:** [[kemet]] / PSMA presentation slide deck, © 2019
**Type:** Industry training / educational

## Summary

A vendor-authored tutorial covering MLCC construction, the capacitance equation `C = K·ε₀·N·A/d` with the (n−1) edge correction, common failure modes (mechanical, thermal-shock, flex crack), surface arcing physics, and four levels of flex-crack mitigation. The latter half details KEMET's proprietary [[kemet-arcshield]] design for high-voltage X7R parts (500/630/1000 V_dc, 0603–2225, 1 nF–560 nF). Treats geometry-driven solutions (open-mode, floating electrode, serial / cascade electrode, flexible termination) and explains the field-redistribution effect of shield electrodes.

## Key points

- Stamp-equation for the capacitance, with `n−1` instead of `n`.
- Three crack root causes: mechanical impact, thermal shock (parallel-plate cracks), flex stress (>0805 case sizes most susceptible).
- Capacitor parallel: `C_T = C_1 + C_2 + ... + C_N`.
- Serial / cascade electrode for HV: effective `C` = `C_unit / N` but each sub-cap sees `V/N`.
- ArcShield = "shield electrode" in the same monolithic body that redistributes field, allowing higher V_breakdown without external coating.
- Flexible termination + open-mode together = level-3 mitigation, fail-open at up to 5 mm board flex.

## Entities mentioned
- [[kemet]] — author, vendor
- [[kemet-arcshield]] — proprietary HV MLCC technology

## Concepts discussed
- [[mlcc-capacitance-equation]]
- [[failure-modes-mlcc]]
- [[bme-vs-pme]]

## References
_Original source: `resources/design-rules/kemet-mlcc-design-and-characteristics.md`_
