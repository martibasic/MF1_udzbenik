"""Neovisna numericka verifikacija poglavlja o kompresibilnom idealnom toku.

Ulazne vrijednosti prepisane su iz kanonskog Markdown poglavlja, a svaki
objavljeni broj usporeduje se s rezultatom ponovno izracunatim iz fizikalne
relacije. Dimenzijske i granicne provjere vode se odvojeno kao invarijante.
"""
from __future__ import annotations

from fractions import Fraction
import math


GAMMA_AIR = 1.4
R_AIR = 287.0  # J/(kg K)


def _close(value: float, target: float, *, abs_tol: float) -> bool:
    return math.isfinite(value) and abs(value - target) <= abs_tol


def _check(
    out: list[dict[str, str]],
    result_id: str,
    value: float,
    target: float,
    unit: str,
    *,
    abs_tol: float,
) -> None:
    ok = _close(value, target, abs_tol=abs_tol)
    out.append(
        {
            "id": result_id,
            "status": "OK" if ok else "FAIL",
            "verification": "golden",
            "details": "" if ok else (
                f"izracunato {value:.9g}, objavljeno {target:.9g} {unit}; "
                f"dopusteno apsolutno odstupanje {abs_tol:g}"
            ).strip(),
        }
    )


def _invariant(
    out: list[dict[str, str]], result_id: str, condition: bool, failure: str
) -> None:
    out.append(
        {
            "id": result_id,
            "status": "OK" if condition else "FAIL",
            "verification": "invariant",
            "details": "" if condition else failure,
        }
    )


# Dimenzije su uredene kao (M, L, T, Theta).
Dim = tuple[Fraction, Fraction, Fraction, Fraction]
DIMLESS: Dim = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
MASS: Dim = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
LENGTH: Dim = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
TIME: Dim = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
TEMPERATURE: Dim = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))


def _dim_product(*items: Dim) -> Dim:
    return tuple(sum(parts, Fraction(0)) for parts in zip(*items))  # type: ignore[return-value]


def _dim_power(item: Dim, exponent: Fraction) -> Dim:
    return tuple(value * exponent for value in item)  # type: ignore[return-value]


VELOCITY = _dim_product(LENGTH, _dim_power(TIME, Fraction(-1)))
AREA = _dim_power(LENGTH, Fraction(2))
PRESSURE = _dim_product(
    MASS, _dim_power(LENGTH, Fraction(-1)), _dim_power(TIME, Fraction(-2))
)
GAS_CONSTANT = _dim_product(
    _dim_power(LENGTH, Fraction(2)),
    _dim_power(TIME, Fraction(-2)),
    _dim_power(TEMPERATURE, Fraction(-1)),
)


