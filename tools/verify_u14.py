"""Numericka verifikacija U14: Bezdimenzijski brojevi, dimenzijska analiza i slicnost."""
from __future__ import annotations

import math

TOL = 0.01

# Zajednicka svojstva (kako su navedena u tekstu poglavlja)
RHO_V = 1000.0       # voda, kg/m^3
NU_V = 1.0e-6        # voda, m^2/s
SIGMA_V = 0.072      # voda-zrak, N/m
PV_V = 2340.0        # tlak isparavanja vode pri 20 C, Pa
RHO_A = 1.2          # zrak, kg/m^3
NU_A = 1.5e-5        # zrak, m^2/s
A_SOUND = 340.0      # brzina zvuka u zraku, m/s
G = 9.81


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


# --------------------------------------------------------------------------
def primjer_1_reynolds(D=0.006, v_voda=1.2, nu_voda=NU_V,
                       v_ulje=0.30, nu_ulje=4.0e-5, Re_kr=2300.0):
    Re_A = v_voda * D / nu_voda
    Re_B = v_ulje * D / nu_ulje
    v_krit_voda = Re_kr * nu_voda / D
    return {"Re_A": Re_A, "Re_B": Re_B, "v_krit_voda": v_krit_voda}


def primjer_2_froude(lam=25.0, L_s=150.0, v_s=9.0, nu=NU_V, g=G):
    L_m = L_s / lam
    v_m = v_s / math.sqrt(lam)
    Fr = v_s / math.sqrt(g * L_s)
    Re_s = v_s * L_s / nu
    Re_m = v_m * L_m / nu
    Re_ratio = Re_s / Re_m
    return {"L_m": L_m, "v_m": v_m, "Fr": Fr, "Re_ratio": Re_ratio}


def primjer_3_venturi(D1=0.060, D2=0.020, Q=0.006, p1=101300.0,
                      rho=RHO_V, p_v=PV_V):
    A1 = math.pi * D1**2 / 4
    A2 = math.pi * D2**2 / 4
    v1 = Q / A1
    v2 = Q / A2
    p2_pred = p1 + 0.5 * rho * (v1**2 - v2**2)
    beta = A2 / A1
    # p1 - p_v = 0.5 rho v2^2 (1 - beta^2)
    v2_max = math.sqrt((p1 - p_v) / (0.5 * rho * (1 - beta**2)))
    Q_max = A2 * v2_max
    sigma = (p1 - p_v) / (0.5 * rho * v2**2)
    return {"v1": v1, "v2": v2, "p2_pred_kPa": p2_pred / 1000,
            "Q_max_Ls": Q_max * 1000, "sigma": sigma}


def primjer_4_weber(d=0.003, v=25.0, rho_a=RHO_A, sigma=SIGMA_V,
                    rho_w=RHO_V, g=G, We_kr=12.0):
    We = rho_a * v**2 * d / sigma
    Bo = rho_w * g * d**2 / sigma
    v_crit = math.sqrt(We_kr * sigma / (rho_a * d))
    L_c = math.sqrt(sigma / (rho_w * g))
    return {"We": We, "Bo": Bo, "v_crit": v_crit, "L_c_mm": L_c * 1000}


def cjeloviti_1_kugla(D=0.020, v=30.0, rho=RHO_A, nu=NU_A, Cd=0.45):
    Re = v * D / nu
    A = math.pi * D**2 / 4
    F_d = Cd * 0.5 * rho * v**2 * A
    Pi1 = F_d / (rho * v**2 * D**2)
    return {"Re": Re, "F_d": F_d, "Pi1": Pi1}


def primjer_6_mach_strouhal(D=0.080, Q1=0.40, Q2=0.80, a=A_SOUND,
                            D_dim=2.0, v_vjetar=12.0, St=0.2, f_n=0.6,
                            D_mj=0.100, d_mj=0.030, f_mj=45.0):
    A = math.pi * D**2 / 4
    v1 = Q1 / A
    v2 = Q2 / A
    Ma_1 = v1 / a
    Ma_2 = v2 / a
    Q_lim = A * (0.3 * a)
    f_dimnjak = St * v_vjetar / D_dim
    v_rez = f_n * D_dim / St
    v_mj = f_mj * d_mj / St
    A_mj = math.pi * D_mj**2 / 4
    Q_mj = A_mj * v_mj
    return {"Ma_1": Ma_1, "Ma_2": Ma_2, "Q_lim_Ls": Q_lim * 1000,
            "f_dimnjak": f_dimnjak, "v_rez": v_rez, "Q_mj_Ls": Q_mj * 1000}


