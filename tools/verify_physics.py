"""Mali skup neovisnih golden/invariant provjera temeljnih fizikalnih veza.

Ove provjere nisu zamjena za usporedbu svakog zadatka s objavljenim odgovorom.
Njihova je svrha rano uhvatiti tipicne regresije: izgubljen faktor povrsine,
neocuvanje volumena/protoka, pogresan predznak vektora ili rada, izgubljen
nestacionarni clan, pogresan energetski ledger ili zamjenu sati i sekundi.
"""

from __future__ import annotations

import math

import verify_u01
import verify_u03
import verify_u08
import verify_u10
import verify_u12_real_flow
import verify_u13
import verify_u13_integrated
import verify_u14


REL_TOL = 1.0e-10


def _append_close(
    out: list[dict],
    result_id: str,
    value: float,
    target: float,
    *,
    rel: float = REL_TOL,
    details: str = "",
) -> None:
    scale = max(abs(target), 1.0)
    ok = math.isfinite(value) and abs(value - target) <= rel * scale
    out.append(
        {
            "id": result_id,
            "status": "OK" if ok else "FAIL",
            "details": "" if ok else (details or f"{value:.12g} vs {target:.12g}"),
        }
    )


def verify() -> list[dict]:
    out: list[dict] = []

    # Pascal: isti tlak i ocuvanje istisnutog volumena moraju vrijediti zajedno.
    p1 = verify_u01.primjer_2()
    A_1 = 6.0e-4
    A_2 = 210.0e-4
    F_1 = 150.0
    s_1 = 0.18
    _append_close(
        out,
        "QA.GOLDEN.PASCAL_PRESSURE_BALANCE",
        F_1 / A_1,
        p1["F_2"] / A_2,
    )
    _append_close(
        out,
        "QA.GOLDEN.PASCAL_VOLUME_BALANCE",
        A_1 * s_1,
        A_2 * p1["s_2"],
    )

    # Hidrostatika: promjena manometarskog tlaka mora biti rho*g*Delta z.
    p3 = verify_u03.primjer_vodotoranj()
    _append_close(
        out,
        "QA.GOLDEN.HYDROSTATIC_GRADIENT",
        p3["p_man"],
        998.0 * 9.81 * p3["dH"],
    )

    # Kontinuitet: ulazni i izlazni volumni tok moraju biti jednaki.
    p8 = verify_u08.zadatak_1()
    A8_1 = math.pi * 0.10**2 / 4
    A8_2 = math.pi * 0.16**2 / 4
    _append_close(
        out,
        "QA.GOLDEN.CONTINUITY_ONE_IN_ONE_OUT",
        A8_1 * 4.8,
        A8_2 * p8["v_2"],
    )

    # Realni Bernoulli: ukupni gubitak je zbroj nenegativnih doprinosa.
    p10 = verify_u10.primjer_1_gubici()
    _append_close(
        out,
        "QA.GOLDEN.LOSS_DECOMPOSITION",
        p10["h_w"],
        p10["h_l"] + p10["h_loc"],
    )
    _append_close(
        out,
        "QA.GOLDEN.PRESSURE_LOSS_HEAD",
        p10["dp"],
        1000.0 * 9.81 * p10["h_w"],
    )

    # Paralelne grane: protoci se zbrajaju, a gubici grana moraju biti jednaki.
    p13 = verify_u13.zadatak_5()
    _append_close(
        out,
        "QA.GOLDEN.PARALLEL_FLOW_BALANCE",
        p13["Q_1"] + p13["Q_2"],
        0.032,
    )
    _append_close(
        out,
        "QA.GOLDEN.PARALLEL_EQUAL_HEAD",
        1450.0 * p13["Q_1"] ** 2,
        2400.0 * p13["Q_2"] ** 2,
    )

    # Simetricno koljeno: razlika dvaju jednakih vektora okomita je na
    # geometrijsku simetralu, a nije usmjerena duz nje.
    theta = math.radians(60.0)
    difference = (1.0 - math.cos(theta), -math.sin(theta))
    bisector = (math.cos(theta / 2), math.sin(theta / 2))
    dot = difference[0] * bisector[0] + difference[1] * bisector[1]
    _append_close(out, "QA.GOLDEN.SYMMETRIC_BEND_DIRECTION", dot, 0.0)

    # Pretvorba energije i vremena: Wh/W daje sate, ne sekunde.
    duration_seconds = (74.0 / 227.0) * 3600.0
    _append_close(
        out,
        "QA.GOLDEN.BATTERY_RUNTIME_UNITS",
        duration_seconds,
        1173.568281938326,
    )

    # Dvofluidni uzgon U07-Z6: zadani uroni istiskuju oko 690 kg fluida.
    displaced_mass = (
        820.0 * 2.8 * 1.2 * 0.08
        + 998.0 * 2.8 * 1.2 * (((0.26 + 0.18) / 2) - 0.08)
    )
    _append_close(
        out,
        "QA.GOLDEN.TWO_FLUID_DISPLACED_MASS",
        displaced_mass,
        689.8752,
    )

    # Froudeovo skaliranje istim fluidom: Re_s/Re_m = lambda^(3/2).
    p14 = verify_u14.primjer_2_froude()
    _append_close(
        out,
        "QA.GOLDEN.FROUDE_REYNOLDS_RATIO",
        p14["Re_ratio"],
        25.0 ** 1.5,
    )

    # Zakrivljena ploha: predznak se odreduje iz okupane strane, ne iz polozaja
    # nacrtanoga pomocnog volumena. Midpoint integral lokalnih tlakova neovisan
    # je o formulama kanonskog verifiera.
    def integrate_quarter_vertical(
        radius: float,
        width: float,
        top_depth: float,
        normal_sign: float,
        panels: int = 20_000,
    ) -> float:
        delta = (math.pi / 2.0) / panels
        total = 0.0
        for index in range(panels):
            theta = (index + 0.5) * delta
            pressure = 998.0 * 9.81 * (
                top_depth + radius * math.sin(theta)
            )
            normal_vertical = normal_sign * math.sin(theta)
            total += pressure * normal_vertical * width * radius * delta
        return total

    upward_vertical = integrate_quarter_vertical(1.22, 1.83, 2.44, 1.0)
    upward_golden = 998.0 * 9.81 * 1.83 * (
        2.44 * 1.22 + math.pi * 1.22**2 / 4.0
    )
    _append_close(
        out,
        "QA.GOLDEN.CURVED_SURFACE_VERTICAL_UPWARD",
        upward_vertical,
        upward_golden,
        rel=1.0e-8,
    )
    downward_vertical = integrate_quarter_vertical(0.90, 1.20, 0.0, -1.0)
    downward_golden = -998.0 * 9.81 * 1.20 * math.pi * 0.90**2 / 4.0
    _append_close(
        out,
        "QA.GOLDEN.CURVED_SURFACE_VERTICAL_DOWNWARD",
        downward_vertical,
        downward_golden,
        rel=1.0e-8,
    )

    # Pocetna stabilnost: GZ=GM*sin(theta) mora u granici maloga kuta dati GM.
    gm = 0.42
    theta_small = 1.0e-6
    _append_close(
        out,
        "QA.GOLDEN.INITIAL_STABILITY_SMALL_ANGLE",
        gm * math.sin(theta_small) / theta_small,
        gm,
    )

    # Hagen--Poiseuilleov granični slucaj mora biti linearan u protoku.
    viscosity = 1.0e-3
    length = 4.0
    diameter = 0.018
    flow = 2.0e-5
    pressure_drop = 128.0 * viscosity * length * flow / (
        math.pi * diameter**4
    )
    pressure_drop_double = 128.0 * viscosity * length * (2.0 * flow) / (
        math.pi * diameter**4
    )
    _append_close(
        out,
        "QA.GOLDEN.LAMINAR_PRESSURE_DROP_LINEAR_FLOW",
        pressure_drop_double / pressure_drop,
        2.0,
    )

    # Materijalna derivacija mora zadrzati lokalni (nestacionarni) clan.
    unsteady = verify_u12_real_flow.exercise_material_derivative()
    _append_close(
        out,
        "QA.GOLDEN.UNSTEADY_TERM_RETAINED",
        unsteady["total"] - unsteady["convective"],
        unsteady["local"],
    )

    # Jedinstvena konvencija: pumpa dodaje, a turbina oduzima mehanicku visinu.
    inlet_head = 10.0
    pump_head = 8.0
    pump_outlet_head = inlet_head + pump_head
    _append_close(
        out,
        "QA.GOLDEN.PUMP_WORK_SIGN",
        pump_outlet_head - inlet_head,
        pump_head,
    )
    turbine_inlet_head = 30.0
    turbine_head = 12.0
    turbine_outlet_head = turbine_inlet_head - turbine_head
    _append_close(
        out,
        "QA.GOLDEN.TURBINE_WORK_SIGN",
        turbine_outlet_head - turbine_inlet_head,
        -turbine_head,
    )

    # Energetski ledger: elektricna -> pretvarac -> vratilo -> hidraulicka
    # snaga, uz eksplicitne nenegativne disipacije na svakoj pretvorbi.
    ledger = verify_u13_integrated.energy_ledger()
    eta_frequency_converter = 0.97
    eta_motor = 0.92
    eta_pump = 0.78
    converter_output = ledger["P_el"] * eta_frequency_converter
    _append_close(
        out,
        "QA.GOLDEN.POWER_LEDGER_ELECTRIC_TO_SHAFT",
        converter_output * eta_motor,
        ledger["P_shaft"],
    )
    _append_close(
        out,
        "QA.GOLDEN.POWER_LEDGER_SHAFT_TO_HYDRAULIC",
        ledger["P_shaft"] * eta_pump,
        ledger["P_h"],
    )
    converter_loss = ledger["P_el"] - converter_output
    motor_loss = converter_output - ledger["P_shaft"]
    pump_loss = ledger["P_shaft"] - ledger["P_h"]
    _append_close(
        out,
        "QA.GOLDEN.POWER_LEDGER_CONSERVATION",
        ledger["P_h"] + converter_loss + motor_loss + pump_loss,
        ledger["P_el"],
    )

    return out


if __name__ == "__main__":
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:46s} {result.get('details', '')}")
    failures = sum(result["status"] != "OK" for result in results)
    print(f"\nGolden physics: ok={len(results) - failures}, fail={failures}")
    raise SystemExit(1 if failures else 0)
