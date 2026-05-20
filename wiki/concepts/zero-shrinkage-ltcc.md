---
title: Zero-Shrinkage LTCC Technologies
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - hagymasi-ltcc-ferrite-dielectric-cofiring.md
tags:
  - paper
status: complete
importance: medium
---

# Zero-Shrinkage LTCC Technologies

A family of **constrained-sintering techniques** developed for Low-Temperature Cofired Ceramics (LTCC) that suppress in-plane shrinkage to **< 1 % (typically 0.1–0.5 %)** while letting all the volume shrinkage occur in the thickness direction. The motivation is **dimensional precision** for high-density circuit modules: when fired conductors and vias must align with sub-µm tolerance over centimeters, you cannot tolerate the usual 12–17 % lateral sintering shrinkage.

These techniques are technically applicable to MLCC manufacturing but rarely used because (a) MLCC accuracy requirements are less stringent and (b) the sacrificial-layer step adds cost. They are however **the highest-accuracy demonstrated case** for in-plane control of fired ceramic dimensions, and the lessons carry over to MLCC design.

## The four main approaches

### 1. Sacrificial constraining tape (DuPont 951 + GreenTape)

**Method**: laminate a layer of **non-sintering tape** (typically alumina + organic binder, sintering temperature > the LTCC's) on **both top and bottom** of the LTCC stack. Cofire. The alumina doesn't densify at the LTCC's sintering temperature, so it stays rigid and **its friction at the interface holds the LTCC tape's in-plane dimensions fixed**. After firing, the alumina is sandblasted, brushed, or chemically removed.

Result: total in-plane shrinkage **< 0.5 %**.

**Prior art**:
- DuPont US 5,474,741 (Mikeska & Schaefer 1995) — the foundational patent.
- Barker & Draudt, "Zero Shrink Process for Cost Sensitive High Volume LTCC Applications", IMAPS 2001.

**Trade-off**: extra process step (lamination + removal); extra material cost.

### 2. Self-constrained sintering (no sacrificial layer)

**Method**: stack two tape materials with **non-overlapping shrinkage windows**. The first to sinter (low-T) becomes the "rigid substrate" for the second (high-T). Each tape acts as a constraining layer for the other in turn.

Demonstrated in [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási et al.]]:
- DT (DuPont 951): sintering window 700–840 °C
- FT (BaFe₁₂O₁₉ + glass): sintering window 760–900 °C+
- DT/FT/DT sandwich, cofired 5 h at 900 °C: in-plane 3.25 % / cross 2.97 % / thickness 33.1 %

The lateral suppression is not as good as the sacrificial-layer route (~3 % vs <0.5 %), because the sintering windows overlap from 760-840 °C. But the **process is single-step** — no sacrificial removal.

### 3. HeraLock / Heraeus self-constrained tape

**Method**: Heraeus HL2000 / HeraLock tape system is engineered so that two **chemically tuned glass-ceramic compositions** with offset sintering windows can be cofired without any external sacrificial layer.

Result (Heraeus claim): in-plane shrinkage **< 0.2 %** with shrinkage tolerance **± 0.02 %**, no sacrificial layer, no external pressure.

This is the most refined of the no-sacrificial-layer approaches. The vendor controls all the recipe magic.

### 4. Pressure-assisted constrained sintering

**Method**: apply mechanical pressure (vertical compressive load) through the firing cycle. Pressure forces all the strain into the thickness direction; lateral shrinkage drops to near-zero.

Closely related to [[spark-plasma-sintering|SPS]] but for tape-cast components, the equipment is custom and expensive (hot-presses with high-precision platens).

Trade-off: equipment cost; limited part complexity.

## Comparison table

| Method | Lateral shrinkage | Sacrificial step | Vendor examples |
|---|---|---|---|
| Sacrificial alumina tape | < 0.5 % | Yes (post-process removal) | DuPont 951 GreenTape + sac. layer |
| Self-constrained (offset windows) | 2–4 % | No | Hagymási, lab-scale |
| HeraLock / HL2000 | < 0.2 % (± 0.02 %) | No | Heraeus HL2000 |
| Pressure-assisted | < 0.5 % | No | Custom hot-press |

## Why MLCC doesn't (much) use these

1. **MLCC dimensional tolerance is more permissive** than dense LTCC RF circuitry — ±20 µm on a 1.6 mm chip is acceptable; sub-µm via alignment is not needed.
2. **Symmetric stack design naturally cancels camber** in MLCC, removing the main constraint-driven failure.
3. **Cost** — MLCC is a high-volume, ultra-low-margin product. The extra sacrificial-tape process adds cost that's hard to justify.

However, **the same physics** applies whenever an MLCC is integrated into a higher-level package (IPD, IPC, EmbeddedCapacitor):
- Embedded MLCC in a printed-circuit substrate cofired with the resin: external constraint suppresses lateral MLCC shrinkage. The 2.5D/3D packaging trend will increasingly force MLCC designers to think about constrained-sintering tolerance.
- AEC-Q104 multi-chip modules ([[aec-q104-rev-a-2025]]) have explicit cofiring-constraint failure modes.

## SOVS-predicted constrained shrinkage

The [[skorohod-olevsky-viscous-sintering|SOVS]] viscous Poisson's ratio gives the in-plane suppression factor directly. For a fully constrained film (zero lateral strain rate), the thickness strain rate is amplified by `1 / (1 − 2ν_v)`. For typical sintering ceramics `ν_v ≈ 0.45`, so the amplification factor ≈ 10× — meaning ~12 % free linear shrinkage becomes ~33 % thickness shrinkage when fully constrained.

This matches the Hagymási observation exactly (12.8 % free thickness → 33.1 % constrained thickness in the DT/FT/DT sandwich).

## Implications for the simulator

For a generic MLCC simulator, zero-shrinkage LTCC is mostly out of scope. But:
- If the simulator targets **embedded MLCC** in a constraining substrate, it must implement the SOVS-style ν_v amplification factor.
- For **AEC-Q104 module-level reliability** prediction, the simulator should model the residual stress that lateral constraint puts on the MLCC's BaTiO₃ — that stress feeds back into [[cubic-tetragonal-transition|domain formation]] and [[dc-bias-aging|DC bias aging]].

## Cross-references

- [[constrained-sintering-mlcc]] — the underlying physics.
- [[cofiring-camber-bilayer]] — the failure mode this technology mitigates.
- [[hagymasi-ltcc-ferrite-dielectric-cofiring]] — experimental data on self-constrained sintering.
- [[skorohod-olevsky-viscous-sintering]] — quantitative prediction of constrained vs free shrinkage.

## References

- Mikeska & Schaefer, "Method For Reducing Shrinkage During Firing Of Ceramic Bodies", US Pat. 5,474,741 (1995) — DuPont foundational.
- Barker & Draudt, "Zero Shrink Process for Cost Sensitive High Volume LTCC Applications", IMAPS 2001, pp. 26–31.
- Rabe et al., "Zero Shrinkage of LTCC by Self-Constrained Sintering", *Int. J. Appl. Ceram. Technol.* 2 (2005) — review of approaches.
- Mohanram & Lee, "Constrained Sintering of Low-Temperature Co-Fired Ceramics" — Semantic Scholar entry.
- Heraeus HeraLock HL2000 technical datasheet.
