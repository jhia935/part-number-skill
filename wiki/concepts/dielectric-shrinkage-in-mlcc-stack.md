---
title: BaTiO₃ Dielectric Layer Shrinkage in the BME MLCC Stack
type: concept
created: 2026-05-21
updated: 2026-05-21
sources:
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
  - hagymasi-ltcc-ferrite-dielectric-cofiring.md
  - shi-2023-jecs-sovs-bilayer-modeling.md
tags:
  - paper
status: complete
importance: high
---

# BaTiO₃ Dielectric Layer Shrinkage in the BME MLCC Stack

A free BaTiO₃ green tape sinters approximately isotropically. **In the alternating Ni / BT / Ni / BT … stack of a BME MLCC, it does not.** The metal electrode layers above and below each ceramic layer act as in-plane constraining sheets and reshape the dielectric's shrinkage in five connected ways:

1. **Macroscopic strain anisotropy** — in-plane shrinkage suppressed, thickness shrinkage enhanced.
2. **Stress-state reversal during the firing cycle** — Ni-tensile early, BT-tensile late.
3. **Pore-orientation anisotropy** in the ceramic layer.
4. **Through-thickness density gradient** within each ceramic layer.
5. **Layer-position effect** — edge layers behave differently from internal layers.

This page synthesizes all five from the [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis (2013)]] (synchrotron nano-CT + FIB-SEM + DEM) and complementary LTCC data, with the explicit aim of feeding a quantitative simulator.

## 1. Strain anisotropy at the chip and layer scale

### Chip-scale (synchrotron, [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan Ch. 4]])

In-situ X-ray nano-CT of a Pd-MLCC representative volume sintered in real time gives **radial and axial strain trajectories per dielectric layer**:

| Stage | Radial strain (ε_r) | Axial strain (ε_a) | Anisotropy (ε_a − ε_r) |
|---|---|---|---|
| Below ~1000 °C (BT cold) | ≈ 0 | ≈ 0 | 0 — isotropic |
| 1000–1100 °C (BT starts) | small | larger | growing |
| End of sinter cycle | ~ −0.15 | ~ −0.25 | **~ 0.10** |

The dielectric layer ends up with **~10 % more linear shrinkage in the thickness direction than in the radial direction**. The mechanism is in-plane tensile stress from the BT-Ni sintering-rate mismatch: BT wants to contract in plane but is held back by the surrounding sintered Ni, and via Poisson coupling its thickness contraction accelerates.

### Chip-scale (dilatometry, [[hagymasi-ltcc-ferrite-dielectric-cofiring|Hagymási LTCC analog]])

Direct measurement on a DT/FT/DT sandwich:

| Direction | Free DT shrinkage | Constrained DT/FT/DT shrinkage | Suppression / enhancement |
|---|---|---|---|
| x (cast) | 12.7 % | **3.25 %** | 4× suppressed |
| y (cross) | 13.9 % | **2.97 %** | 5× suppressed |
| z (thick) | 12.8 % | **33.1 %** | 2.6× enhanced |

Total volume shrinkage is approximately conserved. In an MLCC stack with Ni electrodes top + bottom of every BT layer, the same physics applies — just with a smaller magnitude because the Ni layer also shrinks.

### Layer-scale (FIB-nT)

Within a single dielectric layer of ~ 2–3 µm thickness, the constraint is **strongest near the Ni interface** (top and bottom faces of the BT layer) and weakest near the middle. This produces the density gradient discussed in §4 and **a depth-dependent shrinkage profile** — the BT layer is partly constrained at the interfaces, partly free in its center.

## 2. Stress-state reversal during the firing cycle

The Ni-vs-BT shrinkage onset gap (~450 °C onset for Ni paste, ~950 °C for BT — see [[ni-batio3-cosintering-interface]]) causes **two distinct stress regimes**:

