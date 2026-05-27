"""MLCC part-number decoders for the four Tier-A vendors (SEMCO, Murata, TDK, KEMET).

Lookup tables live in `../data/*.json` so they are a single source of truth and
can be cross-validated by tests.

Each decoder returns a dict with at least these canonical fields:
    vendor, prefix, pn, case, cls, C_F, C_uF, V, tol_text
plus vendor-specific raw codes for forensic inspection.
"""
import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load(name):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)


# Load once at import time
_CASES   = {c["id"]: c for c in _load("cases.json")["cases"]}
_CLASSES = {c["id"]: c for c in _load("classes.json")["classes"]}
SEMCO    = _load("semco_codes.json")
MURATA   = _load("murata_codes.json")
TDK      = _load("tdk_codes.json")
KEMET    = _load("kemet_codes.json")
YAGEO    = _load("yageo_codes.json")
TAIYO    = _load("taiyo_yuden_codes.json")


class DecodeError(ValueError):
    """Raised when a part number can't be parsed."""


# ---------------------------------------------------------------------------
# Shared: capacitance code decoder
# ---------------------------------------------------------------------------

def decode_cap_code(code):
    """Decode the EIA 3-character capacitance code into Farads.

    Standard form: D1 D2 M  →  (D1·10 + D2) × 10^M  pF.
    R-form: 'R' acts as a decimal point for sub-pF values
            ('1R0' = 1.0 pF, 'R47' = 0.47 pF, '4R7' = 4.7 pF).
    """
    if len(code) != 3:
        raise DecodeError(f"cap code must be 3 chars, got {code!r}")
    if "R" in code:
        try:
            pf = float(code.replace("R", "."))
        except ValueError as e:
            raise DecodeError(f"bad R-form cap code {code!r}") from e
        return pf * 1e-12
    if not code.isdigit():
        raise DecodeError(f"cap code must be 3 digits or contain R, got {code!r}")
    d1, d2, m = int(code[0]), int(code[1]), int(code[2])
    return (d1 * 10 + d2) * (10 ** m) * 1e-12


# ---------------------------------------------------------------------------
# Vendor 1: Samsung Electro-Mechanics CL-series
# ---------------------------------------------------------------------------

def parse_semco_cl(pn):
    if not pn.startswith("CL"):
        raise DecodeError(f"not a SEMCO CL part: {pn!r}")
    if len(pn) != SEMCO["length"]:
        raise DecodeError(f"SEMCO CL part must be {SEMCO['length']} chars, got {len(pn)}: {pn!r}")

    size_code = pn[2:4]
    tcc_code  = pn[4]
    cap_code  = pn[5:8]
    tol_code  = pn[8]
    volt_code = pn[9]
    thick     = pn[10]
    plating   = pn[11]
    control   = pn[12]
    reserved  = pn[13]
    packaging = pn[14]

    case = SEMCO["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown SEMCO size code {size_code!r} in {pn!r}")
    cls = SEMCO["tcc_to_class"].get(tcc_code)
    if cls is None and tcc_code not in SEMCO["tcc_to_class"]:
        raise DecodeError(f"unknown SEMCO TCC code {tcc_code!r} in {pn!r}")
    V = SEMCO["voltage"].get(volt_code)
    if V is None:
        raise DecodeError(f"unknown SEMCO voltage code {volt_code!r} in {pn!r}")

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "Samsung",
        "prefix": "CL",
        "pn": pn,
        "case": case,
        "cls": cls,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": SEMCO["tolerance"].get(tol_code),
        "plating_text": SEMCO["plating"].get(plating),
        "control_text": SEMCO["control"].get(control),
        "raw": {
            "sizeCode": size_code, "tccCode": tcc_code, "capCode": cap_code,
            "tolCode": tol_code, "voltCode": volt_code, "thickCode": thick,
            "platingCode": plating, "controlCode": control,
            "reservedCode": reserved, "packagingCode": packaging,
        },
    }


# ---------------------------------------------------------------------------
# Vendor 2: Murata GRM / GCM / GJM
# ---------------------------------------------------------------------------

