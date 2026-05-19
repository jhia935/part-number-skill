---
title: MLCC Failure Modes
type: concept
created: 2026-05-19
updated: 2026-05-19
sources:
  - kemet-mlcc-design-and-characteristics.md
  - psma-ceramic-capacitor-basics.md
tags:
  - paper
---

# MLCC Failure Modes

Ceramic is brittle, strong in compression, weak in tension. Most MLCC field failures are mechanical, not electrical. The major modes ([[kemet-mlcc-design-and-characteristics]]):

## Cracking
| Mode | Root cause | Where in part | Common case sizes |
|---|---|---|---|
| **Mechanical-damage crack** | Pick-and-place impact, hand mishandling | corner / surface | any |
| **Thermal-shock crack** | Rapid ΔT during hand-soldering or wave soldering; CTE mismatch | parallel-plate (perpendicular to length) | large cases (>0805) more sensitive |
| **Flex crack** | PCB bend stress after mounting | initiates near termination, propagates into active | >0805 |

Failure mode is **not always immediate** — a crack can be latent and surface as a short or open later under thermal cycling.

### Flex-crack mitigation levels
[[psma-ceramic-capacitor-basics]] catalogs four protection levels:

| Level | Technology | Flex capability | Failure mode |
|---|---|---|---|
| 0 | Standard MLCC | up to 2 mm | fail-short |
| 1 | Open-mode or floating-electrode design | up to 2 mm | fail-open (crack doesn't reach active area) |
| 2 | Flexible termination (FT-CAP, conductive epoxy in termination) | up to 5 mm | fail-short |
| 3 | Hybrid: flexible termination + floating electrode | up to 5 mm | fail-open |

Cost climbs with level; volumetric efficiency drops (the protection structures take space).

## Surface arcing
At high voltage (>500 V typical), discharge can occur **outside** the part — across the surface between opposite-polarity terminations or between a termination and an exposed internal electrode of opposite polarity ([[kemet-mlcc-design-and-characteristics]]).

Drivers:
- Humidity (water film raises surface conductivity)
- Contamination (flux residue, dust)
- Creepage distance (limited by chip length minus end margins)
- Local electric field strength

Mitigations:
- **Surface coatings** (low-K conformal): increase creepage path, suppress air ionization. Drawback: any damage / void breaks the protection.
- **Serial electrode design**: split the chip into multiple in-series sub-capacitors, distributing the voltage. Drawback: 1/N effective capacitance.
- **Shield design** (e.g., [[kemet-arcshield]]): add "shield" electrodes that lengthen the field path between opposite-polarity electrodes without sacrificing as much capacitance.

## Insulation resistance degradation
Long-term electrochemical mode, dominant in BME parts: oxygen vacancies migrate under DC bias, accumulate at the cathode-side electrode, and reduce the band gap locally → leakage. Models in [[bme-reliability-model]].

## Implications for simulator
The simulator should flag:
- High-V parts (>100 V) for arcing risk and require a creepage check.
- Large cases (>0805) for flex-crack risk and recommend flex termination or open-mode design.
- Hand-soldering / wave-soldering process choice → thermal-shock margin check (CTE mismatch limit on size and rated voltage).

## References
- [[kemet-mlcc-design-and-characteristics]]
- [[psma-ceramic-capacitor-basics]]
