"""Numericka verifikacija U07: Uzgon, plivanje i stabilnost."""
from __future__ import annotations

import math
from itertools import product

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


def primjer_1_ponton(L=2.40, B=1.20, H=0.32, m_p=420.0, m_o=180.0, rho=998.0):
    m = m_p + m_o
    V = m / rho
    h = V / (L * B)
    V_max = L * B * H
    m_max = rho * V_max
    dm = m_max - m
    return {"V": V, "h": h, "m_max": m_max, "dm": dm}


def primjer_2_bocni_pomak(B=1.20, h_L=0.32, h_D=0.24):
    h_m = (h_L + h_D) / 2
    y_B = B * (h_L - h_D) / (12 * h_m)
    return {"h_m": h_m, "y_B": y_B}


def primjer_3_kompresor(L=3.10, B=1.00, m_p=676.0, m_k=190.0,
                         h_L=0.34, h_D=0.22, rho=998.0,
                         KG_p=0.14, KG_k=0.38):
    h_m = (h_L + h_D) / 2
    V = L * B * h_m
    y_B = B * (h_L - h_D) / (12 * h_m)
    tan_theta = (h_L - h_D) / B
    KB = h_m / 2
    BM = B**2 / (12 * h_m)
    KG = (m_p * KG_p + m_k * KG_k) / (m_p + m_k)
    GM = KB + BM - KG
    e = (m_p + m_k) / m_k * GM * tan_theta
    dh_m = m_k / (rho * L * B)
    return {
        "h_m": h_m, "V": V, "y_B": y_B, "tan_theta": tan_theta,
        "KB": KB, "BM": BM, "KG": KG, "GM": GM,
        "e": e, "dh_m": dh_m,
    }


def primjer_4_kalibracijski(b=0.32, l=0.20, t=0.22, rho_1=820.0, rho_2=1030.0,
                              m=12.8, g=9.81, x_misplaced=0.050):
    A = b * l
    # Neutralna ravnoteza: rho_1 A (t-x) + rho_2 A x = m
    # → 820·A·(0.22-x) + 1030·A·x = 12.8 → x ≈ 0.0933 m
    x = (m / A - rho_1 * t) / (rho_2 - rho_1)
    # Pri misplaced x:
    F_U_mis = g * A * (rho_1 * (t - x_misplaced) + rho_2 * x_misplaced)
    G = m * g
    F_V = G - F_U_mis
    return {"A": A, "x": x, "F_U_mis": F_U_mis, "G": G, "F_V": F_V}


def cjeloviti_1_platforma_ulje_voda(L=3.00, B=1.20, H=0.34, m_p=648.0,
                                      rho_o=800.0, delta=0.10, rho_w=1000.0,
                                      m_k=180.0, h_L=0.30, h_D=0.20, g=9.81,
                                      KG_p=0.12, KG_k=0.54):
    h_m = (h_L + h_D) / 2
    V = L * B * h_m
    V_o = L * B * delta
    V_w = L * B * (h_m - delta)
    h_w_L = h_L - delta
    h_w_D = h_D - delta
    h_w_m = h_m - delta
    y_B_w = B * (h_w_L - h_w_D) / (12 * h_w_m)
    displaced_mass = rho_o * V_o + rho_w * V_w
    y_B = rho_w * V_w / displaced_mass * y_B_w
    z_B_o = h_m - delta / 2
    z_B_w = (h_m - delta) / 2
    KB_eq = (rho_o * V_o * z_B_o + rho_w * V_w * z_B_w) / displaced_mass
    I_T = L * B**3 / 12
    BM_eq = rho_w * I_T / displaced_mass
    KG = (m_p * KG_p + m_k * KG_k) / (m_p + m_k)
    GM_eq = KB_eq + BM_eq - KG
    tan_theta = (h_L - h_D) / B
    e = (m_p + m_k) / m_k * GM_eq * tan_theta
    # Predyzo: h_0 from m_p only
    # ρ_o L B δ + ρ_w L B (h_0 - δ) = m_p → h_0 = δ + (m_p - ρ_o L B δ)/(ρ_w L B)
    h_0 = delta + (m_p - rho_o * L * B * delta) / (rho_w * L * B)
    dh_m = h_m - h_0
    return {
        "h_m": h_m, "V": V, "V_o": V_o, "V_w": V_w,
        "displaced_mass": displaced_mass, "y_B_w": y_B_w, "y_B": y_B,
        "z_B_o": z_B_o, "z_B_w": z_B_w, "KB_eq": KB_eq,
        "I_T": I_T, "BM_eq": BM_eq, "KG": KG, "GM_eq": GM_eq,
        "tan_theta": tan_theta, "e": e, "h_0": h_0, "dh_m": dh_m,
    }


