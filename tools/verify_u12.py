"""Numericka verifikacija U12: Pokretne lopatice i potisak."""
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
        "id": rid, "status": "OK" if ok else "FAIL",
        "details": "" if ok else f"{value:.4g} vs {target:.4g} {unit}".strip(),
    })


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
    A = math.pi * d**2 / 4
    m_dot = rho * A * v
    F = m_dot * v
    return {"F": F}


def zadatak_2(v=26.0, b=0.030, h=0.016, beta_deg=110.0, rho=998.0):
    A = b * h
    m_dot = rho * A * v
    beta = math.radians(beta_deg)
    v_2x = v * math.cos(beta)
    v_2y = v * math.sin(beta)
    F_x = m_dot * (v - v_2x)
    F_y = m_dot * (0 - v_2y)
    return {"F_x": F_x, "F_y": F_y}


def zadatak_3(v_1=32.0, u=12.0, m_dot=18.0, beta_deg=150.0):
    w_1 = v_1 - u
    beta = math.radians(beta_deg)
    c_2x = u + w_1 * math.cos(beta)
    F = m_dot * (v_1 - c_2x)
    P = F * u
    return {"F": F, "P": P}


def zadatak_4(R=0.42, m_dot=24.0, v_u1=28.0, v_u2=6.0):
    F_t = m_dot * (v_u1 - v_u2)
    M = F_t * R
    return {"F_t": F_t, "M": M}


def zadatak_5(d=0.030, v=42.0, n_sapnica=3, rho=998.0):
    A_1 = math.pi * d**2 / 4
    A = n_sapnica * A_1
    m_dot = rho * A * v
    F = m_dot * v
    P = 0.5 * m_dot * v**2
    return {"F": F, "P": P}


def zadatak_6(m=110.0, d=0.028, n_sapnica=4, v=36.0, rho=998.0,
              g=9.81, dd=0.0003, dv=1.5, reserve=0.10):
    A_1 = math.pi * d**2 / 4
    A = n_sapnica * A_1
    F_p = rho * A * v**2
    m_max = F_p / g
    G = m * g
    a = (F_p - G) / m
    d_min = d - dd
    v_min = v - dv
    A_min = n_sapnica * math.pi * d_min**2 / 4
    F_min = rho * A_min * v_min**2
    m_cert = F_min / ((1 + reserve) * g)
    return {
        "F_p": F_p,
        "m_max": m_max,
        "a": a,
        "F_min": F_min,
        "m_cert": m_cert,
    }


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
    _check(out, "U12.P2.ratio", r["ratio"], 0.637, "", rel=0.02)

    r = primjer_4_pokretna_ravna()
    _check(out, "U12.P3.m_rel", r["m_rel"], 18.82, "kg/s", rel=0.02)
    _check(out, "U12.P3.F", r["F"], 282.0, "N", rel=0.02)
    _check(out, "U12.P3.P", r["P"], 2541.0, "W", rel=0.02)

    r = cjeloviti_1_zakrivljena()
    _check(out, "U12.P4.m_rel", r["m_rel"], 25.4, "kg/s", rel=0.02)
    _check(out, "U12.P4.c_2x", r["c_2x"], -2.47, "m/s", rel=0.05)
    _check(out, "U12.P4.F_f_x", r["F_f_x"], 723.0, "N", rel=0.02)
    _check(out, "U12.P4.F", r["F"], 746.0, "N", rel=0.02)
    _check(out, "U12.P4.P", r["P"], 7233.0, "W", rel=0.02)

    r = cjeloviti_2_pelton()
    _check(out, "U12.P5.u", r["u"], 15.41, "m/s", rel=0.02)
    _check(out, "U12.P5.w_1", r["w_1"], 15.59, "m/s", rel=0.02)
    _check(out, "U12.P5.m_rel", r["m_rel"], 23.65, "kg/s", rel=0.02)
    _check(out, "U12.P5.F_f_x", r["F_f_x"], 680.4, "N", rel=0.02)
    _check(out, "U12.P5.M", r["M"], 313.0, "Nm", rel=0.02)
    _check(out, "U12.P5.P_kW", r["P"] / 1000, 10.49, "kW", rel=0.02)

    r = primjer_kvadrokopter()
    _check(out, "U12.P6.thrust", r["thrust"], 5.886, "N", rel=0.02)
    _check(out, "U12.P6.induced_velocity", r["induced_velocity"], 6.76, "m/s", rel=0.02)
    _check(out, "U12.P6.P_ideal", r["P_ideal"], 39.8, "W", rel=0.02)
    _check(out, "U12.P6.P_shaft", r["P_shaft"], 56.9, "W", rel=0.02)
    _check(out, "U12.P6.P_total", r["P_total"], 227.0, "W", rel=0.02)
    _check(out, "U12.P6.duration_min", r["duration_min"], 19.6, "min", rel=0.02)

    r = zadatak_1()
    _check(out, "U12.Z1.F", r["F"], 219.0, "N", rel=0.02)

    r = zadatak_2()
    _check(out, "U12.Z2.F_x", r["F_x"], 435.0, "N", rel=0.02)
    _check(out, "U12.Z2.F_y", r["F_y"], -304.0, "N", rel=0.02)
    _check(out, "U12.Z2.R", math.hypot(r["F_x"], r["F_y"]), 531.0, "N", rel=0.02)

    r = zadatak_3()
    _check(out, "U12.Z3.F", r["F"], 672.0, "N", rel=0.02)
    _check(out, "U12.Z3.P_kW", r["P"] / 1000, 8.06, "kW", rel=0.02)

    r = zadatak_4()
    _check(out, "U12.Z4.F_t", r["F_t"], 528.0, "N", rel=0.02)
    _check(out, "U12.Z4.M", r["M"], 222.0, "Nm", rel=0.02)

    r = zadatak_5()
    _check(out, "U12.Z5.F_kN", r["F"] / 1000, 3.73, "kN", rel=0.02)
    _check(out, "U12.Z5.P_kW", r["P"] / 1000, 78.4, "kW", rel=0.02)

    r = zadatak_6()
    _check(out, "U12.Z6.F_p_kN", r["F_p"] / 1000, 3.19, "kN", rel=0.02)
    _check(out, "U12.Z6.m_max", r["m_max"], 325.0, "kg", rel=0.02)
    _check(out, "U12.Z6.a", r["a"], 19.2, "m/s2", rel=0.02)
    _check(out, "U12.Z6.F_min_kN", r["F_min"] / 1000, 2.86, "kN", rel=0.02)
    _check(out, "U12.Z6.m_cert", r["m_cert"], 265.0, "kg", rel=0.02)

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
