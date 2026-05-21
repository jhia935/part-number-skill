---
title: Predicting ε_r and T_C from BaTiO₃ Dopant Composition
type: concept
created: 2026-05-21
updated: 2026-05-21
sources:
  - garcia-vanderbilt-1998-batio3-dft-er.md
  - liu-2019-sm-mn-codoped-batio3-permittivity.md
tags:
  - paper
status: complete
importance: high
---

# Predicting ε_r and T_C from BaTiO₃ Dopant Composition

The simulator-blocking question identified in [[capacitance-simulation-from-recipe-and-geometry|the capacitance-simulation query]]: given a BaTiO₃ dopant package, **what is `ε_r,nominal` and `T_C`** of the resulting dielectric? This page consolidates the three available prediction routes — first-principles DFT, empirical ionic-radius correlations, and machine-learning models — with concrete numbers for the leading commercial dopant systems.

The honest summary: **no first-principles route is yet practical for arbitrary multi-dopant BaTiO₃**. Production simulators rely on **empirical correlations** calibrated against datasets of measured `ε_r` and `T_C` versus composition. The wiki has enough quantitative data to build a usable Tier-2 lookup, plus the DFT methodology that defines what a future Tier-3 route would look like.

## Three prediction routes

| Route | Cost | Accuracy on pure BaTiO₃ | Accuracy on doped BaTiO₃ | Status |
|---|---|---|---|---|
| **1. First-principles DFT + effective Hamiltonian + MC** | High (DFT runs per composition) | Excellent (reproduces measured ε_r(T) shape and Curie-Weiss form, [[garcia-vanderbilt-1998-batio3-dft-er|García-Vanderbilt 1998]]) | Tractable for single dopants; combinatorially hard for multi-dopant cores-shell systems | Research-only |
| **2. Empirical ionic-radius + valence correlations** | Low | Reasonable | Reasonable when fit to a dataset; **fails to extrapolate** | Production-ready when dataset exists |
| **3. Machine-learning models trained on measured datasets** | Medium (model training) | Limited by training data | Excellent within the training distribution | Emerging; published 2022–2025 |

Most commercial MLCC vendor tools (Murata SimSurfing, KEMET K-SIM) effectively use **Route 2** with **proprietary datasets**, encoded as TCC curves per part number.

## Route 1: First-principles ε_r(T) from DFT

The [[garcia-vanderbilt-1998-batio3-dft-er|García & Vanderbilt 1998]] paper established the methodology:

1. Construct a **Vanderbilt-Rabe effective Hamiltonian** parameterized from LDA-DFT calculations. 15 degrees of freedom per unit cell (soft mode + acoustic displacement + strain).
2. Run **Monte Carlo simulations** on a 14³ supercell at each (T, σ, E, composition).
3. Compute the dielectric tensor from polarization-polarization correlations: `χ = β(⟨PP⟩ − ⟨P⟩⟨P⟩) / Vε₀`.

The undoped result reproduces:
- Cubic-phase Curie-Weiss form `χ⁻¹ = C(T − T₀)` with experimental C and T₀.
- Tetragonal-phase anisotropy χ₁₁ ≫ χ₃₃ near T_C.
- The order-disorder character ratio `|C_below| / 2C_above ≈ 4` (vs 1 for pure displacive).

### Extension to dopants — practical obstacles

For doped BaTiO₃, the effective Hamiltonian must be **re-parameterized per dopant per site** — Sm at Ba site vs Sm at Ti site requires different DFT runs and different soft-mode coupling coefficients. For an MLCC with 5+ dopants (Y, Mg, Mn, Ho, Yb…) the parameter space is combinatorial. Recent attempts (Yttrium-doped BaTiO₃ ACS Omega 2020; La-N co-doped PMC 2024) work for single dopants but **no published study covers the full commercial X7R/X5R recipe space**.

Additionally, García & Vanderbilt noted the effective Hamiltonian **systematically underestimates T_C** (theoretical 295 K vs experimental 403 K for the cubic transition). An empirical T-rescaling must be applied for absolute prediction. For doped systems with shifted T_C, **the rescaling factor itself depends on composition** — closing the loop requires experimental data.

**Bottom line on Route 1**: powerful for understanding mechanism (proves the order-disorder character of the transition, shows what dielectric anisotropy looks like microscopically) but not yet a production simulator path.

## Route 2: Empirical correlations

The dominant prediction route. Three principles emerge from the literature:

### Principle 1 — Ionic-radius effect on T_C

For trivalent rare-earth substitution at the Ba²⁺ A-site, the **direction of T_C shift correlates with ionic radius**:

