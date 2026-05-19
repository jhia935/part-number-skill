---
title: Dopant Site Occupancy in BaTiO₃ (A vs B Site)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources: []
tags:
  - paper
---

# Dopant Site Occupancy in BaTiO₃ (A vs B Site)

A foreign cation added to BaTiO₃ can sit on the **A-site** (replacing Ba²⁺, 12-coordinated, large) or the **B-site** (replacing Ti⁴⁺, 6-coordinated, small) — or both, depending mainly on **ionic radius** and the Ba/Ti stoichiometry of the host. Site occupancy determines whether the dopant acts as a **donor** or **acceptor**, which in turn sets [[defect-chemistry-batio3|defect chemistry]], [[core-shell-batio3|core-shell formation]], and ultimately every electrical property of the part.

## Ionic radii reference (Shannon, octahedral / 12-coord. as appropriate)

| Cation | Ionic radius (Å, B-site) | Ionic radius (Å, A-site) | Typical role in BaTiO₃ |
|---|---|---|---|
| **Ba²⁺** | — | 1.61 (12-coord.) | host A-site |
| **Ti⁴⁺** | 0.61 | — | host B-site |
| **La³⁺** | 1.03 | 1.36 (12) | donor (A-site) — large ion |
| **Nd³⁺** | 0.98 | 1.27 (12) | donor (A-site) |
| **Sm³⁺** | 0.96 | 1.24 (12) | donor (A-site) |
| **Gd³⁺** | 0.94 | 1.21 (12) | donor (A-site) |
| **Dy³⁺** | 0.91 | 1.17 (12) | **amphoteric** (both A & B) |
| **Y³⁺** | 0.90 | 1.16 (12) | **amphoteric** |
| **Ho³⁺** | 0.90 | 1.16 (12) | **amphoteric** |
| **Er³⁺** | 0.89 | 1.14 (12) | **amphoteric** |
| **Yb³⁺** | 0.87 | 1.12 (12) | acceptor (B-site) — small ion |
| **Tb³⁺/⁴⁺** | 0.92 / 0.76 | 1.18 (12) | amphoteric, multi-valent |
| **Mg²⁺** | 0.72 | — | acceptor (B-site only) |
| **Mn²⁺/³⁺/⁴⁺** | 0.83 / 0.65 / 0.53 | — | acceptor; multi-valent (charge buffer) |

## The "amphoteric window"
Rare-earth ions with intermediate ionic radius — **Dy³⁺, Y³⁺, Ho³⁺, Er³⁺** — sit in a sweet spot where the size is **simultaneously close enough to Ti⁴⁺ to occupy B-sites and close enough to Ba²⁺ to occupy A-sites**. Their site distribution is set by:

1. **Ba/Ti stoichiometry**: Ba-excess (Ba/Ti > 1) → vacant Ti sites → dopants preferentially go to B-site → acceptor behavior. Ti-excess → vacant Ba sites → A-site donor.
2. **Sintering temperature & atmosphere**: higher T favors higher-entropy distribution; reducing atmosphere shifts equilibrium toward B-site.
3. **Co-doping**: the presence of Mg (forced B-site acceptor) pushes the rare-earth toward A-site for charge balance.

## Why amphoteric is desirable
- The same chemistry produces **both donor and acceptor populations** in a tuned ratio → automatic compensation of free carriers → high IR.
- The A-site rare-earth is **far from V_O** spatially (sits on cube corner, not center) → less direct interaction with the V_O electromigration pathway.
- The B-site rare-earth **traps V_O** at its first-neighbor oxygen → suppresses electromigration without becoming a leakage path itself.

Lanthanide donors **alone** (without acceptor compensation) cause [[grain-growth-dopant-pinning|rapid grain growth]] — the donor electrons screen the GB Schottky barrier, removing the natural drag. Pure acceptors (Mg only) over-suppress free carriers and create insulating but **defect-laden** ceramics. The amphoteric strategy gets both.

## The solubility ranking
The solubility of rare-earth ions on the **Ba-site** of BaTiO₃ decreases as ionic radius decreases — La³⁺ (huge) ≫ Nd³⁺ > Sm³⁺ > Gd³⁺ > Dy³⁺ ≈ Y³⁺ > Yb³⁺ (smallest). Beyond the solubility limit, the rare-earth segregates to **grain boundaries** as rare-earth-oxide secondary phases. This GB segregation is exactly what's wanted for the [[core-shell-batio3|core-shell shell + GB barrier]] microstructure.

## Implications for [[mlcc-manufacturing-process|MLCC manufacturing]]
- Tier-1 vendors **tune Ba/Ti stoichiometry** of the dielectric powder to control A/B partition ratio of rare-earth dopants. Slight Ba-excess (Ba/Ti = 1.001–1.005) is common.
- **Co-doping with Mg** at a defined Mg/RE molar ratio (typically 1–2) forces the rare-earth toward A-site, achieving the desired amphoteric balance.
- **Sintering profile** ([[sintering-profile-mlcc]]) is set so that the dopant has enough time at peak T to reach equilibrium distribution but not so much that grain growth proceeds.

## Cross-references
- [[core-shell-batio3]]
- [[defect-chemistry-batio3]]
- [[grain-growth-dopant-pinning]]
- [[batio3]]
- [[perovskite-structure]]
- [[oxygen-vacancy-migration]]

## References (web search summaries)
- ResearchGate: "Site Occupancy of Rare-earth Cations in BaTiO₃"
- Academia.edu: "Doping Effects of Dy, Y & Ho on BaTiO₃ Ceramics"
- ResearchGate: "The Doping Effects of Intermediate Rare-earth Ions (Dy, Y and Ho) on BaTiO₃ Ceramics"
- Liu et al., *JACerS* 2026, "Enhanced Reliability and Microstructure Control in Dy/Y Co-Doped BaTiO₃ Ceramics"
