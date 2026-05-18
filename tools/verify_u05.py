"""Numericka verifikacija U05: Hidrostatske sile na ravne plohe."""
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


def primjer_1_zaklopka(b=2.0, h=3.0, h_1=2.0, rho=998.0, g=9.81):
    A = b * h
    h_C = h_1 + h / 2
    F = rho * g * A * h_C
    I_G = b * h**3 / 12
    h_CP = h_C + I_G / (A * h_C)
    z = h_CP - h_1
    return {"A": A, "h_C": h_C, "F": F, "I_G": I_G, "h_CP": h_CP, "z": z}


def primjer_2_ukrute(b=1.20, H=2.40, rho=998.0, g=9.81):
    F_uk = 0.5 * rho * g * b * H**2
    F_p = F_uk / 4
    y_1 = H / 2
    y_2 = H / math.sqrt(2)
    y_3 = math.sqrt(3) / 2 * H
    y_CP_4 = (2 / 3) * (H**3 - y_3**3) / (H**2 - y_3**2)
    return {"F_uk": F_uk, "F_p": F_p,
            "y_1": y_1, "y_2": y_2, "y_3": y_3, "y_CP_4": y_CP_4}


def primjer_3_kosi(b=0.90, L=1.20, h_A=0.80, theta_deg=60.0,
                    rho=998.0, g=9.81):
    theta = math.radians(theta_deg)
    A = b * L
    h_C = h_A + (L / 2) * math.sin(theta)
    F = rho * g * A * h_C
    s_R = (h_A * L**2 / 2 + math.sin(theta) * L**3 / 3) / \
          (h_A * L + math.sin(theta) * L**2 / 2)
    M_A = F * s_R
    T = M_A / L
    return {"A": A, "h_C": h_C, "F": F, "s_R": s_R, "M_A": M_A, "T": T}


def cjeloviti_1_pregrada(b=1.40, h_o=1.00, h_w=1.80, rho_o=820.0,
                          rho_w=1000.0, g=9.81):
    H = h_o + h_w
    F_1 = 0.5 * rho_o * g * b * h_o**2
    F_2 = rho_o * g * b * h_o * h_w + 0.5 * rho_w * g * b * h_w**2
    F = F_1 + F_2
    M_1 = rho_o * g * b * h_o**3 / 3
    M_2 = (rho_o * g * b * h_o * h_w * (h_o + h_w / 2) +
           0.5 * rho_w * g * b * h_w**2 * (h_o + 2 * h_w / 3))
    M_A = M_1 + M_2
    y_CP = M_A / F
    T = F * y_CP / H
    R_A = F - T
    return {"F_1": F_1, "F_2": F_2, "F": F, "M_1": M_1, "M_2": M_2,
            "M_A": M_A, "y_CP": y_CP, "T": T, "R_A": R_A}


def primjer_5_kotao(b=0.40, h=0.60, h_1=1.50, rho=998.0, g=9.81):
    h_C = h_1 + h / 2
    A = b * h
    F = rho * g * A * h_C
    I_G = b * h**3 / 12
    y_CP = h_C + I_G / (A * h_C)
    dist_top = y_CP - h_1
    return {"h_C": h_C, "A": A, "F": F, "I_G": I_G,
            "y_CP": y_CP, "dist_top": dist_top}


def primjer_6_vrata(b=1.80, H_vr=1.20, h_1=0.80, rho=998.0, g=9.81):
    h_C = h_1 + H_vr / 2
    A = b * H_vr
    F = rho * g * A * h_C
    I_G = b * H_vr**3 / 12
    y_CP = h_C + I_G / (A * h_C)
    h_from_bottom = (h_1 + H_vr) - y_CP
    return {"h_C": h_C, "A": A, "F": F, "I_G": I_G,
            "y_CP": y_CP, "h_from_bottom": h_from_bottom}


def zadatak_1(b=1.40, h=1.80, h_1=1.10, rho=998.0, g=9.81):
    h_C = h_1 + h / 2
    A = b * h
    F = rho * g * A * h_C
    return {"F": F, "h_C": h_C}


def zadatak_2(D=0.60, h_C=2.20, rho=998.0, g=9.81):
    A = math.pi * D**2 / 4
    F = rho * g * A * h_C
    return {"F": F, "A": A}


def zadatak_3(b=0.80, L=1.00, theta_deg=40.0, h_1=0.90, rho=998.0, g=9.81):
    theta = math.radians(theta_deg)
    A = b * L
    h_C = h_1 + (L / 2) * math.sin(theta)
    F = rho * g * A * h_C
    return {"F": F, "h_C": h_C}


def zadatak_4(b=1.80, h_v=1.50, h_u=0.90, rho_u=820.0, rho_w=998.0, g=9.81):
    # Slojevi: ulje gore (0..h_u), voda dolje (h_u..h_u+h_v)
    F_u = 0.5 * rho_u * g * b * h_u**2
    F_w = (rho_u * g * b * h_u * h_v +
           0.5 * rho_w * g * b * h_v**2)
    F = F_u + F_w
    return {"F": F}


def zadatak_5(H=4.20, b=2.50, rho=998.0, g=9.81):
    # Tri jednake sile -> y_1 = H/sqrt(3), y_2 = H sqrt(2/3)
    y_1 = H / math.sqrt(3)
    y_2 = H * math.sqrt(2 / 3)
    return {"y_1": y_1, "y_2": y_2}


def zadatak_6(b=1.20, H=2.40, h_u=0.80, rho_u=820.0, rho_w=998.0, g=9.81):
    h_w = H - h_u
    F_u = 0.5 * rho_u * g * b * h_u**2
    F_w = (rho_u * g * b * h_u * h_w +
           0.5 * rho_w * g * b * h_w**2)
    F = F_u + F_w
    return {"F": F}


