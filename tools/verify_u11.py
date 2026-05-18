"""Numericka verifikacija U11: Kolicina gibanja i sile strujanja."""
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
        "id": rid, "status": "OK" if ok else "FAIL",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


def primjer_1_mlaz(m_dot=10.0, v=20.0):
    F = m_dot * v
    return {"F": F}


def primjer_2_mlaznica(D=0.220, d=0.090, F_P=215.0, rho=998.0):
    A_1 = math.pi * D**2 / 4
    A_2 = math.pi * d**2 / 4
    v_2 = math.sqrt(F_P / (rho * A_2))
    Q = A_2 * v_2
    v_1 = Q / A_1
    p_M1 = rho / 2 * (v_2**2 - v_1**2)
    m_dot = rho * Q
    R = p_M1 * A_1 - m_dot * (v_2 - v_1)
    return {"v_2": v_2, "Q": Q, "v_1": v_1, "p_M1": p_M1, "R": R}


def primjer_3_koljeno(D_1=0.180, D_2=0.120, Q=0.045, p_M1=52e3, p_M2=18e3,
                       rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = Q / A_1
    v_2 = Q / A_2
    m_dot = rho * Q
    F_st_x = m_dot * (0 - v_1) - p_M1 * A_1
    F_st_y = m_dot * v_2 - (-p_M2 * A_2)
    F_f_x = -F_st_x
    F_f_y = -F_st_y
    F_R = math.sqrt(F_f_x**2 + F_f_y**2)
    return {"v_1": v_1, "v_2": v_2, "F_f_x": F_f_x, "F_f_y": F_f_y, "F_R": F_R}


def cjeloviti_1_T_racva(D_1=0.180, D_2=0.090, D_3=0.080, p_M1=40e3, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    # v = ratio · v_1; Bernoulli → v² - v_1² = 2 p_M1/ρ
    ratio = A_1 / (A_2 + A_3)
    v_1 = math.sqrt(2 * p_M1 / rho / (ratio**2 - 1))
    v = ratio * v_1
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v
    Q_3 = A_3 * v
    m_dot_1 = rho * Q_1
    m_dot_2 = rho * Q_2
    m_dot_3 = rho * Q_3
    F_st_x = m_dot_2 * v - m_dot_1 * v_1 - p_M1 * A_1
    F_st_y = m_dot_3 * v
    F_f_x = -F_st_x
    F_f_y = -F_st_y
    F_R = math.sqrt(F_f_x**2 + F_f_y**2)
    return {"v_1": v_1, "v": v, "Q_1": Q_1, "Q_2": Q_2, "Q_3": Q_3,
            "F_f_x": F_f_x, "F_f_y": F_f_y, "F_R": F_R}


def cjeloviti_2_Y_racva(D_1=0.170, D_2=0.100, D_3=0.080, R_y=625.0,
                         angle_deg=60.0, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    sin60 = math.sin(math.radians(angle_deg))
    cos60 = math.cos(math.radians(angle_deg))
    # R_y = ρ A_3 v² sin60
    v = math.sqrt(R_y / (rho * A_3 * sin60))
    v_1 = (A_2 + A_3) / A_1 * v
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v
    Q_3 = A_3 * v
    p_M1 = rho / 2 * (v**2 - v_1**2)
    m_dot_1 = rho * Q_1
    m_dot_2 = rho * Q_2
    m_dot_3 = rho * Q_3
    # F_st_x: p_M1·A_1 + F_st_x = m_dot_2·v + m_dot_3·v·cos60 - m_dot_1·v_1
    F_st_x = m_dot_2 * v + m_dot_3 * v * cos60 - m_dot_1 * v_1 - p_M1 * A_1
    R_x = -F_st_x
    R_total = math.sqrt(R_x**2 + R_y**2)
    return {"v": v, "v_1": v_1, "Q_1": Q_1,
            "p_M1": p_M1, "R_x": R_x, "R_total": R_total}


def primjer_koljeno_rashladni(D=0.080, Q=0.018, p_1=250e3, p_2=230e3, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    R_x = p_1 * A + m_dot * v
    R_y = p_2 * A + m_dot * v
    F_R = math.sqrt(R_x**2 + R_y**2)
    return {"R_x": R_x, "R_y": R_y, "F_R": F_R}


def primjer_vatrogasni(d=0.050, v_2=28.0, p_1=600e3, D_1=0.100, rho=998.0):
    A_2 = math.pi * d**2 / 4
    Q = A_2 * v_2
    A_1 = math.pi * D_1**2 / 4
    v_1 = Q / A_1
    m_dot = rho * Q
    R_x = p_1 * A_1 - m_dot * (v_2 - v_1)
    return {"v_1": v_1, "Q": Q, "R_x": R_x}


def zadatak_1(m_dot=12.0, v=18.0):
    return {"F": m_dot * v}


def zadatak_2(D=0.100, Q=0.025, p_1=200e3, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    return {"v": v, "m_dot": m_dot}


def zadatak_3(D=0.150, Q=0.040, p_1=180e3, p_2=160e3, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    R_x = p_1 * A + m_dot * v
    return {"v": v, "R_x": R_x}


def zadatak_4(D=0.120, v_1=2.5, p_1=180e3, rho=998.0):
    A = math.pi * D**2 / 4
    Q = A * v_1
    return {"Q": Q}


def zadatak_5(D_1=0.180, D_2=0.110, p_1=300e3, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    return {"A_1": A_1, "A_2": A_2}


def zadatak_6(D=0.090, Q=0.020, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    return {"v": v}


# ------------ Faza 1.5 dodatak: Vodeni udar (CH T3) ----------------
def cjeloviti_3_vodeni_udar(D=0.150, Q=0.050, rho=870.0, c=1200.0, L=200.0,
                              dt_a=0.20, dt_b=1.0, dt_c=5.0):
    A = math.pi * D**2 / 4
    v_0 = Q / A
    T_ref = 2 * L / c
    dp_J = rho * c * v_0
    # (a) direktni udar
    dp_a = dp_J if dt_a < T_ref else dp_J * T_ref / dt_a
    # (b) indirektni
    dp_b = dp_J * T_ref / dt_b
    # (c) vrlo sporo
    dp_c = dp_J * T_ref / dt_c
    F_a = dp_a * A
    F_b = dp_b * A
    F_c = dp_c * A
    return {"v_0": v_0, "T_ref": T_ref, "dp_J": dp_J,
            "dp_a": dp_a, "dp_b": dp_b, "dp_c": dp_c,
            "F_a": F_a, "F_b": F_b, "F_c": F_c}


def verify():
    out = []

    r = primjer_1_mlaz()
    _check(out, "U11.P1.F", r["F"], 200.0, "N")

    r = primjer_2_mlaznica()
    _check(out, "U11.P2.v_2", r["v_2"], 5.82, "m/s", rel=0.02)
    _check(out, "U11.P2.Q_Ls", r["Q"] * 1000, 37.0, "L/s", rel=0.02)
    _check(out, "U11.P2.p_M1_kPa", r["p_M1"] / 1000, 16.4, "kPa", rel=0.02)
    _check(out, "U11.P2.R", r["R"], 445.0, "N", rel=0.03)

    r = primjer_3_koljeno()
    _check(out, "U11.P3.v_1", r["v_1"], 1.77, "m/s", rel=0.02)
    _check(out, "U11.P3.v_2", r["v_2"], 3.98, "m/s", rel=0.02)
    _check(out, "U11.P3.F_f_x", r["F_f_x"], 1402.0, "N", rel=0.02)
    _check(out, "U11.P3.F_f_y", r["F_f_y"], -383.0, "N", rel=0.05)
    _check(out, "U11.P3.F_R", r["F_R"], 1453.0, "N", rel=0.02)

    r = cjeloviti_1_T_racva()
    _check(out, "U11.CH1.v_1", r["v_1"], 4.49, "m/s", rel=0.02)
    _check(out, "U11.CH1.v", r["v"], 10.03, "m/s", rel=0.02)
    _check(out, "U11.CH1.Q_1", r["Q_1"], 0.114, "m^3/s", rel=0.02)
    _check(out, "U11.CH1.F_f_x", r["F_f_x"], 892.0, "N", rel=0.05)
    _check(out, "U11.CH1.F_R", r["F_R"], 1025.0, "N", rel=0.05)

    r = cjeloviti_2_Y_racva()
    _check(out, "U11.CH2.v", r["v"], 11.99, "m/s", rel=0.02)
    _check(out, "U11.CH2.v_1", r["v_1"], 6.81, "m/s", rel=0.02)
    _check(out, "U11.CH2.Q_1_Ls", r["Q_1"] * 1000, 155.0, "L/s", rel=0.02)
    _check(out, "U11.CH2.p_M1_kPa", r["p_M1"] / 1000, 48.6, "kPa", rel=0.02)
    _check(out, "U11.CH2.R_x", r["R_x"], 664.0, "N", rel=0.05)
    _check(out, "U11.CH2.R_total", r["R_total"], 912.0, "N", rel=0.02)

    r = primjer_koljeno_rashladni()
    _check(out, "U11.koljeno.R_x", r["R_x"], 1321.0, "N", rel=0.02)
    _check(out, "U11.koljeno.R_y", r["R_y"], 1221.0, "N", rel=0.02)
    _check(out, "U11.koljeno.F_R", r["F_R"], 1797.0, "N", rel=0.02)

    r = primjer_vatrogasni()
    _check(out, "U11.vatrogasni.v_1", r["v_1"], 7.0, "m/s", rel=0.02)
    _check(out, "U11.vatrogasni.Q_Ls", r["Q"] * 1000, 54.97, "L/s", rel=0.02)
    _check(out, "U11.vatrogasni.R_x", r["R_x"], 3560.0, "N", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U11.{name}.{first_key}_pos", r[first_key], r[first_key])

    # Faza 1.5: Vodeni udar (CH T3)
    r = cjeloviti_3_vodeni_udar()
    _check(out, "U11.CH3.v_0", r["v_0"], 2.83, "m/s", rel=0.02)
    _check(out, "U11.CH3.T_ref", r["T_ref"], 0.333, "s")
    _check(out, "U11.CH3.dp_J_MPa", r["dp_J"] / 1e6, 2.95, "MPa", rel=0.02)
    _check(out, "U11.CH3.dp_b_MPa", r["dp_b"] / 1e6, 0.98, "MPa", rel=0.02)
    _check(out, "U11.CH3.dp_c_kPa", r["dp_c"] / 1000, 197.0, "kPa", rel=0.02)
    _check(out, "U11.CH3.F_a_kN", r["F_a"] / 1000, 52.2, "kN", rel=0.02)
    _check(out, "U11.CH3.F_c_kN", r["F_c"] / 1000, 3.48, "kN", rel=0.02)

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
