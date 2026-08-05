"""Numericka verifikacija U03: Hidrostaticka raspodjela tlaka i manometrija."""
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


def primjer_1(rho=998.0, p_G_m=18e3, h=1.40, p_atm=100.8e3, g=9.81):
    p_G = p_atm + p_G_m
    p_A = p_G + rho * g * h
    p_A_m = p_A - p_atm
    return {"p_G": p_G, "p_A": p_A, "p_A_m": p_A_m}


def primjer_2(G_k=25.0, d_k=0.30, h1=0.25, h2=0.50, rho=1000.0, g=9.81):
    A_k = math.pi * d_k**2 / 4
    p_c = G_k / A_k
    p_A = p_c + rho * g * h1
    p_B = p_c - rho * g * (h2 - h1)
    return {"A_k": A_k, "p_c": p_c, "p_A": p_A, "p_B": p_B}


def primjer_3(rho_v=1000.0, rho_mv=1035.0, rho_Hg=13600.0, rho_zr=1.2,
              h1=0.60, h2=0.10, h3=0.70, h4=0.40, g=9.81):
    dp_bez_zraka = g * (rho_Hg * h2 - rho_mv * h4 - rho_v * h1)
    dp_sa_zrakom = g * (rho_Hg * h2 + rho_zr * h3 - rho_mv * h4 - rho_v * h1)
    return {"dp_bez_zraka": dp_bez_zraka, "dp_sa_zrakom": dp_sa_zrakom}


def primjer_4(rho=1000.0, rho_Hg=13600.0, dh=0.18, h=1.20,
              p_0=101325.0, g=9.81):
    p_g = p_0 - rho_Hg * g * dh
    p_g_m = p_g - p_0
    p_A = p_g + rho * g * h
    p_A_m = p_A - p_0
    return {"p_g": p_g, "p_g_m": p_g_m, "p_A": p_A, "p_A_m": p_A_m}


def cjeloviti_1(rho_w=1000.0, rho_o=850.0, rho_Hg=13600.0,
                h1=0.80, h2=0.55, a=0.30, b=0.25, dh=0.18, h_C=1.20,
                p_0=101325.0, g=9.81):
    p_2 = p_0 + rho_o * g * h2
    p_1 = p_2 - rho_w * g * a + rho_Hg * g * dh + rho_o * g * b
    p_G = p_1 - rho_w * g * h1
    p_G_m = p_G - p_0
    p_C = p_G + rho_w * g * h_C
    p_C_m = p_C - p_0
    return {"p_1": p_1, "p_2": p_2, "p_G": p_G, "p_G_m": p_G_m,
            "p_C": p_C, "p_C_m": p_C_m}


def primjer_pumpa(H=2.40, rho=870.0, p_atm=101.3e3, p_v=200.0, g=9.81):
    p_man = -rho * g * H
    p_aps = p_atm + p_man
    H_max = (p_atm - p_v) / (rho * g)
    return {"p_man": p_man, "p_aps": p_aps, "H_max": H_max}


def primjer_vodotoranj(Z_t=84.0, Z_k=68.0, rho=998.0, p_atm=100.5e3, g=9.81):
    dH = Z_t - Z_k
    p_man = rho * g * dH
    p_aps = p_atm + p_man
    return {"dH": dH, "p_man": p_man, "p_aps": p_aps}


def primjer_iot_tlak(p_A=520e3, dz=38.0, rho=998.0,
                      p_atm=101.3e3, dp_alarm=50e3, g=9.81):
    hydrostatic_drop = rho * g * dz
    p_B_gauge = p_A - hydrostatic_drop
    return {
        "hydrostatic_drop": hydrostatic_drop,
        "p_B_gauge": p_B_gauge,
        "p_B_abs": p_B_gauge + p_atm,
        "equivalent_head": dp_alarm / (rho * g),
    }


def zadatak_1(h=2.40, rho=998.0, p_atm=100.8e3, g=9.81):
    p_m = rho * g * h
    return {"p_m": p_m, "p_aps": p_atm + p_m}


def zadatak_2(p_m=26e3, h=1.80, rho=998.0, p_atm=99.2e3, g=9.81):
    p_priklj = p_m + rho * g * h
    return {"p_priklj_m": p_priklj, "p_priklj_aps": p_priklj + p_atm}


