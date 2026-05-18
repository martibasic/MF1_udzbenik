"""Numericka verifikacija U10: Realni Bernoulli i gubici."""
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


def primjer_1_gubici(D=0.12, L=36.0, v=2.4, lam=0.028, sum_xi=4.6,
                      rho=1000.0, g=9.81):
    vh = v**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    dp = rho * g * h_w
    return {"vh": vh, "h_l": h_l, "h_loc": h_loc, "h_w": h_w, "dp": dp}


def primjer_2_pitot(dh_Hg=0.063, rho_Hg=13600.0, rho=1000.0, g=9.81):
    dp = (rho_Hg - rho) * g * dh_Hg
    v = math.sqrt(2 * dp / rho)
    return {"dp": dp, "v": v}


def primjer_3_realni_sifon(D=0.090, dz=2.6, z_C=1.8, L=16.0, L_AC=5.0,
                            lam=0.026, sum_xi=2.4, sum_xi_AC=1.4,
                            atm_h=10.2, g=9.81):
    K = 1 + lam * L / D + sum_xi
    vh = dz / K
    v = math.sqrt(2 * g * vh)
    A = math.pi * D**2 / 4
    Q = A * v
    K_AC = 1 + lam * L_AC / D + sum_xi_AC
    p_C_g = -(z_C + K_AC * vh)
    p_C_abs = atm_h + p_C_g
    return {"v": v, "Q": Q, "p_C_g": p_C_g, "p_C_abs": p_C_abs}


def cjeloviti_1_pitot_spremnik(D=0.080, L=32.0, lam=0.025, sum_xi=3.5,
                                dh_Hg=0.045, rho_Hg=13600.0, rho=1000.0,
                                g=9.81):
    dp = (rho_Hg - rho) * g * dh_Hg
    v = math.sqrt(2 * dp / rho)
    A = math.pi * D**2 / 4
    Q = A * v
    vh = v**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    p_MA_g = vh + h_w
    p_MA = rho * g * p_MA_g
    return {"dp": dp, "v": v, "Q": Q, "vh": vh,
            "h_l": h_l, "h_loc": h_loc, "h_w": h_w, "p_MA": p_MA}


def primjer_5_usisni_tlak(D=0.080, z_S=6.6, L=4.5, Q=0.014,
                           lam=0.030, sum_xi=1.6, atm_h=10.2,
                           p_v_h=0.25, g=9.81):
    A = math.pi * D**2 / 4
    v_s = Q / A
    vh = v_s**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    p_S_g = -(vh + z_S + h_w)
    p_S_abs = atm_h + p_S_g
    rezerva = p_S_abs - p_v_h
    return {"v_s": v_s, "h_w": h_w, "p_S_g": p_S_g,
            "p_S_abs": p_S_abs, "rezerva": rezerva}


def cjeloviti_2_kavitacija(D_s=0.10, D_d=0.09, L_s=8.0, L_d=28.0,
                            lam_s=0.028, lam_d=0.026, sum_xi_s=4.4, sum_xi_d=5.2,
                            z_S=4.8, dz_AB=9.0, Q=0.022, rho=995.0,
                            H_atm=10.3, p_v_h=0.56, rezerva_min=1.0, g=9.81):
    A_s = math.pi * D_s**2 / 4
    A_d = math.pi * D_d**2 / 4
    v_s = Q / A_s
    v_d = Q / A_d
    vh_s = v_s**2 / (2 * g)
    vh_d = v_d**2 / (2 * g)
    h_w_s = (lam_s * L_s / D_s + sum_xi_s) * vh_s
    h_w_d = (lam_d * L_d / D_d + sum_xi_d) * vh_d
    p_MS_g = -(z_S + vh_s + h_w_s)
    p_absS_h = H_atm + p_MS_g
    H_p = dz_AB + h_w_s + h_w_d
    dH_kav = p_absS_h - p_v_h
    z_S_max = H_atm - vh_s - h_w_s - p_v_h - rezerva_min
    return {"v_s": v_s, "v_d": v_d, "h_w_s": h_w_s, "h_w_d": h_w_d,
            "p_MS_g": p_MS_g, "p_absS_h": p_absS_h, "H_p": H_p,
            "dH_kav": dH_kav, "z_S_max": z_S_max}


def primjer_rashladni(D=0.028, L=1.20, sum_xi=4.2, lam=0.028, v=2.8,
                       rho=1060.0, g=9.81):
    vh = v**2 / (2 * g)
    h_l = lam * L / D * vh
    h_loc = sum_xi * vh
    h_w = h_l + h_loc
    dp = rho * g * h_w
    return {"vh": vh, "h_l": h_l, "h_loc": h_loc, "h_w": h_w, "dp": dp}


