---
title: Ni Electrode Paste Formulation for BME MLCC
type: concept
created: 2026-05-21
updated: 2026-05-21
sources:
  - sugimura-hirao-2009-batio3-additive-ni-electrode.md
  - polotai-2007-cr-doping-ni-electrode-mlcc.md
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
tags:
  - paper
status: complete
importance: high
---

# Ni Electrode Paste Formulation for BME MLCC

The screen-printing paste that becomes the inner Ni electrode in a finished BME MLCC. A typical industrial Ni paste is engineered along five axes:
1. **Ni powder** — size, shape, surface chemistry.
2. **Dielectric (BT) additive** — size, mass%, dispersion.
3. **Refractory-metal alloy** — Cr, V, Mo, Re for interfacial chemistry.
4. **Organic vehicle** — solvent, binder, dispersant, rheology modifiers.
5. **Anti-oxidation additives** — protect Ni during the BBO → reducing transition.

Each axis trades off **rheology** (printability), **shrinkage** (cofiring stress), **continuity** (electrode coverage after sintering), and **conductivity** (final resistance).

## Reference recipe (industry-typical, [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis]])

| Component | Loading | Role |
|---|---|---|
| Ni powder (~0.2 µm PVD) | 55 vol% | The conductive metal |
| BaTiO₃ nano-additive (30 nm) | 7 wt% of Ni, ≈ 5–10 vol% of paste | Shrinkage retardation + oxidation protection |
| Terpineol (solvent) | 41 vol% | Carrier for screen-printing rheology |
| Resin (binder) | 4 vol% | Green-paste cohesion before drying |

After printing, drying, and BBO removal of organics, the green Ni electrode is **~1.2 µm thick** ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan]] for 0603/1206 SEMCO samples).

## Axis 1: Ni powder

### Particle size
| Era | Ni powder size | Dielectric layer | Notes |
|---|---|---|---|
| Legacy (PME 1980s) | 1–3 µm | 5–15 µm | Pd / Ag-Pd electrodes |
| Early BME (1990s–2000s) | 0.4 µm | 2–3 µm | First-generation Ni-MLCC |
| Modern BME (2010s+) | **0.1–0.3 µm** | **0.5–1.0 µm** | Submicron Ni from CVD or PVD; modern thin-layer parts |
| Cutting-edge (2020s) | ~0.05 µm | ~0.4 µm | High-V_cv parts; Murata, SEMCO |

Smaller Ni → faster sintering, lower onset T → need stronger additive retardation to keep shrinkage curve matched to BT.

### Shape and surface
- **Spherical Ni** (PVD route, e.g., Shoei Chemical Tokyo): preferred for printability and uniform packing.
- **Filamentary or irregular Ni**: worse packing, more anisotropic shrinkage.
- **Surface oxide layer** (NiO native, ~2–5 nm): must be controlled — too much gives a buffer against early oxidation but raises contact resistance; too little risks fast Ni oxidation during BBO.

### Bimodal distribution
A mix of two Ni size populations (e.g., 0.2 µm + 50 nm) can tighten the shrinkage curve, raise green density, and improve electrode continuity. Used by several Japanese suppliers.

## Axis 2: BaTiO₃ nano-additive

The dominant tool for retarding Ni sintering. From [[sugimura-hirao-2009-batio3-additive-ni-electrode|Sugimura-Hirao 2009]] and [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan DEM]]:

| Loading (mass% of Ni) | BT size | Effect |
|---|---|---|
| 0 | — | Catastrophic Ni break-up at peak T |
| 5 | 30–60 nm | Marginal; some retardation |
| **10** | **30 nm** | **Industry sweet spot — > 75 % Ni film coverage** |
| 10 | 50–100 nm | Insufficient retardation; need higher mass% |
| 15 | 30 nm | Diminishing returns; conductivity starts dropping |
| 20+ | 30 nm | Percolation threshold approached; resistance rises |

**Smaller is dramatically better per gram**. The DEM result from Yan Ch. 6:
- 20 vol% / 60 nm BT in Ni → retarding factor **7×** at D = 0.70.
- 20 vol% / 300 nm BT in Ni → retarding factor only **2×**.

**Dispersion matters too**: agglomerated nano-BT loses most of the retardation benefit — well-dispersed inclusions are required.

The BT additive matches the dielectric BT composition (same dopant blend, same RE-doped core-shell formulation) so that as Cr/Mn/Y diffuse from the additive into the surrounding dielectric they reinforce rather than degrade the [[core-shell-batio3|core-shell]] chemistry.

## Axis 3: Refractory-metal dopants

Modify interfacial chemistry **without changing the shrinkage curve** ([[polotai-2007-cr-doping-ni-electrode-mlcc|Polotai 2007]]).

