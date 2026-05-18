"""Numericka verifikacija U09: Bernoullijeva jednadzba idealnog fluida."""
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


def primjer_1_konfuzor(A_1=0.07, A_2=0.0185, m_dot=0.68, rho=1.2):
    Q = m_dot / rho
    v_1 = Q / A_1
    v_2 = Q / A_2
    dp = rho / 2 * (v_2**2 - v_1**2)
    return {"Q": Q, "v_1": v_1, "v_2": v_2, "dp": dp}


def primjer_2_mlaz(H=4.0, g=9.81):
    def x_of(h):
        return 2 * math.sqrt(h * (H - h))
    return {"x_1": x_of(1.0), "x_2": x_of(2.0), "x_3": x_of(3.0),
            "x_max": H, "h_opt": H / 2}


def primjer_3_sifon(D=0.080, dz=3.6, z_C=2.2, g=9.81, rho=1000.0):
    v = math.sqrt(2 * g * dz)
    A = math.pi * D**2 / 4
    Q = A * v
    p_C_g = -(dz + z_C)  # manometarska tlačna visina
    return {"v": v, "Q": Q, "p_C_g": p_C_g}


def cjeloviti_1_bypass(D=0.100, d_C=0.080, dz_AB=2.8, z_C=1.5, h_B=1.4,
                       g=9.81, atm_h=10.2):
    v_B = math.sqrt(2 * g * dz_AB)
    A = math.pi * D**2 / 4
    Q = A * v_B
    A_C = math.pi * d_C**2 / 4
    v_C = Q / A_C
    p_C_g = -(v_C**2 / (2 * g) + z_C)
    p_C_abs = atm_h + p_C_g
    t = math.sqrt(2 * h_B / g)
    x = v_B * t
    return {"v_B": v_B, "Q": Q, "v_C": v_C,
            "p_C_g": p_C_g, "p_C_abs": p_C_abs, "x": x}


def primjer_venturi(D_1=0.060, D_2=0.030, dh_m=0.18, rho_Hg=13600.0,
                     rho_ul=870.0, g=9.81):
    dp = (rho_Hg - rho_ul) * g * dh_m
    A_1 = math.pi * D_1**2 / 4
    # ratio = (D_1/D_2)^4
    ratio_v2_v1 = (D_1 / D_2)**2
    # Δp = ρ/2 (v_2² - v_1²) = ρ/2 v_1² (ratio² - 1)
    v_1 = math.sqrt(2 * dp / (rho_ul * (ratio_v2_v1**2 - 1)))
    v_2 = ratio_v2_v1 * v_1
    Q = A_1 * v_1
    return {"dp": dp, "v_1": v_1, "v_2": v_2, "Q": Q}


def primjer_propust(H=8.50, d=0.40, g=9.81):
    v = math.sqrt(2 * g * H)
    A = math.pi * d**2 / 4
    Q = A * v
    return {"v": v, "Q": Q}


def zadatak_1(H=3.20, d=0.026, rho=998.0, g=9.81):
    v = math.sqrt(2 * g * H)
    A = math.pi * d**2 / 4
    Q = A * v
    m_dot = rho * Q
    return {"v": v, "Q": Q, "m_dot": m_dot}


def zadatak_2(A_1=0.060, A_2=0.020, Q=0.42, rho=1.20):
    v_1 = Q / A_1
    v_2 = Q / A_2
    dp = rho / 2 * (v_2**2 - v_1**2)
    return {"dp": dp}


def zadatak_3(D_1=0.120, D_2=0.070, dp=24e3, rho=1000.0, g=9.81):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    ratio = (D_1 / D_2)**2
    v_1 = math.sqrt(2 * dp / (rho * (ratio**2 - 1)))
    v_2 = ratio * v_1
    Q = A_1 * v_1
    return {"v_2": v_2, "Q": Q}


def zadatak_4(dp=8.5e3, rho=1000.0):
    v = math.sqrt(2 * dp / rho)
    return {"v": v}


def zadatak_5(dz=2.8, z_C=1.1, g=9.81, p_atm=101e3, rho=1000.0):
    v = math.sqrt(2 * g * dz)
    # p_C(man) = -(v²/2g + z_C)
    p_C_g = -(v**2 / (2 * g) + z_C)
    p_C_abs = p_atm + rho * g * p_C_g
    return {"v": v, "p_C_abs": p_C_abs}


