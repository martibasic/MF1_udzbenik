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


def allowed_pressure_drop(dp=25000.0, D=0.10, L=50.0, lam=0.025, sum_xi=4.0, rho=998.0, g=G):
    h_w = dp / (rho * g)
    zeta = lam * L / D + sum_xi
    v = math.sqrt(2 * g * h_w / zeta)
    A = math.pi * D**2 / 4
    return {"h_w": h_w, "zeta": zeta, "v": v, "Q": v * A,
            "line_share": (lam * L / D) / zeta, "check_h": zeta * v**2 / (2 * g)}


def two_fluids_same_pipe(D=0.008, L=4.0, Q=3.0e-5, fluids=((1080.0, 6.0e-6), (998.0, 1.0e-6)), g=G):
    A = math.pi * D**2 / 4
    v = Q / A
    out = []
    for rho, nu in fluids:
        Re = v * D / nu
        if Re < 2300:
            lam, regime = 64 / Re, "laminar"
        elif Re > 4000:
            lam, regime = 0.3164 * Re**-0.25, "turbulent"
        else:
            raise ValueError("Prijelazno područje nije obuhvaćeno zadanim modelima.")
        h = lam * L / D * v**2 / (2 * g)
        out.append({"Re": Re, "lam": lam, "regime": regime, "dp": rho * g * h})
    return {"v": v, "fluids": out}


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


def pump_operating_point(
    D=0.100, L=150.0, epsilon=0.100e-3, sum_xi=6.0,
    nu=1.0e-6, rho=1000.0, static_head=8.0,
    pump_a=30.0, pump_b=30000.0, eta_p=0.76, eta_m=0.92,
):
    def state(Q):
        v=4*Q/(math.pi*D**2)
        Re=v*D/nu
        lam,residual=colebrook_factor(Re,epsilon/D)
        Hp=pump_a-pump_b*Q**2
        Hs=static_head+(lam*L/D+sum_xi)*v**2/(2*G)
        return {"Q":Q,"v":v,"Re":Re,"lam":lam,"H":Hp,"Hs":Hs,
                "energy_residual":Hp-Hs,"colebrook_residual":residual}
    lo,hi=0.005,0.030
    if not state(lo)["energy_residual"]>0>state(hi)["energy_residual"]:
        raise ValueError("Radna tocka nije obuhvacena zadanim intervalom.")
    for _ in range(70):
        mid=(lo+hi)/2
        if state(mid)["energy_residual"]>0:lo=mid
        else:hi=mid
    result=state((lo+hi)/2)
    P_h=rho*G*result["Q"]*result["H"]
    result.update(P_h=P_h, P_shaft=P_h/eta_p, P_el=P_h/(eta_p*eta_m))
    return result


def swamee_jain(Re, relative_roughness):
    return 0.25 / math.log10(relative_roughness / 3.7 + 5.74 / Re**0.9) ** 2


def diameter_selection(
    diameters=(0.080, 0.100, 0.125),
    L=150.0,
    Q=0.018,
    sum_xi=6.0,
    epsilon=0.15e-3,
    nu=1.0e-6,
    limit=15.0,
):
    states = {}
    for D in diameters:
        A = math.pi * D**2 / 4
        v = Q / A
        Re = v * D / nu
        lam = swamee_jain(Re, epsilon / D)
        states[D] = {"v": v, "Re": Re, "lam": lam,
                     "h_w": (lam * L / D + sum_xi) * v**2 / (2 * G)}
    acceptable = [D for D in diameters if states[D]["h_w"] <= limit]
    return {"states": states, "selected": min(acceptable)}


def ballast_regulation_task(
    rho=1025.0, eta=0.70, hours=1500.0,
    pump=(22.0, 0.010), system=(4.0, 0.015), throttled=(4.0, 0.026),
    p_atm=101.3e3, p_v=4.2e3, z_s=1.8, h_ws=1.4, npshr=(2.5, 0.004),
    ballast_depth=0.4,
):
    q = math.sqrt((pump[0] - throttled[0]) / (pump[1] + throttled[1]))
    H_throttled = pump[0] - pump[1] * q**2
    Q = q * 1e-3
    P_el_throttled = rho * G * Q * H_throttled / eta
    H_open = system[0] + system[1] * q**2
    speed_ratio = math.sqrt((H_open + pump[1] * q**2) / pump[0])
    P_el_vfd = rho * G * Q * H_open / eta
    head_atm = p_atm / (rho * G)
    head_v = p_v / (rho * G)
    NPSH_a = head_atm + z_s - h_ws - head_v
    NPSH_r = npshr[0] + npshr[1] * q**2
    return {
        "q": q,
        "H_throttled": H_throttled,
        "H_open": H_open,
        "speed_ratio": speed_ratio,
        "P_el_throttled": P_el_throttled,
        "P_el_vfd": P_el_vfd,
        "E_throttled_MWh": P_el_throttled * hours / 1e6,
        "E_vfd_MWh": P_el_vfd * hours / 1e6,
        "saving_MWh": (P_el_throttled - P_el_vfd) * hours / 1e6,
        "NPSH_a": NPSH_a,
        "NPSH_r": NPSH_r,
        "NPSH_difference": NPSH_a - NPSH_r,
        "NPSH_a_ballast": head_atm + ballast_depth - h_ws - head_v,
    }


