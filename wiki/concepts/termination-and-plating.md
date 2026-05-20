---
title: Termination & Plating (External Electrode Stack)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - psma-ceramic-capacitor-basics.md
  - kemet-mlcc-design-and-characteristics.md
tags:
  - paper
---

# Termination & Plating

The three-metal-layer external electrode stack on each end of an MLCC chip. Provides electrical contact to all the internal-electrode tabs of one polarity, mechanical anchor to the PCB pad, and a solderable finish that survives oven reflow.

## Standard BME stack (modern Tier-1)

```
Sn finish (5–10 µm matte, electrolytic)
    └──── solderability + corrosion protection
Ni barrier (2–3 µm electrolytic)
    └──── prevents Sn-Cu intermetallic & solder-leaching
Cu paste sintered termination (10–30 µm)
    └──── ohmic contact to internal Ni electrodes; structural backbone
└── Internal Ni electrode tabs exposed at chip end after dicing/rounding
```

For **PME parts** ([[bme-vs-pme|legacy noble-metal electrode]]): the termination layer is **Ag-Pd or Ag** instead of Cu, again with a Ni barrier and Sn finish.

## Process sequence
1. **Corner rounding**: tumble the as-sintered chips with rounding media to expose internal-electrode tabs and break sharp corners (reduces flex-crack initiation).
2. **Termination dipping**: dip each end into a Cu (or Ag-based) thick-film paste containing metal powder + glass frit + organic vehicle.
3. **Termination sintering**: bake at ~700–900 °C (well below BaTiO₃ peak sintering T) — the glass frit melts, wets the dielectric/electrode tab, and bonds the Cu layer.
4. **Ni barrier plating**: electrolytic Watts-bath nickel; typical 2–3 µm thick over the termination Cu.
5. **Sn finish plating**: matte tin (or SnPb for legacy applications); 5–10 µm.

## Why three layers
- **Cu termination alone**: would dissolve into the molten solder during reflow ("leaching"), exposing the BaTiO₃ and breaking the contact.
- **Cu + Sn (no Ni barrier)**: Sn-Cu intermetallics (Cu₆Sn₅, Cu₃Sn) grow at the interface and embrittle the joint over time.
- **Cu + Ni + Sn (full stack)**: Ni is a slow-diffusion barrier that limits Cu-Sn IMC growth; Sn provides clean solderability; Cu provides bulk conductivity and mechanical anchor.

## Flexible (soft) termination variants
For flex-crack mitigation ([[failure-modes-mlcc]]), some manufacturers insert a **conductive epoxy layer** between Cu and Ni barrier:
- KEMET FT-CAP
- TDK soft-termination CC-Cap
- Murata GRT series

The epoxy is silver-filled (so still conductive) and elastomeric — it absorbs PCB-flex stress that would otherwise crack the rigid ceramic-Cu interface. Bends rated to **5 mm PCB flex** vs **2 mm** for standard termination.

## Defect modes
| Mode | Cause |
|---|---|
| **Termination void** | Cu paste not fully wetting the dielectric/electrode tab — open circuit |
| **Solder leaching** | Excessive reflow heating → Cu termination dissolves into solder; Ni barrier insufficient or porous |
| **Sn whisker** | Pure Sn under compressive stress grows whiskers that short adjacent terminations — mitigated by SnPb (legacy) or Sn-matte + post-anneal |
| **Plating crack** | Improper plating chemistry → cracked Ni/Sn layers admit moisture |
| **Dewetting** | Solder doesn't wet the Sn surface — usually oxide contamination from inadequate storage |

## Implications for the simulator
- Termination contributes a fixed (small) series resistance to the part's ESR — typically < 5 mΩ for modern parts.
- Termination geometry sets the **BW (bandwidth)** dimension in datasheets ([[samsung-cl-series-mlcc-ds]] field 8): the lateral extent of the termination wrap-around. Affects ESL and solderability margin.
- Flex termination reduces ESL slightly (resin layer is poorer conductor) but moves the flex-crack failure point outside the ceramic active area.

## Cross-references
- [[mlcc-manufacturing-process]]
- [[failure-modes-mlcc]]
- [[bme-vs-pme]]
- [[esr-esl-srf]]
- [[case-size-geometry]]

## References
- [[psma-ceramic-capacitor-basics]]
- [[kemet-mlcc-design-and-characteristics]]
- [[octopart-tdk-cga8l3c0g-product-guide]]
- [[nasa-cracking-low-voltage-mlcc]] (Section 2.3 termination materials)
