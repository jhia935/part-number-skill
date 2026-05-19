---
title: Wiki Index
type: index
created: 2026-05-19
updated: 2026-05-19
---

# Wiki Index

A catalog of all pages in this wiki, organized by category. See [[overview]] for a high-level synthesis and [[log]] for chronological activity.

## Entities

### Companies
- [[murata]] — World's largest MLCC manufacturer; BME pioneer (1982); ~100 nm BaTiO₃ powder.
- [[samsung-electro-mechanics]] — Largest Korean MLCC house (SEMCO); active Tb-Dy dopant patent activity.
- [[tdk]] — Japanese Tier-1, broad commercial + automotive lineup; full C-series dimensional table now captured.
- [[taiyo-yuden]] — Japanese Tier-1, miniaturization leadership at small case sizes *(stub)*.
- [[kemet]] — Yageo subsidiary; ArcShield HV MLCC; canonical training references.
- [[vishay]] — Vitramon-brand PME X7R; Tier-1 publisher of DC-bias-aging data.
- [[kyocera-avx]] — Cu-electrode RF MLCCs; classic decoupling-design paper.
- [[yageo]] — Taiwanese parent of KEMET; AEC-Q200 spec contributor *(stub)*.
- [[rohm]] — Switching-regulator IC vendor; MLCC application-note authority *(stub)*.

### Product series
- [[murata-grm-series]] — General-purpose Murata MLCC; GRM03 through GRM55.
- [[samsung-cl-series]] — General-purpose SEMCO MLCC; 11-field part number.
- [[kemet-arcshield]] — KEMET patented HV MLCC with internal shield electrodes.
- [[bme-c0g]] — KEMET CaZrO₃-based Class I BME family; PME-killer in C0G/NP0 territory.

### Materials
- [[batio3]] — Barium titanate; the dominant Class II/III dielectric base.
- [[cazro3]] — Calcium zirconate; modern Class I BME C0G dielectric base.
- [[srtio3]] — Strontium titanate; Curie-point shifter in BST formulations, reliability-physics reference.
- [[nanbo3]] — Sodium niobate; lead-free X8R/X9R extension, antiferroelectric energy-storage material.

### People
- [[donhang-liu]] — NASA Goddard NEPP capacitor reliability specialist; authored the BME reliability framework.

### Organizations
- [[nasa-nepp]] — NASA Electronic Parts and Packaging program; primary public sponsor of BME reliability research.
- [[aec-council]] — Automotive Electronics Council; publisher of AEC-Q200 automotive passive qualification spec.

## Concepts

- [[mlcc-capacitance-equation]] — `C = εr·ε₀·N·A/d` and what each factor is.
- [[eia-rs-198-dielectric-classes]] — Letter-code decoder for C0G, X7R, X5R, X8L, Y5V, etc.
- [[dc-bias-derating]] — VCC effect, field-not-voltage, sigmoid fit for the simulator.
- [[aging-class-2]] — Logarithmic capacitance decay; de-aging above Curie.
- [[bme-vs-pme]] — Base-metal vs precious-metal electrode trade-offs.
- [[bme-reliability-model]] — Liu's three-factor model: structure × acceleration × Weibull.
- [[case-size-geometry]] — EIA case codes, margins, overlap area, height/N budget.
- [[esr-esl-srf]] — Parasitics, equivalent-circuit impedance, decoupling rules.
- [[failure-modes-mlcc]] — Cracks (mechanical/thermal/flex), arcing, mitigation hierarchy.
- [[core-shell-batio3]] — Rare-earth-doped microstructure that makes thin-layer BME work.
- [[dc-bias-aging]] — Slow capacitance drift under continuous DC bias, distinct from natural aging and from VCC.
- [[oxygen-vacancy-migration]] — Schottky-barrier-collapse mechanism behind BME IR degradation.
- [[ferroelectric-domain-wall]] — Where most of MLCC εr comes from; explains VCC, aging, and grain-size effects.
- [[mlcc-manufacturing-process]] — End-to-end process map from powder to packaged chip.
- [[bme-sintering-atmosphere]] — Reducing-atmosphere co-firing with PO₂ control.
- [[re-oxidation-anneal]] — Post-sinter step that refills oxygen vacancies and raises IR.
- [[batio3-powder-synthesis]] — Hydrothermal, solid-state, oxalate, sol-gel routes; size distribution control.

## Sources

- [[kemet-mlcc-design-and-characteristics]] — KEMET/PSMA 2019, construction + failure modes + ArcShield.
- [[psma-ceramic-capacitor-basics]] — KEMET/PSMA 2017, dense quantitative reference deck.
- [[vishay-x7r-cap-drift-dc-bias]] — Coppens et al. 2021, DC-bias aging benchmark.
- [[kyocera-avx-esr-esl-decoupling]] — Cain CARTS 1997, SPICE study of decoupling.
- [[murata-grm-series-tcc-data]] — Murata reference curves for the GRM family.
- [[samsung-cl-series-mlcc-ds]] — SEMCO datasheet, Rosetta stone for vendor codes.
- [[nasa-nepp-bme-mlcc-reliability]] — Liu 2013 framework paper.
- [[nasa-batio3-mlcc-failure-mechanisms]] — Liu & Sampson CARTS 2012 (Outstanding Paper).
- [[nasa-general-reliability-model-ni-batio3]] — Liu CARTS 2014, BME P-V fitted n=4.5 evidence.
- [[electrical-integrity-dce11-200]] — Novak DesignCon 2011, cross-vendor measured DC/AC bias data.
- [[epci-high-cv-mlcc-bias-aging]] — Zednicek 2019, multiplicative-factor formula `C_actual = C·F_DCV·F_ACV·F_T·F_age`.
- [[aec-q200-rev-e-2023]] — Official AEC-Q200 Rev E ceramic-capacitor stress qualification table.
- [[rohm-ceramic-cap-app-note]] — ROHM 2020, MLCC size/thickness/V_r DC-bias comparison.
- [[escies-bme-mlcc-high-reliability]] — Gurav et al. KEMET, BME C0G + X7R high-reliability synthesis.
- [[nasa-ir-degradation-ni-batio3-2015]] — Liu IEEE TCPMT, Schottky barrier model on 3 commercial BME parts.
- [[nasa-time-dependent-ir-2013-prb]] — Liu PRB manuscript, exponential leakage law derivation + E_k 1.6/2.8 eV fits.
- [[arxiv-batio3-domain-wall-motion]] — Gurung et al. arXiv 2024, Landau-Ginzburg domain-wall dielectric response.
- [[nasa-cracking-low-voltage-mlcc]] — Teverovsky NASA NEPP 2018, encyclopedic cracking & process review.
- [[octopart-tdk-cga8l3c0g-product-guide]] — TDK 2012 full MLCC product line-up (C-series + CGA + CKC).

## Comparisons

_No comparisons yet._

## Queries

_No queries yet._
