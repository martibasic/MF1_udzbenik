"""Numericka verifikacija U08: Kontrolni volumen i kontinuitet."""
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
    out.append({"id": rid, "status": "OK" if condition else "FAIL",
                "verification": "invariant",
                "details": "" if condition else details})


def primjer_1_difuzor(D_1=0.120, D_2=0.180, v_2=1.6, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = A_2 / A_1 * v_2
    Q = A_2 * v_2
    m_dot = rho * Q
    return {"A_1": A_1, "A_2": A_2, "v_1": v_1, "Q": Q, "m_dot": m_dot}


def primjer_2_mjesanje(Q_A=0.150, Q_B=0.030, s_B=0.80, D_C=0.30, rho_A=1000.0):
    rho_B = s_B * rho_A
    Q_C = Q_A + Q_B
    A_C = math.pi * D_C**2 / 4
    v_C = Q_C / A_C
    m_dot_C = rho_A * Q_A + rho_B * Q_B
    rho_C = m_dot_C / Q_C
    return {"rho_B": rho_B, "Q_C": Q_C, "v_C": v_C,
            "m_dot_C": m_dot_C, "rho_C": rho_C}


def primjer_2_zahvatni_usis(v_s_kn=18.0, rho=1025.0, A_u=0.040, psi=0.55,
                            Q_m3h=180.0):
    """P2: zahvatni usis morske vode, kontrolni volumen vezan uz brod."""
    v_s = v_s_kn * 1852.0 / 3600.0
    Q = Q_m3h / 3600.0
    m_dot = rho * Q
    w = Q / A_u                   # relativno prema brodu, u usis
    w_r = Q / (psi * A_u)         # u slobodnim otvorima rešetke
    v_abs = v_s - w               # apsolutno, prema pramcu
    m_dot_wrong = rho * A_u * v_abs
    return {"v_s": v_s, "Q": Q, "m_dot": m_dot, "w": w, "w_r": w_r,
            "v_abs": v_abs, "m_dot_wrong": m_dot_wrong}


def cjeloviti_1_mijesajuci(L=4.2, b=1.5, Q_A=0.018, Q_B=0.006, s_r=1.10,
                            D_3=0.100, v_3=1.80, h_0=0.80, h_1=1.20,
                            rho_w=1000.0):
    rho_B = s_r * rho_w
    A_3 = math.pi * D_3**2 / 4
    Q_3 = A_3 * v_3
    m_dot_ul = rho_w * Q_A + rho_B * Q_B
    Q_ul = Q_A + Q_B
    rho_mj = m_dot_ul / Q_ul  # gustoća mješavine
    A_T = L * b
    dhdt = (Q_A + Q_B - Q_3) / A_T
    dh = h_1 - h_0
    dV = A_T * dh
    t = dV / (Q_A + Q_B - Q_3)
    dm = rho_mj * dV
    return {"rho_B": rho_B, "Q_3": Q_3, "rho_3": rho_mj,
            "dhdt": dhdt, "t": t, "dm": dm}


def primjer_5_T_komad(D_1=0.032, v_1=4.5, D_2=0.020, udio_1=0.60, v_3=3.0):
    A_1 = math.pi * D_1**2 / 4
    Q_1 = A_1 * v_1
    Q_2 = udio_1 * Q_1
    Q_3 = (1 - udio_1) * Q_1
    A_2 = math.pi * D_2**2 / 4
    v_2 = Q_2 / A_2
    A_3 = Q_3 / v_3
    D_3 = math.sqrt(4 * A_3 / math.pi)
    return {"Q_1": Q_1, "Q_2": Q_2, "Q_3": Q_3, "v_2": v_2, "D_3": D_3}


def primjer_6_retencija(A_b=120.0, Q_1=0.35, Q_2=0.20, Q_iz=0.18,
                         dh_target=0.50):
    Q_neto = Q_1 + Q_2 - Q_iz
    dhdt = Q_neto / A_b
    t = dh_target / dhdt
    return {"Q_neto": Q_neto, "dhdt": dhdt, "t": t}


def primjer_ev_hladenje(D_1=0.020, d=0.006, n=16, Q_L_min=25.0):
    """Javni primjer rashladnoga razdjelnika baterijskog paketa."""

    Q = Q_L_min * 1.0e-3 / 60.0
    A_1 = math.pi * D_1**2 / 4
    A_d = math.pi * d**2 / 4
    v_1 = Q / A_1
    v_d = Q / (n * A_d)
    v_blocked = Q / ((n - 1) * A_d)
    rise_percent = (v_blocked / v_d - 1) * 100
    return {
        "Q": Q,
        "v_1": v_1,
        "v_d": v_d,
        "v_blocked": v_blocked,
        "rise_percent": rise_percent,
    }


def zadatak_1(rho_1=1.20, v_1=12.0, A_1=0.30, rho_2=1.02, A_2=0.24):
    """Z1: grijač ventilacijskog zraka, masena bilanca uz promjenu gustoće."""
    m_dot = rho_1 * A_1 * v_1
    v_2 = m_dot / (rho_2 * A_2)
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v_2
    return {"m_dot": m_dot, "v_2": v_2, "Q_1": Q_1, "Q_2": Q_2}


def zadatak_2(A=0.004, v=3.0, theta_deg=60.0, rho=998.0):
    v_n = v * math.cos(math.radians(theta_deg))
    Q = A * v_n
    return {"v_n": v_n, "Q": Q, "m_dot": rho*Q}


def zadatak_3(Q_1=0.012, Q_2=0.008, D_3=0.120):
    Q_3 = Q_1 + Q_2
    A_3 = math.pi * D_3**2 / 4
    v_3 = Q_3 / A_3
    return {"Q_3": Q_3, "v_3": v_3}


def zadatak_4(Q=0.030, D_2=0.090, D_3=0.070):
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    # v_2 = 2 v_3, Q = Q_2 + Q_3 = A_2 v_2 + A_3 v_3 = (2 A_2 + A_3) v_3
    v_3 = Q / (2 * A_2 + A_3)
    v_2 = 2 * v_3
    Q_2 = A_2 * v_2
    Q_3 = A_3 * v_3
    return {"Q_2": Q_2, "Q_3": Q_3, "v_2": v_2, "v_3": v_3}


def zadatak_5(D=0.100, d=0.020, Q_in=0.001, w=1.50,
              stroke=0.12, rho=998.0):
    A_p = math.pi*D**2/4
    A_o = math.pi*d**2/4
    Q_out_rel = A_o*w
    u = (Q_in-Q_out_rel)/A_p
    return {"A_p": A_p, "A_o": A_o, "Q_out_rel": Q_out_rel,
            "u": u, "v_out": w+u, "t": stroke/u if u > 0 else math.inf,
            "dm": rho*A_p*stroke, "w_stopped": Q_in/A_o}


def zadatak_6(A_T=36.0, h_0=0.30, h_max=1.60, rho_mv=1025.0, rho_w=1000.0,
               Q_mv_h=250.0, Q_w_h=40.0, Q_iz_h=120.0, t_min=15.0,
               rel_mv=0.04, rel_w=0.05, rel_iz=0.06):
    """Z6: balastni tank dvodna, miješanje morske i slatke vode, odzračnik."""
    Q_mv, Q_w, Q_iz = (x / 3600.0 for x in (Q_mv_h, Q_w_h, Q_iz_h))
    rho_mj = (rho_mv * Q_mv + rho_w * Q_w) / (Q_mv + Q_w)
    Q_net = Q_mv + Q_w - Q_iz
    dhdt = Q_net / A_T
    t = t_min * 60.0
    h_t = h_0 + dhdt * t
    dm = rho_mj * Q_net * t
    Q_net_max = Q_mv * (1 + rel_mv) + Q_w * (1 + rel_w) - Q_iz * (1 - rel_iz)
    dhdt_max = Q_net_max / A_T
    h_t_max = h_0 + dhdt_max * t
    t_air = (h_max - h_0) / dhdt_max
    return {
        "rho_mix": rho_mj,
        "Q_net": Q_net,
        "dhdt": dhdt,
        "h_t": h_t,
        "dm": dm,
        "dhdt_max": dhdt_max,
        "h_t_max": h_t_max,
        "t_air": t_air,
    }


def primjer_kinematika_srednja(R=0.025, v_max=3.0):
    # Paraboloidni profil v(r)=v_max(1-(r/R)^2): srednja = v_max/2
    v_mean = v_max / 2
    A = math.pi * R**2
    Q = v_mean * A
    return {"v_mean": v_mean, "A": A, "Q": Q}


def verify():
    out = []

    r = primjer_kinematika_srednja()
    _check(out, "U08.KIN.v_mean", r["v_mean"], 1.5, "m/s")
    _check(out, "U08.KIN.Q", r["Q"], 2.945e-3, "m^3/s")

    r = primjer_1_difuzor()
    _check(out, "U08.P1.v_1", r["v_1"], 3.6, "m/s", rel=1e-10)
    _check(out, "U08.P1.Q_Ls", r["Q"] * 1000, 40.7, "L/s", rel=0.002)
    _check(out, "U08.P1.m_dot", r["m_dot"], 40.6, "kg/s", rel=0.002)

    r = primjer_2_zahvatni_usis()
    _check(out, "U08.P2.v_s", r["v_s"], 9.26, "m/s", rel=0.001)
    _check(out, "U08.P2.m_dot", r["m_dot"], 51.3, "kg/s", rel=0.002)
    _check(out, "U08.P2.w", r["w"], 1.25, "m/s", rel=1e-10)
    _check(out, "U08.P2.w_r", r["w_r"], 2.27, "m/s", rel=0.002)
    _check(out, "U08.P2.v_abs", r["v_abs"], 8.01, "m/s", rel=0.001)
    _check(out, "U08.P2.m_dot_wrong", r["m_dot_wrong"], 328.0, "kg/s", rel=0.002)

    r = cjeloviti_1_mijesajuci()
    _check(out, "U08.CH1.Q_3", r["Q_3"], 0.01414, "m^3/s")
    _check(out, "U08.CH1.rho_3", r["rho_3"], 1025.0, "kg/m^3")
    _check(out, "U08.CH1.dhdt_mm_s", r["dhdt"] * 1000, 1.57, "mm/s", rel=0.02)
    _check(out, "U08.CH1.t", r["t"], 255.0, "s", rel=0.02)
    _check(out, "U08.CH1.dm", r["dm"], 2583.0, "kg", rel=0.02)

    r = primjer_5_T_komad()
    _check(out, "U08.P5.Q_1_Ls", r["Q_1"] * 1000, 3.62, "L/s")
    _check(out, "U08.P5.Q_2_Ls", r["Q_2"] * 1000, 2.17, "L/s", rel=0.02)
    _check(out, "U08.P5.v_2", r["v_2"], 6.9, "m/s", rel=0.02)
    _check(out, "U08.P5.D_3_mm", r["D_3"] * 1000, 24.8, "mm", rel=0.02)

    r = primjer_ev_hladenje()
    _check(out, "U08.P6.v_1", r["v_1"], 1.326, "m/s", rel=0.02)
    _check(out, "U08.P6.v_d", r["v_d"], 0.921, "m/s", rel=0.02)
    _check(out, "U08.P6.v_blocked", r["v_blocked"], 0.982, "m/s", rel=0.02)
    _check(out, "U08.P6.rise_percent", r["rise_percent"], 6.67, "%", rel=0.02)

    r = zadatak_1()
    _check(out, "U08.Z1.m_dot", r["m_dot"], 4.32, "kg/s", rel=1e-10)
    _check(out, "U08.Z1.v_2", r["v_2"], 17.6, "m/s", rel=0.003)
    _check(out, "U08.Z1.Q_1", r["Q_1"], 3.60, "m^3/s", rel=1e-10)
    _check(out, "U08.Z1.Q_2", r["Q_2"], 4.24, "m^3/s", rel=0.002)

    r = zadatak_2()
    _check(out, "U08.Z2.v_n", r["v_n"], 1.50, "m/s", rel=0.001)
    _check(out, "U08.Z2.Q_Ls", r["Q"]*1000, 6.00, "L/s", rel=0.001)
    _check(out, "U08.Z2.m_dot", r["m_dot"], 5.988, "kg/s", rel=0.001)
    _check(out, "U08.Z2.reverse_Q_Ls", zadatak_2(theta_deg=120)["Q"]*1000, -6.00, "L/s", rel=0.001)

    r = zadatak_3()
    _check(out, "U08.Z3.Q_3_Ls", r["Q_3"] * 1000, 20.0, "L/s")
    _check(out, "U08.Z3.v_3", r["v_3"], 1.768, "m/s", rel=0.02)

    r = zadatak_4()
    _check(out, "U08.Z4.Q_2_Ls", r["Q_2"] * 1000, 23.0, "L/s", rel=0.02)
    _check(out, "U08.Z4.Q_3_Ls", r["Q_3"] * 1000, 7.0, "L/s", rel=0.02)
    _check(out, "U08.Z4.v_2", r["v_2"], 3.62, "m/s", rel=0.02)
    _check(out, "U08.Z4.v_3", r["v_3"], 1.81, "m/s", rel=0.02)

    r = zadatak_5()
    _check(out, "U08.Z5.Q_out_rel_Ls", r["Q_out_rel"]*1000, 0.4712, "L/s", rel=0.001)
    _check(out, "U08.Z5.u", r["u"], 0.06732, "m/s", rel=0.001)
    _check(out, "U08.Z5.v_out", r["v_out"], 1.5673, "m/s", rel=0.001)
    _check(out, "U08.Z5.t", r["t"], 1.7824, "s", rel=0.001)
    _check(out, "U08.Z5.dm", r["dm"], 0.9406, "kg", rel=0.001)
    _check(out, "U08.Z5.w_stopped", r["w_stopped"], 3.1831, "m/s", rel=0.001)

    r = zadatak_6()
    _check(out, "U08.Z6.rho_mix", r["rho_mix"], 1021.6, "kg/m^3", rel=0.0001)
    _check(out, "U08.Z6.dhdt_mm_s", r["dhdt"] * 1000, 1.312, "mm/s", rel=0.001)
    _check(out, "U08.Z6.h_15min", r["h_t"], 1.48, "m", rel=0.002)
    _check(out, "U08.Z6.dm_t", r["dm"] / 1000, 43.4, "t", rel=0.001)
    _check(out, "U08.Z6.dhdt_max_mm_s", r["dhdt_max"] * 1000, 1.460, "mm/s", rel=0.001)
    _check(out, "U08.Z6.h_15min_max", r["h_t_max"], 1.61, "m", rel=0.003)
    _check(out, "U08.Z6.t_air_s", r["t_air"], 890.0, "s", rel=0.001)

    z1,z2,z3,z4,z5,z6 = (zadatak_1(),zadatak_2(),zadatak_3(),
                         zadatak_4(),zadatak_5(),zadatak_6())
    _invariant(out, "U08.INV.z1_mass_not_volume", abs(1.02*.24*z1["v_2"]-z1["m_dot"]) < 1e-12
               and z1["Q_2"] > z1["Q_1"] and z1["v_2"] > 12.0
               and abs(zadatak_1(rho_2=1.20)["Q_2"]-z1["Q_1"]) < 1e-12,
               "Grijac ne zatvara masenu bilancu ili volumenski protok ne raste s padom gustoce.")
    p2 = primjer_2_zahvatni_usis()
    _invariant(out, "U08.INV.p2_relative_velocity", abs(1025*.040*p2["w"]-p2["m_dot"]) < 1e-12
               and abs(primjer_2_zahvatni_usis(v_s_kn=0.0)["m_dot"]-p2["m_dot"]) < 1e-12
               and abs(primjer_2_zahvatni_usis(v_s_kn=0.0)["v_abs"]+p2["w"]) < 1e-12
               and p2["m_dot_wrong"] > 6*p2["m_dot"],
               "Tok kroz pomicnu plohu ne ovisi samo o relativnoj brzini.")
    _invariant(out, "U08.INV.z2_orientation", abs(zadatak_2(theta_deg=90)["Q"]) < 1e-14
               and abs(zadatak_2(theta_deg=0)["Q"]-.012) < 1e-14
               and abs(zadatak_2(theta_deg=120)["Q"]+z2["Q"]) < 1e-14,
               "Predznak ili normalna komponenta protoka nisu konzistentni.")
    _invariant(out, "U08.INV.z3_mass", abs(998*.020-998*math.pi*.12**2/4*z3["v_3"]) < 1e-12,
               "Mjesalica ne zatvara masenu bilancu.")
    _invariant(out, "U08.INV.z4_partition", abs(z4["Q_2"]+z4["Q_3"]-.030) < 1e-14
               and abs(z4["v_2"]-2*z4["v_3"]) < 1e-14,
               "Razdjelnik ne zadovoljava i bilancu i zadani omjer.")
    _invariant(out, "U08.INV.z5_moving_mass", abs(998*.001-998*z5["A_o"]*(z5["v_out"]-z5["u"])
               -z5["dm"]/z5["t"]) < 1e-12,
               "RTT na pomicanom izlazu ne zatvara akumulaciju.")
    _invariant(out, "U08.INV.z5_swept_volume", abs(z5["u"]*z5["t"]-.12) < 1e-14
               and abs(z5["dm"]-998*(.001-z5["Q_out_rel"])*z5["t"]) < 1e-12,
               "Hod i integrirana masena bilanca daju razlicitu akumulaciju.")
    _invariant(out, "U08.INV.z5_impermeable_limit", abs(zadatak_5(w=0)["u"]-4*.001/(math.pi*.1**2)) < 1e-14,
               "Zatvoreni izlaz ne daje pomak klipa iz cijelog dotoka.")
    _invariant(out, "U08.INV.z5_stopped_limit", abs(zadatak_5(w=z5["w_stopped"])["u"]) < 1e-14
               and z5["w_stopped"] > 1.5,
               "Zaustavljeni klip uz zadani dotok ne zatvara izlaz.")
    Qm,Qs,Qiz = 250/3600,40/3600,120/3600
    _invariant(out, "U08.INV.z6_mass", 1000 < z6["rho_mix"] < 1025
               and abs(z6["dm"]/900-(1025*Qm+1000*Qs-z6["rho_mix"]*Qiz)) < 1e-9,
               "Mijesanje i akumulacija nisu maseno konzistentni.")
    from itertools import product
    levels = [.30+(Qm*(1+a)+Qs*(1+b)-Qiz*(1+c))*900/36.0 for a,b,c in product(
              (-.04,.04),(-.05,.05),(-.06,.06))]
    _invariant(out, "U08.INV.z6_interval_and_airpipe", abs(max(levels)-z6["h_t_max"]) < 1e-12
               and z6["h_t"] < 1.60 < z6["h_t_max"]
               and abs(.30+z6["t_air"]*z6["dhdt_max"]-1.60) < 1e-12
               and z6["t_air"] < 900,
               "Nominalni i intervalni kriterij odzracne cijevi nisu ispravno razdvojeni.")

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
