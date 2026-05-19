---
title: Calcium Zirconate (CaZrO₃)
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - escies-bme-mlcc-high-reliability.md
  - rohm-ceramic-cap-app-note.md
tags:
  - material
status: complete
importance: high
---

# Calcium Zirconate (CaZrO₃)

A paraelectric perovskite oxide. The base dielectric for **modern BME C0G** MLCCs ([[bme-c0g]]), as well as the textbook example of a low-loss linear Class I material.

## Crystal & dielectric properties
- Orthorhombic (Pnma) perovskite at room temperature; transitions at high temperature.
- **No ferroelectric transition** in the relevant range — fully **paraelectric** behavior; no domains, no DWs, no hysteresis, **no [[aging-class-2|aging]], no [[dc-bias-derating|DC bias derating]], no piezoelectricity / electrostriction**.
- Modest `εr` ≈ 25–31 (vs BaTiO₃ Class II 600–6000).
- Tightly-bound oxygen in the lattice → reduction-resistant. Makes [[bme-vs-pme|BME]] firing tractable without strong reoxidation requirement.

## Why CaZrO₃ wins Class I BME
[[escies-bme-mlcc-high-reliability]] documents:
- BME C0G with CaZrO₃: εr ≈ 31, dielectric thickness 7.0 µm achievable.
- Legacy PME C0G with BaNd-titanate (BNT): εr ≈ 70, dielectric thickness 11.6 µm.
- For the same case-size and rated V, BME C0G (CaZrO₃) gives higher cap because of thinner d and more layers — **2× thinner, more than 13× longer HALT MTTF** at 175 °C / 400 V.
- BME C0G has **higher IR at high T** (>120 °C, IR even rises) — direct consequence of the wide-band-gap and tight O-binding.

## Compositional tailoring
CaZrO₃ is rarely used neat in commercial parts. Typical Class I formulations are CaZrO₃-based with:
- Small substitutional doping at Ca or Zr sites for shifting the temperature coefficient
- Glass formers (SiO₂, B₂O₃) as sintering aids
- Mn / acceptor for charge compensation under reducing-atmosphere firing
The temperature coefficient can be tuned from C0G (≈ 0 ppm/°C) through P/R/S/T/U-classes (−150 to −750 ppm/°C) by composition adjustment.

## See also
- [[bme-c0g]] — KEMET's flagship CaZrO₃-based product
- [[batio3]] — the Class II/III ferroelectric counterpart
- [[eia-rs-198-dielectric-classes]] — letter code system
- [[bme-vs-pme]]