def zadatak_3(rho_u=860.0, rho_Hg=13600.0, dh=0.185, a=0.12, g=9.81):
    # tlak u kraku s uljem
    p_m = rho_Hg * g * dh - rho_u * g * a
    return {"p_m": p_m}


def zadatak_4(rho_w=998.0, rho_Hg=13600.0, dh=0.145, dz_AB=0.30, g=9.81):
    # Standardna zatvorena putanja: zivin stupac daje kontrast gustoca, a A je
    # dz_AB ispod B pa vodeni visinski clan povecava p_A-p_B.
    p_diff = (rho_Hg - rho_w) * g * dh + rho_w * g * dz_AB
    return {"p_A_minus_p_B": p_diff}


def zadatak_5(rho_Hg=13600.0, dh=0.230, p_atm=98.6e3, h_voda=0.90,
              rho_w=998.0, g=9.81):
    p_g_aps = p_atm - rho_Hg * g * dh
    p_tocka = p_g_aps + rho_w * g * h_voda
    return {"p_g_aps": p_g_aps, "p_tocka": p_tocka}


def zadatak_6(h1=0.65, dh=0.210, h_tocka=1.30, rho_w=998.0, rho_Hg=13600.0,
              p_atm=100.9e3, dh_tol=0.002, h_tol=0.005,
              p_atm_tol=0.4e3, scale_margin=0.05, g=9.81):
    p_priklj = p_atm + rho_Hg * g * dh
    p_G = p_priklj - rho_w * g * h1
    p_tocka = p_G + rho_w * g * h_tocka
    p_max = (
        p_atm + p_atm_tol
        + rho_Hg * g * (dh + dh_tol)
        - rho_w * g * (h1 - h_tol)
        + rho_w * g * (h_tocka + h_tol)
    )
    return {
        "p_G": p_G,
        "p_tocka": p_tocka,
        "p_max": p_max,
        "required_full_scale": (1 + scale_margin) * p_max,
    }


# ------------ Faza 1.5 dodatak: Balastni tank broda ----------------
def primjer_balastni(T_g=8.5, H_t=5.0, h_p=2.0, rho_m=1025.0, rho_b=1000.0, g=9.81):
    # Stanje A (tank pun)
    p_ext_dno = rho_m * g * T_g
    p_int_dno_A = rho_b * g * H_t
    delta_dno_A = p_ext_dno - p_int_dno_A
    delta_dno_B = p_ext_dno - 0.0  # Stanje B (prazan)
    p_ext_proz = rho_m * g * (T_g - h_p)
    p_int_proz_A = rho_b * g * (H_t - h_p)
    delta_proz_A = p_ext_proz - p_int_proz_A
    return {
        "p_ext_dno": p_ext_dno,
        "delta_dno_A": delta_dno_A,
        "delta_dno_B": delta_dno_B,
        "delta_proz_A": delta_proz_A,
    }