def verify():
    out = []

    r = section_losses(0.12, 36.0, 2.4, 0.028, 4.6)
    _check(out, "U13.CANON.P1.velocity_head", r["velocity_head"], 0.294, "m", rel=0.02)
    _check(out, "U13.CANON.P1.h_l", r["h_l"], 2.47, "m", rel=0.02)
    _check(out, "U13.CANON.P1.h_loc", r["h_loc"], 1.35, "m", rel=0.02)
    _check(out, "U13.CANON.P1.h_w", r["h_w"], 3.82, "m", rel=0.02)
    _check(out, "U13.CANON.P1.dp_kPa", r["dp"] / 1000, 37.4, "kPa", rel=0.02)

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

    r = allowed_pressure_drop()
    _check(out, "U13.CANON.Z1.h_w", r["h_w"], 2.554, "m", abs_tol=0.0005)
    _check(out, "U13.CANON.Z1.zeta", r["zeta"], 16.5, "", abs_tol=1e-9)
    _check(out, "U13.CANON.Z1.v", r["v"], 1.743, "m/s", abs_tol=0.0005)
    _check(out, "U13.CANON.Z1.Q_max_Ls", r["Q"] * 1000, 13.69, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z1.line_share_pct", r["line_share"] * 100, 75.8, "%", abs_tol=0.05)
    _invariant(out, "U13.CANON.Z1.inverse_closes_forward",
               abs(r["check_h"] - r["h_w"]) < 1e-12
               and _close(section_losses(0.10, 50.0, r["v"], 0.025, 4.0, rho=998.0)["dp"], 25000.0, 1e-10),
               "Izlučena brzina mora vratiti dopušteni pad tlaka izravnim računom.")

    r = two_fluids_same_pipe()
    a, b = r["fluids"]
    _check(out, "U13.CANON.Z2.v", r["v"], 0.597, "m/s", abs_tol=0.0005)
    _check(out, "U13.CANON.Z2.Re_A", a["Re"], 796.0, "", abs_tol=0.5)
    _check(out, "U13.CANON.Z2.lam_A", a["lam"], 0.0804, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z2.dp_A_kPa", a["dp"] / 1000, 7.73, "kPa", abs_tol=0.005)
    _check(out, "U13.CANON.Z2.Re_B", b["Re"], 4775.0, "", abs_tol=0.5)
    _check(out, "U13.CANON.Z2.lam_B", b["lam"], 0.0381, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z2.dp_B_kPa", b["dp"] / 1000, 3.38, "kPa", abs_tol=0.005)
    double = two_fluids_same_pipe(Q=6.0e-5)
    _check(out, "U13.CANON.Z2.dp_A_double_kPa", double["fluids"][0]["dp"] / 1000, 15.5, "kPa", abs_tol=0.05)
    _check(out, "U13.CANON.Z2.dp_B_double_kPa", double["fluids"][1]["dp"] / 1000, 11.4, "kPa", abs_tol=0.05)
    _invariant(out, "U13.CANON.Z2.regimes_and_scaling",
               a["regime"] == "laminar" and b["regime"] == "turbulent"
               and abs(double["fluids"][0]["dp"] / a["dp"] - 2.0) < 1e-12
               and abs(double["fluids"][1]["dp"] / b["dp"] - 2**1.75) < 1e-12
               and double["fluids"][0]["Re"] < 2300,
               "Isti vod daje laminarni i turbulentni režim; skaliranja s Q moraju pratiti 64/Re i Blasiusa.")

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

    r = pump_operating_point()
    _check(out, "U13.CANON.Z4.Q_Ls", r["Q"] * 1000, 19.030, "L/s", abs_tol=0.0005)
    _check(out, "U13.CANON.Z4.H", r["H"], 19.136, "m", abs_tol=0.0005)
    _check(out, "U13.CANON.Z4.Re", r["Re"], 2.423e5, "", abs_tol=50)
    _check(out, "U13.CANON.Z4.lambda", r["lam"], 0.020812, "", abs_tol=0.0000005)
    _check(out, "U13.CANON.Z4.P_h_kW", r["P_h"] / 1000, 3.572, "kW", abs_tol=0.0005)
    _check(out, "U13.CANON.Z4.P_shaft_kW", r["P_shaft"] / 1000, 4.700, "kW", abs_tol=0.0005)
    _check(out, "U13.CANON.Z4.P_el_kW", r["P_el"] / 1000, 5.109, "kW", abs_tol=0.0005)
    _invariant(out, "U13.CANON.Z4.power_order", r["P_h"] < r["P_shaft"] < r["P_el"], "Mora vrijediti Ph<Pvr<Pel.")
    _invariant(out, "U13.CANON.Z4.coupled_residuals",
               r["Re"]>4000 and abs(r["energy_residual"])<1e-6
               and abs(r["colebrook_residual"])<1e-6,
               "Radna tocka mora zatvoriti obje implicitne jednadzbe u turbulentnom podrucju.")
    rougher=pump_operating_point(epsilon=0.200e-3)
    _invariant(out, "U13.CANON.Z4.roughness_moves_operating_point",
               rougher["Q"]<r["Q"] and rougher["lam"]>r["lam"] and rougher["H"]>r["H"],
               "Veca hrapavost mora smanjiti protok na zadanoj padajucoj crpkinoj krivulji.")

    r = diameter_selection()
    st = r["states"]
    _check(out, "U13.CANON.Z5.lam_080", st[0.080]["lam"], 0.0238, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.lam_100", st[0.100]["lam"], 0.0228, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.lam_125", st[0.125]["lam"], 0.0221, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.h_w_080", st[0.080]["h_w"], 33.1, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z5.h_w_100", st[0.100]["h_w"], 10.8, "m", abs_tol=0.05)
    _check(out, "U13.CANON.Z5.h_w_125", st[0.125]["h_w"], 3.56, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z5.selected_mm", r["selected"] * 1000, 100.0, "mm", abs_tol=0)
    aged = diameter_selection(epsilon=0.50e-3)
    _check(out, "U13.CANON.Z5.lam_100_aged", aged["states"][0.100]["lam"], 0.0309, "", abs_tol=0.00005)
    _check(out, "U13.CANON.Z5.h_w_100_aged", aged["states"][0.100]["h_w"], 14.0, "m", abs_tol=0.05)
    _invariant(out, "U13.CANON.Z5.regime_and_ageing",
               all(v["Re"] > 5000 for v in st.values())
               and st[0.080]["lam"] > st[0.100]["lam"] > st[0.125]["lam"]
               and aged["selected"] == 0.100 and aged["states"][0.100]["h_w"] < 15.0
               and all(aged["states"][D]["lam"] > st[D]["lam"] for D in st),
               "Svi kandidati turbulentni; lambda raste s hrapavošću, a odabrani promjer ostaje unutar granice.")

    r = ballast_regulation_task()
    _check(out, "U13.CANON.Z6.q_Ls", r["q"], 22.36, "L/s", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.H_throttled", r["H_throttled"], 17.00, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.E_throttled_MWh", r["E_throttled_MWh"], 8.19, "MWh/god", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.H_open", r["H_open"], 11.50, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.speed_ratio", r["speed_ratio"], 0.866, "", abs_tol=0.0005)
    _check(out, "U13.CANON.Z6.E_vfd_MWh", r["E_vfd_MWh"], 5.54, "MWh/god", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.saving_MWh", r["saving_MWh"], 2.65, "MWh", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.NPSH_a", r["NPSH_a"], 10.06, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.NPSH_r", r["NPSH_r"], 4.50, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.NPSH_difference", r["NPSH_difference"], 5.56, "m", abs_tol=0.005)
    _check(out, "U13.CANON.Z6.NPSH_a_ballast", r["NPSH_a_ballast"], 8.66, "m", abs_tol=0.005)
    _invariant(out, "U13.CANON.Z6.regulation_and_energy_balance",
               abs(22*r["speed_ratio"]**2-0.010*r["q"]**2-r["H_open"])<1e-12
               and 0<r["speed_ratio"]<1
               and abs(r["E_throttled_MWh"]-r["E_vfd_MWh"]-r["saving_MWh"])<1e-12
               and r["saving_MWh"]>0,
               "Nova brzina mora zatvoriti radnu tocku, a usteda razliku godisnjih energija.")
    _invariant(out, "U13.CANON.Z6.flooded_suction_absolute_reference",
               r["NPSH_a"] > r["NPSH_a_ballast"] > 0
               and abs(r["NPSH_a"] - (101.3e3/(1025*G) + 1.8 - 1.4 - 4.2e3/(1025*G))) < 1e-12
               and ballast_regulation_task(p_v=12.0e3)["NPSH_a"] < r["NPSH_a"]
               and ballast_regulation_task(rho=1000.0)["E_throttled_MWh"] < r["E_throttled_MWh"],
               "Napunjen usis povecava NPSHa; topliji fluid ga smanjuje, a morska voda povecava snagu.")

    return out


if __name__ == "__main__":
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:48s} {result.get('details', '')}")
    print(f"Total: ok={sum(r['status'] == 'OK' for r in results)}, "
          f"fail={sum(r['status'] != 'OK' for r in results)}")
    raise SystemExit(1 if any(r['status'] != 'OK' for r in results) else 0)
