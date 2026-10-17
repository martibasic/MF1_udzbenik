"""Numericka verifikacija U04: Relativno mirovanje fluida."""
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


def _invariant(out, rid, condition, details):
    out.append({
        "id": rid,
        "status": "OK" if condition else "FAIL",
        "verification": "invariant",
        "details": "" if condition else details,
    })


def primjer_1_kolica(L=1.60, h_0=0.42, a=1.35, g=9.81):
    dh = a * L / g
    h_str = h_0 + dh / 2
    h_pred = h_0 - dh / 2
    theta_deg = math.degrees(math.atan(a / g))
    return {"dh": dh, "h_str": h_str, "h_pred": h_pred, "theta_deg": theta_deg}


def primjer_3_modul(a=3.4, g=9.81, H=0.55, p_M_pl=16e3, rho=960.0):
    """P2: kosa stijenka usporedna s g_eff; raspodjela tlaka duz AB i tlak u B."""
    theta = math.atan(a / g)
    phi = math.pi / 2 - theta
    s = H / math.sin(phi)
    g_eff = math.sqrt(g**2 + a**2)
    gradient = rho * g_eff
    p_B = p_M_pl + gradient * s
    p_B_components = p_M_pl + rho * (g * H + a * s * math.cos(phi))
    return {
        "theta_deg": math.degrees(theta), "phi_deg": math.degrees(phi), "s": s,
        "g_eff": g_eff, "gradient": gradient, "p_B": p_B,
        "p_B_components": p_B_components, "dx": s * math.cos(phi),
    }


def primjer_brod_u_zavoju(v=6.17, R=180.0, B=9.0, h_0=1.60, H=2.20,
                          rho=1025.0, g=9.81):
    """P3: balastni tank broda u ustaljenom kruznom zavoju."""
    a = v**2 / R
    theta_deg = math.degrees(math.atan(a / g))
    dh = a * B / g
    h_v = h_0 + dh / 2
    h_u = h_0 - dh / 2
    a_max = 2 * g * (H - h_0) / B
    v_max = math.sqrt(a_max * R)
    omega = v / R
    dh_parabola = omega**2 * ((R + B / 2)**2 - (R - B / 2)**2) / (2 * g)
    return {
        "a": a, "theta_deg": theta_deg, "dh": dh, "h_v": h_v, "h_u": h_u,
        "overflow": h_v >= H, "a_max": a_max, "v_max": v_max,
        "v_max_kn": v_max / 0.5144, "dh_parabola": dh_parabola,
        "curvature_mm": omega**2 * B**2 / (24 * g) * 1000,
        "p_v": rho * g * h_v, "p_u": rho * g * h_u,
    }


def cjeloviti_1_rotacija(R=0.40, H=0.78, h_0=0.60, omega=5.20,
                          rho=1000.0, g=9.81):
    dh = omega**2 * R**2 / (2 * g)
    h_C = h_0 - dh / 2
    h_R = h_0 + dh / 2
    p_M_C = rho * g * h_C
    p_M_D = rho * g * h_R
    omega_max = math.sqrt(4 * g * (H - h_0) / R**2)
    n_max = 60 * omega_max / (2 * math.pi)
    return {
        "dh": dh, "h_C": h_C, "h_R": h_R,
        "p_M_C": p_M_C, "p_M_D": p_M_D,
        "omega_max": omega_max, "n_max": n_max,
    }


def primjer_5_autocisterna(L=1.20, h_0=0.45, H=0.80, a=3.8, rho=750.0, g=9.81):
    dh = a * L / g
    h_pred = h_0 + dh / 2
    h_str = h_0 - dh / 2
    a_overflow = 2 * g * (H - h_0) / L
    a_dry = 2 * g * h_0 / L
    return {
        "dh": dh,
        "h_pred": h_pred,
        "h_str": h_str,
        "a_overflow": a_overflow,
        "a_dry": a_dry,
    }


