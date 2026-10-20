"""Numericka verifikacija U03: Hidrostaticka raspodjela tlaka i manometrija."""
from __future__ import annotations

import math
from itertools import product

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


def primjer_1(rho=998.0, p_pl_m=18e3, h=1.40, p_atm=100.8e3, g=9.81):
    p_pl = p_atm + p_pl_m
    p_A = p_pl + rho * g * h
    p_A_m = p_A - p_atm
    return {"p_pl": p_pl, "p_A": p_A, "p_A_m": p_A_m}


def primjer_3(rho_v=1000.0, rho_mv=1035.0, rho_Hg=13600.0, rho_zr=1.2,
              h1=0.60, h2=0.10, h3=0.70, h4=0.40, g=9.81):
    dp_bez_zraka = g * (rho_Hg * h2 - rho_mv * h4 - rho_v * h1)
    dp_sa_zrakom = g * (rho_Hg * h2 + rho_zr * h3 - rho_mv * h4 - rho_v * h1)
    return {"dp_bez_zraka": dp_bez_zraka, "dp_sa_zrakom": dp_sa_zrakom}


def cjeloviti_sondiranje(p_dno=141.0e3, p_pl=3.0e3, rho_o=860.0, rho_w=1025.0,
                         h_w=0.35, H_ref=18.60, U_m=2.31, A_t=600.0,
                         p_atm=101.0e3, rho_pl=1.2, g=9.81):
    """P3: sondiranje teretnog tanka s tlacnim mjeracem razine (U03, cjeloviti)."""
    p_water = rho_w * g * h_w
    h_o = (p_dno - p_pl - p_water) / (rho_o * g)
    U = H_ref - h_w - h_o
    p_aps = p_atm + p_dno
    h_single = (p_dno - p_pl) / (rho_o * g)          # vodeni talog racunan kao ulje
    h_nogas = (p_dno - p_water) / (rho_o * g)        # zaboravljen pretlak plina
    return {
        "p_water": p_water, "h_o": h_o, "U": U, "U_m": U_m, "p_aps": p_aps,
        "h_single": h_single, "dV_single": (h_single - h_o) * A_t,
        "h_nogas": h_nogas, "dV_nogas": (h_nogas - h_o) * A_t,
        "p_gas_column": rho_pl * g * U,
    }


def primjer_pumpa(H=2.40, rho=870.0, p_atm=101.3e3, p_v=200.0, g=9.81):
    p_man = -rho * g * H
    p_aps = p_atm + p_man
    H_max = (p_atm - p_v) / (rho * g)
    return {"p_man": p_man, "p_aps": p_aps, "H_max": H_max}


def primjer_balastni(T_g=8.5, H_t=5.0, h_p=2.0, h_s=3.0,
                     rho_m=1025.0, rho_b=1025.0, g=9.81):
    """P5: bocni balastni tank s morskom vodom izvana i iznutra."""
    p_ext_dno = rho_m * g * T_g
    p_ext_P = rho_m * g * (T_g - h_p)
    p_int_dno_A = rho_b * g * H_t
    p_int_P_A = rho_b * g * (H_t - h_p)
    return {
        "p_ext_dno": p_ext_dno, "p_ext_P": p_ext_P,
        "p_int_dno_A": p_int_dno_A, "p_int_P_A": p_int_P_A,
        "delta_dno_A": p_ext_dno - p_int_dno_A,
        "delta_P_A": p_ext_P - p_int_P_A,
        "delta_dno_B": p_ext_dno,
        "delta_P_B": p_ext_P,
        "ullage_C": H_t - h_s,
        "delta_dno_C": p_ext_dno - rho_b * g * h_s,
        "uniform_net": rho_m * g * (T_g - H_t),
    }


def primjer_vodotoranj(p_A=520e3, dz=38.0, rho=998.0,
                       p_atm=101.3e3, dp_alarm=50e3, g=9.81):
    """P6: tlak u mrezi iz kote vodotornja i IoT senzor."""
    hydrostatic_drop = rho * g * dz
    p_B_gauge = p_A - hydrostatic_drop
    h_tower = p_B_gauge / (rho * g)
    equivalent_head = dp_alarm / (rho * g)
    return {
        "hydrostatic_drop": hydrostatic_drop,
        "p_B_gauge": p_B_gauge,
        "p_B_abs": p_B_gauge + p_atm,
        "h_tower": h_tower,
        "head_A": p_A / (rho * g),
        "equivalent_head": equivalent_head,
        "h_tower_after": h_tower - equivalent_head,
    }


