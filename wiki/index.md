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
- [[intel]] — CPU OEM whose 2010 thin-layer MLCC reliability report triggered the Liu NASA NEPP framework *(stub)*.

### Product series
- [[murata-grm-series]] — General-purpose Murata MLCC; GRM03 through GRM55.
- [[samsung-cl-series]] — General-purpose SEMCO MLCC; 11-field part number.
- [[kemet-arcshield]] — KEMET patented HV MLCC with internal shield electrodes.
- [[bme-c0g]] — KEMET CaZrO₃-based Class I BME family; PME-killer in C0G/NP0 territory.
- [[tdk-cga-series]] — TDK AEC-Q200-qualified automotive MLCC family (C0G/X7R/X8R; 0402–2220).

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
- [[core-shell-formation-mechanism]] — Dissolution-reprecipitation vs solid-state diffusion; the firing-stage kinetics.
- [[dopant-site-occupancy-batio3]] — A vs B site, amphoteric rare-earths, Y/Ho/Dy/Er ionic-radius window.
- [[dopant-powder-coating]] — Material-stage wet-chemical / sol-gel dopant delivery onto BaTiO₃ particles.
- [[dc-bias-aging]] — Slow capacitance drift under continuous DC bias, distinct from natural aging and from VCC.
- [[oxygen-vacancy-migration]] — Schottky-barrier-collapse mechanism behind BME IR degradation.
- [[ferroelectric-domain-wall]] — Where most of MLCC εr comes from; explains VCC, aging, and grain-size effects.
- [[mlcc-manufacturing-process]] — End-to-end process map from powder to packaged chip.
- [[bme-sintering-atmosphere]] — Reducing-atmosphere co-firing with PO₂ control.
- [[re-oxidation-anneal]] — Post-sinter step that refills oxygen vacancies and raises IR.
- [[batio3-powder-synthesis]] — Hydrothermal, solid-state, oxalate, sol-gel routes; size distribution control.
- [[sintering-kinetics-batio3]] — Mass-transport mechanisms, densification rate, activation-energy hierarchy.
- [[grain-growth-dopant-pinning]] — Normal/abnormal grain growth, solute drag, Zener pinning, co-doping strategy.
- [[defect-chemistry-batio3]] — Kröger-Vink notation, V_O equilibria, donor/acceptor compensation.
- [[ni-batio3-cosintering-interface]] — Interfacial (Ni,Ba,Ti) liquid alloy, electrode discontinuity physics.
- [[cubic-tetragonal-transition]] — T_C cooldown physics: domain formation, twinning, stress relief vs grain size.
- [[sintering-aids-glass]] — BBS, ZBS, PBS glass systems; lowering sintering T for Cu BME and LTCC.
- [[sintering-profile-mlcc]] — Industrial heating-rate / multi-stage profile (200 → 3000 °C/h study, 1250 °C peak).
- [[two-step-sintering]] — Chen-Wang TSS-CW method; density without grain growth (BaTiO₃ at 35 nm grain).
- [[constrained-sintering-mlcc]] — In-plane vs thickness shrinkage anisotropy; camber/warpage origin.
- [[spark-plasma-sintering]] — SPS / FAST; 99 % density in minutes, ~doubled εr.
- [[cold-sintering]] — Sub-300 °C densification with transient liquid phase (Randall group).

### Dielectric class deep-dives
- [[c0g-npo-dielectric]] — Class I ultra-stable; CaZrO₃ or BaNd-titanate base; the only "textbook ideal" cap.
- [[x7r-dielectric]] — Class II workhorse; ±15 % over −55…+125 °C; BaTiO₃ core-shell.
- [[x5r-dielectric]] — Class II lower-T; ±15 % to +85 °C; consumer-dominant.
- [[x8r-x8l-x9r-high-temperature-dielectrics]] — Above-125 °C extensions; automotive standard; X0U / X9V for 175–200 °C.
- [[y5v-z5u-class-iii-dielectric]] — Class III high-K; +22/−82 %; legacy, being phased out.