# --------------------------------------------------------------------------
def zadatak_1(D_a=0.0003, v_a=0.005, nu_a=3.3e-6,
              D_v=0.30, v_v=1.5, nu_v=NU_V):
    Re_krv = v_a * D_a / nu_a
    Re_voda = v_v * D_v / nu_v
    return {"Re_krv": Re_krv, "Re_voda": Re_voda}


def zadatak_2(lam=20.0, v_s=4.5, Q_s=350.0):
    v_m = v_s / math.sqrt(lam)
    Q_m = Q_s / lam**2.5
    return {"v_m": v_m, "Q_m": Q_m}


def zadatak_3(p=80000.0, v=4.0, p_v=PV_V, rho=RHO_V):
    sigma = (p - p_v) / (0.5 * rho * v**2)
    return {"sigma": sigma}


def zadatak_4(d=0.00015, v=80.0, rho_a=RHO_A, sigma=0.025):
    We = rho_a * v**2 * d / sigma
    return {"We": We}


def zadatak_5(D=0.100, Q=0.5, a=A_SOUND):
    A = math.pi * D**2 / 4
    v = Q / A
    Ma = v / a
    return {"v": v, "Ma": Ma}


def zadatak_5_strouhal(D=0.050, rho=1.20, mu=1.80e-5, v=12.0, St=0.190):
    Re = rho * v * D / mu
    f = St * v / D
    return {"Re": Re, "f": f}


def zadatak_6(dp=18000.0, v=2.0, D=0.050, L=20.0, rho=RHO_V, nu=NU_V):
    Eu = dp / (rho * v**2)
    lam = 2 * Eu * D / L
    Re = v * D / nu
    return {"Eu": Eu, "lam": lam, "Re": Re}


def zadatak_6_froude_model(lam_L=30.0, v_p=6.0, Q_p=480.0,
                            F_p=220e3, h_m=0.25, nu=NU_V):
    v_m = v_p / math.sqrt(lam_L)
    Q_m = Q_p / lam_L**2.5
    F_m = F_p / lam_L**3
    Re_m = v_m * h_m / nu
    return {"v_m": v_m, "Q_m": Q_m, "F_m": F_m, "Re_m": Re_m}