# ------------ Faza 1.5 dodatak: Vertikalna ploha kroz tri sloja fluida ----------------
def primjer_tri_sloja(b=0.80, L=1.50, h_0=0.30,
                       h_uv=0.80, h_vg=1.50,
                       rho_u=820.0, rho_w=998.0, rho_g=1260.0, g=9.81):
    h_bot = h_0 + L  # donji rub plohe (= 1.80 m)
    p_h0 = rho_u * g * h_0
    p_uv = rho_u * g * h_uv
    p_vg = p_uv + rho_w * g * (h_vg - h_uv)
    p_bot = p_vg + rho_g * g * (h_bot - h_vg)

    L1 = h_uv - h_0
    L2 = h_vg - h_uv
    L3 = h_bot - h_vg

    F1 = (p_h0 + p_uv) / 2 * b * L1
    F2 = (p_uv + p_vg) / 2 * b * L2
    F3 = (p_vg + p_bot) / 2 * b * L3
    F = F1 + F2 + F3

    def centroid(L_i, p_top, p_bot):
        return L_i * (p_top + 2 * p_bot) / (3 * (p_top + p_bot))

    hF1 = h_0 + centroid(L1, p_h0, p_uv)
    hF2 = h_uv + centroid(L2, p_uv, p_vg)
    hF3 = h_vg + centroid(L3, p_vg, p_bot)
    h_CP = (F1 * hF1 + F2 * hF2 + F3 * hF3) / F
    s_CP = h_CP - h_0

    return {"F1": F1, "F2": F2, "F3": F3, "F": F,
            "h_CP": h_CP, "s_CP": s_CP}


def verify():
    out = []

    r = primjer_1_zaklopka()
    _check(out, "U05.P1.A", r["A"], 6.0, "m^2")
    _check(out, "U05.P1.h_C", r["h_C"], 3.5, "m")
    _check(out, "U05.P1.F_kN", r["F"] / 1000, 205.5, "kN")
    _check(out, "U05.P1.I_G", r["I_G"], 4.5, "m^4")
    _check(out, "U05.P1.h_CP", r["h_CP"], 3.714, "m")
    _check(out, "U05.P1.z", r["z"], 1.714, "m")

    r = primjer_2_ukrute()
    _check(out, "U05.P2.F_p_kN", r["F_p"] / 1000, 8.46, "kN")
    _check(out, "U05.P2.y_1", r["y_1"], 1.20, "m")
    _check(out, "U05.P2.y_2", r["y_2"], 1.697, "m")
    _check(out, "U05.P2.y_3", r["y_3"], 2.078, "m")
    _check(out, "U05.P2.y_CP_4", r["y_CP_4"], 2.244, "m")

    r = primjer_3_kosi()
    _check(out, "U05.P3.A", r["A"], 1.08, "m^2")
    _check(out, "U05.P3.h_C", r["h_C"], 1.320, "m")
    _check(out, "U05.P3.F_kN", r["F"] / 1000, 13.95, "kN")
    _check(out, "U05.P3.s_R", r["s_R"], 0.679, "m", rel=0.02)
    _check(out, "U05.P3.T_kN", r["T"] / 1000, 7.89, "kN", rel=0.02)

    r = cjeloviti_1_pregrada()
    _check(out, "U05.CH1.F_1_kN", r["F_1"] / 1000, 5.63, "kN")
    _check(out, "U05.CH1.F_2_kN", r["F_2"] / 1000, 42.52, "kN", rel=0.02)
    _check(out, "U05.CH1.F_kN", r["F"] / 1000, 48.15, "kN", rel=0.02)
    _check(out, "U05.CH1.y_CP", r["y_CP"], 1.894, "m", rel=0.02)
    _check(out, "U05.CH1.T_kN", r["T"] / 1000, 32.58, "kN", rel=0.02)
    _check(out, "U05.CH1.R_A_kN", r["R_A"] / 1000, 15.57, "kN", rel=0.02)

    r = primjer_5_kotao()
    _check(out, "U05.P5.F_kN", r["F"] / 1000, 4.23, "kN")
    _check(out, "U05.P5.y_CP", r["y_CP"], 1.817, "m")
    _check(out, "U05.P5.dist_top", r["dist_top"], 0.317, "m", rel=0.02)

    r = primjer_6_vrata()
    _check(out, "U05.P6.F_kN", r["F"] / 1000, 29.63, "kN")
    _check(out, "U05.P6.y_CP", r["y_CP"], 1.486, "m")
    _check(out, "U05.P6.h_from_bottom", r["h_from_bottom"], 0.514, "m", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U05.{name}.{first_key}_pos", r[first_key], r[first_key])

    # Faza 1.5: Vertikalna ploha kroz tri sloja fluida
    r = primjer_tri_sloja()
    _check(out, "U05.tri_sloja.F1_N", r["F1"], 1770, "N", rel=0.02)
    _check(out, "U05.tri_sloja.F2_N", r["F2"], 5523, "N", rel=0.02)
    _check(out, "U05.tri_sloja.F3_N", r["F3"], 3634, "N", rel=0.02)
    _check(out, "U05.tri_sloja.F_kN", r["F"] / 1000, 10.93, "kN", rel=0.02)
    _check(out, "U05.tri_sloja.h_CP_m", r["h_CP"], 1.248, "m", rel=0.02)
    _check(out, "U05.tri_sloja.s_CP_m", r["s_CP"], 0.948, "m", rel=0.02)

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
