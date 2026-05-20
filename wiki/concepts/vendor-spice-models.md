---
title: Vendor SPICE / S-Parameter / Simulation Tool Models
type: concept
created: 2026-05-20
updated: 2026-05-20
sources: []
tags:
  - paper
---

# Vendor SPICE / S-Parameter / Simulation Tool Models

The canonical way the MLCC industry encodes **per-part-number characteristics** for use in external circuit simulators. Each Tier-1 vendor exposes a web-based design tool that produces SPICE netlists, Touchstone S-parameters, and impedance plots as a function of (V_DC, V_AC, T) — essentially a vendor-curated, characterized version of the same physics our `resources/design-rules/simulator-model.md` specifies.

## The major vendor tools

| Vendor | Tool name | Output formats | Conditions accepted |
|---|---|---|---|
| [[murata]] | **SimSurfing** | SPICE netlist (R-L-C static + behavioral current source dynamic), S2P Touchstone, impedance .csv | T, V_DC explicit |
| [[samsung-electro-mechanics]] | **myCAP** | SPICE netlist, S-parameter | T, V_DC explicit |
| [[kemet]] / [[yageo]] | **K-SIM** | SPICE netlist, S-parameter, lifetime model | T, V_DC, lifetime |
| [[kyocera-avx]] / KYOCERA | **SpiCap** | S-parameter | T, V_DC |
| [[tdk]] | **SEAT-MLCC** | SPICE netlist, S-parameter | T, V_DC |
| [[taiyo-yuden]] | TY library on DigiKey + vendor portal | S-parameter | T, V_DC |

These tools are typically free, web-based, and updated regularly. Their parameter databases reflect **actual measurements** on commercial parts — the only practical way to get part-number-accurate fits for a third-party simulator without doing the characterization yourself.

## Static vs dynamic SPICE models (Murata example)

### Static model
A simple **R–L–C series network** (sometimes 2nd or 4th-order to capture self-resonance and post-SRF behavior) with fixed values for a specific (V_DC, T) operating point. Most other vendors call this just "the SPICE model."

| Element | Captures |
|---|---|
| C | ideal capacitance at the operating point |
| ESR (series R) | dielectric loss + electrode resistance |
| ESL (series L) | termination + internal-electrode loop inductance |

Compatible with **any SPICE simulator** (ngspice, LTspice, PSpice, HSPICE). User-friendly but requires re-export each time the operating point changes.

### Dynamic model (Murata's innovation)
A static R-L-C network **plus a behavioral current source in parallel** that adjusts C and ESR continuously based on instantaneous V_DC and T. Captures the non-linearity of [[batio3|BaTiO₃]] under bias and temperature swings during transient simulations.

**Key differentiator**: the dynamic model can be used in a single transient simulation that sweeps DC bias or temperature — no re-export needed. Murata reports DC/DC converter output ripple and transient response "very nearly identical to measured values" with the dynamic model, vs significant errors with the static model under varying bias.

Output formats: VerilogA-style behavioral source + static-element wrapper.

## What the models do NOT capture
1. **Aging** ([[aging-class-2|natural]] or [[dc-bias-aging|DC-bias-accelerated]]) — most vendor models don't include time-dependence.
2. **Reliability / lifetime / MTTF** — separate vendor tools (K-SIM Lifetime, Murata DC bias aging analyzer) handle this.
3. **Mechanical (flex, thermal-shock) failure modes** — purely electrical models.
4. **Surface arcing / breakdown** — not in standard SPICE models.
5. **AC-bias dependence at small signal** (10 mV vs 1 V_rms) — typically not exposed; measurement-standard 1 V_rms is the implicit AC drive.

## How a third-party simulator should consume them

### Option A — direct SPICE bridge
- User selects a vendor + part number; simulator fetches the static SPICE netlist via vendor API (Murata SimSurfing has REST-like URL parameters).
- Run circuit-level simulation natively in SPICE.
- **Pro**: vendor-canonical accuracy. **Con**: no support for vendor-specific aging / reliability — we have to layer that on.

### Option B — parameter extraction
- Parse vendor SPICE netlists for several operating points; extract (C₀, ESR_0, ESL, E₀, p) per part number.
- Store in a local lookup table keyed by (vendor, part_number, T, V_DC).
- Use the simulator's own multiplicative-factor decomposition (`f_VCC, f_AC, f_T, f_age`) to combine with reliability and aging models that the vendor tool doesn't provide.
- **Pro**: full simulator stack with all physics. **Con**: extraction layer to build and maintain.

### Option C — touchstone (S-parameter) bridge
- For RF / signal-integrity applications, use the .s2p Touchstone export directly in HSPICE / ADS / Cadence.
- For DC-bias / temperature analysis, request the .s2p at each operating point.
- **Pro**: vendor-blessed frequency-domain accuracy. **Con**: not natively time-domain.

## Implications for the MLCC simulator we're building

The wiki's `resources/design-rules/simulator-model.md` specifies the **physics** of MLCC behavior; vendor SPICE models provide the **fitted parameters per part number**. The cleanest architecture combines them:

1. **Physics layer** (our simulator): `C_eff(V_DC, V_AC, T, t) = C₀ · f_VCC(E) · f_AC · f_T · f_age`, plus reliability `R(t)`.
2. **Parameter layer** (extracted from vendor SPICE): `C₀, ESR(f), ESL, E₀, p, A_age, E_k` per part number.

Vendor models give us the parameters; our simulator adds time-dependence (aging) and reliability (Weibull / Liu two-mode) that the vendor tools don't expose.

## Cross-references
- [[mlcc-capacitance-equation]]
- [[dc-bias-derating]]
- [[esr-esl-srf]]
- [[murata]] — primary SimSurfing source
- [[samsung-electro-mechanics]] — myCAP
- [[kemet]] / [[yageo]] — K-SIM
- [[tdk-cga-series]] — TDK SEAT-MLCC

## References
- Murata SPICE Model / Netlist page: <https://www.murata.com/en-us/tool/data/spicedata/netlist-mlcc>
- Murata article "MLCC Dynamic Model Supports Circuit Simulations" (article.murata.com)
- Murata SimSurfing: <https://ds.murata.com/simsurfing/mlcc.html>
- KEMET K-SIM: <https://ksim3.kemet.com/>
- TDK SEAT-MLCC: <https://product.tdk.com/info/en/technicalsupport/tvcl/index.html>
