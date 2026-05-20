---
title: "Polotai, Jeong et al. — Cr Additions to Ni Electrodes in Ultra-Thin BaTiO₃ MLCC (J. Electroceram. 2007)"
type: source
created: 2026-05-21
updated: 2026-05-21
sources:
  - resources/literature/polotai-2007-cr-doping-ni-electrode-academia-extract.md
tags:
  - paper
status: complete
importance: high
---

# Polotai, Jeong et al. — Cr Additions to Ni Electrodes in Ultra-Thin BME MLCC (2007)

**Source:** `resources/literature/polotai-2007-cr-doping-ni-electrode-academia-extract.md` (academia.edu HTML extract; publisher Springer PDF paywalled)
**Authors:** A. V. Polotai, T.-H. Jeong, G.-Y. Yang, E. C. Dickey, C. A. Randall (Penn State); Pascal Pinceloup, Abhijit S. Gurav (industry collaborators, KEMET/AVX)
**Journal:** *Journal of Electroceramics* 18 (2007), DOI: 10.1007/s10832-007-9124-4

## Summary

A focused electron-microscopy study of how adding **1 wt% Cr to the Ni electrode powder** changes the microstructure and continuity of Ni inner electrodes in ultra-thin BME MLCCs (0805 / 300 layers / 1 µm dielectric + 1 µm electrode). The headline finding inverts a naive expectation: **Cr doping does NOT improve electrode continuity by modifying Ni sintering kinetics**. Both pure-Ni and Cr-doped Ni pastes have **essentially identical densification curves**. Instead, Cr improves continuity by **chemically suppressing the (Ni, Ba, Ti) interfacial liquid alloy** that drives Rayleigh-Plateau electrode break-up at peak T.

This decouples two electrode-stability mechanisms that get conflated elsewhere in the literature:
1. **Shrinkage retardation** (BT nanoparticle additive — see [[sugimura-hirao-2009-batio3-additive-ni-electrode|Sugimura-Hirao]] and [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis]]).
2. **Interfacial chemistry control** (Cr doping — this paper).

Both produce **better electrode continuity** in the finished MLCC, but through entirely different physics. A well-designed BME paste recipe uses **both** levers.

## Materials & methods

- **Samples**: 0805 BME MLCC, 300 active layers, target ~1 µm dielectric thickness and ~1 µm electrode thickness — at the time, this was state-of-the-art thin-layer manufacturing.
- **Electrode powders**: pure Ni vs Ni-1 wt% Cr alloy (refractory metal addition).
- **Sintering**: 5 h dwell at multiple temperatures, reducing atmosphere typical of BME firing.
- **Characterization**:
  - **VC-SEM** (Voltage-Contrast SEM) at 2.5 kV, 7 V DC bias across electrodes — discontinuities appear dark under negative polarity; quantitatively measured as ratio of imperfection length to total electrode length, averaged over ≥ 5 images per sample.
  - **HR-TEM + EELS** (JEOL-2010 FEG-TEM, Gatan Enfina spectrometer) — for ~ 8 nm interfacial alloy layer characterization.
  - **Dilatometry** on undoped vs Cr-doped Ni pellets compared to BT pellets.

## Key findings

### 1. Cr doping does not change Ni shrinkage

Dilatometry curves for **pure Ni and Ni-1 wt% Cr pastes are essentially identical**. The shrinkage onset, peak densification rate, and final density are the same to within experimental error.

> "The undoped and Cr-doped Ni pellets produced from the corresponding electrode inks showed very similar densification curves compared to the dielectric material. The similar densification behaviors of both Cr-doped and unmodified Ni indicate that the level of elastic strain energy generated during sintering will be quite similar for both types of electrode materials, so the differences in the electrode stability cannot be attributed to differences in internal stresses."

**This is the central decoupling result.** Cr's benefit cannot be a constrained-sintering effect, because the sintering trajectory is unchanged.

### 2. Cr suppresses the (Ni, Ba, Ti) interfacial alloy

In undoped samples, sintering at ≥ 1100 °C produces a **~8 nm thick interfacial layer** of (Ni, Ba, Ti) alloy at every Ni / BaTiO₃ interface. EELS shows Ni Lₐ + Ti Lₐ + Ba Mₐ edges and **no O K edge** — confirming the layer is a reduced inter-metallic, not an oxide.