| Stage | T range | Ni state | BT state | Ni stress | BT stress |
|---|---|---|---|---|---|
| **A** | 450 → 950 °C | Sintering, ~25–35 % linear contraction | Cold, rigid | **Tensile** (constrained by cold BT) | **Compressive** (BT is pulled by Ni's contraction across the interface) |
| **B** | 950 → 1050 °C | Done densifying, ~rigid | Initial-stage sintering | Tensile decreasing | **Tensile decreasing** |
| **C** | 1050 → 1250 °C | Quasi-rigid, viscous | Final-stage densification | **Compressive** (BT squeezes the now-dense Ni in plane) | **Tensile** (in plane; constrained by sintered Ni sheet) |

The interesting subtlety: the BT dielectric experiences **compressive stress early** (Stage A) and **tensile stress late** (Stage C). The compressive Stage-A stress accelerates BT particle rearrangement and densification — the BT layer actually *benefits* from the Ni contraction. The tensile Stage-C stress is what drives layer-scale shrinkage anisotropy and pore elongation.

This stress reversal is **the defining feature of constrained sintering in alternating-layer multilayers** and is qualitatively different from sintering a BT tape against a single inert rigid substrate.

## 3. Pore-orientation anisotropy in BT

From [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan FIB-nT Ch. 5.7.1]] on a sintered BT layer:

| Plane | Green tape pore alignment | Sintered pore alignment |
|---|---|---|
| **x'y'** (parallel to tape casting) | ~ 3 % of pores aligned at 0° | **~ 11 % aligned at 0°** — clear preferred direction |
| **y'z'** (perpendicular to casting, through thickness) | randomly distributed | Weak alignment with horizontal (in-plane) direction |
| **xz** (vertical cross-section) | 8 % at 140–160° (casting direction) | Increases in the same direction |

Pores in the sintered BT preferentially elongate **parallel to the layer plane** (i.e., horizontal). The mechanism is two-stage:
1. Early (Stage A, compressive on BT): pores elongate **perpendicular to the compressive load**, i.e., in the lateral direction. This is the sinter-forging analog.
2. Late (Stage C, tensile on BT): pores should reorient vertically, but **the kinetics are too slow** to undo the early alignment.

Result: the BT dielectric ends up with a **pancake-shaped pore population**, oriented in-plane. This has consequences for:
- **Dielectric breakdown** ([[dielectric-breakdown]]): elongated horizontal pores in the field direction are *less* dangerous than vertical pores in the field direction, but they reduce effective dielectric volume.
- **Capacitance**: A in [[mlcc-capacitance-equation|C = εr · ε₀ · A · N / d]] gets reduced by the in-plane pore area fraction.
- **Reliability**: oriented voids are stress concentrators for cooldown TEC mismatch.

## 4. Density gradient within each BT layer

From [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan FIB-nT Ch. 5.7.2]]:

> "In each single BT layer (D1, D2, and D3), the surface region (interface) is much denser than the middle region."

**Counter-intuitive but verified**: the part of the BT layer touching the Ni electrode is *denser* than the part in the middle. This is the opposite of free thin-film-on-rigid-substrate sintering ([[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]], Guillon 2007, Bernard's work) where the substrate-adjacent region is the *less*-dense one.

Mechanism: in MLCC the "rigid substrate" (Ni layer) is itself sintering and contracting at the same time as the dielectric. The early compressive stress from Ni's contraction (Stage A) **densifies the BT region adjacent to the interface** by particle rearrangement under hydrostatic-like compression. The middle of the BT layer is shielded from this compressive load and densifies later under tensile load (Stage C), reaching a lower final density.

Quantitative: Yan's D1/D2/D3 layers showed **interface-region density ~ 60–61 % vs middle-region density ~ 39 %** in the green compact, and the difference persists through sintering. The middle is the structural weak point of the dielectric layer.

## 5. Layer-position effect (edge vs internal)

From the synchrotron nano-CT of a 3-layer Pd-MLCC sample ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan Ch. 4]]):

