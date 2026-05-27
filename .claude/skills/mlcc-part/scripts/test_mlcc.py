"""Test suite for the mlcc-part skill. Standalone — no pytest dependency.

Run:  python3 scripts/test_mlcc.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decoders   # noqa: E402
import search     # noqa: E402

passed = 0
failed = 0
failures = []


def ok(name, cond, detail=None):
    global passed, failed
    if cond:
        passed += 1
    else:
        failed += 1
        failures.append(f"  ✗ {name}" + (f" — {detail}" if detail else ""))


def near(a, b, frac=1e-9):
    if b == 0:
        return abs(a) <= frac
    return abs(a - b) / abs(b) <= frac


def expect_decode_error(name, fn):
    global passed, failed
    try:
        fn()
        failed += 1
        failures.append(f"  ✗ {name} — should have raised DecodeError")
    except decoders.DecodeError:
        passed += 1


# ============================================================
# 1. SEMCO direct decode (verified-real and wiki canonical)
# ============================================================

def t_semco_direct():
    a = decoders.parse_semco_cl("CL21B105KAFNNNE")
    ok("CL21B105KAFNNNE: case=0805_2012", a["case"] == "0805_2012")
    ok("CL21B105KAFNNNE: cls=X7R",         a["cls"]  == "X7R")
    ok("CL21B105KAFNNNE: V=25",            a["V"]    == 25)
    ok("CL21B105KAFNNNE: C=1µF",           near(a["C_uF"], 1.0, 1e-6))
    ok("CL21B105KAFNNNE: tol=±10%",        a["tol_text"] == "±10%")

    b = decoders.parse_semco_cl("CL10B104KB8NNNC")  # wiki canonical
    ok("CL10B104KB8NNNC: case=0603_1608", b["case"] == "0603_1608")
    ok("CL10B104KB8NNNC: cls=X7R",         b["cls"]  == "X7R")
    ok("CL10B104KB8NNNC: C=100nF",         near(b["C_uF"], 0.1, 1e-6))
    ok("CL10B104KB8NNNC: V=50",            b["V"]    == 50)

    c = decoders.parse_semco_cl("CL31B106KAHNNNE")
    ok("CL31B106KAHNNNE: case=1206_3216", c["case"] == "1206_3216")
    ok("CL31B106KAHNNNE: C=10µF",          near(c["C_uF"], 10.0, 1e-6))
    ok("CL31B106KAHNNNE: V=25",            c["V"]    == 25)

    d = decoders.parse_semco_cl("CL05A105KQ5NNNC")
    ok("CL05A105KQ5NNNC: case=0402_1005", d["case"] == "0402_1005")
    ok("CL05A105KQ5NNNC: cls=X5R",         d["cls"]  == "X5R")
    ok("CL05A105KQ5NNNC: V=6.3",           d["V"]    == 6.3)


# ============================================================
# 2. Murata direct decode
# ============================================================

def t_murata_direct():
    a = decoders.parse_murata_grm("GRM21BR71H475K")
    ok("GRM21BR71H475K: vendor=Murata",   a["vendor"] == "Murata")
    ok("GRM21BR71H475K: case=0805_2012", a["case"]   == "0805_2012")
    ok("GRM21BR71H475K: cls=X7R",         a["cls"]    == "X7R")
    ok("GRM21BR71H475K: V=50",            a["V"]      == 50)
    ok("GRM21BR71H475K: C=4.7µF",         near(a["C_uF"], 4.7, 1e-6))

    b = decoders.parse_murata_grm("GRM188R71H104K")
    ok("GRM188R71H104K: case=0603_1608", b["case"] == "0603_1608")
    ok("GRM188R71H104K: cls=X7R",         b["cls"]  == "X7R")
    ok("GRM188R71H104K: V=50",            b["V"]    == 50)
    ok("GRM188R71H104K: C=100nF",         near(b["C_uF"], 0.1, 1e-6))

    c = decoders.parse_murata_grm("GRM21BR61E106K")  # X5R confirmed
    ok("GRM21BR61E106K: cls=X5R (not X6S)", c["cls"] == "X5R")
    ok("GRM21BR61E106K: C=10µF",            near(c["C_uF"], 10.0, 1e-6))
    ok("GRM21BR61E106K: V=25",              c["V"]    == 25)

    d = decoders.parse_murata_grm("GRM2165C2A103J")  # C0G 10nF 100V
    ok("GRM2165C2A103J: cls=C0G",  d["cls"] == "C0G")
    ok("GRM2165C2A103J: V=100",    d["V"]   == 100)
    ok("GRM2165C2A103J: tol=±5%",  d["tol_text"] == "±5%")
    ok("GRM2165C2A103J: C=10nF",   near(d["C_uF"], 0.01, 1e-6))


# ============================================================
# 2b. Yageo CC-series direct decode
# ============================================================

def t_yageo_direct():
    a = decoders.parse_yageo_cc("CC0402MRX5R5BB106")
    ok("CC0402MRX5R5BB106: vendor=Yageo",     a["vendor"] == "Yageo")
    ok("CC0402MRX5R5BB106: case=0402_1005",   a["case"]   == "0402_1005")
    ok("CC0402MRX5R5BB106: cls=X5R",          a["cls"]    == "X5R")
    ok("CC0402MRX5R5BB106: V=6.3",            a["V"]      == 6.3)
    ok("CC0402MRX5R5BB106: C=10µF",           near(a["C_uF"], 10.0, 1e-6))
    ok("CC0402MRX5R5BB106: tol=±20%",         a["tol_text"] == "±20%")

    # X7R variant at higher voltage
    b = decoders.parse_yageo_cc("CC0402KRX7R9BB104")
    ok("CC0402KRX7R9BB104: cls=X7R",          b["cls"] == "X7R")
    ok("CC0402KRX7R9BB104: V=50",             b["V"]   == 50)
    ok("CC0402KRX7R9BB104: C=100nF",          near(b["C_uF"], 0.1, 1e-6))
    ok("CC0402KRX7R9BB104: tol=±10%",         b["tol_text"] == "±10%")


# ============================================================
# 2c. Taiyo Yuden M-series direct decode
# ============================================================

def t_taiyo_yuden_direct():
    a = decoders.parse_taiyo_yuden("JMK105CBJ106MV-F")
    ok("JMK105CBJ106MV-F: vendor=Taiyo Yuden", a["vendor"] == "Taiyo Yuden")
    ok("JMK105CBJ106MV-F: case=0402_1005",    a["case"]   == "0402_1005")
    ok("JMK105CBJ106MV-F: cls=X5R",            a["cls"]    == "X5R")
    ok("JMK105CBJ106MV-F: V=6.3 (from JMK)",   a["V"]      == 6.3)
    ok("JMK105CBJ106MV-F: C=10µF",             near(a["C_uF"], 10.0, 1e-6))
    ok("JMK105CBJ106MV-F: tol=±20%",           a["tol_text"] == "±20%")

    # No-termination variant (older format)
    b = decoders.parse_taiyo_yuden("LMK105BJ105KV-F")
    ok("LMK105BJ105KV-F: V=10 (from LMK)",     b["V"]   == 10)
    ok("LMK105BJ105KV-F: C=1µF",               near(b["C_uF"], 1.0, 1e-6))
    ok("LMK105BJ105KV-F: tol=±10%",            b["tol_text"] == "±10%")

    # 0603 size, with termination char
    c = decoders.parse_taiyo_yuden("JMK107ABJ106KA-T")
    ok("JMK107ABJ106KA-T: case=0603_1608",    c["case"] == "0603_1608")
    ok("JMK107ABJ106KA-T: V=6.3",              c["V"]    == 6.3)


# ============================================================
# 3. TDK direct decode
# ============================================================

def t_tdk_direct():
    a = decoders.parse_tdk("C2012X7R1H105K")
    ok("C2012X7R1H105K: vendor=TDK",     a["vendor"] == "TDK")
    ok("C2012X7R1H105K: case=0805_2012", a["case"]   == "0805_2012")
    ok("C2012X7R1H105K: cls=X7R",         a["cls"]    == "X7R")
    ok("C2012X7R1H105K: V=50",            a["V"]      == 50)
    ok("C2012X7R1H105K: C=1µF",           near(a["C_uF"], 1.0, 1e-6))

    b = decoders.parse_tdk("C3216X7R2A224K")
    ok("C3216X7R2A224K: case=1206_3216", b["case"] == "1206_3216")
    ok("C3216X7R2A224K: V=100",            b["V"]    == 100)
    ok("C3216X7R2A224K: C=220nF",          near(b["C_uF"], 0.22, 1e-6))

    c = decoders.parse_tdk("C4532X7R1H475K")
    ok("C4532X7R1H475K: case=1812_4532", c["case"] == "1812_4532")
    ok("C4532X7R1H475K: V=50",             c["V"]    == 50)
    ok("C4532X7R1H475K: C=4.7µF",          near(c["C_uF"], 4.7, 1e-6))

    # NP0 normalised to C0G
    d = decoders.parse_tdk("C1608NP01H102J")
    ok("TDK NP0 normalises to C0G",       d["cls"] == "C0G")


# ============================================================
# 4. Capacitance code edge cases
# ============================================================

def t_cap_code():
    ok("105 → 1 µF",   near(decoders.decode_cap_code("105"), 1e-6, 1e-9))
    ok("104 → 100 nF", near(decoders.decode_cap_code("104"), 1e-7, 1e-9))
    ok("103 → 10 nF",  near(decoders.decode_cap_code("103"), 1e-8, 1e-9))
    ok("101 → 100 pF", near(decoders.decode_cap_code("101"), 1e-10, 1e-9))
    ok("226 → 22 µF",  near(decoders.decode_cap_code("226"), 22e-6, 1e-9))
    ok("475 → 4.7 µF", near(decoders.decode_cap_code("475"), 4.7e-6, 1e-9))
    # R-form: sub-pF
    ok("1R0 → 1.0 pF", near(decoders.decode_cap_code("1R0"), 1e-12, 1e-9))
    ok("R47 → 0.47 pF", near(decoders.decode_cap_code("R47"), 0.47e-12, 1e-9))
    ok("4R7 → 4.7 pF", near(decoders.decode_cap_code("4R7"), 4.7e-12, 1e-9))


# ============================================================
# 5. Auto-detection / dispatcher
# ============================================================

def t_auto_dispatch():
    ok("decode('CL21...') → Samsung",  decoders.decode("CL21B105KAFNNNE")["vendor"] == "Samsung")
    ok("decode('GRM21...') → Murata",  decoders.decode("GRM21BR71H475K")["vendor"]   == "Murata")
    ok("decode('C2012...') → TDK",     decoders.decode("C2012X7R1H105K")["vendor"]   == "TDK")
    ok("decode('CC0402...') → Yageo",  decoders.decode("CC0402MRX5R5BB106")["vendor"] == "Yageo")
    ok("decode('JMK105...') → Taiyo Yuden",
       decoders.decode("JMK105CBJ106MV-F")["vendor"] == "Taiyo Yuden")


# ============================================================
# 6. Error handling
# ============================================================

def t_errors():
    expect_decode_error("rejects unknown prefix",
                        lambda: decoders.decode("XYZ123"))
    expect_decode_error("SEMCO rejects wrong length",
                        lambda: decoders.parse_semco_cl("CL21B105"))
    expect_decode_error("SEMCO rejects unknown size code",
                        lambda: decoders.parse_semco_cl("CL99B105KAFNNNE"))
    expect_decode_error("SEMCO rejects unknown voltage code",
                        lambda: decoders.parse_semco_cl("CL21B105K?FNNNE"))
    expect_decode_error("cap code rejects bad chars",
                        lambda: decoders.decode_cap_code("ABC"))
    expect_decode_error("cap code rejects 2 chars",
                        lambda: decoders.decode_cap_code("10"))


# ============================================================
# 7. Database cross-check (the bug-catcher)
# ============================================================

def t_database_crosscheck():
    parts = search.all_parts()
    ok(f"vendor_parts.json has ≥ 17 entries", len(parts) >= 17)
    for p in parts:
        try:
            d = decoders.decode(p["pn"])
        except decoders.DecodeError as e:
            ok(f"{p['pn']}: decodes",       False, str(e))
            continue
        ok(f"{p['pn']}: case",              d["case"] == p["case"],
           f"decoded {d['case']} vs metadata {p['case']}")
        ok(f"{p['pn']}: cls",               d["cls"] == p["cls"],
           f"decoded {d['cls']} vs metadata {p['cls']}")
        ok(f"{p['pn']}: V",                 d["V"] == p["V"],
           f"decoded {d['V']} V vs metadata {p['V']} V")
        ok(f"{p['pn']}: C_uF (≤ 5%)",       near(d["C_uF"], p["C_uF"], 0.05),
           f"decoded {d['C_uF']} µF vs metadata {p['C_uF']} µF")


# ============================================================
# 8. Search
# ============================================================

def t_search():
    # All Murata X7R 0805 at 50V should include the GRM21BR71H47*K parts.
    matches = search.search({"case": "0805_2012", "cls": "X7R", "V_exact": 50, "mfr": "Murata"})
    pns = {p["pn"] for p in matches}
    ok("search 0805 X7R 50V Murata returns GRM21BR71H474K",
       "GRM21BR71H474K" in pns)
    ok("search 0805 X7R 50V Murata returns GRM21BR71H475K",
       "GRM21BR71H475K" in pns)

    # Cross from Murata GRM21BR71H475K → no Samsung match in DB but case+class share.
    d = decoders.decode("GRM21BR71H475K")
    cross = search.cross(d, exclude_vendor=True)
    # No exact (50V 4.7µF X7R 0805) at non-Murata vendor in our DB right now → 0 matches.
    ok("cross(GRM21BR71H475K) returns no exact match in current DB",
       len(cross) == 0)
    # Near should produce something same case+class.
    near_m = search.cross_near(d)
    ok("cross_near returns at least 1 same-case + same-class part",
       len(near_m) >= 1)


# ============================================================
# 9. SKILL.md frontmatter validity (regression guard)
# ============================================================

def t_skill_md_frontmatter():
    """Catches the class of YAML breakage that hid /mlcc-part from autocomplete:
    an unquoted colon inside the description value broke yaml.safe_load even
    though Claude Code's lenient lister still surfaced the skill text.
    """
    import re
    skill_md = Path(__file__).resolve().parent.parent / "SKILL.md"
    text = skill_md.read_text()
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    ok("SKILL.md has frontmatter delimiters", m is not None)
    if m is None:
        return
    try:
        import yaml
        parsed = yaml.safe_load(m.group(1))
    except Exception as e:
        ok("SKILL.md frontmatter is valid YAML", False, str(e))
        return
    ok("SKILL.md frontmatter parses to dict", isinstance(parsed, dict))
    ok("SKILL.md has a description",            "description" in parsed)
    if "name" in parsed:
        ok("name ≤ 64 chars",                   len(parsed["name"]) <= 64)
        ok("name is lowercase / hyphens only",
           bool(re.fullmatch(r"[a-z0-9-]+", parsed["name"])))
    if "description" in parsed:
        ok("description ≤ 1024 chars",          len(parsed["description"]) <= 1024)


# ============================================================
# Run
# ============================================================

if __name__ == "__main__":
    for fn in (t_semco_direct, t_murata_direct, t_yageo_direct, t_taiyo_yuden_direct,
               t_tdk_direct, t_cap_code,
               t_auto_dispatch, t_errors, t_database_crosscheck, t_search,
               t_skill_md_frontmatter):
        fn()

    print(f"\n{passed + failed} test cases.")
    print(f"  passed: {passed}")
    print(f"  failed: {failed}")
    if failed:
        print("\nFailures:")
        for line in failures:
            print(line)
        sys.exit(1)
    print("\nAll green.")
