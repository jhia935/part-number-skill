---
title: Cu Electrode MLCC (Base-Metal Class I C0G)
type: concept
created: 2026-05-21
updated: 2026-05-21
sources: []
tags:
  - paper
status: complete
importance: medium
---

# Cu Electrode MLCC (Base-Metal C0G)

A second family of base-metal-electrode MLCCs that uses **copper** instead of nickel for the internal electrode. Cu has lower bulk resistivity than Ni (1.7 vs 6.9 µΩ·cm at 20 °C), better RF performance at high frequencies, and is cheaper per gram — but Cu's much lower melting point (**1083 °C** vs Ni's 1453 °C) forces the entire firing process below ~1050 °C. That in turn forces the **dielectric to be glass-aided** to densify in the same low-T window.

Cu-electrode MLCCs are the dominant base-metal solution for **Class I (C0G/NP0) MLCC** — see [[bme-c0g]] and the [[kyocera-avx]] product line that pioneered them. Class II (X7R) MLCCs are still almost exclusively Ni-electrode because the BaTiO₃ system densifies natively in the Ni-compatible window.

## The Cu sintering trade-off

| Material | Melting point | Practical max sintering T | Compatible dielectric class |
|---|---|---|---|
| Ag | 962 °C | 850 °C | Air-fired LTCC (Ag-Pd-Pt PME C0G or glass-ceramic) |
| **Cu** | **1083 °C** | **1050 °C** | Glass-aided BaTiO₃, CaZrO₃, or BST C0G/X7R |
| Ni | 1453 °C | 1350 °C | Native sintering BaTiO₃ (X7R/X5R standard) |
| Pd | 1555 °C | 1500 °C | Native sintering BaTiO₃, full PME |

Cu sits in an awkward band where you cannot fire the standard Ni-BaTiO₃ recipe — you must lower the dielectric's sintering T into Cu's window.

## Lowering dielectric sintering T to ~ 900–960 °C

The standard approach is **glass aids**: BaO-B₂O₃-SiO₂ (BBS), ZnO-B₂O₃-SiO₂ (ZBS), or PbO-B₂O₃-SiO₂ (PBS, now mostly phased out for RoHS) added to the BaTiO₃ at **2–5 wt%**. The glass forms a transient liquid phase at 700–900 °C that wets the BT particles and accelerates densification by liquid-phase sintering, lowering the densification window into the 900–960 °C range.

Cited recipes (search snippets):
- BaTiO₃ + SiO₂-B₂O₃-Li₂O sintering additives, sintered 900–950 °C in H₂/N₂.
- Cu-electrode MLCC sintering T as low as **960 °C**.

See [[sintering-aids-glass]] for the glass-aid chemistry.

## Cu paste shrinkage characteristics

Cu paste has its own shrinkage curve, qualitatively similar to Ni but **shifted lower in temperature**:

| Cu paste regime | Approx. T window | Note |
|---|---|---|
| Onset of densification | ~400 °C | Below the dielectric onset |
| Max densification rate | ~700 °C | While dielectric is still rigid |
| Effectively dense | ~900 °C | Reaches max density before peak sintering |
| Peak sintering T | 900–960 °C | Below Cu melting (1083 °C) |
| Cooldown | 950 → 25 °C | Reducing atmosphere maintained to ~600 °C |

The Cu-vs-glass-aided-BT shrinkage onset gap is similar to or smaller than Ni's: 300–400 °C vs Ni's 450 °C. The same nano-dielectric-additive trick used in Ni paste (see [[ni-electrode-paste-formulation]]) applies to Cu — Cu paste typically contains **2–10 mass% nano-dielectric inclusions** to retard Cu densification and bring the curve up into the dielectric's window.

## Atmosphere control

Cu oxidizes more easily than Ni (lower ΔH_f for the oxide). The cofiring atmosphere window is **tighter** for Cu:
- BBO (200–500 °C): pure inert (Ar or N₂), no O₂ — Cu would oxidize.
- Peak sinter (900–960 °C): reducing (H₂/N₂ or N₂ with H₂ < 5 vol%).
- Reoxidation anneal (if used): very mild, since Cu can't tolerate the slightly oxidizing PO₂ used for Ni.

The reoxidation step that BME-Ni parts use to refill V_O in BaTiO₃ is **largely absent** in Cu-MLCC because Cu cannot tolerate the required PO₂. Cu-MLCC dielectrics therefore depend more on **dopant compensation** ([[defect-chemistry-batio3|donor-acceptor co-doping]]) to control V_O in the as-fired part.

## Industry use

- **[[kyocera-avx]]**: pioneered Cu-electrode RF MLCC (high-Q C0G with Cu cofiring).
- **[[murata]]**: Cu-electrode RF lineup for sub-6-GHz applications.
- **[[kemet]]** / Yageo: some C0G Cu-MLCC, particularly KEMET's high-CV C0G.
- **TDK**: Cu in selected RF/automotive C0G grades.

For Class I (C0G/NP0) MLCC, Cu is the modern base-metal standard. For Class II (X7R/X5R) MLCC, Ni still dominates because the BT system doesn't need to be glass-aided — the dielectric is already shrinkable at higher T where Ni is fine.

## Constrained-sintering behavior

The Cu/dielectric system shows the same **lateral-suppression / thickness-enhancement** as Ni/BT, but with smaller magnitudes because:
1. The Cu-vs-dielectric shrinkage onset gap is narrower (with glass-aided BT).
2. Cu is softer than Ni at peak T (viscosity is lower), so it cannot constrain the dielectric as rigidly.

Net: Cu-MLCC chips typically show ~10–13 % chip-scale linear shrinkage (vs 12 % for Ni-BME), and **fewer Rayleigh-Plateau electrode-break-up defects** because the cofiring profile is less stressed.

## Implications for the simulator

If the simulator targets both Ni-BME and Cu-BME:
- Cu paste: lower onset T (400 vs 450 °C), lower peak T (960 vs 1250 °C), lower η at peak.
- Dielectric: glass-aided BaTiO₃ or CaZrO₃ — different `η(T)` curve dominated by liquid-phase sintering.
- Atmosphere: tighter PO₂ window; no reoxidation step.
- Continuity: easier (less interfacial liquid metal alloy at peak T).

The same SOVS framework predicts both, just with different material parameters.

## Cross-references

- [[bme-c0g]] — the Class I product class that Cu electrodes serve.
- [[kyocera-avx]] — pioneer Cu-electrode RF MLCC vendor.
- [[bme-vs-pme]] — base-metal vs precious-metal trade-offs (Cu sits in between historically).
- [[sintering-aids-glass]] — glass-frit chemistry for low-T dielectric densification.
- [[metal-electrode-shrinkage-effect]] — parent concept.
- [[ni-electrode-paste-formulation]] — analog for Ni.
- [[bme-sintering-atmosphere]] — atmosphere control across both Ni and Cu.

## References

- KYOCERA AVX HiQ-MLCC product literature — Cu inner electrodes for RF C0G.
- KEMET / Yageo C0G technical notes on BME with Cu inner electrodes.
- Various JECS / ScienceDirect studies on SiO₂-B₂O₃-Li₂O sintering aids in BaTiO₃ for Cu-MLCC.
