---
title: Vishay Intertechnology (Vitramon)
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - vishay-x7r-cap-drift-dc-bias.md
tags:
  - company
status: complete
importance: medium
---

# Vishay Intertechnology (Vitramon)

US-headquartered passive component manufacturer. The MLCC product line operates under the **Vitramon** brand (legacy Vitramon Inc., acquired by Vishay in 1994). A second-tier player by unit volume, but technically active — notably the **only Tier-1 publisher of long-duration DC-bias-aging data** ([[vishay-x7r-cap-drift-dc-bias]]).

## Stance: PME over BME for DC-bias stability
Vishay manufactures its X7R MLCCs using **PME** (noble-metal electrode) technology — Pd or Pd-Ag internal electrodes, Ag termination, air firing. This is the older approach largely abandoned by Asian competitors for cost reasons.

The Coppens et al. 2021 white paper ([[vishay-x7r-cap-drift-dc-bias]]) makes the case empirically: at 1000 h of DC bias at 40 % rated voltage, Vishay's PME X7R drifted only ~5 % while three BME competitors drifted 20–30 %. The implied mechanism is BME's higher concentration of oxygen vacancies (forced by the reducing-atmosphere firing).

## Relevance for the simulator
Vishay's published data is the most quantitative public reference for [[dc-bias-aging]] and supplies the typical Class II VCC curve baseline used in `simulator-model.md` § 3.1.

## See also
- [[dc-bias-aging]]
- [[bme-vs-pme]]