| Layer | Constraint type | Final electrode discontinuity |
|---|---|---|
| E1 (top edge) | One-sided (only one BT layer adjacent) | **56.1 %** |
| E2 (internal) | Two-sided (BT above and below) | **60.4 %** |

The internal electrode is **more discontinuous** than the edge electrode because it experiences bilateral constraint. The dielectric layer adjacent to an internal electrode therefore sees more stress and shows more anisotropy than dielectric layers in edge positions.

> "In a sample with very few layers, as used in these nano-tomographic experiments, external and internal layers are not submitted to the same constraints, thus resulting in different discontinuity levels." — Yan thesis Ch. 4.4 conclusion (3).

**Implication for MLCC manufacturing**: in modern 300+ layer parts, the vast majority of dielectric layers are "internal" and experience the bilateral constraint. The top and bottom 1–2 layers ("cover layers" in industry parlance) are mechanically different and are usually made thicker as a designed safety margin. See [[edge-vs-internal-layer-effects]].

## How electrode geometry shapes the dielectric shrinkage

### Electrode thickness `h_Ni` (Yan DEM Ch. 7.7)

For a fixed BT layer thickness (2.4 µm), varying `h_Ni`:

| `h_Ni` (µm) | Equivalent Ni particle layers | Electrode discontinuity |
|---|---|---|
| 0.2 | 1 | **24.3 %** |
| 0.4 | 2 | 8.0 % |
| 0.6 | 3 | 4.6 % |
| 1.0 | 5 | **2.3 %** |

Thinner Ni → more discontinuity in the metal layer. But importantly, **the dielectric layer between a thinner Ni and the next thinner Ni experiences less constraint** because the Ni layer's effective stiffness is reduced. So the relationship to dielectric shrinkage anisotropy is:

- **Thicker Ni → more rigid constraint → more BT lateral suppression and thickness enhancement.**
- **Thinner Ni → softer constraint → BT shrinkage moves toward isotropic free sintering.**

This is one of the engineering trade-offs in modern thin-layer MLCC: shrinking `h_Ni` reduces material cost and chip height but **also reduces the in-plane shrinkage suppression** the simulator's stack-dimension model relies on.

### Electrode coverage area fraction

In a real MLCC the electrode covers ~ 80–90 % of the chip in-plane area (a margin is left for the termination side). The remaining ~ 10–20 % of the BT layer in the margin region sees **only side-on constraint** from neighboring layers — its lateral shrinkage is much closer to the free-sintering value.

This is observable in fired MLCCs: the **margin region** ([[case-size-geometry|end margin]]) bows slightly inward because the BT shrinks more freely there than in the central electrode-covered region. Vendors compensate by designing the green sheet with a slightly thicker margin region.

### `h_Ni / h_BT` ratio (Jean-Chang)

For thin-layer modern MLCC where `h_Ni ≈ h_BT ≈ 1 µm`, the Ni layer is no longer a thin film embedded in BT — it is a structural member of comparable stiffness. The dielectric and electrode layers **co-determine** the shrinkage:

- `h_Ni / h_BT << 1` (thin electrode, thick dielectric): BT controls the shrinkage trajectory; dielectric anisotropy is small.
- `h_Ni / h_BT ≈ 1` (modern thin-layer): the two compete; differential shrinkage stress at every interface is large.
- `h_Ni / h_BT >> 1` (thick electrode): Ni constraints dominate; BT lateral shrinkage strongly suppressed.

See [[cofiring-camber-bilayer]] for the Jean-Chang formula that quantifies this.

## DEM-confirmed pair anisotropy ([[yan-thesis-2013-mlcc-sintering-nanotomography|Yan Ch. 7.9]])

At the particle-pair scale in a crystalline-packed BT/Ni/BT trilayer:

