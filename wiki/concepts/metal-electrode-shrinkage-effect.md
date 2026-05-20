---
title: Effect of the Metal Electrode on MLCC Shrinkage
type: concept
created: 2026-05-21
updated: 2026-05-21
sources:
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
  - sugimura-hirao-2009-batio3-additive-ni-electrode.md
  - polotai-2007-cr-doping-ni-electrode-mlcc.md
  - hagymasi-ltcc-ferrite-dielectric-cofiring.md
tags:
  - paper
status: complete
importance: high
---

# Effect of the Metal Electrode on MLCC Shrinkage

In a BME MLCC the internal Ni (or Cu) electrode is **not a passive spectator** during sintering. It has its own shrinkage trajectory, sinters in a different temperature window than the BaTiO₃ dielectric, exerts mechanical stress on the surrounding ceramic, and (through interfacial chemistry) modifies the dielectric's own shrinkage behavior at the contact zone. This page consolidates the four levers by which the metal electrode controls — or is controlled by — the chip-level shrinkage.

## Three regimes during the firing cycle

| Stage | Temperature | What the Ni electrode is doing | What the BT dielectric is doing | Net stress on Ni layer |
|---|---|---|---|---|
| **1. Solo Ni densification** | ~450 → 950 °C | Sintering, shrinking 25–35 % linearly | Cold and rigid (still green) | **Tensile** — Ni wants to contract but is anchored to a rigid matrix |
| **2. Coincident shrinkage** | 950 → 1100 °C | Done densifying, grain coarsening | Initial-stage sintering | Tensile decreasing |
| **3. BT-dominated shrinkage** | 1100 → 1250 °C | Quasi-rigid dense Ni | Final-stage densification (5–6 % / 30 min hold) | **Compressive** — dense matrix squeezes the metal layer |

Both stress reversals contribute to electrode discontinuity. Stage 1 tensile stress is largely responsible for the **thinning of heterogeneous Ni regions** ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis]] Ch. 5). Stage 3 compressive stress drives the **Rayleigh-Plateau break-up** at peak T ([[ni-batio3-cosintering-interface|liquid alloy mechanism]]).

## The four engineering knobs

### Knob 1 — Nano-BT additive in the Ni paste (shrinkage retardation)

The primary lever for **moving Ni's shrinkage onset higher** to reduce the gap to BT's onset. Quantitatively from DEM + experiment:

| BT additive vol% | BT size (nm) | Retarding factor at D = 0.70 | Ni film coverage |
|---|---|---|---|
| 0 | — | 1.0 | catastrophic break-up at peak T |
| 5 | 60 | ~1.5 ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan DEM]]) | marginal |
| 10 | 30 | (experimental) | **> 75 %** ([[sugimura-hirao-2009-batio3-additive-ni-electrode|Sugimura-Hirao]]) |
| 20 | 60 | **7×** | excellent |

**Smaller particles outperform larger ones dramatically** at the same vol%. Smaller-and-well-dispersed is the optimum; agglomeration kills the effect.

Mechanism: rigid BT inclusions substitute Ni-Ni contacts (which sinter) by Ni-BT contacts (which don't), per [[bordia-scherer-composite-sintering|Bordia-Scherer]]. The BT also coats Ni grains and **protects them from oxidation** during the BBO-to-reducing transition. See [[ni-electrode-paste-formulation]].

### Knob 2 — Refractory-metal dopants in the Ni alloy (interfacial chemistry)

A separate lever: **changes the interfacial chemistry without changing the shrinkage curve**.

From [[polotai-2007-cr-doping-ni-electrode-mlcc|Polotai 2007]]:
- Ni-1 wt% Cr alloy powder vs pure Ni.
- **Densification curves: identical** within experimental error.
- But: 1 wt% Cr **segregates to the Ni/BT interface** at peak T and chemically suppresses the ~8 nm (Ni, Ba, Ti) liquid alloy layer that drives Rayleigh-Plateau break-up.
- Result: improved electrode continuity at peak T, especially at 1200–1250 °C.

The same family includes **V, Mo, W, and Re** doping of Ni for refractory-metal stabilization. Different elements have different trade-offs against [[defect-chemistry-batio3|BaTiO₃ defect chemistry]] (Cr is double-edged because it diffuses into BT and creates V_O).

### Knob 3 — Ni particle size (shrinkage rate and final density)

Submicron Ni powder (0.1–0.3 µm) is the modern BME standard:
- Smaller Ni → faster initial-stage densification (higher driving force / r_p).
- Smaller Ni → lower shrinkage onset T (~450 °C for 0.2 µm Ni from [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan]]).
- Smaller Ni → larger volume of metal-metal contact subject to substitution by BT inclusions ([[bordia-scherer-composite-sintering|Bordia-Scherer]]), so additive retardation works better.

Going below ~0.1 µm Ni hits diminishing returns: surface oxidation becomes hard to control, paste rheology suffers, and the additive needs to scale to even smaller (sub-30 nm) BT to remain effective.

### Knob 4 — Electrode-to-dielectric thickness ratio (geometric constraint)

For an MLCC with Ni-layer thickness `h_Ni` and BT-layer thickness `h_BT`, the in-plane stress that Ni exerts on the surrounding BT scales with the ratio `h_Ni / h_BT` (approximate beam-bending result). For modern thin-layer parts where `h_Ni ≈ h_BT ≈ 1 µm`:

