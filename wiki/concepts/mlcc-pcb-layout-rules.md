---
title: MLCC PCB Layout & Mechanical Handling Rules
type: concept
created: 2026-05-20
updated: 2026-05-20
sources:
  - kemet-mlcc-design-and-characteristics.md
  - psma-ceramic-capacitor-basics.md
tags:
  - paper
---

# MLCC PCB Layout & Mechanical Handling Rules

The board-level boundary conditions for an MLCC. Pad geometry, placement zone, soldering process, and mechanical-stress profile determine whether the part actually delivers its specified electrical performance or fails by cracking, tombstoning, or thermal shock. The simulator's design-rule output should surface these constraints alongside the electrical model.

## Pad design (IPC-7351 framework)

IPC-7351B is the global standard for SMT footprint design. Three pad-density classes:
- **Density Level A (Most Land Protrusion)**: larger pads, better solder-joint reliability, less anti-tombstoning risk. Used for high-reliability / automotive.
- **Density Level B (Median Land Protrusion)**: balanced. Default for industrial / consumer.
- **Density Level C (Least Land Protrusion)**: smallest pads, highest board density. Used for handhelds / wearables.

### Anti-tombstoning pad rules
Tombstoning ("Manhattan defect") happens when uneven solder reflow lifts one end of the chip vertical. Cause: asymmetric heat capacity / wetting force between the two pads.

Anti-tombstoning rules:
1. **Both pads identical** in size, shape, and via-out routing.
2. **Pad length under the chip** ≥ component metal-end width (gives "anti-tombstoning moment T2").
3. **Symmetric thermal mass**: no thermal-vias under one pad and not the other.
4. **No traces of widely different widths** entering the two pads (one big copper plane on one side + thin trace on other = asymmetric thermal sink → tombstoning).
5. **Solder paste deposition equal mass** on both pads (no aperture asymmetry in the stencil).

Following IPC-7351 reduces first-pass tombstoning rate by **>30 %** vs uncontrolled design.

### Typical pad dimensions for common case sizes (IPC-7351B Level B, mm)
| Case | Pad width | Pad length | Pad separation |
|---|---|---|---|
| 0402 (1005) | 0.55 | 0.50 | 0.50 |
| 0603 (1608) | 0.90 | 0.80 | 0.70 |
| 0805 (2012) | 1.30 | 1.00 | 0.90 |
| 1206 (3216) | 1.70 | 1.10 | 1.80 |
| 1210 (3225) | 2.60 | 1.10 | 1.80 |
| 1812 (4532) | 3.30 | 1.30 | 2.80 |
| 2220 (5750) | 5.10 | 1.30 | 4.10 |

These are starting points; final values depend on solder paste stencil, reflow profile, and reliability requirements.

## Placement rules

### Distance to IC pin (decoupling)
Mounting inductance dominated by via length + loop area:
$$
L_\text{mount} \approx 0.4 \cdot (\text{loop length in mm}) \;\text{nH}
$$
Practical:
- Decoupling caps: place **within 5 mm** of IC pin for handhelds; **within 10 mm** for industrial.
- Use both top-side and bottom-side placement if package density allows.
- Vias from cap pads directly to power/ground planes: < 0.5 mm trace before via.

### Flex-zone exclusion (for boards that flex)
Standard MLCCs ([[failure-modes-mlcc|flex-crack-prone]] above 0805):
- **No MLCCs within 5 mm** of board cutouts, panel-tab break-points, mounting screws (the high-stress zones).
- **No MLCCs parallel to board flex axis** for cases ≥ 1206 — orient perpendicular so the chip length compresses, not bends.
- For 1812 / 2220 cases in flex-prone designs, **mandate soft-termination** or open-mode designs ([[failure-modes-mlcc]] mitigation levels 2–3).

### Thermal-shock zones
Hand-soldering / wave-soldering creates large local ΔT. Mitigations:
- **Pre-heat the assembly** to within 80 °C of the soldering iron temperature before contact.
- **Don't touch the chip body** with the soldering iron — only the pad.
- **Larger case sizes more sensitive** to thermal shock (more thermal-expansion mismatch). 1812 / 2220 in high-thermal-shock environments need flex termination.

## Soft-termination zones

Replace standard MLCCs with [[termination-and-plating|soft-termination variants]] when **any** of:
- Board can flex in service (> 2 mm flex over the cap location)
- Hand-soldering / rework is anticipated
- Wave-soldering (high local ΔT)
- Large case sizes (≥ 1812) in any vibration-prone environment

Cost premium for soft-termination is ~ 50 % over standard.

## Reflow profile interaction

JEDEC J-STD-020E governs the reflow profile:
- **Peak temperature**: 245–260 °C for Pb-free SAC305 solder
- **Time above 217 °C**: 60–150 s
- **Ramp rate**: ≤ 3 °C/s during ramp-up
- **Cool-down rate**: ≤ 6 °C/s

Excessive thermal ramp causes [[failure-modes-mlcc|thermal-shock crack]] in MLCC (the parallel-plate crack). Larger case sizes are more sensitive.

Class II/III parts pick up moisture during storage; MSL-3 rated MLCCs require **bake-out before reflow** (typically 125 °C for 24 h) if exposed to ambient > 168 h.

## Connections to the simulator

The simulator should output **layout constraints alongside electrical predictions**:
- Recommended pad geometry per IPC-7351 density level
- Soft-termination requirement (yes/no) based on case size + flex requirement
- Tombstoning risk score based on case size + design context
- Max distance to IC pin for the decoupling Z_target to hold
- Reflow profile warnings if standard SAC305 violates the part's spec

## Cross-references
- [[failure-modes-mlcc]]
- [[termination-and-plating]]
- [[case-size-geometry]]
- [[decoupling-design-rules]]
- [[kemet-arcshield]]
- [[esr-esl-srf]]

## References
- [[kemet-mlcc-design-and-characteristics]] — flex-crack mitigation hierarchy
- [[psma-ceramic-capacitor-basics]] — board-flex / thermal-shock background
- IPC-7351B: SMT Land Pattern Design Standard
- JEDEC J-STD-020E: Reflow Profile Standard
- IPC-7711/7721: Rework / Repair guidelines
