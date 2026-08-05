"""Numericka verifikacija U08: Kontrolni volumen i kontinuitet."""
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


def primjer_1_difuzor(D_1=0.120, D_2=0.180, v_2=16.0, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = A_2 / A_1 * v_2
    Q = A_2 * v_2
    m_dot = rho * Q
    return {"A_1": A_1, "A_2": A_2, "v_1": v_1, "Q": Q, "m_dot": m_dot}


def primjer_2_mjesanje(Q_A=0.150, Q_B=0.030, s_B=0.80, D_C=0.30, rho_A=1000.0):
    rho_B = s_B * rho_A
    Q_C = Q_A + Q_B
    A_C = math.pi * D_C**2 / 4
    v_C = Q_C / A_C
    m_dot_C = rho_A * Q_A + rho_B * Q_B
    rho_C = m_dot_C / Q_C
    return {"rho_B": rho_B, "Q_C": Q_C, "v_C": v_C,
            "m_dot_C": m_dot_C, "rho_C": rho_C}


def primjer_3_izjednacni(L=3.0, b=1.8, Q_in=0.022, Q_out=0.008,
                          h_0=0.45, h_1=1.20, rho=998.0):
    A_T = L * b
    dhdt = (Q_in - Q_out) / A_T
    dh = h_1 - h_0
    dV = A_T * dh
    t = dV / (Q_in - Q_out)
    dm = rho * dV
    return {"A_T": A_T, "dhdt": dhdt, "dV": dV, "t": t, "dm": dm}


def cjeloviti_1_mijesajuci(L=4.2, b=1.5, Q_A=0.018, Q_B=0.006, s_B=1.10,
                            D_3=0.100, v_3=1.80, h_0=0.80, h_1=1.20,
                            rho_A=1000.0):
    rho_B = s_B * rho_A
    A_3 = math.pi * D_3**2 / 4
    Q_3 = A_3 * v_3
    m_dot_in = rho_A * Q_A + rho_B * Q_B
    Q_in = Q_A + Q_B
    rho_3 = m_dot_in / Q_in
    A_T = L * b
    dhdt = (Q_A + Q_B - Q_3) / A_T
    dh = h_1 - h_0
    dV = A_T * dh
    t = dV / (Q_A + Q_B - Q_3)
    dm = rho_3 * dV
    return {"rho_B": rho_B, "Q_3": Q_3, "rho_3": rho_3,
            "dhdt": dhdt, "t": t, "dm": dm}


def primjer_5_T_komad(D_1=0.032, v_1=4.5, D_2=0.020, udio_1=0.60, v_3=3.0):
    A_1 = math.pi * D_1**2 / 4
    Q_1 = A_1 * v_1
    Q_2 = udio_1 * Q_1
    Q_3 = (1 - udio_1) * Q_1
    A_2 = math.pi * D_2**2 / 4
    v_2 = Q_2 / A_2
    A_3 = Q_3 / v_3
    D_3 = math.sqrt(4 * A_3 / math.pi)
    return {"Q_1": Q_1, "Q_2": Q_2, "Q_3": Q_3, "v_2": v_2, "D_3": D_3}


def primjer_6_retencija(A_b=120.0, Q_1=0.35, Q_2=0.20, Q_iz=0.18,
                         dh_target=0.50):
    Q_neto = Q_1 + Q_2 - Q_iz
    dhdt = Q_neto / A_b
    t = dh_target / dhdt
    return {"Q_neto": Q_neto, "dhdt": dhdt, "t": t}


def primjer_ev_hladenje(D_1=0.020, d=0.006, n=16, Q_L_min=25.0):
    """Javni primjer rashladnoga razdjelnika baterijskog paketa."""

    Q = Q_L_min * 1.0e-3 / 60.0
    A_1 = math.pi * D_1**2 / 4
    A_d = math.pi * d**2 / 4
    v_1 = Q / A_1
    v_d = Q / (n * A_d)
    v_blocked = Q / ((n - 1) * A_d)
    rise_percent = (v_blocked / v_d - 1) * 100
    return {
        "Q": Q,
        "v_1": v_1,
        "v_d": v_d,
        "v_blocked": v_blocked,
        "rise_percent": rise_percent,
    }


def zadatak_1(D_1=0.10, D_2=0.16, v_1=4.8, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    Q = A_1 * v_1
    v_2 = Q / A_2
    m_dot = rho * Q
    return {"v_2": v_2, "Q": Q, "m_dot": m_dot}


def zadatak_2(D_1=0.120, v_1=3.1, D_2=0.050, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    Q = A_1 * v_1
    v_2 = Q / A_2
    m_dot = rho * Q
    return {"v_2": v_2, "m_dot": m_dot}


def zadatak_3(Q_1=0.012, Q_2=0.008, D_3=0.120):
    Q_3 = Q_1 + Q_2
    A_3 = math.pi * D_3**2 / 4
    v_3 = Q_3 / A_3
    return {"Q_3": Q_3, "v_3": v_3}


def zadatak_4(Q=0.030, D_2=0.090, D_3=0.070):
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    # v_2 = 2 v_3, Q = Q_2 + Q_3 = A_2 v_2 + A_3 v_3 = (2 A_2 + A_3) v_3
    v_3 = Q / (2 * A_2 + A_3)
    v_2 = 2 * v_3
    Q_2 = A_2 * v_2
    Q_3 = A_3 * v_3
    return {"Q_2": Q_2, "Q_3": Q_3, "v_2": v_2, "v_3": v_3}


def zadatak_5(D=1.60, Q_in=0.014, Q_out=0.009, dh_target=0.80):
    A = math.pi * D**2 / 4
    dhdt = (Q_in - Q_out) / A
    t = dh_target / dhdt
    return {"dhdt": dhdt, "t": t}


def zadatak_6(A_T=4.8, Q_A=0.011, Q_B=0.004, rho_B=1080.0, D=0.080,
               v_3=1.6, t_min=6.0, rho_A=1000.0,
               rel_Q_A=0.02, rel_Q_B=0.03, dv_3=0.08,
               freeboard=0.560):
    A_3 = math.pi * D**2 / 4
    Q_3 = A_3 * v_3
    m_dot = rho_A * Q_A + rho_B * Q_B
    rho_mix = m_dot / (Q_A + Q_B)
    dhdt = (Q_A + Q_B - Q_3) / A_T
    dm = rho_mix * (Q_A + Q_B - Q_3) * (t_min * 60)
    Q_A_hi = Q_A * (1 + rel_Q_A)
    Q_B_hi = Q_B * (1 + rel_Q_B)
    Q_3_lo = A_3 * (v_3 - dv_3)
    dhdt_max = (Q_A_hi + Q_B_hi - Q_3_lo) / A_T
    rise_max = dhdt_max * t_min * 60
    safe_time = freeboard / dhdt_max
    return {
        "Q_3": Q_3,
        "rho_mix": rho_mix,
        "dhdt": dhdt,
        "dm": dm,
        "dhdt_max": dhdt_max,
        "rise_max": rise_max,
        "safe_time": safe_time,
    }


def primjer_kinematika_srednja(R=0.025, v_max=3.0):
    # Paraboloidni profil v(r)=v_max(1-(r/R)^2): srednja = v_max/2
    v_mean = v_max / 2
    A = math.pi * R**2
    Q = v_mean * A
    return {"v_mean": v_mean, "A": A, "Q": Q}


def verify():
    out = []

    r = primjer_kinematika_srednja()
    _check(out, "U08.KIN.v_mean", r["v_mean"], 1.5, "m/s")
    _check(out, "U08.KIN.Q", r["Q"], 2.945e-3, "m^3/s")

    r = primjer_1_difuzor()
    _check(out, "U08.P1.v_1", r["v_1"], 36.0, "m/s")
    _check(out, "U08.P1.Q", r["Q"], 0.407, "m^3/s")
    _check(out, "U08.P1.m_dot", r["m_dot"], 406.0, "kg/s")

    r = primjer_3_izjednacni()
    _check(out, "U08.P3.A_T", r["A_T"], 5.40, "m^2")
    _check(out, "U08.P3.dhdt_mm_s", r["dhdt"] * 1000, 2.59, "mm/s")
    _check(out, "U08.P3.t", r["t"], 289.0, "s", rel=0.02)
    _check(out, "U08.P3.dm", r["dm"], 4040.0, "kg", rel=0.02)

    r = cjeloviti_1_mijesajuci()
    _check(out, "U08.CH1.Q_3", r["Q_3"], 0.01414, "m^3/s")
    _check(out, "U08.CH1.rho_3", r["rho_3"], 1025.0, "kg/m^3")
    _check(out, "U08.CH1.dhdt_mm_s", r["dhdt"] * 1000, 1.57, "mm/s", rel=0.02)
    _check(out, "U08.CH1.t", r["t"], 255.0, "s", rel=0.02)
    _check(out, "U08.CH1.dm", r["dm"], 2583.0, "kg", rel=0.02)

    r = primjer_5_T_komad()
    _check(out, "U08.P5.Q_1_Ls", r["Q_1"] * 1000, 3.62, "L/s")
    _check(out, "U08.P5.Q_2_Ls", r["Q_2"] * 1000, 2.17, "L/s", rel=0.02)
    _check(out, "U08.P5.v_2", r["v_2"], 6.9, "m/s", rel=0.02)
    _check(out, "U08.P5.D_3_mm", r["D_3"] * 1000, 24.8, "mm", rel=0.02)

    r = primjer_ev_hladenje()
    _check(out, "U08.P6.v_1", r["v_1"], 1.326, "m/s", rel=0.02)
    _check(out, "U08.P6.v_d", r["v_d"], 0.921, "m/s", rel=0.02)
    _check(out, "U08.P6.v_blocked", r["v_blocked"], 0.982, "m/s", rel=0.02)
    _check(out, "U08.P6.rise_percent", r["rise_percent"], 6.67, "%", rel=0.02)

    r = zadatak_1()
    _check(out, "U08.Z1.v_2", r["v_2"], 1.875, "m/s", rel=0.02)
    _check(out, "U08.Z1.Q_Ls", r["Q"] * 1000, 37.70, "L/s", rel=0.02)
    _check(out, "U08.Z1.m_dot", r["m_dot"], 37.62, "kg/s", rel=0.02)

    r = zadatak_2()
    _check(out, "U08.Z2.v_2", r["v_2"], 17.86, "m/s", rel=0.02)
    _check(out, "U08.Z2.m_dot", r["m_dot"], 35.00, "kg/s", rel=0.02)

    r = zadatak_3()
    _check(out, "U08.Z3.Q_3_Ls", r["Q_3"] * 1000, 20.0, "L/s")
    _check(out, "U08.Z3.v_3", r["v_3"], 1.768, "m/s", rel=0.02)

    r = zadatak_4()
    _check(out, "U08.Z4.Q_2_Ls", r["Q_2"] * 1000, 23.0, "L/s", rel=0.02)
    _check(out, "U08.Z4.Q_3_Ls", r["Q_3"] * 1000, 7.0, "L/s", rel=0.02)
    _check(out, "U08.Z4.v_2", r["v_2"], 3.62, "m/s", rel=0.02)
    _check(out, "U08.Z4.v_3", r["v_3"], 1.81, "m/s", rel=0.02)

    r = zadatak_5()
    _check(out, "U08.Z5.dhdt_mm_s", r["dhdt"] * 1000, 2.487, "mm/s", rel=0.02)
    _check(out, "U08.Z5.t", r["t"], 322.0, "s", rel=0.02)

    r = zadatak_6()
    _check(out, "U08.Z6.Q_3_Ls", r["Q_3"] * 1000, 8.04, "L/s", rel=0.02)
    _check(out, "U08.Z6.rho_mix", r["rho_mix"], 1020.0, "kg/m^3", rel=0.02)
    _check(out, "U08.Z6.dhdt_mm_s", r["dhdt"] * 1000, 1.45, "mm/s", rel=0.02)
    _check(out, "U08.Z6.dm", r["dm"], 2.55e3, "kg", rel=0.02)
    _check(out, "U08.Z6.dhdt_max_mm_s", r["dhdt_max"] * 1000, 1.604, "mm/s", rel=0.02)
    _check(out, "U08.Z6.rise_max", r["rise_max"], 0.577, "m", rel=0.02)
    _check(out, "U08.Z6.safe_time", r["safe_time"], 349.0, "s", rel=0.02)

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
