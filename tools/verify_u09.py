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


def primjer_pitot_uav(dp=380.0, rho=1.115, rho_dense=1.25,
                       D_s=0.005, nu=1.5e-5):
    """Javni primjer Pitot-statičke sonde na bespilotnoj letjelici."""

    v = math.sqrt(2 * dp / rho)
    v_dense = math.sqrt(2 * dp / rho_dense)
    Re_s = v * D_s / nu
    change_percent = (v - v_dense) / v * 100
    return {
        "v": v,
        "v_dense": v_dense,
        "Re_s": Re_s,
        "change_percent": change_percent,
    }


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
    HGL_C = p_C_g + z_C
    p_v = 2.34e3
    vapor_margin = p_C_abs - p_v
    return {
        "v": v,
        "p_C_abs": p_C_abs,
        "HGL_C": HGL_C,
        "vapor_margin": vapor_margin,
    }


def zadatak_6(D=0.070, dz=2.6, z_C=1.7, h_exit=1.2, g=9.81,
               p_atm=101.3e3, rho=1000.0, K_sum=2.0, dK_sum=0.5,
               K_C=1.2, dK_C=0.3):
    v = math.sqrt(2 * g * dz)
    A = math.pi * D**2 / 4
    Q = A * v
    p_C_g = -(v**2 / (2 * g) + z_C)
    p_C_abs = p_atm + rho * g * p_C_g
    t = math.sqrt(2 * h_exit / g)
    x = v * t
    v_real = math.sqrt(2 * g * dz / (1 + K_sum))
    Q_real = A * v_real
    Q_max = A * math.sqrt(2 * g * dz / (1 + K_sum - dK_sum))
    Q_min = A * math.sqrt(2 * g * dz / (1 + K_sum + dK_sum))
    # Najmanji tlak nastaje uz najveći K_C i najmanji ukupni K_sum.
    vh_at_p_min = dz / (1 + K_sum - dK_sum)
    p_C_abs_min = p_atm - rho * g * (
        z_C + (1 + K_C + dK_C) * vh_at_p_min
    )
    return {
        "v": v,
        "Q": Q,
        "p_C_abs": p_C_abs,
        "x": x,
        "Q_real": Q_real,
        "Q_min": Q_min,
        "Q_max": Q_max,
        "p_C_abs_min": p_C_abs_min,
    }


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

    r = primjer_pitot_uav()
    _check(out, "U09.P6.v", r["v"], 26.1, "m/s", rel=0.02)
    _check(out, "U09.P6.v_dense", r["v_dense"], 24.7, "m/s", rel=0.02)
    _check(out, "U09.P6.Re_s", r["Re_s"], 8700.0, "", rel=0.02)
    _check(out, "U09.P6.change_percent", r["change_percent"], 5.4, "%", rel=0.05)

    r = zadatak_1()
    _check(out, "U09.Z1.v", r["v"], 7.92, "m/s", rel=0.02)
    _check(out, "U09.Z1.Q_Ls", r["Q"] * 1000, 4.21, "L/s", rel=0.02)
    _check(out, "U09.Z1.m_dot", r["m_dot"], 4.20, "kg/s", rel=0.02)

    r = zadatak_2()
    _check(out, "U09.Z2.dp", r["dp"], 235.0, "Pa", rel=0.02)

    r = zadatak_3()
    _check(out, "U09.Z3.v_2", r["v_2"], 7.38, "m/s", rel=0.02)
    _check(out, "U09.Z3.Q_Ls", r["Q"] * 1000, 28.4, "L/s", rel=0.02)

    r = zadatak_4()
    _check(out, "U09.Z4.v", r["v"], 4.13, "m/s", rel=0.02)

    r = zadatak_5()
    _check(out, "U09.Z5.v", r["v"], 7.41, "m/s", rel=0.02)
    _check(out, "U09.Z5.p_C_abs_kPa", r["p_C_abs"] / 1000, 62.8, "kPa", rel=0.02)
    _check(out, "U09.Z5.HGL_C", r["HGL_C"], -2.8, "m", rel=0.01)
    _check(out, "U09.Z5.vapor_margin_kPa", r["vapor_margin"] / 1000, 60.5, "kPa", rel=0.02)

    r = zadatak_6()
    _check(out, "U09.Z6.v_ideal", r["v"], 7.14, "m/s", rel=0.02)
    _check(out, "U09.Z6.Q_ideal_Ls", r["Q"] * 1000, 27.5, "L/s", rel=0.02)
    _check(out, "U09.Z6.p_C_ideal_kPa", r["p_C_abs"] / 1000, 59.2, "kPa", rel=0.02)
    _check(out, "U09.Z6.x", r["x"], 3.53, "m", rel=0.02)
    _check(out, "U09.Z6.Q_real_Ls", r["Q_real"] * 1000, 15.9, "L/s", rel=0.02)
    _check(out, "U09.Z6.Q_min_Ls", r["Q_min"] * 1000, 14.7, "L/s", rel=0.02)
    _check(out, "U09.Z6.Q_max_Ls", r["Q_max"] * 1000, 17.4, "L/s", rel=0.02)
    _check(out, "U09.Z6.p_C_min_kPa", r["p_C_abs_min"] / 1000, 59.2, "kPa", rel=0.02)

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
