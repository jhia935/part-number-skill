---
title: "Yu et al. — Electron Localization Enhances Cation Diffusion in Reduced ZrO₂, CeO₂ and BaTiO₃ (arXiv 2018)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/arxiv-electron-localization-cation-diffusion.md
tags:
  - paper
status: complete
importance: medium
---

# Yu et al. — Electron Localization Enhances Cation Diffusion in Reduced ZrO₂, CeO₂, BaTiO₃

**Source:** `resources/literature/arxiv-electron-localization-cation-diffusion.md` (PDF: `resources/literature/pdf/arxiv-electron-localization-cation-diffusion.pdf`)
**Authors:** (DFT computation team)
**Venue:** arXiv:1808.05198, 2018

## Summary

First-principles DFT explanation for the long-observed experimental fact that **reducing atmospheres accelerate grain growth in oxide ceramics** — including BaTiO₃. The conventional explanation (more oxygen vacancies → more diffusion paths) is qualitatively right but incomplete. This paper shows that the **electron localization on reduced cations** (Ti⁴⁺ → Ti³⁺) lowers the cation migration barrier by ~ 30–50 %, providing a multiplicative speed-up on top of the vacancy concentration increase.

## Key findings (BaTiO₃-specific)

- Migration of Ti⁴⁺ vs Ti³⁺ next to an oxygen vacancy V_O is studied in cubic BaTiO₃ (DFT supercell 27 Ba + 27 Ti + 81 O).
- Reduced Ti³⁺ is **larger** (0.67 Å vs 0.61 Å for Ti⁴⁺) — counterintuitively, larger ions in this system have lower migration barrier because of better electrostatic screening by the localized electron.
- Synergistic effect: V_O next to Ti **further** lowers the migration barrier (vacancy provides a hopping site).
- Net result: in reducing atmosphere, Ti diffusion is 1–2 orders of magnitude faster than in oxidizing atmosphere at the same T.

## Implications for BME MLCC sintering
1. **BaTiO₃ grain growth is faster in BME (reducing) firing than in PME (air) firing** — a real concern for fine-grain control.
2. The dopant package (Y + Mg + rare earths) compensates by:
   - **Reducing oxygen vacancy concentration** through acceptor-donor pairing
   - **Trapping V_O at grain boundaries** so they can't catalyze grain-interior cation hopping
3. Re-oxidation anneal after main sintering not only fixes V_O but also **re-oxidizes Ti³⁺ → Ti⁴⁺**, locking grain size in.
4. Modern BME atmosphere recipes (steep PO₂ ramp, fast heating through coarsening window) are physically optimized to limit the time spent in the "reduced + slow" regime.

## Concepts discussed
- [[defect-chemistry-batio3]]
- [[sintering-kinetics-batio3]]
- [[grain-growth-dopant-pinning]]
- [[bme-sintering-atmosphere]]
- [[oxygen-vacancy-migration]]

## References
_Original source: `resources/literature/arxiv-electron-localization-cation-diffusion.md`_
