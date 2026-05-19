---
title: KEMET ArcShield MLCC Technology
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - kemet-mlcc-design-and-characteristics.md
tags:
  - series
status: complete
importance: medium
---

# KEMET ArcShield MLCC Technology

A patented [[kemet]] internal-electrode design for high-voltage MLCCs that **adds a shield electrode in the same monolithic body** to redistribute the surface electric field, preventing the three high-voltage failure paths simultaneously:

1. Arcing between the termination and the first internal electrode of opposite polarity.
2. Arcing between the two opposite-polarity terminations along the chip surface.
3. Internal dielectric breakdown.

## Key claims
- Built-in protection — no external surface coating needed (and therefore no risk of coating damage / air gaps that compromise creepage coatings).
- Higher breakdown voltage capability than equally-rated coated parts.
- Maximizes available capacitance in a given case size vs the serial-electrode alternative (which sacrifices `1/N` of capacitance by splitting the chip into N in-series sub-caps).

## Specs (as published)
- 500, 630, and 1000 V_dc
- 0603 to 2225 case sizes
- 1.0 nF – 560 nF
- BME X7R dielectric, flexible termination optional

## Physics (vs standard)
Standard high-V MLCCs need either:
- a surface conformal coating (fragile, ages, can leak); or
- a serial design (effective `C = C_unit / N`, large size penalty).

ArcShield's shield electrodes create a longer effective field path between opposite-polarity surface terminations **without** breaking up the electrode stack, retaining most of the capacitance.

## See also
- [[kemet]]
- [[failure-modes-mlcc]] (surface arcing section)
- [[kemet-mlcc-design-and-characteristics]]