def primjer_5_pumpno_kuciste(V=0.045, m=85.0, rho=1025.0, g=9.81):
    F_U = rho * g * V
    G = m * g
    F_neto = G - F_U
    return {"F_U": F_U, "G": G, "F_neto": F_neto}


def primjer_6_privezni_ponton(L=6.00, B=2.40, m_p=1800.0, m_o=600.0, e=0.60,
                                rho=998.0, g=9.81, KG=0.40):
    m = m_p + m_o
    h_sr = m / (rho * L * B)
    KB = h_sr / 2
    BM = B**2 / (12 * h_sr)
    GM = KB + BM - KG
    tan_theta = m_o * e / (m * GM)
    dh = B * tan_theta
    return {
        "m": m, "h_sr": h_sr, "KB": KB, "BM": BM, "KG": KG,
        "GM": GM, "tan_theta": tan_theta, "dh": dh,
    }


def primjer_plutajuci_vjetroagregat(m=1.10e6, D=9.0, H=95.0,
                                     rho=1025.0):
    A = math.pi * D**2 / 4
    V = m / rho
    draft = V / A
    return {
        "A": A,
        "V": V,
        "draft": draft,
        "freeboard": H - draft,
        "draft_plus": 1.05 * m / (rho * A),
        "draft_minus": 0.95 * m / (rho * A),
    }


def zadatak_1(V=0.085, m=62.0, rho=998.0, g=9.81):
    F_U = rho * g * V
    G = m * g
    # Buduci da je F_U>G, dodatna sila mora djelovati prema dolje.
    F_hold_down = F_U - G
    return {"F_U": F_U, "G": G, "F_hold_down": F_hold_down}


def zadatak_2(L=2.60, B=1.40, H=0.38, m_p=510.0, m_t=220.0, rho=998.0):
    m = m_p + m_t
    V = m / rho
    h = V / (L * B)
    m_max = rho * L * B * H
    dm = m_max - m
    return {"V": V, "h": h, "dm": dm}


def zadatak_3(L=2.20, B=1.00, m=560.0, m_kompresor=85.0, e=0.24,
              rho=998.0, KG=0.18):
    h_m = m / (rho * L * B)
    KB = h_m / 2
    BM = B**2 / (12 * h_m)
    GM = KB + BM - KG
    tan_theta = m_kompresor * e / (m * GM)
    dh = B * tan_theta
    y_B = BM * tan_theta
    return {
        "h_m": h_m, "KB": KB, "BM": BM, "KG": KG, "GM": GM,
        "tan_theta": tan_theta, "y_B": y_B, "dh": dh,
    }


def zadatak_4(m=0.085, d=0.008, h_1=0.082, h_2=0.095, rho_water=1000.0):
    # Areometar: V_uron(voda) = V_tijela + (π d²/4) h_1
    # ρ_water V_uron_water = m  → V_uron_water = m/ρ_water
    # Vrat A = π d²/4. Razlika V_uron između voda i ulje:
    A_vrat = math.pi * d**2 / 4
    V_uron_voda = m / rho_water
    # U ulju: V_uron_ulje = V_uron_voda + A_vrat·(h_2 - h_1)
    V_uron_ulje = V_uron_voda + A_vrat * (h_2 - h_1)
    rho_ulje = m / V_uron_ulje
    return {"rho_ulje": rho_ulje, "V_uron_voda": V_uron_voda,
            "V_uron_ulje": V_uron_ulje}


