---
title: Heywang-Jonker Model (Schottky Grain-Boundary Barrier)
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - nasa-ir-degradation-ni-batio3-2015.md
  - nasa-time-dependent-ir-2013-prb.md
tags:
  - paper
---

# Heywang-Jonker Model

The textbook electronic-conduction model for **donor-doped polycrystalline BaTiO₃**, explaining why a material whose individual grains are semiconducting nonetheless forms an **excellent insulator** at the ceramic level — and why its resistance has a sharp positive temperature coefficient (PTCR) near [[curie-temperature|T_C]]. It is the foundation Liu uses for the [[oxygen-vacancy-migration|BME IR-degradation model]].

## The two contributions

### Heywang (1961)
At each grain boundary, electron-trapping acceptor states pull electrons out of the adjacent grain interiors. This creates a **double Schottky depletion layer** straddling the GB — two back-to-back depletion regions, each ~10 nm wide for typical BaTiO₃. Inside the depletion region, the local resistivity is many orders of magnitude higher than the grain interior because:
- Free-carrier concentration is depleted
- Built-in electrostatic barrier height `φ_B` ≈ 0.3–1 eV blocks thermal hopping

Conduction through the polycrystal goes **through the GB barriers**, not the grain interiors → ceramic resistance is set by the GB barriers in series.

### Jonker (1964) extension
Below T_C, the **ferroelectric polarization in the grain** contributes a counter-charge that **partially neutralizes** the acceptor trap charges at the GB. So `φ_B` is lower below T_C than above.

Above T_C the polarization disappears, the acceptor traps are no longer screened, and `φ_B` shoots up. **This is the origin of PTCR**: donor-doped BaTiO₃ (e.g., Y- or La-doped) shows resistance jumping 3–7 orders of magnitude going through T_C. Used commercially in over-current protection thermistors.

For MLCC dielectric (acceptor + donor co-doped, no PTCR target), the same physics gives the **base level of insulation resistance** of the part — even though each BaTiO₃ grain interior has measurable conductivity.

## The Schottky barrier height formula
$$
\phi_B \;=\; \frac{e^2 \, [n_s]^2}{8 \varepsilon_0 \varepsilon_r N_d}
$$
- `n_s` = surface (GB) acceptor-state density
- `N_d` = donor density in the grain
- `e, ε₀` = elementary charge, vacuum permittivity

A higher acceptor state density `n_s` → higher barrier → higher IR. This is the "barrier height" that [[nasa-ir-degradation-ni-batio3-2015|Liu (2015)]] tracks as a time-dependent quantity that decreases under DC bias due to [[oxygen-vacancy-migration|O-vacancy electromigration]] neutralizing the acceptor states.

## Time evolution under DC bias
Combining the Heywang formula with first-order O-vacancy electromigration kinetics gives the [[nasa-time-dependent-ir-2013-prb|Liu PRB 2013 result]]:
$$
\phi_B(t) \;=\; \phi_B(0) \cdot e^{-2 K t}, \quad K = K_0\, e^{-E_k/kT}
$$
i.e., barrier collapse is exponential. **At first catastrophic failure**, barrier height has dropped 55–70 % from its starting value.

## Why it matters for the simulator
- Base IR(0) of an MLCC scales with `exp(φ_B / kT)` — so even small changes in `φ_B` cause orders-of-magnitude changes in IR.
- Reliability prediction relies on tracking `φ_B(t)` under stress (Liu's framework).
- Class I dielectrics like [[cazro3]] have negligible donor density (they're paraelectric, no free carriers from polarization), so the Heywang model doesn't apply — IR is set by intrinsic band-gap conduction instead, which is why CaZrO₃ IR rises with T while BaTiO₃ falls.

## Cross-references
- [[oxygen-vacancy-migration]]
- [[bme-reliability-model]]
- [[defect-chemistry-batio3]]
- [[curie-temperature]]
- [[batio3]]
- [[cazro3]]

## References
- [[nasa-ir-degradation-ni-batio3-2015]] — Liu IEEE TCPMT 2015, applies Heywang-Jonker to BME MLCC IR
- [[nasa-time-dependent-ir-2013-prb]] — Liu PRB 2013, derives time-dependent barrier collapse
- Heywang, *J. Mater. Sci.* 6 (1971) 1214 — original PTCR explanation
- Jonker, *Solid-State Electronics* 7 (1964) 895 — ferroelectric counter-charge extension
