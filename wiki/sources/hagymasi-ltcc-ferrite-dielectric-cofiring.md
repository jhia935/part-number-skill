---
title: "Hagymási, Roosen et al. — Constrained Sintering of Dielectric+Ferrite LTCC Tapes (Electroceramics conf., ~2008)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/see-electroceramics-ltcc-constrained.md
tags:
  - paper
status: complete
importance: high
---

# Hagymási, Roosen et al. — Constrained Sintering of LTCC Dielectric+Ferrite Composites

**Source:** `resources/literature/see-electroceramics-ltcc-constrained.md` (PDF: `resources/literature/pdf/see-electroceramics-ltcc-constrained.pdf`, 8 pages)
**Authors:** Marcel Hagymási, Andreas Roosen (Erlangen-Nürnberg); Roman Karmazin, Oliver Dernovsek (Siemens AG); Werner Haas (Kerafol GmbH)
**Venue:** SEE Electroceramics conference, paper A04-03 (likely 2008 / Roosen-group output of that era)
**Access:** Open access via http://web1.see.asso.fr/electroceramics/

## Summary

A clean experimental study of **constrained co-firing of a commercial LTCC dielectric tape (DuPont 951 AT)** with a newly developed **BaFe₁₂O₁₉ ferrite tape** for integrating inductors into multilayer microwave devices (e.g., UMTS circulators). Quantitative dilatometry of both single tapes and the DT/FT/DT sandwich shows how the lateral-to-thickness shrinkage exchange plays out when two tapes with **different shrinkage onset temperatures** are forced to cofire.

This is the source paper behind the "12.7% / 13.9% / 12.8%" free-shrinkage numbers and the "lateral → 3.25%, thickness → 33.1%" constrained-shrinkage numbers that already live in [[constrained-sintering-mlcc]].

## Key quantitative findings

### Green-tape properties

| Property | DuPont 951 AT (dielectric) | BaFe₁₂O₁₉ ferrite tape |
|---|---|---|
| Thickness (µm) | 120 | 130 |
| Green density (g/cm³) | 2.17 | 2.5 |
| Laminate density (g/cm³) | 2.25 | 2.88 |
| **Relative laminate density** | **72%** | **53%** |
| End of binder burnout | 400 °C | 350 °C |
| TMA shrinkage onset | 650 °C | 740 °C |
| Organic content (wt%) | 11.4 | **18.0** |
| TEC, 25–300 °C (ppm/K) | 5.8 | 12.2 |

The ferrite tape has **much lower green density (53%)** due to its high organic content (18 wt% binder + plasticizer), which directly drives its much higher total shrinkage. This is the central data point for [[green-density-vs-shrinkage]].

### Free shrinkage (single-tape, unconstrained)

| Direction | DuPont 951 (DT) | Ferrite (FT) |
|---|---|---|
| Casting direction (x) | 12.7 % | 23.2 % |
| Cross direction (y) | 13.9 % | 23.2 % |
| Thickness (z) | 12.8 % | 21.7 % |

Both tapes are nearly isotropic in their free shrinkage (the slight x ≠ y is from casting-shear particle alignment). FT shrinks ~80% more in plane than DT because of its lower green density and the slower BaFe₁₂O₁₉ densification kinetics.

### Sintering temperature windows

| Tape | Onset | Densification window | Notes |
|---|---|---|---|
| DT (DuPont 951) | 700 °C | 700–840 °C | Done before the FT even starts |
| FT (BaFe₁₂O₁₉ + <10% glass) | 740–760 °C | 760 °C → 5 h hold at 900 °C | Requires the long 900 °C hold |

The windows **partially overlap** (760–840 °C). This means an absolute zero-shrink composite is not achievable, but a self-constrained composite is.

### Constrained composite (DT/FT/DT sandwich, 5 h at 900 °C)

| Direction | Composite shrinkage |
|---|---|
| Casting direction (x) | **3.25 %** |
| Cross direction (y) | **2.97 %** |
| Thickness (z) | **33.1 %** |