def primjer_separator(n=7200.0, r_o=0.045, r_w=0.047, r_2=0.120,
                      rho_o=930.0, rho_w=960.0, Q_lph=1500.0, H_b=0.15, g=9.81):
    """P6: centrifugalni separator goriva - tlak u bubnju i razdjelnica."""
    omega = 2 * math.pi * n / 60
    dp = 0.5 * rho_o * omega**2 * (r_2**2 - r_o**2)

    def interface(rho_oil):
        ri2 = (rho_w * r_w**2 - rho_oil * r_o**2) / (rho_w - rho_oil)
        return math.sqrt(ri2) if ri2 > 0 else float("nan")

    r_i = interface(rho_o)
    Q = Q_lph / 1000 / 3600
    V = math.pi * (r_2**2 - r_o**2) * H_b
    v_rel = Q / (2 * math.pi * r_i * H_b)
    return {
        "omega": omega, "acc_g": omega**2 * r_2 / g, "dp": dp,
        "r_i": r_i, "r_i_950": interface(950.0),
        "V": V, "t_res": V / Q, "v_rel": v_rel,
        "speed_ratio": v_rel / (omega * r_i),
        "coriolis_ratio": 2 * omega * v_rel / (omega**2 * r_i),
    }


def zadatak_1(L=1.80, h_0=0.34, a=1.20, H=0.46, g=9.81):
    dh = a * L / g
    h_str = h_0 + dh / 2
    h_pred = h_0 - dh / 2
    return {"dh": dh, "h_str": h_str, "h_pred": h_pred,
            "overflow": h_str >= H}


def zadatak_2(L=1.40, h_0=0.30, H=0.42, g=9.81):
    dh_max = 2 * (H - h_0)
    a_max = g * dh_max / L
    return {"a_max": a_max}


def zadatak_3(rho=870.0, h=0.75, a_z=2.3, g=9.81):
    dp = rho * (g + a_z) * h
    dp_0 = rho * g * h
    increase_percent = 100 * (dp / dp_0 - 1)
    return {"dp": dp, "dp_0": dp_0,
            "increase_percent": increase_percent,
            "dp_braking": rho * (g - a_z) * h}


def zadatak_4(r_A=.080, r_B=.240, p_A=12.40e3, p_B=14.00e3, rho=1000.0):
    dp = p_B - p_A
    omega = math.sqrt(2 * dp / (rho * (r_B**2 - r_A**2)))
    return {"dp": dp, "omega": omega, "rpm": 30 * omega / math.pi}


def zadatak_5(L=1.50, h_0=.300, H=.550, a=2.00, g=9.81,
              error_limit=.005, spread_limit=.004,
              samples_i=((.5,.520,.080),(1.0,.380,.220),(1.5,.500,.100)),
              samples_ii=((8.0,.454,.146),(8.5,.452,.148),(9.0,.453,.147))):
    h_str = h_0 + a * L / (2 * g)
    h_pred = h_0 - a * L / (2 * g)
    errors, spreads, accepted = [], [], []
    for samples in (samples_i, samples_ii):
        error = max(max(abs(hs-h_str), abs(hp-h_pred)) for _,hs,hp in samples)
        spread = max(max(row[col] for row in samples)-min(row[col] for row in samples)
                     for col in (1,2))
        errors.append(error)
        spreads.append(spread)
        accepted.append(error <= error_limit and spread <= spread_limit)
    return {"h_str": h_str, "h_pred": h_pred, "errors": errors,
            "spreads": spreads, "accepted": accepted,
            "reference_fits": 0 < h_pred <= h_str < H}


