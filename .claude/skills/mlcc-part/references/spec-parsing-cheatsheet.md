# Parsing natural-language MLCC specs

The skill's NL-to-filters operation expects you (the assistant) to read user prose
and convert it into structured filters that `scripts/mlcc.py search` accepts. This
sheet gives the canonical mappings and edge-case handling.

## Capacitance

| User phrase                          | Filter            |
|--------------------------------------|-------------------|
| `1uF`, `1 µF`, `1 uF`, `1 microfarad`| `--C-uF 1.0`      |
| `100nF`, `100 nF`, `0.1uF`           | `--C-uF 0.1`      |
| `10pF`, `10 pF`                      | `--C-uF 0.00001`  |
| `>= 10uF`, `at least 10uF`, `10uF+`  | `--C-uF-min 10`   |
| `1uF or higher`                      | `--C-uF-min 1.0`  |
| `under 1nF`, `< 1nF`                 | `--C-uF-max 0.001` |

Default exact-match tolerance is ±5 % to absorb floating-point and E-series quirks.

## Voltage

| User phrase           | Filter        |
|-----------------------|---------------|
| `50V`, `50 volt`      | `--V 50`      |
| `50V rated`           | `--V 50`      |
| `at least 50V`        | `--V-min 50`  |
| `under 100V`          | `--V-max 100` |
| `≥ 16V`, `>= 16V`     | `--V-min 16`  |

## Case size

Map the user's wording to the **canonical case ID** (`<EIA>_<metric>`):

| User phrase                       | Canonical case ID |
|-----------------------------------|--------------------|
| `0805`, `EIA 0805`, `2012m`       | `0805_2012`        |
| `metric 2012`                     | `0805_2012`        |
| `0603`, `EIA 0603`                | `0603_1608`        |
| `metric 0603`, `0603m`            | `0201_0603` ⚠      |
| `0402`, `EIA 0402`                | `0402_1005`        |
| `1206`                            | `1206_3216`        |

> ⚠ Bare `0603` without `m`/`i` defaults to **EIA** here because most engineers
> say "0603" meaning EIA. The full disambiguation table is in
> `wiki/concepts/case-size-geometry.md`. If the user wrote `0603m` they meant the
> tiny metric variant (= EIA 0201).

## Dielectric class

Direct match, case-insensitive:

| User phrase                                   | Filter         |
|-----------------------------------------------|----------------|
| `X7R`, `X7R-grade`, `Class II X7R`            | `--cls X7R`    |
| `X5R`                                         | `--cls X5R`    |
| `C0G`, `NP0`, `Class I`, `temperature-stable` | `--cls C0G`    |
| `X8R`, `automotive 150°C`                     | `--cls X8R`    |
| `Y5V`, `Class III` (rare in modern designs)   | `--cls Y5V`    |

## Vendor preference

| User phrase                       | Filter            |
|-----------------------------------|-------------------|
| `Murata only`, `from Murata`      | `--mfr Murata`    |
| `Samsung`, `SEMCO`                | `--mfr Samsung`   |
| `TDK`                             | `--mfr TDK`       |
| `KEMET`                           | `--mfr KEMET`     |
| (no mention)                      | (no filter)       |

## Combined inference

Some queries imply constraints without naming them. Use these defaults
when the user's intent is clear:

| User phrase                          | Inferred filters                          |
|--------------------------------------|-------------------------------------------|
| `high-CV decoupling cap`             | `--cls X5R` (best CV at low V), `--V-max 25` |
| `power-rail bypass`                  | `--cls X7R`, `--C-uF-min 1.0`             |
| `RF / timing cap`                    | `--cls C0G`                               |
| `automotive`                         | `--cls X8R` or `--cls X7R` + mfr=automotive series |
| `smartphone-class smallest cap`      | `--case 0402_1005` or smaller             |

## Don't infer too much

If the user is vague, prefer **fewer filters** (more results) over guessing.
Example: `"a couple-microfarad cap for a 12V rail"` → `--C-uF-min 1 --C-uF-max 10
--V-min 25` (12V rail typically wants 25V-rated parts; do NOT pin C to exactly 2 µF).

When in doubt, surface the inferred filters in your output so the user can adjust.
