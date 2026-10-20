"""Kanonski U08 (naslijeđeni namespace U09): energija i Bernoulli."""
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


def primjer_1_konfuzor(A_1=0.07, A_2=0.0185, m_dot=0.68, rho=1.2):
    Q = m_dot / rho
    v_1 = Q / A_1
    v_2 = Q / A_2
    dp = rho / 2 * (v_2**2 - v_1**2)
    return {"Q": Q, "v_1": v_1, "v_2": v_2, "dp": dp}


def primjer_2_mlaz(H=4.0, g=9.81):
    def x_of(h):
        return 2 * math.sqrt(h * (H - h))
    return {"x_1": x_of(1.0), "x_2": x_of(2.0), "x_3": x_of(3.0),
            "x_max": H, "h_opt": H / 2}


def primjer_3_sifon(D=0.080, dz=3.6, z_C=2.2, g=9.81, rho=1000.0):
    v = math.sqrt(2 * g * dz)
    A = math.pi * D**2 / 4
    Q = A * v
    p_C_g = -(dz + z_C)  # manometarska tlačna visina
    return {"v": v, "Q": Q, "p_C_g": p_C_g, "HGL_C": z_C+p_C_g}


def cjeloviti_1_usisni_vod(z_P=2.0, D=0.150, Q_m3h=180.0, rho=1025.0,
                           p_v=2.3e3, p_atm=101.3e3, h_w=1.2, g=9.81,
                           dz_ballast=1.5):
    """P4: usisni vod rashladne crpke morske vode, tlak na ulazu u crpku."""
    Q = Q_m3h / 3600.0
    v = 4 * Q / (math.pi * D**2)
    h_v = v**2 / (2 * g)
    h_atm = p_atm / (rho * g)
    h_vap = p_v / (rho * g)
    h_P = h_atm - z_P - h_v - h_w
    p_P = h_P * rho * g
    p_P_ideal = (h_atm - z_P - h_v) * rho * g
    npsh = h_P - h_vap + h_v
    z_max = h_atm - h_vap - h_v - h_w
    h_P_b = h_atm - (z_P + dz_ballast) - h_v - h_w
    return {"v": v, "h_v": h_v, "h_P": h_P, "p_P": p_P, "p_M": p_P - p_atm,
            "p_P_ideal": p_P_ideal, "npsh": npsh, "z_max": z_max,
            "p_P_ballast": h_P_b * rho * g, "npsh_ballast": h_P_b - h_vap + h_v}


def primjer_venturi(D_1=0.060, D_2=0.030, dh_m=0.18, rho_Hg=13600.0,
                     rho_o=870.0, g=9.81):
    dp = (rho_Hg - rho_o) * g * dh_m
    A_1 = math.pi * D_1**2 / 4
    # ratio = (D_1/D_2)^4
    ratio_v2_v1 = (D_1 / D_2)**2
    # Δp = ρ/2 (v_2² - v_1²) = ρ/2 v_1² (ratio² - 1)
    v_1 = math.sqrt(2 * dp / (rho_o * (ratio_v2_v1**2 - 1)))
    v_2 = ratio_v2_v1 * v_1
    Q = A_1 * v_1
    return {"dp": dp, "v_1": v_1, "v_2": v_2, "Q": Q}


def primjer_propust(H=8.50, d=0.40, g=9.81):
    v = math.sqrt(2 * g * H)
    A = math.pi * d**2 / 4
    Q = A * v
    return {"v": v, "Q": Q}


def primjer_pitot_uav(dp=380.0, rho=1.115, rho_dense=1.25,
                       D_s=0.005, nu=1.5e-5):
    """Javni primjer Pitot-statičke sonde na bespilotnoj letjelici."""

    v = math.sqrt(2 * dp / rho)
    v_dense = math.sqrt(2 * dp / rho_dense)
    Re_s = v * D_s / nu
    change_percent = (v - v_dense) / v * 100
    return {
        "v": v,
        "v_dense": v_dense,
        "Re_s": Re_s,
        "change_percent": change_percent,
    }


