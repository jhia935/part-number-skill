# MLCC vendor part-number formats

Field-by-field grammars for the four Tier-A MLCC vendors. Use this as the human-readable
companion to the JSON code tables in `data/*.json`. The Python decoders in
`scripts/decoders.py` are the authoritative implementation; everything here exists to
help you reason about edge cases or extend the skill.

## Samsung Electro-Mechanics (SEMCO) — CL series

**Length**: exactly 15 characters.
**Example**: `CL21B105KAFNNNE` = 0805 / X7R / 1 µF / ±10 % / 25 V / Ni-Cu BME / normal / embossed tape.

| Pos | Len | Field        | Notes |
|-----|-----|--------------|-------|
| 0   | 2   | Prefix `CL`  | also `CG`, `CW` for automotive sub-series |
| 2   | 2   | Size code    | 03 / 05 / 10 / 21 / 31 / 32 / 43 / 55 |
| 4   | 1   | TCC          | B=X7R, A=X5R, C=C0G, F=Y5V, X=X6S, P/R/S/T/U=C0G sub-codes |
| 5   | 3   | Capacitance  | D1·10+D2 × 10^M pF; R = decimal point for sub-pF |
| 8   | 1   | Tolerance    | K=±10 %, J=±5 %, M=±20 %, F=±1 %, G=±2 %, Z=+80/-20 % |
| 9   | 1   | Voltage      | A=25, B=50, C=100, P=10, Q=6.3, O=16, … (full table in `semco_codes.json`) |
| 10  | 1   | Thickness    | vendor-internal option code |
| 11  | 1   | Plating      | N=Ni/Cu BME, A=Pd/Ag PME, G=Cu/Cu |
| 12  | 1   | Control      | N=normal, P=automotive, L=LICC, C=high-Q, A/B=array |
| 13  | 1   | Reserved     | usually N |
| 14  | 1   | Packaging    | E=embossed tape, C=cardboard, etc. |

## Murata — GRM / GCM / GJM / GRT series

**Length**: variable, 13–18 characters (core 14 + optional termination/packaging/revision).
**Example**: `GRM21BR71H475K` = 0805 / X7R / 50 V / 4.7 µF / ±10 % (core only).
Full form like `GRM21BR71H475KA01` adds termination + packaging + revision.

| Pos | Len | Field        | Notes |
|-----|-----|--------------|-------|
| 0   | 3   | Prefix       | `GRM` (general), `GCM`/`GCJ` (automotive AEC-Q200), `GJM` (RF), `GRT` (soft-term) |
| 3   | 2   | Size         | 03 / 15 / 18 / 21 / 31 / 32 / 43 / 55 (same as SEMCO numbering) |
| 5   | 1   | Thickness    | letter or digit; vendor internal |
| 6   | 2   | TCC          | **5C=C0G; R6=X5R; R7=X7R; R8=X8R; F5=Y5V** (R5 is NOT a standard Murata letter — X5R uses R6) |
| 8   | 2   | Voltage      | 0E=2.5, 0G=4.0, 0J=6.3, 1A=10, 1C=16, 1E=25, 1H=50, 2A=100, 2E=250, 2W=450, … |
| 10  | 3   | Capacitance  | same EIA encoding as SEMCO |
| 13  | 1   | Tolerance    | same EIA letters |
| 14+ | *   | Tail         | termination / packaging / revision, optional |

> Common pitfall: it's tempting to map R5→X5R by analogy with R7→X7R, but
> **Murata does not use R5 for X5R production parts**. X5R is encoded as `R6`.
> Verified against the well-known `GRM21BR61E106K` (0805 X5R 10 µF 25 V).

## TDK — C-series

**Length**: variable, 14+ characters. The first ~14 are the structured part code; the tail is
the thickness-in-0.01mm-units (3 digits) plus packaging/control.
**Example**: `C2012X7R1H105K` = 0805 (metric 2012) / X7R / 50 V / 1 µF / ±10 %.
Full form: `C2012X7R1H105K085AC` adds 0.85 mm thickness, A=packaging, C=control.

| Pos | Len | Field        | Notes |
|-----|-----|--------------|-------|
| 0   | 1   | Prefix       | `C` for general, `CGA` for automotive |
| 1   | 4   | Size         | **metric**: 1005 / 1608 / 2012 / 3216 / 3225 / 4532 / 5750 |
| 5   | 3   | Class        | literal `C0G`, `X5R`, `X7R`, `X8R`, `Y5V`, `NP0`, `U2J`, etc. |
| 8   | 2   | Voltage      | 1A=10, 1C=16, 1E=25, 1H=50, 2A=100, 2E=250, 2W=450, 2J=630, … |
| 10  | 3   | Capacitance  | same EIA encoding |
| 13  | 1   | Tolerance    | same EIA letters |
| 14+ | *   | Tail         | thickness (3 digits = mm × 100) + packaging + control |

> TDK is unique in spelling out the class literally (`X7R` not `R7`).
> NP0 and U2J are Class I sub-codes that we normalise to `C0G`.

## KEMET — C-spec

**Length**: variable, 14+ characters.
**Example**: `C0805C105K5RAC` = 0805 (EIA) / 1 µF / ±10 % / 50 V (5R) / X7R (A=X5R? — see warning) / termination C.

