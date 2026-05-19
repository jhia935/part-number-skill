# MLCC Design Simulator — Model Specification

> Predict the electrical, thermal, and reliability behavior of an MLCC from
> **material**, **geometry**, and **process** inputs. This spec is the
> synthesized output of the foundational research collected in
> `resources/{design-rules,literature,market}/`. Every equation and
> parameter range is keyed to a source.
>
> Status: **v0 — sufficient to build a first-cut simulator.** Open gaps listed in §9.

---

## 1. Inputs

### 1.1 Material parameters
| Symbol | Name | Typical range | Source |
|---|---|---|---|
| `class` | EIA RS-198 dielectric class | C0G, X5R, X6S, X7R, X7S, X7T, X8L, X8R, Y5V, Z5U | [psma-ceramic-capacitor-basics] |
| `εr0` | zero-bias relative permittivity at 25 °C, low field | C0G: 20–100 · X7R: 600–4000 · X7R high-K: 4000–18000 (Y5V/Z5U) | [knowles-fundamentals-8] |
| `Tc` | Curie temperature (Class II only) | BaTiO₃ ≈ 125–130 °C; X8R/X8L compositions shift higher | [vishay-x7r-cap-drift-dc-bias], [psma-ceramic-capacitor-basics] |
| `tan δ` | dissipation factor at 1 kHz, 25 °C | C0G ≤ 0.0015 · X7R ≤ 0.025 (rises with V_AC, lower-V parts to 0.16) | [knowles-fundamentals-8], [samsung-cl-series] |
| `Ebd` | dielectric breakdown field | X7R/X5R BME: ~80–150 V/µm intrinsic, derated to ~25 V/µm rated | [nasa-batio3-failure-mechanisms] |
| `r̄` | average BaTiO₃ grain size | thin-layer: 100–300 nm; conventional: 0.5–2 µm | [adv-mater-2026-grain-boundary] (search), [nasa-batio3-failure-mechanisms] |
| `α` | reliability exponent on `r̄/d` | ≈ 6 for V ≤ 50 V · ≈ 5 for V > 50 V | [nasa-nepp-bme-mlcc-reliability] Eq. 14 |
| `n` | Prokopowicz-Vaskas voltage exponent | ≈ 3 (PME); BME mixed (see §5.2) | [nasa-nepp-bme-mlcc-reliability] |
| `Ea1, Ea2` | activation energies | 1.0–2.0 eV (catastrophic), ~1 eV (slow degradation) | [nasa-nepp-bme-mlcc-reliability] |
| `A_age` | aging rate constant | C0G: ~0 · X5R: ~5 %/decade · X7R: 1–2 %/decade · Y5V: 5–7 %/decade | [vishay-x7r-cap-drift-dc-bias], [psma-ceramic-capacitor-basics] |

### 1.2 Geometry parameters
| Symbol | Name | Notes |
|---|---|---|
| `case` | EIA case size code | 0201, 0402, 0603, 0805, 1206, 1210, 1812, 2220 |
| `L, W, H` | outer length × width × height | per [samsung-cl-series] and [nasa-nepp-bme-mlcc-reliability] Table II |
| `m_end, m_side` | end margin, side margin | per Table II; case-size-dependent |
| `d_cover` | cover (passivation) layer thickness | typ. 30–100 µm per side; derived from H − N·(d + d_e) |
| `d` | dielectric layer (sheet) thickness | state-of-the-art: 0.5–1 µm; conventional: 2–10 µm |
| `d_e` | inner electrode (Ni/Cu/Pd) thickness | 0.4–1.0 µm typical |
| `N` | number of **active** dielectric layers | BME: 70–80 (0402), 250–300 (0805+); SOTA: up to 1000 |
| `t_pad` | termination pad thickness | typ. 20–50 µm |

### 1.3 Operating conditions
| Symbol | Name |
|---|---|
| `V_DC` | applied DC bias |
| `V_AC_rms` | applied AC signal amplitude |
| `f` | operating frequency |
| `T` | ambient temperature |
| `t_life` | service time (hours) for reliability prediction |

---

## 2. Capacitance equation (nominal, ideal)

The base model is the parallel-plate stack:

$$
C_0 \;=\; \varepsilon_r(T,f) \cdot \varepsilon_0 \cdot \frac{A \cdot N}{d}
$$