In Cr-doped samples, two interface types coexist (the original paste has inhomogeneous Cr distribution):
- **Cr-segregated interfaces**: NO alloy layer. Moiré fringes appear in the entire Ni region; EELS shows Cr Lₐ + Ni Lₐ at ~ 6.8 at% Cr / 93.2 at% Ni at the interface.
- **Non-Cr-segregated interfaces** (where Cr happens to be absent in that local region): same 8 nm alloy layer as undoped samples.

So **Cr's mechanism is interfacial segregation that chemically blocks the alloy formation** — not bulk Ni-Cr alloying.

### 3. Electrode continuity improves with Cr

Quantitative VC-SEM measurements showed that the discontinuity fraction is reduced in Cr-doped MLCCs across the sintering-temperature range, with the largest improvement at peak sintering temperatures (1200–1250 °C). The paper expresses this as **non-linear decrease in continuity** with rising T in pure-Ni samples vs **flatter / slower decline** in Cr-doped samples.

### 4. Cr diffuses into BaTiO₃ and creates V_O

The paper notes that **Cr diffusing from the electrode into the adjacent BaTiO₃ grain** generates reduced Ti³⁺ (visible in EELS) and **oxygen vacancies V_O**.

This is double-edged:
- More V_O lowers IR (worse insulation) and accelerates [[ni-batio3-cosintering-interface|interfacial barrier degradation]].
- Cr also acts as a [[defect-chemistry-batio3|donor/acceptor co-dopant]], potentially trading off some reliability for continuity.

The companion paper (Polotai, unpublished at the time of this paper) addresses the electrical-property impact.

## Why this matters for the shrinkage story

The user's question is "effect of metal electrode on shrinkage". This paper is the **counter-example** showing that metal-electrode chemistry can improve MLCC quality **without** changing the shrinkage trajectory. The two engineering levers for the Ni paste are independent:

| Lever | Mechanism | Effect on Ni shrinkage curve | Effect on electrode continuity |
|---|---|---|---|
| **Nano-BT additive** (5–15 vol%, 10–30 nm) | Bordia-Scherer rigid-inclusion retardation | **Slows Ni densification**, shifts onset to higher T | Moderate (Yan: 7× retardation factor) |
| **Cr addition** (1 wt%) | Interfacial segregation, suppresses (Ni,Ba,Ti) alloy | **No effect** | Large (continuity improved at peak T) |

A well-engineered paste uses **both**.

## Entities mentioned
- A. V. Polotai, E. C. Dickey, C. A. Randall — Penn State Center for Dielectrics and Piezoelectrics.
- KEMET / AVX (Pinceloup, Gurav) — industry collaborators.
- [[samsung-electro-mechanics]] — implicit (typical of BME industry context).

## Concepts discussed

- [[ni-electrode-paste-formulation]] — Cr is one of multiple refractory-metal additions.
- [[ni-batio3-cosintering-interface]] — the (Ni, Ba, Ti) liquid alloy that Cr suppresses.
- [[metal-electrode-shrinkage-effect]] — paper's contribution to the broader picture.
- [[defect-chemistry-batio3]] — Cr-induced V_O in BaTiO₃ grains.
- [[failure-modes-mlcc]] — electrode discontinuity as a primary failure mode.

## Notable quote

> "The interfacial alloy layer is not observed when Cr is segregated at Ni-BaTiO₃ interface in the Cr-doped samples, while it is found in all undoped samples. The interfacial alloy layer is believed to increase mass-transfer along the Ni-BaTiO₃ interfaces facilitating an acceleration of Ni electrodes discontinuities."

## References

_Source: academia.edu HTML extract of Polotai et al., J. Electroceram. 18 (2007)_
- Yang, Dickey, Randall et al. — earlier Penn State Ni/BaTiO₃ interface work that established the ~8 nm alloy layer.
- Polotai et al., "Utilization of Multiple-Stage Sintering to Control Ni Electrode Continuity in Ultrathin Ni–BaTiO₃ MLC", *J. Am. Ceram. Soc.* 90 (2007) 3811–3817 — sister paper; multi-stage thermal-profile approach.
