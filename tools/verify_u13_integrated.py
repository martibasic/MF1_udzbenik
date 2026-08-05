"""Neovisna numerička provjera kanonskoga U13.

Obuhvaća šest javnih primjera i šest zadataka iz integriranoga poglavlja
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


def _check(out, rid, value, target, unit="", rel=TOL):
    ok = _close(value, target, rel)
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


def series_parallel_network(
    H=12.0,
    D0=0.10,
    K0=8.52,
    D1=0.08,
    K1=12.80,
    D2=0.06,
    K2=15.23,
    D3=0.10,
    K3=5.52,
    g=G,
):
    A0 = math.pi * D0**2 / 4
    A1 = math.pi * D1**2 / 4
    A2 = math.pi * D2**2 / 4
    ratio_v2_v1 = math.sqrt(K1 / K2)
    Q_factor = A1 + A2 * ratio_v2_v1
    ratio_v0_v1 = Q_factor / A0
    coefficient = K0 * ratio_v0_v1**2 + K1 + K3 * ratio_v0_v1**2
    v1 = math.sqrt(2 * g * H / coefficient)
    v2 = ratio_v2_v1 * v1
    Q1 = A1 * v1
    Q2 = A2 * v2
    Q = Q1 + Q2
    v0 = Q / A0
    h0 = K0 * v0**2 / (2 * g)
    hp = K1 * v1**2 / (2 * g)
    h3 = K3 * v0**2 / (2 * g)
    return {
        "ratio_v2_v1": ratio_v2_v1,
        "ratio_v0_v1": ratio_v0_v1,
        "v1": v1,
        "v2": v2,
        "Q1": Q1,
        "Q2": Q2,
        "Q": Q,
        "h0": h0,
        "hp": hp,
        "h3": h3,
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


def pump_operating_point():
    Q = math.sqrt((30 - 8) / (30000 + 20000))
    H = 30 - 30000 * Q**2
    P_h = 1000 * G * Q * H
    P_shaft = P_h / 0.76
    P_el = P_shaft / 0.92
    return {"Q": Q, "H": H, "P_h": P_h, "P_shaft": P_shaft, "P_el": P_el}


def diameter_robustness(
    diameters=(0.080, 0.100, 0.125),
    L=150.0,
    Q=0.018,
    sum_xi=6.0,
    lam_bounds=(0.020, 0.028),
    limit=15.0,
):
    ranges = {}
    for D in diameters:
        A = math.pi * D**2 / 4
        v = Q / A
        ranges[D] = tuple(
            (lam * L / D + sum_xi) * v**2 / (2 * G) for lam in lam_bounds
        )
    acceptable = [D for D in diameters if max(ranges[D]) <= limit]
    return {"ranges": ranges, "selected": min(acceptable)}


def regulation_task():
    q = math.sqrt((24 - 5) / (0.012 + 0.040))
    H_throttled = 24 - 0.012 * q**2
    Q = q * 1e-3
    P_el_throttled = 1000 * G * Q * H_throttled / 0.72
    H_open = 5 + 0.025 * q**2
    speed_ratio = math.sqrt((H_open + 0.012 * q**2) / 24)
    P_el_vfd = 1000 * G * Q * H_open / 0.72
    saving_MWh = (P_el_throttled - P_el_vfd) * 5000 / 1e6
    NPSH_a = 10.2 - 2.0 - 1.2 - 0.35
    NPSH_r = 2 + 0.003 * q**2
    return {
        "q": q,
        "H_throttled": H_throttled,
        "P_el_throttled": P_el_throttled,
        "H_open": H_open,
        "speed_ratio": speed_ratio,
        "P_el_vfd": P_el_vfd,
        "saving_MWh": saving_MWh,
        "NPSH_a": NPSH_a,
        "NPSH_r": NPSH_r,
        "NPSH_difference": NPSH_a - NPSH_r,
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

    r = series_parallel_network()
    _check(out, "U13.CANON.P3.ratio_v2_v1", r["ratio_v2_v1"], 0.9168, "", rel=0.02)
    _check(out, "U13.CANON.P3.ratio_v0_v1", r["ratio_v0_v1"], 0.9700, "", rel=0.02)
    _check(out, "U13.CANON.P3.v1", r["v1"], 3.009, "m/s", rel=0.02)
    _check(out, "U13.CANON.P3.v2", r["v2"], 2.758, "m/s", rel=0.02)
    _check(out, "U13.CANON.P3.Q1_Ls", r["Q1"] * 1000, 15.12, "L/s", rel=0.02)
    _check(out, "U13.CANON.P3.Q2_Ls", r["Q2"] * 1000, 7.80, "L/s", rel=0.02)
    _check(out, "U13.CANON.P3.Q_Ls", r["Q"] * 1000, 22.92, "L/s", rel=0.02)
    _check(out, "U13.CANON.P3.h0", r["h0"], 3.70, "m", rel=0.02)
    _check(out, "U13.CANON.P3.hp", r["hp"], 5.91, "m", rel=0.02)
    _check(out, "U13.CANON.P3.h3", r["h3"], 2.40, "m", rel=0.02)
    _invariant(out, "U13.CANON.P3.energy_balance", _close(r["h0"] + r["hp"] + r["h3"], 12.0, 0.002), "Gubitci moraju zatvoriti 12 m.")

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

    Q = 0.012
    A = math.pi * 0.10**2 / 4
    r = section_losses(0.10, 50.0, Q / A, 0.025, 4.0, rho=998.0)
    _check(out, "U13.CANON.Z1.v", Q / A, 1.528, "m/s", rel=0.02)
    _check(out, "U13.CANON.Z1.h_l", r["h_l"], 1.487, "m", rel=0.02)
    _check(out, "U13.CANON.Z1.h_loc", r["h_loc"], 0.476, "m", rel=0.02)
    _check(out, "U13.CANON.Z1.h_w", r["h_w"], 1.963, "m", rel=0.02)
    _check(out, "U13.CANON.Z1.dp_kPa", r["dp"] / 1000, 19.2, "kPa", rel=0.02)

    r = laminar_pipe(1100.0, 3.0e-6, 0.006, 5.0, 6.0e-6)
    _check(out, "U13.CANON.Z2.v", r["v"], 0.212, "m/s", rel=0.02)
    _check(out, "U13.CANON.Z2.Re", r["Re"], 424.0, "", rel=0.02)
    _check(out, "U13.CANON.Z2.lam", r["lam"], 0.1508, "", rel=0.02)
    _check(out, "U13.CANON.Z2.dp_kPa", r["dp"] / 1000, 3.11, "kPa", rel=0.02)
    r_double = laminar_pipe(1100.0, 3.0e-6, 0.006, 5.0, 12.0e-6)
    _invariant(out, "U13.CANON.Z2.linear_Q_scaling", _close(r_double["dp"] / r["dp"], 2.0, 1e-10), "Laminarni dp mora se udvostručiti s Q.")

    r = parallel_branches()
    _check(out, "U13.CANON.Z3.Q1_Ls", r["Q1"] * 1000, 13.33, "L/s", rel=0.02)
    _check(out, "U13.CANON.Z3.Q2_Ls", r["Q2"] * 1000, 6.67, "L/s", rel=0.02)
    _check(out, "U13.CANON.Z3.h_AB", r["h1"], 2.13, "m", rel=0.02)
    _invariant(out, "U13.CANON.Z3.equal_head", _close(r["h1"], r["h2"], 1e-10), "Paralelne grane moraju imati jednak pad.")

    r = pump_operating_point()
    _check(out, "U13.CANON.Z4.Q_Ls", r["Q"] * 1000, 20.98, "L/s", rel=0.02)
    _check(out, "U13.CANON.Z4.H", r["H"], 16.8, "m", rel=0.02)
    _check(out, "U13.CANON.Z4.P_h_kW", r["P_h"] / 1000, 3.46, "kW", rel=0.02)
    _check(out, "U13.CANON.Z4.P_shaft_kW", r["P_shaft"] / 1000, 4.55, "kW", rel=0.02)
    _check(out, "U13.CANON.Z4.P_el_kW", r["P_el"] / 1000, 4.94, "kW", rel=0.02)
    _invariant(out, "U13.CANON.Z4.power_order", r["P_h"] < r["P_shaft"] < r["P_el"], "Mora vrijediti Ph<Pvr<Pel.")

    r = diameter_robustness()
    _check(out, "U13.CANON.Z5.D080_low", r["ranges"][0.080][0], 28.4, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.D080_high", r["ranges"][0.080][1], 38.2, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.D100_low", r["ranges"][0.100][0], 9.64, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.D100_high", r["ranges"][0.100][1], 12.85, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.D125_low", r["ranges"][0.125][0], 3.29, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.D125_high", r["ranges"][0.125][1], 4.34, "m", rel=0.03)
    _check(out, "U13.CANON.Z5.selected_mm", r["selected"] * 1000, 100.0, "mm")
    _invariant(out, "U13.CANON.Z5.robust_limit", max(r["ranges"][r["selected"]]) < 15.0, "Odabrani promjer mora zadovoljiti najgori slučaj.")

    r = regulation_task()
    _check(out, "U13.CANON.Z6.q_Ls", r["q"], 19.12, "L/s", rel=0.02)
    _check(out, "U13.CANON.Z6.H_throttled", r["H_throttled"], 19.62, "m", rel=0.02)
    _check(out, "U13.CANON.Z6.P_el_throttled_kW", r["P_el_throttled"] / 1000, 5.11, "kW", rel=0.02)
    _check(out, "U13.CANON.Z6.H_open", r["H_open"], 14.13, "m", rel=0.02)
    _check(out, "U13.CANON.Z6.speed_ratio", r["speed_ratio"], 0.878, "", rel=0.02)
    _check(out, "U13.CANON.Z6.P_el_vfd_kW", r["P_el_vfd"] / 1000, 3.68, "kW", rel=0.02)
    _check(out, "U13.CANON.Z6.saving_MWh", r["saving_MWh"], 7.14, "MWh", rel=0.02)
    _check(out, "U13.CANON.Z6.NPSH_a", r["NPSH_a"], 6.65, "m", rel=0.02)
    _check(out, "U13.CANON.Z6.NPSH_r", r["NPSH_r"], 3.10, "m", rel=0.02)
    _check(out, "U13.CANON.Z6.NPSH_difference", r["NPSH_difference"], 3.55, "m", rel=0.02)

    return out


if __name__ == "__main__":
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:48s} {result.get('details', '')}")
    print(f"Total: ok={sum(r['status'] == 'OK' for r in results)}, "
          f"fail={sum(r['status'] != 'OK' for r in results)}")