where `A` is the **effective overlap area** of internal electrodes and `N` is the active layer count. `ε₀ = 8.854 × 10⁻¹² F/m`. Some sources use `(N−1)` instead of `N` (edge-of-stack correction); the difference is <2 % for N > 50.
**Sources:** [kemet-mlcc-design-and-characteristics], [psma-ceramic-capacitor-basics], [nasa-nepp-bme-mlcc-reliability] Eq. 1, [knowles-fundamentals-3].

### 2.1 Effective overlap area from case size
$$
A \;=\; (L - 2 m_\text{end}) \cdot (W - 2 m_\text{side})
$$

Reference values (BME, [nasa-nepp-bme-mlcc-reliability] Table II):

| Case | L (µm) | W (µm) | m_end (µm) | m_side (µm) | A (mm²) | S_scale vs 0402 |
|---|---|---|---|---|---|---|
| 0402 | 1000±100 | 500±100 | 125 | 100 | 0.225 | 1.00 |
| 0603 | 1600±150 | 810±150 | 175 | 100 | 0.763 | 3.39 |
| 0805 | 2010±200 | 1250±200 | 250 | 150 | 1.520 | 6.76 |
| 1206 | 3200±200 | 1600±200 | 250 | 150 | 3.510 | 15.60 |
| 1210 | 3200±200 | 2500±200 | 250 | 150 | 5.940 | 26.40 |
| 1812 | 4500±300 | 3200±200 | 300 | 200 | 10.920 | 48.53 |
| 2220 | 5700±400 | 5000±400 | 320 | 220 | 23.074 | 102.55 |

### 2.2 Max layer count from height
$$
N_\text{max} \;=\; \left\lfloor \frac{H - 2 d_\text{cover}}{d + d_e} \right\rfloor
$$
With `H_max` from datasheet (e.g., 0402 H_max ≈ 0.55 mm, 0805 H_max ≈ 1.35 mm — [samsung-cl-series]) and `d_cover ≈ 30–50 µm`.

### 2.3 Volumetric efficiency
$$
\frac{C_0}{V_\text{chip}} \;\approx\; \varepsilon_0 \cdot \frac{\varepsilon_r}{d^2} \;\approx\; 8.854\times 10^{-8} \cdot \frac{\varepsilon_r}{d^2}\;[\mu F/cm^3]
$$
With `d` in cm. Diverges as `d → 0` only if `εr` stays constant — in practice `εr` collapses below `d ≈ 4·r̄`. **Sources:** [nasa-batio3-failure-mechanisms] Eq. 3 and Fig. 2.

### 2.4 Grain-size constraint
$$
d \;\geq\; (3\!-\!5) \cdot \bar r
$$
Empirically, optimum `εr` for X7R/X5R BaTiO₃ peaks at grain size **200–260 nm** under DC fields > 4 V/µm. Below 200 nm the ceramic loses ferroelectricity (`εr` drops sharply). **Source:** [adv-mater-2026-grain-boundary] (Wiley 2026).

---

## 3. Effective capacitance (under stress)

Apply multiplicative factors to `C₀`:

$$
C_\text{eff}(V_\text{DC}, V_\text{AC}, T, t) \;=\; C_0 \cdot f_\text{VCC}(E) \cdot f_\text{AC}(V_\text{AC}) \cdot f_T(T) \cdot f_\text{age}(t,E,T)
$$

### 3.1 DC bias derating `f_VCC(E)`
`E = V_DC / d` is the **field** inside one dielectric layer (the critical variable — not V).

**Class I (C0G/NP0):** `f_VCC ≈ 1` — paraelectric, no domain effect.

**Class II (X7R/X5R, BaTiO₃-based):** approximately monotonically decreasing with field; key reference values from [vishay-x7r-cap-drift-dc-bias] Fig. 2 (typical Class 2 VCC plot):

| E (V/µm) | Capacitance change (%) |
|---:|---:|
| 0  | 0 |
| 2  | -10 |
| 4  | -25 |
| 6  | -45 |
| 10 | -60 |
| 15 | -75 |
| 20 | -85 |

Vendor-vs-vendor variation is large: at 10 µF / 6.3 V / 0805 X7R, range is −35 % to −65 % across three vendors at rated voltage ([passive-components-eu-mlcc-loss]). Case-size matters mostly via `d` (thicker `d` → lower `E` at same V).

