---
title: Activity Log
type: log
created: 2026-05-19
updated: 2026-05-19
---

# Activity Log

Chronological record of wiki operations. Newest entries first.

---

## [2026-05-20] update | Size-code i/m disambiguation convention

Documented the EIA-vs-metric size-code collision and the `i`/`m` suffix disambiguation convention used by the MLCC simulator's size resolver.

Updates:
- [[case-size-geometry]] — added "naming-convention pitfall" section with collision table (digits `0201`/`0402`/`0603`/`0805`/`1206` have 6–31× volume mismatch between EIA and metric readings). Added "Recommended disambiguation" section with `i` / `m` suffix rules. Added SEMCO 2-digit internal code table (separately from EIA/metric — independent index).
- [[samsung-cl-series]] — extended size-code table with metric column; added cross-reference to disambiguation convention.

Rationale: the bare `0603` notation is ambiguous (EIA = 1.6 × 0.8 mm workhorse vs metric = 0.6 × 0.3 mm ultra-tiny), and BOMs / engineering tools without disambiguation have caused real production mix-ups. The simulator's resolver now accepts `0603` (assumed EIA, with warning), `0603i` (explicit EIA), or `0603m` (explicit metric) — and the wiki documents the convention for future engineers.

---

## [2026-05-20] ingest | Sintering/firing publications — 2 concept pages + 1 source

Per `/wiki ingest` directive to add more sintering/firing research papers and publications. Most Wiley / ScienceDirect papers were paywalled but one open-access EPJ Web of Conferences paper covers both DEM simulation and synchrotron nano-CT of MLCC sintering — the methodological foundation for the bigger 2021 Acta Mater paper.

New raw source:
- Yan, Martin, Bouvard et al. (EPJ Web Conf. 140, 13006, 2017) — open access (CC-BY 4.0). Couples in-situ X-ray tomography with DEM simulation; demonstrates on Cu powder (ESRF) and Ni-BaTiO₃ MLCC (Argonne nano-CT). Quantitative Parhami-McMeeking contact force model.

New wiki concept pages (2):
- [[master-sintering-curve]] — Su-Johnson MSC framework (*JACerS* 1996) built on Hansen et al. combined-stage model. Density-independent normalized curve via `Θ = ∫(1/T)·exp(-Q/RT)dt`. Activation energies for BaTiO₃ from Lee *et al.* 2026: 350–500 kJ/mol below 1200 °C, breaks down above 1200 °C as final-stage mechanism transitions. Limitations + Reed-Hill 2017 critique.
- [[binder-burnout-debinding]] — first firing step (200–600 °C). PVB / PMMA / PVA polymer chemistry; zero/first-order Arrhenius kinetics (Eₐ ≈ 150–250 kJ/mol for PVB); diffusion-limited gas evolution; Ar + 1 vol % O₂ atmosphere as BME-compatible compromise (74% binder removal, ~1600 ppm O on Ni). BBO defect-mode catalog: bloating, parallel-plate crack, delamination, residual carbon, NiO scale. References 2024 *Appl. Thermal Eng.* CFD paper.

New wiki source page:
- [[epj-in-situ-xray-tomography-dem]] — Grenoble + ESRF + Argonne + Jülich collaboration's open-access methodological paper. Companion to the Okuma 2021 *Acta Mater.* MLCC nano-CT paper.

Key insights: (1) Master Sintering Curve is the industrial benchmark methodology but **breaks down above ~1200 °C** for BaTiO₃ — exactly where industrial MLCC sintering happens; (2) **binder burnout** is the most under-credited firing-stage failure source — many defects that look like sintering problems trace back to BBO atmosphere or rate choices; (3) Ni-BaTiO₃ MLCC discontinuity is set **early in sintering** by initial powder packing heterogeneity, not just the peak-T mechanism — DEM + synchrotron nano-CT confirm this.

Updated `wiki/index.md` (2 new concept entries + 1 new source). 0 broken wikilinks (verified).

Wiki: **112 pages** across 6 categories.

---

## [2026-05-20] lint | Wiki health check + frontmatter cleanup

Scan summary:
- 0 broken wikilinks (verified)
- 0 orphan pages (every non-index/log/overview page has at least one inbound wikilink)
- 0 unresolved contradictions
- 0 index inconsistencies (every page indexed; no dangling index references)
- 0 entity classification tag violations (every `type: entity` page carries exactly one of `company | series | material | standard | person | org`)
- 56 pages were missing `status:` and `importance:` frontmatter fields

