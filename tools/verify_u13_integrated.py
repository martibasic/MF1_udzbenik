"""Neovisna numerička provjera kanonskoga U13.

Obuhvaća šest javnih primjera (uključujući petlju gradske mreže) i šest zadataka iz integriranoga poglavlja
``source/u13_gubici_cjevovodi_crpke_i_mreze.md``. Golden vrijednosti su
objavljeni, zaokruženi rezultati, a dodatne invarijante provjeravaju bilance,
monotonost i granične odluke.
"""

from __future__ import annotations

import math


TOL = 0.01
G = 9.81


def _close(value: float, target: float, rel: float = TOL) -> bool:
    if target == 0:
        return abs(value) <= rel
    return abs(value - target) / abs(target) <= rel


def _check(out, rid, value, target, unit="", rel=TOL, *, abs_tol=None):
    ok = math.isfinite(value) and (
        abs(value-target) <= abs_tol if abs_tol is not None else _close(value, target, rel)
    )
    out.append(
        {
            "id": rid,
            "status": "OK" if ok else "FAIL",
            "details": "" if ok else f"{value:.6g} vs {target:.6g} {unit}".strip(),
            "verification": "golden",
        }
    )


def _invariant(out, rid, condition, details=""):
    out.append(
        {
            "id": rid,
            "status": "OK" if condition else "FAIL",
            "details": "" if condition else details,
            "verification": "invariant",
        }
    )


def section_losses(D, L, v, lam, sum_xi, rho=1000.0, g=G):
    velocity_head = v**2 / (2 * g)
    h_l = lam * L / D * velocity_head
    h_loc = sum_xi * velocity_head
    h_w = h_l + h_loc
    return {
        "velocity_head": velocity_head,
        "h_l": h_l,
        "h_loc": h_loc,
        "h_w": h_w,
        "dp": rho * g * h_w,
    }


def laminar_pipe(rho, nu, D, L, Q, g=G):
    A = math.pi * D**2 / 4
    v = Q / A
    Re = v * D / nu
    lam = 64 / Re
    h_l = lam * L / D * v**2 / (2 * g)
    mu = rho * nu
    dp_dw = rho * g * h_l
    dp_poiseuille = 128 * mu * L * Q / (math.pi * D**4)
    return {
        "A": A,
        "v": v,
        "Re": Re,
        "lam": lam,
        "h_l": h_l,
        "mu": mu,
        "dp": dp_dw,
        "dp_poiseuille": dp_poiseuille,
    }


def hardy_cross_loop(
    lam=0.022,
    pipes=(("AB", 0.150, 300.0), ("BC", 0.100, 250.0), ("CD", 0.125, 200.0), ("DA", 0.150, 350.0)),
    initial=(0.022, 0.010, -0.006, -0.018),
    inflow=0.040,
    demands=(0.012, 0.016, 0.012),
    iterations=2,
    g=G,
):
    """Jedna petlja A-B-C-D-A; protok pozitivan u obilaznom smjeru."""
    R = [8 * lam * L / (math.pi**2 * g * D**5) for _, D, L in pipes]
    Q = list(initial)
    history = []
    for _ in range(iterations):
        num = sum(r * q * abs(q) for r, q in zip(R, Q))
        den = 2 * sum(r * abs(q) for r, q in zip(R, Q))
        dQ = -num / den
        history.append({"residual": num, "slope": den, "dQ": dQ})
        Q = [q + dQ for q in Q]
    losses = [r * q * abs(q) for r, q in zip(R, Q)]
    residual = sum(losses)
    qB, qC, qD = demands
    nodes = {
        "A": Q[0] - Q[3] - inflow,
        "B": Q[0] - Q[1] - qB,
        "C": Q[1] - Q[2] - qC,
        "D": Q[2] - Q[3] - qD,
    }
    velocities = [4 * abs(q) / (math.pi * D**2) for q, (_, D, _) in zip(Q, pipes)]
    return {
        "R": R,
        "Q": Q,
        "losses": losses,
        "history": history,
        "loop_residual": residual,
        "nodes": nodes,
        "drop_AC_via_B": losses[0] + losses[1],
        "drop_AC_via_D": -(losses[2] + losses[3]),
        "velocities": velocities,
    }


def pump_speed_example(q2=17.24):
    q_op = math.sqrt((25 - 6) / (0.0175 + 0.0303))
    H_op = 25 - 0.0175 * q_op**2
    H_system_q2 = 6 + 0.0303 * q2**2
    speed_ratio = math.sqrt((H_system_q2 + 0.0175 * q2**2) / 25)
    return {
        "q_op": q_op,
        "H_op": H_op,
        "H_system_q2": H_system_q2,
        "speed_ratio": speed_ratio,
        "flow_ratio": q2 / q_op,
    }


