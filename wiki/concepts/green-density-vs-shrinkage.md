---
title: Green Density vs Sintering Shrinkage
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - hagymasi-ltcc-ferrite-dielectric-cofiring.md
  - heunisch-2010-tape-cast-anisotropic-shrinkage.md
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
tags:
  - paper
status: complete
importance: high
---

# Green Density vs Sintering Shrinkage

For a powder compact that sinters to a given final density (typically ≥ 95 % theoretical), the **total linear shrinkage** required is fixed by **the gap between the green density and the final density**. Higher green density → less shrinkage required → less anisotropy, less stress, less risk of cracking.

This is the single most important process knob in tape-cast ceramic dimensional control: **double the green density (or anywhere in between), and you halve the shrinkage**.

## The volume relation

Mass is conserved during sintering. If `ρ_g` is the green relative density and `ρ_f` is the fired relative density, then:
$$
\rho_g V_g = \rho_f V_f
\quad\Rightarrow\quad
\frac{V_f}{V_g} = \frac{\rho_g}{\rho_f}
$$

For isotropic free sintering, `V_f / V_g = (L_f / L_g)^3`, so the **linear shrinkage** is:
$$
\frac{L_g - L_f}{L_g} = 1 - \left(\frac{\rho_g}{\rho_f}\right)^{1/3}
$$

## Quick numerical reference

Assuming `ρ_f = 0.99` (fully dense), the linear shrinkage as a function of green density:

| ρ_g (relative) | ρ_g / ρ_f | Linear shrinkage |
|---|---|---|
| 0.45 | 0.455 | **23.0 %** |
| 0.50 | 0.505 | 20.5 % |
| 0.55 | 0.556 | 17.8 % |
| 0.60 | 0.606 | 15.0 % |
| 0.65 | 0.657 | 12.0 % |
| 0.70 | 0.707 | 8.9 % |
| 0.75 | 0.758 | 5.4 % |
| 0.80 | 0.808 | 2.0 % |

(For free isotropic sintering. Real-world numbers shift due to anisotropy, residual porosity, and binder + drying contributions.)

## Real-world validation: Hagymási LTCC data

From [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási]]:

| Tape | Green density | Predicted linear (free) | Measured linear (free, x/y/z) |
|---|---|---|---|
| DuPont 951 AT (DT) | 72 % | ~10 % | 12.7 / 13.9 / 12.8 % |
| BaFe₁₂O₁₉ (FT) | 53 % | ~19 % | 23.2 / 23.2 / 21.7 % |

The measured values are **systematically higher** than the volume-conservation prediction because:
1. Drying shrinkage (binder + solvent contraction before firing) adds 2–4 %.
2. Burnout shrinkage (organic vol% removal) adds 1–3 %.
3. Anisotropy from particle alignment redistributes thickness vs in-plane.

But the **ratio of FT to DT shrinkage** (~1.8×) is exactly the ratio of `(ρ_g,DT / ρ_g,FT)^(1/3) ≈ 1.11` × (1 + drying/binder corrections) ≈ 1.8. The green density is the dominant factor.

## Why FT has lower green density

Hagymási attributes the FT tape's 53 % green density to its **18 wt% organic content** (binder + plasticizer + dispersant). For comparison, DT's organic content is 11.4 wt%. More organic vol% in the green tape → less powder vol% → lower green density → more shrinkage.

This is the **engineering link between binder content and shrinkage**:

> Higher binder content → lower green density → more sintering shrinkage required to reach the same fired density.

A direct quantitative relationship.

## The Roosen-Heunisch corollary on shape

[[heunisch-2010-tape-cast-anisotropic-shrinkage|Heunisch 2010]] measured green tape density as a function of **powder shape** at fixed binder content:

| Powder shape | Green tape density (% theoretical) |
|---|---|
| Spherical | **66 %** (high — closest packing) |
| Standard (irregular) | 59–62 % |
| Platelet | **52 %** (lowest — poor packing) |

So powder shape affects shrinkage **two ways**:
1. Directly through anisotropy (platelet → high K_xy).
2. Indirectly through green density (platelet → low ρ_g → more total shrinkage).

Both reinforce the conclusion that **pseudo-spherical BT powder is preferred** for MLCC dielectric tape, because it gives high green density AND low anisotropy.

## Counter-mechanism: pre-sintered powder

If you **pre-calcine** the dielectric powder before tape casting (or use a mixture of fully sintered + green powder), the effective green density rises and total shrinkage drops. This is a niche LTCC trick that has been studied for ultra-low-shrinkage tapes (~3 %), though it complicates [[ni-batio3-cosintering-interface|electrode continuity]] in MLCC.

## Pressure during lamination

Higher lamination pressure raises green density. Hagymási reports:
- Green tape density (no lamination): 2.17 g/cm³
- Laminated density (after 80 °C, 25 MPa, 10 min): 2.25 g/cm³

A ~4 % rise — modest but measurable. In industry, lamination pressure is usually picked to maximize green density without delaminating the layers or smearing the electrodes; values of 10–50 MPa are typical for MLCC.

## Implication for the simulator

The total green-to-fired linear shrinkage `s_total` is well-approximated by:
$$
s_\text{total} \approx s_\text{drying} + s_\text{burnout} + s_\text{sinter}
\approx \underbrace{(2-4\%)}_\text{drying} + \underbrace{(1-3\%)}_\text{burnout} + \underbrace{\left[1 - (\rho_g / \rho_f)^{1/3}\right]}_\text{sinter}
$$

For a typical BME MLCC dielectric tape with `ρ_g ≈ 0.60` and `ρ_f ≈ 0.97`:
- Sinter contribution: `1 - (0.60/0.97)^(1/3)` = **14.5 %**
- Plus 3 % drying + 2 % burnout: **~19 % total free linear shrinkage**

That number rises if `ρ_g` drops (high-binder paste or coarse powder) and falls if `ρ_g` rises (well-packed spherical powder, pre-calcined powder).

In practice, MLCC chip-level fired shrinkage is **~12–15 %** because of constrained sintering — the laminated stack constrains lateral shrinkage and the thickness absorbs the difference (per [[constrained-sintering-mlcc]] and [[skorohod-olevsky-viscous-sintering]]).

## Cross-references

- [[green-tape-shrinkage-anisotropy]] — anisotropy under fixed green density.
- [[constrained-sintering-mlcc]] — how stack constraint redistributes the shrinkage budget.
- [[binder-burnout-debinding]] — how binder content sets green density.
- [[skorohod-olevsky-viscous-sintering]] — `ρ_g` is the initial condition for the FE model.
- [[hagymasi-ltcc-ferrite-dielectric-cofiring]] — direct experimental case study.

## References

- [[hagymasi-ltcc-ferrite-dielectric-cofiring]] — quantitative DT (72 %) vs FT (53 %) green densities and measured shrinkages.
- [[heunisch-2010-tape-cast-anisotropic-shrinkage]] — green density vs powder shape data (52–66 %).
- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — green density of Ni paste (55 vol% + organic 45 vol%).
- Rahaman, *Ceramic Processing and Sintering*, Ch. 7 ([[rahaman-ceramic-processing-sintering-textbook]]) — green-density / sintered-density relations.