def zadatak_5(V_ist=0.62, GM=0.18, phi_deg=7.0, rho=998.0, g=9.81):
    Delta = rho * g * V_ist
    M_r = Delta * GM * math.sin(math.radians(phi_deg))
    return {"Delta": Delta, "M_r": M_r, "stable": GM > 0.0}


def zadatak_6(L=2.80, B=1.20, rho_o=820.0, delta=0.08, rho_w=998.0,
               h_L=0.26, h_D=0.18, m=690.0, m_akumulator=70.0,
               KG=0.200, h_tol=0.003, rho_w_tol=3.0,
               m_akumulator_tol=1.0, KG_tol=0.005, g=9.81):
    def state(h_left, h_right, rho_water, accumulator_mass, kg):
        h_m = (h_left + h_right) / 2
        V_o = L * B * delta
        V_w = L * B * (h_m - delta)
        h_w_L = h_left - delta
        h_w_D = h_right - delta
        h_w_m = h_m - delta
        y_B_w = B * (h_w_L - h_w_D) / (12 * h_w_m)
        equivalent_mass = rho_o * V_o + rho_water * V_w
        y_B = rho_water * V_w / equivalent_mass * y_B_w
        z_B_o = h_m - delta / 2
        z_B_w = (h_m - delta) / 2
        KB_eq = (
            rho_o * V_o * z_B_o + rho_water * V_w * z_B_w
        ) / equivalent_mass
        I_T = L * B**3 / 12
        BM_eq = rho_water * I_T / equivalent_mass
        GM_eq = KB_eq + BM_eq - kg
        tan_theta = (h_left - h_right) / B
        e = m / accumulator_mass * GM_eq * tan_theta
        return {
            "h_m": h_m, "V_o": V_o, "V_w": V_w,
            "equivalent_mass": equivalent_mass, "y_B_w": y_B_w,
            "y_B": y_B, "z_B_o": z_B_o, "z_B_w": z_B_w,
            "KB_eq": KB_eq, "I_T": I_T, "BM_eq": BM_eq,
            "KG": kg, "GM_eq": GM_eq, "tan_theta": tan_theta,
            "e": e, "h_L": h_left, "h_D": h_right,
            "rho_w": rho_water, "m_akumulator": accumulator_mass,
        }

    nominal = state(h_L, h_D, rho_w, m_akumulator, KG)
    corners = [
        state(h_left, h_right, rho_water, accumulator_mass, kg)
        for h_left, h_right, rho_water, accumulator_mass, kg in product(
            (h_L - h_tol, h_L + h_tol),
            (h_D - h_tol, h_D + h_tol),
            (rho_w - rho_w_tol, rho_w + rho_w_tol),
            (m_akumulator - m_akumulator_tol,
             m_akumulator + m_akumulator_tol),
            (KG - KG_tol, KG + KG_tol),
        )
    ]
    worst = max(corners, key=lambda result: result["e"])
    nominal["e_max"] = worst["e"]
    nominal["worst"] = worst
    nominal["corner_count"] = len(corners)
    return nominal


# ------------ Faza 1.5 dodatak: Asimetricno poplavljen tank broda ----------------
def cjeloviti_2_poplavljen_tank(L=80.0, B=15.0, H=8.0, m_b=4000e3,
                                 KGb=3.0, rho_m=1025.0,
                                 L_t=15.0, B_t=6.0, H_t=3.0, g=9.81):
    V_w = L_t * B_t * H_t
    m_w = rho_m * V_w
    e_t = B / 2 - B_t / 2  # bocni pomak centroida tanka od osi simetrije
    m_uk = m_b + m_w
    e_G = m_w * e_t / m_uk
    KG_new = (m_b * KGb + m_w * (H_t / 2)) / m_uk
    T_0 = m_b / (rho_m * L * B)
    T_1 = m_uk / (rho_m * L * B)
    dT = T_1 - T_0
    I_T = L * B**3 / 12
    V_displ = m_uk / rho_m
    BM = I_T / V_displ
    KB = T_1 / 2
    BG = KG_new - KB
    GM = BM - BG
    tan_theta = e_G / GM
    theta_deg = math.degrees(math.atan(tan_theta))
    Fb = H - T_1
    dz_palube = (B / 2) * math.sin(math.radians(theta_deg))
    Fb_L = Fb - dz_palube
    theta_lim = math.degrees(math.asin(Fb / (B / 2)))
    return {"V_w": V_w, "m_w": m_w, "e_G": e_G, "KG_new": KG_new,
            "T_1": T_1, "dT": dT, "BM": BM, "GM": GM,
            "theta_deg": theta_deg, "Fb_L": Fb_L, "theta_lim": theta_lim}