def energy_ledger(
    Q=0.006,
    H=12.0,
    hours=7000.0,
    rho=1000.0,
    eta_p=0.78,
    eta_m=0.92,
    eta_f=0.97,
    H_clean=10.0,
    g=G,
):
    eta_total = eta_p * eta_m * eta_f
    P_h = rho * g * Q * H
    P_shaft = P_h / eta_p
    P_el = P_shaft / (eta_m * eta_f)
    E = P_el * hours / 1e6
    E_clean = E * H_clean / H
    return {
        "eta_total": eta_total,
        "P_h": P_h,
        "P_shaft": P_shaft,
        "P_el": P_el,
        "E_MWh": E,
        "E_clean_MWh": E_clean,
        "saving_MWh": E - E_clean,
    }


def suction_npsh(
    z_s=2.6,
    D=0.080,
    L=5.0,
    Q=0.014,
    lam=0.030,
    sum_xi=1.8,
    p_atm=101e3,
    p_v=2.34e3,
    rho=1000.0,
    g=G,
):
    A = math.pi * D**2 / 4
    v = Q / A
    velocity_head = v**2 / (2 * g)
    h_w = (lam * L / D + sum_xi) * velocity_head
    p_abs_head = p_atm / (rho * g) - z_s - velocity_head - h_w
    NPSH_a = p_abs_head + velocity_head - p_v / (rho * g)
    return {
        "v": v,
        "velocity_head": velocity_head,
        "h_w": h_w,
        "p_abs_head": p_abs_head,
        "p_abs": rho * g * p_abs_head,
        "NPSH_a": NPSH_a,
    }


def parallel_branches(R1=12000.0, R2=48000.0, Q=0.020):
    ratio = math.sqrt(R2 / R1)
    Q1 = ratio / (1 + ratio) * Q
    Q2 = Q - Q1
    return {"Q1": Q1, "Q2": Q2, "h1": R1 * Q1**2, "h2": R2 * Q2**2}


def balanced_branches(R1=12000.0, R2=48000.0, Q=0.020):
    flow = Q/2
    target_resistance = max(R1,R2)
    valve_resistance = abs(R2-R1)
    return {
        "valve_branch": 1 if R1<R2 else 2,
        "Rv": valve_resistance,
        "Q1": flow, "Q2": flow,
        "h_AB": target_resistance*flow**2,
        "h_valve": valve_resistance*flow**2,
        "h1": (R1+max(R2-R1,0))*flow**2,
        "h2": (R2+max(R1-R2,0))*flow**2,
    }


def colebrook_factor(Re, relative_roughness):
    """Neovisna bisekcija u x=1/sqrt(lambda), samo turbulentni model."""
    if Re <= 4000 or relative_roughness < 0:
        raise ValueError("Zadani Colebrookov model zahtijeva Re>4000 i eps/D>=0.")
    def residual(x):
        return x+2*math.log10(relative_roughness/3.7+2.51*x/Re)
    lo,hi=1.0,20.0
    if not residual(lo)<0<residual(hi):
        raise ValueError("Colebrookov korijen izvan zadanog intervala.")
    for _ in range(70):
        mid=(lo+hi)/2
        if residual(mid)<0:lo=mid
        else:hi=mid
    x=(lo+hi)/2
    return 1/x**2,residual(x)


def swamee_jain(Re, relative_roughness):
    return 0.25 / math.log10(relative_roughness / 3.7 + 5.74 / Re**0.9) ** 2


def pipe_area(D):
    return math.pi * D**2 / 4


def village_supply(Q=0.009, D=0.100, L=850.0, lam=0.022, sum_xi=8.0, z2=42.0, p_M=2.5e5, rho=1000.0, g=G):
    """Z1: energijska bilanca od površine jezera do točke 2 na ulazu u kuće."""
    v = Q / pipe_area(D)
    vh = v**2 / (2 * g)
    h_w = (lam * L / D + sum_xi) * vh
    p_head = p_M / (rho * g)
    H_p = z2 + p_head + vh + h_w
    return {"v": v, "vh": vh, "h_w": h_w, "p_head": p_head, "H_p": H_p,
            "P_h": rho * g * Q * H_p,
            "shares": {"z": z2 / H_p, "p": p_head / H_p, "v": vh / H_p, "w": h_w / H_p}}