def zadatak_1(H=3.20, d=0.026, rho=998.0, g=9.81):
    v = math.sqrt(2 * g * H)
    A = math.pi * d**2 / 4
    Q = A * v
    m_dot = rho * Q
    return {"v": v, "Q": Q, "m_dot": m_dot}


def zadatak_2(D_T=1.60, d=0.030, C_d=0.62, H_1=3.20, H_2=0.80, g=9.81):
    """Z2: kvazistacionarno praznjenje spremnika kroz otvor u dnu."""
    A_T = math.pi * D_T**2 / 4
    A_o = math.pi * d**2 / 4
    Q_1 = C_d * A_o * math.sqrt(2 * g * H_1)
    dhdt_1 = -Q_1 / A_T
    k = A_T / (C_d * A_o) * math.sqrt(2 / g)
    t = k * (math.sqrt(H_1) - math.sqrt(H_2))
    t_naive = A_T * (H_1 - H_2) / Q_1
    t_empty = k * math.sqrt(H_1)
    # neovisna numericka integracija dh/dt = -C_d A_o sqrt(2 g h)/A_T (RK4)
    h, tt, dt = H_1, 0.0, 0.05
    f = lambda hh: -C_d * A_o * math.sqrt(2 * g * max(hh, 0.0)) / A_T
    while h > H_2:
        k1 = f(h); k2 = f(h + dt / 2 * k1); k3 = f(h + dt / 2 * k2); k4 = f(h + dt * k3)
        h_new = h + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if h_new <= H_2:
            tt += dt * (h - H_2) / (h - h_new); h = H_2; break
        h = h_new; tt += dt
    return {"A_T": A_T, "A_o": A_o, "Q_1": Q_1, "dhdt_1": dhdt_1, "t": t,
            "t_naive": t_naive, "t_empty": t_empty, "t_num": tt,
            "naive_error": (t_naive - t) / t}


def zadatak_3(D_1=0.120, D_2=0.070, Q=0.020, dz=2.0, rho=1000.0, g=9.81):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1, v_2 = Q/A_1, Q/A_2
    dp = rho*g*dz + rho/2*(v_1**2-v_2**2)
    return {"v_1": v_1, "v_2": v_2, "dp": dp,
            "dHGL": dp/(rho*g)-dz}


def zadatak_4(p_S=24e3, p_A=16e3, dz=1.2, rho=1000.0, g=9.81):
    p_st = p_S + rho*g*dz
    dp = p_st-p_A
    v = math.sqrt(2*dp/rho)
    return {"p_st": p_st, "dp": dp, "v": v, "v_kn": v * 3600 / 1852,
            "v_wrong": math.sqrt(2*(p_S-p_A)/rho)}


def zadatak_5(Q=.020, D_1=.100, p_1=150e3, p_min=60e3,
              dp_min=40e3, rho=1000.0, candidates=(.040,.050,.060)):
    v_1 = 4*Q/(math.pi*D_1**2)
    v_max = math.sqrt(v_1**2+2*(p_1-p_min)/rho)
    v_min = math.sqrt(v_1**2+2*dp_min/rho)
    d_min = math.sqrt(4*Q/(math.pi*v_max))
    d_max = math.sqrt(4*Q/(math.pi*v_min))
    velocities = [4*Q/(math.pi*d**2) for d in candidates]
    pressures = [p_1+rho/2*(v_1**2-v**2) for v in velocities]
    drops = [p_1-p for p in pressures]
    accepted = [d for d,p,dp in zip(candidates,pressures,drops)
                if p >= p_min and dp >= dp_min]
    return {"d_min": d_min, "d_max": d_max, "velocities": velocities,
            "pressures": pressures, "drops": drops, "accepted": accepted}


