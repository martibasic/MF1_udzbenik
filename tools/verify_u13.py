"""Numericka verifikacija U13: Cjevovodi."""
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


def _invariant(out, rid, condition, details=""):
    out.append({
        "id": rid,
        "status": "OK" if condition else "FAIL",
        "details": "" if condition else details,
        "verification": "invariant",
    })


def primjer_1_reynolds(D=0.09, Q=0.018, L=42.0, sum_xi=5.2,
                        lam=0.027, nu=1.0e-6, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    Re = v * D / nu
    vh = v**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    return {"v": v, "Re": Re, "h_l": h_l, "h_loc": h_loc, "h_w": h_w}


def primjer_2_paralelne(Q_tot=0.03, d_1=0.040, d_2=0.080, ratio=1.56):
    A_1 = math.pi * d_1**2 / 4
    A_2 = math.pi * d_2**2 / 4
    # Q_tot = A_1 v_1 + A_2 (ratio v_1) = (A_1 + ratio A_2) v_1
    v_1 = Q_tot / (A_1 + ratio * A_2)
    v_2 = ratio * v_1
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v_2
    return {"v_1": v_1, "v_2": v_2, "Q_1": Q_1, "Q_2": Q_2}


def primjer_3_ispust(D=0.16, L=520.0, H=6.3, Q_0=0.030, L_1C=340.0,
                      Q_2=0.025, p_C_h=1.40, C_d=0.62, g=9.81):
    A = math.pi * D**2 / 4
    v_0 = Q_0 / A
    lam = 2 * g * H * D / (L * v_0**2)
    # H = p_C_h + (1 + lam·L_1C/D)·v_C²/(2g)
    K_AC = 1 + lam * L_1C / D
    vh_C = (H - p_C_h) / K_AC
    v_C = math.sqrt(2 * g * vh_C)
    Q_C = A * v_C
    Q_p = Q_C - Q_2
    A_p = Q_p / (C_d * math.sqrt(2 * g * p_C_h))
    d_p = math.sqrt(4 * A_p / math.pi)
    return {"lam": lam, "Q_C": Q_C, "Q_p": Q_p, "A_p": A_p, "d_p": d_p}


def cjeloviti_1_serijsko_paralelno(D_0=0.10, L_0=28.0, lam_0=0.024, xi_0=1.8,
                                    D_1=0.08, L_1=32.0, lam_1=0.026, xi_1=2.4,
                                    D_2=0.06, L_2=26.0, lam_2=0.028, xi_2=3.1,
                                    D_3=0.10, L_3=18.0, lam_3=0.024, xi_3=1.2,
                                    H=12.0, rho=1000.0, g=9.81):
    K_0 = lam_0 * L_0 / D_0 + xi_0
    K_1 = lam_1 * L_1 / D_1 + xi_1
    K_2 = lam_2 * L_2 / D_2 + xi_2
    K_3 = lam_3 * L_3 / D_3 + xi_3
    A_0 = math.pi * D_0**2 / 4
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    # Iz K_1 v_1² = K_2 v_2² → v_2 = sqrt(K_1/K_2) v_1
    ratio_v2_v1 = math.sqrt(K_1 / K_2)
    # Q = A_1 v_1 + A_2 v_2 = (A_1 + ratio·A_2) v_1
    factor_Q = A_1 + ratio_v2_v1 * A_2
    factor_v0 = factor_Q / A_0  # v_0 = v_3 = factor_v0 · v_1
    # H = K_0·v_0²/(2g) + K_1·v_1²/(2g) + K_3·v_3²/(2g)
    K_total = K_0 * factor_v0**2 + K_1 + K_3 * factor_v0**2
    v_1 = math.sqrt(2 * g * H / K_total)
    v_2 = ratio_v2_v1 * v_1
    Q = factor_Q * v_1
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v_2
    v_0 = Q / A_0
    h_0 = K_0 * v_0**2 / (2 * g)
    h_p = K_1 * v_1**2 / (2 * g)
    h_3 = K_3 * v_0**2 / (2 * g)
    P_gub = rho * g * Q * H
    return {"K_0": K_0, "K_1": K_1, "K_2": K_2, "K_3": K_3,
            "ratio_v2_v1": ratio_v2_v1, "v_1": v_1, "v_2": v_2, "Q": Q,
            "Q_1": Q_1, "Q_2": Q_2, "h_0": h_0, "h_p": h_p,
            "h_3": h_3, "P_gub": P_gub}


def primjer_pec(D=0.10, L=170.0, lam=0.022, sum_xi=13.1, Q=0.025,
                 rho=1000.0, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    vh = v**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    return {"v": v, "h_l": h_l, "h_loc": h_loc, "h_w": h_w}


def primjer_vodovod(D_1=0.150, L_1=250.0, lam_1=0.020, D_2=0.100, L_2=300.0,
                     lam_2=0.018, Q_tot=0.050, g=9.81):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    R_1 = lam_1 * L_1 / D_1 / (2 * g * A_1**2)
    R_2 = lam_2 * L_2 / D_2 / (2 * g * A_2**2)
    ratio = math.sqrt(R_2 / R_1)
    Q_1 = ratio / (ratio + 1) * Q_tot
    Q_2 = Q_tot - Q_1
    h_w = R_1 * Q_1**2
    return {"R_1": R_1, "R_2": R_2, "Q_1": Q_1, "Q_2": Q_2, "h_w": h_w}


def zadatak_1(D=0.075, Q=0.013, L=34.0, sum_xi=4.1, lam=0.026,
               nu=1.0e-6, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    Re = v * D / nu
    vh = v**2 / (2 * g)
    h_w = (lam * L / D + sum_xi) * vh
    return {"v": v, "Re": Re, "h_w": h_w}


def zadatak_2(D=0.018, Q=1.0e-4, nu=1.0e-6, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    Re = v * D / nu
    lam = 64 / Re if Re < 2300 else None
    return {"v": v, "Re": Re, "lam": lam}


def zadatak_3(Q=0.010, D_1=0.080, L_1=28.0, lam_1=0.030, sum_xi_1=2.4,
               D_2=0.060, L_2=16.0, lam_2=0.034, sum_xi_2=3.1, g=9.81):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = Q / A_1
    v_2 = Q / A_2
    h_w_1 = (lam_1 * L_1 / D_1 + sum_xi_1) * v_1**2 / (2 * g)
    h_w_2 = (lam_2 * L_2 / D_2 + sum_xi_2) * v_2**2 / (2 * g)
    return {"h_w_total": h_w_1 + h_w_2}


def zadatak_4(K=68.0, h_w=5.4, D=0.090, g=9.81):
    v = math.sqrt(2 * g * h_w / K)
    A = math.pi * D**2 / 4
    Q = A * v
    return {"v": v, "Q": Q}


def zadatak_5(R_1=1450.0, R_2=2400.0, Q_tot=0.032):
    ratio = math.sqrt(R_2 / R_1)
    Q_1 = ratio / (ratio + 1) * Q_tot
    Q_2 = Q_tot - Q_1
    h_w = R_1 * Q_1**2
    return {"Q_1": Q_1, "Q_2": Q_2, "h_w": h_w}


def zadatak_6(D_0=0.100, L_0=20.0, lam_0=0.025, xi_0=1.6,
               D_1=0.080, L_1=24.0, lam_1=0.028, xi_1=2.0,
               D_2=0.060, L_2=18.0, lam_2=0.030, xi_2=2.6,
               D_3=0.100, L_3=14.0, lam_3=0.025, xi_3=1.0,
               H=9.5, g=9.81):
    K_0 = lam_0 * L_0 / D_0 + xi_0
    K_1 = lam_1 * L_1 / D_1 + xi_1
    K_2 = lam_2 * L_2 / D_2 + xi_2
    K_3 = lam_3 * L_3 / D_3 + xi_3
    A_0 = math.pi * D_0**2 / 4
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    ratio = math.sqrt(K_1 / K_2)
    factor_Q = A_1 + ratio * A_2
    factor_v0 = factor_Q / A_0
    K_total = K_0 * factor_v0**2 + K_1 + K_3 * factor_v0**2
    v_1 = math.sqrt(2 * g * H / K_total)
    Q = factor_Q * v_1
    Q_1 = A_1 * v_1
    Q_2 = A_2 * ratio * v_1
    return {
        "ratio_v2_v1": ratio,
        "ratio_v1_v2": 1 / ratio,
        "Q": Q,
        "Q_1": Q_1,
        "Q_2": Q_2,
    }


# ------------ Faza 1.5 dodatak: Radna tocka crpka-cjevovod (CH T4) ----------------
def cjeloviti_2_radna_tocka(H_0=25.0, a_p=0.0175,
                              dz=6.0, L=40.0, D=0.080,
                              lam=0.022, sum_xi_0=4.0,
                              xi_vent=8.0, rho=1000.0, eta=0.75, g=9.81):
    A = math.pi * D**2 / 4
    # Koeficijent karakteristike sustava (s Q u L/s):
    # H_s = dz + (lam L/D + sum_xi) * v^2/(2g)
    # v^2/(2g) = (Q/A)^2/(2g) = c2 * Q_m3s^2 = c2 * 1e-6 * Q_Ls^2
    c2 = 1 / (2 * g * A**2)  # m * s^2/m^6
    # Otvoren ventil:
    K_0 = lam * L / D + sum_xi_0
    coef_0 = K_0 * c2 * 1e-6  # m/(L/s)^2
    Q_0_Ls = math.sqrt((H_0 - dz) / (a_p + coef_0))
    H_op_0 = H_0 - a_p * Q_0_Ls**2
    Q_0 = Q_0_Ls * 1e-3
    P_el_0 = rho * g * Q_0 * H_op_0 / eta
    # Zatvoren ventil:
    K_1 = lam * L / D + sum_xi_0 + xi_vent
    coef_1 = K_1 * c2 * 1e-6
    Q_1_Ls = math.sqrt((H_0 - dz) / (a_p + coef_1))
    H_op_1 = H_0 - a_p * Q_1_Ls**2
    Q_1 = Q_1_Ls * 1e-3
    v_1 = Q_1 / A
    h_vent = xi_vent * v_1**2 / (2 * g)
    P_disip_vent = rho * g * Q_1 * h_vent
    P_el_1 = rho * g * Q_1 * H_op_1 / eta
    return {"Q_op_1_Ls": Q_0_Ls, "H_op_1": H_op_0, "P_el_1": P_el_0,
            "Q_op_2_Ls": Q_1_Ls, "H_op_2": H_op_1, "P_el_2": P_el_1,
            "h_vent": h_vent, "P_disip_vent": P_disip_vent}


def verify():
    out = []

    r = primjer_1_reynolds()
    _check(out, "U13.P1.v", r["v"], 2.83, "m/s", rel=0.02)
    _check(out, "U13.P1.Re", r["Re"], 2.55e5, "", rel=0.02)
    _check(out, "U13.P1.h_l", r["h_l"], 5.14, "m", rel=0.02)
    _check(out, "U13.P1.h_w", r["h_w"], 7.26, "m", rel=0.02)

    r = primjer_2_paralelne()
    _check(out, "U13.P2.v_1", r["v_1"], 3.29, "m/s", rel=0.02)
    _check(out, "U13.P2.v_2", r["v_2"], 5.14, "m/s", rel=0.02)
    _check(out, "U13.P2.Q_1_Ls", r["Q_1"] * 1000, 4.14, "L/s", rel=0.02)
    _check(out, "U13.P2.Q_2_Ls", r["Q_2"] * 1000, 25.9, "L/s", rel=0.02)

    r = primjer_3_ispust()
    _check(out, "U13.P3.lam", r["lam"], 0.0171, "", rel=0.02)
    _check(out, "U13.P3.Q_C_Ls", r["Q_C"] * 1000, 32.3, "L/s", rel=0.02)
    _check(out, "U13.P3.Q_p_Ls", r["Q_p"] * 1000, 7.3, "L/s", rel=0.05)
    _check(out, "U13.P3.d_p_mm", r["d_p"] * 1000, 53.5, "mm", rel=0.05)

    r = cjeloviti_1_serijsko_paralelno()
    _check(out, "U13.CH1.K_0", r["K_0"], 8.52, "", rel=0.02)
    _check(out, "U13.CH1.K_1", r["K_1"], 12.8, "", rel=0.02)
    _check(out, "U13.CH1.K_2", r["K_2"], 15.23, "", rel=0.02)
    _check(out, "U13.CH1.ratio", r["ratio_v2_v1"], 0.917, "", rel=0.02)
    _check(out, "U13.CH1.v_1", r["v_1"], 3.01, "m/s", rel=0.02)
    _check(out, "U13.CH1.Q_Ls", r["Q"] * 1000, 22.9, "L/s", rel=0.02)
    _check(out, "U13.CH1.Q_1_Ls", r["Q_1"] * 1000, 15.1, "L/s", rel=0.02)
    _check(out, "U13.CH1.h_0", r["h_0"], 3.70, "m", rel=0.02)
    _check(out, "U13.CH1.h_p", r["h_p"], 5.91, "m", rel=0.02)
    _check(out, "U13.CH1.h_3", r["h_3"], 2.40, "m", rel=0.02)
    _check(out, "U13.CH1.P_gub_kW", r["P_gub"] / 1000, 2.70, "kW", rel=0.02)

    r = primjer_pec()
    _check(out, "U13.pec.h_w", r["h_w"], 26.07, "m", rel=0.02)

    r = primjer_vodovod()
    _check(out, "U13.vodovod.Q_1_Ls", r["Q_1"] * 1000, 37.04, "L/s", rel=0.02)
    _check(out, "U13.vodovod.Q_2_Ls", r["Q_2"] * 1000, 12.96, "L/s", rel=0.02)
    _check(out, "U13.vodovod.h_w", r["h_w"], 7.47, "m", rel=0.02)

    r = zadatak_1()
    _check(out, "U13.Z1.v", r["v"], 2.94, "m/s", rel=0.02)
    _check(out, "U13.Z1.Re", r["Re"], 2.2e5, "", rel=0.03)
    _check(out, "U13.Z1.h_w", r["h_w"], 7.0, "m", rel=0.03)

    r = zadatak_2()
    _check(out, "U13.Z2.v", r["v"], 0.393, "m/s", rel=0.02)
    _check(out, "U13.Z2.Re", r["Re"], 7100.0, "", rel=0.02)
    _invariant(
        out,
        "U13.Z2.turbulent_model_choice",
        r["Re"] > 4000 and r["lam"] is None,
        "Za Re>4000 verifier ne smije primijeniti lambda=64/Re.",
    )

    r = zadatak_3()
    _check(out, "U13.Z3.h_w_total", r["h_w_total"], 10.4, "m", rel=0.03)

    r = zadatak_4()
    _check(out, "U13.Z4.v", r["v"], 1.25, "m/s", rel=0.02)
    _check(out, "U13.Z4.Q_Ls", r["Q"] * 1000, 7.9, "L/s", rel=0.03)

    r = zadatak_5()
    _check(out, "U13.Z5.Q_1_Ls", r["Q_1"] * 1000, 18.0, "L/s", rel=0.02)
    _check(out, "U13.Z5.Q_2_Ls", r["Q_2"] * 1000, 14.0, "L/s", rel=0.02)
    _check(out, "U13.Z5.h_w", r["h_w"], 0.47, "m", rel=0.03)

    r = zadatak_6()
    _check(out, "U13.Z6.ratio_v1_v2", r["ratio_v1_v2"], 1.06, "", rel=0.02)
    _check(out, "U13.Z6.Q_Ls", r["Q"] * 1000, 22.9, "L/s", rel=0.02)
    _check(out, "U13.Z6.Q_1_Ls", r["Q_1"] * 1000, 14.9, "L/s", rel=0.03)
    _check(out, "U13.Z6.Q_2_Ls", r["Q_2"] * 1000, 8.0, "L/s", rel=0.03)

    # Faza 1.5: Radna tocka crpka-cjevovod (CH T4)
    r = cjeloviti_2_radna_tocka()
    _check(out, "U13.CH2.Q_op_1_Ls", r["Q_op_1_Ls"], 19.94, "L/s", rel=0.02)
    _check(out, "U13.CH2.H_op_1", r["H_op_1"], 18.04, "m", rel=0.02)
    _check(out, "U13.CH2.P_el_1_kW", r["P_el_1"] / 1000, 4.70, "kW", rel=0.02)
    _check(out, "U13.CH2.Q_op_2_Ls", r["Q_op_2_Ls"], 17.24, "L/s", rel=0.02)
    _check(out, "U13.CH2.H_op_2", r["H_op_2"], 19.80, "m", rel=0.02)
    _check(out, "U13.CH2.h_vent_m", r["h_vent"], 4.80, "m", rel=0.03)
    _check(out, "U13.CH2.P_disip_vent_kW", r["P_disip_vent"] / 1000, 0.81, "kW", rel=0.03)
    _check(out, "U13.CH2.P_el_2_kW", r["P_el_2"] / 1000, 4.46, "kW", rel=0.02)

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