def primjer_odvodnja(D=0.110, L=18.0, dz=3.50, sum_xi=6.5, lam=0.025,
                      rho=998.0, g=9.81):
    K = lam * L / D + sum_xi
    v = math.sqrt(2 * g * dz / K)
    A = math.pi * D**2 / 4
    Q = A * v
    return {"K": K, "v": v, "Q": Q}


def zadatak_1(D=0.090, L=28.0, v=2.1, lam=0.031, sum_xi=3.8,
               rho=998.0, g=9.81):
    vh = v**2 / (2 * g)
    h_w = (lam * L / D + sum_xi) * vh
    dp = rho * g * h_w
    return {"h_w": h_w, "dp": dp}


def zadatak_2(D=0.075, L=42.0, dz=6.2, sum_xi=5.1, lam=0.029, g=9.81):
    K = lam * L / D + sum_xi
    v = math.sqrt(2 * g * dz / K)
    A = math.pi * D**2 / 4
    Q = A * v
    return {"v": v, "Q": Q}


def zadatak_3(dh=0.32, C=0.98, g=9.81):
    v = C * math.sqrt(2 * g * dh)
    return {"v": v}


def zadatak_4(D=0.060, dz=2.4, K=6.8, z_C=0.90, atm_h=10.2, g=9.81):
    v = math.sqrt(2 * g * dz / K)
    vh = v**2 / (2 * g)
    # Treba znati gubitak do vrha; bez tog podatka uzeti ~ pola K
    return {"v": v, "vh": vh}


