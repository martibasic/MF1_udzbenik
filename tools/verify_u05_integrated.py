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


def quarter_cylinder(R, b, h1, vertical_sign, rho=RHO_WATER, g=G, p_gas=0.0):
    """Četvrtina valjka; ``p_gas`` je jednoliki manometarski nadtlak plina
    iznad slobodne površine koji se ne poništava sa suhe strane (P5)."""
    A_x = R * b
    h_cx = h1 + R / 2
    I_g = b * R**3 / 12
    F_H_h = rho * g * A_x * h_cx
    h_H_h = h_cx + I_g / (A_x * h_cx)
    F_H_p = p_gas * A_x
    F_H = F_H_h + F_H_p
    h_H = (F_H_h * h_H_h + F_H_p * h_cx) / F_H
    V_rect = h1 * R * b
    V_quarter = math.pi * R**2 * b / 4
    V = V_rect + V_quarter
    F_V_h = rho * g * V
    x_h = (V_rect * (R / 2) + V_quarter * (4 * R / (3 * math.pi))) / V
    F_V_p = p_gas * R * b
    F_V = vertical_sign * (F_V_h + F_V_p)
    x_from_wall = (F_V_h * x_h + F_V_p * R / 2) / (F_V_h + F_V_p)
    F_R = math.hypot(F_H, F_V)
    angle = math.degrees(math.atan2(F_V, F_H))
    return {
        "A_x": A_x,
        "h_cx": h_cx,
        "I_g": I_g,
        "F_H_h": F_H_h,
        "F_H_p": F_H_p,
        "F_H": F_H,
        "h_H": h_H,
        "V_rect": V_rect,
        "V_quarter": V_quarter,
        "V": V,
        "F_V_h": F_V_h,
        "F_V_p": F_V_p,
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


def task_watertight_door(b=0.80, H=1.60, h1=1.40, rho=1025.0, g=G):
    """Z1: vrata sa šarkama na jednom i dva zasuna na drugom okomitom rubu."""
    r = rectangular_gate(b, H, h1, rho=rho, g=g)
    M_hinge = r["F"] * b / 2          # tlak ne ovisi o vodoravnom položaju
    dogs_total = r["F"] / 2
    arm = r["h_cp"] - h1
    dog_lower = dogs_total * arm / H
    dog_upper = dogs_total - dog_lower
    return {**r, "M_hinge": M_hinge, "dogs_total": dogs_total,
            "offset": arm, "dog_lower": dog_lower, "dog_upper": dog_upper}


def task_parabolic_cover(b=1.50, L=1.20, H=0.90, rho=RHO_WATER, g=G, n=2000):
    """Z2: parabola z=-H(x/L)^2 s tjemenom A na slobodnoj površini uz stijenku.

    Voda kvasi gornju stranu; normala iz fluida u pokrov je (z', -1)/sqrt(1+z'^2).
    Vraća analitičke vrijednosti i neovisnu numeričku integraciju p n dA.
    """
    F_x = -rho * g * b * H**2 / 2
    F_z = -rho * g * b * H * L / 3
    depth_x = 2 * H / 3
    x_z = 3 * L / 4
    M_A = -(abs(F_x) * depth_x + abs(F_z) * x_z)   # oba doprinosa u smjeru kazaljke
    z = lambda x: -H * (x / L) ** 2
    dz = lambda x: -2 * H * x / L**2
    p = lambda x: rho * g * (-z(x))
    F_x_num = integrate(lambda x: p(x) * dz(x) * b, 0, L, n)
    F_z_num = integrate(lambda x: -p(x) * b, 0, L, n)
    M_num = integrate(lambda x: x * (-p(x) * b) - z(x) * (p(x) * dz(x) * b), 0, L, n)
    F_R = math.hypot(F_x, F_z)
    return {"F_x": F_x, "F_z": F_z, "depth_x": depth_x, "x_z": x_z, "F_R": F_R,
            "M_A": M_A, "F_x_num": F_x_num, "F_z_num": F_z_num, "M_num": M_num}


def parabola_normal_intersection(L, H, x1, x2):
    """Sjecište normala parabole z=-H(x/L)^2 u točkama x1 i x2."""
    def normal(x):
        zp = -2 * H * x / L**2
        return (x, -H * (x / L) ** 2), (zp, -1.0)   # točka, smjer normale
    (px, pz), (dx1, dz1) = normal(x1)
    (qx, qz), (dx2, dz2) = normal(x2)
    det = dx1 * (-dz2) - dz1 * (-dx2)
    t = ((qx - px) * (-dz2) - (qz - pz) * (-dx2)) / det
    return px + t * dx1, pz + t * dz1


def task_flap_gate(b=1.50, L=2.00, theta_deg=60.0, a=0.80, y=1.80, rho=RHO_WATER, g=G):
    """Z3: kosa zaklopka s osi na udaljenosti ``a`` uzduž ploče od donjeg ruba.

    Otvara se kad centar tlaka dođe u os. Za djelomično uronjenu ploču hvatište je
    na trećini omočene duljine, pa uvjet traži omočenu duljinu 3a; ako je 3a > L,
    otvaranje nastupa tek pri potpunom uronjenju i rješava se po h_C.
    Vraća i stanje pri zadanoj dubini ``y`` (sila, hvatište, moment, sila praga).
    """
    s = math.sin(math.radians(theta_deg))
    wetted_open = 3 * a
    if wetted_open <= L:
        y_open = wetted_open * s
        h_c_open = y_open / 2
        fully_submerged = False
    else:
        h_c_open = L**2 * s / (12 * (L / 2 - a))
        y_open = h_c_open + L * s / 2
        fully_submerged = True
    A = b * L
    h_c = y - L * s / 2
    F = rho * g * A * h_c
    I_g = b * L**3 / 12
    shift = I_g * s / (A * h_c)        # y_CP - y_C uzduž ploče
    s_cp = L / 2 - shift               # hvatište od donjeg ruba
    M_axis = F * (a - s_cp)            # pozitivno: donji rub pritisnut na prag
    R_sill = M_axis / a
    return {"y_open": y_open, "h_c_open": h_c_open, "top_depth_open": y_open - L * s,
            "fully_submerged": fully_submerged, "wetted_open": wetted_open,
            "A": A, "h_c": h_c, "F": F, "shift": shift, "s_cp": s_cp,
            "M_axis": M_axis, "R_sill": R_sill, "s_centroid": L / 2}


def flap_gate_numeric(y, b=1.50, L=2.00, theta_deg=60.0, a=0.80, rho=RHO_WATER, g=G, n=4000):
    """Neovisna integracija tlaka po omočenom dijelu ploče: sila i moment oko osi."""
    s = math.sin(math.radians(theta_deg))
    wet = min(L, y / s)
    F = integrate(lambda u: rho * g * (y - u * s) * b, 0, wet, n)
    M = integrate(lambda u: rho * g * (y - u * s) * b * (a - u), 0, wet, n)
    return F, M


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
    _check(out, "U05.CANON.P4.moment_about_O_kNm", r["F_H"] * (r["h_H"] - 2.44) / 1000, 43.4, "kNm", rel=0.005)
    _invariant(out, "U05.CANON.P4.resultant_through_centre",
               abs(r["F_H"] * (r["h_H"] - 2.44) - r["F_V"] * r["x_from_wall"]) < 1e-6,
               "Rezultanta kružnog luka mora prolaziti kroz O.")

    r = quarter_cylinder(0.90, 1.20, 0.0, vertical_sign=-1, p_gas=20e3)
    _check(out, "U05.CANON.P5.F_H_h_kN", r["F_H_h"] / 1000, 4.758, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.F_H_p_kN", r["F_H_p"] / 1000, 21.60, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.F_H_kN", r["F_H"] / 1000, 26.36, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.h_H", r["h_H"], 0.477, "m", rel=0.02)
    _check(out, "U05.CANON.P5.V", r["V"], 0.7634, "m3", rel=0.02)
    _check(out, "U05.CANON.P5.F_V_h_kN", r["F_V_h"] / 1000, 7.474, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.F_V_kN", r["F_V"] / 1000, -29.07, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.x_V", r["x_from_wall"], 0.432, "m", rel=0.02)
    _check(out, "U05.CANON.P5.F_R_kN", r["F_R"] / 1000, 39.24, "kN", rel=0.02)
    _check(out, "U05.CANON.P5.angle", r["angle"], -47.8, "deg", rel=0.02)
    _check(out, "U05.CANON.P5.moment_about_O_kNm", r["F_H"] * r["h_H"] / 1000, 12.58, "kNm", rel=0.02)
    _invariant(out, "U05.CANON.P5.resultant_through_O",
               abs(r["F_H"] * r["h_H"] - abs(r["F_V"]) * r["x_from_wall"]) < 1e-6,
               "Rezultanta kružnog luka mora prolaziti kroz O i uz nadtlak plina.")
    open_tank = quarter_cylinder(0.90, 1.20, 0.0, vertical_sign=-1)
    _check(out, "U05.CANON.P5.open_h_H", open_tank["h_H"], 0.600, "m", rel=0.02)
    _check(out, "U05.CANON.P5.open_x_V", open_tank["x_from_wall"], 0.382, "m", rel=0.02)
    _check(out, "U05.CANON.P5.open_ratio", abs(open_tank["F_V"]) / open_tank["F_H"], math.pi / 2, "", rel=0.01)
    _invariant(out, "U05.CANON.P5.gas_moves_centres_towards_centroids",
               open_tank["h_H"] > r["h_H"] > 0.45 and open_tank["x_from_wall"] < r["x_from_wall"] < 0.45,
               "Jednoliki nadtlak mora pomaknuti hvatišta prema težištima projekcija.")

    def arc_integrals(p_gas, R=0.90, b=1.20, n=4000):
        # Neovisna integracija p n dA po luku s p = p_pl + rho g h.
        fh = integrate(lambda ph: (p_gas + RHO_WATER * G * R * math.sin(ph)) * math.cos(ph) * b * R, 0, math.pi / 2, n)
        fv = integrate(lambda ph: (p_gas + RHO_WATER * G * R * math.sin(ph)) * (-math.sin(ph)) * b * R, 0, math.pi / 2, n)
        return fh, fv
    fh, fv = arc_integrals(20e3)
    _invariant(out, "U05.CANON.P5.direct_integration",
               abs(fh - r["F_H"]) < 1e-3 and abs(fv - r["F_V"]) < 1e-3,
               "Integral p n dA po luku ne vraća projekciju i pomoćni volumen s nadtlakom.")

    r = example_hinged_quarter()
    _check(out, "U05.CANON.P6.F_H_kN", r["F_H"] / 1000, 8.292, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.h_H", r["h_H"], 0.733, "m", rel=0.02)
    _check(out, "U05.CANON.P6.F_V_kN", r["F_V"] / 1000, 13.026, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.x_arm", r["x_from_hinge"], 0.633, "m", rel=0.02)
    _check(out, "U05.CANON.P6.F_R_kN", r["F_R"] / 1000, 15.441, "kN", rel=0.02)
    _check(out, "U05.CANON.P6.angle", r["angle"], 57.52, "deg", rel=0.02)
    _check(out, "U05.CANON.P6.T_kN", r["T"] / 1000, 13.026, "kN", rel=0.02)

    r = task_watertight_door()
    _check(out, "U05.CANON.Z1.F_kN", r["F"] / 1000, 28.31, "kN", rel=0.001)
    _check(out, "U05.CANON.Z1.h_cp", r["h_cp"], 2.297, "m", rel=0.001)
    _check(out, "U05.CANON.Z1.offset", r["offset"], 0.897, "m", rel=0.001)
    _check(out, "U05.CANON.Z1.M_hinge_kNm", r["M_hinge"] / 1000, 11.33, "kNm", rel=0.001)
    _check(out, "U05.CANON.Z1.dogs_total_kN", r["dogs_total"] / 1000, 14.16, "kN", rel=0.001)
    _check(out, "U05.CANON.Z1.dog_lower_kN", r["dog_lower"] / 1000, 7.94, "kN", rel=0.001)
    _check(out, "U05.CANON.Z1.dog_upper_kN", r["dog_upper"] / 1000, 6.22, "kN", rel=0.001)
    q = lambda depth: 1025.0 * G * depth * 0.80
    f_num = integrate(q, 1.40, 3.00)
    h_num = integrate(lambda depth: depth * q(depth), 1.40, 3.00) / f_num
    _invariant(out, "U05.CANON.Z1.pressure_integration",
               abs(f_num - r["F"]) < 1e-6 and abs(h_num - r["h_cp"]) < 1e-9,
               "Integral tlaka po vratima ne vraća silu i centar tlaka.")
    _invariant(out, "U05.CANON.Z1.support_balance",
               abs(r["dog_lower"] + r["dog_upper"] - r["F"] / 2) < 1e-9
               and abs(r["dog_lower"] * 1.60 - r["F"] / 2 * r["offset"]) < 1e-9
               and r["dog_lower"] > r["dog_upper"] > 0,
               "Zasuni ne zatvaraju silu i moment reda uz slobodni rub.")
    _invariant(out, "U05.CANON.Z1.seawater_heavier",
               r["F"] > task_watertight_door(rho=998.0)["F"]
               and abs(r["h_cp"] - task_watertight_door(rho=998.0)["h_cp"]) < 1e-12,
               "Gustoća mora mijenja silu, a ne položaj centra tlaka.")

    r = task_parabolic_cover()
    _check(out, "U05.CANON.Z2.F_x_kN", r["F_x"] / 1000, -5.948, "kN", rel=0.001)
    _check(out, "U05.CANON.Z2.depth_x", r["depth_x"], 0.600, "m", rel=0.001)
    _check(out, "U05.CANON.Z2.F_z_kN", r["F_z"] / 1000, -5.287, "kN", rel=0.001)
    _check(out, "U05.CANON.Z2.x_z", r["x_z"], 0.900, "m", rel=0.001)
    _check(out, "U05.CANON.Z2.F_R_kN", r["F_R"] / 1000, 7.958, "kN", rel=0.001)
    _check(out, "U05.CANON.Z2.M_A_kNm", r["M_A"] / 1000, -8.327, "kNm", rel=0.001)
    _invariant(out, "U05.CANON.Z2.direct_integration",
               abs(r["F_x_num"] - r["F_x"]) < 1e-6 and abs(r["F_z_num"] - r["F_z"]) < 1e-6
               and abs(r["M_num"] - r["M_A"]) < 1e-6,
               "Integral p n dA po paraboli ne vraća projekciju, pomoćni volumen i moment.")
    _invariant(out, "U05.CANON.Z2.signs", r["F_x"] < 0 and r["F_z"] < 0 and r["M_A"] < 0,
               "Voda iznad pokrova mora gurati prema stijenci i prema dolje.")
    px, pz = parabola_normal_intersection(1.20, 0.90, 0.30, 0.90)
    qx, qz = parabola_normal_intersection(1.20, 0.90, 0.60, 0.90)
    _invariant(out, "U05.CANON.Z2.no_common_centre",
               math.hypot(px - qx, pz - qz) > 0.05
               and abs(abs(r["F_x"]) * (pz + r["depth_x"]) - abs(r["F_z"]) * (r["x_z"] - px)) > 100.0,
               "Normale parabole ne smiju imati zajedničku točku kao kružni luk.")
    limit = task_parabolic_cover(H=0.09)
    _invariant(out, "U05.CANON.Z2.flat_limit",
               abs(limit["F_x"] / r["F_x"] - 0.01) < 1e-12 and abs(limit["F_z"] / r["F_z"] - 0.1) < 1e-12,
               "Vodoravna komponenta raste s H^2, vertikalna linearno s H.")

    r = task_flap_gate()
    _check(out, "U05.CANON.Z3.wetted_open", r["wetted_open"], 2.40, "m", rel=0.001)
    _check(out, "U05.CANON.Z3.h_c_open", r["h_c_open"], 1.443, "m", rel=0.001)
    _check(out, "U05.CANON.Z3.y_open", r["y_open"], 2.309, "m", rel=0.001)
    _check(out, "U05.CANON.Z3.top_depth_open", r["top_depth_open"], 0.577, "m", rel=0.002)
    _check(out, "U05.CANON.Z3.F_kN", r["F"] / 1000, 27.43, "kN", rel=0.001)
    _check(out, "U05.CANON.Z3.s_cp", r["s_cp"], 0.691, "m", rel=0.001)
    _check(out, "U05.CANON.Z3.M_axis_kNm", r["M_axis"] / 1000, 2.99, "kNm", rel=0.002)
    _check(out, "U05.CANON.Z3.R_sill_kN", r["R_sill"] / 1000, 3.74, "kN", rel=0.001)
    _check(out, "U05.CANON.Z3.s_centroid", r["s_centroid"], 1.00, "m", rel=0.001)
    _invariant(out, "U05.CANON.Z3.fully_submerged_at_opening",
               r["fully_submerged"] and r["wetted_open"] > 2.00 and r["top_depth_open"] > 0,
               "Otvaranje mora nastupiti tek nakon potpunog uronjenja.")
    f_num, m_num = flap_gate_numeric(1.80)
    _invariant(out, "U05.CANON.Z3.pressure_integration",
               abs(f_num - r["F"]) < 1e-3 and abs(m_num - r["M_axis"]) < 1e-3,
               "Integral tlaka po kosoj ploči ne vraća silu i moment oko osi.")
    _, m_open = flap_gate_numeric(r["y_open"])
    _, m_below = flap_gate_numeric(r["y_open"] - 0.1)
    _, m_above = flap_gate_numeric(r["y_open"] + 0.1)
    _invariant(out, "U05.CANON.Z3.moment_changes_sign_at_opening",
               abs(m_open) < 1e-3 and m_below > 0 > m_above,
               "Moment oko osi mora mijenjati predznak upravo pri dubini otvaranja.")
    _invariant(out, "U05.CANON.Z3.closed_at_1_80",
               r["s_cp"] < 0.80 < r["s_centroid"] and r["M_axis"] > 0 and r["R_sill"] > 0,
               "Pri 1,80 m hvatište je ispod osi, a težište iznad: samo težište bi otvorilo zaklopku.")
    _invariant(out, "U05.CANON.Z3.sill_balance",
               abs(r["R_sill"] * 0.80 - r["M_axis"]) < 1e-9,
               "Sila praga mora uravnotežiti moment vode oko osi.")
    low_axis = task_flap_gate(a=0.50)
    _invariant(out, "U05.CANON.Z3.low_axis_opens_partially_submerged",
               not low_axis["fully_submerged"] and abs(low_axis["y_open"] - 1.5 * math.sin(math.radians(60))) < 1e-12,
               "Niža os otvara zaklopku dok je ploča još djelomično uronjena (pravilo trećine).")

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
