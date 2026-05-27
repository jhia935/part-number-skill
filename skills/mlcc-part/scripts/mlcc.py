#!/usr/bin/env python3
"""MLCC part-number CLI: decode, cross, search, validate.

Usage:
    python mlcc.py decode <PN>
    python mlcc.py cross <PN>
    python mlcc.py search [--case 0805_2012] [--cls X7R] [--C-uF 1.0] [--V 50]
                           [--V-min N] [--V-max N] [--C-uF-min N] [--C-uF-max N]
                           [--mfr Murata]
    python mlcc.py validate

Add `--json` to any sub-command for machine-readable output.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decoders          # noqa: E402
import search as srch    # noqa: E402


# ============================================================
# Formatting
# ============================================================

def fmt_C(C_uF):
    if C_uF >= 1.0:    return f"{C_uF:.3g} µF"
    if C_uF >= 0.001:  return f"{C_uF*1000:.3g} nF"
    return f"{C_uF*1e6:.3g} pF"


def print_decoded(d):
    print(f"{d['vendor']} {d['pn']}")
    print()
    print(f"  case      {d['case']}  ({decoders.case_label(d['case'])})")
    print(f"  class     {d['cls']}")
    print(f"  C         {fmt_C(d['C_uF'])}  (code: {d['raw'].get('capCode', '?')})")
    print(f"  V_rated   {d['V']} V")
    if d.get("tol_text"):
        print(f"  tolerance {d['tol_text']}")
    extras = []
    if d.get("plating_text"):  extras.append(("plating",  d["plating_text"]))
    if d.get("control_text"):  extras.append(("control",  d["control_text"]))
    for k, v in extras:
        print(f"  {k:<9} {v}")


def print_parts_table(parts, title=None):
    if title:
        print(title)
    if not parts:
        print("  (no matches)")
        return
    rows = [["Vendor", "P/N", "Case", "Class", "C", "V"]]
    for p in parts:
        rows.append([p["mfr"], p["pn"], p["case"], p["cls"], fmt_C(p["C_uF"]), f"{p['V']} V"])
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    for i, row in enumerate(rows):
        line = "  " + "  ".join(c.ljust(widths[j]) for j, c in enumerate(row))
        print(line)
        if i == 0:
            print("  " + "  ".join("-" * w for w in widths))


# ============================================================
# Sub-commands
# ============================================================

def cmd_decode(args):
    try:
        d = decoders.decode(args.pn)
    except decoders.DecodeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    if args.json:
        # Drop the helper text fields when emitting JSON.
        print(json.dumps(d, indent=2, ensure_ascii=False))
    else:
        print_decoded(d)
    return 0


def cmd_cross(args):
    try:
        d = decoders.decode(args.pn)
    except decoders.DecodeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    matches = srch.cross(d, exclude_vendor=True)
    if args.json:
        print(json.dumps({
            "input": {"vendor": d["vendor"], "pn": d["pn"], "case": d["case"],
                      "cls": d["cls"], "C_uF": d["C_uF"], "V": d["V"]},
            "exact_matches": matches,
            "near_matches":  srch.cross_near(d) if not matches else [],
        }, indent=2, ensure_ascii=False))
        return 0

    print(f"{d['vendor']} {d['pn']}  →  {d['case']} {d['cls']} {fmt_C(d['C_uF'])} {d['V']} V")
    print()
    if matches:
        print_parts_table(matches, title=f"Exact matches ({len(matches)}):")
    else:
        near = srch.cross_near(d)
        if near:
            print("No exact match in database.")
            print_parts_table(near[:8], title="Nearest matches (same case + class):")
        else:
            print("No matches in database.")
            print("Suggestion: escalate to web search (Mouser / Octopart / DigiKey).")
    return 0


def cmd_search(args):
    filters = {
        "case": args.case,
        "cls":  args.cls,
        "mfr":  args.mfr,
        "V_exact":     args.V,
        "V_min":       args.V_min,
        "V_max":       args.V_max,
        "C_uF_exact":  args.C_uF,
        "C_uF_min":    args.C_uF_min,
        "C_uF_max":    args.C_uF_max,
    }
    matches = srch.search(filters)
    if args.json:
        print(json.dumps({"filters": filters, "matches": matches}, indent=2, ensure_ascii=False))
        return 0
    label = " | ".join(f"{k}={v}" for k, v in filters.items() if v is not None) or "(no filters)"
    print_parts_table(matches, title=f"Search: {label}  →  {len(matches)} match(es)")
    return 0


def cmd_validate(args):
    fails = []
    for p in srch.all_parts():
        try:
            d = decoders.decode(p["pn"])
        except decoders.DecodeError as e:
            fails.append((p["pn"], f"decode error: {e}"))
            continue
        for key in ("case", "cls", "V"):
            if d[key] != p[key]:
                fails.append((p["pn"], f"{key}: decoded {d[key]!r} vs metadata {p[key]!r}"))
        if abs(d["C_uF"] - p["C_uF"]) / max(p["C_uF"], 1e-12) > 1e-4:
            fails.append((p["pn"], f"C_uF: decoded {d['C_uF']} vs metadata {p['C_uF']}"))

    if args.json:
        print(json.dumps({"checked": len(srch.all_parts()), "failures": fails}, indent=2))
        return 1 if fails else 0

    print(f"Checked {len(srch.all_parts())} database parts.")
    if fails:
        print(f"  Failures: {len(fails)}")
        for pn, msg in fails:
            print(f"    ✗ {pn}: {msg}")
        return 1
    print("  All decode-equals-metadata. ✓")
    return 0


# ============================================================
# Entry
# ============================================================

def main():
    p = argparse.ArgumentParser(prog="mlcc", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--json", action="store_true", help="emit JSON output")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp_d = sub.add_parser("decode", help="decode a part number into structured fields")
    sp_d.add_argument("pn")

    sp_c = sub.add_parser("cross",  help="find cross-vendor equivalents for a part number")
    sp_c.add_argument("pn")

    sp_s = sub.add_parser("search", help="filter the database by specs")
    sp_s.add_argument("--case", help="canonical case ID, e.g. 0805_2012")
    sp_s.add_argument("--cls",  help="dielectric class (C0G, X5R, X7R, X8R, Y5V, ...)")
    sp_s.add_argument("--mfr",  help="manufacturer name")
    sp_s.add_argument("--V",    type=float, help="exact rated voltage")
    sp_s.add_argument("--V-min", dest="V_min", type=float)
    sp_s.add_argument("--V-max", dest="V_max", type=float)
    sp_s.add_argument("--C-uF",  dest="C_uF",  type=float, help="exact capacitance in µF")
    sp_s.add_argument("--C-uF-min", dest="C_uF_min", type=float)
    sp_s.add_argument("--C-uF-max", dest="C_uF_max", type=float)

    sub.add_parser("validate", help="cross-check every database part against its decoder")

    args = p.parse_args()
    handlers = {
        "decode":   cmd_decode,
        "cross":    cmd_cross,
        "search":   cmd_search,
        "validate": cmd_validate,
    }
    sys.exit(handlers[args.cmd](args))


if __name__ == "__main__":
    main()
