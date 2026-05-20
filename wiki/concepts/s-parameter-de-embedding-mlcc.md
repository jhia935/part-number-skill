---
title: S-Parameter De-Embedding for MLCC (ESL Extraction)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources: []
tags:
  - paper
---

# S-Parameter De-Embedding for MLCC (ESL Extraction)

How to **separate the part's intrinsic ESL from the test-fixture parasitics** when measuring or modeling an MLCC's high-frequency behavior. Critical because MLCC ESL is ~ 0.1–1 nH but a typical PCB test fixture has 0.5–5 nH of parasitic inductance — the fixture can easily dominate the measurement.

## The measurement problem

You connect a VNA (vector network analyzer) to a PCB test fixture holding an MLCC. The VNA gives you S-parameters of the **fixture + DUT** in series. The fixture contributes:
- Connector parasitic L and C
- Trace inductance from connector to part pad
- Via inductance (board-to-plane and plane-to-pad)
- Mounting-pad self-capacitance
- Ground-return path inductance

For a small-ESL MLCC, fixture contribution often **exceeds** the part contribution. Without de-embedding, the measured ESL is the fixture ESL plus part ESL, not just the part.

## De-embedding methods

### TRL (Thru-Reflect-Line) calibration
Most rigorous. Requires three calibration standards (a Thru, a Reflect, a Line of known length) at the **measurement plane** you want, with the same fixture as the DUT.
- Pros: highly accurate to GHz frequencies
- Cons: needs precise fab of three calibration boards; complex math
- Standard for IEEE / NIST-grade work

### Open / Short / Through (OST) de-embedding
The pragmatic compromise.
1. Fab three test boards: one with the DUT site open-circuited, one short-circuited, one with a thru-line where the DUT would be.
2. Measure S-parameters of each.
3. Combine via matrix algebra to extract the DUT's intrinsic 2-port S-parameters.
4. The fixture's `Y_open` and `Z_short` give you fixture parasitics; subtract them.

### Series-pair de-embedding (vendor-style)
A simpler approach when you just want ESL:
1. Measure S₂₁ vs frequency for the DUT in the fixture.
2. Find SRF (frequency at minimum |Z|).
3. **ESL = 1 / [(2π·f_SRF)²·C]** where C is the known low-frequency capacitance.
4. Subtract fixture L (estimated from a thru-trace measurement) to get part-only ESL.

This is what most vendor datasheets report — "ESL = X nH at SRF" with the implicit assumption of a standard mounting fixture.

## Why mounting-aware reporting matters
A 10 µF MLCC has **intrinsic ESL of ~ 0.4 nH** (chip internals only). The same part mounted on a typical PCB with vias to a power plane has **mounting-loop ESL of 0.5–2 nH** — i.e., the mount dominates. So:
- A vendor datasheet ESL of "0.5 nH" is typically the **chip-only** number (de-embedded), not what you measure on your board.
- Your real circuit ESL = `chip_ESL + mounting_ESL` where mounting_ESL depends on via geometry, plane spacing, pad layout.

## ESL hierarchy by case + mounting
| Configuration | Typical ESL |
|---|---|
| Reverse-geometry (0306 / 0204), via-in-pad | 0.1–0.2 nH (chip+mount) |
| LICC 8-terminal interdigitated, optimal mount | 0.05–0.1 nH |
| Standard 0402 / 0603 / 0805, standard mount | 0.5–1.0 nH |
| Standard ≥ 1206 | 1.0–2.5 nH |
| Through-hole leaded ceramic | 5–10 nH |
| Same MLCC mounted with long traces to via | ~ +1 nH per 5 mm trace |

The intrinsic chip ESL increases moderately with case size but mounting dominates for everything < 1206.

## Vendor S-parameter export

Murata SimSurfing, KEMET K-SIM, and TDK SEAT all output **Touchstone .s2p files** with the chip-only S-parameters (no fixture). The user is expected to add their own fixture model on top.

Example .s2p header:
```
! Murata GRM21BR71A106KE15L  10uF 10V X7R 0805
! Conditions: T=25°C, V_DC=0V, V_AC=0.5Vrms
# HZ S RI R 50
0.001 0.99999 0.00001  0.99 0.001  0.99 0.001  0.99999 0.00001
0.01  ...
1000000  ...
```

These .s2p files plug directly into Ansys ADS / Cadence Sigrity / Keysight ADS / SPICE simulators with S-parameter blocks.

## Implications for the MLCC simulator
The simulator should:
1. Use **chip-only ESL** as the part model (from vendor data).
2. Accept a **mounting-loop ESL** as a separate input (user-provided estimate based on layout).
3. Output **total ESL = chip + mount** as the simulated parasitic for Z(f) calculations.
4. Optionally compute mounting ESL from a layout-aware sub-model (`L_mount ≈ 0.4 · loop_length_mm` nH).

This separation is important because the same MLCC on a 4-layer board with 1 mm via vs a 12-layer board with 0.3 mm via has very different effective ESL.

## Cross-references
- [[esr-esl-srf]]
- [[vendor-spice-models]]
- [[murata-spice-library-and-curves]]
- [[decoupling-design-rules]]
- [[mlcc-pcb-layout-rules]] — mounting-loop layout

## References
- Keysight "The ABCs of De-Embedding" application note
- Signal Integrity Journal "Calibration with De-Embedding for Precise Component Measurements"
- US Patents 6,961,669 / 7,741,857 / 8,566,058 on de-embedding methodologies