# Pre-compiled regex for the fixed-width core (positions 0–13, 14 chars).
# Tail (termination/packaging/revision) is variable length and parsed loosely.
_MURATA_CORE = re.compile(r"^(?P<prefix>GRM|GCM|GJM|GRT|GA3)"
                          r"(?P<size>\d{2})"
                          r"(?P<thick>[A-Z0-9])"
                          r"(?P<tcc>[A-Z0-9]{2})"
                          r"(?P<volt>[0-9][A-Z])"
                          r"(?P<cap>[0-9R]{3})"
                          r"(?P<tol>[A-Z])"
                          r"(?P<tail>.*)$")


def parse_murata_grm(pn):
    m = _MURATA_CORE.match(pn)
    if not m:
        raise DecodeError(f"not a recognised Murata GRM/GCM/GJM part: {pn!r}")
    prefix    = m.group("prefix")
    size_code = m.group("size")
    thick     = m.group("thick")
    tcc_code  = m.group("tcc")
    volt_code = m.group("volt")
    cap_code  = m.group("cap")
    tol_code  = m.group("tol")
    tail      = m.group("tail")

    case = MURATA["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown Murata size code {size_code!r} in {pn!r}")
    cls = MURATA["tcc_to_class"].get(tcc_code)
    if cls is None:
        raise DecodeError(f"unknown Murata TCC code {tcc_code!r} in {pn!r}")
    V = MURATA["voltage"].get(volt_code)
    if V is None:
        raise DecodeError(f"unknown Murata voltage code {volt_code!r} in {pn!r}")

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "Murata",
        "prefix": prefix,
        "pn": pn,
        "case": case,
        "cls": cls,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": MURATA["tolerance"].get(tol_code),
        "raw": {
            "sizeCode": size_code, "thickCode": thick, "tccCode": tcc_code,
            "voltCode": volt_code, "capCode": cap_code, "tolCode": tol_code,
            "tail": tail,
        },
    }


# ---------------------------------------------------------------------------
# Vendor 3: TDK C-series
# ---------------------------------------------------------------------------

_TDK_CORE = re.compile(r"^(?P<prefix>CGA|C)"
                       r"(?P<size>\d{4})"
                       r"(?P<cls>[A-Z0-9]{3})"
                       r"(?P<volt>[0-9][A-Z])"
                       r"(?P<cap>[0-9R]{3})"
                       r"(?P<tol>[A-Z])"
                       r"(?P<tail>.*)$")


def parse_tdk(pn):
    m = _TDK_CORE.match(pn)
    if not m:
        raise DecodeError(f"not a recognised TDK C-series part: {pn!r}")
    prefix    = m.group("prefix")
    size_code = m.group("size")
    cls       = m.group("cls")
    volt_code = m.group("volt")
    cap_code  = m.group("cap")
    tol_code  = m.group("tol")
    tail      = m.group("tail")

    case = TDK["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown TDK size code {size_code!r} in {pn!r}")
    if cls not in TDK["class_literal"]:
        raise DecodeError(f"unknown TDK class literal {cls!r} in {pn!r}")
    V = TDK["voltage"].get(volt_code)
    if V is None:
        raise DecodeError(f"unknown TDK voltage code {volt_code!r} in {pn!r}")

    # Normalise NP0 → C0G (same Class I material)
    cls_canon = "C0G" if cls in ("NP0", "U2J") else cls

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "TDK",
        "prefix": prefix,
        "pn": pn,
        "case": case,
        "cls": cls_canon,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": TDK["tolerance"].get(tol_code),
        "raw": {
            "sizeCode": size_code, "classLiteral": cls, "voltCode": volt_code,
            "capCode": cap_code, "tolCode": tol_code, "tail": tail,
        },
    }


# ---------------------------------------------------------------------------
# Vendor 4: KEMET C-spec
# ---------------------------------------------------------------------------

_KEMET_CORE = re.compile(r"^C"
                         r"(?P<size>\d{4})"
                         r"(?P<style>[A-Z])"
                         r"(?P<cap>[0-9R]{3})"
                         r"(?P<tol>[A-Z])"
                         r"(?P<volt>[0-9][A-Z])"
                         r"(?P<dielectric>[A-Z])"
                         r"(?P<tail>.*)$")