def oil_transfer(nu, Q=0.25e-3, d=0.020, L=14.0, dz=5.0, rho=880.0, g=G):
    """Z2: laminarni vod ulja između dviju slobodnih površina."""
    v = Q / pipe_area(d)
    Re = v * d / nu
    if Re >= 2300:
        raise ValueError("Zadatak pretpostavlja laminarni režim.")
    lam = 64 / Re
    h_l = lam * L / d * v**2 / (2 * g)
    H_p = dz + h_l
    # Neovisno: Hagen-Poiseuille bez Darcyjeva zapisa.
    dp_hp = 128 * rho * nu * L * Q / (math.pi * d**4)
    return {"v": v, "Re": Re, "lam": lam, "h_l": h_l, "H_p": H_p,
            "dp_bar": rho * g * H_p / 1e5, "h_l_poiseuille": dp_hp / (rho * g)}


def reservoir_operating_point(
    dz=28.0, L=620.0, D=0.150, k_s=0.10e-3, sum_xi=9.0, H0=46.0, b=9000.0,
    nu=1.0e-6, rho=1000.0, eta_p=0.74, eta_m=0.93, V_day=1500.0, lam0=0.02, rel_stop=0.005,
):
    """Z4: ručna iteracija iz teksta (λ -> Q -> Re -> λ) i neovisna bisekcija po Q."""
    K = 8 / (math.pi**2 * G * D**4)

    def q_for(lam):
        return math.sqrt((H0 - dz) / (b + (lam * L / D + sum_xi) * K))

    history = []
    lam = lam0
    Q_prev = None
    for _ in range(20):
        Q = q_for(lam)
        Re = Q / pipe_area(D) * D / nu
        lam_next = swamee_jain(Re, k_s / D)
        change = None if Q_prev is None else abs(Q - Q_prev) / Q_prev
        history.append({"lam_in": lam, "Q": Q, "Re": Re, "lam_out": lam_next, "change": change})
        if change is not None and change < rel_stop:
            break
        Q_prev, lam = Q, lam_next

    def residual(Q):
        Re = Q / pipe_area(D) * D / nu
        lam = swamee_jain(Re, k_s / D)
        return (H0 - b * Q**2) - (dz + (lam * L / D + sum_xi) * K * Q**2)

    lo, hi = 0.001, math.sqrt(H0 / b)
    for _ in range(80):
        mid = (lo + hi) / 2
        if residual(mid) > 0:
            lo = mid
        else:
            hi = mid
    Q = (lo + hi) / 2
    Re = Q / pipe_area(D) * D / nu
    lam = swamee_jain(Re, k_s / D)
    H = H0 - b * Q**2
    P_h = rho * G * Q * H
    P_vr = P_h / eta_p
    P_el = P_vr / eta_m
    hours = V_day / Q / 3600
    return {"history": history, "Q": Q, "H": H, "Re": Re, "lam": lam,
            "lam_colebrook": colebrook_factor(Re, k_s / D)[0],
            "P_h": P_h, "P_vr": P_vr, "P_el": P_el, "hours": hours, "E_kWh": P_el * hours / 1000}


def pipeline_reconstruction(
    z_N=25.0, L=1800.0, p_M=3.0e5, H0=90.0, b=25000.0, Q0=0.020, D0=0.150, Q1=0.030,
    diameters=(0.150, 0.200, 0.250), k_s=0.05e-3, nu=1.0e-6, rho=1000.0, g=G,
):
    """Z5: dijagnoza starog voda iz današnjeg stanja i izbor promjera novog voda."""
    p_head = p_M / (rho * g)
    H0p = H0 - b * Q0**2
    v0 = Q0 / pipe_area(D0)
    vh0 = v0**2 / (2 * g)
    lam0 = (H0p - z_N - p_head - vh0) / (L / D0 * vh0)
    lam_new_same = swamee_jain(v0 * D0 / nu, k_s / D0)
    H1p = H0 - b * Q1**2
    v1 = Q1 / pipe_area(D0)
    vh1 = v1**2 / (2 * g)
    H_old_needed = z_N + p_head + vh1 + lam0 * L / D0 * vh1
    states = {}
    for D in diameters:
        v = Q1 / pipe_area(D)
        vh = v**2 / (2 * g)
        Re = v * D / nu
        lam = swamee_jain(Re, k_s / D)
        p = (H1p - z_N - vh - lam * L / D * vh) * rho * g
        states[D] = {"v": v, "Re": Re, "lam": lam, "p_bar": p / 1e5}
    ok = [D for D in diameters if states[D]["p_bar"] >= p_M / 1e5]
    return {"H0p": H0p, "v0": v0, "lam0": lam0, "lam_new_same": lam_new_same, "H1p": H1p,
            "H_old_needed": H_old_needed, "deficit": H_old_needed - H1p, "states": states,
            "selected": min(ok)}


