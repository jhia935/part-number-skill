---
title: "Novak et al. — DC and AC Bias Dependence of Capacitors Including Temperature Dependence (DesignCon 2011)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/electrical-integrity-dce11-200.md
tags:
  - paper
status: complete
importance: high
---

# Novak et al. — DC and AC Bias Dependence of Capacitors (DesignCon East 2011)

**Source:** `resources/design-rules/electrical-integrity-dce11-200.md` (PDF: `resources/design-rules/pdf/electrical-integrity-dce11-200.pdf`)
**Authors:** Istvan Novak, Kendrick Barry Williams, Jason R. Miller, Gustavo Blando, Nathaniel Shannon — Oracle-America Inc.
**Venue:** DesignCon East 2011

## Summary

A landmark **measurement** study of DC and AC bias dependence in modern Class II MLCCs. Tests 1 µF / 0603 / 16 V parts from five vendors at 100 Hz with 10 mVrms and 500 mVrms AC bias, DC swept −20 V to +20 V in 0.2 V increments with 100 s settling. Conclusions overturn three pieces of conventional wisdom:

1. **X7R is not always better than X5R** under DC bias. Vendor-F's X7R was worse than its X5R; Vendor-B showed no measurable difference.
2. **Vendor-published data is often optimistic**: Vendors A and F under-predict the measured capacitance loss; B and C agreed well with their published curves.
3. **Thinner-package parts are dramatically worse**: Vendor-C's 0.5 mm tall 1 µF X5R 0603 16 V dropped −85 % at 16 V vs −40 % for the 0.8 mm tall X5R and −25 % for the 0.8 mm tall X7R from the same vendor. The lesson: a "drop-in replacement" with same footprint but lower height is **not** electrically interchangeable.

Adds temperature-dependence sweeps (−5, +20, +45, +70 °C) showing DC-bias sensitivity does shift with temperature; AC-bias sensitivity surface plots showing capacitance becomes more linear when DC bias is far from zero; and time-dependent settling on log scale showing −2.8 %/decade (best) to −13.8 %/decade (worst) tail drift even after the immediate VCC step.

## Key quantitative anchors for the simulator

- Same nominal 1 µF 0603 16 V part — vendor spread at −20 V DC: from **0 % to −80 %** capacitance loss across 8 part numbers from 5 vendors.
- Three Vendor-C variants of 1 µF 0603 16 V at +16 V:
  - X7R 0.8 mm: −25 %
  - X5R 0.8 mm: −40 %
  - X5R 0.5 mm: −85 %
- Time-dependent **slow tail** under DC bias (after the immediate VCC step):
  - 47 µF 1206 6.3 V X5R: −2.78 %/log(s) at worst-case bias
  - 4.7 µF 0805 16 V X7R: −13.79 %/log(s) at worst-case bias
- AC-bias dependence is largest at zero DC bias and minimal near rated DC bias.

## Concepts discussed
- [[dc-bias-derating]]
- [[dc-bias-aging]]
- [[aging-class-2]]
- [[case-size-geometry]]

## Entities mentioned
- Oracle Corporation (then Oracle-America Inc., succeeding Sun Microsystems)

## References
_Original source: `resources/design-rules/electrical-integrity-dce11-200.md`_
