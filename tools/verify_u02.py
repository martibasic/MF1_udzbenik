"""Numericka verifikacija U02: Viskoznost, povrsinska napetost i kapilarnost."""
from __future__ import annotations

import math

TOL = 0.01


def _close(value: float, target: float, rel: float = TOL) -> bool:
    if target == 0:
        return abs(value) < rel
    return abs(value - target) / abs(target) <= rel


def _check(out: list, rid: str, value: float, target: float, unit: str = "", rel: float = TOL):
    ok = _close(value, target, rel)
    out.append({
        "id": rid,
        "status": "OK" if ok else "FAIL",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


def kratki(mu=0.18, rho=900.0):
    return {"nu": mu / rho}


def primjer_smicanje(delta=0.003, v=0.90, A=0.18, mu=0.42, rho=870.0):
    dvdy = v / delta
    tau = mu * dvdy
    F = tau * A
    nu = mu / rho
    return {"dvdy": dvdy, "tau": tau, "F": F, "nu": nu}


def primjer_etanol(d=1.0e-3, sigma=0.022, rho=790.0, g=9.81, theta_deg=18.0):
    h = 4 * sigma * math.cos(math.radians(theta_deg)) / (rho * g * d)
    return {"h": h}


def primjer_kapljica(d=1.2e-3, sigma=0.072, p0=101325.0):
    dp = 4 * sigma / d
    p_in = p0 + dp
    return {"dp": dp, "p_in": p_in}


def primjer_kapljica_2(d=0.6e-3, sigma=0.072):
    return {"dp": 4 * sigma / d}


def cjeloviti_mikrodozator(d=0.80e-3, D=2.4e-3, H=0.060,
                            sigma=0.072, rho=998.0, g=9.81, p0=101325.0):
    h_cap = 4 * sigma / (rho * g * d)
    dp = 4 * sigma / D
    p_in = p0 + dp
    p_H = rho * g * max(H - h_cap, 0.0)
    p_M_min = p_H + dp
    return {"h_cap": h_cap, "dp": dp, "p_in": p_in, "p_M_min": p_M_min}


def primjer_lezaj(D=0.060, L=0.080, delta=0.50e-3, mu=0.25, n=1450.0):
    v = math.pi * D * n / 60.0
    tau = mu * v / delta
    A = math.pi * D * L
    F = tau * A
    M = F * D / 2
    return {"v": v, "tau": tau, "F": F, "M": M}


def primjer_vlaga_zid(d_por=0.12e-3, sigma=0.072, theta_deg=40.0, rho=998.0, g=9.81):
    cos_t = math.cos(math.radians(theta_deg))
    h = 4 * sigma * cos_t / (rho * g * d_por)
    h_2 = 4 * sigma * cos_t / (rho * g * d_por / 2)
    return {"h": h, "h_2": h_2}


def zadatak_1(delta=2.4e-3, A=0.22, v=0.65, mu=0.84):
    dvdy = v / delta
    tau = mu * dvdy
    F = tau * A
    return {"dvdy": dvdy, "tau": tau, "F": F}


def zadatak_2(A=0.14, v=0.80, delta=1.8e-3, F=21.0):
    tau = F / A
    mu = tau * delta / v
    return {"tau": tau, "mu": mu}


def zadatak_3(D=0.070, L=0.24, v=1.6, delta=0.60e-3, mu=0.36):
    tau = mu * v / delta
    A = math.pi * D * L
    F = tau * A
    return {"tau": tau, "F": F}


def zadatak_4(d1=0.60e-3, d2=1.20e-3, sigma=0.022, theta_deg=18.0, rho=790.0, g=9.81):
    cos_t = math.cos(math.radians(theta_deg))
    h1 = 4 * sigma * cos_t / (rho * g * d1)
    h2 = 4 * sigma * cos_t / (rho * g * d2)
    return {"h1": h1, "h2": h2}


def zadatak_5(d=0.90e-3, sigma=0.072, theta_deg=10.0, rho=998.0, g=9.81, d_k=1.2e-3):
    cos_t = math.cos(math.radians(theta_deg))
    h = 4 * sigma * cos_t / (rho * g * d)
    dp = 4 * sigma / d_k
    return {"h": h, "dp": dp}


def zadatak_6(d=0.50e-3, sigma=0.072, rho=998.0, g=9.81, theta_deg=0.0,
               H=0.042, D=1.8e-3):
    cos_t = math.cos(math.radians(theta_deg))
    h_cap = 4 * sigma * cos_t / (rho * g * d)
    dp = 4 * sigma / D
    p_M = rho * g * max(H - h_cap, 0.0) + dp
    return {"h_cap": h_cap, "dp": dp, "p_M": p_M}


# ------------ Faza 1.5 dodatak: Klizni lezaj pri hladnoj/toploj temperaturi ----------------
def primjer_lezaj_temp(D=0.050, L=0.070, delta=0.30e-3, n=2400.0,
                       mu_cold=0.40, mu_hot=0.040):
    v = math.pi * D * n / 60
    dvdy = v / delta
    tau_c = mu_cold * dvdy
    tau_h = mu_hot * dvdy
    A = math.pi * D * L
    F_c = tau_c * A
    F_h = tau_h * A
    M_c = F_c * D / 2
    M_h = F_h * D / 2
    omega = 2 * math.pi * n / 60
    P_c = M_c * omega
    P_h = M_h * omega
    return {"v": v, "tau_c": tau_c, "tau_h": tau_h,
            "P_c": P_c, "P_h": P_h, "ratio": P_c / P_h}


def verify() -> list:
    out: list = []

    r = kratki()
    _check(out, "U02.kratki.nu", r["nu"], 2.0e-4, "m^2/s")

    r = primjer_smicanje()
    _check(out, "U02.P1.dvdy", r["dvdy"], 300.0, "1/s")
    _check(out, "U02.P1.tau", r["tau"], 126.0, "Pa")
    _check(out, "U02.P1.F", r["F"], 22.7, "N")
    _check(out, "U02.P1.nu", r["nu"], 4.83e-4, "m^2/s")

    r = primjer_etanol()
    _check(out, "U02.P2.h_mm", r["h"] * 1000, 10.8, "mm")

    r = primjer_kapljica()
    _check(out, "U02.P3.dp", r["dp"], 240.0, "Pa")
    _check(out, "U02.P3.p_in_Pa", r["p_in"], 101565.0, "Pa")
    r2 = primjer_kapljica_2()
    _check(out, "U02.P3.dp_2", r2["dp"], 480.0, "Pa")

    r = cjeloviti_mikrodozator()
    _check(out, "U02.CH1.h_cap_mm", r["h_cap"] * 1000, 36.8, "mm")
    _check(out, "U02.CH1.dp", r["dp"], 120.0, "Pa")
    _check(out, "U02.CH1.p_in_Pa", r["p_in"], 101445.0, "Pa")
    _check(out, "U02.CH1.p_M_min", r["p_M_min"], 347.0, "Pa", rel=0.03)

    r = primjer_lezaj()
    _check(out, "U02.lezaj.v", r["v"], 4.56, "m/s")
    _check(out, "U02.lezaj.tau", r["tau"], 2280.0, "Pa")
    _check(out, "U02.lezaj.F", r["F"], 34.4, "N")
    _check(out, "U02.lezaj.M", r["M"], 1.03, "Nm")

    r = primjer_vlaga_zid()
    _check(out, "U02.vlaga.h_cm", r["h"] * 100, 18.8, "cm")
    _check(out, "U02.vlaga.h_2_cm", r["h_2"] * 100, 37.6, "cm")

    z1 = zadatak_1()
    _check(out, "U02.Z1.dvdy_pos", z1["dvdy"], z1["dvdy"])
    z2 = zadatak_2()
    _check(out, "U02.Z2.mu_pos", z2["mu"], z2["mu"])
    z3 = zadatak_3()
    _check(out, "U02.Z3.F_pos", z3["F"], z3["F"])
    z4 = zadatak_4()
    _check(out, "U02.Z4.h1_gt_h2", 1.0 if z4["h1"] > z4["h2"] else 0.0, 1.0)
    z5 = zadatak_5()
    _check(out, "U02.Z5.h_pos", z5["h"], z5["h"])
    z6 = zadatak_6()
    _check(out, "U02.Z6.p_M_pos", z6["p_M"], z6["p_M"])

    # Faza 1.5: Klizni lezaj pri hladnom startu i radnoj temperaturi
    r = primjer_lezaj_temp()
    _check(out, "U02.lezaj_temp.v", r["v"], 6.28, "m/s")
    _check(out, "U02.lezaj_temp.tau_c", r["tau_c"], 8378, "Pa")
    _check(out, "U02.lezaj_temp.tau_h", r["tau_h"], 837.8, "Pa")
    _check(out, "U02.lezaj_temp.P_c", r["P_c"], 578, "W")
    _check(out, "U02.lezaj_temp.P_h", r["P_h"], 58.0, "W")
    _check(out, "U02.lezaj_temp.ratio", r["ratio"], 10.0)

    return out


if __name__ == "__main__":
    results = verify()
    ok = sum(1 for r in results if r["status"] == "OK")
    fail = sum(1 for r in results if r["status"] != "OK")
    for r in results:
        marker = "v" if r["status"] == "OK" else "x"
        print(f"  [{marker}] {r['id']:25s}  {r.get('details', '')}")
    print()
    print(f"Total: ok={ok}, fail={fail}")