def night_filling(
    Q_n=0.012, z_N=20.0, p_M=3.0e5, z_V=62.0, D=0.200, L_A=3000.0, lam_A=0.019,
    L_1=1200.0, lam_1=0.019, L_3=2000.0, lam_3=0.020, eta=0.65,
    price_day=0.20, price_night=0.12, hours_day=16.0, hours_night=8.0, rho=1000.0, g=G,
):
    """Z6: izravna opskrba prema noćnom punjenju vodospreme."""
    v = Q_n / pipe_area(D)
    vh = v**2 / (2 * g)
    H_A = z_N + p_M / (rho * g) + vh + lam_A * L_A / D * vh
    P_A = rho * g * Q_n * H_A / eta
    E_A = P_A * (hours_day + hours_night) / 1000
    C_A = P_A / 1000 * (hours_day * price_day + hours_night * price_night)
    Q_B = Q_n * (hours_day + hours_night) / hours_night
    v_B = Q_B / pipe_area(D)
    H_B = z_V + lam_1 * L_1 / D * v_B**2 / (2 * g)
    P_B = rho * g * Q_B * H_B / eta
    E_B = P_B * hours_night / 1000
    C_B = E_B * price_night
    # Granična noćna cijena: C_A(c) = C_B(c).
    c_star = P_A / 1000 * hours_day * price_day / (E_B - P_A / 1000 * hours_night)
    p_N = (z_V - z_N - vh - lam_3 * L_3 / D * vh) * rho * g
    V_min = Q_n * hours_day * 3600
    return {"H_A": H_A, "P_A": P_A, "E_A": E_A, "C_A": C_A, "Q_B": Q_B, "H_B": H_B,
            "P_B": P_B, "E_B": E_B, "C_B": C_B, "energy_rise": E_B / E_A - 1,
            "cost_saving": 1 - C_B / C_A, "saving_eur": C_A - C_B, "c_star": c_star,
            "p_N_bar": p_N / 1e5, "V_min": V_min,
            "night_net_volume": (Q_B - Q_n) * hours_night * 3600}