Auto-fix applied (option 2 — fix + audit):
- Added `status: complete` to all 56 pages that needed it.
- Added `importance: high` to **24 simulator-core pages**: mlcc-capacitance-equation, eia-rs-198-dielectric-classes, dielectric-class-comparison, dc-bias-derating, aging-class-2, bme-reliability-model, case-size-geometry, esr-esl-srf, core-shell-batio3, x7r-dielectric, c0g-npo-dielectric, mlcc-manufacturing-process, bme-sintering-atmosphere, failure-modes-mlcc, dc-bias-aging, curie-temperature, temperature-coefficient-of-capacitance, vendor-spice-models, decoupling-design-rules, heywang-jonker-model, oxygen-vacancy-migration, bme-vs-pme, permittivity, insulation-resistance.
- Added `importance: medium` to the remaining 32 pages (supporting concepts).

Final distribution: **52 importance:high**, **51 importance:medium**, **3 importance:low**, **101 status:complete**, **5 status:draft** (intentional entity stubs: nanbo3, srtio3, intel, rohm, tdk).

Tag hygiene unchanged: 84 `paper` tags, 10 `company`, 5 `series`, 4 `material`, 2 `org`, 1 `person`. All within Tag Policy bounds.

Suggestions logged (not auto-fixed):
- 5 entity stubs (`nanbo3`, `srtio3`, `intel`, `rohm`, `tdk`) could be expanded with more research.
- 23 concept pages have ≤ 1 `sources:` frontmatter entry while having multiple references in the body — could be polished by lifting body references into frontmatter.
- Some "Murata"/"KEMET" mentions inside markdown URL captions (e.g., `[Murata WO...](url)`) appear as unlinked entity references to the lint scan. Most are intentional citation captions.

---

## [2026-05-20] ingest | Final-pass gap-filling — all remaining suggestions

Per `/wiki ingest` directive to continue with the remaining gap-filling suggestions surfaced in the previous query.

New raw sources:
- AEC-Q104 Rev A (Nov 28, 2025) — official AEC MCM qualification standard
- Sci. Rep. 9953 (2015) "Unfolding grain size effects in BaTiO₃ ferroelectric ceramics" — open-access cross-method survey

New wiki concept pages (5):
- [[murata-spice-library-and-curves]] (**High priority**) — practical bridge: SPICE netlist structure example + digitized DC-bias / TCC / aging tables from the public Murata GRM Series Data PDF. Concrete values for C0G/X7R/Y5V at 50 V; SRF lookup by case+value+class.
- [[kemet-k-sim-tool]] (**Medium**) — KEMET / Yageo K-SIM characterization tool. Broader cap-type coverage than SimSurfing (ceramic + tantalum + polymer + film + Al-electrolytic). Built-in lifetime model `L = L_rated · (V_r/V)^n · 2^((T_r-T)/10)` for non-ceramic.
- [[s-parameter-de-embedding-mlcc]] (**Medium**) — TRL / OST / series-pair de-embedding methodology. Quantitative ESL hierarchy: 0.05–0.1 nH (LICC) to 1.0–2.5 nH (1206 standard mount). Mounting-loop ESL dominates chip ESL for cases ≤ 1206.
- [[nano-grain-batio3-epsilon-r]] (**Low**) — quantitative εr vs grain size in the 5 µm → 10 nm range. εr peak at 0.8–1.1 µm (~5000–6000), drops below 1000 at 50 nm, c/a → 1.000 at 100 nm. Critical size for ferroelectric collapse: 10–30 nm. Dead-layer model.

New wiki source pages (2):
- [[srep-batio3-grain-size-unfolding]] — Sci. Rep. 2015 cross-method study.
- [[aec-q104-rev-a-2025]] — AEC-Q104 framework for MCM-embedded MLCCs (30×3 lot sample sizes; "H" category MCM-specific tests; VISM thermal-shock migration).

Key insights: (1) Murata static SPICE = simple R-L-C-R series (typical 10µF/10V/X7R/0805: 9.85µF + 8.5mΩ ESR + 0.43nH ESL + 1.2GΩ IR); dynamic adds behavioral current source for V_DC + T; (2) K-SIM has lifetime model for non-ceramic, defers to AEC-Q200 for MLCC; (3) mounting-loop ESL **dominates** chip ESL for cases ≤ 1206; (4) εr falls below 1000 at 50 nm grain — quantitative reason for thin-layer scaling ceiling; (5) AEC-Q104 matters when MLCCs embedded in automotive power modules.

Updated `wiki/index.md` (5 new app-layer concept entries + 2 new source entries). 0 broken wikilinks (verified).

Wiki now: **114 pages** across 6 categories. The v0–v0.3 simulator-model.md gaps are essentially all documented.

