---
name: mlcc-part
description: Decode, cross-reference, and search MLCC (multi-layer ceramic capacitor) part numbers across vendors. Use this skill whenever the user mentions an MLCC part number (Murata GRM/GCM/GJM, Samsung SEMCO CL, TDK C-series, KEMET C-spec), asks to find an equivalent part at another vendor, or describes capacitor specs in plain English ("0805 X7R 1µF 50V", "10uF X5R for a 6.3V rail", "what is GRM21BR71H475K"). Handles three operations: natural-language spec → part list, part number → structured specs, part number → cross-vendor equivalents.
---

# MLCC part number skill

Decodes MLCC part numbers, finds equivalents across vendors, and searches a curated
parts database from natural-language specs. Backed by a Python CLI in `scripts/mlcc.py`
and a JSON database of verified parts.

## When this skill triggers

- The user types **an MLCC part number** (anything starting with `GRM`, `GCM`, `GJM`, `GRT`, `GA3`, `CL`, `CG`, `CW`, `CGA`, or `C` + 4 digits).
- The user describes a capacitor in **plain English** with units (µF, nF, pF, V) or class names (C0G, X5R, X7R, X8R, Y5V).
- The user asks for **"the same part at another vendor"** or **"a cross-reference"**.
- The user asks **what a part number means** or **how to decode** it.

If the user mentions resistors, inductors, tantalum / film / aluminium-electrolytic caps,
DO NOT use this skill — it covers MLCC only.

## Three operations

### 1. Part number → specs (decode)

When the input is a single part number, decode it.

```
python3 scripts/mlcc.py decode <PN>
```

Returns vendor, case, dielectric class, capacitance, voltage, tolerance, and the
raw vendor-specific codes (plating, control, packaging).

### 2. Part number → cross-vendor equivalents (cross)

When the user wants the "same part" at other vendors:

```
python3 scripts/mlcc.py cross <PN>
```

Decodes the input, then searches the database for exact matches at other vendors
(same case + class + voltage + capacitance within 5 %). If no exact matches, falls
back to nearest matches (same case + class) sorted by spec proximity.

### 3. Natural-language specs → part list (search)

When the user describes a capacitor in plain English, parse the description into
structured filters first (see `references/spec-parsing-cheatsheet.md`), then:

```
python3 scripts/mlcc.py search [--case 0805_2012] [--cls X7R] [--C-uF 1.0] [--V 50]
                                [--V-min N] [--V-max N] [--C-uF-min N] [--C-uF-max N]
                                [--mfr Murata]
```

## How to handle user input

**Step 1: classify the input.** Without thinking too hard:

- Single token, alphanumeric, no spaces, starts with a known prefix, length 10–20 → **part number** → run `decode` (and offer `cross` as next step).
- Contains unit words (`uF`, `nF`, `pF`, `V`), or class names (`X7R`, `C0G`, etc.), or case sizes (`0805`, `1206`) → **specs** → parse to filters and run `search`.
- Mixed (PN plus modifiers) → decode the PN, then narrow with the modifiers as a `search` call.

**Step 2: detect the explicit verb if the user used one.**

- "decode X" or "what is X" → `decode`
- "cross X" or "alternatives to X" or "equivalent of X" → `cross`
- "find X" or "search for X" or "I need X" → `search`

If no verb is present and the input looks like a part number, default to **decode + cross**
(show specs and same-spec parts at other vendors in one response).

**Step 3: parse natural-language specs.**

Use `references/spec-parsing-cheatsheet.md` for the canonical mappings.
Convert phrases like "1uF X7R 50V 0805" into:

```
python3 scripts/mlcc.py search --case 0805_2012 --cls X7R --C-uF 1.0 --V 50
```

If the user is vague, prefer fewer filters over guessing. Surface the inferred
filters in the output so the user can correct them.

**Step 4: present the result.**

Use the CLI's plain-text output by default. It's already formatted for humans.
Pass `--json` if you need machine-readable output to compose with other tooling.

## Database miss → web search escalation

If `search` or `cross` returns zero matches, the database is too small to answer
the question. Don't dead-end — offer to escalate to web search:

> "No matches in the local database. Want me to search Mouser / Octopart / DigiKey
> for 0805 X7R 1µF 50V parts?"

If the user agrees, use the `WebSearch` tool with a query like:
`"0805" "X7R" "1uF" "50V" site:mouser.com OR site:octopart.com OR site:digikey.com`

When a new verified part is found via web search, **suggest adding it** to
`data/vendor_parts.json` so future invocations don't need the same web call.

## Adding new parts to the database

When the user provides a verified vendor part number (from a real Mouser/LCSC/DigiKey
page, not a guess), append it to `data/vendor_parts.json` with:

```json
{ "case": "0805_2012", "cls": "X7R", "V": 50, "C_uF": 1.0,
  "mfr": "Murata", "pn": "GRM21BR71H105KA01" }
```

Then run `python3 scripts/mlcc.py validate` to confirm the part decodes consistently.
The validate step is the safety net — it catches the kind of metadata typo
(50 V vs 25 V) that this skill was originally built to prevent.

## Adding new vendors

See `references/vendor-formats.md` §"How to add a new vendor". The pattern:
new JSON file in `data/`, new `parse_<vendor>` function in `scripts/decoders.py`,
prefix added to the dispatcher, verified parts added to the database.

## Validate the database

Periodically (or after edits to either `vendor_parts.json` or any decoder):

```
python3 scripts/mlcc.py validate
```

Reports any database entry whose declared `case` / `cls` / `V` / `C_uF` doesn't match
what the decoder extracts from the part number. Zero failures is the goal.

For a full regression run (decoder + database + edge cases):

```
python3 scripts/test_mlcc.py
```

## Output style

- For `decode`: a structured one-line-per-field block. Include human-readable case label.
- For `cross`: input summary on one line, then a table of matches (or near-matches with proximity ranking).
- For `search`: one-line filter summary, then a table of matches.
- Always include match count.
- For empty results, say so clearly and offer the web-search escalation.

## Files in this skill

- `scripts/mlcc.py` — CLI entry point (decode / cross / search / validate sub-commands)
- `scripts/decoders.py` — per-vendor parsers (SEMCO, Murata, TDK, KEMET) and auto-dispatch
- `scripts/search.py` — database load and filter logic
- `scripts/test_mlcc.py` — standalone test suite (run with `python3`, no pytest needed)
- `data/cases.json` — case-size lookup
- `data/classes.json` — dielectric class info
- `data/{semco,murata,tdk,kemet}_codes.json` — per-vendor field grammars
- `data/vendor_parts.json` — curated database of verified parts (self-validating)
- `references/vendor-formats.md` — detailed field grammars for each vendor (read for edge cases)
- `references/spec-parsing-cheatsheet.md` — how to convert natural-language specs into CLI filters

The skill is self-contained: no dependencies on the rest of the chip-sim project,
no external Python packages beyond the standard library.