def verify():
    out = []

    r = primjer_1()
    _check(out, "U03.P1.p_G_kPa", r["p_G"] / 1000, 118.8, "kPa")
    _check(out, "U03.P1.p_A_kPa", r["p_A"] / 1000, 132.5, "kPa")
    _check(out, "U03.P1.p_A_m_kPa", r["p_A_m"] / 1000, 31.7, "kPa")

    r = primjer_3()
    _check(out, "U03.P3.dp_bez_zraka_Pa", r["dp_bez_zraka"], 3394.0, "Pa")
    _check(out, "U03.P3.dp_sa_zrakom_Pa", r["dp_sa_zrakom"], 3402.0, "Pa")

    r = cjeloviti_1()
    _check(out, "U03.CH1.p_2_kPa", r["p_2"] / 1000, 105.9, "kPa")
    _check(out, "U03.CH1.p_1_kPa", r["p_1"] / 1000, 129.1, "kPa")
    _check(out, "U03.CH1.p_G_kPa", r["p_G"] / 1000, 121.2, "kPa")
    _check(out, "U03.CH1.p_G_m_kPa", r["p_G_m"] / 1000, 19.9, "kPa")
    _check(out, "U03.CH1.p_C_kPa", r["p_C"] / 1000, 133.0, "kPa")
    _check(out, "U03.CH1.p_C_m_kPa", r["p_C_m"] / 1000, 31.7, "kPa")

    r = primjer_pumpa()
    _check(out, "U03.pumpa.p_man_kPa", r["p_man"] / 1000, -20.5, "kPa")
    _check(out, "U03.pumpa.p_aps_kPa", r["p_aps"] / 1000, 80.8, "kPa")
    _check(out, "U03.pumpa.H_max_m", r["H_max"], 11.8, "m")

    z1 = zadatak_1()
    _check(out, "U03.Z1.p_m_kPa", z1["p_m"] / 1000, 23.5, "kPa")
    _check(out, "U03.Z1.p_aps_kPa", z1["p_aps"] / 1000, 124.3, "kPa")
    z2 = zadatak_2()
    _check(out, "U03.Z2.p_m_kPa", z2["p_priklj_m"] / 1000, 43.6, "kPa")
    _check(out, "U03.Z2.p_aps_kPa", z2["p_priklj_aps"] / 1000, 142.8, "kPa")
    z3 = zadatak_3()
    _check(out, "U03.Z3.p_m_kPa", z3["p_m"] / 1000, 23.7, "kPa")
    z4 = zadatak_4()
    _check(out, "U03.Z4.p_diff_kPa", z4["p_A_minus_p_B"] / 1000, 20.9, "kPa")
    z5 = zadatak_5()
    _check(out, "U03.Z5.p_g_aps_kPa", z5["p_g_aps"] / 1000, 67.9, "kPa")
    _check(out, "U03.Z5.p_tocka_kPa", z5["p_tocka"] / 1000, 76.7, "kPa")
    z6 = zadatak_6()
    _check(out, "U03.Z6.p_G_kPa", z6["p_G"] / 1000, 122.6, "kPa")
    _check(out, "U03.Z6.p_tocka_kPa", z6["p_tocka"] / 1000, 135.3, "kPa")
    _check(out, "U03.Z6.p_max_kPa", z6["p_max"] / 1000, 136.05, "kPa", rel=0.02)
    _check(out, "U03.Z6.required_full_scale_kPa", z6["required_full_scale"] / 1000, 142.9, "kPa", rel=0.02)
    _invariant(
        out,
        "U03.Z6.sensor_range_choice",
        140e3 < z6["required_full_scale"] <= 160e3,
        "Ocekivani omotac ne zahtijeva deklarirani raspon 0--160 kPa.",
    )

    _invariant(
        out,
        "U03.INV.absolute_gauge_offset",
        abs((z1["p_aps"] - z1["p_m"]) - 100.8e3) < 1e-9,
        "Apsolutni i manometarski tlak ne razlikuju se za p_atm.",
    )
    _invariant(
        out,
        "U03.INV.pressure_increases_with_depth",
        z5["p_tocka"] > z5["p_g_aps"] and z6["p_tocka"] > z6["p_G"],
        "Tlak u istom mirnom fluidu nije porastao s dubinom.",
    )
    _invariant(
        out,
        "U03.INV.manometer_pressure_signs",
        z5["p_g_aps"] < 98.6e3 and z6["p_G"] > 100.9e3,
        "Vakuumski i nadtlacni manometar nemaju ocekivane predznake.",
    )

    # Faza 1.5: Balastni tank broda
    r = primjer_balastni()
    _check(out, "U03.balastni.p_ext_dno_kPa", r["p_ext_dno"] / 1000, 85.5, "kPa")
    _check(out, "U03.balastni.delta_dno_A_kPa", r["delta_dno_A"] / 1000, 36.4, "kPa")
    _check(out, "U03.balastni.delta_dno_B_kPa", r["delta_dno_B"] / 1000, 85.5, "kPa")
    _check(out, "U03.balastni.delta_proz_A_kPa", r["delta_proz_A"] / 1000, 35.9, "kPa")

    r = primjer_iot_tlak()
    _check(out, "U03.iot.hydrostatic_drop_kPa", r["hydrostatic_drop"] / 1000, 372.1, "kPa", rel=0.02)
    _check(out, "U03.iot.p_B_gauge_kPa", r["p_B_gauge"] / 1000, 147.9, "kPa", rel=0.02)
    _check(out, "U03.iot.p_B_abs_kPa", r["p_B_abs"] / 1000, 249.2, "kPa", rel=0.02)
    _check(out, "U03.iot.equivalent_head", r["equivalent_head"], 5.11, "m", rel=0.02)

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