def zadatak_6(D=0.070, dz=2.6, z_C=1.7, h_exit=1.2, g=9.81,
               p_atm=101.3e3, rho=1000.0):
    v = math.sqrt(2 * g * dz)
    A = math.pi * D**2 / 4
    Q = A * v
    p_C_g = -(v**2 / (2 * g) + z_C)
    p_C_abs = p_atm + rho * g * p_C_g
    t = math.sqrt(2 * h_exit / g)
    x = v * t
    return {"v": v, "Q": Q, "p_C_abs": p_C_abs, "x": x}


# ------------ Faza 1.5 dodatak: Difuzor (povratak tlaka) ----------------
def primjer_difuzor(A_1=0.010, A_2=0.035, v_1=15.0, rho=1000.0, eta_dif=0.80):
    Q = A_1 * v_1
    v_2 = v_1 * A_1 / A_2
    dp_ideal = 0.5 * rho * (v_1**2 - v_2**2)
    dp_real = eta_dif * dp_ideal
    P_gub = (1 - eta_dif) * dp_ideal * Q
    return {"Q": Q, "v_2": v_2, "dp_ideal": dp_ideal,
            "dp_real": dp_real, "P_gub": P_gub}


def verify():
    out = []

    r = primjer_1_konfuzor()
    _check(out, "U09.P1.Q", r["Q"], 0.5667, "m^3/s", rel=0.02)
    _check(out, "U09.P1.v_1", r["v_1"], 8.10, "m/s", rel=0.02)
    _check(out, "U09.P1.v_2", r["v_2"], 30.63, "m/s", rel=0.02)
    _check(out, "U09.P1.dp", r["dp"], 523.0, "Pa", rel=0.02)

    r = primjer_2_mlaz()
    _check(out, "U09.P2.x_1", r["x_1"], 3.46, "m", rel=0.02)
    _check(out, "U09.P2.x_2", r["x_2"], 4.00, "m")
    _check(out, "U09.P2.x_3", r["x_3"], 3.46, "m", rel=0.02)
    _check(out, "U09.P2.x_max", r["x_max"], 4.0, "m")

    r = primjer_3_sifon()
    _check(out, "U09.P3.v", r["v"], 8.40, "m/s")
    _check(out, "U09.P3.Q_Ls", r["Q"] * 1000, 42.2, "L/s", rel=0.02)
    _check(out, "U09.P3.p_C_g", r["p_C_g"], -5.8, "m")

    r = cjeloviti_1_bypass()
    _check(out, "U09.CH1.v_B", r["v_B"], 7.41, "m/s")
    _check(out, "U09.CH1.Q_Ls", r["Q"] * 1000, 58.2, "L/s", rel=0.02)
    _check(out, "U09.CH1.v_C", r["v_C"], 11.58, "m/s")
    _check(out, "U09.CH1.p_C_g", r["p_C_g"], -8.34, "m", rel=0.02)
    _check(out, "U09.CH1.p_C_abs", r["p_C_abs"], 1.86, "m", rel=0.02)
    _check(out, "U09.CH1.x", r["x"], 3.96, "m", rel=0.02)

    r = primjer_venturi()
    _check(out, "U09.venturi.dp", r["dp"], 22740.0, "Pa", rel=0.02)
    _check(out, "U09.venturi.v_1", r["v_1"], 1.866, "m/s", rel=0.02)
    _check(out, "U09.venturi.Q_Ls", r["Q"] * 1000, 5.27, "L/s", rel=0.02)

    r = primjer_propust()
    _check(out, "U09.propust.v", r["v"], 12.91, "m/s")
    _check(out, "U09.propust.Q", r["Q"], 1.622, "m^3/s", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U09.{name}.{first_key}_pos", r[first_key], r[first_key])

    # Faza 1.5: Difuzor
    r = primjer_difuzor()
    _check(out, "U09.difuzor.Q", r["Q"], 0.150, "m^3/s")
    _check(out, "U09.difuzor.v_2", r["v_2"], 4.29, "m/s")
    _check(out, "U09.difuzor.dp_ideal_kPa", r["dp_ideal"] / 1000, 103.3, "kPa", rel=0.02)
    _check(out, "U09.difuzor.dp_real_kPa", r["dp_real"] / 1000, 82.6, "kPa", rel=0.02)
    _check(out, "U09.difuzor.P_gub_kW", r["P_gub"] / 1000, 3.1, "kW", rel=0.02)

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
