---
title: Taiyo Yuden
type: entity
created: 2026-05-19
updated: 2026-05-20
sources:
  - taiyo-yuden-mlcc-whitepaper.md
tags:
  - company
status: complete
importance: high
---

# Taiyo Yuden

Japanese passive-component manufacturer (太陽誘電), HQ Tokyo. The **fourth Tier-1 MLCC house** alongside [[murata]], [[samsung-electro-mechanics]], and [[tdk]]. Historically the **miniaturization leader** at small case sizes and the company with the highest commercial capacitance values (270 µF, 330 µF, 470 µF MLCC firsts).

## Notable milestones (per [[taiyo-yuden-mlcc-whitepaper|TY whitepaper]])
- **2013**: First commercial **330 µF MLCC** (1210 case).
- **2014**: First commercial **470 µF MLCC** (1812 case, 1200+ layers).
- **2016 target**: 1000 µF (announced; commercialization status varied).
- 2022/2023 (EE Times reporting): doubled capacitance in 0402 case.
- 2024+: Sub-µm dielectric layer technology in mass production.

## Product family
Naming convention: `[Prefix][Case][TCC class][Cap value][Tolerance][Suffix]`
| Prefix | V_r tier | Typical use |
|---|---|---|
| **PMK** | 2.5 V | sub-V supply rails (DDR Vtt, FPGA core) |
| **AMK** | 4 V | high-cap consumer |
| **JMK** | 6.3 V | consumer / industrial general |
| **LMK** | 10 V | bulk decoupling |
| **EMK** | 10 V | high-cap industrial |
| **GMK** | 25 V | mid-V automotive |
| **TMK** | 50 V | industrial |
| **HMK** | 100 V+ | high-voltage |

Suffix `HT` = AEC-Q200 automotive-grade (e.g., `AMK316ABJ107MLHT` = 100 µF / 4 V / 1206 / X5R / AEC-Q200).

## Differentiated technologies
- **High-value MLCC** (100+ µF): TY's strategic focus; documented MTTF 10 000 to >1 000 000 years for premium parts.
- **Acoustic noise suppression dielectric**: proprietary engineered BaTiO₃ chemistry that **suppresses piezoelectric "singing"** at high AC drive while accepting a small DC-bias-derating penalty. Targeted at notebook PC power circuits.
- **Soft termination**: heat-cycle + flex resistance, analogous to [[kemet-arcshield|KEMET FT-CAP]] / [[tdk-cga-series|TDK soft-term]].
- **Sub-µm dielectric**: production-grade thin-layer with 1200+ layers in 1812 case.

## Public technical content
- [[taiyo-yuden-mlcc-whitepaper]] — flagship positioning paper for high-value MLCC vs polymer caps.
- DigiKey: MLCC Series HQ Catalog and MLCC High Value Capacitor Catalog.
- TTI: Taiyo Yuden Resources + High Reliability Automotive Product Catalog.
- Public landing: <https://www.yuden.co.jp/en/product/solutions/mlcc/>

## See also
- [[taiyo-yuden-mlcc-whitepaper]]
- [[x5r-dielectric]] — most of TY's high-CV portfolio is X5R / X6S
- [[core-shell-batio3]]
- [[case-size-geometry]]
- [[bme-reliability-model]]