| Dopant | Typical loading | Mechanism | Trade-off |
|---|---|---|---|
| **Cr** | 0.5–1.5 wt% | Segregates to Ni/BT interface; chemically suppresses the (Ni, Ba, Ti) liquid alloy → reduces Rayleigh-Plateau break-up at peak T | Cr diffuses into BT and creates V_O → modest IR penalty |
| V | 0.5–2 wt% | Similar interfacial segregation effect; less aggressive on BT defect chemistry than Cr | Slightly weaker continuity improvement |
| Mo | 0.5–1 wt% | High-melting refractory; suppresses Ni grain coarsening at peak T | Reduces electrode conductivity slightly |
| Re | 0.3–1 wt% | The most refractory option; Re segregates without diffusing into BT | Expensive; mostly research-stage |

A typical premium BME paste uses **both** a nano-BT additive (shrinkage retardation) and a small Cr or V loading (interfacial chemistry). The two levers are independent and additive.

## Axis 4: Organic vehicle

The printable wet paste is ~50 vol% solids + ~50 vol% organics. Components:

| Component | Typical wt% of paste | Role |
|---|---|---|
| Terpineol (or texanol, butyl carbitol acetate) | 30–45 % | Primary solvent; evaporates during drying |
| Ethyl cellulose | 1–5 % | Binder for green-paste cohesion |
| Polymeric dispersant | 1–3 % | Stabilizes Ni-BT suspension against agglomeration |
| Rheology modifier (e.g., polyacrylate) | 0.5–2 % | Tunes thixotropy for screen-printing |

The organic vehicle must:
- Evaporate cleanly between drying (60–100 °C) and BBO (250–500 °C).
- Not leave carbon residue that could oxidize Ni.
- Match the wetting behavior of the dielectric green tape so the printed pattern is sharp.

## Axis 5: Anti-oxidation additives

BBO happens at 200–600 °C in a **mildly oxidizing** atmosphere (Ar + 1 % O₂) — see [[binder-burnout-debinding]] and [[bme-sintering-atmosphere]]. The Ni is exposed to oxygen at exactly the temperature where Ni → NiO is thermodynamically favored. Two strategies:

1. **Nano-BT coating** ([[sugimura-hirao-2009-batio3-additive-ni-electrode|Sugimura-Hirao]]) — the BT additive physically coats Ni grains, raising effective oxidation onset by 100–200 °C.
2. **Reducing organic vehicle** — some pastes use reducing-agent additives (e.g., polyols) that scavenge O₂ during BBO.

## Paste shrinkage curve

A free-paste pellet (without dielectric constraint) sintered in reducing atmosphere shows:
- Onset T: ~450 °C (for ~0.2 µm Ni with no additive); ~600–700 °C with 10 mass% nano-BT.
- Max-rate T: ~900 °C without additive; ~1000 °C with additive.
- Final density: ~95 % theoretical Ni density.
- Total linear shrinkage: ~25–35 % for high-organic-vehicle paste, less for low-organic / pressed pellets.

This curve is the input to the [[skorohod-olevsky-viscous-sintering|SOVS]] model for the bilayer / multilayer constrained-sintering prediction.

## Implications for the simulator

A simulator that takes "Ni paste recipe" → "shrinkage trajectory" needs at minimum:

| Input | Determines |
|---|---|
| Ni particle size | Shrinkage onset T, max-rate T |
| Ni vol% in dried paste | Green density, fired density, final conductivity |
| BT additive size + mass% | Retarding factor (looks up the [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan]] table) |
| Refractory-metal dopant flag | Continuity-improvement flag (independent of shrinkage) |
| Print thickness | h_Ni in the bilayer model |

These map directly into `η_Ni(T)`, `ρ_g,Ni` in the SOVS or simpler Bordia-Scherer model.

## Cross-references

- [[metal-electrode-shrinkage-effect]] — the parent concept.
- [[ni-batio3-cosintering-interface]] — what happens at the Ni/BT interface at peak T.
- [[bordia-scherer-composite-sintering]] — analytical retardation framework.
- [[skorohod-olevsky-viscous-sintering]] — full continuum model.
- [[cu-electrode-mlcc]] — Cu paste analogue.
- [[binder-burnout-debinding]] — BBO oxidation challenge.
- [[bme-sintering-atmosphere]] — reducing-atmosphere requirement.

## References

- [[sugimura-hirao-2009-batio3-additive-ni-electrode]] — empirical 30 nm / 10 mass% sweet spot.
- [[polotai-2007-cr-doping-ni-electrode-mlcc]] — Cr-1 wt% interfacial-chemistry effect.
- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — quantitative DEM retardation curves.
- Kang, Joo, Cha, Jung, Paik, "Shrinkage behavior and interfacial diffusion in Ni-based internal electrodes with BaTiO₃ additive", *Ceram. Int.* 34 (2008) 1487 — independent confirmation.
