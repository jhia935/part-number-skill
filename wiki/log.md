---
title: Activity Log
type: log
created: 2026-05-19
updated: 2026-05-19
---

# Activity Log

Chronological record of wiki operations. Newest entries first.

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
