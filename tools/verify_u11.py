"""Numericka verifikacija U11: Kolicina gibanja i sile strujanja."""
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


def primjer_1_mlaz(m_dot=10.0, v=20.0):
    F = m_dot * v
    return {"F": F}


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


def primjer_3_koljeno(D_1=0.180, D_2=0.120, Q=0.045, p_M1=52e3, p_M2=18e3,
                       rho=998.0):
    A_1 = math.pi * D_1**2 / 4
    A_2 = math.pi * D_2**2 / 4
    v_1 = Q / A_1
    v_2 = Q / A_2
    m_dot = rho * Q
    F_st_x = m_dot * (0 - v_1) - p_M1 * A_1
    F_st_y = m_dot * v_2 - (-p_M2 * A_2)
    F_f_x = -F_st_x
    F_f_y = -F_st_y
    F_R = math.sqrt(F_f_x**2 + F_f_y**2)
    return {"v_1": v_1, "v_2": v_2, "F_f_x": F_f_x, "F_f_y": F_f_y, "F_R": F_R}


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
    # F_st_x: p_M1·A_1 + F_st_x = m_dot_2·v + m_dot_3·v·cos60 - m_dot_1·v_1
    F_st_x = m_dot_2 * v + m_dot_3 * v * cos60 - m_dot_1 * v_1 - p_M1 * A_1
    R_x = -F_st_x
    R_total = math.sqrt(R_x**2 + R_y**2)
    return {"v": v, "v_1": v_1, "Q_1": Q_1,
            "p_M1": p_M1, "R_x": R_x, "R_total": R_total}


