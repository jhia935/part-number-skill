---
title: Polarization Mechanisms in Dielectrics
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources:
  - arxiv-batio3-domain-wall-motion.md
tags:
  - paper
---

# Polarization Mechanisms in Dielectrics

The four physical processes by which a dielectric responds to an applied electric field — collectively determining [[permittivity|εᵣ]] and its frequency dependence. Each has its own characteristic time scale, and together they explain why the same MLCC dielectric behaves differently at DC vs 1 kHz vs 1 MHz vs 1 GHz.

## The four mechanisms

### 1. Electronic polarization
**Time scale**: ~10⁻¹⁵ s (UV-visible). Universal, present in every material.
The electron cloud of every atom displaces slightly in the field direction, opposite the nucleus. Tiny dipole moment per atom. Contributes εᵣ ~ 2–5 in vacuum-like media and is the only mechanism in noble-gas insulators.

### 2. Ionic (atomic) polarization
**Time scale**: ~10⁻¹² s (infrared). Present in ionic crystals.
Cations and anions in the lattice displace in opposite directions under the field. In BaTiO₃ this is the **Ti⁴⁺ off-center displacement** that creates the spontaneous polarization below T_C. The infrared phonon modes carry this polarization. Contributes εᵣ ~ 5–50 in ordinary ionic oxides.

### 3. Dipolar (orientational) polarization
**Time scale**: 10⁻⁹ – 10⁻³ s, depending on system. Dominant in ferroelectrics and polar liquids.
**For BaTiO₃**: each tetragonal unit cell has a permanent dipole. The dipoles are organized into [[ferroelectric-domain-wall|domains]]; on applying an external field, domains with parallel alignment grow at the expense of misaligned ones, and within each domain dipoles wobble around their axes. **This is where most of the εᵣ in Class II MLCCs comes from** — see [[arxiv-batio3-domain-wall-motion|Gurung et al. 2024]].
For polar liquids (water, alcohols), it's the molecular dipole reorientation.
Contributes εᵣ 1000+ in ferroelectric BaTiO₃; 80 in liquid water; 0 in symmetric molecules / non-ferroelectric crystals.

### 4. Space-charge (interfacial / Maxwell-Wagner) polarization
**Time scale**: 10⁻³ s – seconds, depending on conductivity contrast.
Free charge carriers (electrons, ions) drift in the field and pile up at interfaces — grain boundaries in a polycrystalline ceramic, or electrode-dielectric interfaces. Once piled up, they shield the field from the bulk → appears as additional polarization. Very slow because mobility is limited.
Contributes large εᵣ at low frequency in high-defect or high-leakage materials.

## εᵣ as the sum
$$
\varepsilon_r(\omega) \;=\; \varepsilon_\text{electronic} \;+\; \varepsilon_\text{ionic} \;+\; \varepsilon_\text{dipolar}(\omega) \;+\; \varepsilon_\text{space-charge}(\omega)
$$
The first two are essentially frequency-independent up to their respective phonon / electronic resonances. The latter two are frequency-dependent, with **εᵣ rolloffs** at the inverse of their characteristic time:
- Dipolar in BaTiO₃: rolloff in the GHz range (10 GHz for 180° DW motion per [[arxiv-batio3-domain-wall-motion]]).
- Space-charge: rolloff in the kHz–MHz range.

## The MLCC datasheet εᵣ frequency curve
| f | dominant contributions | εᵣ |
|---|---|---|
| DC – 1 kHz | electronic + ionic + dipolar + space-charge | maximum |
| 1 kHz – 1 MHz | electronic + ionic + dipolar (space-charge rolling off) | mostly flat for clean parts |
| 1 MHz – 1 GHz | electronic + ionic + dipolar | dipolar starts rolling off |
| > 1 GHz | electronic + ionic only | drops to ~ ionic value (~ 100–500 for BaTiO₃) |

This is why the same nominal "X7R 10 µF" looks different in a 100 kHz buck-converter loop vs in a 1 GHz signal-integrity simulation: the εᵣ at the relevant frequency is different.

## Why DC bias kills εᵣ (mechanism)
Applied DC field **pins the dipolar polarization** in the field direction. Domain walls can no longer freely wobble around equilibrium → dipolar εᵣ drops to near zero. Only electronic + ionic remain → εᵣ drops from 3000 to ~100. This is the physics behind [[dc-bias-derating]] and the explanation for the f_VCC sigmoid in `simulator-model.md`.

## Cross-references
- [[permittivity]]
- [[batio3]]
- [[ferroelectric-domain-wall]]
- [[dc-bias-derating]]
- [[curie-temperature]]
- [[arxiv-batio3-domain-wall-motion]]
