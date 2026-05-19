---
title: "EPCI / Zednicek — High CV MLCC DC/AC Bias Aging Capacitance Loss Explained (PCNS 2019)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/epci-high-cv-mlcc-bias-aging.md
tags:
  - paper
status: complete
importance: high
---

# EPCI / Zednicek — High CV MLCC DC/AC Bias Aging Capacitance Loss Explained

**Source:** `resources/design-rules/epci-high-cv-mlcc-bias-aging.md` (PDF: `resources/design-rules/pdf/epci-high-cv-mlcc-bias-aging.pdf`)
**Author:** Tomas Zednicek, Ph.D., President of EPCI (European Passive Components Institute)
**Venue:** Updated September 2019 based on the 2nd PCNS Passive Components Networking Symposium hot panel
**Co-panelists referenced:** AVX, KEMET, [[murata]] Europe, [[samsung-electro-mechanics]], Wuerth Elektronik, Continental Automotive

## Summary

A practitioner-oriented synthesis paper that **packages the field's empirical knowledge** about MLCC Class II capacitance loss into a single multiplicative formula for design engineers:

$$
C_\text{actual} \;=\; C_\text{rated} \cdot F_\text{DCV} \cdot F_\text{ACV} \cdot F_\text{temp} \cdot F_\text{aging}
$$

Worked example: X5R 0805 10 µF / 6.3 V at 5 V coupling app gives
`C_actual = 10 µF · 0.4 · 0.85 · 0.9 · 0.95 = 2.9 µF`.

Equally important, Zednicek shows that the **worst-case across vendors can drive the same nominal part as low as 10 % of nameplate**. The conclusions formed the basis of an open letter to the AEC-Q200 committee about Class II DC/AC bias aging.

## Key data points

- **10 µF / 6.3 V / X7R / 0805 across three vendors**: −35 % to −65 % at rated V; −12 % to −32 % at 3.3 V (derated).
- **Case size effect on 10 µF / 6.3 V / X5R**: 0805 vs 0603 at full DC bias — the 0603 is worse because of thinner dielectric.
- **X5R vs X7R on 1 µF / 6.3 V / 0402**: X5R falls ~−70 % at 6.3 V; X7R only ~−40 %.
- **AC bias effect at 10 mVrms (vs 1 Vrms reference)**: additional −5 to −15 %.
- Reference time for capacitance: 48 h or 1000 h after last heat (different vendors); 24 h is the MIL spec.

## Cross-references the multiplicative-factor formula
This paper is the explicit articulation of the multiplication that the simulator implements as `f_VCC · f_AC · f_T · f_age` in §3 of `simulator-model.md`.

## Concepts discussed
- [[dc-bias-derating]]
- [[dc-bias-aging]]
- [[aging-class-2]]
- [[esr-esl-srf]] (briefly, on paralleled cap impedance)

## Entities mentioned
- [[murata]]
- [[samsung-electro-mechanics]]
- [[kemet]]
- AVX (now [[kyocera-avx]])
- Wuerth Elektronik
- Continental Automotive — automotive OEM end-user voice

## References
_Original source: `resources/design-rules/epci-high-cv-mlcc-bias-aging.md`_
