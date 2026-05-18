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
    return {"dh": dh, "h_pred": h_pred, "h_str": h_str}


def primjer_6_vatrogasna(L=2.40, h_0=1.20, H=1.60, a=4.5, g=9.81):
    dh = a * L / g
    h_pred = h_0 + dh / 2
    h_str = h_0 - dh / 2
    theta_deg = math.degrees(math.atan(a / g))
    return {"dh": dh, "h_pred": h_pred, "h_str": h_str, "theta_deg": theta_deg}


def zadatak_1(L=1.80, h_0=0.34, a=1.20, H=0.46, g=9.81):
    dh = a * L / g
    return {"dh": dh, "h_str": h_0 + dh / 2, "h_pred": h_0 - dh / 2}


def zadatak_2(L=1.40, h_0=0.30, H=0.42, g=9.81):
    dh_max = 2 * (H - h_0)
    a_max = g * dh_max / L
    return {"a_max": a_max}


def zadatak_3(rho=870.0, h=0.75, a_z=2.3, g=9.81):
    dp = rho * (g + a_z) * h
    return {"dp": dp}


def zadatak_4(b=0.75, L=1.60, h_0=0.36, F=820.0, rho=1000.0, g=9.81):
    h_str = math.sqrt(2 * F / (rho * g * b))
    dh = 2 * (h_str - h_0)
    a = g * dh / L
    return {"h_str": h_str, "a": a}


def zadatak_5(R=0.28, h_0=0.22, omega=5.5, g=9.81):
    dh = omega**2 * R**2 / (2 * g)
    return {"dh": dh, "h_rub": h_0 + dh / 2, "h_osa": h_0 - dh / 2}


def zadatak_6(R=0.32, H=0.62, h_0=0.46, rho=1000.0, g=9.81):
    omega_max = math.sqrt(4 * g * (H - h_0) / R**2)
    omega = 0.80 * omega_max
    dh = omega**2 * R**2 / (2 * g)
    return {"omega_max": omega_max, "dh": dh,
            "h_osa": h_0 - dh / 2, "h_rub": h_0 + dh / 2}


def verify():
    out = []

    r = primjer_1_kolica()
    _check(out, "U04.P1.dh", r["dh"], 0.220, "m")
    _check(out, "U04.P1.h_str", r["h_str"], 0.530, "m")
    _check(out, "U04.P1.h_pred", r["h_pred"], 0.310, "m")
    _check(out, "U04.P1.theta_deg", r["theta_deg"], 7.9, "deg", rel=0.02)

    r = primjer_2_kada()
    _check(out, "U04.P2.h_pred", r["h_pred"], 0.36, "m")
    _check(out, "U04.P2.a_max", r["a_max"], 1.962, "m/s^2")
    _check(out, "U04.P2.F_R", r["F_R"], 2343.0, "N", rel=0.02)

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

    r = primjer_6_vatrogasna()
    _check(out, "U04.P6.dh", r["dh"], 1.101, "m")
    _check(out, "U04.P6.h_pred", r["h_pred"], 1.751, "m")
    _check(out, "U04.P6.h_str", r["h_str"], 0.650, "m")
    _check(out, "U04.P6.theta_deg", r["theta_deg"], 24.7, "deg", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U04.{name}.{first_key}_pos", r[first_key], r[first_key])

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
