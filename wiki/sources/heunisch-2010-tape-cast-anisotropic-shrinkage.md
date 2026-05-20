---
title: "Heunisch, Dellert, Roosen — Powder/Binder/Process Effect on Anisotropic Shrinkage in Tape-Cast Ceramics (JECS 2010)"
type: source
created: 2026-05-20
updated: 2026-05-20
sources:
  - resources/literature/heunisch-dellert-roosen-2010-anisotropic-shrinkage.md
tags:
  - paper
status: complete
importance: high
---

# Heunisch, Dellert, Roosen — Anisotropic Shrinkage in Tape-Cast Ceramics (JECS 2010)

**Source:** `resources/literature/heunisch-dellert-roosen-2010-anisotropic-shrinkage.md` (WebFetch-extracted summary from academia.edu; publisher PDF paywalled)
**Authors:** Andreas Heunisch, Armin Dellert, Andreas Roosen (Erlangen-Nürnberg)
**Journal:** *Journal of the European Ceramic Society* 30 (2010) 3397–3406
**DOI:** 10.1016/j.jeurceramsoc.2010.08.012

## Summary

A clean designed-experiment paper that **factorially varied powder shape, binder MW, and casting parameters** to identify which lever dominates anisotropic shrinkage in tape-cast alumina. Three alumina powders (platelet, standard, spherical) with similar d₅₀ (3.8–4.2 µm) were tested with three PVB binders (19, 40–70, and 120–150 × 10³ g/mol). Blade gap (150, 450 µm) and casting speed (10, 50, 250 mm/s) were also varied.

**Headline result: particle morphology dominates shrinkage anisotropy.** Binder MW and casting speed have only minor effects within tested ranges.

## Key quantitative findings

### Shrinkage anisotropy factor K_xy

| Powder shape | K_xy (avg) | Notes |
|---|---|---|
| Platelet (CL 3000) | **12.7** | Strong shape-induced anisotropy |
| Standard (WRA FG) | 8.4 | Moderate anisotropy |
| Spherical (DAW 05) | **1.9** | Near-isotropic, the dream case |

### Directional shrinkage values

| Direction | Range |
|---|---|
| In-plane casting direction (x) | 2.7–3.9% |
| In-plane transverse direction (y) | 3.0–4.0% |
| Thickness (z), 150 µm blade gap | ~11% |
| Thickness (z), 450 µm blade gap | ~6% |

**Thickness shrinkage is 2–4× the in-plane shrinkage**, and gets larger as the blade gap (thus the wet-tape thickness) gets smaller. The mechanism is particle alignment in the casting shear field — particles orient flat-side-down, so densification has more room in the through-thickness direction.

### Standard slurry composition (wt%)

| Component | wt% |
|---|---|
| Al₂O₃ powder | 63.87 |
| Solvent (ethanol/toluol) | 25.65 |
| Dispersant | 1.28 |
| Binder (PVB) | 4.73 |
| Plasticizer | 4.47 |

Plasticizer/binder ratio ≈ 0.95 (close to the optimum of 1.0 found in other studies).

### Particle orientation
- Platelet tapes: 70% of particles aligned within ±30° of casting direction
- Standard tapes: 62% aligned
- Spherical tapes: orientation is undefined, hence the K_xy → 1 result

### Green density
- 52–66% of theoretical Al₂O₃ density depending on powder + binder combination.

## Implication for MLCC dielectric tape design

The conclusion translates almost directly to BaTiO₃ MLCC dielectric tape:
1. **Choose pseudo-spherical or equiaxed BT powder** if dimensional accuracy in plane matters. Hydrothermally synthesized BT comes close. Solid-state-milled BT can be irregular and induce anisotropy.
2. **Don't over-tune the binder MW** for shrinkage; the powder shape budget is bigger.
3. **Thinner tapes shrink more in thickness** — for sub-µm green layers in modern MLCC, plan on z-shrinkage being the dominant direction and design layer count + cover thickness around the post-sinter `H`.

This is the cleanest experimental confirmation in the literature that **green-sheet shrinkage anisotropy is set primarily by powder morphology, secondarily by tape thickness, and only weakly by binder choice**.

## Entities mentioned
- (none — paper is generic alumina materials science, no named products)

## Concepts discussed
- [[green-tape-shrinkage-anisotropy]] — direct topic of the paper.
- [[binder-burnout-debinding]] — slurry composition includes PVB binder; debinding stage was not the focus.
- [[constrained-sintering-mlcc]] — paper studies *free* sintering of tapes; constrained sintering would amplify the anisotropy further.

## Notable quotes

> "Particle morphology has the predominant effect on shrinkage anisotropy."

> "Binder molecular weight has only minor influence within the tested ranges."

## References

_Original publication: Heunisch, Dellert, Roosen, J. Eur. Ceram. Soc. 30 (2010) 3397–3406. doi:10.1016/j.jeurceramsoc.2010.08.012_
