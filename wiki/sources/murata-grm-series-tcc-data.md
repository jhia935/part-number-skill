---
title: "Murata — GRM Series Data Sheet (TCC, DC Bias, AC Bias, Aging, Impedance, Allowables)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/market/murata-grm-series-tcc-data.md
tags:
  - paper
status: complete
importance: medium
---

# Murata — GRM Series Data Sheet (Reference Curves)

**Source:** `resources/market/murata-grm-series-tcc-data.md` (PDF: `resources/market/pdf/murata-grm-series-tcc-data.pdf`)
**Publisher:** [[murata]]
**Type:** Reference graph compilation accompanying the [[murata-grm-series]] catalog

## Summary

A compact (2-page) reference card with the canonical [[murata-grm-series]] curves:
- Capacitance vs temperature: C0G (P2H/R2H/S2H/T2H/U2J) all within ±10 % across −60…+125 °C; X5R 50 V near-flat; Y5V 50 V cliff to −80 % at +85 °C and reaches lower at −40 °C.
- Impedance vs frequency: standard SRF rolloff for 1 pF through 1 µF (GRM21).
- Capacitance vs DC voltage: C0G 50 V flat; X7R 50 V drops to ~−50 % near 50 V_dc; Y5V 50 V drops to nearly −90 %.
- Capacitance vs AC voltage: X7R, Y5V rise (Y5V up to +14 %, X7R up to ~+6 %) with increasing V_rms; C0G flat.
- Aging: C0G ~0 %; X7R drops ~−10 % by 10 000 h; Y5V drops ~−30 %.
- Allowable apparent power, voltage, and current vs frequency, parametrized by capacitor case/value family (GRM55, GRM43, GRM31, GRM21, GRM18, etc.).

The actual numerical scales are partially graphical and not directly digitizable from the PDF-extracted text, but the **qualitative envelopes** are clear and match the consensus in [[psma-ceramic-capacitor-basics]] and [[vishay-x7r-cap-drift-dc-bias]].

## Implications for the simulator

- Provides vendor-disclosed reference curves to ground the heuristic `f_VCC(E)`, `f_age(t)`, `f_T(T)` fits.
- GRM family naming scheme: GRM18 = 0603, GRM21 = 0805, GRM31 = 1206/1210, GRM43 = 1812, GRM55 = 2220 (roughly).
- Murata's published "allowable apparent power" curves are the practical limits for AC bias / power applications.

## Concepts discussed
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[esr-esl-srf]]

## Entities mentioned
- [[murata]]
- [[murata-grm-series]]

## References
_Original source: `resources/market/murata-grm-series-tcc-data.md`_
