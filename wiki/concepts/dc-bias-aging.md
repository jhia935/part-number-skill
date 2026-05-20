---
title: DC-Bias Aging
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - vishay-x7r-cap-drift-dc-bias.md
  - electrical-integrity-dce11-200.md
  - epci-high-cv-mlcc-bias-aging.md
tags:
  - paper
---

# DC-Bias Aging

**Long-time capacitance drift under continuous DC bias**, distinct from both the immediate [[dc-bias-derating]] (VCC) step and from natural [[aging-class-2]]. Under continuous DC bias the capacitance keeps decreasing logarithmically with time at a rate **much faster** than the unbiased aging rate — sometimes 5–10× faster. Recovers slowly when bias is removed and fully when heated above the [[curie-temperature]].

## Two distinct components in the time-domain response
After applying DC bias to a Class II MLCC, the capacitance trajectory has two parts ([[electrical-integrity-dce11-200]] Fig. 16):

1. **Immediate VCC step** (seconds): the [[dc-bias-derating]] effect; depends on field `E = V_DC / d`. Sigmoid in field magnitude.
2. **Slow tail** (hours to thousands of hours): the DC-bias-aging component. Logarithmic in time. Rates from −2.8 %/decade (best) up to −13.8 %/decade (worst) measured on real parts ([[electrical-integrity-dce11-200]]).

The slow tail can dominate the long-term capacitance budget.

## Vishay's vendor benchmark
[[vishay-x7r-cap-drift-dc-bias]] tested 0603 X7R 100 nF / 50 V parts from Vishay (PME) and three BME competitors at 40 % rated V (20 V_dc, 2.5 V/µm field) and 100 % rated V (50 V_dc, 6 V/µm field) for 1000 hours:

| Vendor | Loss after 1000 h at 40 % rated V |
|---|---|
| Vishay (PME) | ~5 % |
| Competitor 1 (BME) | > 20 % |
| Competitor 2 (BME) | > 25 % |
| Competitor 3 (BME) | > 30 % |

Average BME competitor rate after 3 decades: > 7 %/decade. Natural aging on the same parts would be 1–2 %/decade.

## Mechanism (proposed)
Linked to oxygen-vacancy migration in BaTiO₃ under continuous DC bias. The PME advantage (no reducing-atmosphere firing → fewer vacancies) is consistent with Vishay PME's much smaller drift. Domain-wall re-pinning by the static field is the other proposed mechanism.

## Recovery
Removing bias → slow recovery (Vishay PME 95 % in minutes; BME competitors 50–1000 h to 95 %). Full recovery requires heating above [[curie-temperature]] (~125–150 °C × 1 h).

## Implication for simulator
The aging factor `f_age(t, E, T)` in §3.4 of `simulator-model.md` must encompass **two regimes**:
- At zero bias: natural log-aging rate `A_age` (Class- and material-specific, 1–7 %/decade)
- Under bias: an accelerated rate (typically 5–10× faster on BME, 1× on PME)

For conservative design simulation, use the higher bias-accelerated rate for any deployment with non-trivial DC bias. The EPCI multiplicative formula ([[epci-high-cv-mlcc-bias-aging]]) folds this into `F_aging`.

## Cross-references
- [[dc-bias-derating]] — the immediate VCC step, not the same phenomenon
- [[aging-class-2]] — unbiased natural aging, slower
- [[bme-vs-pme]] — PME is the only proven counter to DC-bias-aging
- [[batio3]]

## References
- [[vishay-x7r-cap-drift-dc-bias]]
- [[electrical-integrity-dce11-200]]
- [[epci-high-cv-mlcc-bias-aging]]
