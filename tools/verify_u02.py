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


def _invariant(out: list, rid: str, condition: bool, details: str):
    out.append({
        "id": rid,
        "status": "OK" if condition else "FAIL",
        "verification": "invariant",
        "details": "" if condition else details,
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


def primjer_lab_on_chip(d=60e-6, sigma=0.055, theta_deg=25.0,
                         rho=1010.0, theta_hydrophobic_deg=110.0, g=9.81):
    theta = math.radians(theta_deg)
    h = 4 * sigma * math.cos(theta) / (rho * g * d)
    dp = 4 * sigma * math.cos(theta) / d
    h_hydrophobic = (
        4 * sigma * math.cos(math.radians(theta_hydrophobic_deg)) / (rho * g * d)
    )
    return {"h": h, "dp": dp, "h_hydrophobic": h_hydrophobic}


def zadatak_1(delta=2.4e-3, A=0.22, v=0.65, mu=0.84):
    dvdy = v / delta
    tau = mu * dvdy
    F = tau * A
    return {"dvdy": dvdy, "tau": tau, "F": F}


def zadatak_2(d=1.20e-3, sigma=0.030):
    dp_drop = 4 * sigma / d
    dp_bubble = 8 * sigma / d
    return {"dp_drop": dp_drop, "dp_bubble": dp_bubble,
            "ratio": dp_bubble / dp_drop}


def zadatak_3(A=0.020, v=0.30, delta_1=1.0e-3, delta_2=2.0e-3, mu=0.12):
    tau_1 = mu * v / delta_1
    tau_2 = mu * v / delta_2
    F_1, F_2 = tau_1 * A, tau_2 * A
    return {"tau_1": tau_1, "tau_2": tau_2, "F_1": F_1, "F_2": F_2,
            "F": F_1 + F_2, "F_wrong": mu * A * v / (delta_1 + delta_2)}


def zadatak_4(d1=0.60e-3, d2=1.20e-3, sigma=0.022, theta_deg=18.0, rho=790.0, g=9.81):
    cos_t = math.cos(math.radians(theta_deg))
    h1 = 4 * sigma * cos_t / (rho * g * d1)
    h2 = 4 * sigma * cos_t / (rho * g * d2)
    return {"h1": h1, "h2": h2}


def zadatak_5(S=0.010, delta=1.0e-3, velocities=(0.10, 0.20, 0.40),
              forces_a=(0.20, 0.40, 0.80), forces_b=(0.30, 0.45, 0.60), v_star=0.30):
    gradients = [v / delta for v in velocities]
    tau_a = [F / S for F in forces_a]
    tau_b = [F / S for F in forces_b]
    mu_a = [tau / rate for tau, rate in zip(tau_a, gradients, strict=True)]
    mu_b = [tau / rate for tau, rate in zip(tau_b, gradients, strict=True)]
    def constant(values):
        return all(math.isclose(value, values[0], rel_tol=1e-10) for value in values)
    return {"gradients": gradients, "tau_a": tau_a, "tau_b": tau_b,
            "mu_a": mu_a, "mu_b": mu_b,
            "newton_a": constant(mu_a), "newton_b": constant(mu_b),
            "F_star": mu_a[0] * S * v_star / delta,
            "F_b_wrong": mu_b[0] * S * velocities[-1] / delta}


def zadatak_6(d=0.50e-3, sigma=0.072, rho=998.0, g=9.81, theta_deg=0.0,
               H=0.042, D=1.8e-3, D_min=1.6e-3, D_max=2.0e-3,
               regulator_low=500.0, regulator_high=600.0):
    cos_t = math.cos(math.radians(theta_deg))
    h_cap = 4 * sigma * cos_t / (rho * g * d)
    dp = 4 * sigma / D
    # Two separate interface configurations: no meniscus credit once a drop exists.
    p_start = max(rho * g * H - 4 * sigma * cos_t / d, 0.0)
    p_drop = rho * g * H + dp
    p_min = rho * g * H + 4 * sigma / D_max
    p_max = rho * g * H + 4 * sigma / D_min
    required = max(p_start, p_max)
    return {"h_cap": h_cap, "dp": dp, "p_start": p_start, "p_drop": p_drop,
            "p_min": p_min, "p_max": p_max, "reserve": regulator_high - required,
            "low_sufficient": regulator_low >= required,
            "high_sufficient": regulator_high >= required}


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

    r = cjeloviti_mikrodozator()
    _check(out, "U02.CH1.h_cap_mm", r["h_cap"] * 1000, 36.8, "mm")
    _check(out, "U02.CH1.dp", r["dp"], 120.0, "Pa")
    _check(out, "U02.CH1.p_in_Pa", r["p_in"], 101445.0, "Pa")
    _check(out, "U02.CH1.p_M_min", r["p_M_min"], 347.0, "Pa", rel=0.03)

    z1 = zadatak_1()
    _check(out, "U02.Z1.dvdy", z1["dvdy"], 271.0, "1/s")
    _check(out, "U02.Z1.tau", z1["tau"], 228.0, "Pa")
    _check(out, "U02.Z1.F", z1["F"], 50.0, "N")
    _invariant(out, "U02.Z1.force_balance", abs(z1["F"] * 0.0024 - 0.84 * 0.65 * 0.22) < 1e-12,
               "Newtonova bilanca sile nije zadovoljena.")

    z2 = zadatak_2()
    _check(out, "U02.Z2.dp_drop", z2["dp_drop"], 100.0, "Pa")
    _check(out, "U02.Z2.dp_bubble", z2["dp_bubble"], 200.0, "Pa")
    _check(out, "U02.Z2.ratio", z2["ratio"], 2.0)
    doubled_drop = zadatak_2(d=2.4e-3)
    _invariant(out, "U02.Z2.diameter_scaling",
               abs(doubled_drop["dp_drop"] * 2 - z2["dp_drop"]) < 1e-12
               and abs(doubled_drop["dp_bubble"] * 2 - z2["dp_bubble"]) < 1e-12,
               "Dvostruki promjer mora prepoloviti oba skoka tlaka.")

    z3 = zadatak_3()
    _check(out, "U02.Z3.tau_1", z3["tau_1"], 36.0, "Pa")
    _check(out, "U02.Z3.tau_2", z3["tau_2"], 18.0, "Pa")
    _check(out, "U02.Z3.F_1", z3["F_1"], 0.72, "N")
    _check(out, "U02.Z3.F_2", z3["F_2"], 0.36, "N")
    _check(out, "U02.Z3.F", z3["F"], 1.08, "N")
    _check(out, "U02.Z3.F_wrong", z3["F_wrong"], 0.24, "N")
    equal_gaps = zadatak_3(delta_2=1.0e-3)
    _invariant(out, "U02.Z3.equal_gaps", abs(equal_gaps["F"] - 2 * z3["F_1"]) < 1e-12,
               "Jednaki procjepi moraju dati dva jednaka doprinosa.")
    far_wall = zadatak_3(delta_2=1.0e6)
    _invariant(out, "U02.Z3.far_wall_limit", abs(far_wall["F"] - z3["F_1"]) < 1e-8,
               "Udaljena donja stijenka mora dati zanemariv doprinos unutar modela.")
    _invariant(out, "U02.Z3.reverse_motion", abs(zadatak_3(v=-0.30)["F"] + z3["F"]) < 1e-12,
               "Promjena smjera brzine mora promijeniti smjer potrebne vucne sile.")

    z4 = zadatak_4()
    _check(out, "U02.Z4.h1_mm", z4["h1"] * 1000, 18.0, "mm")
    _check(out, "U02.Z4.h2_mm", z4["h2"] * 1000, 9.0, "mm")
    _invariant(out, "U02.Z4.inverse_diameter", abs(z4["h1"] / z4["h2"] - 2.0) < 1e-12,
               "Udvostrucenje promjera nije prepolovilo kapilarni uspon.")

    z5 = zadatak_5()
    _check(out, "U02.Z5.gradient_1", z5["gradients"][0], 100.0, "1/s")
    _check(out, "U02.Z5.gradient_2", z5["gradients"][1], 200.0, "1/s")
    _check(out, "U02.Z5.gradient_3", z5["gradients"][2], 400.0, "1/s")
    _check(out, "U02.Z5.tau_a1", z5["tau_a"][0], 20.0, "Pa")
    _check(out, "U02.Z5.tau_a2", z5["tau_a"][1], 40.0, "Pa")
    _check(out, "U02.Z5.tau_a3", z5["tau_a"][2], 80.0, "Pa")
    _check(out, "U02.Z5.tau_b1", z5["tau_b"][0], 30.0, "Pa")
    _check(out, "U02.Z5.tau_b2", z5["tau_b"][1], 45.0, "Pa")
    _check(out, "U02.Z5.tau_b3", z5["tau_b"][2], 60.0, "Pa")
    _check(out, "U02.Z5.mu_a1", z5["mu_a"][0], 0.20, "Pa s")
    _check(out, "U02.Z5.mu_a2", z5["mu_a"][1], 0.20, "Pa s")
    _check(out, "U02.Z5.mu_a3", z5["mu_a"][2], 0.20, "Pa s")
    _check(out, "U02.Z5.mu_b1", z5["mu_b"][0], 0.30, "Pa s")
    _check(out, "U02.Z5.mu_b2", z5["mu_b"][1], 0.225, "Pa s")
    _check(out, "U02.Z5.mu_b3", z5["mu_b"][2], 0.15, "Pa s")
    _check(out, "U02.Z5.F_star", z5["F_star"], 0.60, "N")
    _check(out, "U02.Z5.F_b_wrong", z5["F_b_wrong"], 1.20, "N")
    _invariant(out, "U02.Z5.model_selection", z5["newton_a"] and not z5["newton_b"],
               "Samo uzorak A dopusta stalan omjer naprezanja i gradijenta.")
    perturbed = zadatak_5(forces_a=(0.20, 0.40, 0.70))
    _invariant(out, "U02.Z5.use_all_measurements", not perturbed["newton_a"],
               "Odluka o modelu mora uzeti u obzir i trece mjerenje.")
    swapped = zadatak_5(forces_a=(0.30, 0.45, 0.60), forces_b=(0.20, 0.40, 0.80))
    _invariant(out, "U02.Z5.selection_follows_data", swapped["newton_b"] and not swapped["newton_a"],
               "Izbor modela mora slijediti podatke, ne ime uzorka.")

    z6 = zadatak_6()
    _check(out, "U02.Z6.h_cap_mm", z6["h_cap"] * 1000, 58.8, "mm")
    _check(out, "U02.Z6.p_start", z6["p_start"], 0.0, "Pa")
    _check(out, "U02.Z6.p_drop_kPa", z6["p_drop"] / 1000, 0.571, "kPa")
    _check(out, "U02.Z6.p_min_kPa", z6["p_min"] / 1000, 0.555, "kPa")
    _check(out, "U02.Z6.p_max_kPa", z6["p_max"] / 1000, 0.591, "kPa")
    _check(out, "U02.Z6.reserve_Pa", z6["reserve"], 8.8, "Pa")
    _invariant(out, "U02.Z6.regulator_selection", not z6["low_sufficient"] and z6["high_sufficient"],
               "Samo regulator do 0.60 kPa pokriva oba zadana staticka stanja.")
    wider_needle = zadatak_6(d=1.0e-3)
    _invariant(out, "U02.Z6.separate_interfaces",
               wider_needle["p_start"] > 0 and abs(wider_needle["p_drop"] - z6["p_drop"]) < 1e-12,
               "Promjer igle utjece na punjenje, ali ne na tlak vec formirane kapljice zadanog D.")
    small_drop, large_drop = zadatak_6(D=1.6e-3), zadatak_6(D=2.0e-3)
    _invariant(out, "U02.Z6.diameter_bounds",
               abs(small_drop["p_drop"] - z6["p_max"]) < 1e-12
               and abs(large_drop["p_drop"] - z6["p_min"]) < 1e-12
               and z6["p_min"] < z6["p_drop"] < z6["p_max"],
               "Manja kapljica mora odrediti vecu potrebnu vrijednost tlaka.")
    _invariant(out, "U02.Z6.insufficient_range",
               not zadatak_6(regulator_high=580.0)["high_sufficient"],
               "Regulator koji pokriva nominalno stanje ne mora pokriti najmanju kapljicu.")


    # Faza 1.5: Klizni lezaj pri hladnom startu i radnoj temperaturi
    r = primjer_lezaj_temp()
    _check(out, "U02.lezaj_temp.v", r["v"], 6.28, "m/s")
    _check(out, "U02.lezaj_temp.tau_c", r["tau_c"], 8378, "Pa")
    _check(out, "U02.lezaj_temp.tau_h", r["tau_h"], 837.8, "Pa")
    _check(out, "U02.lezaj_temp.P_c", r["P_c"], 578, "W")
    _check(out, "U02.lezaj_temp.P_h", r["P_h"], 58.0, "W")
    _check(out, "U02.lezaj_temp.ratio", r["ratio"], 10.0)

    r = primjer_lab_on_chip()
    _check(out, "U02.lab_chip.h_cm", r["h"] * 100, 33.5, "cm", rel=0.02)
    _check(out, "U02.lab_chip.dp_kPa", r["dp"] / 1000, 3.32, "kPa", rel=0.02)
    _check(out, "U02.lab_chip.h_hydrophobic", r["h_hydrophobic"], -0.127, "m", rel=0.02)

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
