---
title: Murata SPICE Library & Sample DC-Bias Curves
type: concept
created: 2026-05-20
updated: 2026-05-20
status: complete
importance: medium
sources:
  - murata-grm-series-tcc-data.md
tags:
  - paper
---

# Murata SPICE Library & Sample DC-Bias Curves

A practical bridge from [[vendor-spice-models|vendor SPICE conceptual framework]] to **concrete parameter extraction** for the MLCC simulator. Documents (a) how the Murata SimSurfing tool exposes part data, (b) the structure of an exported SPICE netlist, and (c) a digest of DC-bias / temperature / aging values extractable from publicly available Murata documents ([[murata-grm-series-tcc-data]]).

## Where to get the data
**Murata SimSurfing**: <https://ds.murata.com/simsurfing/mlcc.html>
1. Pick part number (e.g., GRM21BR71A106KE15L = 10 µF / 10 V / 0805 / X7R).
2. Set operating point (V_DC, T).
3. Export: S-parameters (.s2p Touchstone), SPICE netlist (.sp / .lib), impedance CSV.

**Murata netlist library**: <https://www.murata.com/en-us/tool/data/spicedata/netlist-mlcc>
- ZIP archives per series (GRM, GR3, GRT, GCM, GA2, etc.) — sizes 0.1–8.3 MB
- Each ZIP contains one .sp or .lib per part number
- Values are **typical** at 1 MHz / small-signal AC / 20 or 25 °C / 0 V DC bias (per the docs)

**Dynamic model** (Murata's distinguishing feature): a separate library that includes the behavioral current source for V_DC + T runtime adjustment. Per [[vendor-spice-models]].

## SPICE netlist structure (static model)
A Murata-exported netlist for a single MLCC part typically looks like:

```spice
* GRM21BR71A106KE15L  10uF 10V X7R 0805
* Conditions: T=25°C, V_DC=0V
.SUBCKT MLCC_xxxx  port1  port2
  C1  port1  node_a    9.85u
  R1  node_a node_b    8.5m   ; ESR (dielectric loss)
  L1  node_b port2     0.43n  ; ESL (geometric)
  R2  port1  port2     1.2G   ; IR (leakage)
.ENDS
```

Some Murata models extend to a 4th-order network for above-SRF behavior:
```spice
  ...
  C2  node_b node_c    5p     ; high-f capacitive shunt
  L2  node_c port2     0.1n   ; secondary inductance
```

The dynamic model adds a parallel behavioral current source `G1` that adjusts based on `V(port1, port2)`:
```spice
  G1  port1  port2  cur=  f(V_DC, T, C0)
```
where `f` encodes the proprietary [[core-shell-batio3|core-shell]]-derived VCC and TCC fits.

## Digest of GRM Series quantitative data
From [[murata-grm-series-tcc-data]] (the public 2-page reference PDF):

### Capacitance vs temperature (C0G GRM21 family)
- C0G, **all P2H/R2H/S2H/T2H/U2J variants**: within ±10 % across −60 to +125 °C.
- C0G zero-bias data: flat near 0 % across the range.

### Capacitance vs temperature (X5R 50 V vs Y5V 50 V GRM21)
| T (°C) | X5R 50 V (ΔC %) | Y5V 50 V (ΔC %) |
|---:|---:|---:|
| −40 | +5 | −10 |
| −20 | +3 | −10 |
| 0   | 0 | 0 |
| +25 | 0 | 0 |
| +60 | −10 | −20 |
| +80 | −15 | −40 |
| +85 | (X5R limit) | **−80** |

### Capacitance vs DC voltage (50 V parts, GRM21 0805)
| V_DC (V) | C0G 50 V | X7R 50 V | Y5V 50 V |
|---:|---:|---:|---:|
| 0  | 0 % | 0 % | 0 % |
| 10 | 0 | −10 | −30 |
| 20 | 0 | −20 | −60 |
| 30 | 0 | −30 | −75 |
| 40 | 0 | −40 | −80 |
| 50 | 0 | **−50** | **−90** |

(Approximate values read from the published curves; vendor measurement conditions: C0G at 1 MHz, X7R/Y5V at 1 kHz.)

### Capacitance vs AC voltage (50 V parts)
| V_AC_rms (V) | C0G | X7R | Y5V |
|---:|---:|---:|---:|
| 0   | 0 % | 0 % | 0 % |
| 0.5 | 0 | +1 | +2 |
| 1.0 | 0 | +2 | +5 |
| 2.0 | 0 | +4 | +10 |
| 3.0 | 0 | +5 | +13 |
| 4.0 | 0 | +5 | **+14** |

Class II εr **grows** with increasing V_AC because larger AC drive sweeps more domain-wall response.

### Aging (capacitance vs time post-heat)
| Time (h) | C0G | X7R | Y5V |
|---:|---:|---:|---:|
| 10    | 0 % | 0 | 0 |
| 100   | 0 | −2 | −5 |
| 1 000  | 0 | −5 | −13 |
| 10 000 | 0 | **−10** | **−30** |

X7R: ~1.7 %/decade. Y5V: ~7 %/decade. Both consistent with the spec envelope.

## SRF / impedance curves (GRM21 family)
From the impedance-vs-frequency plots in the GRM data PDF:
- 1 pF C0G GRM21: SRF ≈ 800 MHz
- 100 pF C0G: SRF ≈ 200 MHz
- 1 nF C0G: SRF ≈ 50 MHz
- 1 µF X5R: SRF ≈ 5 MHz
- 10 µF X5R: SRF ≈ 1–2 MHz
- 100 µF X5R/Y5V: SRF ≈ 100–500 kHz
- 0.01 µF Y5V (10 nF): SRF ≈ 25 MHz

This roughly matches the textbook expectation `f_SRF = 1/(2π√(L·C))` with L ≈ 0.5–1 nH for GRM21 mounting geometry.

## Allowable apparent-power / current curves
Per the GRM data PDF (graphical, family-specific):
- GRM55 (2220): up to ~ 100 VA at ~ 30 MHz (large case, high-power tolerance)
- GRM21 (0805): up to ~ 10 VA at ~ 30 MHz
- GRM18 (0603): up to ~ 3 VA at ~ 30 MHz
- GRM31 (1206): up to ~ 30 VA at ~ 30 MHz

These limit derived from ΔT = 20 °C self-heating constraint.

## How a simulator should use this
1. **Class-level f_VCC fit** from the GRM Series data: X7R 0805 50 V drops to −50 % at 50 V_DC (rated) — calibrates the simulator's `f_VCC` sigmoid for X7R.
2. **AC-bias fit** is small in X7R (peaks +5 %), large in Y5V (+14 %). Class-II-only.
3. **Aging fit** for X7R: A_age ≈ 1.7 %/decade per the chart; matches the 1.5 %/decade industry spec.
4. **SRF lookup table** keyed by (case_size, cap_value, class) for a first-cut prediction.

For part-number-accurate predictions, the simulator should pull the Murata SPICE netlist (or use the API) for the specific PN and apply local R, L, C overrides instead of class-level defaults.

## Cross-references
- [[vendor-spice-models]] — the general framework
- [[murata-grm-series-tcc-data]] — the raw vendor doc
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[esr-esl-srf]]
- [[murata-grm-series]] — vendor product family
- [[x7r-dielectric]], [[y5v-z5u-class-iii-dielectric]] — class context

## References
- Murata SPICE library: <https://www.murata.com/en-us/tool/data/spicedata/netlist-mlcc>
- Murata SimSurfing MLCC: <https://ds.murata.com/simsurfing/mlcc.html>
- [[murata-grm-series-tcc-data]] — the underlying curve set
