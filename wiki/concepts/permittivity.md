---
title: Permittivity (Dielectric Constant εᵣ)
type: concept
created: 2026-05-19
updated: 2026-05-19
sources: []
tags:
  - paper
---

# Permittivity (Dielectric Constant εᵣ)

The fundamental material property that determines **how much charge a dielectric can store per unit electric field**. Appears as the multiplier on every MLCC equation. The single biggest material design lever — most of MLCC chemistry exists to push εᵣ higher while keeping every other property (TCC, IR, breakdown V, aging) inside spec.

## Definition
The relative permittivity:
$$
\varepsilon_r \;=\; \frac{\varepsilon}{\varepsilon_0}
$$
where ε is the material's absolute permittivity and ε₀ = 8.854 × 10⁻¹² F/m is the vacuum permittivity. Dimensionless. Sometimes called the "dielectric constant K" — same thing.

Appears in the [[mlcc-capacitance-equation|MLCC capacitance equation]]:
$$
C \;=\; \varepsilon_r \cdot \varepsilon_0 \cdot \frac{A \cdot N}{d}
$$

## Physical origin (polarization mechanisms)
εᵣ measures how easily the material's charge structure polarizes in an applied field. **Four polarization mechanisms** contribute, each with its own characteristic time scale:

| Mechanism | Time scale | εᵣ contribution |
|---|---|---|
| **Electronic** (electron cloud distortion) | 10⁻¹⁵ s (UV) | small (εᵣ ~ 2–5) |
| **Ionic** (cation-anion displacement) | 10⁻¹² s (IR) | moderate (εᵣ ~ 5–50) |
| **Dipolar** (permanent dipole reorientation; ferroelectric domain motion) | 10⁻⁹ – 10⁻³ s | dominant in BaTiO₃ ferroelectrics (εᵣ 1000+) |
| **Space-charge / interfacial** (carriers piling up at GBs, electrodes) | 10⁻³ s – ∞ | dominant at low f for high-defect materials |

At MLCC operating frequencies (DC to ~100 MHz) all four contribute, but **dipolar (ferroelectric domain motion)** dominates for Class II/III. As frequency rises through ~1–10 GHz, dipolar response rolls off ([[ferroelectric-domain-wall|domain wall relaxation]]) and εᵣ drops to the ionic contribution.

## Typical εᵣ values for MLCC materials
| Material | εᵣ at 25 °C, 1 kHz, low field |
|---|---|
| Vacuum / air | 1.0 |
| Silicon dioxide (SiO₂) | 3.9 |
| Aluminum oxide (Al₂O₃) | 9–10 |
| [[cazro3]] (Class I BME C0G base) | 25–31 |
| BaNd-titanate (legacy PME C0G) | ~70 |
| Calcium-zirconium titanate hybrids | 50–200 |
| Pure [[batio3]] (single crystal at 25 °C) | ~ 1500–2000 |
| BaTiO₃ ceramic, 1 µm grain (no doping) | ~ 6000 (peak) |
| BaTiO₃ ceramic, 200 nm grain (X7R-engineered) | ~ 3000–4000 |
| BaTiO₃ ceramic at T_C | **~ 9000–15 000** (Curie peak) |
| Y5V / Z5U Class III formulations | 4000–18 000 |

## What makes εᵣ vary
Even for a single composition, εᵣ depends on:
- **Frequency**: drops at high f as polarization mechanisms can't keep up
- **Temperature**: peaks near [[curie-temperature|T_C]] for ferroelectrics, follows Curie-Weiss above
- **DC bias**: drops in ferroelectrics as DC field pins [[ferroelectric-domain-wall|domain walls]] → [[dc-bias-derating]]
- **AC drive amplitude**: small-signal εᵣ differs from large-signal effective εᵣ
- **Grain size**: collapses below ~200 nm in BaTiO₃ ([[batio3]])
- **Aging time**: drops logarithmically with time in Class II ([[aging-class-2]])
- **Pressure / strain**: piezoelectric coupling shifts εᵣ

## Complex permittivity & dielectric loss
In AC measurements:
$$
\varepsilon^* \;=\; \varepsilon' - j \varepsilon''
$$
- `ε'` = real part (the stored-charge εᵣ that goes into the capacitance equation)
- `ε''` = imaginary part (related to dielectric loss; see [[dissipation-factor]])
- `tan δ = ε'' / ε'` = dissipation factor (the standard datasheet spec)

## Implications for the simulator
The simulator needs εᵣ as a function of:
- material composition (dielectric class + dopants)
- operating point (V_DC, V_AC, T, f, time)
- microstructure (grain size, defect density)

This is exactly the multiplicative-factor decomposition in [[epci-high-cv-mlcc-bias-aging|`C_actual = C_rated · F_DCV · F_ACV · F_T · F_age`]] — each F-factor is a correction to the material's nominal εᵣ.

## Cross-references
- [[mlcc-capacitance-equation]]
- [[curie-temperature]]
- [[ferroelectric-domain-wall]]
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[dissipation-factor]]
- [[batio3]], [[cazro3]]
