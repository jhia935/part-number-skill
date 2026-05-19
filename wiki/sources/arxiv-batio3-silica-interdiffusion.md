---
title: "Nuzhnyy et al. — High-Frequency Dielectric Spectroscopy of BaTiO₃ Core/Silica Shell Nanocomposites (J. Adv. Dielectr. / arXiv 2011)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/arxiv-batio3-silica-interdiffusion.md
tags:
  - paper
status: complete
importance: medium
---

# Nuzhnyy et al. — BaTiO₃ Core / Silica Shell Nanocomposites & Interdiffusion

**Source:** `resources/literature/arxiv-batio3-silica-interdiffusion.md` (PDF: `resources/literature/pdf/arxiv-batio3-silica-interdiffusion.pdf`)
**Authors:** D. Nuzhnyy, J. Petzelt, V. Bovtun, M. Kempa, M. Savinov (Institute of Physics ASCR, Czech Republic); C. Elissalde, U-C. Chung, D. Michau, M. Maglione (CNRS Bordeaux); C. Estournès (CIRIMAT Toulouse)
**Venue:** *Journal of Advanced Dielectrics* (also posted on arXiv:1111.3738)
**Year:** 2011

## Summary

A spectroscopy study of **BaTiO₃ @ SiO₂ core-shell composite ceramics** using high-frequency dielectric spectroscopy (1 kHz to 10¹³ Hz, including THz and IR ranges). Three samples processed from the **same** silica-coated BaTiO₃ powder via three different sintering routes — **conventional sintering, spark plasma sintering (SPS), and two-step sintering** — to produce ceramics with different degrees of interdiffusion between core and shell.

The key finding: **interdiffusion between core and shell creates a strong interfacial polarization** detectable by high-frequency spectroscopy as additional dielectric loss in the THz-MW range. Effective-medium-approximation models with sharp boundaries can't reproduce the observed loss — the gradient interdiffusion layer is what's responsible.

## Process anchors
| Sintering route | Peak T | Hold | Pressure | Final density |
|---|---|---|---|---|
| Standard (S) | 600 °C | 2 h | none | 58 % (very low — porous) |
| SPS | 1000 °C | 15 min | 100 MPa | ~80 % |
| Two-step (TSS) | 1225 °C / 900 °C | 1 min / 12 h | none | 95 % |

The TSS sample showed clear fresnoite (Ba₂TiSi₂O₈) secondary-phase formation (XRD ratio fresnoite/BaTiO₃ ≈ 0.07 — "almost the whole shells transformed into fresnoite").

## Key physical insights

1. **The 5 nm SiO₂ shell** prepared by sol-gel (Stöber process derivative) provides a uniform coating on 500 nm Sakai BaTiO₃ powder — basis of the "soft chemistry route" to core-shell powders.
2. **Sintering route directly controls interdiffusion**: SPS preserves the most distinct core-shell boundary (fastest); two-step sintering with long hold induces fresnoite formation across the shell-core interface.
3. **High-frequency dielectric spectroscopy** is far more sensitive to interfacial polarization than conventional 1 kHz / 1 MHz measurements — engineers checking only at conventional frequencies can miss interdiffusion-induced changes.
4. **The dielectric loss at THz frequencies tracks the volume fraction of the interdiffusion gradient layer** — quantitative connection between processing and high-f loss.

## Implications for MLCC engineering
- For MLCC operation in the kHz-MHz range, interdiffusion-induced changes appear mostly as **modified εr at high T (near Curie peak)** and **modified dissipation factor**.
- Process control aimed at "preserving sharp core-shell boundaries" needs high-f spectroscopy (or TEM) to verify — not just standard LCR-bridge measurements.
- SPS produces the cleanest core-shell preservation but is impractical for production MLCC geometry.

## Concepts discussed
- [[core-shell-batio3]]
- [[core-shell-formation-mechanism]]
- [[sintering-aids-glass]]
- [[spark-plasma-sintering]]
- [[two-step-sintering]]
- [[dissipation-factor]]
- [[permittivity]]

## Entities mentioned
- Institute of Physics ASCR (Czech Academy)
- CNRS Bordeaux (ICMCB)
- CIRIMAT / Plateforme Nationale CNRS de Frittage Flash (Toulouse)
- Sakai Chemical (BaTiO₃ powder supplier — also Murata supplier)

## References
_Original source: `resources/literature/arxiv-batio3-silica-interdiffusion.md`_