def primjer_koljeno_rashladni(D=0.080, Q=0.018, p_1=250e3, p_2=230e3, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    R_x = p_1 * A + m_dot * v
    R_y = p_2 * A + m_dot * v
    F_R = math.sqrt(R_x**2 + R_y**2)
    return {"R_x": R_x, "R_y": R_y, "F_R": F_R}


def primjer_vatrogasni(d=0.050, v_2=28.0, p_1=600e3, D_1=0.100, rho=998.0):
    A_2 = math.pi * d**2 / 4
    Q = A_2 * v_2
    A_1 = math.pi * D_1**2 / 4
    v_1 = Q / A_1
    m_dot = rho * Q
    R_x = p_1 * A_1 - m_dot * (v_2 - v_1)
    return {"v_1": v_1, "Q": Q, "R_x": R_x}


def primjer_mala_hidroelektrana(D=0.200, Q=0.18, p=280e3,
                                 beta_deg=60.0, rho=998.0):
    """Javni primjer sile na simetrično koljeno tlačnoga voda."""

    A = math.pi * D**2 / 4
    v = Q / A
    F_int = rho * Q * v + p * A
    beta = math.radians(beta_deg)
    F_x = F_int * (1 - math.cos(beta))
    F_y = F_int * math.sin(beta)
    F_R = math.hypot(F_x, F_y)
    phi = math.degrees(math.atan2(F_y, F_x))
    return {
        "v": v,
        "F_int": F_int,
        "F_x": F_x,
        "F_y": F_y,
        "F_R": F_R,
        "phi": phi,
    }


def zadatak_1(d=0.038, v=22.0, rho=998.0):
    A = math.pi * d**2 / 4
    Q = A * v
    m_dot = rho * Q
    return {"m_dot": m_dot, "F": m_dot * v}


def zadatak_2(d=0.042, F=310.0, rho=998.0):
    A = math.pi * d**2 / 4
    v = math.sqrt(F / (rho * A))
    Q = A * v
    return {"v": v, "Q": Q}


def zadatak_3(D=0.100, Q=0.026, p_1=180e3, p_2=150e3, rho=998.0):
    A = math.pi * D**2 / 4
    v = Q / A
    m_dot = rho * Q
    F_x = p_1 * A + m_dot * v
    F_y = -(p_2 * A + m_dot * v)
    F_R = math.hypot(F_x, F_y)
    return {"v": v, "F_x": F_x, "F_y": F_y, "F_R": F_R}


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
        beta = math.radians(angle_deg)
        F_x = (
            p_value * A_1
            + rho * Q_value * v_1
            - rho * Q_2 * v_2
            - rho * Q_3 * v_3 * math.cos(beta)
        )
        F_y = -rho * Q_3 * v_3 * math.sin(beta)
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


# ------------ Faza 1.5 dodatak: Vodeni udar (CH T3) ----------------
def cjeloviti_3_vodeni_udar(D=0.150, Q=0.050, rho=870.0, c=1200.0, L=200.0,
                              dt_a=0.20, dt_b=1.0, dt_c=5.0):
    A = math.pi * D**2 / 4
    v_0 = Q / A
    T_ref = 2 * L / c
    dp_J = rho * c * v_0
    # (a) direktni udar
    dp_a = dp_J if dt_a < T_ref else dp_J * T_ref / dt_a
    # (b) indirektni
    dp_b = dp_J * T_ref / dt_b
    # (c) vrlo sporo
    dp_c = dp_J * T_ref / dt_c
    F_a = dp_a * A
    F_b = dp_b * A
    F_c = dp_c * A
    return {"v_0": v_0, "T_ref": T_ref, "dp_J": dp_J,
            "dp_a": dp_a, "dp_b": dp_b, "dp_c": dp_c,
            "F_a": F_a, "F_b": F_b, "F_c": F_c}


def verify():
    out = []

    r = primjer_1_mlaz()
    _check(out, "U11.P1.F", r["F"], 200.0, "N")

    r = primjer_2_mlaznica()
    _check(out, "U11.P2.v_2", r["v_2"], 5.82, "m/s", rel=0.02)
    _check(out, "U11.P2.Q_Ls", r["Q"] * 1000, 37.0, "L/s", rel=0.02)
    _check(out, "U11.P2.p_M1_kPa", r["p_M1"] / 1000, 16.4, "kPa", rel=0.02)
    _check(out, "U11.P2.R", r["R"], 445.0, "N", rel=0.03)

    r = primjer_3_koljeno()
    _check(out, "U11.P3.v_1", r["v_1"], 1.77, "m/s", rel=0.02)
    _check(out, "U11.P3.v_2", r["v_2"], 3.98, "m/s", rel=0.02)
    _check(out, "U11.P3.F_f_x", r["F_f_x"], 1402.0, "N", rel=0.02)
    _check(out, "U11.P3.F_f_y", r["F_f_y"], -383.0, "N", rel=0.05)
    _check(out, "U11.P3.F_R", r["F_R"], 1453.0, "N", rel=0.02)

    r = cjeloviti_1_T_racva()
    _check(out, "U11.CH1.v_1", r["v_1"], 4.49, "m/s", rel=0.02)
    _check(out, "U11.CH1.v", r["v"], 10.03, "m/s", rel=0.02)
    _check(out, "U11.CH1.Q_1", r["Q_1"], 0.114, "m^3/s", rel=0.02)
    _check(out, "U11.CH1.F_f_x", r["F_f_x"], 892.0, "N", rel=0.05)
    _check(out, "U11.CH1.F_R", r["F_R"], 1025.0, "N", rel=0.05)

    r = cjeloviti_2_Y_racva()
    _check(out, "U11.CH2.v", r["v"], 11.99, "m/s", rel=0.02)
    _check(out, "U11.CH2.v_1", r["v_1"], 6.81, "m/s", rel=0.02)
    _check(out, "U11.CH2.Q_1_Ls", r["Q_1"] * 1000, 155.0, "L/s", rel=0.02)
    _check(out, "U11.CH2.p_M1_kPa", r["p_M1"] / 1000, 48.6, "kPa", rel=0.02)
    _check(out, "U11.CH2.R_x", r["R_x"], 664.0, "N", rel=0.05)
    _check(out, "U11.CH2.R_total", r["R_total"], 912.0, "N", rel=0.02)

    r = primjer_mala_hidroelektrana()
    _check(out, "U11.P6.v", r["v"], 5.73, "m/s", rel=0.02)
    _check(out, "U11.P6.F_x_kN", r["F_x"] / 1000, 4.91, "kN", rel=0.02)
    _check(out, "U11.P6.F_y_kN", r["F_y"] / 1000, 8.51, "kN", rel=0.02)
    _check(out, "U11.P6.F_R_kN", r["F_R"] / 1000, 9.83, "kN", rel=0.02)
    _check(out, "U11.P6.phi", r["phi"], 60.0, "deg", rel=0.01)

    r = zadatak_1()
    _check(out, "U11.Z1.m_dot", r["m_dot"], 24.90, "kg/s", abs_tol=0.005)
    _check(out, "U11.Z1.F", r["F"], 547.8, "N", abs_tol=0.05)
    _check(out, "U11.Z1.R_x", -r["F"], -547.8, "N", abs_tol=0.05)

    r = zadatak_2()
    _check(out, "U11.Z2.v", r["v"], 14.97, "m/s", abs_tol=0.005)
    _check(out, "U11.Z2.Q_Ls", r["Q"] * 1000, 20.74, "L/s", abs_tol=0.005)

    r = zadatak_3()
    _check(out, "U11.Z3.v", r["v"], 3.310, "m/s", abs_tol=0.0005)
    _check(out, "U11.Z3.F_x_kN", r["F_x"] / 1000, 1.500, "kN", abs_tol=0.0005)
    _check(out, "U11.Z3.F_y_kN", r["F_y"] / 1000, -1.264, "kN", abs_tol=0.0005)
    _check(out, "U11.Z3.F_R_kN", r["F_R"] / 1000, 1.961, "kN", abs_tol=0.0005)

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
    h_loss=(52e3-18e3)/(998*9.81)+(p3["v_1"]**2-p3["v_2"]**2)/(2*9.81)
    _check(out,"U11.P3.h_loss",h_loss,2.825,"m",abs_tol=0.0005)
    _invariant(out,"U11.P3.positive_loss",h_loss>0,"Zadani tlakovi P3 zahtijevaju pozitivan energijski gubitak.")

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