**Heuristic fit** for Class II (sigmoid-like, suitable for simulator):
$$
f_\text{VCC}(E) \;=\; \frac{1}{1 + (E/E_{0})^{p}}
$$
with `E₀` and `p` fitted per dielectric class. Typical X7R: `E₀ ≈ 5 V/µm`, `p ≈ 1.3`. Y5V more aggressive: `E₀ ≈ 1.5 V/µm`, `p ≈ 1.0` (drops to −90 % at rated V — [murata-grm-series-tcc-data]).

### 3.2 AC bias `f_AC(V_AC)`
Class I: ≈ 1. Class II at low V_AC (e.g., 10 mV vs 1 V_rms standard test): −5 % to −15 % capacitance loss due to ferroelectric hysteresis [passive-components-eu-mlcc-loss]. Class II at high V_AC: capacitance **rises** modestly (Y5V grows up to +14 %, X7R up to +6 % at several V_rms — [murata-grm-series-tcc-data]).

### 3.3 Temperature `f_T(T)`
Class I: `f_T(T) = 1 + TCC·(T − 25)`; TCC from EIA letter code (see §4).

Class II: piecewise / tabulated curve within the class spec:
- X7R: ±15 % over −55…+125 °C
- X5R: ±15 % over −55…+85 °C
- X6S: ±22 % over −55…+105 °C
- Y5V: +22 % / −82 % over −30…+85 °C

Peak `εr` for BaTiO₃ near `Tc` (~125 °C) is the cause of the X7R sag at high T (and Y5V's collapse at low T below tetragonal→orthorhombic phase).

### 3.4 Aging `f_age(t, E, T)`
Logarithmic for Class II at zero bias [vishay-x7r-cap-drift-dc-bias] Eq. (from Fig. 3):
$$
f_\text{age}(t) \;=\; 1 - \tfrac{A_\text{age}}{100}\cdot \log_{10}(t/t_\text{ref})
$$
with `t_ref` typically 1 h after last de-aging (heat above `Tc`). X7R: `A_age ≈ 1.5 %/decade`. Aging fully resets above `Tc`.

**DC-bias-accelerated aging**: at field `E`, the rate accelerates. Empirical fits show competitor X7R parts lose **7–10 %/decade** at 40 % V_rated and even faster at 100 % V_rated [vishay-x7r-cap-drift-dc-bias] Fig. 5–6. Best-in-class parts hold to 1–2 %/decade.

---

## 4. Dielectric class code decoder (EIA RS-198)

### 4.1 Class I (e.g., `C0G`, `U2J`) — significant-figure × multiplier × tolerance
| 1st letter | TCC significant figure | 2nd digit | TCC multiplier | 3rd letter | TCC tolerance (ppm/°C) |
|---|---|---|---|---|---|
| C | 0.0 | 0 | −1 | G | ±30 |
| B | 0.3 | 1 | −10 | H | ±60 |
| L | 0.8 | 2 | −100 | J | ±120 |
| A | 0.9 | 3 | −1000 | K | ±250 |
| M | 1.0 | 4 | −10 000 | L | ±500 |
| P | 1.5 | 5 | +1 | M | ±1000 |
| R | 2.2 | 6 | +10 | N | ±2500 |
| S | 3.3 | 7 | +100 |  |  |
| T | 4.7 | 8 | +1000 |  |  |
| U | 7.5 | 9 | +10 000 |  |  |
Examples: `C0G` = 0 × −1 = 0 ppm/°C, ±30; `U2J` = −750 ppm/°C ±120; `P2H` = −150 ppm/°C ±60. Range: −55…+125 °C.
**Source:** [psma-ceramic-capacitor-basics], [samsung-cl-series].

### 4.2 Class II/III — temp range + max ΔC
| 1st (T_low) | 2nd (T_high) | 3rd (ΔC) |
|---|---|---|
| X = −55 °C | 4 = +65 | A = ±1.0 % |
| Y = −30 °C | 5 = +85 | B = ±1.5 % |
| Z = +10 °C | 6 = +105 | C = ±2.2 % |
|             | 7 = +125 | D = ±3.3 % |
|             | 8 = +150 | E = ±4.7 % |
|             | 9 = +200 | F = ±7.5 % |
|             |          | P = ±10 % |
|             |          | R = ±15 %  ← **X5R, X7R, X8R** |
|             |          | S = ±22 %  ← **X6S, X7S** |
|             |          | T = +22/−33 % |
|             |          | U = +22/−56 % |
|             |          | V = +22/−82 % ← **Y5V** |
|             |          | L = +15/−40 % (industry non-EIA) ← **X8L** |

---

## 5. Reliability model

### 5.1 Geometry factor (microstructure)
From [nasa-nepp-bme-mlcc-reliability] Eqs. 12–14:
$$
P \;=\; \left(1 - \left(\tfrac{\bar r}{d}\right)^{\alpha}\right) \qquad (\alpha \approx 6 \text{ for } V\le 50\text{ V},\; \alpha \approx 5 \text{ for } V > 50\text{ V})
$$

Whole-MLCC structural reliability:
$$
R_\text{geom}(N, d, \bar r) \;=\; P^{N}
$$

Note the **amplifier effect of N**: single-layer reliability 0.99 → at N=200, only 0.134.

### 5.2 Voltage/temperature acceleration (TTF)
**PME — single-mode Prokopowicz-Vaskas:**
$$
\frac{t_1}{t_2} \;=\; \left(\frac{V_2}{V_1}\right)^{n} \exp\left[\frac{E_a}{k}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)\right] \quad (n\approx 3,\; 1<E_a<2\text{ eV})
$$