### Primitives (foundational concepts)
- [[permittivity]] — Dielectric constant εᵣ; the fundamental material property.
- [[polarization-mechanisms]] — Electronic / ionic / dipolar / space-charge polarization.
- [[perovskite-structure]] — ABO₃ crystal framework underlying every MLCC dielectric.
- [[curie-temperature]] — Ferroelectric-to-paraelectric transition; the aging-clock reset point.
- [[temperature-coefficient-of-capacitance]] — TCC; Class I letter-code, Class II envelope.
- [[dissipation-factor]] — DF / tan δ; dielectric loss spec.
- [[dielectric-breakdown]] — Intrinsic vs defect-limited vs surface arcing.
- [[insulation-resistance]] — IR(t, V, T); the BME reliability proxy.
- [[heywang-jonker-model]] — Schottky double-depletion grain-boundary barrier model.
- [[prokopowicz-vaskas-equation]] — Single-mode reliability-acceleration equation.
- [[weibull-distribution]] — Two-parameter Weibull for TTF statistics.
- [[termination-and-plating]] — Cu/Ni/Sn external electrode stack.

### Application-layer design rules
- [[vendor-spice-models]] — Murata SimSurfing, K-SIM, SpiCap, SEAT: static vs dynamic SPICE models, how a simulator consumes them.
- [[murata-spice-library-and-curves]] — Practical: netlist structure + digitized DC-bias / TCC / aging values from GRM Series data.
- [[kemet-k-sim-tool]] — KEMET / Yageo K-SIM; what it exposes vs SimSurfing; built-in lifetime model for non-ceramic capacitors.
- [[decoupling-design-rules]] — PDN target impedance, "myth of 3 cap values", same-value-paralleled approach, ESR-controlled damping.
- [[mlcc-pcb-layout-rules]] — IPC-7351 pad design, anti-tombstoning, flex-zone exclusion, reflow profile.
- [[s-parameter-de-embedding-mlcc]] — How to separate chip ESL from fixture parasitics; chip-vs-mounting ESL hierarchy.
- [[nano-grain-batio3-epsilon-r]] — Quantitative εr vs grain size 5 µm → 10 nm; critical size; dead-layer model.

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
- [[epfl-ceramics-sintering-microstructure]] — EPFL TP3 lab guide; canonical solid-state sintering physics.
- [[arxiv-electron-localization-cation-diffusion]] — Yu et al. 2018, DFT showing why reducing atmosphere accelerates BaTiO₃ grain growth.
- [[arxiv-batio3-cubic-to-tetragonal-md]] — First-principles MD of the cubic↔tetragonal phase transition.
- [[nasa-time-dependent-ir-2013-prb]] — Liu PRB 2013, exponential IR-degradation law derivation + E_k 1.6/2.8 eV fits.
- [[cold-sintering-annual-review-mse]] — Guo, Randall et al. 2019, authoritative cold-sintering review.
- [[llnl-particle-rigid-body-sintering]] — LLNL, rigid-body particle rearrangement in early-stage sintering.
- [[arxiv-batio3-silica-interdiffusion]] — Nuzhnyy et al. 2011, BaTiO₃@SiO₂ core-shell composites; interdiffusion creates strong THz dielectric dispersion.
- [[taiyo-yuden-mlcc-whitepaper]] — TY mid-2010s flagship; documents 100-470 µF MLCC commercialization, MTTF 10⁴-10⁶ yr claims, acoustic-noise dielectric.
- [[srep-batio3-grain-size-unfolding]] — Sci. Rep. 9953 (2015), cross-method survey: εr peak at 0.8-1.1 µm, drops below 1000 at 50 nm, c/a → 1.000 at 100 nm.
- [[aec-q104-rev-a-2025]] — Official AEC-Q104 Rev A (Nov 2025); MCM qualification framework for capacitors-embedded-in-modules.

## Comparisons

- [[dielectric-class-comparison]] — Master table covering every commercially significant TCC code (Class I C0G/U2J/extended; Class II X5R/X7R/X8R/X8L/X0U/X9R; Class III Y5V/Z5U) with εr ranges, tolerances, T_op, aging, applications.

## Queries

_No queries yet._
