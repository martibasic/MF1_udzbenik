"""Numericka verifikacija U06: Zakrivljene plohe i rastav sila."""
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


def primjer_1_cetvrtina(R=1.22, b=1.83, h_1=2.44, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = h_1 + R / 2
    F_H = rho * g * A_x * h_Cx
    I_G = b * R**3 / 12
    h_FH = h_Cx + I_G / (h_Cx * A_x)
    V_1 = h_1 * R * b
    V_2 = math.pi * R**2 / 4 * b
    V_star = V_1 + V_2
    F_V = rho * g * V_star
    x_FV = (V_1 * (R / 2) + V_2 * (4 * R / (3 * math.pi))) / V_star
    F_R = math.sqrt(F_H**2 + F_V**2)
    return {"F_H": F_H, "h_FH": h_FH, "V_star": V_star,
            "F_V": F_V, "x_FV": x_FV, "F_R": F_R}


def primjer_2_brana(H=2.10, h=1.92, a=0.46, B=1.00, m=580.0,
                     rho=998.0, g=9.81):
    L = (h - a) * math.sqrt(2)
    y = H + a - h
    h_C = (h - a) / 2
    A = L * B
    F_OA = rho * g * h_C * A
    Delta_y = L / 6
    krak = L / 2 - Delta_y
    V_star = y**2 * B
    F_V = rho * g * V_star
    W = m * g
    F = ((W + F_V) * H - F_OA * krak) / H
    return {"L": L, "y": y, "F_OA": F_OA, "krak": krak,
            "F_V": F_V, "W": W, "F": F}


def primjer_3_cetvrtcilindricni(R=0.90, b=1.20, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = R / 2
    F_H = rho * g * A_x * h_Cx
    h_H = 2 * R / 3
    V_star = math.pi * R**2 / 4 * b
    F_V = rho * g * V_star
    x_V = 4 * R / (3 * math.pi)
    F_R = math.sqrt(F_H**2 + F_V**2)
    alpha_deg = math.degrees(math.atan(F_V / F_H))
    return {"F_H": F_H, "h_H": h_H, "F_V": F_V, "x_V": x_V,
            "F_R": F_R, "alpha_deg": alpha_deg}


def cjeloviti_1_spojnica(R=1.10, b=1.40, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = R / 2
    F_H = rho * g * A_x * h_Cx
    h_H = 2 * R / 3
    V_star = math.pi * R**2 / 4 * b
    F_V = rho * g * V_star
    # Kvasi se konveksna donja/lijeva strana. Teziste cetvrtine kruga udaljeno
    # je 4R/(3pi) od desnoga radijusa, pa je krak prema zglobu A njegov komplement.
    x_V = R - 4 * R / (3 * math.pi)
    F_R = math.sqrt(F_H**2 + F_V**2)
    alpha_deg = math.degrees(math.atan2(F_V, F_H))
    T = (F_H * h_H + F_V * x_V) / R
    return {"F_H": F_H, "h_H": h_H, "F_V": F_V, "x_V": x_V,
            "F_R": F_R, "alpha_deg": alpha_deg, "T": T}


def primjer_5_kotao(R=0.60, b=1.50, h_1=1.20, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = h_1 + R / 2
    F_H = rho * g * A_x * h_Cx
    V_star = b * (h_1 * R + math.pi * R**2 / 4)
    F_V = rho * g * V_star
    F_R = math.sqrt(F_H**2 + F_V**2)
    return {"F_H": F_H, "F_V": F_V, "V_star": V_star, "F_R": F_R}


def primjer_6_jezerce(R=1.00, b=4.00, h_1=2.50, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = h_1 + R / 2
    F_H = rho * g * A_x * h_Cx
    V_star = b * (h_1 * R + math.pi * R**2 / 4)
    F_V = rho * g * V_star
    F_R = math.sqrt(F_H**2 + F_V**2)
    return {"F_H": F_H, "F_V": F_V, "V_star": V_star, "F_R": F_R}


def zadatak_1(R=0.65, b=1.20, h_1=1.10, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = h_1 + R / 2
    F_H = rho * g * A_x * h_Cx
    V_star = b * (h_1 * R + math.pi * R**2 / 4)
    F_V = rho * g * V_star
    return {"F_H": F_H, "F_V": F_V,
            "F_R": math.sqrt(F_H**2 + F_V**2)}


def zadatak_2(R=0.30, b=0.90, h_C=1.20, rho=998.0, g=9.81):
    A_x = 2 * R * b
    F_H = rho * g * h_C * A_x
    V_star = math.pi * R**2 * b / 2
    F_V = rho * g * V_star
    F_R = math.hypot(F_H, F_V)
    alpha_deg = math.degrees(math.atan2(F_V, F_H))
    return {"F_H": F_H, "F_V": F_V, "F_R": F_R,
            "alpha_deg": alpha_deg}


def zadatak_3(R=0.40, b=1.00, h_top=0.85, rho=998.0, g=9.81):
    # Simetricna polukapa: horizontalni doprinosi i svi momenti oko C se
    # ponistavaju. Pomocni volumen je stupac iznad tjemena plus polucilindar.
    F_H = 0.0
    V_star = b * (2 * R * h_top + math.pi * R**2 / 2)
    F_V = rho * g * V_star
    return {"F_H": F_H, "F_V": F_V, "F_R": F_V, "M_C": 0.0}


def zadatak_4(R=0.55, p_0=18e3, b=1.0):
    # Trazene su promjene u odnosu na p0=0. Jednoliki tlak integrira se po
    # okomitoj odnosno vodoravnoj projekciji, obje povrsine Rb.
    delta_F_H = p_0 * R * b
    delta_F_V = p_0 * R * b
    return {"delta_F_H": delta_F_H, "delta_F_V": delta_F_V}


def zadatak_5(V_star=0.42, F_H=18.5e3, rho=998.0, g=9.81):
    F_V = rho * g * V_star
    F_R = math.sqrt(F_H**2 + F_V**2)
    return {"F_V": F_V, "F_R": F_R}


def zadatak_6(R=0.75, b=1.10, h_1=0.45, rho=998.0, g=9.81):
    A_x = R * b
    h_Cx = h_1 + R / 2
    F_H = rho * g * A_x * h_Cx
    I_G = b * R**3 / 12
    h_H = h_Cx + I_G / (A_x * h_Cx)
    lever_H = h_H - h_1
    V_rect = b * h_1 * R
    V_quarter = b * math.pi * R**2 / 4
    V_star = V_rect + V_quarter
    F_V = rho * g * V_star
    x_bar_V = (
        V_rect * (R / 2) + V_quarter * (4 * R / (3 * math.pi))
    ) / V_star
    lever_V = R - x_bar_V
    F_R = math.sqrt(F_H**2 + F_V**2)
    T = (F_H * lever_H + F_V * lever_V) / R
    return {"F_H": F_H, "h_H": h_H, "lever_H": lever_H,
            "F_V": F_V, "x_bar_V": x_bar_V, "lever_V": lever_V,
            "F_R": F_R, "T": T}


# ------------ Faza 1.5 dodatak: Plinski jastuk iznad cetvrtkruga ----------------
def primjer_plinski_jastuk(R=0.50, b=1.20, rho=860.0, p_g=200e3, g=9.81):
    A_proj_v = R * b
    A_proj_h = R * b
    h_C = R / 2
    F_H_oil = rho * g * h_C * A_proj_v
    F_H_gas = p_g * A_proj_v
    F_H = F_H_oil + F_H_gas
    V_imag = math.pi * R**2 / 4 * b
    F_V_oil = rho * g * V_imag
    F_V_gas = p_g * A_proj_h
    F_V = F_V_oil + F_V_gas
    F = math.sqrt(F_H**2 + F_V**2)
    alpha_deg = math.degrees(math.atan2(F_V, F_H))
    # Otvoren slucaj (p_g = 0):
    F_open = math.sqrt(F_H_oil**2 + F_V_oil**2)
    return {"F_H": F_H, "F_V": F_V, "F": F, "alpha_deg": alpha_deg,
            "F_H_gas": F_H_gas, "F_V_gas": F_V_gas, "F_open": F_open}


def verify():
    out = []

    r = primjer_1_cetvrtina()
    _check(out, "U06.P1.F_H_kN", r["F_H"] / 1000, 66.7, "kN")
    _check(out, "U06.P1.h_FH", r["h_FH"], 3.09, "m", rel=0.02)
    _check(out, "U06.P1.V_star", r["V_star"], 7.587, "m^3")
    _check(out, "U06.P1.F_V_kN", r["F_V"] / 1000, 74.3, "kN")
    _check(out, "U06.P1.x_FV", r["x_FV"], 0.584, "m", rel=0.02)
    _check(out, "U06.P1.F_R_kN", r["F_R"] / 1000, 99.8, "kN")

    r = primjer_2_brana()
    _check(out, "U06.P2.L", r["L"], 2.065, "m")
    _check(out, "U06.P2.y", r["y"], 0.64, "m")
    _check(out, "U06.P2.F_OA_kN", r["F_OA"] / 1000, 14.76, "kN")
    _check(out, "U06.P2.F_V_kN", r["F_V"] / 1000, 4.01, "kN")
    _check(out, "U06.P2.F_kN", r["F"] / 1000, 4.86, "kN", rel=0.02)

    r = primjer_3_cetvrtcilindricni()
    _check(out, "U06.P3.F_H_kN", r["F_H"] / 1000, 4.76, "kN")
    _check(out, "U06.P3.h_H", r["h_H"], 0.60, "m")
    _check(out, "U06.P3.F_V_kN", r["F_V"] / 1000, 7.47, "kN")
    _check(out, "U06.P3.x_V", r["x_V"], 0.382, "m")
    _check(out, "U06.P3.F_R_kN", r["F_R"] / 1000, 8.86, "kN")
    _check(out, "U06.P3.alpha_deg", r["alpha_deg"], 57.5, "deg", rel=0.02)

    r = cjeloviti_1_spojnica()
    _check(out, "U06.CH1.F_H_kN", r["F_H"] / 1000, 8.29, "kN")
    _check(out, "U06.CH1.h_H", r["h_H"], 0.733, "m")
    _check(out, "U06.CH1.F_V_kN", r["F_V"] / 1000, 13.03, "kN")
    _check(out, "U06.CH1.x_V", r["x_V"], 0.633, "m")
    _check(out, "U06.CH1.F_R_kN", r["F_R"] / 1000, 15.44, "kN", rel=0.02)
    _check(out, "U06.CH1.alpha_deg", r["alpha_deg"], 57.5, "deg", rel=0.02)
    _check(out, "U06.CH1.T_kN", r["T"] / 1000, 13.03, "kN", rel=0.02)

    r = primjer_5_kotao()
    _check(out, "U06.P5.F_H_kN", r["F_H"] / 1000, 13.22, "kN")
    _check(out, "U06.P5.F_V_kN", r["F_V"] / 1000, 14.74, "kN")
    _check(out, "U06.P5.F_R_kN", r["F_R"] / 1000, 19.8, "kN", rel=0.02)

    r = primjer_6_jezerce()
    _check(out, "U06.P6.F_H_kN", r["F_H"] / 1000, 117.6, "kN")
    _check(out, "U06.P6.F_V_kN", r["F_V"] / 1000, 128.6, "kN")
    _check(out, "U06.P6.F_R_kN", r["F_R"] / 1000, 174.0, "kN", rel=0.02)

    z1 = zadatak_1()
    _check(out, "U06.Z1.F_H_kN", z1["F_H"] / 1000, 10.9, "kN")
    _check(out, "U06.Z1.F_V_kN", z1["F_V"] / 1000, 12.3, "kN")
    _check(out, "U06.Z1.F_R_kN", z1["F_R"] / 1000, 16.4, "kN")

    z2 = zadatak_2()
    _check(out, "U06.Z2.F_H_kN", z2["F_H"] / 1000, 6.34, "kN")
    _check(out, "U06.Z2.F_V_kN", z2["F_V"] / 1000, 1.25, "kN")
    _check(out, "U06.Z2.F_R_kN", z2["F_R"] / 1000, 6.47, "kN")
    _check(out, "U06.Z2.alpha_deg", z2["alpha_deg"], 11.1, "deg")

    z3 = zadatak_3()
    _check(out, "U06.Z3.F_H_kN", z3["F_H"] / 1000, 0.0, "kN")
    _check(out, "U06.Z3.F_V_kN", z3["F_V"] / 1000, 9.12, "kN")
    _check(out, "U06.Z3.F_R_kN", z3["F_R"] / 1000, 9.12, "kN")
    _check(out, "U06.Z3.M_C", z3["M_C"], 0.0, "N m")

    z4 = zadatak_4()
    _check(out, "U06.Z4.delta_F_H_kN", z4["delta_F_H"] / 1000, 9.90, "kN")
    _check(out, "U06.Z4.delta_F_V_kN", z4["delta_F_V"] / 1000, 9.90, "kN")

    z5 = zadatak_5()
    _check(out, "U06.Z5.F_V_kN", z5["F_V"] / 1000, 4.11, "kN")
    _check(out, "U06.Z5.F_R_kN", z5["F_R"] / 1000, 19.0, "kN")

    z6 = zadatak_6()
    _check(out, "U06.Z6.F_H_kN", z6["F_H"] / 1000, 6.66, "kN")
    _check(out, "U06.Z6.h_H", z6["h_H"], 0.882, "m")
    _check(out, "U06.Z6.lever_H", z6["lever_H"], 0.432, "m")
    _check(out, "U06.Z6.F_V_kN", z6["F_V"] / 1000, 8.39, "kN")
    _check(out, "U06.Z6.x_bar_V", z6["x_bar_V"], 0.343, "m")
    _check(out, "U06.Z6.lever_V", z6["lever_V"], 0.407, "m")
    _check(out, "U06.Z6.F_R_kN", z6["F_R"] / 1000, 10.7, "kN")
    _check(out, "U06.Z6.T_kN", z6["T"] / 1000, 8.39, "kN")

    _invariant(
        out,
        "U06.INV.resultant_component_balance",
        abs(z1["F_R"] ** 2 - z1["F_H"] ** 2 - z1["F_V"] ** 2) < 1e-6,
        "Rezultanta nije vektorski zbroj komponenti.",
    )
    _invariant(
        out,
        "U06.INV.semicylinder_symmetry",
        z3["F_H"] == 0.0 and z3["M_C"] == 0.0 and z3["F_V"] > 0.0,
        "Simetricna polukapa ne ponistava FH i moment oko C.",
    )
    _invariant(
        out,
        "U06.INV.uniform_pressure_projections",
        z4["delta_F_H"] == z4["delta_F_V"] == 18e3 * 0.55,
        "Jednaki projekcijski presjeci nisu dali jednake dodatke sile.",
    )
    _invariant(
        out,
        "U06.INV.hinge_moment_balance",
        abs(
            z6["T"] * 0.75
            - z6["F_H"] * z6["lever_H"]
            - z6["F_V"] * z6["lever_V"]
        ) < 1e-9,
        "Sila spojnice ne zatvara moment hidrostatskih komponenti.",
    )

    # Faza 1.5: Plinski jastuk iznad cetvrtkruga
    r = primjer_plinski_jastuk()
    _check(out, "U06.plinski.F_H_kN", r["F_H"] / 1000, 121.3, "kN", rel=0.02)
    _check(out, "U06.plinski.F_V_kN", r["F_V"] / 1000, 122.0, "kN", rel=0.02)
    _check(out, "U06.plinski.F_kN", r["F"] / 1000, 172.0, "kN", rel=0.02)
    _check(out, "U06.plinski.alpha_deg", r["alpha_deg"], 45.2, "deg", rel=0.02)
    _check(out, "U06.plinski.F_open_kN", r["F_open"] / 1000, 2.36, "kN", rel=0.03)

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
