---
title: "KYOCERA AVX — The Effects of ESR and ESL in Digital Decoupling Applications"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/design-rules/kyocera-avx-esr-esl-decoupling.md
tags:
  - paper
status: complete
importance: medium
---

# KYOCERA AVX — The Effects of ESR and ESL in Digital Decoupling

**Source:** `resources/design-rules/kyocera-avx-esr-esl-decoupling.md` (PDF: `resources/design-rules/pdf/kyocera-avx-esr-esl-decoupling.pdf`)
**Author:** Jeffrey Cain, Ph.D. ([[kyocera-avx]])
**Venue:** CARTS 1997 — 17th Capacitor and Resistor Technology Symposium

## Summary

A classic SPICE-driven study of how ESR and ESL of decoupling MLCCs affect ripple voltage seen at an IC switching node. Uses a simplified model: PCB power/ground plane via inductance ~400 pH, cap-to-IC trace ~1 nH, IC modeled as a current sink with adjustable slew rate (0.5, 1, 2 A/ns) and frequency (25/50/100 MHz). Demonstrates the breakdown of the naive `C = I·Δt/ΔV` rule when parasitics dominate; gives the equivalent-impedance formula `Z = √(ESR² + (ωL − 1/ωC)²)`; and concludes with the rule of thumb `1/(ESR·C) ≳ f_op`.

## Key points

- Equivalent-circuit impedance equation (Eq. 1).
- Capacitance sizing for decoupling: `C = I·Δt/ΔV` ideal-case only; reality is dominated by trace L and cap ESR.
- ESR effect: higher ESR → larger ripple at constant `C`. Increasing `C` doesn't reduce ripple once ESR dominates.
- ESL effect: higher ESL → larger ripple, especially on fast (high-di/dt) edges.
- Practical via inductance: ~400 pH; trace-to-IC inductance: ~1 nH.

## Concepts discussed
- [[esr-esl-srf]]
- [[mlcc-capacitance-equation]]

## Entities mentioned
- [[kyocera-avx]]

## References
_Original source: `resources/design-rules/kyocera-avx-esr-esl-decoupling.md`_
