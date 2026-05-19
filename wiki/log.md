---
title: Activity Log
type: log
created: 2026-05-19
updated: 2026-05-19
---

# Activity Log

Chronological record of wiki operations. Newest entries first.

---

## [2026-05-19] ingest | Sintering-physics pass — 5 new sources, 6 new concept pages

Directive: research the physics of dielectric material during the sintering process. Targeted five sub-topics — mass transport, grain growth, defect chemistry, Ni co-sintering, phase transition.

New raw sources (in `resources/literature/`):
- [[epfl-ceramics-sintering-microstructure]] — EPFL TP3 lab guide. The clean teaching reference for solid-state sintering physics: 4 mass-transport mechanisms, Q_surf < Q_GB < Q_volume activation energy hierarchy (α-Al₂O₃ 399/464/616 kJ/mol, ZnO 158/282/376), Young-Laplace curvature driving force, dilatometry protocol.
- [[arxiv-electron-localization-cation-diffusion]] — Yu et al. arXiv:1808.05198. DFT explanation for why reducing atmosphere accelerates BaTiO₃ grain growth: Ti⁴⁺ → Ti³⁺ + electron localization lowers cation migration barrier 30–50 %.
- [[arxiv-batio3-cubic-to-tetragonal-md]] — arXiv:1010.6147. First-principles MD of the T_C transition; soft-phonon precursor region above T_C explains εr peak.
- LLNL particle rigid-body motion in sintering, Cold sintering Annual Review (in resources/literature/, source pages pending).

New wiki concept pages (the deliverable):
- [[sintering-kinetics-batio3]] — Mass-transport framework + BaTiO₃-specific activation energies (Q ≈ 119–172 kJ/mol for grain growth).
- [[grain-growth-dopant-pinning]] — Normal vs abnormal grain growth; solute drag, Zener pinning; lanthanide-donor vs acceptor-cation grain-growth behaviors; the Y+Mg co-doping consensus.
- [[defect-chemistry-batio3]] — Kröger-Vink notation, O₂ ⇌ V_O + 2e' equilibrium, Ti³⁺/Ti⁴⁺ redox, donor/acceptor compensation strategies. The chemistry layer under the BME atmosphere recipe.
- [[ni-batio3-cosintering-interface]] — The interfacial (Ni, Ba, Ti) liquid alloy at 1000–1100 °C that drives electrode discontinuity; NiO 0.13 wt% solubility limit in BaTiO₃ pins GBs.
- [[cubic-tetragonal-transition]] — Cooldown through T_C; 90° twin domains relieve stress in coarse grain; **fine grains lack room for 90° twins → εr collapses below ~200 nm** (structural origin of the grain-size cliff).
- [[sintering-aids-glass]] — BaO-B₂O₃-SiO₂ / ZnO-B₂O₃-SiO₂ glass aids; reduce BaTiO₃ sintering T from 1300 °C to 900 °C; essential for BME Cu C0G firing below Cu melting point.

New wiki source pages: 3 ([[epfl-ceramics-sintering-microstructure]], [[arxiv-electron-localization-cation-diffusion]], [[arxiv-batio3-cubic-to-tetragonal-md]]).

Updated `resources/design-rules/simulator-model.md` §9 (sintering physics anchors), §10 (source registry extended). Updated `wiki/index.md` (new concept and source entries).

Key insights: (1) the entire "core-shell + dopant" engineering effort is downstream of one defect-chemistry fact — Ti³⁺/Ti⁴⁺ equilibrium under reducing atmosphere creates V_O and accelerates cation diffusion; (2) the εr-vs-grain-size cliff at ~200 nm has a clean structural cause (no room for 90° twins to relieve cooldown stress); (3) Ni electrode discontinuity in thin-layer BME isn't a tape/printing defect — it's a Rayleigh-Plateau instability driven by a thin liquid (Ni, Ba, Ti) alloy that forms at 1000–1100 °C.

---

## [2026-05-19] ingest | Deep-research pass — materials, physics, processes (12+ new sources)

Directive: do a comprehensive web search across MLCC materials, physical behavior, and processes (academic papers + product spec sheets + manufacturer/association technical reports). Eleven major documents collected and ingested. Focus on closing the §9 gaps in `simulator-model.md`.