In-plane shrinkage is suppressed by **~4×** (from 12.7–23.2% to ~3%) and thickness shrinkage is enhanced ~2.5× (from 12.8–21.7% to 33.1%). The **volume shrinkage budget is approximately conserved**, just redistributed into the thickness axis — a textbook constrained-sintering result.

### Defects observed

| Defect | Where | Cause |
|---|---|---|
| **BBO-stage convex camber** | FT layer (single FT laminate) at 300 °C | Inhomogeneous binder distribution through tape thickness; **eliminated by reducing BBO ramp from 2 K/min to 0.5 K/min** |
| **Cavitation** (~2 vol%) | DuPont 951 layer | Tensile stress during constrained sintering at 700–840 °C |
| **Porosity increase** in FT | Free 6 vol% → constrained **8.5 vol%** | Tensile stress reduces densification driving force |
| **Channel cracks** | Only in the FT layer | High TEC (12.2 vs 5.8 ppm/K) puts FT in residual tensile stress on cooling |
| **Debonding** at DT/FT interface | Cooling stage | Worse at faster cool rate (3 K/min); reduced at 1 K/min via visco-elastic stress relaxation |

## Implications for MLCC

Even though the system studied here is **LTCC (low-temperature 900 °C) cofiring** of dielectric with ferrite, every mechanism transfers directly to Ni-BME MLCC at 1200–1300 °C:

1. **Onset-temperature gap drives constraint.** DT-vs-FT onset gap of ~50–100 °C creates the same in-plane-suppression / thickness-enhancement that Ni-vs-BT's 450 °C gap creates in BME MLCC ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis]]).
2. **High-organic tapes have low green density and shrink more.** Direct quantitative confirmation: 18 wt% organic → 53% green density → 23% free shrinkage.
3. **Slow BBO ramps cure binder-distribution camber.** The 2 → 0.5 K/min reduction of the BBO ramp is the same prescription used in MLCC industry (see [[binder-burnout-debinding]]).
4. **TEC mismatch drives cooldown channel cracks.** Same as the Ni/BT TEC mismatch that drives delamination in MLCC failure modes.

## Entities mentioned

- Andreas Roosen (Erlangen) — see [[heunisch-2010-tape-cast-anisotropic-shrinkage]] (same group).
- Siemens CTMM2 — corporate co-author (UMTS circulator end-application).
- Kerafol GmbH — tape-casting industrial partner.

## Concepts discussed

- [[constrained-sintering-mlcc]] — the central topic; this paper's numbers underwrite that page.
- [[green-density-vs-shrinkage]] — the 72% vs 53% / 12.8% vs 21.7% case study.
- [[cofiring-camber-bilayer]] — BBO-stage camber from binder gradient.
- [[zero-shrinkage-ltcc]] — DuPont 951 is one of the canonical zero-shrinkage tape systems.
- [[binder-burnout-debinding]] — slow BBO ramp prescription.

## Notable quotes

> "Sintering of the ferrite tape starts at 760°C and requires 5 h dwell time at 900°C for densification. The low green density causes high in-plane shrinkage of 23.2 %."

> "The in-plane shrinkage was decreased to 3.25 %, while the main shrinkage of 33.1 % occurs in the height."

> "From these results it is assumed that the high binder concentration is not distributed homogenously over the tape height and leads to camber during binder burnout."

## References

_Original PDF: `resources/literature/pdf/see-electroceramics-ltcc-constrained.pdf`_
- Barker & Draudt, "Zero Shrink Process for Cost Sensitive High Volume LTCC Applications", IMAPS 2001 — the DuPont zero-shrink prior art.
- Mikeska & Schaefer, US 5,474,741 (1995) — DuPont's foundational zero-shrinkage patent.
- Cai, Green, Messing, "Constrained Densification of Alumina/Zirconia Hybrid Laminates I & II", *J. Am. Ceram. Soc.* 80 (1997) — the canonical academic constrained-sintering benchmark.
- Tzeng & Jean, "Stress Development during Constrained Sintering of Alumina/Glass/Alumina Sandwich", *J. Am. Ceram. Soc.* 85 (2002) 335–340.