**BME — two-mode (catastrophic + slow degradation):**
- Catastrophic (power law): η(V,T) = C/V^n · exp(Ea₁/kT)
- Slow degradation (exponential): η(E,T) = C′·exp(−b·E) · exp(Ea₂/kT)

Combined Weibull:
$$
R(t) = P^{N} \cdot \Big[p\cdot e^{-(t/\eta_1)^{\beta_1}} \;+\; (1-p)\cdot e^{-(t/\eta_2)^{\beta_2}}\Big]
$$

### 5.3 MTTF
$$
\text{MTTF} \;=\; \eta \cdot \Gamma(1 + 1/\beta) \;\approx\; 0.9\,\eta \quad (\beta > 3)
$$

---

## 6. Parasitics (ESR, ESL, SRF)

### 6.1 Equivalent circuit
$$
Z(\omega) \;=\; \sqrt{\text{ESR}^2 + \big(\omega L_\text{ESL} - 1/\omega C\big)^2}
$$
**Source:** [kyocera-avx-esr-esl-decoupling] Eq. 1.

### 6.2 SRF
$$
f_\text{SRF} \;=\; \frac{1}{2\pi\sqrt{L_\text{ESL}\cdot C}}
$$
Example: 10 µF · 0.5 nH → 7 MHz [kyocera-avx-esr-esl-decoupling].

### 6.3 ESR
Two parts: (a) dielectric loss `R_d = tan δ / (ω·C)` (dominates below SRF); (b) electrode resistance `R_e` (dominates above SRF). For decoupling apps, designer cares about minimum ESR near SRF.

**Material effect**: Cu inner electrode (BME RF parts) gives lowest R; Ni-BME ~3× higher; Pd-PME higher still — [psma-ceramic-capacitor-basics].

### 6.4 ESL
Geometric, dominated by current loop. Long-narrow term-to-term geometry has higher L; short-wide (reverse-aspect) and interdigitated patterns lower it.
- Standard 0402 X7R: ~ 0.5–1.0 nH
- Reverse-geometry 0306/0204: 0.2–0.5 nH
- LICC (low-inductance chip caps): 0.1–0.3 nH

---

## 7. Rated voltage (Vr)

$$
V_r \;=\; E_\text{rated} \cdot d
$$
with `E_rated ≈ 25 V/µm` for X7R/X5R BME at commercial grade. Withstand voltage test (Class II) is **2.5 × Vr** for 1–5 s without breakdown — [samsung-cl-series].

For high-voltage MLCCs (>100 V) the simulator must check:
- Bulk breakdown: `E < E_bd_intrinsic` (margin ≥ 3×)
- Surface arcing: function of creepage distance (chip length minus 2·m_end), surface coating, humidity — see [kemet-mlcc-design-and-characteristics] for ArcShield mitigation.

---

## 8. Worked example (sanity check)

**Inputs**: X7R BME 0805, d = 1.0 µm, N = 300, εr0 = 2500, V = 6.3 V, T = 25 °C.