def zadatak_1(p0=101.3e3, p=84.5e3, T0=288.0, R=287.0, g=9.81, dp_sensor=10.0):
    """Z1: visina leta iz barometarskog ocitanja; izotermalna atmosfera prema stalnoj gustoci."""
    H = R * T0 / g
    z_iso = H * math.log(p0 / p)
    rho0 = p0 / (R * T0)
    z_lin = (p0 - p) / (rho0 * g)
    rho_top = p / (R * T0)
    # neovisna integracija dp/dz = -rho g s rho = p/(R T0) (Eulerova metoda po tlaku)
    n = 20000; pp = p0; z = 0.0; dp = (p0 - p) / n
    for _ in range(n):
        rho_mid = (pp - dp / 2) / (R * T0)
        z += dp / (rho_mid * g); pp -= dp
    return {"H": H, "z_iso": z_iso, "rho0": rho0, "z_lin": z_lin,
            "rel": (z_lin - z_iso) / z_iso, "dz_top": dp_sensor / (rho_top * g),
            "dz_base": dp_sensor / (rho0 * g), "z_num": z}


def zadatak_2(dp=17.62e3, rho=998.0, gas_change=5e3, g=9.81):
    h = dp / (rho * g)
    return {"h": h, "dp_after": (dp + gas_change) - gas_change}


def zadatak_3(D=0.040, d=0.005, alpha_deg=15.0, rho=820.0, L=0.185, g=9.81):
    """Z3: nagnuti manometar s posudom; spustanje razine u posudi iz jednakosti volumena."""
    sin_a = math.sin(math.radians(alpha_deg))
    area_ratio = (d / D) ** 2
    well_drop = L * area_ratio
    h_simple = L * sin_a
    h_exact = h_simple + well_drop
    p_simple = rho * g * h_simple
    p_exact = rho * g * h_exact
    sens = 1 / (rho * g * (sin_a + area_ratio))
    sens_u = 1 / (rho * g)
    return {"area_ratio": area_ratio, "well_drop": well_drop, "h_simple": h_simple,
            "h_exact": h_exact, "p_simple": p_simple, "p_exact": p_exact,
            "rel_err": (p_simple - p_exact) / p_exact, "sens": sens, "sens_u": sens_u,
            "gain": sens / sens_u}


def zadatak_4(rho_u=850.0, rho_w=1000.0, H=1.50, p_bottom=13.83e3, g=9.81):
    h_u = (rho_w * g * H - p_bottom) / ((rho_w - rho_u) * g)
    h_w = H - h_u
    return {"h_u": h_u, "h_w": h_w, "p_interface": rho_u * g * h_u,
            "p_oil_only": rho_u * g * H, "p_water_only": rho_w * g * H,
            "gradient_oil": rho_u * g, "gradient_water": rho_w * g}


def zadatak_5(p_vac=6e3, p_atm=98.6e3, rho_u=860.0, rho_w=998.0,
              rho_Hg=13600.0, dh_max=0.650, h_error=0.001, p_error_max=20.0, g=9.81):
    densities = (rho_u, rho_w, rho_Hg)
    heights = tuple(p_vac / (rho * g) for rho in densities)
    errors = tuple(rho * g * h_error for rho in densities)
    feasible = tuple(h <= dh_max and error <= p_error_max
                     for h, error in zip(heights, errors))
    return {"heights": heights, "errors": errors, "feasible": feasible,
            "p_g_aps": p_atm - p_vac}


def zadatak_6(h1=0.65, dh=0.210, h_tocka=1.30, rho_w=998.0, rho_Hg=13600.0,
              p_atm=100.9e3, dh_tol=0.002, h_tol=0.005,
              p_atm_tol=0.4e3, scale_margin=0.05, g=9.81):
    # Granica vode i zive je na visini prikljucka u svim dopustenim stanjima.
    p_priklj = p_atm + rho_Hg * g * dh
    p_G = p_priklj - rho_w * g * h1
    p_tocka = p_G + rho_w * g * h_tocka
    p_max = (
        p_atm + p_atm_tol
        + rho_Hg * g * (dh + dh_tol)
        - rho_w * g * (h1 - h_tol)
        + rho_w * g * (h_tocka + h_tol)
    )
    return {
        "p_G": p_G,
        "p_tocka": p_tocka,
        "p_max": p_max,
        "required_full_scale": (1 + scale_margin) * p_max,
    }


