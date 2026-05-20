---
title: MLCC Case Sizes & Internal Geometry
type: concept
created: 2026-05-19
updated: 2026-05-19
status: complete
importance: high
sources:
  - nasa-nepp-bme-mlcc-reliability.md
  - samsung-cl-series-mlcc-ds.md
tags:
  - paper
---

# MLCC Case Sizes & Internal Geometry

The outer case size sets a hard envelope on `L`, `W`, `H`. Internal geometry — end margin, side margin, electrode overlap area, cover (passivation) thickness, dielectric layer thickness, electrode thickness, active layer count — has to fit inside that envelope. The active overlap area `A` and the maximum `N` are derived quantities, not free parameters.

## EIA case codes vs metric
| EIA | Metric (mm) | Typical L × W (mm) |
|---|---|---|
| 008004 | 0201 | 0.25 × 0.125 |
| 01005  | 0402 | 0.4 × 0.2 |
| 0201   | 0603 | 0.6 × 0.3 |
| 0402   | 1005 | 1.0 × 0.5 |
| 0603   | 1608 | 1.6 × 0.8 |
| 0805   | 2012 | 2.0 × 1.25 |
| 1206   | 3216 | 3.2 × 1.6 |
| 1210   | 3225 | 3.2 × 2.5 |
| 1812   | 4532 | 4.5 × 3.2 |
| 2220   | 5750 | 5.7 × 5.0 |

Source: [[samsung-cl-series-mlcc-ds]] §2.

### The naming-convention pitfall
The **same digits in EIA and metric encode different physical sizes**. EIA codes derive from **0.01-inch units** (`0805` = 0.080" × 0.050"); metric codes derive from **0.1-mm units** (`2012` = 2.0 × 1.2 mm — which happens to be the same physical part as EIA `0805`). The collision becomes dangerous because **`0603` exists in both schemes with very different meanings**:

| Bare digits | EIA reading | Metric reading | Volume ratio |
|---|---|---|---|
| `0201` | 0.6 × 0.3 mm | 0.2 × 0.1 mm | **27×** |
| `0402` | 1.0 × 0.5 mm | 0.4 × 0.2 mm | **31×** |
| `0603` | **1.6 × 0.8 mm** (workhorse) | **0.6 × 0.3 mm** (ultra-tiny) | **~7×** |
| `0805` | 2.0 × 1.25 mm | 0.8 × 0.5 mm | **6×** |
| `1206` | 3.2 × 1.6 mm | 1.2 × 0.6 mm | **11×** |

A BOM or datasheet that says `"0603"` without context has bitten plenty of engineers.

### Recommended disambiguation: `i` / `m` suffix
Suffixes `i` (inch-derived EIA) and `m` (metric) make the intent explicit:

| Input | Resolves to | Notes |
|---|---|---|
| `0805` | EIA 0805 (= 2012m) | assumed EIA; **no warning** (the metric form `0805m` doesn't exist as a standard) |
| `0805i` | EIA 0805 | explicit EIA |
| `2012m` | EIA 0805 | explicit metric, same physical part |
| `0603` | EIA 0603 (= 1608m) | assumed EIA; **emit a warning** because `0603m` is a real different size |
| `0603i` | EIA 0603 | explicit workhorse cap, 1.6 × 0.8 mm |
| `0603m` | EIA 0201 | explicit metric, tiny 0.6 × 0.3 mm |
| `1608m` | EIA 0603 | unambiguous metric form for the workhorse |

The simulator's size-resolver follows this convention: bare 4-digit input is treated as EIA but **warns** for the collision-prone codes (`0201`, `0402`, `0603`, `0805`, `1206`). Explicit `i` / `m` suffixed input never warns.

### SEMCO internal size code
[[samsung-electro-mechanics|SEMCO]] CL-series part numbers use a **2-digit internal index** (field 2 of the 11-field PN) that's independent of either EIA or metric digits:

| SEMCO field | EIA | Metric | mm |
|---|---|---|---|
| `03` | 0201 | 0603 | 0.6 × 0.3 |
| `05` | 0402 | 1005 | 1.0 × 0.5 |
| `10` | 0603 | 1608 | 1.6 × 0.8 |
| `21` | 0805 | 2012 | 2.0 × 1.25 |
| `31` | 1206 | 3216 | 3.2 × 1.6 |
| `32` | 1210 | 3225 | 3.2 × 2.5 |
| `43` | 1812 | 4532 | 4.5 × 3.2 |
| `55` | 2220 | 5750 | 5.7 × 5.0 |

The simulator's [[samsung-cl-series|SEMCO]] encoder takes either user-side notation (with or without `i`/`m` suffix) and emits the correct 2-digit SEMCO field.

## Margins & overlap area
For BME construction, [[nasa-nepp-bme-mlcc-reliability]] Table II:

| Case | L (µm) | W (µm) | End margin (µm) | Side margin (µm) | Overlap A (mm²) | Scale vs 0402 |
|---|---|---|---|---|---|---|
| 0402 | 1000 | 500  | 125 | 100 | 0.225 | 1.00 |
| 0603 | 1600 | 810  | 175 | 100 | 0.763 | 3.39 |
| 0805 | 2010 | 1250 | 250 | 150 | 1.520 | 6.76 |
| 1206 | 3200 | 1600 | 250 | 150 | 3.510 | 15.60 |
| 1210 | 3200 | 2500 | 250 | 150 | 5.940 | 26.40 |
| 1812 | 4500 | 3200 | 300 | 200 | 10.920 | 48.53 |
| 2220 | 5700 | 5000 | 320 | 220 | 23.074 | 102.55 |

The **end margin** is the keep-out between the buried internal electrode tip and the termination of opposite polarity (anti-arcing distance). The **side margin** is the keep-out between the electrode edge and the chip side wall (anti-delamination, mechanical robustness).

## Height & layer count budget
Total external height:
$$
H \;=\; 2 d_\text{cover} \;+\; N (d + d_e)
$$
With `d_e ≈ 0.5–1.0 µm` for inner Ni/Cu electrodes and `d_cover ≈ 30–50 µm` per side (mechanical robustness + dielectric strength margin to the surface).

Typical published `H_max` ([[samsung-cl-series-mlcc-ds]] §7):

| Case | H_max (mm) |
|---|---|
| 0201 (0603) | 0.33 |
| 0402 (1005) | 0.55 |
| 0603 (1608) | 0.90 |
| 0805 (2012) | 1.35 |
| 1206 (3216) | 1.80 |
| 1210 (3225) | 2.80 |
| 1812 (4532) | 3.50 (option L = 3.2) |
| 2220 (5750) | 3.50 (option L = 3.2) |

Working backward: a 0805 with `d = 1 µm`, `d_e = 1 µm`, `d_cover = 50 µm/side` allows `N ≤ (1350 − 100) / 2 = 625` layers — comfortably above the 300-layer state-of-the-art commercial value.

## Volumetric-efficiency ceiling
[[nasa-batio3-mlcc-failure-mechanisms]] Fig. 2 shows that volumetric efficiency saturates around **3000–4000 µF/cm³** as `d → 0.5 µm` because `εr` collapses with grain size. Sub-µm dielectrics need [[core-shell-batio3]] microstructure engineering to keep `εr` from falling apart.

## Related
- [[mlcc-capacitance-equation]] — uses `A` and `N`
- [[bme-reliability-model]] — uses `S` (chip-size scale factor)
- [[failure-modes-mlcc]] — larger cases (>0805) are more susceptible to flex crack

## References
- [[nasa-nepp-bme-mlcc-reliability]]
- [[samsung-cl-series-mlcc-ds]]
