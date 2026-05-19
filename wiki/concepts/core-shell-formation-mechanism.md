---
title: Core-Shell Formation Mechanism (Sintering Kinetics)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - arxiv-batio3-silica-interdiffusion.md
tags:
  - paper
---

# Core-Shell Formation Mechanism

How the core-shell grain architecture **actually emerges** during MLCC firing is a debated question in the literature. Two competing pictures:

1. **Solid-state diffusion**: dopants Fickian-diffuse from the particle surface into the BaTiO₃ grain interior, creating a concentration gradient.
2. **Dissolution-reprecipitation**: small, dopant-rich BaTiO₃ particles dissolve into a transient liquid (often Mg-Ti-O eutectic or [[sintering-aids-glass|glass-aid]]-derived), then re-precipitate as a doped shell on larger, surviving cores.

The modern consensus (Jeon JACerS 2012, Chen JACerS 2020) is that **dissolution-reprecipitation dominates** in high-dopant-loading commercial systems, while pure diffusion contributes more at moderate loading.

## The dissolution-reprecipitation picture (Jeon 2012)

```
Starting state:                Mixing:                       Sintering:
─────────────────              ─────────────────             ─────────────────
large undoped     +            small dopant-rich            cores grow with
BaTiO₃ particles  +   →  →  →  particles uniformly   →  →   doped shells from
(100-300 nm)                   coating them                  redissolved fines
small dopant-     →
rich BaTiO₃                    (or dopant in
particles (<50 nm)             liquid phase)
```

### Evidence
1. **Shell thickness depends on milling time**, not on heat-treatment time, in some studies. Long milling produces more "fines" → more material to redissolve → thicker shells.
2. **Core size is roughly constant** regardless of total milling/sintering schedule — i.e., the core is the largest starting particle.
3. STEM-EDS shows **sharp** rather than gradual dopant concentration steps at the core-shell boundary — inconsistent with pure Fickian diffusion (which gives smooth gradients).
4. Without a transient liquid phase (or sintering aid forming one), core-shell formation is much slower.

### Kinetic window
For core-shell to form **and survive** through sintering:
- Sintering time must be **long enough** for dissolution-reprecipitation but **short enough** that subsequent interdiffusion doesn't smear the shell back into the core.
- Sintering temperature must be **above** the transient-liquid eutectic but **below** the temperature where rapid grain-interior diffusion homogenizes the system.
- Reference recipe (Chen JACerS 2020): BaTiO₃ particles > 100 nm, sintering 0.5–2.0 h at peak T → core-shell retained.

## The solid-state diffusion picture
At moderate dopant loadings (< 0.5 mol%) and longer sintering times (> 4 h), solid-state diffusion contributes more:
- Rare-earth ions diffuse from the GB into the grain along oxygen vacancy migration paths.
- The shell thickness grows as `√(D·t)` (Fickian).
- The concentration gradient is smooth, not stepped.

For commercial high-rel BME parts at the 0.5–2 mol% loading range and 1–2 h sintering, **both mechanisms operate simultaneously** — dissolution-reprecipitation does most of the "shell creation" work and Fickian diffusion fine-tunes the boundary smoothness.

## Interdiffusion (the unwanted consequence)
If sintering is **too hot or too long**, the dopant diffuses **past the shell into the core**, washing out the gradient. The ceramic ends up homogeneous — and **loses the X7R temperature-stability advantage**.

[[arxiv-batio3-silica-interdiffusion]] (BaTiO₃ @ SiO₂ nanocomposites) shows that interdiffusion creates **strong interfacial polarization** — a third εr contribution between the well-defined core and shell phases. High-frequency dielectric spectroscopy (THz / IR range) is sensitive enough to detect this; conventional 1 kHz / 1 MHz measurements are not.

The competing process kinetics:
- Liquid-phase sintering / dissolution-reprecipitation: 1100–1300 °C, minutes to ~ 1 h
- Solid-state interdiffusion: ~ 1300 °C, hours

**The window for "good core-shell" is narrow.** Modern sintering profiles ([[sintering-profile-mlcc]]) are explicitly engineered to be in the liquid-phase regime briefly, then ramp down before interdiffusion takes over.

## Special case: BaTiO₃ @ SiO₂
SiO₂-coated BaTiO₃ during firing **forms fresnoite (Ba₂TiSi₂O₈)** as a secondary phase at the core-shell interface. If the heat treatment is engineered carefully, fresnoite can be **suppressed** to preserve the amorphous SiO₂ shell — or **promoted** to create a graded ceramic-Si phase distribution ([[arxiv-batio3-silica-interdiffusion]]).

## Process levers for core-shell control
| Lever | Effect on shell thickness | Effect on interdiffusion |
|---|---|---|
| Peak sintering T | Higher → thicker shell **and** more interdiffusion | Higher → more |
| Hold time at peak | Longer → thicker shell then thinner via interdiffusion | Longer → more |
| Heating rate | Faster → less time for both | — |
| Dopant loading | Higher → thicker shell | — |
| Dopant particle size | Smaller → faster dissolution → thicker shell | — |
| Ba/Ti stoichiometry | Slight Ba-excess favors B-site, slower diffusion | — |
| Sintering aid presence | Lower-T liquid → faster shell formation | Lower-T = less interdiffusion |

## Implications for the simulator
The simulator's `f_VCC(E)` sigmoid, `f_T(T)` temperature curve, and `E_k` reliability activation energy are all downstream of **shell ratio and shell composition**, which are determined by **firing recipe** and **dopant chemistry**. Two parts with the same nominal "X7R 10 µF" can have wildly different behaviors if their sintering recipes produced different shell ratios.

This is why the BME competitor variation in [[dc-bias-aging|DC-bias-aging]] (Vishay's 5 %/decade vs competitors' 20–30 %/decade per [[vishay-x7r-cap-drift-dc-bias]]) is most plausibly due to **different core-shell shell quality**, not just different bulk chemistry.

## Cross-references
- [[core-shell-batio3]]
- [[dopant-site-occupancy-batio3]]
- [[dopant-powder-coating]]
- [[sintering-kinetics-batio3]]
- [[sintering-profile-mlcc]]
- [[sintering-aids-glass]]
- [[grain-growth-dopant-pinning]]

## References
- Jeon et al., "The Mechanism of Core/Shell Structure Formation During Sintering of BaTiO₃-Based Ceramics", *J. Am. Ceram. Soc.* 95:8 (2012) 2435–2440.
- Chen et al., "The role of diffusion behavior on the formation and evolution of the core-shell structure in BaTiO₃-based ceramics", *J. Am. Ceram. Soc.* 103 (2020).
- [[arxiv-batio3-silica-interdiffusion]] — high-frequency spectroscopy of interdiffusion.
- An et al., *Adv. Mater.* 2026 — grain-boundary segregation as design lever.