def zadatak_6(D=0.070, dz=2.6, z_C=1.7, h_exit=1.2, g=9.81,
               p_atm=101.3e3, rho=1000.0, zeta_sum=2.0, dzeta_sum=0.5,
               zeta_C=1.2, dzeta_C=0.3):
    v = math.sqrt(2 * g * dz)
    A = math.pi * D**2 / 4
    Q = A * v
    p_C_g = -(v**2 / (2 * g) + z_C)
    p_C_abs = p_atm + rho * g * p_C_g
    t = math.sqrt(2 * h_exit / g)
    x = v * t
    v_real = math.sqrt(2 * g * dz / (1 + zeta_sum))
    Q_real = A * v_real
    Q_max = A * math.sqrt(2 * g * dz / (1 + zeta_sum - dzeta_sum))
    Q_min = A * math.sqrt(2 * g * dz / (1 + zeta_sum + dzeta_sum))
    # Najmanji tlak nastaje uz najveći zeta_C i najmanji ukupni zeta_sum.
    vh_at_p_min = dz / (1 + zeta_sum - dzeta_sum)
    p_C_abs_min = p_atm - rho * g * (
        z_C + (1 + zeta_C + dzeta_C) * vh_at_p_min
    )
    p_C_abs_max = p_atm-rho*g*(z_C+(1+zeta_C-dzeta_C)*dz/(1+zeta_sum+dzeta_sum))
    p_C_abs_real = p_atm-rho*g*(z_C+(1+zeta_C)*dz/(1+zeta_sum))
    return {
        "v": v,
        "Q": Q,
        "p_C_abs": p_C_abs,
        "x": x,
        "Q_real": Q_real,
        "Q_min": Q_min,
        "Q_max": Q_max,
        "p_C_abs_min": p_C_abs_min,
        "p_C_abs_max": p_C_abs_max,
        "p_C_abs_real": p_C_abs_real,
    }


# ------------ Faza 1.5 dodatak: Difuzor (povratak tlaka) ----------------
def primjer_difuzor(A_1=0.010, A_2=0.035, v_1=15.0, rho=1000.0, eta_dif=0.80):
    Q = A_1 * v_1
    v_2 = v_1 * A_1 / A_2
    dp_ideal = 0.5 * rho * (v_1**2 - v_2**2)
    dp_real = eta_dif * dp_ideal
    P_gub = (1 - eta_dif) * dp_ideal * Q
    return {"Q": Q, "v_2": v_2, "dp_ideal": dp_ideal,
            "dp_real": dp_real, "P_gub": P_gub}


def _invariant(out, rid, condition, message):
    out.append({"id":rid,"status":"OK" if condition else "FAIL",
                "details":"" if condition else message,"verification":"invariant"})