def parse_kemet(pn):
    m = _KEMET_CORE.match(pn)
    if not m:
        raise DecodeError(f"not a recognised KEMET C-spec part: {pn!r}")
    size_code   = m.group("size")
    case_style  = m.group("style")
    cap_code    = m.group("cap")
    tol_code    = m.group("tol")
    volt_code   = m.group("volt")
    dielectric  = m.group("dielectric")
    tail        = m.group("tail")

    case = KEMET["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown KEMET size code {size_code!r} in {pn!r}")
    cls = KEMET["dielectric_to_class"].get(dielectric)
    if cls is None:
        raise DecodeError(f"unknown KEMET dielectric letter {dielectric!r} in {pn!r}")
    V = KEMET["voltage"].get(volt_code)
    if V is None:
        raise DecodeError(f"unknown KEMET voltage code {volt_code!r} in {pn!r}")

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "KEMET",
        "prefix": "C",
        "pn": pn,
        "case": case,
        "cls": cls,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": KEMET["tolerance"].get(tol_code),
        "raw": {
            "sizeCode": size_code, "caseStyle": case_style,
            "capCode": cap_code, "tolCode": tol_code,
            "voltCode": volt_code, "dielectricCode": dielectric, "tail": tail,
        },
    }


# ---------------------------------------------------------------------------
# Vendor 5: Yageo CC-series
# ---------------------------------------------------------------------------

def parse_yageo_cc(pn):
    if not pn.startswith("CC"):
        raise DecodeError(f"not a Yageo CC part: {pn!r}")
    if len(pn) != YAGEO["length"]:
        raise DecodeError(f"Yageo CC part must be {YAGEO['length']} chars, got {len(pn)}: {pn!r}")

    size_code  = pn[2:6]
    tol_code   = pn[6]
    pack_code  = pn[7]
    dielectric = pn[8:11]
    volt_code  = pn[11]
    process    = pn[12:14]
    cap_code   = pn[14:17]

    case = YAGEO["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown Yageo size code {size_code!r} in {pn!r}")
    cls = YAGEO["dielectric_to_class"].get(dielectric)
    if cls is None:
        raise DecodeError(f"unknown Yageo dielectric literal {dielectric!r} in {pn!r}")
    V = YAGEO["voltage"].get(volt_code)
    if V is None:
        raise DecodeError(f"unknown Yageo voltage code {volt_code!r} in {pn!r}")

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "Yageo",
        "prefix": "CC",
        "pn": pn,
        "case": case,
        "cls": cls,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": YAGEO["tolerance"].get(tol_code),
        "raw": {
            "sizeCode": size_code, "tolCode": tol_code, "packingCode": pack_code,
            "dielectricLiteral": dielectric, "voltCode": volt_code,
            "processCode": process, "capCode": cap_code,
        },
    }


# ---------------------------------------------------------------------------
# Vendor 6: Taiyo Yuden M-series
# ---------------------------------------------------------------------------

_TAIYO_RE = re.compile(
    r"^(?P<prefix>AMK|JMK|LMK|EMK|TMK|UMK|HMK|GMK)"
    r"(?P<size>\d{3})"
    r"(?P<term>[A-Z]?)"                   # optional termination char
    r"(?P<tcc>(?:BJ|B7|BB|CG|CH|C7|CK|F5|EB))"
    r"(?P<cap>[0-9R]{3})"
    r"(?P<tol>[A-Z])"
    r"(?P<thick>[A-Z])"
    r"(?P<tail>(?:-[A-Z0-9]+)?)$"
)


