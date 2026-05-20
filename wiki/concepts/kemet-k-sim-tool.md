---
title: KEMET K-SIM Parameter Simulation Tool
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: medium
sources: []
tags:
  - paper
---

# KEMET K-SIM Parameter Simulation Tool

[[kemet|KEMET]] / [[yageo|Yageo]]'s web-based capacitor characterization tool, the KEMET-side equivalent of [[murata|Murata]]'s SimSurfing. Distinguished from SimSurfing by **broader capacitor-type coverage**: ceramic (MLCC), KO-CAP (polymer-tantalum), tantalum, polymer, film, and aluminum electrolytic — useful when the simulator is asked to compare ceramic vs alternative technologies for the same decoupling problem.

## What K-SIM exposes
For a selected part number, K-SIM models:
- **Impedance vs frequency**: |Z(f)| including ESR floor at SRF
- **ESR vs frequency**: with dielectric vs electrode contributions separated
- **Capacitance vs frequency**: showing the rolloff approaching SRF
- **Inductance vs frequency**: above-SRF ESL
- **AC current vs frequency**: derived from ripple capability + heating
- **AC voltage vs frequency**: same, V-side
- **Capacitance vs DC voltage**: the [[dc-bias-derating|VCC curve]]
- **Temperature rise vs AC current**: self-heating prediction (a feature SimSurfing doesn't expose as cleanly)
- **Lifetime vs operating condition**: Arrhenius-Eyring style prediction for some series (especially tantalum / KO-CAP)

URL: <https://ksim3.kemet.com/capacitor-simulation>

## What K-SIM does NOT expose (or only partially)
- **Touchstone S-parameter** export — SimSurfing's strength, less prominent in K-SIM
- **Dynamic SPICE model** — K-SIM uses static models; per-operating-point export
- **Aging-over-time prediction** — not a full Liu-framework MTTF, more an empirical curve
- **Reliability statistics** (Weibull β, η) — vendor private

## K-SIM lifetime model
For tantalum / polymer / aluminum series, K-SIM has a built-in **operational-life prediction**:
$$
L = L_\text{rated} \cdot \left(\frac{V_\text{rated}}{V_\text{applied}}\right)^n \cdot 2^{(T_\text{rated} - T_\text{applied})/10}
$$
- `L_rated` = rated life at full V and T (typically 1000–5000 h)
- `V` and `T` factors are Arrhenius-like multipliers
- `n` is voltage acceleration exponent (varies by family; ~ 17 for tantalum, ~ 5 for polymer)
- Doubling for every 10 °C reduction is the simplified Arrhenius rule (10 °C → Ea ≈ 0.4 eV equivalent)

For **ceramic (MLCC)**, K-SIM doesn't expose a separate lifetime number — relies on the Class II aging spec and AEC-Q200 / IEC 60384 endurance test data. This is consistent with how ceramic reliability is treated industry-wide ([[prokopowicz-vaskas-equation|P-V model]] is used internally by vendors but rarely surfaced in a public tool).

## How a third-party simulator should use K-SIM
1. **For non-ceramic comparison**: Pull tantalum / polymer / aluminum lifetime predictions from K-SIM for the same Z_target as the ceramic solution. Lets the simulator output "you'd need 8 MLCCs vs 2 tantalums for this decoupling problem".
2. **For temperature-rise self-heating**: K-SIM's ripple-current-vs-T_rise data is more accessible than SimSurfing's; useful for high-current rails.
3. **For lifetime sanity check**: K-SIM's simplified Arrhenius lifetime prediction (for non-ceramic) is a good order-of-magnitude check against our simulator's BME-MLCC MTTF prediction.
4. **For comparing KEMET part numbers** against Murata equivalents.

## Cross-references
- [[vendor-spice-models]]
- [[murata-spice-library-and-curves]] — the SimSurfing counterpart
- [[kemet]] / [[yageo]]
- [[bme-c0g]] — KEMET specialty
- [[kemet-arcshield]] — KEMET specialty
- [[prokopowicz-vaskas-equation]]

## References
- KEMET K-SIM: <https://ksim3.kemet.com/capacitor-simulation>
- Mouser product page for K-SIM Simulation Tool
- KEMET Facebook announcement (2021) describing K-SIM coverage