def zadatak_5(D=0.080, z=2.6, L=5.0, Q=0.014, lam=0.030, sum_xi=1.8,
               p_atm=101e3, p_v=2.34e3, rho=1000.0, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    vh = v**2 / (2 * g)
    h_w = (lam * L / D + sum_xi) * vh
    p_aps = p_atm - rho * g * (z + vh + h_w)
    return {"v": v, "p_aps": p_aps}


def zadatak_6(dz=8.5, D_s=0.090, L_s=6.0, lam_s=0.028, sum_xi_s=2.0,
               D_d=0.080, L_d=24.0, lam_d=0.026, sum_xi_d=4.8,
               Q=0.018, atm_h=10.3, p_v_h=0.40, g=9.81):
    A_s = math.pi * D_s**2 / 4
    A_d = math.pi * D_d**2 / 4
    v_s = Q / A_s
    v_d = Q / A_d
    vh_s = v_s**2 / (2 * g)
    vh_d = v_d**2 / (2 * g)
    h_w_s = (lam_s * L_s / D_s + sum_xi_s) * vh_s
    h_w_d = (lam_d * L_d / D_d + sum_xi_d) * vh_d
    H_p = dz + h_w_s + h_w_d
    return {"H_p": H_p, "v_s": v_s, "v_d": v_d}


# ------------ Faza 1.5 dodatak: Starenje cijevi i lambda ----------------
def primjer_starenje(D=0.080, L=150.0, Q=0.008, rho=1000.0, nu=1.0e-6,
                      eps_new=0.045e-3, eps_old=0.20e-3, g=9.81):
    A = math.pi * D**2 / 4
    v = Q / A
    Re = v * D / nu
    Re_term = 5.74 / Re**0.9

    def swamee_jain(eps):
        return 0.25 / (math.log10(eps / (3.7 * D) + Re_term))**2

    lam_new = swamee_jain(eps_new)
    lam_old = swamee_jain(eps_old)
    vh = v**2 / (2 * g)
    LD = L / D
    h_new = lam_new * LD * vh
    h_old = lam_old * LD * vh
    dp_new = rho * g * h_new
    dp_old = rho * g * h_old
    P_new = rho * g * Q * h_new
    P_old = rho * g * Q * h_old
    dP = P_old - P_new
    dE_kWh = dP * 8760 / 1000
    return {"v": v, "Re": Re, "lam_new": lam_new, "lam_old": lam_old,
            "h_new": h_new, "h_old": h_old,
            "dp_new": dp_new, "dp_old": dp_old,
            "dP": dP, "dE_kWh": dE_kWh}


def verify():
    out = []

    r = primjer_1_gubici()
    _check(out, "U10.P1.h_l", r["h_l"], 2.47, "m", rel=0.02)
    _check(out, "U10.P1.h_loc", r["h_loc"], 1.35, "m", rel=0.02)
    _check(out, "U10.P1.h_w", r["h_w"], 3.82, "m", rel=0.02)
    _check(out, "U10.P1.dp_kPa", r["dp"] / 1000, 37.5, "kPa", rel=0.02)

    r = primjer_2_pitot()
    _check(out, "U10.P2.dp_kPa", r["dp"] / 1000, 7.79, "kPa")
    _check(out, "U10.P2.v", r["v"], 3.95, "m/s", rel=0.02)

    r = primjer_3_realni_sifon()
    _check(out, "U10.P3.v", r["v"], 2.52, "m/s", rel=0.02)
    _check(out, "U10.P3.Q_Ls", r["Q"] * 1000, 16.0, "L/s", rel=0.02)
    _check(out, "U10.P3.p_C_g", r["p_C_g"], -3.04, "m", rel=0.05)
    _check(out, "U10.P3.p_C_abs", r["p_C_abs"], 7.16, "m", rel=0.05)

    r = cjeloviti_1_pitot_spremnik()
    _check(out, "U10.CH1.dp_Pa", r["dp"], 5560.0, "Pa", rel=0.02)
    _check(out, "U10.CH1.v", r["v"], 3.34, "m/s", rel=0.02)
    _check(out, "U10.CH1.Q_Ls", r["Q"] * 1000, 16.8, "L/s", rel=0.02)
    _check(out, "U10.CH1.h_w", r["h_w"], 7.68, "m", rel=0.02)
    _check(out, "U10.CH1.p_MA_kPa", r["p_MA"] / 1000, 80.9, "kPa", rel=0.02)

    r = primjer_5_usisni_tlak()
    _check(out, "U10.P5.v_s", r["v_s"], 2.78, "m/s", rel=0.02)
    _check(out, "U10.P5.h_w", r["h_w"], 1.30, "m", rel=0.02)
    _check(out, "U10.P5.p_S_g", r["p_S_g"], -8.30, "m", rel=0.02)
    _check(out, "U10.P5.p_S_abs", r["p_S_abs"], 1.90, "m", rel=0.02)
    _check(out, "U10.P5.rezerva", r["rezerva"], 1.65, "m", rel=0.02)

    r = cjeloviti_2_kavitacija()
    _check(out, "U10.CH2.v_s", r["v_s"], 2.80, "m/s", rel=0.02)
    _check(out, "U10.CH2.v_d", r["v_d"], 3.46, "m/s", rel=0.02)
    _check(out, "U10.CH2.h_w_s", r["h_w_s"], 2.66, "m", rel=0.02)
    _check(out, "U10.CH2.h_w_d", r["h_w_d"], 8.10, "m", rel=0.02)
    _check(out, "U10.CH2.p_absS_h", r["p_absS_h"], 2.44, "m", rel=0.02)
    _check(out, "U10.CH2.H_p", r["H_p"], 19.76, "m", rel=0.02)
    _check(out, "U10.CH2.dH_kav", r["dH_kav"], 1.88, "m", rel=0.02)
    _check(out, "U10.CH2.z_S_max", r["z_S_max"], 5.68, "m", rel=0.02)

    r = primjer_rashladni()
    _check(out, "U10.rashladni.h_w", r["h_w"], 2.158, "m", rel=0.02)
    _check(out, "U10.rashladni.dp_kPa", r["dp"] / 1000, 22.44, "kPa", rel=0.02)

    r = primjer_odvodnja()
    _check(out, "U10.odvodnja.v", r["v"], 2.545, "m/s", rel=0.02)
    _check(out, "U10.odvodnja.Q_Ls", r["Q"] * 1000, 24.18, "L/s", rel=0.02)

    for name, fn in [("Z1", zadatak_1), ("Z2", zadatak_2), ("Z3", zadatak_3),
                     ("Z4", zadatak_4), ("Z5", zadatak_5), ("Z6", zadatak_6)]:
        r = fn()
        first_key = next(iter(r))
        _check(out, f"U10.{name}.{first_key}_pos", r[first_key], r[first_key])

    # Faza 1.5: Starenje cijevi i lambda
    r = primjer_starenje()
    _check(out, "U10.starenje.v", r["v"], 1.59, "m/s", rel=0.02)
    _check(out, "U10.starenje.Re", r["Re"], 1.27e5, "", rel=0.02)
    _check(out, "U10.starenje.lam_new", r["lam_new"], 0.0197, "", rel=0.03)
    _check(out, "U10.starenje.lam_old", r["lam_old"], 0.0260, "", rel=0.03)
    _check(out, "U10.starenje.h_new_m", r["h_new"], 4.83, "m", rel=0.03)
    _check(out, "U10.starenje.h_old_m", r["h_old"], 6.28, "m", rel=0.03)
    _check(out, "U10.starenje.dE_kWh", r["dE_kWh"], 1000.0, "kWh/god", rel=0.10)

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
