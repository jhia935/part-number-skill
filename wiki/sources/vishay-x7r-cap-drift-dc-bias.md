---
title: "Vishay — Time-Dependent Capacitance Drift of X7R MLCCs Under Constant DC Bias"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/vishay-x7r-cap-drift-dc-bias.md
tags:
  - paper
status: complete
importance: high
---

# Vishay — Time-Dependent Capacitance Drift of X7R MLCCs Under Constant DC Bias

**Source:** `resources/design-rules/vishay-x7r-cap-drift-dc-bias.md` (PDF: `resources/design-rules/pdf/vishay-x7r-cap-drift-dc-bias.pdf`)
**Authors:** Paul Coppens, Eli Bershadsky, John Rogers, Brian Ward ([[vishay]])
**Date:** Revision Dec 14, 2021 — Document Number 45263

## Summary

A white paper documenting the **DC-bias-accelerated aging** phenomenon: that prolonged exposure to a DC bias voltage produces capacitance drift over time that is much larger than the well-known VCC effect plus normal log-decade aging combined. Tests were on 0603 X7R 100 nF, 50 V MLCCs from Vishay and three competitors at 40 % (20 V_dc, 2.5 V/µm) and 100 % (50 V_dc, 6 V/µm) rated voltage for 1000 hours. Competing parts lost more than **20 % over the 1000-h test** at 40 % rated and proceeded faster at 100 % rated, **far exceeding** the 1–2 %/decade normal aging rate (some near 10 %/decade). Vishay's part remained ~5 % drift only at 40 % rated, but lost its advantage by 1000 h at 100 % rated. Recovery after bias removal was much faster for Vishay; competitors took 50–1000 h to recover to 95 % at room temperature. **All parts** recovered fully at 150 °C × 1 h thermal de-aging.

## Key points / numerical data

- Capacitance formula reproduced: `C = n·A·ε₀·K / t` (n = layer count, A = overlap, t = thickness).
- Typical Class 2 VCC plot (Fig. 2): −10 % at 2 V/µm, −25 % at 4 V/µm, −45 % at 6 V/µm, −60 % at 10 V/µm, −80 % at 20 V/µm.
- Logarithmic natural aging: `C(t) = C₀(1 − (A/100)·log₁₀(t))`, A ≈ 1–2 %/decade for X7R.
- Vendor benchmark: Vishay 0603 X7R 100 nF 50 V vs three competitors. After 1000 h at 40 % V_rated: Vishay ~5 % drift, competitors 20–30 %.
- Vishay attributes its advantage to noble-metal (PME) construction, vs competitors' BME — opens the question of BME-specific oxygen-vacancy migration as the DC-bias-aging mechanism.
- Hysteresis loop physics, domain re-orientation aging, Curie temperature ~125 °C.

## Cited references useful for follow-up

- Hahn et al., "Effects of MgO Doping on DC Bias Aging Behavior of Mn-Doped BaTiO3", *JJAP* 47:7 (2008), pp. 5526–5529.
- Tsurumi et al., "Mechanism of Capacitance Aging Under DC Bias Field in X7R-MLCCs", *J. Electroceram.* 21:17–21 (2008).
- Genenko et al., "Mechanisms of Aging and Fatigue in Ferroelectrics", *Elsevier MSE B*.

## Entities mentioned
- [[vishay]] — author, advocates PME for DC-bias robustness

## Concepts discussed
- [[dc-bias-derating]]
- [[dc-bias-aging]] — the central phenomenon
- [[aging-class-2]] — distinguished from DC-bias aging
- [[bme-vs-pme]]
- [[batio3]]

## References
_Original source: `resources/design-rules/vishay-x7r-cap-drift-dc-bias.md`_