- The Ni layer is no longer a passive thin film — it's a structural member of the laminate.
- Constrained Ni shrinkage tensile stress affects BT layer cracking probability.
- Constrained BT shrinkage compressive stress affects Ni layer break-up probability.

Lower `h_Ni / h_BT` (thinner electrode) relaxes both, but reduces conductive cross-section. The sweet spot is around `h_Ni / h_BT = 0.5–1.0` for state-of-the-art 1 µm dielectric MLCCs.

## Why the metal electrode dominates the **lateral** shrinkage but not **thickness**

In a finished MLCC stack the Ni electrode is a **continuous in-plane sheet** between dielectric layers. During sintering:
- **Lateral shrinkage** of the BT layer is constrained by the Ni sheet **on both faces** — a stiff Ni layer pushes the lateral shrinkage toward zero.
- **Thickness shrinkage** of the BT layer is approximately **unconstrained** — the Ni layer can shrink with the BT in the through-thickness direction because both contract together.

Per [[constrained-sintering-mlcc|constrained-sintering]] physics: in-plane shrinkage suppressed by ~4×, thickness enhanced by ~2.5×, total volume shrinkage approximately conserved. So **the metal electrode is the direct cause of the lateral/thickness asymmetry in MLCC**. Without the electrode, an isotropic green BT tape would shrink isotropically.

This is the key insight that links the metal electrode to dimensional control: **a denser, more rigid, more continuous Ni layer constrains BT lateral shrinkage harder**, and produces a larger thickness enhancement. The simulator's chip-dimension prediction is therefore a function of:

1. Ni paste recipe → Ni shrinkage curve → effective `η_Ni(T)`.
2. BT tape recipe → BT shrinkage curve → effective `η_BT(T)`.
3. `h_Ni`, `h_BT`, electrode coverage area → geometric constraint.

The [[skorohod-olevsky-viscous-sintering|SOVS]] framework predicts all three contributions simultaneously.

## The Hagymási analog

The DT/FT/DT LTCC sandwich from [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási]] is **exactly the same geometry** as an MLCC stack, with the LTCC dielectric playing the role of BT and the ferrite tape playing the role of Ni paste. Free DT shrinkage of 12.8 % in thickness becomes 33.1 % in the constrained sandwich. **The MLCC's lateral suppression by Ni is the same physics**, just with Ni in place of a sacrificial dielectric layer.

## Cu electrode systems

A separate base-metal class. See [[cu-electrode-mlcc]]:
- Cu melts at 1083 °C — sintering must stay below ~1050 °C.
- C0G / Class-I dielectrics with [[sintering-aids-glass|glass aids]] (BBS, ZBS, PBS) densify at 900–960 °C.
- Cu shrinkage onset is ~400 °C, max rate at ~700 °C — even larger gap to its glass-aided BT-equivalent than Ni has to BT.
- The same retardation tricks apply: nano-dielectric additives in Cu paste.

## Implications for the simulator

A complete shrinkage model for a BME MLCC needs separate inputs for each electrode-effect knob:

1. `η_Ni(T)` from free-Ni-paste dilatometry (sensitive to BT-additive loading and size).
2. Optional Cr/V/refractory-metal flag — doesn't change `η_Ni(T)` but does suppress the (Ni, Ba, Ti) alloy → reduces post-peak electrode break-up probability.
3. `h_Ni`, `h_BT` from the green-tape and paste-print spec.
4. Electrode coverage % from print pattern.

Output:
- Chip-scale linear shrinkage (in-plane and thickness separately, per [[constrained-sintering-mlcc]] and [[skorohod-olevsky-viscous-sintering]]).
- Electrode continuity / discontinuity probability (set by both shrinkage mismatch AND interfacial alloy formation).
- Residual stress on the BaTiO₃ that modifies [[cubic-tetragonal-transition|tetragonal domain]] formation on cooling.

## Cross-references

- [[ni-batio3-cosintering-interface]] — interfacial chemistry, where the metal-vs-ceramic mismatch plays out.
- [[ni-electrode-paste-formulation]] — recipe-level details for paste design.
- [[cu-electrode-mlcc]] — Cu-based base-metal systems.
- [[constrained-sintering-mlcc]] — the constraint physics.
- [[bordia-scherer-composite-sintering]] — analytical foundation for additive retardation.
- [[skorohod-olevsky-viscous-sintering]] — continuum-mechanics model for the full prediction.
- [[failure-modes-mlcc]] — electrode discontinuity and delamination as failure modes.

## References

- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — DEM + nano-CT on Ni/BT cofiring.
- [[sugimura-hirao-2009-batio3-additive-ni-electrode]] — empirical BT-additive sweet spot.
- [[polotai-2007-cr-doping-ni-electrode-mlcc]] — Cr-doping decoupling between shrinkage and continuity.
- [[hagymasi-ltcc-ferrite-dielectric-cofiring]] — direct analog in LTCC.
- Kang, Joo, Cha, Jung, Paik, "Shrinkage behavior and interfacial diffusion in Ni-based internal electrodes with BaTiO₃ additive", *Ceram. Int.* 34 (2008) 1487.
- Jean & Chang, "Effect of Densification Mismatch on Camber Development during Cofiring of Nickel-Based MLCCs", *J. Am. Ceram. Soc.* 80 (1997) 2401.
- Polotai et al., "Utilization of Multiple-Stage Sintering to Control Ni Electrode Continuity in Ultrathin Ni–BaTiO₃ MLCC", *J. Am. Ceram. Soc.* 90 (2007) 3811.
