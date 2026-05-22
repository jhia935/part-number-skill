// MLCC Tier 1 capacitance estimator — pure math + lookup tables.
// Browser: loads as <script src="tier1.js"></script>, exposes window.tier1.
// Node:    require('./tier1.js') returns the same namespace.
// No DOM dependencies in this file.

(function (root) {
  'use strict';

  // ============================================================
  // Lookup tables (traced to wiki concept pages)
  // ============================================================

  // Case dimensions in µm — wiki/concepts/case-size-geometry.md
  const CASES = [
    { id: '0201_0603', label: 'EIA 0201 / metric 0603 (0.6 × 0.3 mm)', L: 600,  W: 300,  em: 125, sm: 100, Hmax: 330 },
    { id: '0402_1005', label: 'EIA 0402 / metric 1005 (1.0 × 0.5 mm)', L: 1000, W: 500,  em: 125, sm: 100, Hmax: 550 },
    { id: '0603_1608', label: 'EIA 0603 / metric 1608 (1.6 × 0.8 mm)', L: 1600, W: 810,  em: 175, sm: 100, Hmax: 900 },
    { id: '0805_2012', label: 'EIA 0805 / metric 2012 (2.0 × 1.25 mm)', L: 2010, W: 1250, em: 250, sm: 150, Hmax: 1350 },
    { id: '1206_3216', label: 'EIA 1206 / metric 3216 (3.2 × 1.6 mm)', L: 3200, W: 1600, em: 250, sm: 150, Hmax: 1800 },
    { id: '1210_3225', label: 'EIA 1210 / metric 3225 (3.2 × 2.5 mm)', L: 3200, W: 2500, em: 250, sm: 150, Hmax: 2800 },
    { id: '1812_4532', label: 'EIA 1812 / metric 4532 (4.5 × 3.2 mm)', L: 4500, W: 3200, em: 300, sm: 200, Hmax: 3500 },
    { id: '2220_5750', label: 'EIA 2220 / metric 5750 (5.7 × 5.0 mm)', L: 5700, W: 5000, em: 320, sm: 220, Hmax: 3500 },
  ];

  // ε_r,nominal — wiki/concepts/eia-rs-198-dielectric-classes.md
  const CLASSES = [
    { id: 'C0G', label: 'C0G / NP0 (Class I, ultra-stable)',   er: 30   },
    { id: 'X5R', label: 'X5R (Class II, −55…+85 °C, ±15 %)',   er: 2500 },
    { id: 'X7R', label: 'X7R (Class II, −55…+125 °C, ±15 %)',  er: 2200 },
    { id: 'X8R', label: 'X8R (Class II, −55…+150 °C, ±15 %)',  er: 1800 },
    { id: 'Y5V', label: 'Y5V (Class III, −30…+85 °C, +22/−82 %)', er: 7000 },
  ];

  // DC-bias sigmoid params: f_V = 1 / (1 + (E/E0)^p), E in V/µm
  // wiki/concepts/dc-bias-derating.md
  const DCBIAS = {
    'C0G': { E0: 1e9, p: 1 },    // effectively none
    'X5R': { E0: 3.0, p: 2 },
    'X7R': { E0: 4.0, p: 2 },
    'X8R': { E0: 5.0, p: 2 },
    'Y5V': { E0: 1.5, p: 1.5 },
  };

  const EPS0 = 8.854187817e-12; // F/m

  // Vendor reference parts — for the UI's vendor lookup table and as anchors
  // for the test suite's order-of-magnitude calibration. Mostly Murata/TDK/Samsung
  // standard part numbers. Not exhaustive; covers ~20 common case+class+V+C combos.
  const VENDOR_PARTS = [
    // 0402
    { case: '0402_1005', cls: 'X5R', V: 6.3, C_uF: 1.0,    mfr: 'TDK',     pn: 'C1005X5R0J105K' },
    { case: '0402_1005', cls: 'X7R', V: 25,  C_uF: 0.010,  mfr: 'Murata',  pn: 'GRM155R71E103KA' },
    { case: '0402_1005', cls: 'C0G', V: 50,  C_uF: 0.0001, mfr: 'Murata',  pn: 'GRM1555C1H101J' },
    // 0603
    { case: '0603_1608', cls: 'X7R', V: 50,  C_uF: 0.1,    mfr: 'Murata',  pn: 'GRM188R71H104K' },
    { case: '0603_1608', cls: 'X7R', V: 16,  C_uF: 1.0,    mfr: 'Murata',  pn: 'GRM188R71C105K' },
    { case: '0603_1608', cls: 'X5R', V: 6.3, C_uF: 10,     mfr: 'Murata',  pn: 'GRM188R60J106M' },
    { case: '0603_1608', cls: 'C0G', V: 50,  C_uF: 0.0001, mfr: 'Murata',  pn: 'GRM1885C1H101J' },
    { case: '0603_1608', cls: 'C0G', V: 50,  C_uF: 0.001,  mfr: 'Murata',  pn: 'GRM1885C1H102J' },
    // 0805
    { case: '0805_2012', cls: 'X7R', V: 50,  C_uF: 0.47,   mfr: 'Murata',  pn: 'GRM21BR71H474K' },
    { case: '0805_2012', cls: 'X7R', V: 50,  C_uF: 4.7,    mfr: 'Murata',  pn: 'GRM21BR71H475K' },
    { case: '0805_2012', cls: 'X5R', V: 25,  C_uF: 10,     mfr: 'Murata',  pn: 'GRM21BR61E106K' },
    { case: '0805_2012', cls: 'X7R', V: 50,  C_uF: 1.0,    mfr: 'Samsung', pn: 'CL21B105KAFNNNE' },
    { case: '0805_2012', cls: 'X7R', V: 100, C_uF: 1.0,    mfr: 'Murata',  pn: 'GRM21BR72A105K' },
    { case: '0805_2012', cls: 'C0G', V: 100, C_uF: 0.01,   mfr: 'Murata',  pn: 'GRM2165C2A103J' },
    { case: '0805_2012', cls: 'X8R', V: 50,  C_uF: 1.0,    mfr: 'Murata',  pn: 'GCM21BR71H105KA73' },
    // 1206
    { case: '1206_3216', cls: 'X7R', V: 50,  C_uF: 1.0,    mfr: 'Murata',  pn: 'GRM31MR71H105K' },
    { case: '1206_3216', cls: 'X7R', V: 100, C_uF: 0.22,   mfr: 'TDK',     pn: 'C3216X7R2A224K' },
    { case: '1206_3216', cls: 'X7R', V: 50,  C_uF: 10,     mfr: 'Murata',  pn: 'GRM31CR71H106K' },
    { case: '1206_3216', cls: 'X7R', V: 250, C_uF: 0.1,    mfr: 'TDK',     pn: 'C3216X7R2E104K' },
    // 1210
    { case: '1210_3225', cls: 'X5R', V: 25,  C_uF: 22,     mfr: 'Murata',  pn: 'GRM32ER61E226M' },
    { case: '1210_3225', cls: 'X7R', V: 100, C_uF: 10,     mfr: 'TDK',     pn: 'C3225X7R2A106K' },
    // 1812 / 2220 — HV / bulk
    { case: '1812_4532', cls: 'X7R', V: 50,  C_uF: 4.7,    mfr: 'TDK',     pn: 'C4532X7R1H475K' },
    { case: '2220_5750', cls: 'X7R', V: 50,  C_uF: 22,     mfr: 'Murata',  pn: 'GRM55ER71H226K' },
  ];

  // ============================================================
  // Pure functions
  // ============================================================

  // Class II TCC ranges: asymmetric span from 25 °C to each spec endpoint.
  // The function hits the ±15 % limit at exactly the spec boundary.
  const TCC_RANGES = {
    'X5R': { plus: 60,  minus: 80 },   // [-55, +85]   → ΔT_max = 60 up, 80 down
    'X7R': { plus: 100, minus: 80 },   // [-55, +125]
    'X8R': { plus: 125, minus: 80 },   // [-55, +150]
  };

  function tccFactor(cls, T) {
    const dT = T - 25;
    if (cls === 'C0G') return 1 + 30e-6 * dT;
    if (cls === 'Y5V') {
      if (dT < 0) return 1 + 0.22 * Math.max(-1, dT / 55);  // -30 °C → -22 %
      return 1 - 0.82 * Math.min(1, dT / 60);               // +85 °C → -82 %
    }
    const r = TCC_RANGES[cls];
    if (!r) return 1;
    const span = dT >= 0 ? r.plus : r.minus;
    return 1 - 0.15 * Math.min(1, Math.abs(dT) / span);
  }

  function dcBiasFactor(cls, E_V_per_um) {
    const p = DCBIAS[cls] || DCBIAS['X7R'];
    return 1 / (1 + Math.pow(E_V_per_um / p.E0, p.p));
  }

  // Main estimator. Returns derived values + warnings array.
  function compute(inp) {
    const c   = CASES.find(x => x.id === inp.case);
    const cls = CLASSES.find(x => x.id === inp.cls);
    if (!c)   throw new Error(`Unknown case id: ${inp.case}`);
    if (!cls) throw new Error(`Unknown class id: ${inp.cls}`);

    const A_overlap_um2 = (c.L - 2 * c.em) * (c.W - 2 * c.sm);
    const A_eff_um2     = A_overlap_um2 * inp.coverage * (1 - inp.disc);
    const d_fired_um    = inp.hBT * (1 - inp.sTotal);
    const hNi_fired_um  = inp.hNi * (1 - inp.sTotal);
    const H_active_um   = inp.Ne * (d_fired_um + hNi_fired_um);
    const H_stack_um    = H_active_um + 2 * inp.cover;

    const A_eff_m2    = A_eff_um2 * 1e-12;
    const d_fired_m   = d_fired_um * 1e-6;
    const C_nominal_F = cls.er * EPS0 * A_eff_m2 * inp.Ne / d_fired_m;

    const E_applied   = inp.vdc / d_fired_um;
    const f_T         = tccFactor(inp.cls, inp.top);
    const f_V         = dcBiasFactor(inp.cls, E_applied);
    const C_derated_F = inp.tier2 ? (C_nominal_F * f_T * f_V) : C_nominal_F;

    const chip_vol_mm3 = (c.L / 1000) * (c.W / 1000) * (H_stack_um / 1000);
    const vol_density  = (C_derated_F * 1e6) / chip_vol_mm3;

    const warnings = [];
    if (H_stack_um > c.Hmax) {
      warnings.push({ level: 'error', code: 'H_OVER',
        msg: `Stack H = ${(H_stack_um/1000).toFixed(2)} mm exceeds H_max ${(c.Hmax/1000).toFixed(2)} mm for ${c.label.split('(')[0].trim()}. Reduce N_e, h_BT, h_Ni, or cover.` });
    }
    if (d_fired_um < 0.3) {
      warnings.push({ level: 'warn', code: 'D_GRAIN_FLOOR',
        msg: `d_fired = ${d_fired_um.toFixed(2)} µm is below ~0.3 µm grain-size floor — reliability degrades sharply (see core-shell-batio3).` });
    }
    if (hNi_fired_um < 0.3) {
      warnings.push({ level: 'warn', code: 'NI_PARTICLE_FLOOR',
        msg: `h_Ni fired = ${hNi_fired_um.toFixed(2)} µm is near the 3-particle floor (~0.3 µm for 100 nm Ni) — electrode discontinuity will be high.` });
    }
    const ratio = inp.hNi / inp.hBT;
    if (ratio < 0.3) {
      warnings.push({ level: 'info', code: 'THIN_NI',
        msg: `h_Ni/h_BT = ${ratio.toFixed(2)} (thin-electrode regime) — weak in-plane constraint; near-isotropic shrinkage.` });
    }
    if (ratio > 2.0) {
      warnings.push({ level: 'info', code: 'THICK_NI',
        msg: `h_Ni/h_BT = ${ratio.toFixed(2)} (electrode-dominated) — metal volume fraction high; check stack stiffness assumptions.` });
    }
    if (inp.coverage > 0.95) {
      warnings.push({ level: 'warn', code: 'COVERAGE_HIGH',
        msg: `Coverage ${(inp.coverage*100).toFixed(0)} % leaves very little margin — production-risky shorting between opposing electrodes.` });
    }

    return {
      caseRec: c, clsRec: cls,
      A_overlap_um2, A_eff_um2, d_fired_um, hNi_fired_um, H_active_um, H_stack_um,
      C_nominal_F, C_derated_F, f_T, f_V, E_applied,
      chip_vol_mm3, vol_density, warnings,
    };
  }

  // ============================================================
  // Formatting helpers (used by both UI and tests)
  // ============================================================

  function fmtCap(C) {
    if (!isFinite(C) || C <= 0) return '—';
    if (C >= 1e-6)  return (C / 1e-6).toPrecision(3) + ' µF';
    if (C >= 1e-9)  return (C / 1e-9).toPrecision(3) + ' nF';
    if (C >= 1e-12) return (C / 1e-12).toPrecision(3) + ' pF';
    return C.toExponential(2) + ' F';
  }

  function fmt(x, dec, suf) {
    if (dec === undefined) dec = 2;
    if (suf === undefined) suf = '';
    return (isFinite(x) ? x.toFixed(dec) : '—') + suf;
  }

  // Default-input factory: handy for tests and the UI's reset action.
  function defaultInputs() {
    return {
      case: '0805_2012',
      cls:  'X7R',
      hBT:  2.0,
      hNi:  1.0,
      Ne:   300,
      cover: 40,
      coverage: 0.85,
      sTotal:   0.12,
      disc:     0.20,
      tier2:    true,
      vdc:      0,
      top:      25,
    };
  }

  // ============================================================
  // Export
  // ============================================================

  const api = {
    CASES, CLASSES, DCBIAS, TCC_RANGES, EPS0, VENDOR_PARTS,
    tccFactor, dcBiasFactor, compute,
    fmtCap, fmt, defaultInputs,
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
  }
  if (typeof root !== 'undefined') {
    root.tier1 = api;
  }
})(typeof window !== 'undefined' ? window : (typeof globalThis !== 'undefined' ? globalThis : this));