| Pos | Len | Field         | Notes |
|-----|-----|---------------|-------|
| 0   | 1   | Prefix `C`    | |
| 1   | 4   | Size          | **EIA**: 0402 / 0603 / 0805 / 1206 / 1210 / 1812 / 1825 / 2220 |
| 5   | 1   | Case style    | C=standard; A/B/E for special geometries |
| 6   | 3   | Capacitance   | same EIA encoding |
| 9   | 1   | Tolerance     | same EIA letters |
| 10  | 2   | Voltage       | KEMET uses its own 2-char codes (5R / 1H / 3K …); see `kemet_codes.json` |
| 12  | 1   | Dielectric    | **R=X7R, A=X5R, G=C0G, P=X8R, U=Y5V** |
| 13+ | *   | Tail          | termination + packaging |

> **KEMET caveat**: KEMET maintains *several* part-code families (C-spec, HP, KGM, T520, …).
> This skill only covers the standard commercial C-spec format. Specialty / film capacitor /
> tantalum codes will fail to decode and that's correct behaviour — they're different products.

## Yageo — CC series

**Length**: exactly 17 characters.
**Example**: `CC0402MRX5R5BB106` = 0402 / ±20 % / paper tape / X5R / 6.3 V / 10 µF.

| Pos | Len | Field        | Notes |
|-----|-----|--------------|-------|
| 0   | 2   | Prefix `CC`  | |
| 2   | 4   | Size         | **EIA**: 0201, 0402, 0603, 0805, 1206, 1210, 1812, 1825, 2220 |
| 6   | 1   | Tolerance    | J=±5 %, K=±10 %, M=±20 %, Z=+80/-20 % |
| 7   | 1   | Packing      | R=paper 7" / K=blister 7" / P=paper 13" / F=blister 13" |
| 8   | 3   | Dielectric   | literal: `X5R`, `X7R`, `NP0`, `Y5V`, `X8R`, etc. |
| 11  | 1   | Voltage      | **single digit**: 5=6.3 V, 6=10 V, 7=16 V, 8=25 V, 9=50 V, B=100 V, D=250 V |
| 12  | 2   | Process      | `BB` = standard termination; other process codes for special variants |
| 14  | 3   | Capacitance  | same EIA encoding as everyone else |

> Yageo writes the dielectric class **literally** in the part code (like TDK), but the voltage is a **single digit** (unlike everyone else's 2-char codes). The fixed 17-character length makes it easy to validate.

## Taiyo Yuden — M-series (JMK, LMK, EMK, TMK, AMK, UMK, HMK, GMK)

**Length**: variable, typically 14–17 characters plus a `-X` packaging suffix.
**Example**: `JMK105CBJ106MV-F` = 6.3 V (from JMK) / 0402 / standard termination / X5R / 10 µF / ±20 % / thickness V / packaging F.

| Pos | Len   | Field        | Notes |
|-----|-------|--------------|-------|
| 0   | 3     | Voltage prefix | **Voltage is encoded in the prefix** — JMK=6.3 V, LMK=10 V, EMK=16 V, TMK=25 V, AMK=4 V, UMK=50 V, HMK=100 V, GMK=250 V |
| 3   | 3     | Size         | Taiyo Yuden's own size codes: 105=0402, 107=0603, 212=0805, 316=1206, 325=1210, 432=1812, 550=2220 |
| 6   | 0 or 1| Termination  | **Optional** single char (A, B, C, …) for end-termination variant. Older parts omit it; newer parts include it. |
| —   | 2     | TCC          | `BJ`=X5R, `B7`=X7R, `BB`=X7R (alt), `CG`/`CH`/`C7`/`CK`=C0G, `F5`=Y5V, `EB`=X8R |
| —   | 3     | Capacitance  | same EIA encoding |
| —   | 1     | Tolerance    | same EIA letters |
| —   | 1     | Thickness    | usually V or K |
| —   | 0–N   | Packaging suffix | `-T`, `-F` etc., dash-separated |

> Two unusual choices: (1) **voltage is in the prefix**, not a field after the size; (2) the size codes (105/107/212/…) are Taiyo Yuden's own, not the universal EIA or metric pattern. The optional termination char is the source of regex ambiguity — handled by making the regex group optional.
>
> Verified-real anchor parts: `JMK105CBJ106MV-F` (with termination), `LMK105BJ105KV-F` (without).

## How to add a new vendor

1. Create `data/<vendor>_codes.json` with the same structure (`fields`, `size_to_case`,
   `voltage`, `tolerance`, etc.).
2. Add a `parse_<vendor>` function in `scripts/decoders.py` that returns the canonical
   dict (`vendor`, `prefix`, `pn`, `case`, `cls`, `C_F`, `C_uF`, `V`, `tol_text`, `raw`).
3. Add the prefix to `_PREFIX_DISPATCH` (or extend `decode()` if the prefix overlaps
   with an existing vendor).
4. Add ≥ 2 verified-real parts of that vendor to `data/vendor_parts.json`.
5. Add direct decoder tests + the cross-check loop picks up the new parts automatically.

The cross-check test will catch any mismatch between the decoder output and the
declared metadata — that's the safety net.