New raw sources in `resources/literature/` and `resources/market/`:
- [[escies-bme-mlcc-high-reliability]] — Gurav et al. (KEMET, ESA ESCIES archive). BME C0G (CaZrO₃) vs PME C0G (BaNd-titanate); 13× HALT MTTF improvement. **Source for CaZrO₃ Class I BME data.**
- [[nasa-ir-degradation-ni-batio3-2015]] — Liu (IEEE TCPMT 2015). Schottky double-depletion / Heywang-Jonker mechanism for IR degradation; 3 commercial BME 0.47 µF / 50 V / 0805 parts cross-compared with explicit layer counts (98–103), thicknesses (5.8–8.1 µm), grain sizes (0.33–0.40 µm).
- [[nasa-time-dependent-ir-2013-prb]] — Liu (PRB manuscript 2013). Derives exponential leakage law `I(t) = I₀·exp((t-t₀)/τ_SD)`, exponential barrier collapse `φ(t) = φ(0)·exp(-2Kt)`, K Arrhenius with **E_k ≈ 1.6 eV (commercial BME) vs 2.8 eV (automotive BME)** — direct quantitative anchors for the simulator slow-degradation branch.
- [[nasa-cracking-low-voltage-mlcc]] — Teverovsky (NASA NEPP 2018). 200+ pages encyclopedic cracking + qualification + processes survey.
- [[arxiv-batio3-domain-wall-motion]] — Gurung et al. (UConn / arXiv 2024). Landau-Ginzburg domain wall dielectric response in BaTiO₃; DW contribution ~2 orders of magnitude > intrinsic; DW relaxation 10 GHz vs intrinsic 500 GHz.
- [[octopart-tdk-cga8l3c0g-product-guide]] — TDK 2012 full MLCC product line-up, 62 pages (via Octopart). Closes the TDK side of the case-size geometry table.
- Murata SimSurfing documents (overview + measurement conditions) → `resources/market/murata-simsurfing-*.md`.
- IEC 60384-9-1:2005 standard preview (Class II ceramic capacitor blank detail spec) — `resources/design-rules/iec-60384-9-1-2005-sample.md`.
- ESCIES BME reliability evaluation for space + Wuerth (Zednicek) 2025 capacitor degradation paper.
- KEMET C1100 CAS-SMD automotive datasheet (`resources/market/kemet-c1100-cas-smd.md`).
- TDK MLCC temperature characteristics application guide (`resources/market/tdk-mlcc-temperature-characteristics-guide.md`).

New wiki concept pages:
- [[oxygen-vacancy-migration]] — IR-degradation root mechanism.
- [[ferroelectric-domain-wall]] — DW physics (the seat of MLCC εr).
- [[mlcc-manufacturing-process]] — End-to-end process map.
- [[bme-sintering-atmosphere]] — Reducing atmosphere + PO₂ window (10⁻¹⁰ to 10⁻¹² atm at peak sinter).
- [[re-oxidation-anneal]] — Post-sinter O-vacancy refill.
- [[batio3-powder-synthesis]] — Hydrothermal / solid-state / oxalate / sol-gel routes.

New wiki entity pages:
- Materials: [[cazro3]], [[srtio3]], [[nanbo3]].
- Series: [[bme-c0g]].

New wiki source pages: 6 (one per major new document).

Updated `resources/design-rules/simulator-model.md` §9 (more gaps closed: CaZrO₃ Class I path, BME E_k 1.6/2.8 eV from Liu PRB, BaTiO₃ powder hierarchy, DW physics, atmosphere recipe), §10 (source registry extended), and `wiki/index.md` (new materials/series/concepts/sources sections).

Key insights: (1) the v0 simulator can now handle Class I (CaZrO₃) separately with `f_VCC ≈ f_AC ≈ f_age ≈ 1, f_T = TCC·(T-25)`; (2) **vendor identity matters** — automotive BME runs E_k ~2.8 eV vs commercial 1.6 eV, an order of magnitude difference in degradation rate at 165 °C; (3) the entire MLCC εr observed at MHz is **DW contribution** — once DWs are pinned (by DC bias), εr drops to the intra-domain intrinsic value, which is ~2 orders of magnitude smaller. This is the mechanistic origin of the sigmoid VCC curve.

---

## [2026-05-19] ingest | Gap-filling pass — 5 new sources

Directive: comprehensive web search to fill the open gaps documented in `resources/design-rules/simulator-model.md` §9. Five new authoritative documents collected and ingested:

- [[aec-q200-rev-e-2023]] — official Automotive Electronics Council Q200 Rev E (March 2023) ceramic-capacitor stress qualification table. Closes Gap 6.
- [[electrical-integrity-dce11-200]] — Novak et al. (Oracle, DesignCon East 2011) measured DC/AC bias dependence across 5 vendors. Closes Gap 1 with quantitative VCC anchors.
- [[epci-high-cv-mlcc-bias-aging]] — Zednicek (EPCI / PCNS 2019) packaged multiplicative-factor formula `C_actual = C · F_DCV · F_ACV · F_T · F_age`. Reinforces Gap 1.
- [[nasa-general-reliability-model-ni-batio3]] — Liu (NASA Goddard / CARTS 2014) — direct evidence of BME single-mode P-V over-prediction (6.6× at one sample), with fitted **n = 4.524**, **E_a = 2.60 eV**. Closes Gap 3.
- [[rohm-ceramic-cap-app-note]] — ROHM AN 62AN089E (Jan 2020) DC-V comparisons across case size, thickness, and rated voltage on 10 µF B-char parts. Reinforces Gap 1.

