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


def integrate(f, lo, hi, n=800):
    """Složeno Simpsonovo pravilo; koristi se neovisno od formula težišta."""
    step = (hi - lo) / n
    return step / 3 * (f(lo) + f(hi) + sum(
        (4 if i % 2 else 2) * f(lo + i * step) for i in range(1, n)))


def task_two_levels(b=1.20, H=3.0, h_left=2.40, h_right=1.20):
    # Moment sile udesno na y>0 je negativan za pozitivnu rotaciju CCW.
    F = RHO_WATER * G * b * (h_left**2 - h_right**2) / 2
    M = -RHO_WATER * G * b * (h_left**3 - h_right**3) / 6
    return {"F": F, "M": M, "y_R": -M / F if F else None, "T": -M / H}


def task_triangle(H=1.50, h0=0.40, limit=12e3, offered=1.20):
    h_c = h0 + 2 * H / 3
    b_max = limit / (RHO_WATER * G * H / 2 * h_c)
    h_cp = h_c + H**2 / (18 * h_c)
    F_offered = RHO_WATER * G * offered * H / 2 * h_c
    return {"b_max": b_max, "h_cp": h_cp, "F_offered": F_offered}


def task_radial_gate(R=0.85, b=1.30, h1=0.60, W=2.40e3, x_g=-0.32):
    # Stvarna lokalna normala od vody na poklopac: (cos(phi), sin(phi)).
    def df(phi):
        return RHO_WATER * G * (h1 + R * math.sin(phi)) * b * R
    F_x = integrate(lambda phi: df(phi) * math.cos(phi), 0, math.pi / 2)
    F_y = integrate(lambda phi: df(phi) * math.sin(phi), 0, math.pi / 2)
    M_water = integrate(lambda phi:
        (-R * math.cos(phi)) * df(phi) * math.sin(phi)
        - (-R * math.sin(phi)) * df(phi) * math.cos(phi), 0, math.pi / 2)
    T = (-x_g * W + M_water) / R
    return {"F_x": F_x, "F_y": F_y, "M_water": M_water,
            "T": T, "R_x": T - F_x, "R_y": W - F_y}


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

    r = task_two_levels()
    _check(out, "U05.CANON.Z3.F_kN", r["F"] / 1000, 25.377, "kN", rel=0.001)
    _check(out, "U05.CANON.Z3.y_R", r["y_R"], 0.9333, "m", rel=0.001)
    _check(out, "U05.CANON.Z3.M_kNm", r["M"] / 1000, -23.685, "kNm", rel=0.001)
    _check(out, "U05.CANON.Z3.T_kN", r["T"] / 1000, 7.895, "kN", rel=0.001)
    q = lambda y: RHO_WATER * G * 1.2 * (max(2.4-y, 0)-max(1.2-y, 0))
    f_num = sum(integrate(q, lo, hi) for lo, hi in [(0,1.2),(1.2,2.4),(2.4,3)])
    m_num = sum(integrate(lambda y: -y*q(y), lo, hi)
                for lo, hi in [(0,1.2),(1.2,2.4),(2.4,3)])
    _invariant(out, "U05.CANON.Z3.pressure_integration", abs(f_num-r["F"]) < 1e-6)
    _invariant(out, "U05.CANON.Z3.moment_balance", abs(m_num+3*r["T"]) < 1e-6)
    equal = task_two_levels(h_left=1.2, h_right=1.2)
    reverse = task_two_levels(h_left=1.2, h_right=2.4)
    _invariant(out, "U05.CANON.Z3.equal_levels", equal["F"] == equal["M"] == equal["T"] == 0)
    _invariant(out, "U05.CANON.Z3.reversed_levels", reverse["F"] == -r["F"] and reverse["T"] == -r["T"])

    r = task_triangle()
    _check(out, "U05.CANON.Z4.b_max", r["b_max"], 1.1673, "m", rel=0.001)
    _check(out, "U05.CANON.Z4.h_cp", r["h_cp"], 1.4893, "m", rel=0.001)
    _check(out, "U05.CANON.Z4.F_offered_kN", r["F_offered"] / 1000, 12.336, "kN", rel=0.001)
    q = lambda depth: RHO_WATER * G * depth * r["b_max"] * (depth-0.4)/1.5
    f_num = integrate(q, 0.4, 1.9)
    h_num = integrate(lambda depth: depth*q(depth), 0.4, 1.9)/f_num
    _invariant(out, "U05.CANON.Z4.triangular_strip_integral", abs(f_num-12000) < 1e-6 and abs(h_num-r["h_cp"]) < 1e-10)
    _invariant(out, "U05.CANON.Z4.offered_rejected", r["F_offered"] > 12000 and r["b_max"] < 1.2)
    _invariant(out, "U05.CANON.Z4.width_scaling", abs(task_triangle(limit=24000)["b_max"]-2*r["b_max"]) < 1e-12 and task_triangle(limit=24000)["h_cp"] == r["h_cp"])
    _invariant(out, "U05.CANON.Z4.surface_limit", abs(task_triangle(h0=0)["h_cp"]-3*1.5/4) < 1e-12)

    r = task_radial_gate()
    _check(out, "U05.CANON.Z5.F_x_kN", r["F_x"] / 1000, 11.089, "kN", rel=0.001)
    _check(out, "U05.CANON.Z5.F_y_kN", r["F_y"] / 1000, 13.713, "kN", rel=0.001)
    _check(out, "U05.CANON.Z5.M_water_kNm", r["M_water"] / 1000, 0, "kNm", rel=1e-9)
    _check(out, "U05.CANON.Z5.T_kN", r["T"] / 1000, 0.904, "kN", rel=0.001)
    _check(out, "U05.CANON.Z5.R_x_kN", r["R_x"] / 1000, -10.185, "kN", rel=0.001)
    _check(out, "U05.CANON.Z5.R_y_kN", r["R_y"] / 1000, -11.313, "kN", rel=0.001)
    analytic = quarter_cylinder(.85, 1.3, .6, 1)
    _invariant(out, "U05.CANON.Z5.projection_and_volume", abs(r["F_x"]-analytic["F_H"]) < 1e-6 and abs(r["F_y"]-analytic["F_V"]) < 1e-6)
    _invariant(out, "U05.CANON.Z5.component_moments_cancel", abs(analytic["F_H"]*(analytic["h_H"]-.6)-analytic["F_V"]*analytic["x_from_wall"]) < 1e-7)
    _invariant(out, "U05.CANON.Z5.support_balances", abs(r["F_x"]+r["R_x"]-r["T"]) < 1e-7 and abs(r["F_y"]+r["R_y"]-2400) < 1e-7 and abs(2400*.32-r["T"]*.85) < 1e-7)
    _invariant(out, "U05.CANON.Z5.tie_capacity", 0 < r["T"] < 1000)
    deeper = task_radial_gate(h1=1.2)
    _invariant(out, "U05.CANON.Z5.depth_changes_support_not_tie", deeper["F_x"] > r["F_x"] and deeper["F_y"] > r["F_y"] and abs(deeper["T"]-r["T"]) < 1e-7)
    _invariant(out, "U05.CANON.Z5.weightless_limit", abs(task_radial_gate(W=0)["T"]) < 1e-7)

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
