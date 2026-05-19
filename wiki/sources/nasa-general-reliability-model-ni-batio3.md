---
title: "NASA / Liu — A General Reliability Model for Ni-BaTiO₃ MLCCs (CARTS 2014)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-general-reliability-model-ni-batio3.md
tags:
  - paper
status: complete
importance: high
---

# NASA / Liu — A General Reliability Model for Ni-BaTiO₃ MLCCs (CARTS 2014)

**Source:** `resources/literature/nasa-general-reliability-model-ni-batio3.md` (PDF: `resources/literature/pdf/nasa-general-reliability-model-ni-batio3.pdf`)
**Author:** Donhang (David) Liu ([[donhang-liu]]), AS and D Inc., for NASA Goddard
**Venue:** CARTS, Santa Clara CA, April 1–3 2014

## Summary

A consolidation paper that re-presents the three-factor reliability framework from [[nasa-nepp-bme-mlcc-reliability]] and [[nasa-batio3-mlcc-failure-mechanisms]] in a single, unified form, with one critical new addition: **direct quantitative evidence for the breakdown of single-mode Prokopowicz-Vaskas** on BME parts.

Table V reports the single-mode P-V fit to a specific sample (C08X47516, an 0805 X7 47nF):
- Fitted **n = 4.524** (the voltage acceleration exponent)
- Fitted **E_a = 2.60 eV** (the activation energy)
- Predicted MTTF @ 135 °C / 72 V: **2111 hours**
- Actually measured MTTF: **318 hours** — **6.6× shorter** than P-V predicts

Liu uses this as the empirical justification for the two-mode (catastrophic + slow degradation) acceleration model: when individual TTF data are separated by failure mode (using leakage-current curves to classify catastrophic vs slow), each subset fits its own acceleration function — catastrophic to a power law, slow degradation to an exponential — and the combined model reproduces the measured lifetime.

## Quantitative anchors for the simulator

| Parameter | Value | Source |
|---|---|---|
| BME single-mode P-V `n` | 4.524 (one sample, but consistent with 2.5–6 lit range) | Liu 2014 Table V |
| BME P-V activation energy `E_a` | 2.60 eV (this sample) | Liu 2014 Table V |
| Discrepancy: P-V prediction vs measurement | **6.6× over-prediction** at 135 °C / 72 V | Liu 2014 |
| α (structural exponent) | 6 for V ≤ 50 V, 5 for V > 50 V | Liu 2014 Eq. 11 (= same as 2013) |
| Commercial BME typical N | > 250 layers | Liu 2014 |

This is the **closest answer we have for the simulator's open gap on BME catastrophic `n`**: ~3 for PME, ~4.5 for BME single-mode fits, **but use the two-mode model** if you actually care about predicted lifetime.

## Cross-reference notes
The N-amplifier 5-year reliability table (Ri vs N) is reproduced verbatim here from [[nasa-batio3-mlcc-failure-mechanisms]]. Equations (5)–(12) are the same as in [[nasa-nepp-bme-mlcc-reliability]].

## Concepts discussed
- [[bme-reliability-model]]
- [[mlcc-capacitance-equation]]
- [[bme-vs-pme]]
- [[core-shell-batio3]]

## Entities mentioned
- [[donhang-liu]]
- [[nasa-nepp]]

## References
_Original source: `resources/literature/nasa-general-reliability-model-ni-batio3.md`_
