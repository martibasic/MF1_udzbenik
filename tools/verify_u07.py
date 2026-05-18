"""Numericka verifikacija U07: Uzgon, plivanje i stabilnost."""
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
                         h_L=0.34, h_D=0.22, rho=998.0):
    h_m = (h_L + h_D) / 2
    V = L * B * h_m
    y_B = B * (h_L - h_D) / (12 * h_m)
    e = (m_p + m_k) / m_k * y_B
    dh_m = m_k / (rho * L * B)
    return {"h_m": h_m, "V": V, "y_B": y_B, "e": e, "dh_m": dh_m}


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
                                      m_k=180.0, h_L=0.30, h_D=0.20, g=9.81):
    h_m = (h_L + h_D) / 2
    V = L * B * h_m
    V_o = L * B * delta
    V_w = L * B * (h_m - delta)
    h_w_L = h_L - delta
    h_w_D = h_D - delta
    h_w_m = h_m - delta
    y_B_w = B * (h_w_L - h_w_D) / (12 * h_w_m)
    y_B = rho_w * V_w / (rho_o * V_o + rho_w * V_w) * y_B_w
    e = (m_p + m_k) / m_k * y_B
    # Predyzo: h_0 from m_p only
    # ρ_o L B δ + ρ_w L B (h_0 - δ) = m_p → h_0 = δ + (m_p - ρ_o L B δ)/(ρ_w L B)
    h_0 = delta + (m_p - rho_o * L * B * delta) / (rho_w * L * B)
    dh_m = h_m - h_0
    return {"h_m": h_m, "V": V, "V_o": V_o, "V_w": V_w,
            "y_B_w": y_B_w, "y_B": y_B, "e": e, "h_0": h_0, "dh_m": dh_m}


def primjer_5_pumpno_kuciste(V=0.045, m=85.0, rho=1025.0, g=9.81):
    F_U = rho * g * V
    G = m * g
    F_neto = G - F_U
    return {"F_U": F_U, "G": G, "F_neto": F_neto}


def primjer_6_privezni_ponton(L=6.00, B=2.40, m_p=1800.0, m_o=600.0, e=0.60,
                                rho=998.0, g=9.81):
    m = m_p + m_o
    h_sr = m / (rho * L * B)
    dh = 6 * m_o * e / (rho * L * B**2)
    return {"m": m, "h_sr": h_sr, "dh": dh}


def zadatak_1(V=0.085, m=62.0, rho=998.0, g=9.81):
    F_U = rho * g * V
    G = m * g
    F_drz = G - F_U  # >0 if G>F_U (sink); <0 if F_U>G (float up — need to hold down)
    return {"F_U": F_U, "F_drz": F_drz}


def zadatak_2(L=2.60, B=1.40, H=0.38, m_p=510.0, m_t=220.0, rho=998.0):
    m = m_p + m_t
    V = m / rho
    h = V / (L * B)
    m_max = rho * L * B * H
    dm = m_max - m
    return {"V": V, "h": h, "dm": dm}


def zadatak_3(L=2.20, B=1.00, m=560.0, m_kompresor=85.0, e=0.24, rho=998.0):
    h_m = m / (rho * L * B)
    y_B = m_kompresor * e / m
    dh = 12 * h_m * y_B / B
    return {"h_m": h_m, "y_B": y_B, "dh": dh}


def zadatak_4(m=0.085, d=0.008, h_1=0.082, h_2=0.095, rho_water=1000.0):
    # Areometar: V_uron(voda) = V_tijela + (π d²/4) h_1
    # ρ_water V_uron_water = m  → V_uron_water = m/ρ_water
    # Vrat A = π d²/4. Razlika V_uron između voda i ulje:
    A_vrat = math.pi * d**2 / 4
    V_uron_voda = m / rho_water
    # U ulju: V_uron_ulje = V_uron_voda + A_vrat·(h_2 - h_1)
    V_uron_ulje = V_uron_voda + A_vrat * (h_2 - h_1)
    rho_ulje = m / V_uron_ulje
    return {"rho_ulje": rho_ulje}


def zadatak_5(V_ist=0.62, GM=0.18, phi_deg=7.0, rho=1000.0, g=9.81):
    Delta = rho * g * V_ist
    M_r = Delta * GM * math.sin(math.radians(phi_deg))
    return {"M_r": M_r}


def zadatak_6(L=2.80, B=1.20, rho_o=820.0, delta=0.08, rho_w=998.0,
               h_L=0.26, h_D=0.18, m=640.0, m_akumulator=70.0, g=9.81):
    h_m = (h_L + h_D) / 2
    V_o = L * B * delta
    V_w = L * B * (h_m - delta)
    h_w_L = h_L - delta
    h_w_D = h_D - delta
    h_w_m = h_m - delta
    y_B_w = B * (h_w_L - h_w_D) / (12 * h_w_m)
    y_B = rho_w * V_w / (rho_o * V_o + rho_w * V_w) * y_B_w
    e = m / m_akumulator * y_B
    return {"h_m": h_m, "V_o": V_o, "V_w": V_w, "y_B": y_B, "e": e}


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

    r = primjer_2_bocni_pomak()
    _check(out, "U07.P2.h_m", r["h_m"], 0.28, "m")
    _check(out, "U07.P2.y_B", r["y_B"], 0.0286, "m")

    r = primjer_3_kompresor()
    _check(out, "U07.P3.h_m", r["h_m"], 0.28, "m")
    _check(out, "U07.P3.V", r["V"], 0.868, "m^3")
    _check(out, "U07.P3.y_B", r["y_B"], 0.0357, "m")
    _check(out, "U07.P3.e", r["e"], 0.1628, "m", rel=0.02)
    _check(out, "U07.P3.dh_m", r["dh_m"], 0.0614, "m")

    r = primjer_4_kalibracijski()
    _check(out, "U07.P4.A", r["A"], 0.064, "m^2")
    _check(out, "U07.P4.x", r["x"], 0.0933, "m", rel=0.02)
    _check(out, "U07.P4.F_V", r["F_V"], 5.7, "N", rel=0.05)

    r = cjeloviti_1_platforma_ulje_voda()
    _check(out, "U07.CH1.h_m", r["h_m"], 0.25, "m")
    _check(out, "U07.CH1.V", r["V"], 0.900, "m^3")
    _check(out, "U07.CH1.V_o", r["V_o"], 0.360, "m^3")
    _check(out, "U07.CH1.V_w", r["V_w"], 0.540, "m^3")
    _check(out, "U07.CH1.y_B_w", r["y_B_w"], 0.0667, "m")
    _check(out, "U07.CH1.y_B", r["y_B"], 0.0435, "m", rel=0.02)
    _check(out, "U07.CH1.e", r["e"], 0.200, "m", rel=0.02)
    _check(out, "U07.CH1.h_0", r["h_0"], 0.20, "m")
    _check(out, "U07.CH1.dh_m", r["dh_m"], 0.05, "m")

    r = primjer_5_pumpno_kuciste()
    _check(out, "U07.P5.F_U", r["F_U"], 452.5, "N")
    _check(out, "U07.P5.G", r["G"], 833.9, "N")
    _check(out, "U07.P5.F_neto", r["F_neto"], 381.4, "N", rel=0.02)

    r = primjer_6_privezni_ponton()
    _check(out, "U07.P6.h_sr", r["h_sr"], 0.167, "m", rel=0.02)
    _check(out, "U07.P6.dh", r["dh"], 0.0626, "m", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U07.{name}.{first_key}_pos", r[first_key], r[first_key])

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
