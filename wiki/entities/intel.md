---
title: Intel Corporation
type: entity
created: 2026-05-19
updated: 2026-05-19
sources:
  - nasa-batio3-mlcc-failure-mechanisms.md
  - nasa-general-reliability-model-ni-batio3.md
tags:
  - company
status: draft
importance: low
---

# Intel Corporation

US semiconductor manufacturer. Appears in this MLCC knowledge base **only** as the **end-user that surfaced the thin-layer MLCC reliability crisis** in 2010.

## The 2010 report
[[donhang-liu|Liu]] cites Intel as the source of a 2010 internal/industry report noting that as MLCC volumetric efficiency increased (thinner dielectric, more layers), **usable life of high-cap MLCCs dropped from the model-predicted "thousands of years" to as low as 5 years**. A typical Intel CPU package uses **more than 100 ceramic capacitors** for power delivery and signal integrity. With cost-pressure-driven reduction in redundancy, the failure of **one** decoupling cap can take down the whole system.

This report is what triggered the NASA NEPP-funded deep dive into BME MLCC reliability that produced the [[bme-reliability-model|Liu framework]].

## Why it shows up in NASA papers
Intel is mentioned as:
- The market driver for sub-µm BaTiO₃ dielectric (a typical Intel CPU package needs >100 caps, each smaller than the last)
- The discoverer of the field-failure pattern that motivated the reliability research
- A counter-example to the assumption that "MLCCs are free": they're not, at scale and at sub-µm dielectric thickness

## See also
- [[nasa-batio3-mlcc-failure-mechanisms]]
- [[bme-reliability-model]]
- [[case-size-geometry]] (sub-µm dielectric trade-offs)