- A = (2.01 − 2·0.25)(1.25 − 2·0.15) mm = 1.51 × 0.95 = **1.43 mm²**
- C₀ = 2500 × 8.854e-12 × (1.43e-6 × 300) / 1e-6 = **9.5 µF** ✓ (matches the 10 µF/6.3V/0805 X7R market reality)
- Field at rated V: E = 6.3 / 1 = 6.3 V/µm → from §3.1 table, f_VCC ≈ 0.55 → C_eff ≈ 5.2 µF
- At 3.3 V: E = 3.3 V/µm → f_VCC ≈ 0.82 → C_eff ≈ 7.8 µF
- After 10 000 h aging at zero bias (1.5 %/decade × 4 decades): −6 % → C_eff(0V, 10⁴ h) ≈ 8.9 µF
- After 10 000 h at 6.3 V DC bias (competitor rate ≈ 8 %/decade × 4 dec): another −32 % on top of VCC → C_eff ≈ 3.5 µF
- SRF with ESL ≈ 0.5 nH: f_SRF ≈ 2.4 MHz

These numbers all fall inside the published vendor envelopes. ✓

---

## 9. Open gaps for v1

- [ ] Empirical `(E₀, p)` fits to `f_VCC` per published vendor curve set (need digitized Murata GRM / Samsung CL DC-bias curves at multiple case sizes and rated voltages — datasheets give graphs, not equations).
- [ ] Better `εr(T)` curve for X7R near `Tc` than the ±15 % box (vendor measured curves at 1 kHz vs 1 MHz differ).
- [ ] BME `n` for the catastrophic-failure branch — typical literature values cluster 2.5–6 depending on extraction method.
- [ ] εr-vs-grain-size data points for sub-200 nm range (the regime where state-of-the-art parts now live).
- [ ] Case-size-specific `H_max` and `d_cover` for all Tier-1 vendors (Samsung CL has it; need TDK, Murata, TY).
- [ ] AEC-Q200 derating curves for automotive grade — currently approximated as the commercial curve × 0.8.

---

## 10. Source registry

Short keys used above. Full bibliography is maintained in `resources/bibliography.md` (TBC).

- `[kemet-mlcc-design-and-characteristics]` → `resources/design-rules/kemet-mlcc-design-and-characteristics.md` (Wilmer Companioni, KEMET / PSMA, 2019)
- `[psma-ceramic-capacitor-basics]` → `resources/design-rules/psma-ceramic-capacitor-basics.md` (KEMET / PSMA, 2017)
- `[vishay-x7r-cap-drift-dc-bias]` → `resources/design-rules/vishay-x7r-cap-drift-dc-bias.md` (Coppens et al., Vishay, Dec 2021)
- `[kyocera-avx-esr-esl-decoupling]` → `resources/design-rules/kyocera-avx-esr-esl-decoupling.md` (Cain, KYOCERA AVX, CARTS 1997)
- `[murata-grm-series-tcc-data]` → `resources/market/murata-grm-series-tcc-data.md`
- `[samsung-cl-series]` → `resources/market/samsung-cl-series-mlcc-ds.md`
- `[nasa-nepp-bme-mlcc-reliability]` → `resources/literature/nasa-nepp-bme-mlcc-reliability.md` (Liu, NASA NEPP, 2013)
- `[nasa-batio3-failure-mechanisms]` → `resources/literature/nasa-batio3-mlcc-failure-mechanisms.md` (Liu & Sampson, CARTS 2012)
- `[knowles-fundamentals-3]` → Knowles Capacitor Fundamentals Part 3 (factors affecting capacitance)
- `[knowles-fundamentals-8]` → Knowles Capacitor Fundamentals Part 8 (dielectric classifications)
- `[passive-components-eu-mlcc-loss]` → passive-components.eu high-CV MLCC DC bias and aging loss article
- `[adv-mater-2026-grain-boundary]` → An et al., *Adv. Mater.* 2026, doi:10.1002/adma.202507233 (microstructure optimization via grain-boundary segregation)
- Patents observed: WO2024247128A1 (Murata, 2024); US 11,211,181 / 11,295,894 / 11,763,990 / 11,776,748 / 12,488,941 (Samsung Electro-Mechanics, BaTiO₃ + Tb/Dy)