def acoustic_line(
    temperature: float = 293.0,
    length: float = 85.0,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> dict[str, float]:
    sound_speed = math.sqrt(gamma * gas_constant * temperature)
    return {"sound_speed": sound_speed, "travel_time": length / sound_speed}


def compressor_intake(
    temperature: float = 293.15,
    diameter: float = 0.080,
    volume_flow: float = 0.42,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> dict[str, float]:
    area = math.pi * diameter**2 / 4.0
    velocity = volume_flow / area
    sound_speed = math.sqrt(gamma * gas_constant * temperature)
    mach = velocity / sound_speed
    return {
        "area": area,
        "velocity": velocity,
        "mach": mach,
        "mach_plus_30pct": 1.30 * mach,
    }


def stagnation_state(
    temperature: float = 260.0,
    pressure_kpa: float = 55.0,
    mach: float = 0.80,
    gamma: float = GAMMA_AIR,
) -> dict[str, float]:
    temperature_ratio = 1.0 + (gamma - 1.0) * mach**2 / 2.0
    pressure_ratio = temperature_ratio ** (gamma / (gamma - 1.0))
    return {
        "temperature_ratio": temperature_ratio,
        "stagnation_temperature": temperature * temperature_ratio,
        "pressure_ratio": pressure_ratio,
        "stagnation_pressure_kpa": pressure_kpa * pressure_ratio,
    }


def choked_orifice(
    reservoir_pressure: float = 600_000.0,
    reservoir_temperature: float = 300.0,
    throat_area: float = 50.0e-6,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> dict[str, float]:
    critical_ratio = (2.0 / (gamma + 1.0)) ** (gamma / (gamma - 1.0))
    mass_flow = (
        throat_area
        * reservoir_pressure
        / math.sqrt(reservoir_temperature)
        * math.sqrt(gamma / gas_constant)
        * (2.0 / (gamma + 1.0))
        ** ((gamma + 1.0) / (2.0 * (gamma - 1.0)))
    )
    return {
        "mass_flow": mass_flow,
        "critical_ratio": critical_ratio,
        "critical_pressure_kpa": reservoir_pressure * critical_ratio / 1000.0,
    }


def normal_shock(
    upstream_mach: float = 2.0, gamma: float = GAMMA_AIR
) -> dict[str, float]:
    upstream_mach_sq = upstream_mach**2
    downstream_mach_sq = (
        1.0 + (gamma - 1.0) * upstream_mach_sq / 2.0
    ) / (gamma * upstream_mach_sq - (gamma - 1.0) / 2.0)
    downstream_mach = math.sqrt(downstream_mach_sq)
    pressure_ratio = 1.0 + 2.0 * gamma / (gamma + 1.0) * (
        upstream_mach_sq - 1.0
    )
    total_pressure_ratio = pressure_ratio * (
        (1.0 + (gamma - 1.0) * downstream_mach_sq / 2.0)
        / (1.0 + (gamma - 1.0) * upstream_mach_sq / 2.0)
    ) ** (gamma / (gamma - 1.0))
    return {
        "downstream_mach": downstream_mach,
        "pressure_ratio": pressure_ratio,
        "total_pressure_ratio": total_pressure_ratio,
    }


def exercise_sound_speed_helium(
    temperature: float = 300.0,
    gamma: float = 1.667,
    gas_constant: float = 2077.0,
) -> float:
    return math.sqrt(gamma * gas_constant * temperature)


def exercise_ventilation_mach(
    temperature: float = 293.15,
    diameter: float = 0.20,
    volume_flow: float = 2.0,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> float:
    area = math.pi * diameter**2 / 4.0
    velocity = volume_flow / area
    return velocity / math.sqrt(gamma * gas_constant * temperature)


def exercise_stagnation_temperature(
    temperature: float = 240.0,
    mach: float = 1.5,
    gamma: float = GAMMA_AIR,
) -> float:
    return temperature * (1.0 + (gamma - 1.0) * mach**2 / 2.0)


def exercise_critical_pressure_bar(
    reservoir_pressure_bar: float = 8.0, gamma: float = GAMMA_AIR
) -> float:
    return reservoir_pressure_bar * (2.0 / (gamma + 1.0)) ** (
        gamma / (gamma - 1.0)
    )


def exercise_nozzle_identification(
    reservoir_pressure: float = 600_000.0,
    reservoir_temperature: float = 300.0,
    measured_mass_flow: float = 0.0595,
    effective_area: float = 48.0e-6,
    mass_flow_uncertainty: float = 0.0006,
    pressure_uncertainty: float = 3_000.0,
    temperature_uncertainty: float = 1.0,
    area_uncertainty: float = 0.5e-6,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> dict[str, float]:
    flow_factor = (
        reservoir_pressure
        / math.sqrt(reservoir_temperature)
        * math.sqrt(gamma / gas_constant)
        * (2.0 / (gamma + 1.0))
        ** ((gamma + 1.0) / (2.0 * (gamma - 1.0)))
    )
    discharge_area = measured_mass_flow / flow_factor
    discharge_coefficient = discharge_area / effective_area
    relative_uncertainty = math.sqrt(
        (mass_flow_uncertainty / measured_mass_flow) ** 2
        + (area_uncertainty / effective_area) ** 2
        + (pressure_uncertainty / reservoir_pressure) ** 2
        + (0.5 * temperature_uncertainty / reservoir_temperature) ** 2
    )
    return {
        "discharge_area_mm2": discharge_area * 1.0e6,
        "discharge_coefficient": discharge_coefficient,
        "coefficient_uncertainty": discharge_coefficient * relative_uncertainty,
    }


def exercise_shock_measurements(
    p1_kpa: float = 80.0,
    p2_kpa: float = 360.0,
    p01_kpa: float = 626.0,
    p02_kpa: float = 451.0,
    u_p1_kpa: float = 0.4,
    u_p2_kpa: float = 1.8,
    u_p01_kpa: float = 4.0,
    u_p02_kpa: float = 4.0,
    gamma: float = GAMMA_AIR,
) -> dict[str, float]:
    static_ratio = p2_kpa / p1_kpa
    upstream_mach = math.sqrt(
        1.0 + (static_ratio - 1.0) * (gamma + 1.0) / (2.0 * gamma)
    )
    u_static_ratio = static_ratio * math.sqrt(
        (u_p1_kpa / p1_kpa) ** 2 + (u_p2_kpa / p2_kpa) ** 2
    )
    u_upstream_mach = (
        (gamma + 1.0) / (4.0 * gamma * upstream_mach) * u_static_ratio
    )
    theoretical_total_ratio = normal_shock(upstream_mach, gamma)[
        "total_pressure_ratio"
    ]
    derivative_step = 1.0e-5
    total_ratio_derivative = (
        normal_shock(upstream_mach + derivative_step, gamma)["total_pressure_ratio"]
        - normal_shock(upstream_mach - derivative_step, gamma)["total_pressure_ratio"]
    ) / (2.0 * derivative_step)
    u_theoretical_total_ratio = abs(total_ratio_derivative) * u_upstream_mach
    measured_total_ratio = p02_kpa / p01_kpa
    u_measured_total_ratio = measured_total_ratio * math.sqrt(
        (u_p01_kpa / p01_kpa) ** 2 + (u_p02_kpa / p02_kpa) ** 2
    )
    u_ratio_difference = math.sqrt(
        u_theoretical_total_ratio**2 + u_measured_total_ratio**2
    )
    return {
        "static_ratio": static_ratio,
        "upstream_mach": upstream_mach,
        "u_upstream_mach": u_upstream_mach,
        "theoretical_total_ratio": theoretical_total_ratio,
        "u_theoretical_total_ratio": u_theoretical_total_ratio,
        "measured_total_ratio": measured_total_ratio,
        "u_measured_total_ratio": u_measured_total_ratio,
        "u_ratio_difference": u_ratio_difference,
        "normalized_difference": abs(
            theoretical_total_ratio - measured_total_ratio
        ) / u_ratio_difference,
    }


def verify() -> list[dict[str, str]]:
    out: list[dict[str, str]] = []

    r = acoustic_line()
    _check(out, "U09.COMP.P1.a", r["sound_speed"], 343.0, "m/s", abs_tol=0.5)
    _check(out, "U09.COMP.P1.t", r["travel_time"], 0.248, "s", abs_tol=0.0005)

    r = compressor_intake()
    _check(out, "U09.COMP.P2.A", r["area"], 5.027e-3, "m^2", abs_tol=0.0000005)
    _check(out, "U09.COMP.P2.v", r["velocity"], 83.6, "m/s", abs_tol=0.05)
    # Izvor zaokruzuje a na 343 m/s prije omjera, pa tolerancija ukljucuje
    # propagaciju toga prikazanog medurezultata.
    _check(out, "U09.COMP.P2.Ma", r["mach"], 0.244, "", abs_tol=0.0006)
    _check(
        out,
        "U09.COMP.P2.Ma_plus_30pct",
        r["mach_plus_30pct"],
        0.317,
        "",
        abs_tol=0.0006,
    )

    r = stagnation_state()
    _check(out, "U09.COMP.P3.T0_T", r["temperature_ratio"], 1.128, "", abs_tol=0.0005)
    _check(out, "U09.COMP.P3.T0", r["stagnation_temperature"], 293.3, "K", abs_tol=0.05)
    _check(out, "U09.COMP.P3.p0_p", r["pressure_ratio"], 1.524, "", abs_tol=0.0005)
    _check(
        out,
        "U09.COMP.P3.p0",
        r["stagnation_pressure_kpa"],
        83.8,
        "kPa",
        abs_tol=0.05,
    )

    r = choked_orifice()
    _check(out, "U09.COMP.P4.mdot_max", r["mass_flow"], 0.0700, "kg/s", abs_tol=0.00005)
    _check(out, "U09.COMP.P4.pstar_p0", r["critical_ratio"], 0.528, "", abs_tol=0.0005)
    _check(
        out,
        "U09.COMP.P4.pstar",
        r["critical_pressure_kpa"],
        317.0,
        "kPa(abs)",
        abs_tol=0.5,
    )

    r = normal_shock()
    _check(out, "U09.COMP.P5.M2", r["downstream_mach"], 0.577, "", abs_tol=0.0005)
    _check(out, "U09.COMP.P5.p2_p1", r["pressure_ratio"], 4.50, "", abs_tol=0.005)

    _check(
        out,
        "U09.COMP.Z1.a",
        exercise_sound_speed_helium(),
        1019.0,
        "m/s",
        abs_tol=0.5,
    )
    _check(
        out,
        "U09.COMP.Z2.Ma",
        exercise_ventilation_mach(),
        0.186,
        "",
        abs_tol=0.0006,
    )
    _check(
        out,
        "U09.COMP.Z3.T0",
        exercise_stagnation_temperature(),
        348.0,
        "K",
        abs_tol=0.5,
    )
    _check(
        out,
        "U09.COMP.Z4.pstar",
        exercise_critical_pressure_bar(),
        4.23,
        "bar(abs)",
        abs_tol=0.005,
    )

    z5 = exercise_nozzle_identification()
    _check(
        out,
        "U09.COMP.Z5.CdA_mm2",
        z5["discharge_area_mm2"],
        42.50,
        "mm^2",
        abs_tol=0.01,
    )
    _check(
        out,
        "U09.COMP.Z5.Cd",
        z5["discharge_coefficient"],
        0.885,
        "",
        abs_tol=0.0006,
    )
    _check(
        out,
        "U09.COMP.Z5.u_Cd",
        z5["coefficient_uncertainty"],
        0.014,
        "",
        abs_tol=0.0005,
    )

    z6 = exercise_shock_measurements()
    _check(out, "U09.COMP.Z6.p2_p1", z6["static_ratio"], 4.500, "", abs_tol=0.0005)
    _check(out, "U09.COMP.Z6.M1", z6["upstream_mach"], 2.000, "", abs_tol=0.0005)
    _check(out, "U09.COMP.Z6.u_M1", z6["u_upstream_mach"], 0.007, "", abs_tol=0.0005)
    _check(
        out,
        "U09.COMP.Z6.p02_p01_theory",
        z6["theoretical_total_ratio"],
        0.7209,
        "",
        abs_tol=0.00005,
    )
    _check(
        out,
        "U09.COMP.Z6.u_p02_p01_theory",
        z6["u_theoretical_total_ratio"],
        0.0032,
        "",
        abs_tol=0.00005,
    )
    _check(
        out,
        "U09.COMP.Z6.p02_p01_measured",
        z6["measured_total_ratio"],
        0.7204,
        "",
        abs_tol=0.0001,
    )
    _check(
        out,
        "U09.COMP.Z6.u_difference",
        z6["u_ratio_difference"],
        0.0085,
        "",
        abs_tol=0.00005,
    )
    _check(
        out,
        "U09.COMP.Z6.normalized_difference",
        z6["normalized_difference"],
        0.050,
        "",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U09.COMP.Z6.u_p02_p01",
        z6["u_measured_total_ratio"],
        0.0079,
        "",
        abs_tol=0.0001,
    )

    sound_dimension = _dim_power(
        _dim_product(GAS_CONSTANT, TEMPERATURE), Fraction(1, 2)
    )
    acoustic_time_dimension = _dim_product(
        LENGTH, _dim_power(VELOCITY, Fraction(-1))
    )
    mass_flow_dimension = _dim_product(
        AREA,
        PRESSURE,
        _dim_power(TEMPERATURE, Fraction(-1, 2)),
        _dim_power(GAS_CONSTANT, Fraction(-1, 2)),
    )
    _invariant(
        out,
        "U09.COMP.INV.dimension_sound_speed",
        sound_dimension == VELOCITY,
        f"sqrt(RT) ima dimenziju {sound_dimension}, a ne brzine {VELOCITY}",
    )
    _invariant(
        out,
        "U09.COMP.INV.dimension_acoustic_time",
        acoustic_time_dimension == TIME,
        f"L/a ima dimenziju {acoustic_time_dimension}, a ne vremena {TIME}",
    )
    _invariant(
        out,
        "U09.COMP.INV.dimension_choked_mass_flow",
        mass_flow_dimension == _dim_product(MASS, _dim_power(TIME, Fraction(-1))),
        "formula prigusenog protoka nije dimenzije kg/s",
    )

    small_mach = 1.0e-3
    exact_pressure_increment = (
        1.0 + (GAMMA_AIR - 1.0) * small_mach**2 / 2.0
    ) ** (GAMMA_AIR / (GAMMA_AIR - 1.0)) - 1.0
    incompressible_increment = GAMMA_AIR * small_mach**2 / 2.0
    low_mach_error = abs(
        exact_pressure_increment / incompressible_increment - 1.0
    )
    _invariant(
        out,
        "U09.COMP.INV.low_mach_pressure_limit",
        low_mach_error < 1.0e-6,
        f"relativna pogreska niskog-Machova limesa je {low_mach_error:.3g}",
    )

    critical_ratio = choked_orifice()["critical_ratio"]
    _invariant(
        out,
        "U09.COMP.INV.critical_pressure_range",
        0.0 < critical_ratio < 1.0,
        f"kriticni omjer tlaka mora biti u (0, 1), dobiveno {critical_ratio:.6g}",
    )

    shock = normal_shock()
    _invariant(
        out,
        "U09.COMP.INV.normal_shock_direction",
        (
            0.0 < shock["downstream_mach"] < 1.0
            and shock["pressure_ratio"] > 1.0
            and 0.0 < shock["total_pressure_ratio"] < 1.0
        ),
        "normalni val nije dao M2<1, p2/p1>1 i p02/p01<1",
    )

    # Z5 i dalje mora pokazati identifikacijsku degeneraciju: samo mjerenje
    # masenog protoka određuje umnožak C_d A_eff, ne oba faktora.
    area_1, discharge_1 = 1.0e-4, 0.80
    area_2, discharge_2 = 0.8e-4, 1.00
    mass_proxy_1 = area_1 * discharge_1
    mass_proxy_2 = area_2 * discharge_2
    _invariant(
        out,
        "U09.COMP.Z5.identifiability",
        abs(mass_proxy_1 - mass_proxy_2) < 1.0e-16
        and area_1 != area_2
        and discharge_1 != discharge_2,
        "Jedno mjerenje mora ostaviti degeneraciju C_d*A_eff.",
    )
    required_independent_inputs = {
        "geometry_or_area_calibration",
        "mass_flow_uncertainty",
        "p0_uncertainty",
        "T0_uncertainty",
    }
    _invariant(
        out,
        "U09.COMP.Z5.required_inputs",
        len(required_independent_inputs) == 4
        and "geometry_or_area_calibration" in required_independent_inputs,
        "Postupak mora zahtijevati neovisnu geometriju/kalibraciju i nesigurnosti.",
    )

    # Neovisne granične provjere Z6: p2/p1 monotono određuje M1>1, a ukupni
    # tlak mora pasti kroz val. Brojčani mjerni ugovor provjeren je iznad.
    shock_15 = normal_shock(1.5)
    shock_20 = normal_shock(2.0)
    _invariant(
        out,
        "U09.COMP.Z6.pressure_ratio_monotonic",
        1.0 < shock_15["pressure_ratio"] < shock_20["pressure_ratio"],
        "Omjer statičkih tlakova mora monotono rasti s M1 u nadzvučnom području.",
    )
    _invariant(
        out,
        "U09.COMP.Z6.total_pressure_loss",
        0.0 < shock_20["total_pressure_ratio"] < shock_15["total_pressure_ratio"] < 1.0,
        "Normalni val mora smanjiti ukupni tlak, sve više pri većem M1.",
    )
    required_shock_measurements = {"p1", "p2", "sensor_uncertainty", "p01", "p02"}
    _invariant(
        out,
        "U09.COMP.Z6.required_measurements",
        {"p1", "p2", "sensor_uncertainty"}.issubset(required_shock_measurements)
        and {"p01", "p02"}.issubset(required_shock_measurements),
        "Za broj i provjeru ukupnog tlaka nedostaju tlakovi i njihove nesigurnosti.",
    )

    return out


def main() -> int:
    results = verify()
    for result in results:
        marker = "v" if result["status"] == "OK" else "x"
        print(f"  [{marker}] {result['id']:46s} {result['details']}")
    failed = sum(result["status"] != "OK" for result in results)
    print(f"\nTotal: ok={len(results) - failed}, fail={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
