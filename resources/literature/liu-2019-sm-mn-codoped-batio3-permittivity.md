<!-- Source URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6416545/ | Fetched: 2026-05-21 -->
<!-- Original publication: Q. Liu, J. Liu, D. Lu, T. Li, W. Zheng. Materials 12 (2019) 678. doi:10.3390/ma12040678 -->
<!-- Open access (MDPI / Materials journal). -->

# Dense Sm and Mn Co-Doped BaTiO₃ Ceramics with High Permittivity

**Authors:** Q. Liu, J. Liu, D. Lu, T. Li, W. Zheng
**Journal:** *Materials* 12 (4) (2019) 678
**DOI:** 10.3390/ma12040678 (open access, MDPI)

## Abstract

Investigates the structure, valence state, and dielectric properties of (Ba₁₋ₓSmₓ)(Ti₀.₉₉Mn₀.₀₁)O₃ (BSTM) ceramics across Sm concentrations x = 0.02 to 0.07 (2–7 mol%).

## Key quantitative findings

### Composition

- **Samarium**: 2–7 mol% substituting Ba²⁺ at A-site
- **Manganese**: constant at 1 mol% substituting Ti⁴⁺ at B-site
- General formula: (Ba₁₋ₓSmₓ)(Ti₀.₉₉Mn₀.₀₁)O₃

### Permittivity vs Sm content

| Sm content x | Peak permittivity ε'_max | RT permittivity ε'_RT |
|---|---|---|
| 0.02 (2 mol%) | **5,480** | — |
| 0.03 | — | — |
| 0.05 | — | — |
| **0.07 (7 mol%)** | **15,220** | **13,810** |

Peak permittivity nearly **triples** as Sm content rises from 2 → 7 mol%.

### Curie temperature shift

| Sm content x | Curie T (°C) |
|---|---|
| 0.02 | **105.5** |
| 0.07 | **20.4** |

**T_C drops by ~85 °C** as Sm rises 2 → 7 mol%. Sm³⁺ at the A-site lowers T_C (consistent with smaller ionic radius than Ba²⁺).

### Dielectric loss

- tan δ < 0.03 across the temperature range tested — meets MLCC dielectric-loss requirements.

## Mechanism

The high permittivity is enabled by:

1. **Reduction of Mn**: Sm³⁺ donor doping reduces Mn from Mn³⁺/Mn⁴⁺ back to **Mn²⁺**, stabilizing the tetragonal ferroelectric phase and suppressing hexagonal phase formation.

2. **Donor-acceptor defect complexes** (`2 Sm_Ba• — Mn_Ti″`): Sm³⁺ at Ba²⁺ site acts as a donor; Mn²⁺ at Ti⁴⁺ site acts as an acceptor. Together they form charge-neutral defect complexes that **prevent space-charge polarization** at electrode interfaces. This lets ionic-displacement polarization dominate across the 1 Hz – 1 MHz range, maintaining high ε' uniformly.

3. **Maintaining ferroelectric domains**: at 7 mol% Sm, the system is still ferroelectric (T_C just below room temperature), so domain-wall contributions to permittivity remain large.

## Implications for the simulator

This paper gives a quantitative recipe: choose Sm 2–7 mol% on Ba-site + Mn 1 mol% on Ti-site → predictable ε' from 5,500 → 15,000 with predictable T_C from 105 → 20 °C. The relationship is approximately **linear in Sm mol%** for both ε' (slope ≈ +2,000 per mol% Sm) and T_C (slope ≈ −17 °C per mol% Sm).

This is the kind of empirical correlation that, gathered across many dopant systems, would let a recipe-aware simulator predict ε_r and T_C from the dopant composition.

## Caveats

- Only one acceptor co-dopant (Mn) was studied — the literature has Mg, Co, Cu, Ni co-dopants with different valence-state stabilization behavior.
- One sintering profile, one grain-size regime. ε' values include grain-size contributions that this study did not vary independently.
- Donor-acceptor compensation requires precise Sm:Mn stoichiometry; deviation introduces space-charge polarization and ε' drops.