def parse_taiyo_yuden(pn):
    m = _TAIYO_RE.match(pn)
    if not m:
        raise DecodeError(f"not a recognised Taiyo Yuden M-series part: {pn!r}")
    prefix    = m.group("prefix")
    size_code = m.group("size")
    term      = m.group("term")
    tcc_code  = m.group("tcc")
    cap_code  = m.group("cap")
    tol_code  = m.group("tol")
    thick     = m.group("thick")
    tail      = m.group("tail")

    V = TAIYO["prefix_to_voltage"].get(prefix)
    if V is None:
        raise DecodeError(f"unknown Taiyo Yuden prefix {prefix!r} in {pn!r}")
    case = TAIYO["size_to_case"].get(size_code)
    if case is None:
        raise DecodeError(f"unknown Taiyo Yuden size code {size_code!r} in {pn!r}")
    cls = TAIYO["tcc_to_class"].get(tcc_code)
    if cls is None:
        raise DecodeError(f"unknown Taiyo Yuden TCC code {tcc_code!r} in {pn!r}")

    C_F = decode_cap_code(cap_code)
    return {
        "vendor": "Taiyo Yuden",
        "prefix": prefix,
        "pn": pn,
        "case": case,
        "cls": cls,
        "C_F": C_F,
        "C_uF": C_F * 1e6,
        "V": V,
        "tol_text": TAIYO["tolerance"].get(tol_code),
        "raw": {
            "voltageFromPrefix": prefix, "sizeCode": size_code,
            "terminationCode": term, "tccCode": tcc_code,
            "capCode": cap_code, "tolCode": tol_code, "thickCode": thick,
            "tail": tail,
        },
    }


# ---------------------------------------------------------------------------
# Auto-detection dispatcher
# ---------------------------------------------------------------------------

_PREFIX_DISPATCH = [
    (("GRM", "GCM", "GJM", "GRT", "GA3"), parse_murata_grm),
    (("CL", "CG", "CW"),                  parse_semco_cl),  # CG/CW are SEMCO automotive
    (("CGA",),                            parse_tdk),
]


def detect_vendor(pn):
    """Return the vendor name (string) without fully decoding. Useful for dispatch UI."""
    p = pn.upper()
    for prefixes, fn in _PREFIX_DISPATCH:
        if any(p.startswith(pr) for pr in prefixes):
            return fn.__name__.replace("parse_", "").upper()
    # Disambiguate single-letter C: TDK uses C + 4 digits; KEMET uses C + 4 digits + letter.
    if p.startswith("C") and len(p) >= 5 and p[1:5].isdigit():
        return "TDK" if len(p) >= 8 and p[5] in "XCN0Y" and p[5:8] in (
            "C0G", "X5R", "X7R", "X6S", "X7S", "X8R", "X8L", "Y5V", "NP0", "U2J"
        ) else "KEMET"
    return None


def decode(pn):
    """Auto-detect vendor and decode. Returns the canonical dict or raises DecodeError."""
    p = pn.upper()
    candidates = []
    if p.startswith(("GRM", "GCM", "GJM", "GRT", "GA3")):
        candidates.append(parse_murata_grm)
    if p.startswith(("CL", "CG", "CW")):
        candidates.append(parse_semco_cl)
    if p.startswith("CC"):
        candidates.append(parse_yageo_cc)
    if p.startswith(("AMK", "JMK", "LMK", "EMK", "TMK", "UMK", "HMK", "GMK")):
        candidates.append(parse_taiyo_yuden)
    if p.startswith("CGA") or (p.startswith("C") and len(p) >= 8 and p[5:8] in
                               ("C0G", "X5R", "X7R", "X6S", "X7S", "X8R", "X8L", "Y5V", "NP0", "U2J")):
        candidates.append(parse_tdk)
    if p.startswith("C") and parse_kemet not in candidates:
        candidates.append(parse_kemet)

    if not candidates:
        raise DecodeError(f"no vendor decoder matches prefix of {pn!r}")

    last_error = None
    for fn in candidates:
        try:
            return fn(pn)
        except DecodeError as e:
            last_error = e
    raise last_error or DecodeError(f"no decoder accepted {pn!r}")


# ---------------------------------------------------------------------------
# Helper: human-readable case label
# ---------------------------------------------------------------------------

def case_label(case_id):
    c = _CASES.get(case_id)
    if c is None:
        return case_id
    return f"EIA {c['eia']} / metric {c['metric']} ({c['L']/1000:.2g}×{c['W']/1000:.2g} mm)"