---

## [2026-05-20] ingest | P0–P3 gap-filling per senior-engineer priority

Per `/wiki ingest` directive to research and ingest gap-fillers prioritized as a senior MLCC engineer would: vendor sim-tool docs (P0), application-layer design rules (P1), PCB layout (P2), and underserved Tier-1 vendor coverage (P3).

New raw source:
- Taiyo Yuden MLCC Whitepaper (mid-2010s flagship) — documents 100–470 µF commercialization, MTTF 10⁴–10⁶ yr claims, acoustic-noise-suppression dielectric, soft-termination, full product family naming.

New wiki concept pages:
- [[vendor-spice-models]] (**P0**) — Murata SimSurfing, K-SIM, SpiCap, SEAT-MLCC, myCAP. Static R-L-C vs dynamic (R-L-C + behavioral current source for V_DC + T) models. How a simulator should consume them: direct SPICE bridge / parameter extraction / Touchstone. Lists what vendor models do NOT capture (aging, reliability, mechanical) — i.e., what our simulator must add.
- [[decoupling-design-rules]] (**P1**) — PDN target impedance Z_target = ΔV_max / I_max; "myth of three capacitor values" debunked (modern MLCC ESL is geometry-not-value); same-value parallel approach; anti-resonance ESR damping `ESR_req ≥ √(L_1/C_2)`; mounting-via inductance dominance; Bandini Mountain on-die resonance.
- [[mlcc-pcb-layout-rules]] (**P2**) — IPC-7351 pad geometry (Levels A/B/C); anti-tombstoning rules (symmetric pads, identical thermal mass); flex-zone exclusion (no MLCCs >0805 within 5 mm of cutouts/screws); soft-termination decision rules; JEDEC J-STD-020E reflow profile; MSL bake-out. Concrete pad-dimension table for 0402–2220.

New wiki source page:
- [[taiyo-yuden-mlcc-whitepaper]] — quantitative anchors for TY's 100–470 µF MLCC technology; product family naming (PMK/AMK/JMK/LMK/EMK/GMK/TMK/HMK); soft-termination + acoustic-noise-suppression details.

Updated entity pages:
- [[taiyo-yuden]] — promoted from stub to complete with full product family table, milestones (330 µF in 2013, 470 µF in 2014, 1200+ layers in 1812), differentiated technologies.
- [[yageo]] — promoted from stub to complete with full automotive product portfolio (AC, AS, AQ, AC Array, AC HiCap, AC HiTemp), KEMET-brand continuation, AEC-Q200 sub-committee role, quality framework details.

Notable findings: (1) **Murata's dynamic SPICE model** is unique — static R-L-C plus behavioral current source for runtime adjustment to V_DC and T; reproduces measured DC/DC ripple "very nearly identical to measured"; (2) the **"3-capacitor-value rule" is obsolete** for MLCC because ESL doesn't scale with capacitance value in modern parts (mounting geometry dominates); same-value paralleled banks avoid anti-resonance; (3) **Taiyo Yuden documented MTTF 10⁴–10⁶ years** for premium high-CV parts — consistent with the Liu reliability framework at the high-quality end; (4) Yageo's AC/AS/AQ series structure exposes a useful boardflex / RF / general decomposition pattern.

Updated `wiki/index.md` (new "Application-layer design rules" section + new source entry). 0 broken wikilinks (verified).

Wiki now has **107 pages** across 6 categories.

---

## [2026-05-20] ingest | Full TCC family — comparison table + per-class deep dives

Per `/wiki ingest` directive to expand temperature characteristics beyond X7R to all ranges and investigate TCC.

New wiki comparison page:
- [[dielectric-class-comparison]] — master reference table covering every commercially significant TCC code:
  - **Class I**: C0G/NP0 (±30 ppm/°C), P2H (−150), R2H (−220), S2H (−330), T2H (−470), U2J (−750), S2L, X8G (high-T Class I)
  - **Class II**: X5R, X6S, X7R, X7S, X7T, X7U, X7P, X8R, X8L, X0U (175 °C, new), X9R (200 °C research), X9V (Vishay HOTcap 200 °C)
  - **Class III**: Y5V, Z5U (high-K legacy)
  - **Mil hi-rel**: BP, BX, BR (MIL-C-55681)
  - With εr ranges, max ΔC, aging %/decade, DF max, material basis, and application notes.