def verify():
    out = []

    r = primjer_1_konfuzor()
    _check(out, "U09.P1.Q", r["Q"], 0.5667, "m^3/s", rel=0.02)
    _check(out, "U09.P1.v_1", r["v_1"], 8.10, "m/s", rel=0.02)
    _check(out, "U09.P1.v_2", r["v_2"], 30.63, "m/s", rel=0.02)
    _check(out, "U09.P1.dp", r["dp"], 523.62, "Pa", rel=.00005)

    r = primjer_2_mlaz()
    _check(out, "U09.P2.x_1", r["x_1"], 3.46, "m", rel=0.02)
    _check(out, "U09.P2.x_2", r["x_2"], 4.00, "m")
    _check(out, "U09.P2.x_3", r["x_3"], 3.46, "m", rel=0.02)
    _check(out, "U09.P2.x_max", r["x_max"], 4.0, "m")

    r = primjer_3_sifon()
    _check(out, "U09.P3.v", r["v"], 8.40, "m/s")
    _check(out, "U09.P3.Q_Ls", r["Q"] * 1000, 42.2, "L/s", rel=0.02)
    _check(out, "U09.P3.p_C_g", r["p_C_g"], -5.8, "m")
    _check(out, "U09.P3.HGL_C", r["HGL_C"], -3.6, "m", rel=1e-10)

    r = cjeloviti_1_usisni_vod()
    _check(out, "U09.CH1.v", r["v"], 2.83, "m/s", rel=0.001)
    _check(out, "U09.CH1.h_v", r["h_v"], 0.408, "m", rel=0.001)
    _check(out, "U09.CH1.h_P", r["h_P"], 6.47, "m", rel=0.001)
    _check(out, "U09.CH1.p_P_kPa", r["p_P"] / 1000, 65.0, "kPa", rel=0.001)
    _check(out, "U09.CH1.p_M_kPa", r["p_M"] / 1000, -36.3, "kPa", rel=0.001)
    _check(out, "U09.CH1.p_P_ideal_kPa", r["p_P_ideal"] / 1000, 77.1, "kPa", rel=0.001)
    _check(out, "U09.CH1.npsh_m", r["npsh"], 6.65, "m", rel=0.001)
    _check(out, "U09.CH1.z_max_m", r["z_max"], 8.24, "m", rel=0.001)
    _check(out, "U09.CH1.p_P_ballast_kPa", r["p_P_ballast"] / 1000, 49.9, "kPa", rel=0.001)
    _check(out, "U09.CH1.npsh_ballast_m", r["npsh_ballast"], 5.15, "m", rel=0.001)

    r = primjer_venturi()
    _check(out, "U09.venturi.dp", r["dp"], 22478.634, "Pa", rel=1e-10)
    _check(out, "U09.venturi.v_1", r["v_1"], 1.856, "m/s", rel=.00005)
    _check(out, "U09.venturi.Q_Ls", r["Q"] * 1000, 5.248, "L/s", rel=.00005)

    r = primjer_pitot_uav()
    _check(out, "U09.P6.v", r["v"], 26.1, "m/s", rel=0.02)
    _check(out, "U09.P6.v_dense", r["v_dense"], 24.7, "m/s", rel=0.02)
    _check(out, "U09.P6.Re_s", r["Re_s"], 8700.0, "", rel=0.02)
    _check(out, "U09.P6.change_percent", r["change_percent"], 5.5, "%", rel=0.01)

    r = zadatak_1()
    _check(out, "U09.Z1.v", r["v"], 7.92, "m/s", rel=0.02)
    _check(out, "U09.Z1.Q_Ls", r["Q"] * 1000, 4.21, "L/s", rel=0.02)
    _check(out, "U09.Z1.m_dot", r["m_dot"], 4.20, "kg/s", rel=0.02)

    r = zadatak_2()
    _check(out, "U09.Z2.Q_1_Ls", r["Q_1"] * 1000, 3.47, "L/s", rel=0.002)
    _check(out, "U09.Z2.dhdt_1_mm_s", r["dhdt_1"] * 1000, -1.73, "mm/s", rel=0.003)
    _check(out, "U09.Z2.t_s", r["t"], 1853.0, "s", rel=0.001)
    _check(out, "U09.Z2.t_min", r["t"] / 60, 30.9, "min", rel=0.002)
    _check(out, "U09.Z2.t_naive_s", r["t_naive"], 1390.0, "s", rel=0.001)
    _check(out, "U09.Z2.naive_error_percent", r["naive_error"] * 100, -25.0, "%", rel=0.01)
    _check(out, "U09.Z2.t_empty_s", r["t_empty"], 3706.0, "s", rel=0.001)
    _invariant(out, "U09.Z2.quasi_steady_integration",
               abs(r["t_num"] - r["t"]) / r["t"] < 2e-3 and abs(r["t_empty"] - 2 * r["t"]) < 1e-9
               and r["t_naive"] < r["t"],
               "RK4 integracija bilance mase mora dati analiticko vrijeme; praznjenje do H1/4 traje polovinu ukupnog.")

    r = zadatak_3()
    _check(out, "U09.Z3.v_1", r["v_1"], 1.768, "m/s", rel=.0005)
    _check(out, "U09.Z3.v_2", r["v_2"], 5.197, "m/s", rel=.0005)
    _check(out, "U09.Z3.dp_kPa", r["dp"]/1000, 7.680, "kPa", rel=.0005)

    r = zadatak_4()
    _check(out, "U09.Z4.v", r["v"], 6.288, "m/s", rel=.0005)
    _check(out, "U09.Z4.v_kn", r["v_kn"], 12.2, "čv", rel=.002)
    _check(out, "U09.Z4.v_wrong", r["v_wrong"], 4.000, "m/s", rel=1e-10)
    _check(out, "U09.Z4.p_st_kPa", r["p_st"]/1000, 35.772, "kPa", rel=1e-10)
    _check(out, "U09.Z4.dp_kPa", r["dp"]/1000, 19.772, "kPa", rel=1e-10)

    r = zadatak_5()
    _check(out, "U09.Z5.d_min_mm", r["d_min"]*1000, 43.183, "mm", rel=.00005)
    _check(out, "U09.Z5.d_max_mm", r["d_max"]*1000, 52.328, "mm", rel=.00005)
    _check(out, "U09.Z5.p40_kPa", r["pressures"][0]/1000, 26.591, "kPa", rel=.00005)
    _check(out, "U09.Z5.p50_kPa", r["pressures"][1]/1000, 101.366, "kPa", rel=.00005)
    _check(out, "U09.Z5.p60_kPa", r["pressures"][2]/1000, 128.225, "kPa", rel=.00005)
    _check(out, "U09.Z5.dp40_kPa", r["drops"][0]/1000, 123.409, "kPa", rel=.00005)
    _check(out, "U09.Z5.dp50_kPa", r["drops"][1]/1000, 48.634, "kPa", rel=.00005)
    _check(out, "U09.Z5.dp60_kPa", r["drops"][2]/1000, 21.775, "kPa", rel=.00005)

    r = zadatak_6()
    _check(out, "U09.Z6.v_ideal", r["v"], 7.14, "m/s", rel=0.02)
    _check(out, "U09.Z6.Q_ideal_Ls", r["Q"] * 1000, 27.5, "L/s", rel=0.02)
    _check(out, "U09.Z6.p_C_ideal_kPa", r["p_C_abs"] / 1000, 59.1, "kPa", rel=.001)
    _check(out, "U09.Z6.x", r["x"], 3.53, "m", rel=0.02)
    _check(out, "U09.Z6.Q_real_Ls", r["Q_real"] * 1000, 15.9, "L/s", rel=0.02)
    _check(out, "U09.Z6.Q_min_Ls", r["Q_min"] * 1000, 14.7, "L/s", rel=0.02)
    _check(out, "U09.Z6.Q_max_Ls", r["Q_max"] * 1000, 17.4, "L/s", rel=0.02)
    _check(out, "U09.Z6.p_C_min_kPa", r["p_C_abs_min"] / 1000, 59.1, "kPa", rel=.001)
    _check(out, "U09.Z6.p_C_max_kPa", r["p_C_abs_max"]/1000, 70.8, "kPa", rel=.002)
    _check(out, "U09.Z6.p_C_real_kPa", r["p_C_abs_real"]/1000, 65.9, "kPa", rel=.002)

    a,b,c,d,e,f=(zadatak_1(),zadatak_2(),zadatak_3(),zadatak_4(),zadatak_5(),zadatak_6())
    _invariant(out, "U09.INV.z1_energy_mass", abs(a['v']**2/2-9.81*3.2)<1e-12
              and abs(a['m_dot']-998*a['Q'])<1e-12, "Istjecanje ne zatvara energiju i masu.")
    _invariant(out, "U09.INV.z2_torricelli_rate", abs(b['Q_1']-0.62*math.pi*0.030**2/4*math.sqrt(2*9.81*3.20))<1e-12
               and abs(b['dhdt_1']*b['A_T']+b['Q_1'])<1e-12,
               "Pocetni protok mora slijediti iz C_d A_o sqrt(2 g H1), a pad razine iz bilance mase.")
    ch1=cjeloviti_1_usisni_vod()
    _invariant(out, "U09.INV.ch1_energy", abs(ch1['h_P']+ch1['h_v']+2.0+1.2-101.3e3/(1025*9.81))<1e-12
              and ch1['p_P_ideal']>ch1['p_P']>0
              and abs(cjeloviti_1_usisni_vod(z_P=ch1['z_max'])['p_P']-2.3e3)<1e-8
              and ch1['npsh']>ch1['npsh_ballast']>0,
              "Usisni vod ne zatvara energijsku jednadzbu ili granicu tlaka pare.")
    _invariant(out, "U09.INV.z3_bernoulli", abs(c['dp']/1000+c['v_2']**2/2-c['v_1']**2/2-9.81*2)<1e-12
              and c['dp']>0 and c['dHGL']<0, "Silazno suzenje ne zatvara predznake i energiju.")
    _invariant(out, "U09.INV.z3_horizontal_limit", zadatak_3(dz=0)['dp']<0
              and abs(zadatak_3(Q=0)['dp']-19620)<1e-10, "Horizontalna ili hidrostaticka granica ne prolazi.")
    _invariant(out, "U09.INV.z4_hydrostatic", abs(d['p_st']-1000*d['v']**2/2-16000)<1e-10
              and abs(zadatak_4(p_S=35772,dz=0)['v']-d['v'])<1e-12,
              "Premjestanje senzora uz odgovarajuce ocitanje mijenja brzinu.")
    def drop(diameter):
        return 8*1000*.020**2/math.pi**2*(diameter**-4-.100**-4)
    _invariant(out, "U09.INV.z5_bounds", abs(drop(e['d_min'])-90000)<1e-8
              and abs(drop(e['d_max'])-40000)<1e-8
              and drop(e['d_min']*.999)>90000 and drop(e['d_max']*1.001)<40000,
              "Rubovi promjera ne zatvaraju zadane nejednakosti.")
    _invariant(out, "U09.INV.z5_selection", e['accepted']==[.050], "Odabir ne zadovoljava oba tlacna uvjeta.")
    from itertools import product
    corners=[zadatak_6(zeta_sum=ks,dzeta_sum=0,zeta_C=kc,dzeta_C=0)
             for ks,kc in product((1.5,2.5),(.9,1.5))]
    _invariant(out, "U09.INV.z6_corners", abs(min(r['p_C_abs_real'] for r in corners)-f['p_C_abs_min'])<1e-8
              and abs(max(r['p_C_abs_real'] for r in corners)-f['p_C_abs_max'])<1e-8
              and min(r['Q_real'] for r in corners)<.015<max(r['Q_real'] for r in corners)
              and f['p_C_abs_min']>30000, "Intervalni rubovi i odluka nisu konzistentni.")
    no_loss=zadatak_6(zeta_sum=0,dzeta_sum=0,zeta_C=0,dzeta_C=0)
    _invariant(out, "U09.INV.z6_ideal_limit", abs(no_loss['Q_real']-f['Q'])<1e-12
              and abs(no_loss['p_C_abs_real']-f['p_C_abs'])<1e-8,
              "Nulti gubitci ne vracaju idealni sifon.")
    _invariant(out, "U09.INV.z6_trajectory", abs(9.81/2*(f['x']/f['v'])**2-1.2)<1e-12,
              "Mlaz ne doseze tlo u objavljenom dometu.")
    p3=primjer_3_sifon()
    _invariant(out, "U09.INV.p3_reference", abs(p3['HGL_C']+p3['v']**2/(2*9.81))<1e-12,
              "HGL u sifonu i brzinska visina ne vracaju EGL povrsine A.")

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
