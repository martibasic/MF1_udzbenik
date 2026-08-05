"""Numericka verifikacija U04: Relativno mirovanje fluida."""
from __future__ import annotations

import math

TOL = 0.01


def _close(value, target, rel=TOL):
    if target == 0:
        return abs(value) < rel
    return abs(value - target) / abs(target) <= rel


def _check(out, rid, value, target, unit="", rel=TOL):
    ok = _close(value, target, rel)
    out.append({
        "id": rid,
        "status": "OK" if ok else "FAIL",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


def _invariant(out, rid, condition, details):
    out.append({
        "id": rid,
        "status": "OK" if condition else "FAIL",
        "verification": "invariant",
        "details": "" if condition else details,
    })


def primjer_1_kolica(L=1.60, h_0=0.42, a=1.35, g=9.81):
    dh = a * L / g
    h_str = h_0 + dh / 2
    h_pred = h_0 - dh / 2
    theta_deg = math.degrees(math.atan(a / g))
    return {"dh": dh, "h_str": h_str, "h_pred": h_pred, "theta_deg": theta_deg}


def primjer_2_kada(L=1.80, H=0.72, h_0=0.54, B=0.95, rho=970.0, g=9.81):
    h_str = H
    h_pred = 2 * h_0 - h_str
    dh = h_str - h_pred
    a_max = g * dh / L
    F_R = 0.5 * rho * g * B * h_str**2
    return {"h_pred": h_pred, "dh": dh, "a_max": a_max, "F_R": F_R}


def primjer_3_modul(a=3.4, g=9.81, H=0.55, p_M0=16e3, rho=960.0):
    theta = math.atan(a / g)
    theta_deg = math.degrees(theta)
    alpha_deg = 90 - theta_deg
    alpha = math.radians(alpha_deg)
    s = H / math.sin(alpha)
    g_eff = math.sqrt(g**2 + a**2)
    A_AB = s
    F_0 = p_M0 * A_AB
    F_h = 0.5 * rho * g_eff * s**2
    F_R = F_0 + F_h
    y_R = (F_0 * (s / 2) + F_h * (2 * s / 3)) / F_R
    return {
        "theta_deg": theta_deg, "alpha_deg": alpha_deg, "s": s, "g_eff": g_eff,
        "F_0": F_0, "F_h": F_h, "F_R": F_R, "y_R": y_R,
    }


def primjer_4_rotacija(R=0.35, h_0=0.28, omega=6.0, g=9.81):
    dh = omega**2 * R**2 / (2 * g)
    h_rub = h_0 + dh / 2
    h_osa = h_0 - dh / 2
    return {"dh": dh, "h_rub": h_rub, "h_osa": h_osa}


def cjeloviti_1_rotacija(R=0.40, H=0.78, h_0=0.60, omega=5.20,
                          rho=1000.0, g=9.81):
    dh = omega**2 * R**2 / (2 * g)
    h_C = h_0 - dh / 2
    h_R = h_0 + dh / 2
    p_M_C = rho * g * h_C
    p_M_D = rho * g * h_R
    omega_max = math.sqrt(4 * g * (H - h_0) / R**2)
    n_max = 60 * omega_max / (2 * math.pi)
    return {
        "dh": dh, "h_C": h_C, "h_R": h_R,
        "p_M_C": p_M_C, "p_M_D": p_M_D,
        "omega_max": omega_max, "n_max": n_max,
    }


def primjer_5_autocisterna(L=1.20, h_0=0.45, H=0.80, a=3.8, rho=750.0, g=9.81):
    dh = a * L / g
    h_pred = h_0 + dh / 2
    h_str = h_0 - dh / 2
    a_overflow = 2 * g * (H - h_0) / L
    a_dry = 2 * g * h_0 / L
    return {
        "dh": dh,
        "h_pred": h_pred,
        "h_str": h_str,
        "a_overflow": a_overflow,
        "a_dry": a_dry,
    }


def primjer_centrifuga(n=4000.0, r_d=0.095, r_v=0.025,
                        rho=1060.0, g=9.81):
    omega = 2 * math.pi * n / 60
    a_cf = omega**2 * r_d
    dp = 0.5 * rho * omega**2 * (r_d**2 - r_v**2)
    return {"omega": omega, "a_cf": a_cf, "a_cf_g": a_cf / g, "dp": dp}


def primjer_6_vatrogasna(L=2.40, h_0=1.20, H=1.60, a=4.5, g=9.81):
    dh = a * L / g
    h_pred = h_0 + dh / 2
    h_str = h_0 - dh / 2
    theta_deg = math.degrees(math.atan(a / g))
    return {"dh": dh, "h_pred": h_pred, "h_str": h_str, "theta_deg": theta_deg}


def zadatak_1(L=1.80, h_0=0.34, a=1.20, H=0.46, g=9.81):
    dh = a * L / g
    h_str = h_0 + dh / 2
    h_pred = h_0 - dh / 2
    return {"dh": dh, "h_str": h_str, "h_pred": h_pred,
            "overflow": h_str >= H}


def zadatak_2(L=1.40, h_0=0.30, H=0.42, g=9.81):
    dh_max = 2 * (H - h_0)
    a_max = g * dh_max / L
    return {"a_max": a_max}


def zadatak_3(rho=870.0, h=0.75, a_z=2.3, g=9.81):
    dp = rho * (g + a_z) * h
    dp_0 = rho * g * h
    increase_percent = 100 * (dp / dp_0 - 1)
    return {"dp": dp, "dp_0": dp_0,
            "increase_percent": increase_percent}


def zadatak_4(b=0.75, L=1.60, h_0=0.36, F=820.0, rho=1000.0, g=9.81):
    h_str = math.sqrt(2 * F / (rho * g * b))
    dh = 2 * (h_str - h_0)
    a = g * dh / L
    return {"h_str": h_str, "a": a}


def zadatak_5(R=0.28, h_0=0.22, omega=5.5, g=9.81):
    dh = omega**2 * R**2 / (2 * g)
    h_rub = h_0 + dh / 2
    h_osa = h_0 - dh / 2
    return {"dh": dh, "h_rub": h_rub, "h_osa": h_osa,
            "axis_covered": h_osa > 0.0}


def zadatak_6(R=0.32, H=0.62, h_0=0.46, rho=1000.0, g=9.81,
              alpha=0.80, overspeed=0.05, h_axis_min=0.350):
    omega_max = math.sqrt(4 * g * (H - h_0) / R**2)
    omega = alpha * omega_max
    dh = omega**2 * R**2 / (2 * g)
    h_osa = h_0 - dh / 2
    h_rub = h_0 + dh / 2
    actual_ratio = alpha * (1 + overspeed)
    h_axis_worst = h_0 - actual_ratio**2 * (H - h_0)
    h_rim_worst = h_0 + actual_ratio**2 * (H - h_0)
    alpha_max = math.sqrt((h_0 - h_axis_min) / (H - h_0)) / (1 + overspeed)
    return {"omega_max": omega_max, "dh": dh,
            "h_osa": h_osa, "h_rub": h_rub,
            "p_M_osa": rho * g * h_osa,
            "p_M_rub": rho * g * h_rub,
            "actual_ratio": actual_ratio,
            "h_axis_worst": h_axis_worst,
            "h_rim_worst": h_rim_worst,
            "alpha_max": alpha_max}


def verify():
    out = []

    r = primjer_1_kolica()
    _check(out, "U04.P1.dh", r["dh"], 0.220, "m")
    _check(out, "U04.P1.h_str", r["h_str"], 0.530, "m")
    _check(out, "U04.P1.h_pred", r["h_pred"], 0.310, "m")
    _check(out, "U04.P1.theta_deg", r["theta_deg"], 7.9, "deg", rel=0.02)

    r = primjer_3_modul()
    _check(out, "U04.P3.theta_deg", r["theta_deg"], 19.1, "deg", rel=0.02)
    _check(out, "U04.P3.alpha_deg", r["alpha_deg"], 70.9, "deg", rel=0.02)
    _check(out, "U04.P3.s", r["s"], 0.582, "m")
    _check(out, "U04.P3.g_eff", r["g_eff"], 10.38, "m/s^2")
    _check(out, "U04.P3.F_0", r["F_0"], 9312.0, "N")
    _check(out, "U04.P3.F_h", r["F_h"], 1688.0, "N", rel=0.02)
    _check(out, "U04.P3.F_R", r["F_R"], 11000.0, "N", rel=0.02)
    _check(out, "U04.P3.y_R", r["y_R"], 0.306, "m", rel=0.02)

    r = primjer_4_rotacija()
    _check(out, "U04.P4.dh", r["dh"], 0.225, "m")
    _check(out, "U04.P4.h_rub", r["h_rub"], 0.393, "m")
    _check(out, "U04.P4.h_osa", r["h_osa"], 0.168, "m")

    r = cjeloviti_1_rotacija()
    _check(out, "U04.CH1.dh", r["dh"], 0.2205, "m")
    _check(out, "U04.CH1.h_C", r["h_C"], 0.4897, "m")
    _check(out, "U04.CH1.h_R", r["h_R"], 0.7103, "m")
    _check(out, "U04.CH1.p_M_C", r["p_M_C"], 4804.0, "Pa")
    _check(out, "U04.CH1.p_M_D", r["p_M_D"], 6968.0, "Pa")
    _check(out, "U04.CH1.omega_max", r["omega_max"], 6.64, "rad/s")
    _check(out, "U04.CH1.n_max", r["n_max"], 63.4, "okr/min")

    r = primjer_5_autocisterna()
    _check(out, "U04.P5.dh", r["dh"], 0.465, "m")
    _check(out, "U04.P5.h_pred", r["h_pred"], 0.683, "m")
    _check(out, "U04.P5.h_str", r["h_str"], 0.217, "m")
    _check(out, "U04.P5.a_overflow", r["a_overflow"], 5.72, "m/s2", rel=0.02)
    _check(out, "U04.P5.a_dry", r["a_dry"], 7.36, "m/s2", rel=0.02)

    r = primjer_centrifuga()
    _check(out, "U04.P6.omega", r["omega"], 418.9, "rad/s", rel=0.02)
    _check(out, "U04.P6.a_cf", r["a_cf"], 1.666e4, "m/s2", rel=0.02)
    _check(out, "U04.P6.a_cf_g", r["a_cf_g"], 1.699e3, "g", rel=0.02)
    _check(out, "U04.P6.dp_kPa", r["dp"] / 1000, 781.0, "kPa", rel=0.02)

    z1 = zadatak_1()
    _check(out, "U04.Z1.dh", z1["dh"], 0.22, "m")
    _check(out, "U04.Z1.h_str", z1["h_str"], 0.45, "m")
    _check(out, "U04.Z1.h_pred", z1["h_pred"], 0.23, "m")

    z2 = zadatak_2()
    _check(out, "U04.Z2.a_max", z2["a_max"], 1.68, "m/s^2")

    z3 = zadatak_3()
    _check(out, "U04.Z3.dp_kPa", z3["dp"] / 1000, 7.90, "kPa")
    _check(out, "U04.Z3.dp_0_kPa", z3["dp_0"] / 1000, 6.40, "kPa")
    _check(out, "U04.Z3.increase_percent", z3["increase_percent"], 23.0, "%", rel=0.03)

    z4 = zadatak_4()
    _check(out, "U04.Z4.h_str", z4["h_str"], 0.47, "m")
    _check(out, "U04.Z4.a", z4["a"], 1.38, "m/s^2")

    z5 = zadatak_5()
    _check(out, "U04.Z5.dh", z5["dh"], 0.12, "m")
    _check(out, "U04.Z5.h_rub", z5["h_rub"], 0.28, "m")
    _check(out, "U04.Z5.h_osa", z5["h_osa"], 0.16, "m")

    z6 = zadatak_6()
    _check(out, "U04.Z6.omega_max", z6["omega_max"], 7.83, "rad/s")
    _check(out, "U04.Z6.h_osa", z6["h_osa"], 0.36, "m")
    _check(out, "U04.Z6.h_rub", z6["h_rub"], 0.56, "m")
    _check(out, "U04.Z6.p_M_osa_kPa", z6["p_M_osa"] / 1000, 3.51, "kPa")
    _check(out, "U04.Z6.p_M_rub_kPa", z6["p_M_rub"] / 1000, 5.52, "kPa")
    _check(out, "U04.Z6.actual_ratio", z6["actual_ratio"], 0.84, "")
    _check(out, "U04.Z6.h_axis_worst", z6["h_axis_worst"], 0.347, "m", rel=0.02)
    _check(out, "U04.Z6.h_rim_worst", z6["h_rim_worst"], 0.573, "m", rel=0.02)
    _check(out, "U04.Z6.alpha_max", z6["alpha_max"], 0.790, "", rel=0.02)
    _invariant(
        out,
        "U04.Z6.coverage_not_met_at_alpha_080",
        z6["h_rim_worst"] < 0.62 and z6["h_axis_worst"] < 0.350,
        "Nepovoljna tolerancija mora zadrzati volumen, ali prekrsiti dubinu usisa.",
    )

    _invariant(
        out,
        "U04.INV.translational_volume_balance",
        abs((z1["h_str"] + z1["h_pred"]) / 2 - 0.34) < 1e-14,
        "Srednja dubina ubrzanog spremnika nije sacuvana.",
    )
    _invariant(
        out,
        "U04.INV.no_overflow_and_axis_covered",
        not z1["overflow"] and z5["axis_covered"],
        "Objavljeni granicni zakljucak o preljevu/pokrivenosti osi nije ispunjen.",
    )
    _invariant(
        out,
        "U04.INV.effective_gravity_sign",
        z3["dp"] > z3["dp_0"] > 0.0,
        "Ubrzanje prema gore nije povecalo tlakovnu razliku.",
    )
    _invariant(
        out,
        "U04.INV.rotational_volume_and_limit",
        abs((z6["h_osa"] + z6["h_rub"]) / 2 - 0.46) < 1e-14
        and z6["h_rub"] < 0.62,
        "Radni rotacijski rezim ne cuva volumen ili prelijeva.",
    )

    return out


if __name__ == "__main__":
    results = verify()
    ok = sum(1 for r in results if r["status"] == "OK")
    fail = sum(1 for r in results if r["status"] != "OK")
    for r in results:
        marker = "v" if r["status"] == "OK" else "x"
        print(f"  [{marker}] {r['id']:30s}  {r.get('details', '')}")
    print()
    print(f"Total: ok={ok}, fail={fail}")