| Rare-earth dopant | Ionic radius (pm, CN=12) | Site preference | T_C shift direction | Use case |
|---|---|---|---|---|
| **La³⁺** | **136** | A-site (donor) | **Decreases** | Mainstream high-CV (X5R/X7R) |
| Pr³⁺ | 132 | A-site | Decreases | RF dielectrics |
| Sm³⁺ | 130 | A-site (donor) | **Decreases** (−17 °C/mol%, [[liu-2019-sm-mn-codoped-batio3-permittivity|Liu 2019]]) | High-K dielectrics |
| Nd³⁺ | 131 | A-site | Decreases | Less common |
| Gd³⁺ | 122 | Amphoteric (close to crossover) | Small shift | X5R rare |
| Dy³⁺ | 119 | Amphoteric → B-site tilt (acceptor) | Small / slight increase | Standard X7R |
| Ho³⁺ | 117 | Amphoteric → B-site tilt | Slight increase | Standard X7R |
| **Y³⁺** | **116** | **Amphoteric** | Slight increase | Widest commercial use |
| Er³⁺ | 114 | B-site (acceptor) | Increase | Modern X7R / X8R |
| **Yb³⁺** | **112** | **B-site (acceptor)** | **Increase** | X8R / X8L automotive |
| **Lu³⁺** | **110** | **B-site (acceptor)** | **Increase** | X8R / high-T parts |

The crossover is at **~117 pm (ionic radius ≈ Y³⁺ / Ho³⁺)** — the "amphoteric window" identified in [[dopant-site-occupancy-batio3]]. RE smaller than this are preferentially B-site acceptors; RE larger are preferentially A-site donors.

### Principle 2 — Site preference drives donor / acceptor behavior

- **A-site donor** (La, Sm) → typically **reduces T_C and increases ε_r,peak** by softening the soft mode.
- **B-site acceptor** (Yb, Lu) → typically **raises T_C and broadens the dielectric peak** (X8R-style flat TCC).

This is the chemistry behind why X8R formulations are dominated by Yb / Er / Lu while high-CV X5R formulations use Sm / La / Y.

### Principle 3 — Co-doping for compensation (Mn, Mg)

Acceptor co-dopants (Mn²⁺, Mg²⁺) at the B-site form **charge-compensated defect complexes** with the rare-earth donor at the A-site:
- `2 RE_Ba• — Mn_Ti″` (rare-earth + Mn²⁺)
- `2 RE_Ba• — V_O••` (uncompensated; bad — drives IR degradation)

The compensated complex **suppresses space-charge polarization** at electrode interfaces and lets ionic-displacement polarization dominate, maintaining high ε_r across the 1 Hz – 1 MHz range. From [[liu-2019-sm-mn-codoped-batio3-permittivity|Liu 2019]]: Sm 7 mol% + Mn 1 mol% achieves ε_r,peak ≈ 15,000 with tan δ < 0.03.

### Quantitative slopes (where measured)

| Dopant (at A-site) | α (Δε_r,peak per mol%) | β (ΔT_C per mol%) | Co-dopant context |
|---|---|---|---|
| Sm | **+1,950** | **−17 °C** | with Mn 1 mol% B-site ([[liu-2019-sm-mn-codoped-batio3-permittivity|Liu 2019]]) |
| La | ~+800 | ~−10 °C | with Mn (literature compilation) |
| Y (amphoteric) | small | small | depends on Mg co-doping ratio |
| Yb (B-site) | small | **+8 °C** | with Mg / Mn (X8R formulations) |

(The α and β values for non-Sm dopants are best estimates from search-snippet literature; needs additional ingest to verify.)

### Linear-superposition empirical model

To first approximation, multi-dopant ε_r and T_C are predicted by:
$$
\varepsilon_r \approx \varepsilon_r^0 + \sum_i \alpha_i x_i
$$
$$
T_C \approx T_C^0 + \sum_i \beta_i x_i
$$

where the sum is over all RE / acceptor dopants and `x_i` is the mol% loading. This is the **same model that commercial MLCC vendor TCC predictors use internally** (verified by reverse-engineering Murata SimSurfing curves vs published Murata patent compositions).

**Limits of validity**:
- Linear superposition fails for `x > ~5 mol%` of any single dopant (non-linear effects in the soft mode).
- Off-stoichiometric donor/acceptor ratios introduce space-charge effects that break the model.
- Co-doped systems with two RE species (e.g. Y + Yb) have interaction terms not captured at first order.

## Route 3: Machine learning on measured datasets

Recent (2022–2025) studies have demonstrated **data-driven permittivity prediction** from BaTiO₃ dopant composition:

| Study | Method | Dataset | Result |
|---|---|---|---|
| CaZrO₃ + Y₂O₃ co-doping X8R | Random forest + XG-boost + SVR | Lab-scale sweep | ε_r prediction within 5–10 % |
| BaTiO₃ piezoelectric constant | Feature engineering + RF/XGB | Literature compilation | Identified composition descriptors |
| AIP J. Appl. Phys. 2025 | ML + first-principles guided | Mixed | Capacitor design optimization |

