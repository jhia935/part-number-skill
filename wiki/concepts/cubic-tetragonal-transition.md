---
title: Cubic→Tetragonal Phase Transition (BaTiO₃ Cooldown)
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - arxiv-batio3-cubic-to-tetragonal-md.md
  - arxiv-batio3-domain-wall-motion.md
tags:
  - paper
---

# Cubic→Tetragonal Phase Transition

The last physics event in the sintering recipe — and the one that **creates the ferroelectric structure** that the MLCC will rely on for the rest of its life. Above the [[curie-temperature|Curie temperature]] (T_C ≈ 393 K = 120 °C for bulk BaTiO₃), the perovskite is cubic and paraelectric. On cooldown through T_C, the structure shears to tetragonal, the Ti⁴⁺ shifts off-center along one of six C₄ axes, and a permanent dipole appears. **Spontaneous polarization, ferroelectric domains, twins, and residual stresses all originate here.**

## Order of the transition
First-order with a small thermal hysteresis (~1–2 °C). On cooling: cubic (a) → tetragonal (a × a × c, c/a ≈ 1.01); on further cooling below 5 °C → orthorhombic; below −90 °C → rhombohedral.
For MLCC operation only the tetragonal phase matters (it's the room-T phase).

## Stress consequence on cooling
The unit cell that was cubic at high T becomes tetragonal with c/a ≈ 1.01 — an anisotropic shape change. In a polycrystalline ceramic this transformation produces:
1. **Internal stresses** of order 100 MPa range, depending on grain size and constraint.
2. **90° twin domains** to relieve those stresses: the c-axis direction alternates between adjacent twin lamellae, balancing strain.
3. **180° domain walls** that don't relieve strain but separate antiparallel polarization regions.
4. In **fine-grain ceramics (sub-200 nm)**, no 90° domain twins form because the grain is too small to nucleate them → **stress builds up and εr drops** (consistent with the εr collapse below 200 nm).

## Stress relief vs grain size
In **coarse-grained** ceramics: 90° domain walls nucleate readily, relieving shear stress. Twin patterns are visible by polarized-light or TEM.
In **dense nanocrystalline** ceramics: no room for 90° domains; stress is retained → tetragonal distortion is suppressed → c/a → 1 → **paraelectric-like dielectric response** even below "T_C".

This is the structural origin of the [[batio3]] grain-size collapse below ~200 nm: the ceramic isn't really tetragonal anymore (or only partially), so εr crashes.

## Domain pattern formation kinetics
Sub-100-µs domain formation right at the transition (essentially structural, not diffusive). Then slower relaxation of:
- Surface charge dynamics on freshly formed domains ([Phase Transition Effect on Ferroelectric Domain Surface Charge](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8398434/))
- Domain-wall wandering toward minimum-energy configuration ([[ferroelectric-domain-wall]])
- Aging: long-time domain re-orientation; basis of [[aging-class-2|Class II aging]]

## "Aging clock" reset
Heating above T_C **erases all domain structure**. Upon cooling back below T_C, a fresh domain pattern forms and the aging clock restarts at t=0. This is the basis of:
- Post-solder de-aging (parts re-aged after wave/reflow soldering)
- The "1 day or 24 h after last heat" reference time in vendor datasheets
- The Vishay 150 °C × 1 h thermal recovery from [[dc-bias-aging]]

## Core-shell complication
[[core-shell-batio3|Modern core-shell BaTiO₃ grains]] have a ferroelectric tetragonal **core** and a paraelectric cubic-like **shell**. The Curie transition only happens in the core. The shell stays paraelectric at all T in the operating range — that's where the **temperature stability** of X7R comes from, but also where most of the **non-ferroelectric εr** sits.

The thermal-expansion mismatch between the still-cubic shell and the now-tetragonal core during cooldown is **another stress source** at the grain interior level. This appears to feed back into the domain pattern formation ("the mismatch of thermal expansion coefficient between core and shell plays a crucial role in cubic to tetragonal phase transformation of BaTiO₃").

## Implications for the simulator
- The simulator must treat **bulk T_C** (≈ 120 °C) as the dividing line for Class II behavior. Above T_C: no aging, no DC-bias derating, εr peaks. Below: full Class II non-idealities.
- For modeling X8R / X8L (T_C shifted higher by Zr substitution or other dopants), T_C becomes a material parameter.
- Grain-size collapse of εr below 200 nm should be modeled as a sigmoid `εr(r̄) = εr_∞ / (1 + (r_crit/r̄)^p)` with r_crit ≈ 150 nm and p ≈ 4 — anchored to data points like 100 nm BaTiO₃ → εr ≈ 2551.

## Cross-references
- [[batio3]]
- [[curie-temperature]]
- [[ferroelectric-domain-wall]]
- [[core-shell-batio3]]
- [[aging-class-2]]
- [[dc-bias-aging]]
- [[grain-growth-dopant-pinning]]

## References
- [[arxiv-batio3-cubic-to-tetragonal-md]] — first-principles molecular dynamics study of the transition
- [[arxiv-batio3-domain-wall-motion]] — domain wall dynamics in tetragonal BaTiO₃
- Springer / Twinning in ferroelectric and ferroelastic ceramics: stress relief
- PMC 8398434 — Phase transition effect on ferroelectric domain surface charge dynamics