def verify():
    out = []

    r = primjer_1_ponton()
    _check(out, "U07.P1.V", r["V"], 0.601, "m^3")
    _check(out, "U07.P1.h", r["h"], 0.209, "m")
    _check(out, "U07.P1.m_max", r["m_max"], 920.0, "kg")
    _check(out, "U07.P1.dm", r["dm"], 320.0, "kg", rel=0.02)

    r = primjer_3_kompresor()
    _check(out, "U07.P3.h_m", r["h_m"], 0.28, "m")
    _check(out, "U07.P3.V", r["V"], 0.868, "m^3")
    _check(out, "U07.P3.y_B", r["y_B"], 0.0357, "m")
    _check(out, "U07.P3.KB", r["KB"], 0.1400, "m")
    _check(out, "U07.P3.BM", r["BM"], 0.2976, "m")
    _check(out, "U07.P3.KG", r["KG"], 0.1927, "m")
    _check(out, "U07.P3.GM", r["GM"], 0.2450, "m")
    _check(out, "U07.P3.e", r["e"], 0.1340, "m", rel=0.02)
    _check(out, "U07.P3.dh_m", r["dh_m"], 0.0614, "m")

    r = cjeloviti_1_platforma_ulje_voda()
    _check(out, "U07.CH1.h_m", r["h_m"], 0.25, "m")
    _check(out, "U07.CH1.V", r["V"], 0.900, "m^3")
    _check(out, "U07.CH1.V_o", r["V_o"], 0.360, "m^3")
    _check(out, "U07.CH1.V_w", r["V_w"], 0.540, "m^3")
    _check(out, "U07.CH1.y_B_w", r["y_B_w"], 0.0667, "m")
    _check(out, "U07.CH1.y_B", r["y_B"], 0.0435, "m", rel=0.02)
    _check(out, "U07.CH1.KB_eq", r["KB_eq"], 0.1185, "m")
    _check(out, "U07.CH1.BM_eq", r["BM_eq"], 0.5217, "m")
    _check(out, "U07.CH1.KG", r["KG"], 0.2113, "m")
    _check(out, "U07.CH1.GM_eq", r["GM_eq"], 0.4289, "m")
    _check(out, "U07.CH1.e", r["e"], 0.1644, "m", rel=0.02)
    _check(out, "U07.CH1.h_0", r["h_0"], 0.20, "m")
    _check(out, "U07.CH1.dh_m", r["dh_m"], 0.05, "m")

    r = primjer_5_pumpno_kuciste()
    _check(out, "U07.P5.F_U", r["F_U"], 452.5, "N")
    _check(out, "U07.P5.G", r["G"], 833.9, "N")
    _check(out, "U07.P5.F_neto", r["F_neto"], 381.4, "N", rel=0.02)

    z1 = zadatak_1()
    _check(out, "U07.Z1.F_U", z1["F_U"], 832.0, "N")
    _check(out, "U07.Z1.G", z1["G"], 608.0, "N")
    _check(out, "U07.Z1.F_hold_down", z1["F_hold_down"], 224.0, "N")

    z2 = zadatak_2()
    _check(out, "U07.Z2.V", z2["V"], 0.73, "m^3")
    _check(out, "U07.Z2.h", z2["h"], 0.20, "m")
    _check(out, "U07.Z2.dm", z2["dm"], 650.0, "kg")

    z3 = zadatak_3()
    _check(out, "U07.Z3.h_m", z3["h_m"], 0.25, "m", rel=0.03)
    _check(out, "U07.Z3.KB", z3["KB"], 0.1275, "m")
    _check(out, "U07.Z3.BM", z3["BM"], 0.3267, "m")
    _check(out, "U07.Z3.GM", z3["GM"], 0.2743, "m")
    _check(out, "U07.Z3.dh", z3["dh"], 0.1328, "m", rel=0.02)

    z4 = zadatak_4()
    _check(out, "U07.Z4.rho_ulje", z4["rho_ulje"], 990.0, "kg/m^3")

    z5 = zadatak_5()
    _check(out, "U07.Z5.Delta_kN", z5["Delta"] / 1000, 6.07, "kN")
    _check(out, "U07.Z5.M_r", z5["M_r"], 133.0, "N m")

    z6 = zadatak_6()
    _check(out, "U07.Z6.h_m", z6["h_m"], 0.22, "m")
    _check(out, "U07.Z6.V_o", z6["V_o"], 0.269, "m^3")
    _check(out, "U07.Z6.V_w", z6["V_w"], 0.470, "m^3")
    _check(out, "U07.Z6.equivalent_mass", z6["equivalent_mass"], 689.9, "kg")
    _check(out, "U07.Z6.y_B_w", z6["y_B_w"], 0.057, "m")
    _check(out, "U07.Z6.y_B", z6["y_B"], 0.039, "m")
    _check(out, "U07.Z6.KB_eq", z6["KB_eq"], 0.1051, "m")
    _check(out, "U07.Z6.BM_eq", z6["BM_eq"], 0.5833, "m")
    _check(out, "U07.Z6.GM_eq", z6["GM_eq"], 0.4884, "m")
    _check(out, "U07.Z6.e", z6["e"], 0.3209, "m", rel=0.02)
    _check(out, "U07.Z6.e_max", z6["e_max"], 0.3540, "m", rel=0.02)
    _invariant(
        out,
        "U07.Z6.corridor_rejected",
        z6["e"] < 0.34 < z6["e_max"],
        "Nominalni i konzervativni omotac ne daju deklariranu odluku.",
    )

    p3_balance = primjer_3_kompresor()
    _invariant(
        out,
        "U07.INV.compressor_gm_balance",
        abs(p3_balance["y_B"] - p3_balance["BM"] * p3_balance["tan_theta"])
        < 1e-12
        and abs(
            190.0 * p3_balance["e"]
            - 866.0 * p3_balance["GM"] * p3_balance["tan_theta"]
        ) < 1e-12
        and abs(p3_balance["GM"] - p3_balance["BM"]) > 0.04,
        "Geometrijski y_B pomijesan je s GZ ili moment ne koristi GM.",
    )

    ch1_balance = cjeloviti_1_platforma_ulje_voda()
    _invariant(
        out,
        "U07.INV.two_fluid_gm_balance",
        abs(
            ch1_balance["y_B"]
            - ch1_balance["BM_eq"] * ch1_balance["tan_theta"]
        ) < 1e-12
        and abs(
            180.0 * ch1_balance["e"]
            - 828.0 * ch1_balance["GM_eq"] * ch1_balance["tan_theta"]
        ) < 1e-12,
        "Dvofluidni geometrijski pomak ili momentna ravnoteza nisu zatvoreni.",
    )

    _invariant(
        out,
        "U07.INV.z3_uses_gm",
        abs(85.0 * 0.24 - 560.0 * z3["GM"] * z3["tan_theta"])
        < 1e-12
        and abs(z3["dh"] - 1.00 * z3["tan_theta"]) < 1e-12,
        "Z3 ne zatvara mali-nagibni moment preko GM.",
    )

    _invariant(
        out,
        "U07.INV.z6_corner_envelope",
        z6["corner_count"] == 32
        and abs(z6["worst"]["h_L"] - 0.263) < 1e-12
        and abs(z6["worst"]["h_D"] - 0.177) < 1e-12
        and abs(z6["worst"]["rho_w"] - 1001.0) < 1e-12
        and abs(z6["worst"]["m_akumulator"] - 69.0) < 1e-12
        and abs(z6["worst"]["KG"] - 0.195) < 1e-12,
        "Konzervativni omotac Z6 nije provjerio sve rubne kombinacije.",
    )

    _invariant(
        out,
        "U07.INV.submerged_force_balance",
        abs(z1["F_U"] - z1["G"] - z1["F_hold_down"]) < 1e-12,
        "Dodatna sila ne zatvara vertikalnu ravnotezu uronjenog tijela.",
    )
    _invariant(
        out,
        "U07.INV.ponton_capacity_limit",
        z2["dm"] > 0.0 and z2["h"] < 0.38,
        "Ponton je dosegnuo rub prije deklarirane dodatne mase.",
    )
    _invariant(
        out,
        "U07.INV.areometer_buoyancy_balance",
        abs(1000.0 * z4["V_uron_voda"] - 0.085) < 1e-14
        and abs(z4["rho_ulje"] * z4["V_uron_ulje"] - 0.085) < 1e-14,
        "Areometar ne istiskuje vlastitu masu u oba fluida.",
    )
    _invariant(
        out,
        "U07.INV.metacentric_restoring_sign",
        z5["stable"] and z5["M_r"] > 0.0,
        "Pozitivan GM nije dao pozitivan povratni moment.",
    )
    _invariant(
        out,
        "U07.INV.two_fluid_balance_and_centroid",
        abs(z6["equivalent_mass"] - 690.0) < 0.2
        and 0.0 < z6["y_B"] < z6["y_B_w"]
        and abs(z6["y_B"] - z6["BM_eq"] * z6["tan_theta"]) < 1e-12
        and abs(
            70.0 * z6["e"] - 690.0 * z6["GM_eq"] * z6["tan_theta"]
        ) < 1e-12,
        "Dvofluidna istisnina ne zatvara masu ili rezultantni centar nije izmedu komponenti.",
    )

    # Faza 1.5: Asimetricno poplavljen tank broda (CH T4)
    r = cjeloviti_2_poplavljen_tank()
    _check(out, "U07.CH2.V_w_m3", r["V_w"], 270.0, "m^3")
    _check(out, "U07.CH2.m_w_t", r["m_w"] / 1000, 276.75, "t")
    _check(out, "U07.CH2.e_G_m", r["e_G"], 0.291, "m", rel=0.02)
    _check(out, "U07.CH2.KG_new_m", r["KG_new"], 2.903, "m", rel=0.02)
    _check(out, "U07.CH2.T_1_m", r["T_1"], 3.478, "m")
    _check(out, "U07.CH2.dT_m", r["dT"], 0.226, "m", rel=0.02)
    _check(out, "U07.CH2.BM_m", r["BM"], 5.394, "m", rel=0.02)
    _check(out, "U07.CH2.GM_m", r["GM"], 4.230, "m", rel=0.02)
    _check(out, "U07.CH2.theta_deg", r["theta_deg"], 3.94, "deg", rel=0.02)
    _check(out, "U07.CH2.theta_lim_deg", r["theta_lim"], 37.1, "deg", rel=0.02)

    r = primjer_plutajuci_vjetroagregat()
    _check(out, "U07.wind.A", r["A"], 63.62, "m2", rel=0.02)
    _check(out, "U07.wind.V", r["V"], 1073.2, "m3", rel=0.02)
    _check(out, "U07.wind.draft", r["draft"], 16.87, "m", rel=0.02)
    _check(out, "U07.wind.freeboard", r["freeboard"], 78.13, "m", rel=0.02)
    _check(out, "U07.wind.draft_plus", r["draft_plus"], 17.71, "m", rel=0.02)
    _check(out, "U07.wind.draft_minus", r["draft_minus"], 16.02, "m", rel=0.02)

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
