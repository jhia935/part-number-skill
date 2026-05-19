---
title: Oxygen-Vacancy Migration & IR Degradation
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - nasa-ir-degradation-ni-batio3-2015.md
  - nasa-nepp-bme-mlcc-reliability.md
  - escies-bme-mlcc-high-reliability.md
tags:
  - paper
---

# Oxygen-Vacancy Migration & IR Degradation

The dominant **slow-degradation** failure mechanism in [[bme-vs-pme|BME]] MLCCs. Oxygen vacancies (V_O••) are created when BaTiO₃ is fired in the reducing atmosphere needed to keep Ni electrodes from oxidizing. Under DC bias they electromigrate toward the cathode, accumulate at grain boundaries, and progressively lower the Schottky barrier height — capacitor leakage rises until breakdown.

## Why oxygen vacancies exist in BME parts
1. Co-firing of Ni inner electrode and BaTiO₃ dielectric requires reducing atmosphere (~10⁻¹⁰ to 10⁻¹² atm PO₂) to keep Ni metallic.
2. Reducing atmosphere drives the oxidation equilibrium `2 O²⁻ ↔ O₂ + 4e⁻ + 2 V_O••` toward the right.
3. The resulting V_O•• concentration creates donor-like behavior and free electrons, which is countered by **acceptor doping** (Mg, Mn) — but never fully eliminates the vacancies.

## What [[re-oxidation-anneal]] does
After main sintering, a lower-temperature anneal (~900–1100 °C) in slightly higher PO₂ refills some vacancies near grain boundaries. Limits: (1) can't be too oxidizing or Ni electrodes start to oxidize, (2) penetration depth limited by O-diffusion kinetics. Modern thin-layer parts have shorter diffusion paths but more critical V_O budget.

## Migration kinetics & IR degradation
Under DC field at elevated T, V_O•• migrate toward the cathode. They pile up at grain boundaries, **reducing the Schottky depletion-barrier height** (Heywang-Jonker model). [[donhang-liu|Liu (2015)]] proposes:
$$
\phi(t) \;=\; \phi(0)\, e^{-2 K t}, \quad K = K_0 \, e^{-E_k / k T}
$$
- `φ(t)`: instantaneous barrier height after time t
- `K`: temperature-dependent degradation rate (Arrhenius)
- `K ∝ 1/MTTF`

**Counterintuitive design trade-off**: too low `φ(0)` → too much electronic leakage; too high → fast electromigration. Optimum is moderate.

## Rare-earth-doping countermeasure
Y, Ho, Dy, Er, Yb, Tb, La substitute at Ba or Ti sites and pin O-vacancies, slowing electromigration. First-principles calculations confirm reduced O-diffusion coefficient in doped vs undoped BaTiO₃ ([[core-shell-batio3]]). This is the **chemistry** behind the modern [[core-shell-batio3|core-shell microstructure]].

## CaZrO₃ alternative
[[cazro3-dielectric|CaZrO₃-based]] BME C0G is intrinsically reduction-resistant — Ca and Zr bind O strongly in the perovskite. The reoxidation anneal is "for refinement, not necessity" per [[escies-bme-mlcc-high-reliability]]. IR drops far less with temperature than in BaTiO₃ systems, and may even **rise** above 120 °C.

## Implication for the simulator
- IR(t) is the right observable for BME reliability prediction, not just TTF.
- Use Arrhenius temperature acceleration on `K` to project lifetime; Eₐ here is in the 1.0–1.7 eV range for typical BME.
- For Class I BME (CaZrO₃), this whole degradation path is much slower — and high-T (>125 °C) operation safer.

## Cross-references
- [[bme-reliability-model]]
- [[bme-sintering-atmosphere]]
- [[re-oxidation-anneal]]
- [[core-shell-batio3]]
- [[cazro3-dielectric]]
- [[bme-vs-pme]]

## References
- [[nasa-ir-degradation-ni-batio3-2015]]
- [[nasa-nepp-bme-mlcc-reliability]]
- [[escies-bme-mlcc-high-reliability]]
