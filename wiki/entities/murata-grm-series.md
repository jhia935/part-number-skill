---
title: Murata GRM Series MLCC
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - murata-grm-series-tcc-data.md
tags:
  - series
status: complete
importance: high
---

# Murata GRM Series MLCC

The general-purpose MLCC family from [[murata]] — the largest single product line in the global MLCC market by volume. The series name encodes case size in the digits suffix.

## Sub-family naming
| Suffix | Case size (metric / EIA) |
|---|---|
| GRM03  | 0603 / 0201 |
| GRM15  | 1005 / 0402 (commonly the GRM155) |
| GRM18  | 1608 / 0603 |
| GRM21  | 2012 / 0805 |
| GRM31  | 3216 / 1206 |
| GRM32  | 3225 / 1210 |
| GRM43  | 4532 / 1812 |
| GRM55  | 5750 / 2220 |

(Sub-family numbers extracted from the curves in [[murata-grm-series-tcc-data]], which references GRM18/21/31/32/43/55 explicitly on its "Allowable" plots.)

## Dielectric portfolio
- **C0G** (Class I) up to ~150 V, capacitance from sub-pF to ~10 nF depending on case.
- **X5R, X6S, X7R** (Class II) — bulk of unit volume.
- **X8R, X8L** automotive-grade temperature.
- **Y5V** (Class III) — legacy bulk decoupling.

## Cousin families at Murata
- **GCM / GCJ** — AEC-Q200 automotive-grade variants.
- **GJM** — RF / high-frequency.
- **GRT** — soft-termination (flex mitigation, analogous to [[kemet]]'s FT-CAP).

## See also
- [[murata]]
- [[murata-grm-series-tcc-data]]
