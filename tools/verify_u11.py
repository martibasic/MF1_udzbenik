"""Numericka verifikacija U11 (javno poglavlje 10): kolicina i moment kolicine gibanja."""
from __future__ import annotations

import math

TOL = 0.01


def _close(value, target, rel=TOL):
    if target == 0:
        return abs(value) < rel
    return abs(value - target) / abs(target) <= rel


def _check(out, rid, value, target, unit="", rel=TOL, abs_tol=None):
    ok = math.isfinite(value) and (abs(value-target) <= abs_tol if abs_tol is not None else _close(value, target, rel))
    out.append({
        "id": rid, "status": "OK" if ok else "FAIL",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


def _invariant(out, rid, condition, message):
    out.append({"id": rid, "status": "OK" if condition else "FAIL",
                "verification": "invariant", "details": "" if condition else message})


def primjer_1_pelton(d=0.050, v=30.0, u=12.0, theta_deg=165.0, rho=998.0):
    """P1: Peltonova lopatica u gibanju; jedna lopatica i kolo."""
    A = math.pi * d**2 / 4
    w = v - u
    theta = math.radians(theta_deg)
    mdot_rel = rho * A * w
    F = mdot_rel * w * (1 - math.cos(theta))
    P = F * u
    v2x = u + w * math.cos(theta)
    v2y = w * math.sin(theta)
    v2 = math.hypot(v2x, v2y)
    energy_power = mdot_rel * (v * v - v2 * v2) / 2
    mdot_wheel = rho * A * v
    F_wheel = mdot_wheel * w * (1 - math.cos(theta))
    P_wheel = F_wheel * u
    u_opt = v / 2
    P_wheel_max = mdot_wheel * u_opt * (v - u_opt) * (1 - math.cos(theta))
    return {"A": A, "w": w, "mdot_rel": mdot_rel, "F": F, "P": P, "v2": v2,
            "energy_power": energy_power, "mdot_wheel": mdot_wheel,
            "F_wheel": F_wheel, "P_wheel": P_wheel, "u_opt": u_opt,
            "P_wheel_max": P_wheel_max}


def primjer_2_mlaznica(D=0.220, d=0.090, F_P=215.0, rho=998.0):
    A_1 = math.pi * D**2 / 4
    A_2 = math.pi * d**2 / 4
    v_2 = math.sqrt(F_P / (rho * A_2))
    Q = A_2 * v_2
    v_1 = Q / A_1
    p_M1 = rho / 2 * (v_2**2 - v_1**2)
    m_dot = rho * Q
    R = p_M1 * A_1 - m_dot * (v_2 - v_1)
    return {"v_2": v_2, "Q": Q, "v_1": v_1, "p_M1": p_M1, "R": R}


def primjer_3_koljeno(D_1=0.180, D_2=0.120, Q=0.045, p_M1=52e3, p_M2=43e3,
                       rho=998.0, beta=1.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = Q / A_1
    v_2 = Q / A_2
    m_dot = rho * Q
    R_st_x = beta * m_dot * (0 - v_1) - p_M1 * A_1
    R_st_y = beta * m_dot * v_2 - (-p_M2 * A_2)
    F_x = -R_st_x
    F_y = -R_st_y
    F_R = math.sqrt(F_x**2 + F_y**2)
    return {"v_1": v_1, "v_2": v_2, "R_st_x": R_st_x, "R_st_y": R_st_y,
            "F_f_x": F_x, "F_f_y": F_y, "F_R": F_R}


def cjeloviti_1_T_racva(D_1=0.180, D_2=0.090, D_3=0.080, p_M1=40e3, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    # v = ratio · v_1; Bernoulli → v² - v_1² = 2 p_M1/ρ
    ratio = A_1 / (A_2 + A_3)
    v_1 = math.sqrt(2 * p_M1 / rho / (ratio**2 - 1))
    v = ratio * v_1
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v
    Q_3 = A_3 * v
    m_dot_1 = rho * Q_1
    m_dot_2 = rho * Q_2
    m_dot_3 = rho * Q_3
    F_st_x = m_dot_2 * v - m_dot_1 * v_1 - p_M1 * A_1
    F_st_y = m_dot_3 * v
    F_f_x = -F_st_x
    F_f_y = -F_st_y
    F_R = math.sqrt(F_f_x**2 + F_f_y**2)
    return {"v_1": v_1, "v": v, "Q_1": Q_1, "Q_2": Q_2, "Q_3": Q_3,
            "F_f_x": F_f_x, "F_f_y": F_f_y, "F_R": F_R}


def cjeloviti_2_Y_racva(D_1=0.170, D_2=0.100, D_3=0.080, R_y=625.0,
                         angle_deg=60.0, rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    A_3 = math.pi * D_3**2 / 4
    sin60 = math.sin(math.radians(angle_deg))
    cos60 = math.cos(math.radians(angle_deg))
    # R_y = ρ A_3 v² sin60
    v = math.sqrt(R_y / (rho * A_3 * sin60))
    v_1 = (A_2 + A_3) / A_1 * v
    Q_1 = A_1 * v_1
    Q_2 = A_2 * v
    Q_3 = A_3 * v
    p_M1 = rho / 2 * (v**2 - v_1**2)
    m_dot_1 = rho * Q_1
    m_dot_2 = rho * Q_2
    m_dot_3 = rho * Q_3
    # R_st_x: p_M1·A_1 + R_st_x = m_dot_2·v + m_dot_3·v·cos60 - m_dot_1·v_1
    R_st_x = m_dot_2 * v + m_dot_3 * v * cos60 - m_dot_1 * v_1 - p_M1 * A_1
    R_x = R_st_x  # reakcija nosaca na racvu = sila stijenke na fluid (isti smjer)
    R_total = math.sqrt(R_x**2 + R_y**2)
    return {"v": v, "v_1": v_1, "Q_1": Q_1,
            "p_M1": p_M1, "R_x": R_x, "R_total": R_total}


def primjer_mala_hidroelektrana(D=0.200, Q=0.18, p=280e3,
                                 theta_deg=60.0, rho=998.0):
    """P6: sila na koljeno stalnog promjera preko impulsne funkcije I=pA+mv."""

    A = math.pi * D**2 / 4
    v = Q / A
    I = rho * Q * v + p * A
    theta = math.radians(theta_deg)
    F_x = I * (1 - math.cos(theta))
    F_y = I * math.sin(theta)
    F_R = math.hypot(F_x, F_y)
    phi = math.degrees(math.atan2(F_y, F_x))
    # Neovisna vektorska bilanca: F = F_p - mdot (v2 - v1).
    e_in = (1.0, 0.0)
    e_out = (math.cos(theta), -math.sin(theta))
    F_p = tuple(p * A * (a - b) for a, b in zip(e_in, e_out))
    d_mom = tuple(rho * Q * v * (b - a) for a, b in zip(e_in, e_out))
    F_vec = tuple(fp - dm for fp, dm in zip(F_p, d_mom))
    return {"v": v, "I": I, "F_x": F_x, "F_y": F_y, "F_R": F_R, "phi": phi,
            "F_vec": F_vec}


def primjer_7_rotirajuca_mlaznica(d=0.010, R=0.25, Q=2.8e-3, n_rpm=60.0, rho=998.0):
    """P7: rotirajuca mlaznica za pranje tanka pri zadanoj brzini vrtnje."""
    A = math.pi * d**2 / 4
    w = (Q / 2) / A
    omega = 2 * math.pi * n_rpm / 60
    u = omega * R
    mdot = rho * Q
    v_t = w - u
    M = mdot * R * v_t
    P = M * omega
    M_0 = mdot * R * w
    omega_max = w / R
    jet_power = mdot * (w * w - u * u) / 2
    return {"w": w, "omega": omega, "u": u, "mdot": mdot, "v_t": v_t, "M": M,
            "P": P, "M_0": M_0, "omega_max": omega_max,
            "n_max_rpm": omega_max * 60 / (2 * math.pi), "jet_power": jet_power}


def zadatak_1(Q=1.80, v_j=32.0, v_s=18.0, rho=1025.0):
    """Z1: potisak vodomlaznog pogona u sustavu broda."""
    m_dot = rho * Q
    F_T = m_dot * (v_j - v_s)
    P_T = F_T * v_s
    P_jet = m_dot * (v_j**2 - v_s**2) / 2
    return {"m_dot": m_dot, "F_T": F_T, "P_T": P_T, "P_jet": P_jet,
            "eta": P_T / P_jet if P_jet else 1.0}


def zadatak_2(D=4.00, v_A=6.00, v_j=8.00, rho=1025.0):
    """Z2: propeler kao aktuatorski disk."""
    A_d = math.pi * D**2 / 4
    v_d = (v_A + v_j) / 2
    m_dot = rho * A_d * v_d
    F_T = m_dot * (v_j - v_A)
    dp = rho * (v_j**2 - v_A**2) / 2
    return {"A_d": A_d, "v_d": v_d, "m_dot": m_dot, "F_T": F_T,
            "F_T_from_dp": dp * A_d, "dp": dp, "P_T": F_T * v_A,
            "eta_i": v_A / v_d}


def zadatak_3(D=0.200, Q=0.090, p_1=150e3, dz=0.40, V=0.030, xi=0.30, rho=998.0, g=9.81):
    """Z3: koljeno 90 stupnjeva u okomitoj ravnini; ulaz +x, izlaz +z, s tezinom vode i gubitkom."""
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    h_g = xi * v**2 / (2 * g)
    p_2 = p_1 - rho * g * dz - rho * g * h_g
    W = rho * g * V
    F_x = p_1 * A + m_dot * v
    R_z = m_dot * v + p_2 * A + W          # stijenka na fluid, prema gore
    F_z = -R_z
    F_R = math.hypot(F_x, F_z)
    F_z_horizontal_model = -(m_dot * v + p_1 * A)
    return {"v": v, "m_dot": m_dot, "p_2": p_2, "W": W, "F_x": F_x, "F_z": F_z, "F_R": F_R,
            "weight_share": W / R_z, "F_z_horizontal_model": F_z_horizontal_model,
            "F_y": F_z, "h_g": h_g}


def zadatak_4(Q=0.016, v=18.0, b=0.20, e=0.35, rho=998.0):
    F_x = rho * Q * v
    F_y = 0.0
    moment = b * F_y - e * F_x
    return {"F_x": F_x, "F_y": F_y, "M_z": moment,
            "R_x": -F_x, "R_y": -F_y, "M_Rz": -moment}


def zadatak_5(d=0.040, v=20.0, u=8.0, rho=998.0):
    A = math.pi * d**2 / 4
    mdot = rho * A * (v-u)
    F_x = mdot * (v-u)
    v_2 = math.hypot(u, v-u)
    optimum = v/3.0
    return {"mdot_rel": mdot, "F_x": F_x, "power": F_x*u,
            "v_2": v_2, "energy_power": mdot*(v*v-v_2*v_2)/2,
            "u_opt": optimum, "power_max": rho*A*(v-optimum)**2*optimum}


def zadatak_6(D_1=0.140, D_2=0.090, D_3=0.080, Q_1=0.040,
              p_1=185e3, split=0.60, angle_deg=60.0, rho=998.0,
              dp=5e3, rel_Q=0.02, dsplit=0.03, design_factor=1.15):
    def force(p_value, Q_value, split_value):
        A_1 = math.pi * D_1**2 / 4
        A_2 = math.pi * D_2**2 / 4
        A_3 = math.pi * D_3**2 / 4
        Q_2 = split_value * Q_value
        Q_3 = Q_value - Q_2
        v_1 = Q_value / A_1
        v_2 = Q_2 / A_2
        v_3 = Q_3 / A_3
        theta = math.radians(angle_deg)
        F_x = (
            p_value * A_1
            + rho * Q_value * v_1
            - rho * Q_2 * v_2
            - rho * Q_3 * v_3 * math.cos(theta)
        )
        F_y = -rho * Q_3 * v_3 * math.sin(theta)
        return Q_2, Q_3, F_x, F_y, math.hypot(F_x, F_y)

    Q_2, Q_3, F_x, F_y, F_R = force(p_1, Q_1, split)
    corner_forces = []
    for p_value in (p_1 - dp, p_1 + dp):
        for Q_value in (Q_1 * (1 - rel_Q), Q_1 * (1 + rel_Q)):
            for split_value in (split - dsplit, split + dsplit):
                corner_forces.append((force(p_value, Q_value, split_value)[-1],p_value,Q_value,split_value))
    F_max, p_max, Q_max, split_max = max(corner_forces)
    required_rating = design_factor * F_max
    return {
        "Q_2": Q_2,
        "Q_3": Q_3,
        "F_x": F_x,
        "F_y": F_y,
        "F_R": F_R,
        "F_max": F_max,
        "required_rating": required_rating,
        "p_at_max": p_max,
        "Q_at_max": Q_max,
        "split_at_max": split_max,
    }


def verify():
    out = []

    r = primjer_1_pelton()
    _check(out, "U11.P1.mdot_rel", r["mdot_rel"], 35.3, "kg/s", rel=0.005)
    _check(out, "U11.P1.F", r["F"], 1248.0, "N", rel=0.005)
    _check(out, "U11.P1.P_kW", r["P"] / 1000, 14.98, "kW", rel=0.005)
    _check(out, "U11.P1.v_2", r["v2"], 7.12, "m/s", rel=0.005)
    _check(out, "U11.P1.mdot_wheel", r["mdot_wheel"], 58.8, "kg/s", rel=0.005)
    _check(out, "U11.P1.F_wheel", r["F_wheel"], 2080.0, "N", rel=0.005)
    _check(out, "U11.P1.P_wheel_kW", r["P_wheel"] / 1000, 24.96, "kW", rel=0.005)
    _check(out, "U11.P1.u_opt", r["u_opt"], 15.0, "m/s", abs_tol=1e-12)
    _check(out, "U11.P1.P_wheel_max_kW", r["P_wheel_max"] / 1000, 26.0, "kW", rel=0.005)

    r = primjer_2_mlaznica()
    _check(out, "U11.P2.v_2", r["v_2"], 5.82, "m/s", rel=0.02)
    _check(out, "U11.P2.Q_Ls", r["Q"] * 1000, 37.0, "L/s", rel=0.02)
    _check(out, "U11.P2.p_M1_kPa", r["p_M1"] / 1000, 16.4, "kPa", rel=0.02)
    _check(out, "U11.P2.R", r["R"], 445.0, "N", rel=0.03)

    r = primjer_3_koljeno()
    _check(out, "U11.P3.v_1", r["v_1"], 1.77, "m/s", rel=0.02)
    _check(out, "U11.P3.v_2", r["v_2"], 3.98, "m/s", rel=0.02)
    _check(out, "U11.P3.F_f_x", r["F_f_x"], 1402.0, "N", rel=0.02)
    _check(out, "U11.P3.F_f_y", r["F_f_y"], -665.0, "N", rel=0.02)
    _check(out, "U11.P3.F_R", r["F_R"], 1552.0, "N", rel=0.02)
    _check(out, "U11.P3.R_st_x_beta102", primjer_3_koljeno(beta=1.02)["R_st_x"], -1404.0, "N", rel=0.002)
    _check(out, "U11.P3.R_st_y_beta102", primjer_3_koljeno(beta=1.02)["R_st_y"], 669.0, "N", rel=0.002)
    _check(out, "U11.P3.R_st_x_beta133", primjer_3_koljeno(beta=4/3)["R_st_x"], -1429.0, "N", rel=0.002)
    _check(out, "U11.P3.R_st_y_beta133", primjer_3_koljeno(beta=4/3)["R_st_y"], 725.0, "N", rel=0.002)

    r = cjeloviti_1_T_racva()
    _check(out, "U11.CH1.v_1", r["v_1"], 4.48, "m/s", rel=0.005)
    _check(out, "U11.CH1.v", r["v"], 10.01, "m/s", rel=0.005)
    _check(out, "U11.CH1.Q_1", r["Q_1"], 0.1140, "m^3/s", rel=0.005)
    _check(out, "U11.CH1.F_f_x", r["F_f_x"], 891.0, "N", rel=0.005)
    _check(out, "U11.CH1.F_f_y", r["F_f_y"], -503.0, "N", rel=0.005)
    _check(out, "U11.CH1.F_R", r["F_R"], 1023.0, "N", rel=0.005)

    r = cjeloviti_2_Y_racva()
    _check(out, "U11.CH2.v", r["v"], 11.99, "m/s", rel=0.02)
    _check(out, "U11.CH2.v_1", r["v_1"], 6.81, "m/s", rel=0.02)
    _check(out, "U11.CH2.Q_1_Ls", r["Q_1"] * 1000, 155.0, "L/s", rel=0.02)
    _check(out, "U11.CH2.p_M1_kPa", r["p_M1"] / 1000, 48.6, "kPa", rel=0.02)
    _check(out, "U11.CH2.R_x", r["R_x"], -665.0, "N", rel=0.05)
    _check(out, "U11.CH2.R_total", r["R_total"], 913.0, "N", rel=0.02)
    _check(out, "U11.CH2.reserve", 1000.0 - r["R_total"], 87.0, "N", abs_tol=1.0)

    r = primjer_mala_hidroelektrana()
    _check(out, "U11.P6.v", r["v"], 5.73, "m/s", rel=0.02)
    _check(out, "U11.P6.I", r["I"], 9827.0, "N", rel=0.002)
    _check(out, "U11.P6.F_x_kN", r["F_x"] / 1000, 4.91, "kN", rel=0.02)
    _check(out, "U11.P6.F_y_kN", r["F_y"] / 1000, 8.51, "kN", rel=0.02)
    _check(out, "U11.P6.F_R_kN", r["F_R"] / 1000, 9.83, "kN", rel=0.02)
    _check(out, "U11.P6.phi", r["phi"], 60.0, "deg", rel=0.01)

    r = primjer_7_rotirajuca_mlaznica()
    _check(out, "U11.P7.w", r["w"], 17.8, "m/s", rel=0.005)
    _check(out, "U11.P7.omega", r["omega"], 6.28, "1/s", rel=0.002)
    _check(out, "U11.P7.u", r["u"], 1.57, "m/s", rel=0.005)
    _check(out, "U11.P7.v_t", r["v_t"], 16.3, "m/s", rel=0.005)
    _check(out, "U11.P7.M", r["M"], 11.4, "N m", rel=0.005)
    _check(out, "U11.P7.P", r["P"], 71.0, "W", rel=0.01)
    _check(out, "U11.P7.M_0", r["M_0"], 12.5, "N m", rel=0.005)
    _check(out, "U11.P7.omega_max", r["omega_max"], 71.0, "1/s", rel=0.01)
    _check(out, "U11.P7.n_max", r["n_max_rpm"], 680.0, "1/min", rel=0.01)
    _check(out, "U11.P7.jet_power", r["jet_power"], 440.0, "W", rel=0.01)

    r = zadatak_1()
    _check(out, "U11.Z1.m_dot", r["m_dot"], 1845.0, "kg/s", abs_tol=0.5)
    _check(out, "U11.Z1.F_T_kN", r["F_T"] / 1000, 25.8, "kN", abs_tol=0.05)
    _check(out, "U11.Z1.P_T_kW", r["P_T"] / 1000, 465.0, "kW", abs_tol=0.5)
    _check(out, "U11.Z1.P_jet_kW", r["P_jet"] / 1000, 646.0, "kW", abs_tol=0.5)
    _check(out, "U11.Z1.eta", r["eta"], 0.72, "", abs_tol=0.0005)

    r = zadatak_2()
    _check(out, "U11.Z2.v_d", r["v_d"], 7.00, "m/s", abs_tol=1e-12)
    _check(out, "U11.Z2.m_dot", r["m_dot"], 9.02e4, "kg/s", abs_tol=50.0)
    _check(out, "U11.Z2.F_T_kN", r["F_T"] / 1000, 180.0, "kN", abs_tol=0.5)
    _check(out, "U11.Z2.dp_kPa", r["dp"] / 1000, 14.35, "kPa", abs_tol=0.005)
    _check(out, "U11.Z2.P_T_MW", r["P_T"] / 1e6, 1.08, "MW", abs_tol=0.005)
    _check(out, "U11.Z2.eta_i", r["eta_i"], 0.857, "", abs_tol=0.0005)

    r = zadatak_3()
    _check(out, "U11.Z3.v", r["v"], 2.865, "m/s", abs_tol=0.0005)
    _check(out, "U11.Z3.p_2_kPa", r["p_2"] / 1000, 144.9, "kPa", abs_tol=0.05)
    _check(out, "U11.Z3.W_N", r["W"], 294.0, "N", abs_tol=0.5)
    _check(out, "U11.Z3.F_x_kN", r["F_x"] / 1000, 4.97, "kN", abs_tol=0.005)
    _check(out, "U11.Z3.F_z_kN", r["F_z"] / 1000, -5.10, "kN", abs_tol=0.005)
    _check(out, "U11.Z3.F_R_kN", r["F_R"] / 1000, 7.12, "kN", abs_tol=0.005)
    _check(out, "U11.Z3.weight_share_percent", r["weight_share"] * 100, 5.8, "%", abs_tol=0.05)
    _check(out, "U11.Z3.F_z_horizontal_kN", r["F_z_horizontal_model"] / 1000, -4.97, "kN", abs_tol=0.005)

    r = zadatak_4()
    _check(out, "U11.Z4.F_x", r["F_x"], 287.4, "N", abs_tol=0.05)
    _check(out, "U11.Z4.F_y", r["F_y"], 0.0, "N", abs_tol=1e-12)
    _check(out, "U11.Z4.M_z", r["M_z"], -100.6, "N m", abs_tol=0.05)
    _check(out, "U11.Z4.R_x", r["R_x"], -287.4, "N", abs_tol=0.05)
    _check(out, "U11.Z4.M_Rz", r["M_Rz"], 100.6, "N m", abs_tol=0.05)

    r = zadatak_5()
    _check(out, "U11.Z5.mdot_rel", r["mdot_rel"], 15.05, "kg/s", abs_tol=0.005)
    _check(out, "U11.Z5.F_x", r["F_x"], 180.6, "N", abs_tol=0.05)
    _check(out, "U11.Z5.power_kW", r["power"] / 1000, 1.445, "kW", abs_tol=0.0005)
    _check(out, "U11.Z5.v_2", r["v_2"], 14.42, "m/s", abs_tol=0.005)
    _check(out, "U11.Z5.u_opt", r["u_opt"], 6.667, "m/s", abs_tol=0.0005)
    _check(out, "U11.Z5.power_max_kW", r["power_max"] / 1000, 1.486, "kW", abs_tol=0.0005)

    r = zadatak_6()
    _check(out, "U11.Z6.Q_2_Ls", r["Q_2"] * 1000, 24.0, "L/s")
    _check(out, "U11.Z6.Q_3_Ls", r["Q_3"] * 1000, 16.0, "L/s")
    _check(out, "U11.Z6.F_x", r["F_x"], 2835.8, "N", abs_tol=0.05)
    _check(out, "U11.Z6.F_y", r["F_y"], -44.0, "N", abs_tol=0.05)
    _check(out, "U11.Z6.F_R", r["F_R"], 2836.2, "N", abs_tol=0.05)
    _check(out, "U11.Z6.F_max", r["F_max"], 2918.3, "N", abs_tol=0.05)
    _check(out, "U11.Z6.required_rating", r["required_rating"], 3356.1, "N", abs_tol=0.05)
    _check(out, "U11.Z6.p_at_max_kPa", r["p_at_max"] / 1000, 190.0, "kPa", abs_tol=1e-10)
    _check(out, "U11.Z6.Q_at_max_Ls", r["Q_at_max"] * 1000, 39.2, "L/s", abs_tol=1e-10)
    _check(out, "U11.Z6.split_at_max", r["split_at_max"], 0.57, "", abs_tol=1e-12)

    # P1: energetska provjera, granice u=0 i u=v, optimumi jedne lopatice i kola.
    p1 = primjer_1_pelton()
    _invariant(out, "U11.P1.energy_balance", abs(p1["P"] - p1["energy_power"]) < 1e-9,
               "Snaga iz sile mora biti jednaka padu toka kineticke energije uz apsolutne brzine.")
    _invariant(out, "U11.P1.limits",
               primjer_1_pelton(u=0.0)["P"] == 0.0 and abs(primjer_1_pelton(u=30.0)["F"]) < 1e-12
               and primjer_1_pelton(u=0.0)["F"] > p1["F"],
               "Zadrzana lopatica ima najvecu silu bez snage; pri u=v voda ne doseze lopaticu.")
    wheel = lambda u: primjer_1_pelton(u=u)["P_wheel"]
    single = lambda u: primjer_1_pelton(u=u)["P"]
    _invariant(out, "U11.P1.optima",
               wheel(15.0) > wheel(14.9) and wheel(15.0) > wheel(15.1)
               and single(10.0) > single(9.9) and single(10.0) > single(10.1),
               "Kolo ima maksimum snage pri u=v/2, jedna lopatica pri u=v/3.")
    _invariant(out, "U11.P1.plate_vs_bucket",
               abs(primjer_1_pelton(theta_deg=90.0)["F"] / p1["F"] - 1 / (1 - math.cos(math.radians(165)))) < 1e-12,
               "Okomita ploca daje silu u omjeru 1:(1-cos theta) prema lopatici.")

    # P6: impulsna funkcija i neovisna vektorska bilanca daju iste komponente.
    p6 = primjer_mala_hidroelektrana()
    _invariant(out, "U11.P6.vector_balance",
               abs(p6["F_vec"][0] - p6["F_x"]) < 1e-9 and abs(p6["F_vec"][1] - p6["F_y"]) < 1e-9
               and abs(p6["F_R"] - 2 * p6["I"] * math.sin(math.radians(30))) < 1e-9,
               "Vektorska bilanca mora reproducirati I(1-cos theta) i I sin theta te |F|=2 I sin(theta/2).")
    _invariant(out, "U11.P6.straight_pipe",
               abs(primjer_mala_hidroelektrana(theta_deg=0.0)["F_R"]) < 1e-9,
               "Ravna cijev jednakih tlakova i promjera ne smije davati rezultantu.")

    # P7: moment nestaje pri omega_max, zadrzana glava ima najveci moment, snaga = M omega.
    p7 = primjer_7_rotirajuca_mlaznica()
    _invariant(out, "U11.P7.torque_limits",
               abs(primjer_7_rotirajuca_mlaznica(n_rpm=p7["n_max_rpm"])["M"]) < 1e-9
               and primjer_7_rotirajuca_mlaznica(n_rpm=0.0)["M"] == p7["M_0"]
               and primjer_7_rotirajuca_mlaznica(n_rpm=0.0)["P"] == 0.0,
               "Moment mora linearno padati do nule pri u=w, a zadrzana glava nema snagu.")
    _invariant(out, "U11.P7.power_consistency",
               abs(p7["P"] - p7["mdot"] * p7["u"] * p7["v_t"]) < 1e-9 and 0 < p7["P"] < p7["jet_power"],
               "Snaga M*omega mora biti jednaka mdot*u*(w-u) i manja od hidraulicke snage mlazova.")
    # Dva suprotna tangencijalna mlaza: sile se ponistavaju, momenti zbrajaju.
    half = p7["mdot"] / 2
    net_force = half * p7["v_t"] * (+1.0) + half * p7["v_t"] * (-1.0)
    net_moment = half * 0.25 * p7["v_t"] + half * 0.25 * p7["v_t"]
    _invariant(out, "U11.P7.force_cancellation",
               abs(net_force) < 1e-12 and abs(net_moment - p7["M"]) < 1e-9,
               "Dva suprotna mlaza ponistavaju sile, ali zbrajaju momente.")

    # Z1: potisak nestaje kad je v_j = v_s; korisnost je 2 v_s/(v_j+v_s).
    z1 = zadatak_1()
    _invariant(out, "U11.Z1.zero_thrust", zadatak_1(v_j=18.0)["F_T"] == 0.0,
               "Mlaz brzine jednake brzini broda ne daje potisak.")
    _invariant(out, "U11.Z1.froude_efficiency",
               abs(z1["eta"] - 2 * 18.0 / (32.0 + 18.0)) < 1e-12 and z1["P_T"] < z1["P_jet"],
               "Omjer korisne i predane snage mora biti 2 v_s/(v_j+v_s) i manji od 1.")

    # Z2: potisak iz skoka tlaka i iz kolicine gibanja; granica v_j -> v_A.
    z2 = zadatak_2()
    _invariant(out, "U11.Z2.pressure_jump_equals_momentum",
               abs(z2["F_T"] - z2["F_T_from_dp"]) < 1e-6,
               "Delta p * A_d mora biti jednak mdot (v_j - v_A).")
    _invariant(out, "U11.Z2.ideal_efficiency_limit",
               zadatak_2(v_j=6.0)["F_T"] == 0.0 and abs(zadatak_2(v_j=6.0)["eta_i"] - 1.0) < 1e-12
               and z2["eta_i"] < 1.0,
               "Bez prirasta brzine nema potiska, a korisnost tezi jedinici.")

    z4 = zadatak_4()
    _invariant(out, "U11.Z4.moment_equilibrium", abs(z4["M_z"]+z4["M_Rz"])<1e-12
               and abs(z4["F_x"]+z4["R_x"])<1e-12,"Uklještenje mora zatvoriti i silu i moment.")
    _invariant(out, "U11.Z4.perpendicular_arm", zadatak_4(e=0)["M_z"]==0
               and zadatak_4(b=0.8)["M_z"]==z4["M_z"],"Moment ovisi o e, ne o b.")
    for u in (0.0,4.0,8.0,12.0,19.0,20.0):
        z5 = zadatak_5(u=u)
        _invariant(out, f"U11.Z5.energy_u{u:g}",abs(z5["power"]-z5["energy_power"])<1e-9,
                   "Apsolutni tok kinetičke energije kroz pomični KV mora dati F*u.")
    z5 = zadatak_5()
    opt=z5["u_opt"]
    _invariant(out, "U11.Z5.maximum", zadatak_5(u=0)["power"]==0
               and zadatak_5(u=20)["power"]==0
               and zadatak_5(u=opt-0.01)["power"]<z5["power_max"]
               and zadatak_5(u=opt+0.01)["power"]<z5["power_max"]
               and abs((20-opt)*(20-3*opt))<1e-12,
               "Unutarnji maksimum i rubovi moraju odgovarati jednoj pomičnoj ploči.")
    _invariant(out, "U11.Z5.relative_mass_balance",
               abs(z5["mdot_rel"]+998*math.pi*.04**2/4*8-998*math.pi*.04**2/4*20)<1e-12,
               "Razlika protoka sapnice i dotoka ploči mora odgovarati produljenju slobodnog mlaza.")

    # A global sign proof over the complete independent parameter box.
    # Fx=p*A1+rho*Q²*f(s), Fy=rho*Q²*g(s). F² grows with p and decreases
    # with s (f'<0, g'>0, Fx>0, Fy<0). Bound its Q derivative from above.
    A1,A2,A3=(math.pi*d*d/4 for d in (.14,.09,.08))
    slo,shi=.57,.63
    f=lambda s: 1/A1-s*s/A2-.5*(1-s)**2/A3
    g=lambda s: -math.sin(math.pi/3)*(1-s)**2/A3
    fprime=lambda s: -2*s/A2+(1-s)/A3
    fx_min=180e3*A1+998*.0408**2*f(shi)
    fy_abs_max=998*.0408**2*abs(g(slo))
    q_derivative_upper=fx_min*f(slo)+fy_abs_max*abs(g(slo))
    _invariant(out,"U11.Z6.global_monotonicity",fx_min>0 and f(slo)<0
               and fprime(slo)<0 and fprime(shi)<0 and q_derivative_upper<0,
               "Maksimum nad cijelim intervalima zahtijeva dokazane predznake promjene rezultante.")
    _invariant(out,"U11.Z6.rating_selection",3000<r["required_rating"]<=3500,
               "Samo veća ponuđena nosivost zadovoljava zadani statički kriterij.")
    p3=primjer_3_koljeno()
    h_loss=(52e3-43e3)/(998*9.81)+(p3["v_1"]**2-p3["v_2"]**2)/(2*9.81)
    _check(out,"U11.P3.h_loss",h_loss,0.272,"m",abs_tol=0.0005)
    xi=h_loss*2*9.81/p3["v_2"]**2
    _check(out,"U11.P3.xi",xi,0.34,"",abs_tol=0.005)
    _invariant(out,"U11.P3.positive_loss",h_loss>0,"Zadani tlakovi P3 zahtijevaju pozitivan energijski gubitak.")
    z3=zadatak_3()
    no_weight=zadatak_3(V=0.0); flat=zadatak_3(dz=0.0, xi=0.0, V=0.0)
    _invariant(out,"U11.Z3.weight_and_elevation_terms",
               abs(z3["F_z"]-no_weight["F_z"]+z3["W"])<1e-9
               and abs(flat["F_z"]-z3["F_z_horizontal_model"])<1e-9
               and z3["p_2"]<150e3 and abs((150e3-z3["p_2"])-998*9.81*(0.40+z3["h_g"]))<1e-9,
               "Tezina vode mora uci u F_z, a vodoravni model mora odgovarati dz = 0, xi = 0, V = 0.")

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
