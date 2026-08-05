"""Neovisna numerička provjera kanonskoga U05: ravne i zakrivljene plohe.

Modul ponovno računa šest javnih primjera i šest zadataka iz
``source/u05_hidrostatske_sile_na_plohe.md``. Očekivanja su objavljene,
zaokružene vrijednosti; nijedna se vrijednost ne uspoređuje sa samom sobom.
"""

from __future__ import annotations

import math


TOL = 0.01
G = 9.81
RHO_WATER = 998.0


def _close(value: float, target: float, rel: float = TOL) -> bool:
    if target == 0:
        return abs(value) <= rel
    return abs(value - target) / abs(target) <= rel


def _check(out, rid, value, target, unit="", rel=TOL):
    ok = _close(value, target, rel)
    out.append(
        {
            "id": rid,
            "status": "OK" if ok else "FAIL",
            "details": "" if ok else f"{value:.6g} vs {target:.6g} {unit}".strip(),
            "verification": "golden",
        }
    )


def _invariant(out, rid, condition, details=""):
    out.append(
        {
            "id": rid,
            "status": "OK" if condition else "FAIL",
            "details": "" if condition else details,
            "verification": "invariant",
        }
    )


def rectangular_gate(b, H, h1, rho=RHO_WATER, g=G):
    A = b * H
    h_c = h1 + H / 2
    I_g = b * H**3 / 12
    F = rho * g * A * h_c
    h_cp = h_c + I_g / (A * h_c)
    return {"A": A, "h_c": h_c, "I_g": I_g, "F": F, "h_cp": h_cp}


def inclined_gate(b, L, h1, theta_deg, rho=RHO_WATER, g=G):
    sin_theta = math.sin(math.radians(theta_deg))
    A = b * L
    h_c = h1 + L * sin_theta / 2
    F = rho * g * A * h_c
    numerator = h1 * L**2 / 2 + sin_theta * L**3 / 3
    denominator = h1 * L + sin_theta * L**2 / 2
    s_cp = numerator / denominator
    M = F * s_cp
    return {"A": A, "h_c": h_c, "F": F, "s_cp": s_cp, "M": M, "T": M / L}


def layered_wall(b, rho_o, h_o, rho_w, h_w, g=G):
    F1 = 0.5 * rho_o * g * b * h_o**2
    F2_rect = rho_o * g * b * h_o * h_w
    F2_tri = 0.5 * rho_w * g * b * h_w**2
    F = F1 + F2_rect + F2_tri
    M = (
        F1 * (2 * h_o / 3)
        + F2_rect * (h_o + h_w / 2)
        + F2_tri * (h_o + 2 * h_w / 3)
    )
    depth = h_o + h_w
    T = M / depth
    return {
        "F1": F1,
        "F2_rect": F2_rect,
        "F2_tri": F2_tri,
        "F": F,
        "M": M,
        "h_cp": M / F,
        "T": T,
        "R_A": F - T,
    }


def quarter_cylinder(R, b, h1, vertical_sign, rho=RHO_WATER, g=G):
    A_x = R * b
    h_cx = h1 + R / 2
    I_g = b * R**3 / 12
    F_H = rho * g * A_x * h_cx
    h_H = h_cx + I_g / (A_x * h_cx)
    V_rect = h1 * R * b
    V_quarter = math.pi * R**2 * b / 4
    V = V_rect + V_quarter
    F_V = vertical_sign * rho * g * V
    x_from_wall = (
        V_rect * (R / 2) + V_quarter * (4 * R / (3 * math.pi))
    ) / V
    F_R = math.hypot(F_H, F_V)
    angle = math.degrees(math.atan2(F_V, F_H))
    return {
        "A_x": A_x,
        "h_cx": h_cx,
        "I_g": I_g,
        "F_H": F_H,
        "h_H": h_H,
        "V_rect": V_rect,
        "V_quarter": V_quarter,
        "V": V,
        "F_V": F_V,
        "x_from_wall": x_from_wall,
        "F_R": F_R,
        "angle": angle,
    }


def example_hinged_quarter(R=1.10, b=1.40, rho=RHO_WATER, g=G):
    r = quarter_cylinder(R, b, h1=0.0, vertical_sign=1, rho=rho, g=g)
    x_from_hinge = R - 4 * R / (3 * math.pi)
    T = (r["F_H"] * r["h_H"] + r["F_V"] * x_from_hinge) / R
    return {**r, "x_from_hinge": x_from_hinge, "T": T}


def task_hinged_quarter(R=0.75, b=1.10, h1=0.45, rho=RHO_WATER, g=G):
    r = quarter_cylinder(R, b, h1, vertical_sign=-1, rho=rho, g=g)
    horizontal_arm = r["h_H"] - h1
    # Težište pomoćnoga volumena mjereno od lijevoga vertikalnog zatvaranja;
    # krak prema zglobu u gornjoj desnoj točki jest R-x.
    vertical_arm = R - r["x_from_wall"]
    T = (r["F_H"] * horizontal_arm + abs(r["F_V"]) * vertical_arm) / R
    return {**r, "horizontal_arm": horizontal_arm, "vertical_arm": vertical_arm, "T": T}


