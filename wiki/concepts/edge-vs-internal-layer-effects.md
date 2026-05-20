---
title: Edge vs Internal Layer Effects in MLCC Sintering
type: concept
created: 2026-05-21
updated: 2026-05-21
sources:
  - yan-thesis-2013-mlcc-sintering-nanotomography.md
tags:
  - paper
status: complete
importance: medium
---

# Edge vs Internal Layer Effects in MLCC Sintering

Not every dielectric or electrode layer in an MLCC stack experiences the same sintering constraint. **Edge layers** (the top and bottom of the active stack) have a free outer face, while **internal layers** are constrained on both sides by neighboring layers. The asymmetry produces real, measurable differences in shrinkage, electrode continuity, and pore alignment.

For modern 300+ layer commercial MLCCs the asymmetry is mostly hidden because the proportion of edge layers is small. But it matters for:
- **Cover-layer design** (the thick BT-only layers at the top and bottom of the stack).
- **Research-scale samples** (3–10 layers) where the asymmetry is large and easy to mistake for an intrinsic material effect.
- **Symmetry-breaking modes** (asymmetric loading, gravity sag).

## The synchrotron measurement (Yan Ch. 4)

From [[yan-thesis-2013-mlcc-sintering-nanotomography|Yan thesis (2013) Ch. 4]], using in-situ X-ray nano-CT on a representative Pd-MLCC sample with two active electrodes (E1 = top edge, E2 = internal):

| Layer | Constraint type | Final electrode discontinuity |
|---|---|---|
| **E1** (top edge) | One-sided — only one BT layer adjacent | **56.1 %** |
| **E2** (internal) | Two-sided — BT above and below | **60.4 %** |

The internal electrode is **4 percentage points more discontinuous** than the edge electrode. The mechanism, per Yan:

> "The top electrode layer has only one adjacent dielectric layer on the bottom. This layer acts as a rigid substrate and imposes a geometrical constraint. In contrast, the second electrode is constrained by both adjacent layers. This difference has consequences on the radial shrinkage but also more significantly on the degree of discontinuity."

The bilateral constraint of the internal layer:
- Restricts particle rearrangement on both faces simultaneously.
- Generates higher tensile stress in the Ni layer at Stage A (when Ni is sintering and BT is rigid).
- Amplifies the Rayleigh-Plateau break-up driving force at Stage C.

## Radial shrinkage in dielectric layers

Yan's synchrotron also tracked **radial strain in the dielectric layers**:

| Layer | Constraint | Radial shrinkage (final) |
|---|---|---|
| **D1** (top) | Bottom face against E1; free top face | Lower |
| **D2** (internal between E1 and E2) | Both faces against electrodes | Higher (closer to free) |
| **D3** (bottom edge) | Only one electrode-facing face | Lower (similar to D1) |

> "Both radial and axial strains are nearly equal in the first and second dielectric layers, which are sintered under the same constraining conditions." — Yan thesis Ch. 4.

So **the strain anisotropy of an internal dielectric layer is greater than that of an edge layer**. The thickness enhancement vs lateral suppression is more pronounced where the layer is sandwiched.

## Why research-scale samples can mislead

A 3-layer sample (BT/Ni/BT/Ni/BT in Yan's experiments) has:
- 2 edge BT layers (top + bottom)
- 1 internal BT layer
- 0 internal electrode layers (both electrodes are technically edge in this configuration)

So 67% of dielectric layers are edge, vs < 1% in a 300-layer commercial chip. **The strain measurements on small samples systematically underestimate the constraint anisotropy** that the dominant internal layers in a real part experience.

Yan's own Ch. 4.4 conclusion (3) flags this explicitly:

> "Care must be taken in interpreting results. The sintering behavior of the extracted small sample may deviate from that of a real several-hundred-layer chip. In a sample with very few layers, as used in these nano-tomographic experiments, external and internal layers are not submitted to the same constraints, thus resulting in different discontinuity levels."

This is a fundamental epistemic constraint on **all** lab-scale MLCC sintering studies: the results scale **non-monotonically** with layer count and need to be extrapolated carefully.

## Cover layer design

Commercial MLCCs include **cover layers** — extra BT-only layers (with no electrodes) at the top and bottom of the active stack, typically **30–50 µm thick per side** (see [[case-size-geometry]] for the H_max budgets). These layers serve four roles:

1. **Mechanical protection** — barrier between the active stack and the external termination / packaging.
2. **Dielectric strength margin** — distance between any active electrode and the chip surface keeps surface-creepage breakdown manageable.
3. **Free-shrinkage buffer** — cover layers shrink approximately freely on their outer face, partially absorbing edge-layer asymmetry. The next-in active dielectric layer then sees a less-extreme constraint than it would if it were truly the edge.
4. **Cooldown stress accommodator** — the thick cover layers provide compliance for the TEC mismatch between the active stack and the external termination metal.

The cover layer thickness is therefore a **designed compensation** for the edge-vs-internal asymmetry: by giving the active stack a thick passive buffer, the design ensures that the topmost active dielectric/electrode pair behaves more like an internal layer than a true edge layer.

## Implications for the simulator

A multi-layer MLCC shrinkage model should distinguish:

| Layer role | Boundary condition | Treatment in the simulator |
|---|---|---|
| **Cover layer (outer face free)** | Free in-plane strain on the outer surface | Free SOVS sintering; nearly isotropic |
| **Cover layer (inner face vs active stack)** | Constrained against active stack | Mixed; some lateral suppression |
| **Top/bottom active dielectric (D1, D_last)** | One face against electrode, other face against cover | Asymmetric constraint; ~ 10–20 % less lateral suppression than internal layers |
| **Internal active dielectric (most layers)** | Both faces against electrodes | Full bilateral constraint; maximum lateral suppression / thickness enhancement |

For a quick first-pass simulator, treating the entire active stack as "internal" introduces only a small error in chip-scale dimensions (since 95 %+ of layers are truly internal in a modern part), but it overestimates the lateral suppression at the edges. For high-fidelity stress prediction (delamination risk, cooldown crack risk), the per-layer constraint type matters.

## Cross-references

- [[dielectric-shrinkage-in-mlcc-stack]] — the parent concept page; this page details the layer-position case.
- [[constrained-sintering-mlcc]] — the constraint physics.
- [[metal-electrode-shrinkage-effect]] — the electrode-centric view.
- [[case-size-geometry]] — cover-layer dimension data.
- [[failure-modes-mlcc]] — edge-related cracking and delamination modes.

## References

- [[yan-thesis-2013-mlcc-sintering-nanotomography]] — Ch. 4.2–4.4, the three-layer synchrotron experiment that quantifies the asymmetry directly.
- Bouvard, Martin et al., "Microstructure evolution during the co-sintering of Ni/BaTiO₃ MLCC", *J. Eur. Ceram. Soc.* 34 (2014) — distillation paper.
- Olevsky, "Sintering of Multilayered Porous Structures Part I", *J. Am. Ceram. Soc.* 96 (2013) 2295 — analytical treatment of bilayer / trilayer / N-layer asymmetries.
