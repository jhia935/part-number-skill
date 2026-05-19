---
title: "ROHM — Multi-layer Ceramic Capacitor Used in Buck Converter Circuit (App Note 62AN089E)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/rohm-ceramic-cap-app-note.md
tags:
  - paper
status: complete
importance: medium
---

# ROHM — MLCC Used in Buck Converter (App Note 62AN089E)

**Source:** `resources/design-rules/rohm-ceramic-cap-app-note.md` (PDF: `resources/design-rules/pdf/rohm-ceramic-cap-app-note.pdf`)
**Publisher:** [[rohm]] Co., Ltd., No. 62AN089E Rev.002, January 2020 (© 2013, 2020)
**Audience:** Power supply designers using ROHM switching regulators

## Summary

A practitioner-grade app note from a power-IC vendor describing how MLCC choice affects buck-converter stability. The valuable content is **three concrete DC-voltage characteristic comparisons** — case-size, thickness, and rated-voltage swept independently — using Murata's published SimSurfing data.

## Quantitative DC-bias data points (10 µF / B-char [≈X7R] MLCCs)

**Size sweep (same 0.95 mm thickness, 10 V rated):**
| EIA | Drop at 10 V_dc |
|---|---|
| 1608 (0603) | ~ −85 % |
| 2012 (0805) | ~ −55 % |
| 3216 (1206) | ~ −65 % |

(0805 wins over 1206 — counter to "bigger is always better", because both have the same `T = 0.95 mm` so the dominant effect is layer-thinning to hit higher cap density in the 1206 part.)

**Thickness sweep (same 3216 case, 10 V rated):**
| T (mm) | Drop at 10 V_dc |
|---|---|
| 0.95 | ~ −65 % |
| 1.25 | ~ −30 % |
| 2.70 | ~ −12 % |

**Rated-voltage sweep (same 3216, 1.80 mm thick, 10 µF):**
- 16 V part at 16 V: ~ −55 %
- 50 V part at 50 V: ~ −85 %

Confirms field, not voltage, as the dominant variable.

## Chronological aging plot (Fig. 6)
- B-char: ~ −12 % over 10 → 100 000 h
- F-char: ~ −30 % over same range

## Other content
- Standardized dielectric class table covering JIS B/R + EIA X5R/X5S/X5T/X6S/X6T/X7R/X7S/X7T/X7U/X8R/Y5V/Z5U/Z5V — explicit tolerance brackets confirming the [[eia-rs-198-dielectric-classes]] table.
- BaTiO₃ εr stated as 1000–20 000; CaZrO₃/TiO₂ paraelectric εr 20–300.
- Ripple current self-heating chart for 10 µF / 10 V / B / 3216: temperature rises < 10 °C up to 1 A_rms; ~100 °C at 6 A_rms.
- Stability warning: MLCC's very low ESR can over-rotate phase in older switching regulator feedback designs; ≥ 10 mΩ series resistor recommended when designing in legacy controllers.

## Concepts discussed
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[esr-esl-srf]]
- [[case-size-geometry]]

## Entities mentioned
- [[rohm]]
- [[murata]] (SimSurfing tool referenced)

## References
_Original source: `resources/design-rules/rohm-ceramic-cap-app-note.md`_
