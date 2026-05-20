---
title: Decoupling Capacitor Design Rules (PDN Target Impedance)
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - kyocera-avx-esr-esl-decoupling.md
tags:
  - paper
---

# Decoupling Capacitor Design Rules (PDN Target Impedance)

The **application layer** on top of the MLCC physics. Tells you **how many capacitors of what value to place where** so that the power distribution network (PDN) meets the IC's voltage-noise budget across frequency. Modern best practice is the **target-impedance method**, which replaced the legacy "three capacitor values" rule of thumb in the early 2000s.

## Target impedance method

The PDN's job is to deliver current to the IC with bounded voltage fluctuation. Given:
- `ΔV_max` = maximum allowable ripple at the IC pin
- `I_max` = peak transient current the IC will draw

The required PDN impedance is:
$$
Z_\text{target} \;=\; \frac{\Delta V_\text{max}}{I_\text{max}}
$$

The decoupling network must keep `|Z_PDN(f)| ≤ Z_target` across the operating frequency range (typically DC to f_clk × 3–5).

**Example** (passive-components.eu analysis of automotive PDN):
- Operating window 1.35 V – 1.5 V (150 mV total budget)
- Subtract VRM tolerance and IR drop → AC budget ≈ 46 mV
- Peak dynamic current step = 1 A
- **Z_target ≈ 46 mΩ**

For modern compute ICs:
- Microcontroller: Z_target ~ Ω
- Application processor: Z_target ~ 10–100 mΩ
- Server CPU / GPU: Z_target < 10 mΩ
- Network processor: Z_target down to **< 10 µΩ** at peak (six orders of magnitude span across markets!)

## The "myth of three capacitor values"

Legacy guidance: place 10 µF + 100 nF + 1 nF in parallel, with each cap covering a different frequency band based on its self-resonant frequency (SRF). This was based on **through-hole capacitor technology** where:
- 47 µF electrolytic: ~ 30 nH ESL
- 0.1 µF ceramic disc: ~ 7 nH ESL
- ESL scaled with case size → smaller case = higher-f effectiveness

**For modern MLCC, this rule is wrong.** [[esr-esl-srf|ESL of an MLCC]] depends on **mounting geometry**, not capacitance value. A 10 µF MLCC and a 100 nF MLCC, mounted in the same footprint, have essentially the **same ESL** (~0.5–1 nH). The benefit of stacking three different values across the frequency spectrum largely **vanishes**.

Worse, three different values in parallel produce **anti-resonance peaks** between their SRFs:
$$
f_\text{antires} \;=\; \frac{1}{2\pi\sqrt{L_1 \cdot C_2}}
$$
where `L_1` is ESL of the smaller-cap and `C_2` is the larger-cap. At this frequency the impedance **spikes upward**, often well above either cap's individual peak — exactly the opposite of what the design intended.

## Modern recommended approach

### Step 1 — Define target impedance
$$
Z_\text{target} = \Delta V_\text{max} / I_\text{max}
$$

### Step 2 — Use same-value caps in parallel
N parallel identical caps have impedance `1/N × Z_single`. No anti-resonance peaks because they're all at the same SRF.
Recommended: 4–8 same-value caps near each IC power pin, distributed around the package perimeter.

### Step 3 — Stack frequency bands with different SRFs only when necessary
If a single cap value can't cover the full frequency band, add a second value but **engineer the ESR** to damp the anti-resonance:
$$
\text{ESR}_\text{required} \;\geq\; \sqrt{L_1/C_2}
$$
This is sometimes called the **controlled-ESR approach** ([[kyocera-avx-esr-esl-decoupling|Cain CARTS 1997]] discusses early version).

### Step 4 — Minimize mounting inductance
ESL is dominated by **via length + via-pair spacing**, not the cap itself. Per the passive-components.eu PDN analysis: "minimizing via length and keeping vias close together reduces ESL significantly compared to capacitor height or power plane spreading inductance effects."

Concrete rules:
- Via length: ≤ board thickness; use thinner stackups or buried vias when possible.
- Via pair spacing: < 0.5 mm (close together = lower loop inductance).
- Place capacitor as close as possible to IC pin (loop area is dominant).

### Step 5 — Account for DC bias and temperature derating
A 10 µF X7R 6.3 V at the actual operating point can be 4–6 µF effective. **Specify Z_PDN at the derated capacitance**, not at nominal. Vendor [[vendor-spice-models|dynamic SPICE models]] capture this automatically.

## Anti-resonance damping with ESR

The peak impedance of two paralleled cap families:
$$
Z_\text{peak} \;\approx\; \sqrt{\frac{L_1}{C_2}} \quad\text{(if undamped)}
$$

Adding ESR `R_d` flattens the peak:
$$
Z_\text{peak,damped} \;=\; Z_\text{peak,undamped} \;\cdot\; \frac{1}{1 + 2\zeta\sqrt{C_2/C_1}}
$$
with damping ratio ζ = R_d / (2·√(L_1/C_2)).

Special MLCC products with **engineered ESR** (e.g., KEMET's "ESR-controlled" series, KYOCERA AVX's high-Q vs lossy variants) exist specifically for this purpose.

## Bandini Mountain (on-die resonance)
A separate resonance often dominates above ~ 100 MHz: the interaction between **on-die capacitance** and **package lead inductance**. No board-level decoupling cap can damp this — it must be addressed at the package or on-die level. Mentioned because system-level PDN analysis must account for it.

## Design output: a parts list and placement

The simulator's design-rule output should be:
- Recommended cap count, value, dielectric class per power pin / per rail
- Z_PDN(f) plot showing target compliance
- Anti-resonance peak prediction
- DC-bias-derated capacitance per part
- Recommended placement zone (max distance to IC pin in mm)
- AEC-Q200 / grade requirements per part

## Cross-references
- [[esr-esl-srf]]
- [[dc-bias-derating]]
- [[mlcc-capacitance-equation]]
- [[case-size-geometry]] (low-ESL reverse geometry)
- [[vendor-spice-models]]
- [[kyocera-avx-esr-esl-decoupling]]
- [[mlcc-pcb-layout-rules]]

## References
- [[kyocera-avx-esr-esl-decoupling]] — Cain CARTS 1997
- "The Myth of Three Capacitor Values" — *Signal Integrity Journal* 2020 (Larry Smith / Eric Bogatin school)
- "Analysis of Multi-Layer Ceramic Capacitors used in Power Distribution Networks" — passive-components.eu
- US Patent 8,627,261 "Method and apparatus for performing automatic decoupling capacitor selection for power distribution networks"
