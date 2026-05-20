---
title: Bordia-Scherer Composite-Sintering Retardation Model
type: concept
created: 2026-05-20
updated: 2026-05-20
sources: []
tags:
  - paper
status: draft
importance: medium
---

# Bordia-Scherer Composite-Sintering Retardation Model

The foundational continuum-mechanics framework for **sintering of a powder matrix containing rigid (or slow-sintering) inclusions**. The three Bordia-Scherer papers (*Acta Metall.* 36 (1988) 2393, 2399, 2411) and the Scherer 1987 *J. Am. Ceram. Soc.* 70, 719 paper established the constitutive model that predicts how the densification rate of the matrix is reduced by the presence of inclusions.

The first-order linear bound:
$$
\frac{\dot{\varepsilon}_c}{\dot{\varepsilon}_{m,\text{free}}} \;=\; 1 - v_i
$$

where `v_i` is the inclusion volume fraction. The composite densification rate is at most (1 − v_i) times the free matrix rate. Higher-order corrections include the stress field around each inclusion and contact-substitution effects.

Direct application to MLCC: this is the textbook foundation for **why nano-BT addition retards Ni-paste sintering**. See [[ni-batio3-cosintering-interface]] for the quantitative Yan DEM table that goes far beyond the linear bound (retarding factor reaches 7× at 20 vol% / 60 nm BT in Ni, vs the linear bound's 1.25×).

## Three-paper series

1. **I — Constitutive model for a sintering body**: derives the viscous-flow constitutive equations for a porous matrix.
2. **II — Comparison of constitutive models**: compares Bordia-Scherer to Skorohod's earlier formulation; the two are equivalent under specific assumptions. Connects to the modern [[skorohod-olevsky-viscous-sintering|SOVS]] framework.
3. **III — Rigid inclusions**: derives the inclusion-induced backstress and retardation, including the linear bound above.

## Status

Draft because the original Bordia-Scherer papers are not in `resources/`. The model is well-summarized in [[rahaman-ceramic-processing-sintering-textbook|Rahaman]] Chapter 10. This page exists to give other pages ([[skorohod-olevsky-viscous-sintering]], [[constrained-sintering-mlcc]], [[ni-batio3-cosintering-interface]]) a target for the Bordia-Scherer cross-reference.

## References

- R. K. Bordia & G. W. Scherer, "On constrained sintering I, II, III", *Acta Metallurgica* 36 (1988) 2393, 2399, 2411.
- G. W. Scherer, "Sintering with Rigid Inclusions", *J. Am. Ceram. Soc.* 70 (1987) 719–725.
- D. J. Green, O. Guillon, J. Rödel, "Constrained sintering: A delicate balance of scales", *J. Eur. Ceram. Soc.* 28 (2008) 1451–1466 — modern review.