New per-class concept deep-dive pages:
- [[c0g-npo-dielectric]] — Class I ultra-stable; CaZrO₃ BME (εr ≈ 31) or BaNd-titanate PME (εr ≈ 70); only "textbook ideal" cap. Extended-range Class I (P2H to U2J) gets εr up to ~500 with linear negative TCC for temperature-compensation use.
- [[x7r-dielectric]] — Class II workhorse; BaTiO₃ core-shell with Sr/Zr Curie-shifting; X7R/X7S/X7T/X7U cousin tradeoffs (more εr for relaxed tolerance); 1–2 %/decade aging spec.
- [[x5r-dielectric]] — Class II consumer-dominant; chemistry essentially same as X7R but less doped → higher peak εr, less stable, ~5 %/decade aging.
- [[x8r-x8l-x9r-high-temperature-dielectrics]] — above-125 °C: X8R (±15 % to 150 °C), X8L (asymmetric drift, automotive standard), X8G (Class I, rare), X9R (200 °C research), X0U (new 175 °C automotive), X9V (Vishay HOTcap 200 °C with +22/−82 %). Chemistry: Sr/Zr/Bi shift, NaNbO₃/BiMg-titanate solid solutions to broaden Curie peak.
- [[y5v-z5u-class-iii-dielectric]] — Class III; +22/−82 % Y5V, +22/−56 % Z5U; aging 5–7 %/decade; combined operating-point CV can fall to 5–10 % of nameplate; **being phased out** by modern X5R.

Key insights: (1) the X7-family proliferation (R/S/T/U/P) is a single εr-vs-tolerance tradeoff axis at the same −55…+125 °C range; (2) high-T extensions (X8R etc.) work by **flattening the Curie peak** rather than shifting it past T_max — the cost is lower peak εr; (3) **X0U is the newest 2024-era automotive code** for 175 °C operation with asymmetric tolerance allowed above 125 °C; (4) Y5V is being deprecated industry-wide as X5R catches up on εr.

Updated `wiki/index.md` with new "Dielectric class deep-dives" section and the first entry in the previously-empty Comparisons category.

---

## [2026-05-20] ingest | Core-shell structure deep-dive — chemistry, kinetics, coating, electrical link

Per `/wiki ingest` directive to search for core-shell structure and its relation to characteristics, MLCC process (especially material stage and firing).

New raw source:
- arXiv:1111.3738 (Nuzhnyy et al. 2011) "High-Frequency Dielectric Spectroscopy of BaTiO₃ Core–Silica Shell Nanocomposites: Problem of Interdiffusion" — three sintering routes (standard, SPS, two-step) on the same BaTiO₃@SiO₂ powder; THz dielectric dispersion correlates with interdiffusion gradient layer thickness.

New wiki concept pages:
- [[dopant-site-occupancy-batio3]] — A-site (donor) vs B-site (acceptor) substitution; ionic-radius hierarchy (La 1.36 → Yb 1.12 Å); amphoteric window for Dy/Y/Ho/Er at ~1.16 Å gives the modern co-doping playbook.
- [[core-shell-formation-mechanism]] — solid-state diffusion vs dissolution-reprecipitation debate. Modern consensus (Jeon JACerS 2012, Chen JACerS 2020): dissolution-reprecipitation dominates at high dopant loadings, with a narrow kinetic window that must be hit by sintering recipe.
- [[dopant-powder-coating]] — material-stage preparation: dry mechanical mixing (legacy) vs wet-chemical surface modification (modern standard) vs co-precipitation (no shell) vs ALD (research). Coating method matters more than total dopant content for shell uniformity.

Updated existing page:
- [[core-shell-batio3]] — substantially expanded with quantitative shell thickness (10–50 nm), rare-earth concentration in shell (~3–10 mol%), Mg/RE molar ratio (0.5–2), and a detailed table linking shell properties to each electrical characteristic (εr(T) flattening, DC-bias stability, IR/MTTF, aging, DF).

New wiki source page:
- [[arxiv-batio3-silica-interdiffusion]] — quantitative process anchors for three sintering routes; fresnoite formation in TSS; THz spectroscopy probes interdiffusion gradient layer.

Key insights: (1) **amphoteric rare-earth window** (Dy/Y/Ho/Er, ionic radius ~1.16 Å) is the chemistry sweet spot — same dopant produces donor + acceptor populations in a tuned ratio for automatic carrier compensation; (2) **core-shell forms by dissolution-reprecipitation**, not Fickian diffusion — sintering recipe matters far more than just hold time; (3) **dopant coating method** is one of the biggest Tier-1 vs Tier-2 differentiators (wet-chemical 3–10 nm coating vs dry-mixed bulk dopant); (4) the same nominal "X7R 10 µF" can have wildly different DC-bias / aging behavior depending on shell quality — explains the [[vishay-x7r-cap-drift-dc-bias|3-vendor benchmark]] variation.