def verify():
    out = []

    r = primjer_1()
    _check(out, "U03.P1.p_pl_kPa", r["p_pl"] / 1000, 118.8, "kPa")
    _check(out, "U03.P1.p_A_kPa", r["p_A"] / 1000, 132.506532, "kPa", rel=1e-9)
    _check(out, "U03.P1.p_A_m_kPa", r["p_A_m"] / 1000, 31.706532, "kPa", rel=1e-9)

    r = primjer_3()
    _check(out, "U03.P3.dp_bez_zraka_Pa", r["dp_bez_zraka"], 3394.26, "Pa", rel=1e-9)
    _check(out, "U03.P3.dp_sa_zrakom_Pa", r["dp_sa_zrakom"], 3402.50, "Pa", rel=2e-7)

    r = cjeloviti_sondiranje()
    _check(out, "U03.CH1.p_water_Pa", r["p_water"], 3519.3, "Pa", rel=2e-5)
    _check(out, "U03.CH1.h_o_m", r["h_o"], 15.940, "m", rel=1e-4)
    _check(out, "U03.CH1.U_m", r["U"], 2.310, "m", rel=1e-3)
    _check(out, "U03.CH1.p_aps_dno_kPa", r["p_aps"] / 1000, 242.0, "kPa", rel=1e-9)
    _check(out, "U03.CH1.h_single_fluid_m", r["h_single"], 16.357, "m", rel=5e-5)
    _check(out, "U03.CH1.dV_single_fluid_m3", r["dV_single"], 250.0, "m3", rel=2e-3)
    _check(out, "U03.CH1.h_no_gas_m", r["h_nogas"], 16.296, "m", rel=5e-5)
    _check(out, "U03.CH1.dV_no_gas_m3", r["dV_nogas"], 213.0, "m3", rel=2e-3)
    _check(out, "U03.CH1.gas_column_Pa", r["p_gas_column"], 27.2, "Pa", rel=2e-3)
    _invariant(out, "U03.CH1.ullage_tape_agreement",
               abs(r["U"] - r["U_m"]) < 1e-3,
               "Ullage iz tlaka i ullage vrpce moraju se slagati unutar 1 mm.")
    _invariant(out, "U03.CH1.geometry_closure",
               abs(r["h_o"] + 0.35 + r["U"] - 18.60) < 1e-12,
               "Stupci ulja, vode i ullage ne zatvaraju visinu do referentne tocke.")
    _invariant(out, "U03.CH1.simplifications_overestimate",
               r["h_single"] > r["h_nogas"] > r["h_o"],
               "Oba pojednostavljenja moraju precijeniti stupac ulja.")
    _invariant(out, "U03.CH1.gas_column_negligible",
               r["p_gas_column"] < 1e-3 * 141.0e3,
               "Stupac inertnog plina mora biti ispod promila ocitanja na dnu.")

    r = primjer_pumpa()
    _check(out, "U03.pumpa.p_man_kPa", r["p_man"] / 1000, -20.48328, "kPa", rel=1e-9)
    _check(out, "U03.pumpa.p_aps_kPa", r["p_aps"] / 1000, 80.81672, "kPa", rel=1e-9)
    _check(out, "U03.pumpa.H_max_m", r["H_max"], 11.8, "m")

    z1 = zadatak_1()
    _check(out, "U03.Z1.H_m", z1["H"], 8426.0, "m")
    _check(out, "U03.Z1.z_iso_m", z1["z_iso"], 1528.0, "m")
    _check(out, "U03.Z1.rho0", z1["rho0"], 1.226, "kg/m^3")
    _check(out, "U03.Z1.z_lin_m", z1["z_lin"], 1397.0, "m")
    _check(out, "U03.Z1.rel_percent", z1["rel"] * 100, -8.5, "%", rel=0.02)
    _check(out, "U03.Z1.dz_top_m", z1["dz_top"], 1.0, "m", rel=0.01)
    _check(out, "U03.Z1.dz_base_m", z1["dz_base"], 0.83, "m", rel=0.01)
    _invariant(out, "U03.Z1.numeric_integration",
               abs(z1["z_num"] - z1["z_iso"]) / z1["z_iso"] < 1e-6,
               "Integracija dp/dz = -rho g s rho = p/(R T) ne vraca izotermalnu visinu.")
    small = zadatak_1(p=101.3e3 - 100.0)
    _invariant(out, "U03.Z1.constant_density_limit",
               z1["z_lin"] < z1["z_iso"] and abs(small["rel"]) < 1e-3,
               "Stalna gustoca mora podcijeniti visinu, a za mali pad tlaka oba modela moraju se slagati.")
    z2 = zadatak_2()
    _check(out, "U03.Z2.h_m", z2["h"], 1.80, "m", rel=0.0005)
    _check(out, "U03.Z2.dp_after_kPa", z2["dp_after"] / 1000, 17.62, "kPa", rel=1e-9)
    _invariant(out, "U03.Z2.depth_balance",
               abs(998 * 9.81 * z2["h"] - 17620) < 1e-8,
               "Rekonstruirana visina ne daje zadanu razliku tlakova.")
    _invariant(out, "U03.Z2.common_pressure_shift",
               abs(zadatak_2(gas_change=-20e3)["dp_after"] - z2["dp_after"]) < 1e-8,
               "Zajednicka promjena tlaka ne smije promijeniti diferencijalno ocitanje.")
    z3 = zadatak_3()
    _check(out, "U03.Z3.area_ratio", z3["area_ratio"], 0.015625, "1")
    _check(out, "U03.Z3.h_simple_mm", z3["h_simple"] * 1000, 47.9, "mm")
    _check(out, "U03.Z3.p_simple_Pa", z3["p_simple"], 385.0, "Pa")
    _check(out, "U03.Z3.well_drop_mm", z3["well_drop"] * 1000, 2.9, "mm", rel=0.01)
    _check(out, "U03.Z3.h_exact_mm", z3["h_exact"] * 1000, 50.8, "mm")
    _check(out, "U03.Z3.p_exact_Pa", z3["p_exact"], 408.0, "Pa")
    _check(out, "U03.Z3.rel_err_percent", z3["rel_err"] * 100, -5.7, "%", rel=0.01)
    _check(out, "U03.Z3.sens_mm_per_Pa", z3["sens"] * 1000, 0.45, "mm/Pa", rel=0.01)
    _check(out, "U03.Z3.sens_u_mm_per_Pa", z3["sens_u"] * 1000, 0.124, "mm/Pa", rel=0.01)
    _check(out, "U03.Z3.gain", z3["gain"], 3.6, "1", rel=0.02)
    _invariant(out, "U03.Z3.volume_conservation",
               abs(math.pi * 0.005**2 / 4 * 0.185 - math.pi * 0.040**2 / 4 * z3["well_drop"]) < 1e-15,
               "Istisnuti volumen cjevcice mora biti jednak volumenu spustene razine u posudi.")
    steeper = zadatak_3(alpha_deg=30.0); vertical = zadatak_3(alpha_deg=90.0)
    _invariant(out, "U03.Z3.sensitivity_falls_with_angle",
               z3["gain"] > steeper["gain"] > vertical["gain"] and abs(vertical["gain"] - 1 / (1 + z3["area_ratio"])) < 1e-12,
               "Osjetljivost mora padati s kutom i pri 90 stupnjeva teziti jednoj nozi s korekcijom posude.")
    wide_well = zadatak_3(D=0.400)
    _invariant(out, "U03.Z3.wide_well_limit",
               abs(wide_well["p_exact"] / wide_well["p_simple"] - 1) < 2e-3,
               "Vrlo siroka posuda mora ukloniti razliku izmedu tocnog i pojednostavljenog tlaka.")
    z4 = zadatak_4()
    _check(out, "U03.Z4.h_oil_m", z4["h_u"], .601, "m", rel=.001)
    _check(out, "U03.Z4.h_water_m", z4["h_w"], .899, "m", rel=.001)
    _check(out, "U03.Z4.p_interface_kPa", z4["p_interface"] / 1000, 5.015, "kPa", rel=1e-8)
    _check(out, "U03.Z4.p_oil_only_kPa", z4["p_oil_only"] / 1000, 12.508, "kPa", rel=.0001)
    _check(out, "U03.Z4.p_water_only_kPa", z4["p_water_only"] / 1000, 14.715, "kPa", rel=1e-8)
    _check(out, "U03.Z4.gradient_oil_kPa_m", z4["gradient_oil"] / 1000, 8.339, "kPa/m", rel=.0001)
    _check(out, "U03.Z4.gradient_water_kPa_m", z4["gradient_water"] / 1000, 9.810, "kPa/m", rel=1e-8)
    _invariant(out, "U03.Z4.layer_balances",
               abs(z4["h_u"] + z4["h_w"] - 1.5) < 1e-12
               and abs(9.81 * (850*z4["h_u"] + 1000*z4["h_w"]) - 13830) < 1e-8
               and 0 < z4["h_u"] < 1.5 and 0 < z4["h_w"] < 1.5,
               "Slojevi ne zatvaraju geometriju i hidrostatski tlak.")
    _invariant(out, "U03.Z4.pure_fluid_limits",
               abs(zadatak_4(p_bottom=14715)["h_u"]) < 1e-12
               and abs(zadatak_4(p_bottom=12507.75)["h_w"]) < 1e-12,
               "Granice ciste vode i ulja moraju ukloniti drugi sloj.")
    z5 = zadatak_5()
    _check(out, "U03.Z5.h_oil_m", z5["heights"][0], .711, "m", rel=.001)
    _check(out, "U03.Z5.h_water_m", z5["heights"][1], .613, "m", rel=.001)
    _check(out, "U03.Z5.h_Hg_m", z5["heights"][2], .04497, "m", rel=.0001)
    _check(out, "U03.Z5.error_oil_Pa", z5["errors"][0], 8.44, "Pa", rel=.001)
    _check(out, "U03.Z5.error_water_Pa", z5["errors"][1], 9.79, "Pa", rel=.001)
    _check(out, "U03.Z5.error_Hg_Pa", z5["errors"][2], 133.42, "Pa", rel=.0001)
    _check(out, "U03.Z5.p_g_aps_kPa", z5["p_g_aps"] / 1000, 92.6, "kPa", rel=1e-9)
    _invariant(out, "U03.Z5.both_constraints", z5["feasible"] == (False, True, False),
               "Samo voda zadovoljava visinu i pogresku.")
    _invariant(out, "U03.Z5.constraint_sensitivity",
               zadatak_5(dh_max=.8)["feasible"] == (True, True, False)
               and zadatak_5(p_error_max=150)["feasible"] == (False, True, True),
               "Izbor mora reagirati na oba mjerna ogranicenja.")
    _invariant(out, "U03.Z5.pressure_reconstruction",
               all(abs(z5["p_g_aps"] + rho*9.81*h - 98600) < 1e-8
                   for rho,h in zip((860,998,13600), z5["heights"])),
               "Uspon od atmosfere do vise razine mora dati isti podtlak za sve fluide.")
    z6 = zadatak_6()
    _check(out, "U03.Z6.p_G_kPa", z6["p_G"] / 1000, 122.6, "kPa")
    _check(out, "U03.Z6.p_tocka_kPa", z6["p_tocka"] / 1000, 135.3, "kPa")
    _check(out, "U03.Z6.p_max_kPa", z6["p_max"] / 1000, 136.05, "kPa", rel=0.00005)
    _check(out, "U03.Z6.required_full_scale_kPa", z6["required_full_scale"] / 1000, 142.85, "kPa", rel=0.00005)
    corners = [pa + 13600*9.81*dh + 998*9.81*(h2-h1)
               for pa,dh,h1,h2 in product((100500,101300),(.208,.212),(.645,.655),(1.295,1.305))]
    _invariant(out, "U03.Z6.interval_corners", abs(max(corners)-z6["p_max"]) < 1e-8,
               "Analiticka granica mora odgovarati najvecem tlaku svih rubnih kombinacija.")
    _invariant(out, "U03.Z6.manometer_walk",
               abs(z6["p_G"] + 998*9.81*.65 - 13600*9.81*.210 - 100900) < 1e-8,
               "Hod preko razdjelnice na visini prikljucka ne zatvara tlak.")
    _invariant(
        out,
        "U03.Z6.sensor_range_choice",
        140e3 < z6["required_full_scale"] <= 160e3,
        "Ocekivani omotac ne zahtijeva deklarirani raspon 0--160 kPa.",
    )

    _invariant(
        out,
        "U03.INV.absolute_gauge_offset",
        abs((primjer_1()["p_A"] - primjer_1()["p_A_m"]) - 100.8e3) < 1e-9,
        "Apsolutni i manometarski tlak ne razlikuju se za p_atm.",
    )
    _invariant(
        out,
        "U03.INV.pressure_increases_with_depth",
        primjer_1()["p_A"] > primjer_1()["p_pl"] and z6["p_tocka"] > z6["p_G"],
        "Tlak u istom mirnom fluidu nije porastao s dubinom.",
    )
    _invariant(
        out,
        "U03.INV.manometer_pressure_signs",
        z5["p_g_aps"] < 98.6e3 and z6["p_G"] > 100.9e3,
        "Vakuumski i nadtlacni manometar nemaju ocekivane predznake.",
    )

    # P5: bocni balastni tank broda (morska voda izvana i iznutra)
    r = primjer_balastni()
    _check(out, "U03.balastni.p_ext_dno_kPa", r["p_ext_dno"] / 1000, 85.47, "kPa", rel=5e-5)
    _check(out, "U03.balastni.p_ext_P_kPa", r["p_ext_P"] / 1000, 65.36, "kPa", rel=2e-5)
    _check(out, "U03.balastni.p_int_dno_A_kPa", r["p_int_dno_A"] / 1000, 50.28, "kPa", rel=1e-4)
    _check(out, "U03.balastni.p_int_P_A_kPa", r["p_int_P_A"] / 1000, 30.17, "kPa", rel=2e-4)
    _check(out, "U03.balastni.delta_dno_A_kPa", r["delta_dno_A"] / 1000, 35.19, "kPa", rel=1e-4)
    _check(out, "U03.balastni.delta_P_A_kPa", r["delta_P_A"] / 1000, 35.19, "kPa", rel=1e-4)
    _check(out, "U03.balastni.delta_dno_B_kPa", r["delta_dno_B"] / 1000, 85.47, "kPa", rel=5e-5)
    _check(out, "U03.balastni.delta_P_B_kPa", r["delta_P_B"] / 1000, 65.36, "kPa", rel=2e-5)
    _check(out, "U03.balastni.ullage_C_m", r["ullage_C"], 2.0, "m", rel=1e-12)
    _check(out, "U03.balastni.delta_dno_C_kPa", r["delta_dno_C"] / 1000, 55.30, "kPa", rel=1e-4)
    _invariant(out, "U03.balastni.uniform_net_pressure",
               abs(r["delta_dno_A"] - r["delta_P_A"]) < 1e-9
               and abs(r["delta_dno_A"] - r["uniform_net"]) < 1e-9,
               "Jednake gustoce moraju dati jednolik neto tlak rho*g*(T_g-H_t) na zajednickoj oplati.")
    _invariant(out, "U03.balastni.state_ordering",
               r["delta_dno_B"] > r["delta_dno_C"] > r["delta_dno_A"] > 0,
               "Prazan tank mora opteretiti dno jace od djelomicno punog, a ovaj jace od punog.")
    _invariant(out, "U03.balastni.density_difference_gradient",
               abs(primjer_balastni(rho_b=1000.0)["delta_P_A"]
                   - primjer_balastni(rho_b=1000.0)["delta_dno_A"]
                   + 25 * 9.81 * 2.0) < 1e-9,
               "Pri razlicitim gustocama neto tlak mora rasti s dubinom za (rho_m-rho_b)*g.")

    # P6: tlak u mrezi iz kote vodotornja i IoT senzor
    r = primjer_vodotoranj()
    _check(out, "U03.iot.hydrostatic_drop_kPa", r["hydrostatic_drop"] / 1000, 372.0, "kPa", rel=1e-4)
    _check(out, "U03.iot.p_B_gauge_kPa", r["p_B_gauge"] / 1000, 148.0, "kPa", rel=3e-4)
    _check(out, "U03.iot.p_B_abs_kPa", r["p_B_abs"] / 1000, 249.3, "kPa", rel=2e-4)
    _check(out, "U03.iot.h_tower_m", r["h_tower"], 15.11, "m", rel=3e-4)
    _check(out, "U03.iot.head_A_m", r["head_A"], 53.1, "m", rel=3e-4)
    _check(out, "U03.iot.equivalent_head", r["equivalent_head"], 5.11, "m", rel=1e-3)
    _check(out, "U03.iot.h_tower_after_m", r["h_tower_after"], 10.0, "m", rel=1e-3)
    _invariant(out, "U03.iot.tower_level_closure",
               abs(r["h_tower"] + 38.0 - r["head_A"]) < 1e-9,
               "Kota slobodne povrsine vodotornja mora zatvoriti piezometarsku visinu u A.")

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