def zadatak_6(R=0.32, H=0.62, h_0=0.46, rho=1000.0, g=9.81,
              alpha=0.80, overspeed=0.05, h_axis_min=0.350):
    # ``alpha`` je omjer zadane i granicne brzine, u tekstu zadatka oznacen k.
    omega_max = math.sqrt(4 * g * (H - h_0) / R**2)
    omega = alpha * omega_max
    dh = omega**2 * R**2 / (2 * g)
    h_osa = h_0 - dh / 2
    h_rub = h_0 + dh / 2
    actual_ratio = alpha * (1 + overspeed)
    h_axis_worst = h_0 - actual_ratio**2 * (H - h_0)
    h_rim_worst = h_0 + actual_ratio**2 * (H - h_0)
    alpha_max = min(1.0, math.sqrt((h_0 - h_axis_min) / (H - h_0))) / (1 + overspeed)
    return {"omega_max": omega_max, "dh": dh,
            "h_osa": h_osa, "h_rub": h_rub,
            "p_M_osa": rho * g * h_osa,
            "p_M_rub": rho * g * h_rub,
            "actual_ratio": actual_ratio,
            "h_axis_worst": h_axis_worst,
            "h_rim_worst": h_rim_worst,
            "alpha_max": alpha_max}


def verify():
    out = []

    r = primjer_1_kolica()
    _check(out, "U04.P1.dh", r["dh"], 0.220, "m")
    _check(out, "U04.P1.h_str", r["h_str"], 0.530, "m")
    _check(out, "U04.P1.h_pred", r["h_pred"], 0.310, "m")
    _check(out, "U04.P1.theta_deg", r["theta_deg"], 7.8, "deg", rel=0.005)

    r = primjer_3_modul()
    _check(out, "U04.P3.theta_deg", r["theta_deg"], 19.1, "deg", rel=0.002)
    _check(out, "U04.P3.phi_deg", r["phi_deg"], 70.9, "deg", rel=0.001)
    _check(out, "U04.P3.s", r["s"], 0.582, "m", rel=0.001)
    _check(out, "U04.P3.g_eff", r["g_eff"], 10.38, "m/s^2", rel=0.001)
    _check(out, "U04.P3.gradient_Pa_m", r["gradient"], 9967.0, "Pa/m", rel=1e-4)
    _check(out, "U04.P3.p_B_kPa", r["p_B"] / 1000, 21.8, "kPa", rel=0.001)
    _check(out, "U04.P3.dx_m", r["dx"], 0.191, "m", rel=0.002)
    _invariant(out, "U04.P3.wall_parallel_to_g_eff",
               abs(r["p_B"] - r["p_B_components"]) < 1e-9 and r["phi_deg"] > 45,
               "Tlak u B po g_eff i po komponentama mora biti isti; kut stijenke veci od 45 stupnjeva.")

    r = primjer_brod_u_zavoju()
    _check(out, "U04.P3b.a", r["a"], 0.2115, "m/s2", rel=2e-4)
    _check(out, "U04.P3b.theta_deg", r["theta_deg"], 1.24, "deg", rel=0.004)
    _check(out, "U04.P3b.dh", r["dh"], 0.194, "m", rel=1e-3)
    _check(out, "U04.P3b.h_v", r["h_v"], 1.697, "m", rel=1e-4)
    _check(out, "U04.P3b.h_u", r["h_u"], 1.503, "m", rel=1e-4)
    _check(out, "U04.P3b.a_max", r["a_max"], 1.308, "m/s2", rel=1e-6)
    _check(out, "U04.P3b.v_max", r["v_max"], 15.3, "m/s", rel=0.003)
    _check(out, "U04.P3b.v_max_kn", r["v_max_kn"], 29.8, "kn", rel=0.002)
    _check(out, "U04.P3b.curvature_mm", r["curvature_mm"], 0.4, "mm", rel=0.02)
    _invariant(out, "U04.P3b.volume_and_no_overflow",
               abs((r["h_v"] + r["h_u"]) / 2 - 1.60) < 1e-12 and not r["overflow"],
               "Srednja razina sondi mora ostati h_0, bez prelijevanja.")
    _invariant(out, "U04.P3b.paraboloid_equals_linear",
               abs(r["dh_parabola"] - r["dh"]) < 1e-12,
               "Tocan paraboloid u rotirajucem okviru daje isti dh kao linearna aproksimacija.")
    _invariant(out, "U04.P3b.outer_side_higher",
               r["h_v"] > r["h_u"] and r["p_v"] > r["p_u"],
               "Razina i tlak na dnu moraju biti veci na vanjskoj strani zavoja.")

    r = cjeloviti_1_rotacija()
    _check(out, "U04.CH1.dh", r["dh"], 0.2205, "m")
    _check(out, "U04.CH1.h_C", r["h_C"], 0.4897, "m")
    _check(out, "U04.CH1.h_R", r["h_R"], 0.7103, "m")
    _check(out, "U04.CH1.p_M_C", r["p_M_C"], 4804.0, "Pa")
    _check(out, "U04.CH1.p_M_D", r["p_M_D"], 6968.0, "Pa")
    _check(out, "U04.CH1.omega_max", r["omega_max"], 6.64, "rad/s")
    _check(out, "U04.CH1.n_max", r["n_max"], 63.4, "min^-1")

    r = primjer_5_autocisterna()
    _check(out, "U04.P5.dh", r["dh"], 0.465, "m")
    _check(out, "U04.P5.h_pred", r["h_pred"], 0.682416, "m", rel=1e-6)
    _check(out, "U04.P5.h_str", r["h_str"], 0.217584, "m", rel=1e-6)
    _check(out, "U04.P5.a_overflow", r["a_overflow"], 5.72, "m/s2", rel=0.02)
    _check(out, "U04.P5.a_dry", r["a_dry"], 7.36, "m/s2", rel=0.02)

    r = primjer_separator()
    _check(out, "U04.P6.omega", r["omega"], 754.0, "rad/s", rel=1e-4)
    _check(out, "U04.P6.acc_g", r["acc_g"], 6950.0, "g", rel=1e-3)
    _check(out, "U04.P6.dp_bar", r["dp"] / 1e5, 32.7, "bar", rel=5e-4)
    _check(out, "U04.P6.r_i_mm", r["r_i"] * 1000, 89.0, "mm", rel=1e-3)
    _check(out, "U04.P6.r_i_950_mm", r["r_i_950"] * 1000, 140.0, "mm", rel=3e-3)
    _check(out, "U04.P6.V_m3", r["V"], 5.83e-3, "m3", rel=1e-3)
    _check(out, "U04.P6.t_res_s", r["t_res"], 14.0, "s", rel=1e-3)
    _check(out, "U04.P6.v_rel", r["v_rel"], 5e-3, "m/s", rel=0.01)
    _check(out, "U04.P6.coriolis_ratio", r["coriolis_ratio"], 1.5e-4, "", rel=0.02)
    _invariant(out, "U04.P6.interface_inside_bowl",
               0.047 < r["r_i"] < 0.120 and r["r_i_950"] > 0.120,
               "Razdjelnica mora biti unutar bubnja za 930 kg/m3, a izvan njega za 950 kg/m3.")
    _invariant(out, "U04.P6.interface_independent_of_speed",
               abs(primjer_separator(n=3600.0)["r_i"] - r["r_i"]) < 1e-12,
               "Polozaj razdjelnice ne smije ovisiti o kutnoj brzini.")
    _invariant(out, "U04.P6.relative_rest_justified",
               r["speed_ratio"] < 1e-3 and r["coriolis_ratio"] < 1e-3,
               "Relativna brzina i Coriolisov clan moraju biti zanemarivi prema krutoj vrtnji.")

    z1 = zadatak_1()
    _check(out, "U04.Z1.dh", z1["dh"], 0.22, "m")
    _check(out, "U04.Z1.h_str", z1["h_str"], 0.45, "m")
    _check(out, "U04.Z1.h_pred", z1["h_pred"], 0.23, "m")

    z2 = zadatak_2()
    _check(out, "U04.Z2.a_max", z2["a_max"], 1.68, "m/s^2")
    h_back_limit = .30 + z2["a_max"] * 1.40 / (2 * 9.81)
    _invariant(out, "U04.Z2.spill_before_dry",
               abs(h_back_limit-.42) < 1e-12 and 2*.30-h_back_limit > 0,
               "Pri prvom dodiru ruba prednji dio dna mora ostati pokriven.")

    z3 = zadatak_3()
    _check(out, "U04.Z3.dp_kPa", z3["dp"] / 1000, 7.90, "kPa")
    _check(out, "U04.Z3.dp_0_kPa", z3["dp_0"] / 1000, 6.40, "kPa")
    _check(out, "U04.Z3.increase_percent", z3["increase_percent"], 23.0, "%", rel=0.03)
    _check(out, "U04.Z3.dp_braking_kPa", z3["dp_braking"] / 1000, 4.90, "kPa", rel=.001)
    _invariant(out, "U04.Z3.acceleration_not_velocity",
               0 < z3["dp_braking"] < z3["dp_0"] < z3["dp"]
               and abs(z3["dp"] + z3["dp_braking"] - 2*z3["dp_0"]) < 1e-8,
               "Suprotna ubrzanja moraju dati suprotne promjene hidrostatskog gradijenta.")
    _invariant(out, "U04.Z3.zero_and_free_fall",
               abs(zadatak_3(a_z=0)["dp"]-z3["dp_0"]) < 1e-8
               and abs(zadatak_3(a_z=-9.81)["dp"]) < 1e-8,
               "Mirni slucaj i slobodni pad nemaju ocekivane gradijente.")

    z4 = zadatak_4()
    _check(out, "U04.Z4.dp_kPa", z4["dp"] / 1000, 1.60, "kPa", rel=1e-9)
    _check(out, "U04.Z4.omega", z4["omega"], 7.91, "rad/s", rel=.001)
    _check(out, "U04.Z4.rpm", z4["rpm"], 75.5, "min^-1", rel=.001)
    # The linear radial gradient integrates exactly by the trapezoid rule.
    reconstructed = 1000*z4["omega"]**2 * (.080+.240)/2 * (.240-.080)
    _invariant(out, "U04.Z4.radial_integral", abs(reconstructed-1600) < 1e-8,
               "Integrirani radijalni gradijent ne vraca izmjerenu razliku tlakova.")
    shifted = zadatak_4(p_A=15.40e3,p_B=17.00e3)
    swapped = zadatak_4(r_A=.240,r_B=.080,p_A=14e3,p_B=12.4e3)
    _invariant(out, "U04.Z4.reference_and_point_order",
               abs(shifted["omega"]-z4["omega"]) < 1e-12
               and abs(swapped["omega"]-z4["omega"]) < 1e-12,
               "Iznos vrtnje mora ostati isti nakon pomaka reference ili zamjene tocaka.")

    z5 = zadatak_5()
    _check(out, "U04.Z5.h_back_m", z5["h_str"], .45291, "m", rel=.00002)
    _check(out, "U04.Z5.h_front_m", z5["h_pred"], .14709, "m", rel=.00004)
    _check(out, "U04.Z5.error_i_mm", z5["errors"][0]*1000, 72.91, "mm", rel=.0001)
    _check(out, "U04.Z5.error_ii_mm", z5["errors"][1]*1000, 1.095, "mm", rel=.0002)
    _check(out, "U04.Z5.spread_i_mm", z5["spreads"][0]*1000, 140, "mm", rel=1e-9)
    _check(out, "U04.Z5.spread_ii_mm", z5["spreads"][1]*1000, 2, "mm", rel=1e-9)
    _invariant(out, "U04.Z5.series_selection",
               z5["accepted"] == [False, True] and z5["reference_fits"],
               "Samo drugi niz mora zadovoljiti oba kriterija.")
    stable_wrong = zadatak_5(samples_i=((1,.460,.140),(2,.460,.140),(3,.460,.140)))
    near_oscillating = zadatak_5(samples_ii=((1,.450,.150),(2,.456,.144),(3,.450,.150)))
    _invariant(out, "U04.Z5.both_tests_needed",
               stable_wrong["spreads"][0] == 0 and not stable_wrong["accepted"][0]
               and near_oscillating["errors"][1] < .005 and not near_oscillating["accepted"][1],
               "Stabilan pogresan niz i oscilacije blizu modela moraju pasti razlicite kriterije.")
    _invariant(out, "U04.Z5.reference_balance",
               abs((z5["h_str"]+z5["h_pred"])/2-.300) < 1e-12
               and abs(9.81*(z5["h_str"]-z5["h_pred"])-2*1.5) < 1e-12,
               "Referentni profil ne zatvara volumen i nagib.")

    z6 = zadatak_6()
    _check(out, "U04.Z6.omega_max", z6["omega_max"], 7.83, "rad/s")
    _check(out, "U04.Z6.h_osa", z6["h_osa"], 0.36, "m")
    _check(out, "U04.Z6.h_rub", z6["h_rub"], 0.56, "m")
    _check(out, "U04.Z6.p_M_osa_kPa", z6["p_M_osa"] / 1000, 3.51, "kPa")
    _check(out, "U04.Z6.p_M_rub_kPa", z6["p_M_rub"] / 1000, 5.52, "kPa")
    _check(out, "U04.Z6.actual_ratio", z6["actual_ratio"], 0.84, "")
    _check(out, "U04.Z6.h_axis_worst", z6["h_axis_worst"], 0.347, "m", rel=0.02)
    _check(out, "U04.Z6.h_rim_worst", z6["h_rim_worst"], 0.573, "m", rel=0.02)
    _check(out, "U04.Z6.alpha_max", z6["alpha_max"], 0.790, "", rel=0.001)
    recommended = zadatak_6(alpha=.78)
    _check(out, "U04.Z6.recommended_axis_m", recommended["h_axis_worst"], .35268, "m", rel=.00002)
    _check(out, "U04.Z6.recommended_rim_m", recommended["h_rim_worst"], .56732, "m", rel=.00002)
    _check(out, "U04.Z6.depth_margin_mm", (recommended["h_axis_worst"]-.350)*1000, 2.68, "mm", rel=.001)
    limiting = zadatak_6(alpha=z6["alpha_max"])
    above_limit = zadatak_6(alpha=z6["alpha_max"]+.0001)
    _invariant(out, "U04.Z6.recommendation_and_active_limit",
               recommended["h_axis_worst"] > .350 and recommended["h_rim_worst"] < .62
               and abs(limiting["h_axis_worst"]-.350) < 1e-12
               and limiting["h_rim_worst"] < .62 and above_limit["h_axis_worst"] < .350,
               "Preporucena postavka i aktivna granica dubine nisu uskladene.")
    _invariant(out, "U04.Z6.bounded_speed",
               all(zadatak_6(alpha=.78,overspeed=e)["h_axis_worst"] >= .350
                   and zadatak_6(alpha=.78,overspeed=e)["h_rim_worst"] <= .62
                   for e in (0,.01,.025,.04,.05)),
               "Preporuka mora zadovoljiti cijeli zadani raspon brzine; dubina je monotona u omega².")
    _invariant(
        out,
        "U04.Z6.coverage_not_met_at_alpha_080",
        z6["h_rim_worst"] < 0.62 and z6["h_axis_worst"] < 0.350,
        "Nepovoljna tolerancija mora zadrzati volumen, ali prekrsiti dubinu usisa.",
    )

    _invariant(
        out,
        "U04.INV.translational_volume_balance",
        abs((z1["h_str"] + z1["h_pred"]) / 2 - 0.34) < 1e-14,
        "Srednja dubina ubrzanog spremnika nije sacuvana.",
    )
    _invariant(
        out,
        "U04.INV.no_overflow_and_axis_covered",
        not z1["overflow"] and z6["h_osa"] > 0,
        "Objavljeni granicni zakljucak o preljevu/pokrivenosti osi nije ispunjen.",
    )
    _invariant(
        out,
        "U04.INV.effective_gravity_sign",
        z3["dp"] > z3["dp_0"] > 0.0,
        "Ubrzanje prema gore nije povecalo tlakovnu razliku.",
    )
    _invariant(
        out,
        "U04.INV.rotational_volume_and_limit",
        abs((z6["h_osa"] + z6["h_rub"]) / 2 - 0.46) < 1e-14
        and z6["h_rub"] < 0.62,
        "Radni rotacijski rezim ne cuva volumen ili prelijeva.",
    )

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