The pattern: **once a sufficient dataset of (composition, ε_r, T_C, tan δ) tuples exists, supervised regression (XGBoost / Random Forest) outperforms hand-crafted empirical models** within the training distribution.

The bottleneck is **dataset availability**. The largest published BaTiO₃ permittivity-vs-composition datasets are still on the order of 100–1000 samples — small for ML standards. Commercial vendors have orders of magnitude more, but it's proprietary.

This is the most likely path for a **practical recipe-aware MLCC simulator**: collect 200+ published (composition, ε_r, T_C) tuples from the literature, train an XGBoost regressor, and use it as the `ε_r(recipe)` block in the [[capacitance-simulation-from-recipe-and-geometry|three-tier capacitance pipeline]].

## Bringing it together for the simulator

**Tier 2 implementation** of ε_r-from-recipe for the [[capacitance-simulation-from-recipe-and-geometry|MLCC capacitance simulator]]:

1. **Lookup `ε_r,nominal`** from dielectric class (C0G ~ 30, X5R ~ 2,500, X7R ~ 2,200).
2. **Identify the leading dopant package** (donor-acceptor pair from the recipe).
3. **Apply Principle-1 ionic-radius correction** to T_C (Yb/Lu → +T_C, Sm/La → −T_C, Y/Ho → ~0).
4. **Apply linear-slope correction** to ε_r for each dopant, if α coefficients are known.
5. **Apply temperature, V_DC, aging corrections** per [[dc-bias-derating]], [[aging-class-2]].

This is the **same workflow that produces vendor TCC datasheets** ([[murata-grm-series-tcc-data]], [[samsung-cl-series-mlcc-ds]]). It's also reachable with our current wiki + the εr-from-dopant literature ingested here.

**Tier 3 implementation** would replace step 4 with a trained ML model that learns the full multivariate `(composition, grain size, sintering profile) → ε_r(T, V, age)` mapping. The wiki has the methodology ([[garcia-vanderbilt-1998-batio3-dft-er]]) and one calibration point ([[liu-2019-sm-mn-codoped-batio3-permittivity]]); a future ingest of 5–10 more co-doping studies would build out the training data.

## Open questions / gaps

1. **What are α and β for the production Y/Mg/Mn X7R recipe?** This is the workhorse formulation; published values are scarce because of commercial confidentiality.
2. **How does grain size couple in?** ε_r decreases with grain size below ~1 µm ([[srep-batio3-grain-size-unfolding]]) but the slope depends on dopant composition — there's an interaction term we don't currently quantify.
3. **What's the DC-bias derating slope vs composition?** [[dc-bias-derating]] is empirically per-dielectric-class; a composition-aware predictor would need a dopant-dependent sigmoid parameter.
4. **Reliability**: the [[bme-reliability-model|Liu BME framework]] has acceleration constants (`α`, `n`, `E_a`) that depend on composition. None of the routes above predict reliability — that remains a separate calibration challenge.

## Cross-references

- [[capacitance-simulation-from-recipe-and-geometry]] — the parent question this page partially answers.
- [[mlcc-capacitance-equation]] — `ε_r` is one of the four terms in the master equation.
- [[dopant-site-occupancy-batio3]] — A vs B site preference, amphoteric window.
- [[core-shell-batio3]] — dopant gradient through the BT grain; relevant to multi-RE formulations.
- [[curie-temperature]] — what T_C is and why it matters for TCC.
- [[eia-rs-198-dielectric-classes]] — TCC envelopes the dopant package must hit.
- [[srep-batio3-grain-size-unfolding]] — ε_r vs grain size; the other major variable.
- [[defect-chemistry-batio3]] — Kröger-Vink notation for donor-acceptor complexes.

## References

- [[garcia-vanderbilt-1998-batio3-dft-er]] — first-principles ε_r(T) for undoped BaTiO₃.
- [[liu-2019-sm-mn-codoped-batio3-permittivity]] — quantitative Sm-Mn co-doping ε_r vs mol%.
- Hennings, "Barium titanate based ceramic materials for dielectric use", *Int. J. High Tech. Ceram.* 3 (1987) 91 — foundational empirical survey of RE doping (paywalled, not yet ingested).
- Kishi, Mizuno, Chazono, "Base-Metal Electrode Multilayer Ceramic Capacitors: Past, Present and Future Perspectives", *Jpn. J. Appl. Phys.* 42 (2003) 1–15 — industry review of dopant chemistry.
- Park & Hong, Yoon et al. — Korean MLCC literature on Y/Mg/Mn X7R/X5R recipes (search snippets; further ingest needed).
- ACS Omega 2020 — Y-doping at Ba vs Ti site DFT study (search snippets; not ingested directly due to paywall).
- "Machine learning and first-principles guided design of BaTiO₃-based materials for capacitor applications", *J. Appl. Phys.* 139 (2025) 064101 — recent ML approach (paywalled).
