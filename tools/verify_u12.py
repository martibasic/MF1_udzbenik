"""Numerička verifikacija kanonskoga U14; naslijeđeni namespace U12."""
from __future__ import annotations

import math

TOL = 0.01


def _close(value, target, rel=TOL):
    if target == 0:
        return abs(value) < rel
    return abs(value - target) / abs(target) <= rel


def _check(out, rid, value, target, unit="", rel=TOL, *, abs_tol=None):
    ok = math.isfinite(value) and (
        abs(value-target) <= abs_tol if abs_tol is not None else _close(value, target, rel)
    )
    out.append({
        "id": rid, "status": "OK" if ok else "FAIL", "verification": "golden",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


def _invariant(out, rid, condition, details=""):
    out.append({"id": rid, "status": "OK" if condition else "FAIL",
                "verification": "invariant", "details": "" if condition else details})


def primjer_1_vodilica(b=0.036, h=0.014, v_1=24.0, v_2=19.0, beta_deg=120.0,
                        rho=998.0):
    A = b * h
    m_dot = rho * A * v_1
    beta = math.radians(beta_deg)
    v_2x = v_2 * math.cos(beta)
    v_2y = v_2 * math.sin(beta)
    F_f_x = -m_dot * (v_2x - v_1)
    F_f_y = -m_dot * (v_2y - 0)
    R = math.sqrt(F_f_x**2 + F_f_y**2)
    return {"m_dot": m_dot, "F_f_x": F_f_x, "F_f_y": F_f_y, "R": R}


def primjer_2_ukljestena(Q=0.015, v=12.5, h=0.45, l=0.70, alpha_deg=60.0,
                          rho=998.0):
    d = math.sqrt(4 * Q / (math.pi * v))
    m_dot = rho * Q
    alpha = math.radians(alpha_deg)
    v_2x = -v * math.cos(alpha)
    v_2y = v * math.sin(alpha)
    F_l_x = m_dot * (v_2x - v)
    F_l_y = m_dot * v_2y
    R_x = -F_l_x
    R_y = -F_l_y
    M_O = -m_dot * v * (h + l * math.sin(alpha))
    return {"d": d, "R_x": R_x, "R_y": R_y, "M_O": M_O}


def primjer_3_relativni(d=0.038, c_1=22.0, u=8.0, rho=998.0):
    A = math.pi * d**2 / 4
    w_1 = c_1 - u
    m_rel = rho * A * w_1
    m_full = rho * A * c_1
    ratio = m_rel / m_full
    return {"w_1": w_1, "m_rel": m_rel, "ratio": ratio}


def primjer_4_pokretna_ravna(d=0.040, c_1=24.0, u=9.0, rho=998.0):
    A = math.pi * d**2 / 4
    c_r = c_1 - u
    m_rel = rho * A * c_r
    F = m_rel * (c_1 - u)
    P = F * u
    return {"m_rel": m_rel, "F": F, "P": P}


def cjeloviti_1_zakrivljena(d=0.045, c_1=26.0, u=10.0, k=0.90,
                             beta_deg=30.0, rho=998.0):
    A = math.pi * d**2 / 4
    w_1 = c_1 - u
    m_rel = rho * A * w_1
    w_2 = k * w_1
    beta = math.radians(beta_deg)
    w_2x = -w_2 * math.cos(beta)
    w_2y = w_2 * math.sin(beta)
    c_2x = u + w_2x
    c_2y = w_2y
    F_l_x = m_rel * (c_2x - c_1)
    F_l_y = m_rel * (c_2y - 0)
    F_f_x = -F_l_x
    F_f_y = -F_l_y
    F = math.sqrt(F_f_x**2 + F_f_y**2)
    P = F_f_x * u
    return {"m_rel": m_rel, "c_2x": c_2x, "c_2y": c_2y,
            "F_f_x": F_f_x, "F_f_y": F_f_y, "F": F, "P": P}


def cjeloviti_2_pelton(d=0.044, c_1=31.0, n=320.0, r=0.46, k=0.90,
                        beta_deg=20.0, rho=998.0, P_G=9.5e3):
    A = math.pi * d**2 / 4
    omega = 2 * math.pi * n / 60
    u = omega * r
    w_1 = c_1 - u
    m_rel = rho * A * w_1
    w_2 = k * w_1
    beta = math.radians(beta_deg)
    w_2x = -w_2 * math.cos(beta)
    c_2x = u + w_2x
    F_l_x = m_rel * (c_2x - c_1)
    F_f_x = -F_l_x
    M = F_f_x * r
    P = M * omega
    dP = P - P_G
    return {"u": u, "w_1": w_1, "m_rel": m_rel, "c_2x": c_2x,
            "F_f_x": F_f_x, "M": M, "P": P, "dP": dP}


def cjeloviti_3_flyboard(m=150.0, d=0.050, v=15.0, h=10.0, rho=1000.0, g=9.81):
    A_1 = math.pi * d**2 / 4
    A = 4 * A_1
    v_min = math.sqrt(m * g / (rho * A))
    F_p = rho * A * v**2
    G = m * g
    F_R = F_p - G
    a = F_R / m
    t = math.sqrt(2 * h / a)
    v_10 = a * t
    dh = v_10**2 / (2 * g)
    h_max = h + dh
    t_gore = v_10 / g
    t_iznad_10 = 2 * t_gore
    return {"A": A, "v_min": v_min, "F_p": F_p, "a": a, "t": t,
            "v_10": v_10, "dh": dh, "h_max": h_max, "t_iznad_10": t_iznad_10}


def primjer_pelton_lopatica(d=0.060, c_1=40.0, u=18.0, beta2_deg=165.0,
                              rho=998.0):
    A = math.pi * d**2 / 4
    w_1 = c_1 - u
    m_dot = rho * A * w_1
    w_2 = w_1
    c_2x = u + w_2 * math.cos(math.radians(beta2_deg))
    F_t = m_dot * (c_1 - c_2x)
    P = F_t * u
    return {"w_1": w_1, "m_dot": m_dot, "c_2x": c_2x, "F_t": F_t, "P": P}


def primjer_hidromlazni(d=0.120, v_mlaz=8.5, rho=1005.0, V_plovilo=1.2):
    A = math.pi * d**2 / 4
    m_dot = rho * A * v_mlaz
    F_p = m_dot * v_mlaz
    P_kin = 0.5 * m_dot * v_mlaz**2
    return {"A": A, "m_dot": m_dot, "F_p": F_p, "P_kin": P_kin}


def primjer_kvadrokopter(m=2.4, rotor_count=4, D=0.280, rho=1.045,
                          eta=0.70, g=9.81, battery_Wh=74.0):
    """Javni primjer aktuatorskoga diska kvadrokoptera u visu."""

    thrust = m * g / rotor_count
    A = math.pi * D**2 / 4
    induced_velocity = math.sqrt(thrust / (2 * rho * A))
    P_ideal = thrust * induced_velocity
    P_shaft = P_ideal / eta
    P_total = rotor_count * P_shaft
    duration_min = battery_Wh / P_total * 60
    return {
        "thrust": thrust,
        "induced_velocity": induced_velocity,
        "P_ideal": P_ideal,
        "P_shaft": P_shaft,
        "P_total": P_total,
        "duration_min": duration_min,
    }


def zadatak_1(d=0.022, v=24.0, rho=998.0):
    A = math.pi*d*d/4
    m_dot = rho*A*v
    return {"m_dot": m_dot, "F": m_dot*v, "P": 0.0}


def zadatak_2(v=26.0, b=0.030, h=0.016, beta_deg=110.0, rho=998.0):
    m_dot = rho*b*h*v
    beta = math.radians(beta_deg)
    c2x,c2y = v*math.cos(beta),v*math.sin(beta)
    Fx,Fy = m_dot*(v-c2x),-m_dot*c2y
    return {"m_dot":m_dot,"F_x":Fx,"F_y":Fy,"R_x":-Fx,"R_y":-Fy,
            "R":math.hypot(Fx,Fy),"c2x":c2x,"c2y":c2y}


def zadatak_3(c1=32.0, u=12.0, m_rel=18.0, Fx=625.0, Fy=-153.0):
    """Reconstruct the flow from the given force of fluid on the moving blade."""
    if c1 <= u or m_rel <= 0:
        raise ValueError("Potreban je pozitivan relativni dotok.")
    c2x,c2y = c1-Fx/m_rel,-Fy/m_rel
    w1 = c1-u
    w2x,w2y = c2x-u,c2y
    w2 = math.hypot(w2x,w2y)
    P = Fx*u
    loss = .5*m_rel*(w1*w1-w2*w2)
    return {"c2x":c2x,"c2y":c2y,"w2x":w2x,"w2y":w2y,
            "w1":w1,"w2":w2,"k":w2/w1,
            "beta_deg":math.degrees(math.atan2(w2y,w2x)),"P":P,"loss":loss,
            "absolute_kinetic_drop":.5*m_rel*(c1*c1-c2x*c2x-c2y*c2y)}


def zadatak_4(r1=.060, r2=.140, omega=200.0, m_dot=3.00,
              c1t=5.0, c1r=4.0, c2t=20.0, c2r=6.0):
    """Steady rotor control volume; signs are rotor-to-fluid."""
    u1,u2 = omega*r1,omega*r2
    M = m_dot*(r2*c2t-r1*c1t)
    specific_work = u2*c2t-u1*c1t
    return {"u1":u1,"u2":u2,"w1t":c1t-u1,"w1r":c1r,
            "w2t":c2t-u2,"w2r":c2r,"M":M,"M_reaction":-M,
            "P":m_dot*specific_work,"e":specific_work}


def zadatak_5(T=2000.0, U=8.0, rho=1000.0, eta=.80,
              jet_speeds=(20.0,30.0), electric_limit=40000.0):
    candidates=[]
    for Vj in jet_speeds:
        if Vj <= U or U < 0 or T <= 0 or not 0 < eta <= 1:
            raise ValueError("Model zahtijeva Vj>U>=0, T>0 i 0<eta<=1.")
        m_dot = T/(Vj-U)
        Q = m_dot/rho
        d = math.sqrt(4*Q/(math.pi*Vj))
        Ph = .5*m_dot*(Vj*Vj-U*U)
        candidates.append({"Vj":Vj,"m_dot":m_dot,"Q":Q,"d":d,
                           "Ph":Ph,"Pel":Ph/eta,"useful":T*U,
                           "eta_prop":T*U/Ph,"wake":.5*m_dot*(Vj-U)**2})
    feasible=[i+1 for i,r in enumerate(candidates) if r["Pel"]<=electric_limit]
    return {"candidates":candidates,"feasible":feasible}


def zadatak_6(m=110.0, d=0.028, n_sapnica=4, v=36.0, rho=998.0,
              g=9.81, dd=0.0003, dv=1.5, reserve=0.10):
    A = n_sapnica*math.pi*d*d/4
    F_p = rho*A*v*v
    A_min = n_sapnica*math.pi*(d-dd)**2/4
    F_min = rho*A_min*(v-dv)**2
    return {"F_p":F_p,"m_max":F_p/g,"a":F_p/m-g,
            "F_min":F_min,"m_limit":F_min/((1+reserve)*g)}


# ------------ Faza 1.5 dodatak: Krivulja snage P(u) i optimum (CH T3) ----------------
def cjeloviti_4_optimum(d=0.050, c_1=30.0, beta2_deg=165.0, k=0.90,
                         rho=998.0, R_rotor=0.20):
    A = math.pi * d**2 / 4
    m_dot = rho * A * c_1
    faktor = 1 - k * math.cos(math.radians(beta2_deg))  # 1 - k*cos(beta2)
    # Sila i snaga kao funkcija u:
    def F(u):
        return m_dot * (c_1 - u) * faktor

    def P(u):
        return F(u) * u

    u_opt = c_1 / 2
    P_max = P(u_opt)
    omega_opt = u_opt / R_rotor
    n_opt = omega_opt * 60 / (2 * math.pi)
    P_hid = 0.5 * m_dot * c_1**2
    eta_max = P_max / P_hid
    # Suboptimumi
    P_quart = P(c_1 / 4)
    P_third = P(c_1 / 3)
    P_two_third = P(2 * c_1 / 3)
    return {"u_opt": u_opt, "P_max": P_max, "n_opt": n_opt,
            "P_hid": P_hid, "eta_max": eta_max, "faktor": faktor,
            "P_quart": P_quart, "P_third": P_third, "P_two_third": P_two_third}


def verify():
    out = []

    r = primjer_1_vodilica()
    _check(out, "U12.P1.m_dot", r["m_dot"], 12.07, "kg/s", rel=0.02)
    _check(out, "U12.P1.F_f_x", r["F_f_x"], 404.4, "N", rel=0.02)
    _check(out, "U12.P1.R", r["R"], 451.0, "N", rel=0.02)

    r = primjer_3_relativni()
    _check(out, "U12.P2.w_1", r["w_1"], 14.0, "m/s")
    _check(out, "U12.P2.m_rel", r["m_rel"], 15.85, "kg/s", rel=0.02)
    _check(out, "U12.P2.ratio", r["ratio"], 0.636, "", rel=0.02)

    r = primjer_4_pokretna_ravna()
    _check(out, "U12.P3.m_rel", r["m_rel"], 18.81, "kg/s", rel=0.02)
    _check(out, "U12.P3.F", r["F"], 282.0, "N", rel=0.02)
    _check(out, "U12.P3.P", r["P"], 2540.0, "W", rel=0.02)

    r = cjeloviti_1_zakrivljena()
    _check(out, "U12.P4.m_rel", r["m_rel"], 25.4, "kg/s", rel=0.02)
    _check(out, "U12.P4.c_2x", r["c_2x"], -2.47, "m/s", rel=0.05)
    _check(out, "U12.P4.F_f_x", r["F_f_x"], 723.0, "N", rel=0.02)
    _check(out, "U12.P4.F", r["F"], 746.0, "N", rel=0.02)
    _check(out, "U12.P4.P", r["P"], 7230.0, "W", rel=0.02)

    r = cjeloviti_2_pelton()
    _check(out, "U12.P5.u", r["u"], 15.41, "m/s", rel=0.02)
    _check(out, "U12.P5.w_1", r["w_1"], 15.59, "m/s", rel=0.02)
    _check(out, "U12.P5.m_rel", r["m_rel"], 23.65, "kg/s", rel=0.02)
    _check(out, "U12.P5.F_f_x", r["F_f_x"], 680.3, "N", rel=0.02)
    _check(out, "U12.P5.M", r["M"], 313.0, "Nm", rel=0.02)
    _check(out, "U12.P5.P_kW", r["P"] / 1000, 10.49, "kW", rel=0.02)

    r = primjer_kvadrokopter()
    _check(out, "U12.P6.thrust", r["thrust"], 5.886, "N", rel=0.02)
    _check(out, "U12.P6.induced_velocity", r["induced_velocity"], 6.76, "m/s", rel=0.02)
    _check(out, "U12.P6.P_ideal", r["P_ideal"], 39.8, "W", rel=0.02)
    _check(out, "U12.P6.P_shaft", r["P_shaft"], 56.9, "W", rel=0.02)
    _check(out, "U12.P6.P_total", r["P_total"], 227.0, "W", rel=0.02)
    _check(out, "U12.P6.duration_min", r["duration_min"], 19.5, "min", rel=0.02)

    r = zadatak_1()
    _check(out, "U12.Z1.m_dot", r["m_dot"], 9.10, "kg/s", abs_tol=.005)
    _check(out, "U12.Z1.F", r["F"], 219.0, "N", abs_tol=.5)
    _check(out, "U12.Z1.P", r["P"], 0.0, "W", abs_tol=1e-12)
    faster = zadatak_1(v=48.0)
    _invariant(out, "U12.Z1.quadratic_velocity", abs(faster["F"]/r["F"]-4)<1e-12,
               "Sila na nepomicnu plocu raste kvadratom brzine pri istom presjeku.")

    r = zadatak_2()
    _check(out, "U12.Z2.m_dot", r["m_dot"], 12.46, "kg/s", abs_tol=.005)
    _check(out, "U12.Z2.F_x", r["F_x"], 435.0, "N", abs_tol=.5)
    _check(out, "U12.Z2.F_y", r["F_y"], -304.0, "N", abs_tol=.5)
    _check(out, "U12.Z2.R_x", r["R_x"], -435.0, "N", abs_tol=.5)
    _check(out, "U12.Z2.R_y", r["R_y"], 304.0, "N", abs_tol=.5)
    _check(out, "U12.Z2.R", r["R"], 531.0, "N", abs_tol=.5)
    _invariant(out, "U12.Z2.energy_and_direction",
               abs(r["c2x"]**2+r["c2y"]**2-26**2)<1e-10
               and r["F_x"]>0>r["F_y"] and r["R_x"]<0<r["R_y"],
               "Mirna idealna vodilica ne mijenja kineticku energiju, ali mijenja impuls.")

    r = zadatak_3()
    _check(out, "U12.Z3.c2x", r["c2x"], -2.722, "m/s", abs_tol=.0005)
    _check(out, "U12.Z3.c2y", r["c2y"], 8.500, "m/s", abs_tol=.0005)
    _check(out, "U12.Z3.w2x", r["w2x"], -14.722, "m/s", abs_tol=.0005)
    _check(out, "U12.Z3.w2y", r["w2y"], 8.500, "m/s", abs_tol=.0005)
    _check(out, "U12.Z3.k", r["k"], .850, "", abs_tol=.0005)
    _check(out, "U12.Z3.beta", r["beta_deg"], 150.00, "degree", abs_tol=.005)
    _check(out, "U12.Z3.P_kW", r["P"]/1000, 7.500, "kW", abs_tol=.0005)
    _check(out, "U12.Z3.loss_kW", r["loss"]/1000, .999, "kW", abs_tol=.0005)
    _invariant(out, "U12.Z3.momentum_and_energy",
               abs(18*(32-r["c2x"])-625)<1e-10
               and abs(-18*r["c2y"]+153)<1e-10
               and abs(r["absolute_kinetic_drop"]-r["P"]-r["loss"])<1e-9
               and 0<r["k"]<1 and r["loss"]>0,
               "Rekonstruirani tok zatvara obje sile i energiju pasivne lopatice.")
    active = zadatak_3(Fx=800.0)
    _invariant(out, "U12.Z3.reject_active_blade", active["k"]>1 and active["loss"]<0,
               "Nedopusteni mjerni skup mora otkriti potrebu dodatnog energetskog ulaza.")

    r = zadatak_4()
    _check(out, "U12.Z4.u1", r["u1"], 12.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.u2", r["u2"], 28.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.w1t", r["w1t"], -7.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.w1r", r["w1r"], 4.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.w2t", r["w2t"], -8.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.w2r", r["w2r"], 6.0, "m/s", abs_tol=1e-10)
    _check(out, "U12.Z4.M", r["M"], 7.50, "Nm", abs_tol=.005)
    _check(out, "U12.Z4.M_reaction", r["M_reaction"], -7.50, "Nm", abs_tol=.005)
    _check(out, "U12.Z4.P_kW", r["P"]/1000, 1.500, "kW", abs_tol=.0005)
    _check(out, "U12.Z4.e", r["e"], 500.0, "J/kg", abs_tol=.5)
    _invariant(out, "U12.Z4.euler_and_torque", abs(r["P"]-200*r["M"])<1e-10
               and r["M"]>0 and r["M_reaction"]<0,
               "Crpni rotor predaje fluidu rad; reakcijski moment je suprotan.")
    reverse=zadatak_4(c2t=-2.0)
    radial=zadatak_4(c2r=10.0)
    _invariant(out, "U12.Z4.swirl_controls_work", reverse["P"]<0
               and abs(radial["P"]-r["P"])<1e-10,
               "Radijalna komponenta ne doprinosi osnom momentu, vrtlog moze promijeniti znak rada.")

    r = zadatak_5();a,b=r["candidates"]
    _check(out, "U12.Z5.Q_A_Ls", a["Q"]*1000, 166.67, "L/s", abs_tol=.005)
    _check(out, "U12.Z5.Q_B_Ls", b["Q"]*1000, 90.91, "L/s", abs_tol=.005)
    _check(out, "U12.Z5.d_A_mm", a["d"]*1000, 103.01, "mm", abs_tol=.005)
    _check(out, "U12.Z5.d_B_mm", b["d"]*1000, 62.12, "mm", abs_tol=.005)
    _check(out, "U12.Z5.Ph_A_kW", a["Ph"]/1000, 28.0, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.Ph_B_kW", b["Ph"]/1000, 38.0, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.Pel_A_kW", a["Pel"]/1000, 35.0, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.Pel_B_kW", b["Pel"]/1000, 47.5, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.eta_A", a["eta_prop"], .571, "", abs_tol=.0005)
    _check(out, "U12.Z5.eta_B", b["eta_prop"], .421, "", abs_tol=.0005)
    _check(out, "U12.Z5.useful_kW", a["useful"]/1000, 16.0, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.wake_A_kW", a["wake"]/1000, 12.0, "kW", abs_tol=1e-9)
    _check(out, "U12.Z5.wake_B_kW", b["wake"]/1000, 22.0, "kW", abs_tol=1e-9)
    _invariant(out, "U12.Z5.energy_and_selection", r["feasible"]==[1]
               and all(abs(c["Ph"]-c["useful"]-c["wake"])<1e-8 for c in (a,b))
               and a["Q"]>b["Q"] and a["eta_prop"]>b["eta_prop"],
               "Oba toka daju isti potisak, ali samo A zadovoljava elektricnu granicu.")
    static=zadatak_5(U=0.0)["candidates"][0]
    _invariant(out, "U12.Z5.static_limit", static["Ph"]>0 and static["useful"]==0
               and static["eta_prop"]==0,
               "Statički potisak ne daje korisnu translacijsku snagu TU.")

    r = zadatak_6()
    _check(out, "U12.Z6.F_p_kN", r["F_p"]/1000, 3.186, "kN", abs_tol=.0005)
    _check(out, "U12.Z6.m_max", r["m_max"], 324.7, "kg", abs_tol=.05)
    _check(out, "U12.Z6.a", r["a"], 19.15, "m/s2", abs_tol=.005)
    _check(out, "U12.Z6.F_min_kN", r["F_min"]/1000, 2.863, "kN", abs_tol=.0005)
    _check(out, "U12.Z6.m_limit", r["m_limit"], 265.3, "kg", abs_tol=.05)
    _invariant(out, "U12.Z6.force_and_worst_case",
               abs(110*(r["a"]+9.81)-r["F_p"])<1e-9
               and r["F_min"]<r["F_p"] and r["m_limit"]<r["m_max"]
               and abs(r["F_min"]-1.1*r["m_limit"]*9.81)<1e-9
               and r["F_min"]<1.1*(r["m_limit"]+.1)*9.81,
               "Nazivna sila zatvara Newtonov zakon, a granicna masa cijeli interval i rezervu.")

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
    raise SystemExit(1 if fail else 0)