def task_uncertainty(
    b=1.20,
    H=0.80,
    h1=0.90,
    u_h1=0.020,
    rho=998.0,
    u_rho=3.0,
    F_m=11.60e3,
    u_Fm=0.30e3,
    g=G,
):
    F = rho * g * b * H * (h1 + H / 2)
    relative_u = math.sqrt((u_rho / rho) ** 2 + (u_h1 / (h1 + H / 2)) ** 2)
    u_F = F * relative_u
    u_delta = math.hypot(u_F, u_Fm)
    z = abs(F - F_m) / u_delta
    return {"F": F, "u_F": u_F, "u_delta": u_delta, "z": z}


def verify():
    out = []

    r = rectangular_gate(2.0, 3.0, 2.0)
    _check(out, "U05.CANON.P1.A", r["A"], 6.0, "m2")
    _check(out, "U05.CANON.P1.h_c", r["h_c"], 3.5, "m")
    _check(out, "U05.CANON.P1.I_g", r["I_g"], 4.50, "m4")
    _check(out, "U05.CANON.P1.F_kN", r["F"] / 1000, 205.6, "kN", rel=0.02)
    _check(out, "U05.CANON.P1.h_cp", r["h_cp"], 3.714, "m", rel=0.02)
    _check(out, "U05.CANON.P1.offset", r["h_cp"] - 2.0, 1.714, "m", rel=0.02)
    _check(out, "U05.CANON.P1.p_top_kPa", RHO_WATER * G * 2.0 / 1000, 19.58, "kPa")
    _check(out, "U05.CANON.P1.p_bottom_kPa", RHO_WATER * G * 5.0 / 1000, 48.95, "kPa")

    r = inclined_gate(0.90, 1.20, 0.80, 60.0)
    _check(out, "U05.CANON.P2.A", r["A"], 1.08, "m2")
    _check(out, "U05.CANON.P2.h_c", r["h_c"], 1.3196, "m", rel=0.02)
    _check(out, "U05.CANON.P2.F_kN", r["F"] / 1000, 13.95, "kN", rel=0.02)
    _check(out, "U05.CANON.P2.s_cp", r["s_cp"], 0.679, "m", rel=0.02)
    _check(out, "U05.CANON.P2.M_kNm", r["M"] / 1000, 9.47, "kNm", rel=0.02)
    _check(out, "U05.CANON.P2.T_kN", r["T"] / 1000, 7.89, "kN", rel=0.02)

    r = layered_wall(1.40, 820.0, 1.00, 1000.0, 1.80)
    _check(out, "U05.CANON.P3.F1_kN", r["F1"] / 1000, 5.631, "kN", rel=0.02)
    _check(out, "U05.CANON.P3.F2_rect_kN", r["F2_rect"] / 1000, 20.271, "kN", rel=0.02)
    _check(out, "U05.CANON.P3.F2_tri_kN", r["F2_tri"] / 1000, 22.249, "kN", rel=0.02)
    _check(out, "U05.CANON.P3.F_kN", r["F"] / 1000, 48.151, "kN", rel=0.02)
    _check(out, "U05.CANON.P3.M_kNm", r["M"] / 1000, 91.218, "kNm", rel=0.02)
    _check(out, "U05.CANON.P3.h_cp", r["h_cp"], 1.894, "m", rel=0.02)
    _check(out, "U05.CANON.P3.T_kN", r["T"] / 1000, 32.578, "kN", rel=0.02)
    _check(out, "U05.CANON.P3.R_A_kN", r["R_A"] / 1000, 15.574, "kN", rel=0.02)

    r = quarter_cylinder(1.22, 1.83, 2.44, vertical_sign=1)
    _check(out, "U05.CANON.P4.A_x", r["A_x"], 2.233, "m2", rel=0.02)
    _check(out, "U05.CANON.P4.h_cx", r["h_cx"], 3.05, "m", rel=0.02)
    _check(out, "U05.CANON.P4.F_H_kN", r["F_H"] / 1000, 66.67, "kN", rel=0.02)
    _check(out, "U05.CANON.P4.h_H", r["h_H"], 3.091, "m", rel=0.02)
    _check(out, "U05.CANON.P4.V", r["V"], 7.587, "m3", rel=0.02)
    _check(out, "U05.CANON.P4.F_V_kN", r["F_V"] / 1000, 74.28, "kN", rel=0.02)
    _check(out, "U05.CANON.P4.x_V", r["x_from_wall"], 0.584, "m", rel=0.02)
    _check(out, "U05.CANON.P4.F_R_kN", r["F_R"] / 1000, 99.81, "kN", rel=0.02)
    _check(out, "U05.CANON.P4.angle", r["angle"], 48.1, "deg", rel=0.02)

    r = quarter_cylinder(0.90, 1.20, 0.0, vertical_sign=-1)
    _check(out, "U05.CANON.P5.F_H_kN", r["F_H"] / 1000, 4.758, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.h_H", r["h_H"], 0.600, "m", rel=0.02)
    _check(out, "U05.CANON.P5.V", r["V"], 0.7634, "m3", rel=0.02)
    _check(out, "U05.CANON.P5.F_V_kN", r["F_V"] / 1000, -7.474, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.x_V", r["x_from_wall"], 0.382, "m", rel=0.02)
    _check(out, "U05.CANON.P5.F_R_kN", r["F_R"] / 1000, 8.860, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.angle", r["angle"], -57.52, "deg", rel=0.02)
    _check(out, "U05.CANON.P5.ratio", abs(r["F_V"]) / r["F_H"], math.pi / 2, "", rel=0.01)

    r = example_hinged_quarter()
    _check(out, "U05.CANON.P6.F_H_kN", r["F_H"] / 1000, 8.292, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.h_H", r["h_H"], 0.733, "m", rel=0.02)
    _check(out, "U05.CANON.P6.F_V_kN", r["F_V"] / 1000, 13.026, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.x_arm", r["x_from_hinge"], 0.633, "m", rel=0.02)
    _check(out, "U05.CANON.P6.F_R_kN", r["F_R"] / 1000, 15.441, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.angle", r["angle"], 57.52, "deg", rel=0.02)
    _check(out, "U05.CANON.P6.T_kN", r["T"] / 1000, 13.026, "kN", rel=0.02)

    r = rectangular_gate(1.40, 1.80, 1.10)
    _check(out, "U05.CANON.Z1.F_kN", r["F"] / 1000, 49.34, "kN", rel=0.02)
    _check(out, "U05.CANON.Z1.h_cp", r["h_cp"], 2.135, "m", rel=0.02)
    _check(out, "U05.CANON.Z1.offset", r["h_cp"] - 1.10, 1.035, "m", rel=0.02)

    r = quarter_cylinder(0.65, 1.20, 1.10, vertical_sign=1)
    _check(out, "U05.CANON.Z2.F_H_kN", r["F_H"] / 1000, 10.88, "kN", rel=0.02)
    _check(out, "U05.CANON.Z2.F_V_kN", r["F_V"] / 1000, 12.30, "kN", rel=0.02)
    _check(out, "U05.CANON.Z2.F_R_kN", r["F_R"] / 1000, 16.42, "kN", rel=0.02)

    r = inclined_gate(0.80, 1.00, 0.90, 40.0)
    _check(out, "U05.CANON.Z3.F_kN", r["F"] / 1000, 9.566, "kN", rel=0.02)
    _check(out, "U05.CANON.Z3.s_cp", r["s_cp"], 0.5439, "m", rel=0.02)
    _check(out, "U05.CANON.Z3.T_kN", r["T"] / 1000, 5.203, "kN", rel=0.02)

    r = layered_wall(1.80, 820.0, 0.90, 998.0, 1.50)
    _check(out, "U05.CANON.Z4.F_kN", r["F"] / 1000, 45.24, "kN", rel=0.02)
    _check(out, "U05.CANON.Z4.h_cp", r["h_cp"], 1.623, "m", rel=0.02)

    r = task_hinged_quarter()
    _check(out, "U05.CANON.Z5.F_H_kN", r["F_H"] / 1000, 6.664, "kN", rel=0.02)
    _check(out, "U05.CANON.Z5.h_H", r["h_H"], 0.8818, "m", rel=0.02)
    _check(out, "U05.CANON.Z5.horizontal_arm", r["horizontal_arm"], 0.4318, "m", rel=0.02)
    _check(out, "U05.CANON.Z5.F_V_kN", r["F_V"] / 1000, -8.392, "kN", rel=0.02)
    _check(out, "U05.CANON.Z5.vertical_arm", r["vertical_arm"], 0.4071, "m", rel=0.02)
    _check(out, "U05.CANON.Z5.F_R_kN", r["F_R"] / 1000, 10.72, "kN", rel=0.02)
    _check(out, "U05.CANON.Z5.T_kN", r["T"] / 1000, 8.392, "kN", rel=0.02)

    r = task_uncertainty()
    _check(out, "U05.CANON.Z6.F_kN", r["F"] / 1000, 12.218, "kN", rel=0.02)
    _check(out, "U05.CANON.Z6.u_F_kN", r["u_F"] / 1000, 0.192, "kN", rel=0.02)
    _check(out, "U05.CANON.Z6.u_delta_kN", r["u_delta"] / 1000, 0.356, "kN", rel=0.02)
    _check(out, "U05.CANON.Z6.z", r["z"], 1.74, "", rel=0.02)
    _invariant(out, "U05.CANON.Z6.no_2u_disagreement", r["z"] < 2.0, "Z mora biti manji od 2.")

    return out


if __name__ == "__main__":
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:42s} {result.get('details', '')}")
    print(f"Total: ok={sum(r['status'] == 'OK' for r in results)}, "
          f"fail={sum(r['status'] != 'OK' for r in results)}")