def verify():
    out = []

    # P1: turbulentni lambda iz Re i k_s/D (Swamee-Jain), provjera Colebrookom.
    Re_p1 = 2.4 * 0.12 / 1.0e-6
    lam_p1 = swamee_jain(Re_p1, 0.26e-3 / 0.12)
    lam_cb, _ = colebrook_factor(Re_p1, 0.26e-3 / 0.12)
    rhs_cb = (-2 * math.log10(0.26e-3 / 0.12 / 3.7 + 2.51 / (Re_p1 * math.sqrt(lam_p1)))) ** -2
    _check(out, "U13.CANON.P1.Re", Re_p1, 2.88e5, "", rel=0.005)
    _check(out, "U13.CANON.P1.lam_swamee_jain", lam_p1, 0.02467, "", rel=0.002)
    _check(out, "U13.CANON.P1.colebrook_rhs", rhs_cb, 0.02452, "", rel=0.002)
    _invariant(out, "U13.CANON.P1.explicit_within_1pct", abs(lam_p1 / lam_cb - 1) < 0.01,
               "Swamee-Jain mora biti unutar 1 % od Colebrooka, kako tvrdi tekst.")
    r = section_losses(0.12, 36.0, 2.4, lam_p1, 4.6)
    _check(out, "U13.CANON.P1.velocity_head", r["velocity_head"], 0.2936, "m", rel=0.002)
    _check(out, "U13.CANON.P1.h_l", r["h_l"], 2.173, "m", rel=0.002)
    _check(out, "U13.CANON.P1.h_loc", r["h_loc"], 1.351, "m", rel=0.002)
    _check(out, "U13.CANON.P1.h_w", r["h_w"], 3.524, "m", rel=0.002)
    _check(out, "U13.CANON.P1.dp_kPa", r["dp"] / 1000, 34.57, "kPa", rel=0.002)
    _check(out, "U13.CANON.P1.local_share", 4.6 / (lam_p1 * 36.0 / 0.12 + 4.6), r["h_loc"] / r["h_w"], "", rel=1e-12)

    r = laminar_pipe(1050.0, 5.0e-6, 0.004, 2.0, 8.0e-6)
    _check(out, "U13.CANON.P2.A", r["A"], 1.257e-5, "m2", rel=0.02)
    _check(out, "U13.CANON.P2.v", r["v"], 0.637, "m/s", rel=0.02)
    _check(out, "U13.CANON.P2.Re", r["Re"], 509.0, "", rel=0.02)
    _check(out, "U13.CANON.P2.lam", r["lam"], 0.1257, "", rel=0.02)
    _check(out, "U13.CANON.P2.h_l", r["h_l"], 1.298, "m", rel=0.02)
    _check(out, "U13.CANON.P2.dp_kPa", r["dp"] / 1000, 13.37, "kPa", rel=0.02)
    _check(out, "U13.CANON.P2.dp_poiseuille_kPa", r["dp_poiseuille"] / 1000, 13.37, "kPa", rel=0.02)
    _invariant(out, "U13.CANON.P2.model_agreement", _close(r["dp"], r["dp_poiseuille"], 1e-10), "Darcy i Poiseuille moraju se podudarati.")

    r = hardy_cross_loop()
    _check(out, "U13.CANON.P3.R_AB", r["R"][0], 7181.0, "s2/m5", rel=0.002)
    _check(out, "U13.CANON.P3.R_BC", r["R"][1], 45445.0, "s2/m5", rel=0.002)
    _check(out, "U13.CANON.P3.R_CD", r["R"][2], 11913.0, "s2/m5", rel=0.002)
    _check(out, "U13.CANON.P3.R_DA", r["R"][3], 8378.0, "s2/m5", rel=0.002)
    _check(out, "U13.CANON.P3.residual_1", r["history"][0]["residual"], 4.877, "m", rel=0.002)
    _check(out, "U13.CANON.P3.dQ_1_Ls", r["history"][0]["dQ"] * 1000, -2.92, "L/s", rel=0.01)
    _check(out, "U13.CANON.P3.dQ_2_Ls", r["history"][1]["dQ"] * 1000, -0.19, "L/s", rel=0.03)
    _check(out, "U13.CANON.P3.Q_AB_Ls", r["Q"][0] * 1000, 18.89, "L/s", rel=0.002)
    _check(out, "U13.CANON.P3.Q_BC_Ls", r["Q"][1] * 1000, 6.89, "L/s", rel=0.002)
    _check(out, "U13.CANON.P3.Q_CD_Ls", r["Q"][2] * 1000, -9.11, "L/s", rel=0.002)
    _check(out, "U13.CANON.P3.Q_DA_Ls", r["Q"][3] * 1000, -21.11, "L/s", rel=0.002)
    _check(out, "U13.CANON.P3.h_AB", r["losses"][0], 2.56, "m", rel=0.005)
    _check(out, "U13.CANON.P3.h_BC", r["losses"][1], 2.16, "m", rel=0.005)
    _check(out, "U13.CANON.P3.h_DC", -r["losses"][2], 0.99, "m", rel=0.005)
    _check(out, "U13.CANON.P3.h_AD", -r["losses"][3], 3.73, "m", rel=0.005)
    _check(out, "U13.CANON.P3.drop_AC", r["drop_AC_via_B"], 4.72, "m", rel=0.005)
    _invariant(out, "U13.CANON.P3.nodes_and_loop",
               all(abs(v) < 1e-12 for v in r["nodes"].values())
               and abs(r["loop_residual"]) < 0.002
               and abs(r["drop_AC_via_B"] - r["drop_AC_via_D"]) < 0.002,
               "Čvorovi moraju ostati zatvoreni, a petlja i oba puta A-C usklađeni nakon dvije iteracije.")
    converged = hardy_cross_loop(iterations=12)
    _invariant(out, "U13.CANON.P3.convergence_and_velocities",
               abs(converged["loop_residual"]) < 1e-9
               and all(abs(a - b) < 1e-5 for a, b in zip(converged["Q"], r["Q"]))
               and all(0.5 < v < 2.0 for v in r["velocities"]),
               "Dvije iteracije moraju biti unutar 0,01 L/s od konvergiranog rješenja, uz realne brzine.")

    r = pump_speed_example()
    _check(out, "U13.CANON.P4.q_op_Ls", r["q_op"], 19.94, "L/s", rel=0.02)
    _check(out, "U13.CANON.P4.H_op", r["H_op"], 18.04, "m", rel=0.02)
    _check(out, "U13.CANON.P4.H_system_q2", r["H_system_q2"], 15.01, "m", rel=0.02)
    _check(out, "U13.CANON.P4.speed_ratio", r["speed_ratio"], 0.899, "", rel=0.02)
    _invariant(out, "U13.CANON.P4.static_head_breaks_simple_ratio", not _close(r["speed_ratio"], r["flow_ratio"], 0.01), "Uz statičku visinu s ne smije biti q2/q1.")

    r = energy_ledger()
    _check(out, "U13.CANON.P5.P_h_kW", r["P_h"] / 1000, 0.706, "kW", rel=0.02)
    _check(out, "U13.CANON.P5.P_shaft_kW", r["P_shaft"] / 1000, 0.906, "kW", rel=0.02)
    _check(out, "U13.CANON.P5.P_el_kW", r["P_el"] / 1000, 1.015, "kW", rel=0.02)
    _check(out, "U13.CANON.P5.E_MWh", r["E_MWh"], 7.10, "MWh", rel=0.02)
    _check(out, "U13.CANON.P5.E_clean_MWh", r["E_clean_MWh"], 5.92, "MWh", rel=0.02)
    _check(out, "U13.CANON.P5.saving_MWh", r["saving_MWh"], 1.18, "MWh", rel=0.03)
    _check(out, "U13.CANON.P5.eta_total", r["eta_total"], 0.696, "", rel=0.02)
    _invariant(out, "U13.CANON.P5.power_order", r["P_h"] < r["P_shaft"] < r["P_el"], "Mora vrijediti Ph<Pvr<Pel.")

    r = suction_npsh()
    _check(out, "U13.CANON.P6.v", r["v"], 2.785, "m/s", rel=0.02)
    _check(out, "U13.CANON.P6.h_w", r["h_w"], 1.453, "m", rel=0.02)
    _check(out, "U13.CANON.P6.p_abs_head", r["p_abs_head"], 5.847, "m", rel=0.02)
    _check(out, "U13.CANON.P6.p_abs_kPa", r["p_abs"] / 1000, 57.36, "kPa", rel=0.02)
    _check(out, "U13.CANON.P6.NPSH_a", r["NPSH_a"], 6.00, "m", rel=0.02)

    r = village_supply()
    _check(out, "U13.CANON.Z1.v", r["v"], 1.146, "m/s", abs_tol=0.0005)
    _check(out, "U13.CANON.Z1.velocity_head", r["vh"], 0.067, "m", abs_tol=0.0005)
    _check(out, "U13.CANON.Z1.h_w", r["h_w"], 13.05, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z1.p_head", r["p_head"], 25.48, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z1.H_p", r["H_p"], 80.6, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z1.P_h_kW", r["P_h"] / 1000, 7.12, "kW", abs_tol=0.005)
    _check(out, "U13.CANON.Z1.share_z_pct", r["shares"]["z"] * 100, 52.0, "%", abs_tol=0.5)
    _check(out, "U13.CANON.Z1.share_p_pct", r["shares"]["p"] * 100, 32.0, "%", abs_tol=0.5)
    _check(out, "U13.CANON.Z1.share_w_pct", r["shares"]["w"] * 100, 16.0, "%", abs_tol=0.5)
    steeper = village_supply(lam=0.044)
    _invariant(out, "U13.CANON.Z1.balance_and_friction_sensitivity",
               abs(sum(r["shares"].values()) - 1) < 1e-12
               and r["shares"]["v"] < 0.001
               and abs(steeper["H_p"] - r["H_p"] - 0.022 * 850.0 / 0.100 * r["vh"]) < 1e-9,
               "Dijelovi H_p moraju dati cjelinu; dvostruki lambda povećava H_p točno za linijski gubitak.")

    warm, cold = oil_transfer(40e-6), oil_transfer(320e-6)
    _check(out, "U13.CANON.Z2.v", warm["v"], 0.796, "m/s", abs_tol=0.0005)
    _check(out, "U13.CANON.Z2.Re_warm", warm["Re"], 398.0, "", abs_tol=0.5)
    _check(out, "U13.CANON.Z2.lam_warm", warm["lam"], 0.161, "", abs_tol=0.0005)
    _check(out, "U13.CANON.Z2.h_l_warm", warm["h_l"], 3.63, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z2.H_p_warm", warm["H_p"], 8.63, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z2.dp_warm_bar", warm["dp_bar"], 0.745, "bar", abs_tol=0.0005)
    _check(out, "U13.CANON.Z2.Re_cold", cold["Re"], 49.7, "", abs_tol=0.05)
    _check(out, "U13.CANON.Z2.lam_cold", cold["lam"], 1.29, "", abs_tol=0.005)
    _check(out, "U13.CANON.Z2.h_l_cold", cold["h_l"], 29.1, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z2.H_p_cold", cold["H_p"], 34.1, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z2.dp_cold_bar", cold["dp_bar"], 2.94, "bar", abs_tol=0.005)
    _invariant(out, "U13.CANON.Z2.laminar_loss_scales_with_viscosity",
               abs(cold["h_l"] / warm["h_l"] - 8.0) < 1e-12
               and abs(warm["h_l"] - warm["h_l_poiseuille"]) < 1e-12
               and abs(cold["h_l"] - cold["h_l_poiseuille"]) < 1e-12,
               "U laminarnom toku gubitak raste s viskoznošću i podudara se s Hagen-Poiseuilleom.")


    free = parallel_branches()
    _check(out, "U13.CANON.Z3.free_Q1_Ls", free["Q1"] * 1000, 13.33, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.free_Q2_Ls", free["Q2"] * 1000, 6.67, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.free_h_AB", free["h1"], 2.13, "m", abs_tol=0.005)
    _invariant(out, "U13.CANON.Z3.free_equal_head", _close(free["h1"], free["h2"], 1e-10),
               "Bez ventila paralelne grane imaju jednak pad.")

    r = balanced_branches()
    _check(out, "U13.CANON.Z3.Q1_Ls", r["Q1"] * 1000, 10.00, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.Q2_Ls", r["Q2"] * 1000, 10.00, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.h_AB", r["h_AB"], 4.80, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.Rv", r["Rv"], 36000.0, "s2/m5", abs_tol=1e-8)
    _check(out, "U13.CANON.Z3.h_valve", r["h_valve"], 3.60, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z3.valve_branch", r["valve_branch"], 1, "", abs_tol=0)
    _invariant(out, "U13.CANON.Z3.equal_head", _close(r["h1"], r["h2"], 1e-10), "Paralelne grane moraju imati jednak pad.")
    _invariant(out, "U13.CANON.Z3.passive_balance_and_continuity",
               abs(r["Q1"]+r["Q2"]-0.020)<1e-14
               and r["Rv"]>=0 and r["h_valve"]>0
               and balanced_branches(R1=48000,R2=12000)["valve_branch"]==2,
               "Ventil mora dodavati nenegativni otpor grani manjeg otpora i zatvoriti cvor.")

    r = reservoir_operating_point()
    h = r["history"]
    _check(out, "U13.CANON.Z4.Q_step1_Ls", h[0]["Q"] * 1000, 27.41, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z4.Re_step1", h[0]["Re"], 2.33e5, "", abs_tol=500)
    _check(out, "U13.CANON.Z4.lam_step1", h[0]["lam_out"], 0.01954, "", abs_tol=0.000005)
    _check(out, "U13.CANON.Z4.Q_step2_Ls", h[1]["Q"] * 1000, 27.59, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z4.change_step2_pct", h[1]["change"] * 100, 0.65, "%", abs_tol=0.005)
    _check(out, "U13.CANON.Z4.Q_Ls", r["Q"] * 1000, 27.6, "L/s", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.H", r["H"], 39.1, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.Re", r["Re"], 2.34e5, "", abs_tol=500)
    _check(out, "U13.CANON.Z4.lambda", r["lam"], 0.0195, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z4.P_h_kW", r["P_h"] / 1000, 10.6, "kW", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.P_shaft_kW", r["P_vr"] / 1000, 14.3, "kW", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.P_el_kW", r["P_el"] / 1000, 15.4, "kW", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.hours", r["hours"], 15.1, "h", abs_tol=0.05)
    _check(out, "U13.CANON.Z4.E_kWh", r["E_kWh"], 233.0, "kWh", abs_tol=0.5)
    rougher = reservoir_operating_point(k_s=0.30e-3)
    _invariant(out, "U13.CANON.Z4.iteration_matches_bisection",
               len(h) == 3 and h[2]["change"] < 0.005
               and abs(h[-1]["Q"] / r["Q"] - 1) < 1e-4
               and abs(r["lam"] / r["lam_colebrook"] - 1) < 0.01
               and r["Re"] > 4000 and r["P_h"] < r["P_vr"] < r["P_el"],
               "Ručna iteracija mora se zaustaviti u trećem koraku na rješenju bisekcije; Swamee-Jain unutar 1 % od Colebrooka.")
    _invariant(out, "U13.CANON.Z4.roughness_moves_operating_point",
               rougher["Q"] < r["Q"] and rougher["lam"] > r["lam"] and rougher["H"] > r["H"],
               "Veća hrapavost mora smanjiti protok na zadanoj padajućoj krivulji crpke.")

    r = pipeline_reconstruction()
    st = r["states"]
    _check(out, "U13.CANON.Z5.H_p_today", r["H0p"], 80.0, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z5.v0", r["v0"], 1.13, "m/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z5.lambda_old", r["lam0"], 0.0311, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.lambda_new_same_D", r["lam_new_same"], 0.0183, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.H_p_Q1", r["H1p"], 67.5, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z5.H_old_needed", r["H_old_needed"], 110.5, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z5.deficit", r["deficit"], 43.0, "m", abs_tol=0.5)
    _check(out, "U13.CANON.Z5.lam_150", st[0.150]["lam"], 0.0176, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.p_150_bar", st[0.150]["p_bar"], 1.12, "bar", abs_tol=0.005)
    _check(out, "U13.CANON.Z5.lam_200", st[0.200]["lam"], 0.0176, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.p_200_bar", st[0.200]["p_bar"], 3.44, "bar", abs_tol=0.005)
    _check(out, "U13.CANON.Z5.p_250_bar", st[0.250]["p_bar"], 3.93, "bar", abs_tol=0.005)
    _check(out, "U13.CANON.Z5.selected_mm", r["selected"] * 1000, 200.0, "mm", abs_tol=0)
    _invariant(out, "U13.CANON.Z5.diagnosis_and_selection",
               r["lam0"] > 1.5 * r["lam_new_same"]
               and st[0.150]["p_bar"] < 3.0 <= st[0.200]["p_bar"] < st[0.250]["p_bar"]
               and all(s["Re"] > 5000 for s in st.values())
               and r["deficit"] > 0,
               "Stari vod mora pokazati ostarjelost; najmanji dopušteni promjer je prvi koji daje barem 3 bar.")

    r = night_filling()
    _check(out, "U13.CANON.Z6.H_p_direct", r["H_A"], 52.7, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.P_el_direct_kW", r["P_A"] / 1000, 9.55, "kW", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.E_direct_kWh", r["E_A"], 229.0, "kWh", abs_tol=0.5)
    _check(out, "U13.CANON.Z6.cost_direct_eur", r["C_A"], 39.7, "€", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.Q_night_Ls", r["Q_B"] * 1000, 36.0, "L/s", abs_tol=1e-9)
    _check(out, "U13.CANON.Z6.H_p_night", r["H_B"], 69.6, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.P_el_night_kW", r["P_B"] / 1000, 37.8, "kW", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.E_night_kWh", r["E_B"], 303.0, "kWh", abs_tol=0.5)
    _check(out, "U13.CANON.Z6.cost_night_eur", r["C_B"], 36.3, "€", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.energy_rise_pct", r["energy_rise"] * 100, 32.0, "%", abs_tol=0.5)
    _check(out, "U13.CANON.Z6.cost_saving_pct", r["cost_saving"] * 100, 8.5, "%", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.saving_eur", r["saving_eur"], 3.4, "€", abs_tol=0.05)
    _check(out, "U13.CANON.Z6.break_even_price", r["c_star"], 0.135, "€/kWh", abs_tol=0.0005)
    _check(out, "U13.CANON.Z6.p_N_gravity_bar", r["p_N_bar"], 3.97, "bar", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.V_min_m3", r["V_min"], 691.0, "m3", abs_tol=0.5)
    at_star = night_filling(price_night=r["c_star"])
    _invariant(out, "U13.CANON.Z6.break_even_and_volume_balance",
               abs(at_star["C_A"] - at_star["C_B"]) < 1e-9
               and abs(r["night_net_volume"] - r["V_min"]) < 1e-9
               and r["E_B"] > r["E_A"] and r["C_B"] < r["C_A"]
               and r["p_N_bar"] >= 3.0,
               "Pri graničnoj cijeni troškovi su jednaki; noćni višak mora pokriti dnevnu potrošnju; više energije uz manji trošak.")

    return out


if __name__ == "__main__":
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:48s} {result.get('details', '')}")
    print(f"Total: ok={sum(r['status'] == 'OK' for r in results)}, "
          f"fail={sum(r['status'] != 'OK' for r in results)}")
    raise SystemExit(1 if any(r['status'] != 'OK' for r in results) else 0)