Updated `wiki/index.md` (3 new concept entries + 1 new source).

---

## [2026-05-20] ingest | MLCC sintering process — 5 new concept pages, 2 new source pages

Per `/wiki ingest` directive to search for MLCC process material, especially sintering. Targeted gaps not covered in the earlier sintering-physics pass: industrial process recipes, alternative methods, equipment-aware modeling.

New wiki concept pages:
- [[sintering-profile-mlcc]] — multi-stage profile (binder burnout → pre-sinter → fast ramp → peak hold → cooldown → re-oxidation), heating-rate effect on Ni electrode continuity (Polotai JACerS 2007 study: 200–3000 °C/h sweep, 1250 °C / 60 °C/min optimum).
- [[two-step-sintering]] — Chen-Wang TSS-CW method: ramp to 1300 °C for partial density, drop to 1100 °C and hold; achieves 96 % density at 35 nm grain in BaTiO₃ (vs 1–5 µm grain conventional).
- [[constrained-sintering-mlcc]] — in-plane shrinkage suppressed by electrode constraint, thickness absorbs slack; LTCC-style 12.7 / 13.9 / 12.8 % anisotropy. Camber/warpage from sintering-kinetics mismatch.
- [[spark-plasma-sintering]] — SPS / FAST; 99 % density in minutes; εr ≈ 3500 (vs 2000 conventional) due to GB defect reduction.
- [[cold-sintering]] — Randall group's <300 °C process with transient liquid phase; cold-sintered BaTiO₃ at 90–95 % density.

New wiki source pages:
- [[cold-sintering-annual-review-mse]] — Guo, Randall et al. *Annu. Rev. Mater. Res.* 2019.
- [[llnl-particle-rigid-body-sintering]] — LLNL paper on rigid-body particle rearrangement.

Key insights: (1) heating rate is the dominant industrial knob — 60 °C/min through the 1000–1100 °C interfacial-liquid window optimizes Ni-electrode continuity; (2) two-step sintering (Chen-Wang) is the foundation of fine-grain BaTiO₃; (3) constrained sintering creates anisotropic shrinkage in the multilayer stack and residual stress that superposes with the cooldown phase transition; (4) SPS / cold sintering are research frontier but not yet competitive for production MLCC.

Updated `wiki/index.md` (5 new concepts + 2 new sources).

---

## [2026-05-20] lint | Wiki health check — promote primitives, fix broken links

Per `/wiki lint` directive to investigate need for more primitive concepts/entities.

**Scan results (before fix):**
- 11 truly broken wikilinks identified after sort-order correction (LC_ALL=C):
  - Primitive concepts missing: `curie-temperature`, `temperature-coefficient-of-capacitance`, `heywang-jonker-model`, `termination-and-plating`
  - Entities missing: `tdk-cga-series`, `intel`
  - Typos/aliases: `cazro3-dielectric` → `cazro3`, `c0g-dielectric` (drop)
  - Web-only refs treated as wikilinks: `adv-mater-2026-grain-boundary`, `knowles-fundamentals-8`, `passive-components-eu-mlcc-loss`, `btu-international`

**Auto-fix applied — Created 12 new primitive pages:**
- Concepts: [[curie-temperature]], [[temperature-coefficient-of-capacitance]], [[heywang-jonker-model]], [[termination-and-plating]], [[perovskite-structure]], [[permittivity]], [[polarization-mechanisms]], [[dissipation-factor]], [[dielectric-breakdown]], [[insulation-resistance]], [[prokopowicz-vaskas-equation]], [[weibull-distribution]]
- Entities: [[tdk-cga-series]], [[intel]]

**Broken-link cleanup:**
- `cazro3-dielectric` → `cazro3` (all occurrences in oxygen-vacancy-migration and escies-bme-mlcc-high-reliability)
- `c0g-dielectric` → drop the broken alias, inline-link `cazro3` instead (in eia-rs-198-dielectric-classes and batio3)
- `adv-mater-2026-grain-boundary` → replace with full citation + DOI link (in core-shell-batio3 and batio3)
- `knowles-fundamentals-8` → replace with markdown link to the Knowles blog post (in eia-rs-198-dielectric-classes)
- `passive-components-eu-mlcc-loss` → redirect to existing [[epci-high-cv-mlcc-bias-aging]] page (in dc-bias-derating)
- `btu-international` → plain-text reference to BTU International OEM (in bme-sintering-atmosphere)

**Re-scan after fix:** 0 broken wikilinks remaining.

Updated `wiki/index.md` with new "Primitives (foundational concepts)" section + new entities.

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
