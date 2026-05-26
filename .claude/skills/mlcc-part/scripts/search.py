"""Database operations: load the vendor parts file, filter by spec, find cross-vendor matches."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _load():
    with open(DATA_DIR / "vendor_parts.json", "r", encoding="utf-8") as f:
        return json.load(f)["parts"]


_PARTS = _load()


def all_parts():
    return list(_PARTS)


def _matches(p, filters):
    """True if part p satisfies every key in filters (None means 'any')."""
    if filters.get("case") and p["case"] != filters["case"]:
        return False
    if filters.get("cls") and p["cls"] != filters["cls"]:
        return False
    if filters.get("mfr") and p["mfr"].lower() != filters["mfr"].lower():
        return False
    if filters.get("V_min") is not None and p["V"] < filters["V_min"]:
        return False
    if filters.get("V_max") is not None and p["V"] > filters["V_max"]:
        return False
    if filters.get("V_exact") is not None and p["V"] != filters["V_exact"]:
        return False
    C_uF = p["C_uF"]
    if filters.get("C_uF_exact") is not None:
        # 5% tolerance to allow for FP / E-series spread.
        target = filters["C_uF_exact"]
        if abs(C_uF - target) / target > 0.05:
            return False
    if filters.get("C_uF_min") is not None and C_uF < filters["C_uF_min"]:
        return False
    if filters.get("C_uF_max") is not None and C_uF > filters["C_uF_max"]:
        return False
    return True


def search(filters):
    """Return all database parts matching the given filters."""
    return [p for p in _PARTS if _matches(p, filters)]


def cross(decoded, exclude_vendor=True):
    """Given a decoded part dict, find equivalent parts at other vendors.

    Matches on (case, cls, V exact, C_uF within 5%). Optionally excludes the
    decoded part's own vendor from the result.
    """
    filters = {
        "case": decoded["case"],
        "cls": decoded["cls"],
        "V_exact": decoded["V"],
        "C_uF_exact": decoded["C_uF"],
    }
    matches = search(filters)
    if exclude_vendor:
        matches = [p for p in matches if p["mfr"].lower() != decoded["vendor"].lower()
                   and p["pn"].upper() != decoded["pn"].upper()]
    return matches


def cross_near(decoded, exclude_vendor=True):
    """Looser fallback when `cross()` returns nothing: same case + class, any V or C."""
    filters = {"case": decoded["case"], "cls": decoded["cls"]}
    matches = search(filters)
    if exclude_vendor:
        matches = [p for p in matches if p["mfr"].lower() != decoded["vendor"].lower()
                   and p["pn"].upper() != decoded["pn"].upper()]
    # Sort by spec proximity: smaller penalty = closer.
    def penalty(p):
        v_dist = abs(p["V"] - decoded["V"]) / max(decoded["V"], 1)
        c_dist = abs(p["C_uF"] - decoded["C_uF"]) / max(decoded["C_uF"], 1e-12)
        return v_dist + c_dist
    return sorted(matches, key=penalty)


def reload():
    """Reload vendor_parts.json — useful in tests after the file mutates."""
    global _PARTS
    _PARTS = _load()
    return _PARTS
