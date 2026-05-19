---
title: "Gurung et al. — Extrinsic Dielectric Response due to Domain Wall Motion in Ferroelectric BaTiO₃ (arXiv 2024)"
type: source
created: 2026-05-19
updated: 2026-05-19
sources:
  - resources/literature/arxiv-batio3-domain-wall-motion.md
tags:
  - paper
status: complete
importance: medium
---

# Gurung et al. — Extrinsic Dielectric Response due to Domain Wall Motion in BaTiO₃

**Source:** `resources/literature/arxiv-batio3-domain-wall-motion.md` (PDF: `resources/literature/pdf/arxiv-batio3-domain-wall-motion.pdf`)
**Authors:** Ashok Gurung, Mohammad Fatin Ishtiyaq, S. Pamir Alpay, John Mangeri, Serge Nakhmanson
**Affiliation:** University of Connecticut (UConn) Physics + Materials Science; Technical University of Denmark (CAMD)
**Venue:** arXiv:2407.20354, July 2024 (AFRL distribution-A release)

## Summary

A computational physics study using Landau-Ginzburg continuum theory to quantify how **180° ferroelectric domain walls (DWs)** in tetragonal BaTiO₃ contribute to the small-signal dielectric susceptibility. The paper formalizes a long-suspected truth in MLCC engineering: **most of the εr in a fine-grain BaTiO₃ ceramic comes from domain-wall motion, not from intra-domain dipole response**.

## Key quantitative anchors

- Tetragonal-to-cubic Curie temperature for bulk BaTiO₃: **T_C = 393 K (120 °C)**
- DW dielectric susceptibility exceeds the monodomain intrinsic susceptibility by **nearly 2 orders of magnitude** (extrinsic contribution dominates).
- Characteristic dielectric-loss-peak frequency:
  - Monodomain BaTiO₃: ~500 GHz
  - 180° domain-wall vibration: **~10 GHz**
- DW dynamics decompose into **sliding** (rigid-plane motion, lower-frequency) and **breathing** (profile-thickness oscillation, higher-frequency) modes — analogous to ferromagnetic-DW dynamics.
- The DW contribution grows sharply as `T → T_C`.

## Why this matters for MLCC design
1. The published `εr` of a ceramic is mostly a **DW contribution** — engineering `εr` is engineering DW density and mobility.
2. The frequency response of an MLCC's capacitance (the `εr(f)` rolloff seen in vendor curves) is dominated by DW dynamics in the GHz range; below GHz, εr is roughly flat.
3. The aging law (`C(t) = C₀ · (1 − A·log₁₀(t))`) reflects slow DW re-arrangement seeking a lower-energy domain configuration — a direct corollary of this DW physics framework.
4. DC bias **pins DWs**, removing the DW contribution from `εr` — the mechanistic explanation for [[dc-bias-derating]].

## Implications for simulator
The `εr(f, T)` term in the simulator should explicitly capture DW frequency rolloff (sub-100 MHz flat, drop near ~10 GHz). For aging, DW re-arrangement is the physical basis.

## Concepts discussed
- [[ferroelectric-domain-wall]]
- [[batio3]]
- [[dc-bias-derating]]
- [[aging-class-2]]
- [[curie-temperature]]

## Entities mentioned
- UConn Physics / Materials Science (Nakhmanson group)

## References
_Original source: `resources/literature/arxiv-batio3-domain-wall-motion.md`_
