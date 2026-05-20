---
title: BaTiO₃ Powder Synthesis Routes
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: medium
sources: []
tags:
  - paper
---

# BaTiO₃ Powder Synthesis Routes

The starting powder properties — particle size, distribution width, Ba/Ti stoichiometry, impurity level, surface termination — propagate all the way to MLCC reliability. Modern thin-layer parts demand 100–300 nm grain after sintering, which requires starting powder around 50–200 nm with narrow distribution.

## Synthesis routes (in order of industrial dominance for MLCC)

### Solid-state reaction (legacy / lowest-cost)
$$
\text{BaCO}_3 + \text{TiO}_2 \;\xrightarrow{1100\text{--}1400\,^\circ\text{C}}\; \text{BaTiO}_3 + \text{CO}_2 \!\uparrow
$$
- **Process**: ball-mill BaCO₃ + TiO₂ → calcine 1100–1400 °C → re-mill → screen.
- **Pros**: cheapest, scalable, well-understood.
- **Cons**: agglomerated particles, broad size distribution (sub-µm to several µm), residual impurities, low homogeneity, hard to get below 0.5 µm without aggressive milling that contaminates and amorphizes.
- **Used by**: most second-tier MLCC and ceramic-component manufacturers; Korean / Chinese producers historically at this size range (300–500 nm Ba(Ti)O₃).

### Hydrothermal (modern fine-grain BME workhorse)
$$
\text{Ba(OH)}_2 + \text{TiO}_2 \cdot n\text{H}_2\text{O} \;\xrightarrow{100\text{--}250\,^\circ\text{C},\,\text{H}_2\text{O}}\; \text{BaTiO}_3 + (n{+}1)\text{H}_2\text{O}
$$
- **Process**: aqueous chemistry in autoclave at 100–250 °C and elevated pressure.
- **Pros**: directly crystalline (no calcination needed), narrow size distribution, single-crystal grains, sub-100 nm achievable (down to 10–15 nm).
- **Cons**: residual OH⁻ groups in the lattice, batch process, more expensive than solid-state.
- **Used by**: [[murata]] — produces own 100 nm powder; [[samsung-electro-mechanics]] increasingly via this route; Sakai Chemical commercial powder supplier.

### Oxalate co-precipitation
$$
\text{Ba}^{2+} + \text{Ti}^{4+} + 2\text{C}_2\text{O}_4^{2-} \to \text{BaTiO(C}_2\text{O}_4)_2\cdot 4\text{H}_2\text{O} \xrightarrow{\,>600\,^\circ\text{C}\,} \text{BaTiO}_3
$$
- **Process**: precipitate Ba-Ti-oxalate from nitrate solution → wash → calcine 600–900 °C.
- **Pros**: very narrow size distribution, Ba/Ti stoichiometry well-controlled, lower calcination T than solid-state.
- **Cons**: filtration and washing steps, oxalate decomposition releases CO/CO₂ (process safety).

### Sol-gel
- **Process**: hydrolysis of barium and titanium alkoxides (e.g., Ti(OiPr)₄ + Ba(OAc)₂) → gel → calcine.
- **Pros**: high purity, narrow distribution, molecular-level dopant homogeneity (great for [[core-shell-batio3|core-shell]] formulations).
- **Cons**: expensive precursors, low yield, mostly research-scale.

### Microwave-assisted solid-state and combustion
Niche / research routes producing 30–85 nm powders with significantly lower energy input.

## Critical specs the MLCC line wants
1. **Median grain diameter**: 50–300 nm depending on target dielectric layer thickness (rule: d ≥ 3–5 r̄ from [[core-shell-batio3]]).
2. **Size distribution**: D₉₀ / D₅₀ ≤ 2 — narrow distribution suppresses outlier grain growth during sintering.
3. **Ba/Ti ratio**: 1.000 ± 0.001 — slight Ba-excess favors stable sintering; Ti-rich causes liquid-phase wetting issues.
4. **Crystallinity**: tetragonal phase fraction ≥ 0.95 at room temperature in coarse powders; transitions to cubic in very fine powders below ~70 nm.
5. **Surface OH⁻ / carbonate content**: < 0.5 wt % — high OH leads to sintering shrinkage drift.

## Implications for the simulator
- Powder grain size sets the **lower bound on dielectric thickness** (the [[core-shell-batio3|3–5 grains rule]]).
- Powder narrowness sets the **standard deviation on εr** across the part lot.
- Hydrothermal vs solid-state routes give different sintering kinetics → different shrinkage curves → different yield envelopes. Vendor identification of powder route is a key reliability signal.

## Cross-references
- [[batio3]]
- [[core-shell-batio3]]
- [[mlcc-manufacturing-process]]
- [[murata]]
- [[samsung-electro-mechanics]]

## References (to be filled)
- Surface modifier (Tween 80) hydrothermal route — ultrafine <100 nm BaTiO₃
- Cole et al., hydrothermal BaTiO₃ 10–15 nm at 100–150 °C (multiple papers via Sci. Rep., PMC)
- Sol-gel hydrothermal hybrid via Pmc / sciencedirect references
