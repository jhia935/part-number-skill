---
title: "NASA / Liu — Insulation Resistance Degradation in Ni-BaTiO₃ MLCCs (IEEE TCPMT 2015)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/nasa-ir-degradation-ni-batio3-2015.md
tags:
  - paper
status: complete
importance: high
---

# NASA / Liu — Insulation Resistance Degradation in Ni-BaTiO₃ MLCCs

**Source:** `resources/literature/nasa-ir-degradation-ni-batio3-2015.md` (PDF: `resources/literature/pdf/nasa-ir-degradation-ni-batio3-2015.pdf`)
**Author:** Donhang (David) Liu ([[donhang-liu]]), ASRC Federal Space and Defense, work for NASA Goddard
**Venue:** *IEEE Transactions on Components, Packaging and Manufacturing Technology* Vol. 5 No. 1, January 2015

## Summary

The mechanistic companion to Liu's 2013/2014 framework papers. Identifies **oxygen vacancy migration to grain boundaries** as the dominant IR-degradation mechanism in [[bme-vs-pme|BME]] MLCCs and proposes a quantitative model where the Schottky double-depletion barrier height `φ(t)` decreases exponentially:
$$
\phi(t) = \phi(0)\, e^{-2Kt}, \quad K = K_0\, e^{-E_k/kT}
$$
The Arrhenius pre-factor `K` is inversely proportional to MTTF. Counterintuitively, an **intermediate barrier height** gives the best reliability: too low `φ(0)` → too much electronic carrier conduction → degraded IR; too high → fast oxygen-vacancy electromigration and rapid barrier collapse.

## Experimental design

Three commercial AEC-Q200 BME 0.47 µF / 50 V / 0805 parts (Manufacturers A, B, C) examined under HALST.

| Sample | Layers | Dielectric thickness | Avg grain | V/grain @ 250V/175°C |
|---|---|---|---|---|
| Mfr A (AA47450) | 98 | 6.39 µm | 0.38 µm | 14.75 |
| Mfr B (AB47450) | 100 | 5.80 µm | 0.33 µm | 14.13 |
| Mfr C (AC47450) | 103 | 8.10 µm | 0.40 µm | 12.45 |

V/grain values are tightly clustered (12.5–14.8) confirming the **"voltage per grain boundary" invariant** that Liu first identified in his 2013 work with Murata HALT data.

## Key physics
- **Heywang-Jonker model**: double Schottky depletion layers at grain boundaries explain the positive temperature coefficient of resistance (PTCR) in donor-doped BaTiO₃ and the high resistivity of the grain-boundary network.
- **Rare-earth doping** (Y, Ho, La, Yb, Tb) reduces O-vacancy diffusion coefficient and improves IR. The dopant atoms sit at grain boundaries and trap O-vacancies.
- **Re-oxidation anneal** after reducing-atmosphere firing fills some O-vacancies, but never all of them — residual vacancy concentration is the BME-specific reliability liability.

## TTF criterion
Liu uses **leakage current = 100 µA** as the failure threshold. Older work used IR drop of 3–4 orders of magnitude (MIL-PRF-123); thin-layer parts have to use absolute current limits because IR drops much further from a higher initial value.

## Historical anchor
MIL-PRF-123 required `d_min = 25 µm` for V_r > 50 V. Modern thin-layer BME is **sub-2 µm** — over 12× thinner. The N-amplifier + thinner d combination is what drives the IR-degradation problem.

## Concepts discussed
- [[oxygen-vacancy-migration]]
- [[bme-reliability-model]]
- [[core-shell-batio3]]
- [[bme-sintering-atmosphere]]
- [[re-oxidation-anneal]]

## Entities mentioned
- [[donhang-liu]]
- [[nasa-nepp]]
- [[batio3]]

## References
_Original source: `resources/literature/nasa-ir-degradation-ni-batio3-2015.md`_