New entity pages: [[aec-council]], [[yageo]] (draft), [[rohm]] (draft).
Updated: [[index]], [[log]], `resources/design-rules/simulator-model.md` §9 (gaps marked closed/partial with new data inline) and §10 (source registry extended).

Gaps closed: 1 (VCC fit), 3 (BME n), 4 (εr vs grain size — quantitative anchors), 5 (TDK case-size dimensions), 6 (AEC-Q200).
Gaps still open: 2 (frequency-dependent εr(T) digitized curves for X7R), partial 5 (Murata + Taiyo Yuden thickness option tables — vendor PDFs still blocked by anti-bot).

Key new insight: the single most authoritative quantitative anchor for BME-MLCC reliability — Liu's measured n = 4.524 for sample C08X47516 — is the public reference value the simulator should use for **single-mode** BME P-V approximations, while still recommending the two-mode model for accurate lifetime prediction.

---

## [2026-05-19] ingest | Batch: 8 sources + simulator spec

Goal: collect enough MLCC knowledge to design a simulator predicting electrical/reliability behavior from material, sheet thickness, layer count, overlap area, chip size.

Web research collected 8 foundational documents into `resources/{design-rules, literature, market}/` (raw PDFs in `<topic>/pdf/`, pdftotext-extracted `.md` alongside):
- KEMET/PSMA 2019 "MLCCs Design and Characteristics" → [[kemet-mlcc-design-and-characteristics]]
- KEMET/PSMA 2017 "Ceramic Capacitor Basics" → [[psma-ceramic-capacitor-basics]]
- Vishay 2021 "Time-Dependent Capacitance Drift of X7R MLCCs" → [[vishay-x7r-cap-drift-dc-bias]]
- KYOCERA AVX 1997 "Effects of ESR and ESL" → [[kyocera-avx-esr-esl-decoupling]]
- Murata GRM Series Data (TCC, DC bias, AC bias, aging, impedance) → [[murata-grm-series-tcc-data]]
- Samsung CL Series datasheet → [[samsung-cl-series-mlcc-ds]]
- NASA NEPP 2013 BME reliability → [[nasa-nepp-bme-mlcc-reliability]]
- NASA CARTS 2012 BaTiO₃ failure mechanisms → [[nasa-batio3-mlcc-failure-mechanisms]]

Synthesis deliverable: [`resources/design-rules/simulator-model.md`](../resources/design-rules/simulator-model.md) — full input/output/equation specification for the MLCC design simulator, with a worked example reproducing published 0805 X7R 10 µF / 6.3 V vendor envelopes.

Pages created (this batch):
- Concepts: [[mlcc-capacitance-equation]], [[eia-rs-198-dielectric-classes]], [[dc-bias-derating]], [[aging-class-2]], [[bme-reliability-model]], [[case-size-geometry]], [[bme-vs-pme]], [[esr-esl-srf]], [[failure-modes-mlcc]], [[core-shell-batio3]].
- Sources: 8 source-summary pages (one per document above).
- Entities — companies: [[murata]], [[samsung-electro-mechanics]], [[kemet]], [[vishay]], [[kyocera-avx]], [[tdk]] (draft), [[taiyo-yuden]] (draft).
- Entities — series: [[murata-grm-series]], [[samsung-cl-series]], [[kemet-arcshield]].
- Entities — material/person/org: [[batio3]], [[donhang-liu]], [[nasa-nepp]].
- Index + overview updated.

Key takeaways: (1) field `E = V/d`, not voltage, is the right driver for all Class-II non-idealities; (2) the N-amplifier `(per-layer reliability)^N` makes thin-layer high-N parts only viable with tightly controlled defect density and engineered grain microstructure; (3) [[murata]] (Tb/Dy/Re patents) and [[samsung-electro-mechanics]] (Tb-Dy molar ratio patents) are still patenting dopant ratios in 2024–2025, indicating live competition on dielectric chemistry.

Contradictions: none; sources align on the framework but disagree on quantitative DC-bias-aging rates by vendor (Vishay PME at ~5 %/decade vs BME competitors at 7–10 %/decade — captured in [[dc-bias-aging]] candidate page).

Pending: drop TDK / Taiyo Yuden full catalogs into `resources/market/` (blocked during this batch by anti-bot); digitize Murata/Samsung VCC curves for empirical (E₀, p) sigmoid fits; deepen `resources/manufacturing/` for process-yield-style simulation.

---

## [2026-05-19] init | Wiki initialized

Wiki created for: **MLCC (Multi-Layer Ceramic Capacitor) research** — manufacturing, market & product lineups, academic literature & patents, design rules & specs.

Directories created: `resources/assets/`, `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`, `wiki/comparisons/`, `wiki/queries/`.
Existing `resources/{manufacturing,market,literature,design-rules}/` retained as raw drop zones.
Schema generated: `CLAUDE.md` (merged with pointers to `AGENTS.md` and `RESEARCH_PLAN.md`).
Vault config: `vault_path=null` (local mode); `sources_dir=resources`; `wiki_dir=wiki`.