| Contact type | Vertical (z) vs horizontal | Mechanism |
|---|---|---|
| BT–BT | **Vertical contacts grow more** | Compressive stress on BT (from Ni contraction) facilitates vertical neck growth |
| Ni–Ni | **Vertical contacts grow LESS** | Tensile stress on Ni (constrained by cold BT) hinders vertical neck growth |

The anisotropy is **more pronounced for Ni–Ni than for BT–BT contacts** because Ni sinters earlier and faster. This particle-scale anisotropy compounds through the layer to produce the macroscopic strain anisotropy in §1.

## How the simulator should model dielectric shrinkage in the stack

A high-fidelity dielectric-layer shrinkage prediction in a BME MLCC needs:

| Input | Source | Output |
|---|---|---|
| BT tape `η_BT(T)`, `ρ_g,BT` | Free-tape dilatometry | Free-shrinkage trajectory |
| Ni paste `η_Ni(T)`, `ρ_g,Ni` | Free-paste dilatometry | Constraining-layer stiffness vs T |
| `h_BT`, `h_Ni` | Green sheet + print spec | Geometric constraint factor |
| Electrode coverage area % | Print pattern | Margin-region correction |
| Layer count, edge/internal flag | Stack design | Per-layer constraint type |
| Sintering profile | Recipe | Time integration of stress field |

Output:
- Chip-scale 3D linear shrinkage (anisotropic per [[constrained-sintering-mlcc]]).
- Per-layer thickness shrinkage trajectory.
- Stress field that, combined with [[cubic-tetragonal-transition|cooldown TEC mismatch]], feeds back into ferroelectric domain formation.
- BT pore-orientation distribution → effective `A` reduction for [[mlcc-capacitance-equation|capacitance prediction]].
- Density-gradient profile within each BT layer → IR / [[dielectric-breakdown]] prediction.

The [[skorohod-olevsky-viscous-sintering|SOVS]] framework with anisotropic `φ`, `ψ` per layer can compute all of this on a laptop ([[shi-2023-jecs-sovs-bilayer-modeling|Shi 2023]] proved this for ZnO bilayers; the extension to MLCC is direct).

## Cross-references

- [[constrained-sintering-mlcc]] — the underlying lateral-vs-thickness physics.
- [[metal-electrode-shrinkage-effect]] — the parent concept (electrode-centric view).
- [[edge-vs-internal-layer-effects]] — layer-position dependence in detail.
- [[ni-batio3-cosintering-interface]] — what happens chemically at the Ni/BT contact.
- [[cofiring-camber-bilayer]] — Jean-Chang camber theory.
- [[skorohod-olevsky-viscous-sintering]] — quantitative continuum framework.
- [[green-tape-shrinkage-anisotropy]] — free-tape anisotropy (the input, before constraint kicks in).
- [[case-size-geometry]] — margin region and `H_max` budgeting.

## References

- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — Chapters 4, 5, 7. The most thorough single source for all five effects on this page.
- Bouvard, Martin et al., "Microstructure evolution during the co-sintering of Ni/BaTiO₃ MLCC modeled by DEM", *J. Eur. Ceram. Soc.* 34 (2014) — the published distillation of Yan thesis Ch. 6-7.
- Olevsky, "Sintering of Multilayered Porous Structures: Part I — Constitutive Models", *J. Am. Ceram. Soc.* 96 (2013) 2295–2304 — analytical continuum framework.
- Tzeng & Jean, "Stress Development during Constrained Sintering of Alumina/Glass/Alumina Sandwich Structure", *J. Am. Ceram. Soc.* 85 (2002) 335–340 — the canonical trilayer benchmark.
- Ollagnier et al., "Constrained Sintering of a Glass Ceramic Composite: II. Symmetric Laminate", *J. Am. Ceram. Soc.* 92 (2009) — symmetric-laminate analog.
- Guillon, "Microstructural Characterization of Alumina Films During Constrained Sintering", *J. Am. Ceram. Soc.* 93 (2010) 627–629 — interface-region density anomaly in the free thin-film case.