def verify():
    out = []

    r = primjer_1_reynolds()
    _check(out, "U14.P1.Re_A", r["Re_A"], 7200.0, "", rel=0.01)
    _check(out, "U14.P1.Re_B", r["Re_B"], 45.0, "", rel=0.01)
    _check(out, "U14.P1.v_krit_voda", r["v_krit_voda"], 0.383, "m/s", rel=0.02)

    r = primjer_2_froude()
    _check(out, "U14.P2.L_m", r["L_m"], 6.0, "m", rel=0.01)
    _check(out, "U14.P2.v_m", r["v_m"], 1.8, "m/s", rel=0.01)
    _check(out, "U14.P2.Fr", r["Fr"], 0.235, "", rel=0.02)
    _check(out, "U14.P2.Re_ratio", r["Re_ratio"], 125.0, "", rel=0.01)

    r = primjer_3_venturi()
    _check(out, "U14.P3.v1", r["v1"], 2.122, "m/s", rel=0.01)
    _check(out, "U14.P3.v2", r["v2"], 19.10, "m/s", rel=0.01)
    _check(out, "U14.P3.p2_pred_kPa", r["p2_pred_kPa"], -78.8, "kPa", rel=0.02)
    _check(out, "U14.P3.Q_max_Ls", r["Q_max_Ls"], 4.45, "L/s", rel=0.02)
    _check(out, "U14.P3.sigma", r["sigma"], 0.543, "", rel=0.02)

    r = primjer_4_weber()
    _check(out, "U14.P4.We", r["We"], 31.25, "", rel=0.01)
    _check(out, "U14.P4.Bo", r["Bo"], 1.226, "", rel=0.01)
    _check(out, "U14.P4.v_crit", r["v_crit"], 15.49, "m/s", rel=0.02)
    _check(out, "U14.P4.L_c_mm", r["L_c_mm"], 2.71, "mm", rel=0.02)

    r = cjeloviti_1_kugla()
    _check(out, "U14.CH1.Re", r["Re"], 40000.0, "", rel=0.01)
    _check(out, "U14.CH1.F_d", r["F_d"], 0.0763, "N", rel=0.02)
    _check(out, "U14.CH1.Pi1", r["Pi1"], 0.1767, "", rel=0.01)

    r = primjer_6_mach_strouhal()
    _check(out, "U14.P6.Ma_1", r["Ma_1"], 0.234, "", rel=0.02)
    _check(out, "U14.P6.Ma_2", r["Ma_2"], 0.468, "", rel=0.02)
    _check(out, "U14.P6.Q_lim_Ls", r["Q_lim_Ls"], 512.7, "L/s", rel=0.02)
    _check(out, "U14.P6.f_dimnjak", r["f_dimnjak"], 1.2, "Hz", rel=0.01)
    _check(out, "U14.P6.v_rez", r["v_rez"], 6.0, "m/s", rel=0.01)
    _check(out, "U14.P6.Q_mj_Ls", r["Q_mj_Ls"], 53.0, "L/s", rel=0.02)

    r = zadatak_1()
    _check(out, "U14.Z1.Re_krv", r["Re_krv"], 0.4545, "", rel=0.02)
    _check(out, "U14.Z1.Re_voda", r["Re_voda"], 450000.0, "", rel=0.01)

    r = zadatak_5()
    _check(out, "U14.Z2.v", r["v"], 63.7, "m/s", rel=0.02)
    _check(out, "U14.Z2.Ma", r["Ma"], 0.187, "", rel=0.02)

    r = zadatak_3()
    _check(out, "U14.Z3.sigma", r["sigma"], 9.707, "", rel=0.02)

    r = zadatak_4()
    _check(out, "U14.Z4.We", r["We"], 46.08, "", rel=0.02)

    r = zadatak_5_strouhal()
    _check(out, "U14.Z5.Re", r["Re"], 4.00e4, "", rel=0.01)
    _check(out, "U14.Z5.f", r["f"], 45.6, "Hz", rel=0.01)

    # Buckinghamov dio zadatka jednoznačno mora dati n-k=2 i dimenzijski
    # valjane St i Re grupe; broj St i dalje dolazi iz podataka ili modela.
    n_variables, k_dimensions = 5, 3
    _invariant(
        out,
        "U14.Z5.group_count",
        n_variables - k_dimensions == 2,
        "Pet veličina i tri neovisne dimenzije moraju dati dvije Pi-grupe.",
    )
    dim_f = (0, 0, -1)
    dim_D = (0, 1, 0)
    dim_v = (0, 1, -1)
    dim_rho = (1, -3, 0)
    dim_mu = (1, -1, -1)
    dim_St = tuple(dim_f[i] + dim_D[i] - dim_v[i] for i in range(3))
    dim_Re = tuple(
        dim_rho[i] + dim_v[i] + dim_D[i] - dim_mu[i] for i in range(3)
    )
    _invariant(
        out,
        "U14.Z5.group_dimensions",
        dim_St == (0, 0, 0) and dim_Re == (0, 0, 0),
        "St=fD/v i Re=rho*v*D/mu moraju biti bezdimenzijski.",
    )

    r = zadatak_6_froude_model()
    _check(out, "U14.Z6.v_m", r["v_m"], 1.10, "m/s", rel=0.02)
    _check(out, "U14.Z6.Q_m_Ls", r["Q_m"] * 1000, 97.4, "L/s", rel=0.02)
    _check(out, "U14.Z6.F_m", r["F_m"], 8.15, "N", rel=0.02)
    _check(out, "U14.Z6.Re_m", r["Re_m"], 2.7e5, "", rel=0.03)

    return out


if __name__ == "__main__":
    results = verify()
    ok = sum(1 for r in results if r["status"] == "OK")
    fail = sum(1 for r in results if r["status"] != "OK")
    for r in results:
        marker = "v" if r["status"] == "OK" else "x"
        print(f"  [{marker}] {r['id']:24s}  {r.get('details', '')}")
    print()
    print(f"Total: ok={ok}, fail={fail}")
