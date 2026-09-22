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


def exercise_acoustic_measurement(
    length: float = 1.20,
    downstream_time: float = 0.003,
    upstream_time: float = 0.004,
    gamma: float = GAMMA_AIR,
    gas_constant: float = R_AIR,
) -> dict[str, float]:
    downstream_speed = length / downstream_time
    upstream_speed = -length / upstream_time
    sound_speed = (downstream_speed - upstream_speed) / 2.0
    velocity = (downstream_speed + upstream_speed) / 2.0
    return {
        "sound_speed": sound_speed,
        "velocity": velocity,
        "temperature": sound_speed**2 / (gamma * gas_constant),
        "mach": velocity / sound_speed,
        "downstream_speed": downstream_speed,
        "upstream_speed": upstream_speed,
    }


def exercise_critical_pressure_bar(
    reservoir_pressure_bar: float = 8.0, gamma: float = GAMMA_AIR
) -> float:
    return reservoir_pressure_bar * (2.0 / (gamma + 1.0)) ** (
        gamma / (gamma - 1.0)
    )


def convergent_exit(
    back_pressure_bar: float,
    reservoir_pressure_bar: float = 8.0,
    gamma: float = GAMMA_AIR,
) -> dict[str, float]:
    critical = exercise_critical_pressure_bar(reservoir_pressure_bar, gamma)
    exit_pressure = max(back_pressure_bar, critical)
    mach = math.sqrt(2.0 / (gamma - 1.0) * (
        (reservoir_pressure_bar / exit_pressure) ** ((gamma - 1.0) / gamma) - 1.0
    ))
    return {"exit_pressure_bar": exit_pressure, "mach": mach}


def exercise_back_pressure_settings(
    reservoir_gauge_bar: float = 7.0,
    atmosphere_bar: float = 1.0,
    back_gauge_i_bar: float = 4.0,
    back_gauge_ii_bar: float = 3.0,
) -> dict[str, float]:
    reservoir_abs = reservoir_gauge_bar + atmosphere_bar
    back_i = back_gauge_i_bar + atmosphere_bar
    back_ii = back_gauge_ii_bar + atmosphere_bar
    case_i = convergent_exit(back_i, reservoir_abs)
    case_ii = convergent_exit(back_ii, reservoir_abs)
    return {
        "reservoir_abs_bar": reservoir_abs,
        "critical_bar": exercise_critical_pressure_bar(reservoir_abs),
        "back_i_bar": back_i,
        "back_ii_bar": back_ii,
        "exit_i_bar": case_i["exit_pressure_bar"],
        "exit_ii_bar": case_ii["exit_pressure_bar"],
        "mach_i": case_i["mach"],
        "mach_ii": case_ii["mach"],
    }


def exercise_nozzle_identification(
    reservoir_pressure: float = 600_000.0,
    reservoir_temperature: float = 300.0,
    measured_mass_flow: float = 0.0595,
    measured_area: float = 48.0e-6,
    back_pressure: float = 100_000.0,
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
    discharge_coefficient = discharge_area / measured_area
    return {
        "discharge_area_mm2": discharge_area * 1.0e6,
        "discharge_coefficient": discharge_coefficient,
        "ideal_mass_flow": measured_area * flow_factor,
        "back_pressure_ratio": back_pressure / reservoir_pressure,
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
    z2_velocity = 2.0 / (math.pi * 0.20**2 / 4.0)
    _check(out, "U09.COMP.Z2.v", z2_velocity, 63.66, "m/s", abs_tol=0.005)

    z3 = exercise_acoustic_measurement()
    _check(out, "U09.COMP.Z3.a", z3["sound_speed"], 350.0, "m/s", abs_tol=0.5)
    _check(out, "U09.COMP.Z3.v", z3["velocity"], 50.0, "m/s", abs_tol=0.05)
    _check(out, "U09.COMP.Z3.T", z3["temperature"], 304.9, "K", abs_tol=0.05)
    _check(out, "U09.COMP.Z3.Ma", z3["mach"], 0.143, "", abs_tol=0.0005)
    _check(out, "U09.COMP.Z3.c_AB", z3["downstream_speed"], 400.0, "m/s", abs_tol=0.5)
    _check(out, "U09.COMP.Z3.c_BA", z3["upstream_speed"], -300.0, "m/s", abs_tol=0.5)

    z4 = exercise_back_pressure_settings()
    _check(out, "U09.COMP.Z4.p0", z4["reservoir_abs_bar"], 8.00, "bar(abs)", abs_tol=0.005)
    _check(out, "U09.COMP.Z4.pstar", z4["critical_bar"], 4.226, "bar(abs)", abs_tol=0.0005)
    _check(out, "U09.COMP.Z4.pb_I", z4["back_i_bar"], 5.00, "bar(abs)", abs_tol=0.005)
    _check(out, "U09.COMP.Z4.pb_II", z4["back_ii_bar"], 4.00, "bar(abs)", abs_tol=0.005)
    _check(out, "U09.COMP.Z4.pe_I", z4["exit_i_bar"], 5.00, "bar(abs)", abs_tol=0.005)
    _check(out, "U09.COMP.Z4.pe_II", z4["exit_ii_bar"], 4.226, "bar(abs)", abs_tol=0.0005)
    _check(out, "U09.COMP.Z4.Ma_I", z4["mach_i"], 0.848, "", abs_tol=0.0005)
    _check(out, "U09.COMP.Z4.Ma_II", z4["mach_ii"], 1.0, "", abs_tol=1e-12)

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
        "U09.COMP.Z5.mdot_ideal",
        z5["ideal_mass_flow"],
        0.0672,
        "kg/s",
        abs_tol=0.00005,
    )
    _check(out, "U09.COMP.Z5.pb_p0", z5["back_pressure_ratio"], 0.167, "", abs_tol=0.0005)

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

    _invariant(out, "U09.COMP.Z3.upstream_propagation",
               0.0 < z3["velocity"] < z3["sound_speed"] and z3["upstream_speed"] < 0.0,
               "Signal mora stizati uzvodno jer je v<a.")
    quiet = exercise_acoustic_measurement(downstream_time=0.004, upstream_time=0.004)
    _invariant(out, "U09.COMP.Z3.equal_times_at_rest",
               abs(quiet["velocity"]) < 1e-12 and abs(quiet["sound_speed"] - 300.0) < 1e-12,
               "Jednaka vremena u oba smjera moraju dati v=0 i a=L/t.")
    reversed_flow = exercise_acoustic_measurement(downstream_time=0.004, upstream_time=0.003)
    _invariant(out, "U09.COMP.Z3.reverse_flow",
               abs(reversed_flow["temperature"] - z3["temperature"]) < 1e-10
               and abs(reversed_flow["velocity"] + z3["velocity"]) < 1e-10,
               "Zamjena smjerova mjerenja mora promijeniti predznak v, ali ne T.")

    _invariant(out, "U09.COMP.Z4.regime_selection",
               z4["back_i_bar"] > z4["critical_bar"] > z4["back_ii_bar"]
               and z4["mach_i"] < 1.0 and z4["exit_ii_bar"] > z4["back_ii_bar"],
               "I mora ostati podzvučan, a u II izlazni tlak nadmašiti protutlak.")
    # Independent rho*v evaluation at the exit checks the plateau, not just M.
    def exit_flux(back: float) -> float:
        state = convergent_exit(back)
        t = 300.0 / (1.0 + 0.2 * state["mach"]**2)
        density = state["exit_pressure_bar"] * 1e5 / (R_AIR * t)
        return density * state["mach"] * math.sqrt(GAMMA_AIR * R_AIR * t)
    max_flux = choked_orifice(reservoir_pressure=8e5, throat_area=1.0)["mass_flow"]
    _invariant(out, "U09.COMP.Z4.mass_flux_plateau",
               exit_flux(5.0) < max_flux
               and all(abs(exit_flux(back) / max_flux - 1.0) < 1e-12 for back in (4.0, 2.0, 0.1)),
               "rho_e v_e mora prije prigušenja biti manji, a potom ostati na maksimumu.")

    # Z5: samo mjerenje protoka određuje umnožak C_d A_g, ne oba faktora.
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
        "Jedno mjerenje mora ostaviti degeneraciju C_d*A_g.",
    )
    _invariant(
        out,
        "U09.COMP.Z5.geometry_not_sufficient",
        z5["back_pressure_ratio"] < critical_ratio
        and z5["ideal_mass_flow"] > 0.0595
        and 0.0 < z5["discharge_coefficient"] < 1.0,
        "Izmjereni otvor sam ne smije objasniti izmjereni manji prigušeni protok.",
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
    # Independent Rankine-Hugoniot form of the total-pressure ratio (NACA 1135).
    m, g = z6["upstream_mach"], GAMMA_AIR
    density_ratio = (g + 1.0) * m**2 / ((g - 1.0) * m**2 + 2.0)
    direct_total_ratio = density_ratio ** (g / (g - 1.0)) * (
        (g + 1.0) / (2.0 * g * m**2 - (g - 1.0))
    ) ** (1.0 / (g - 1.0))
    _invariant(
        out,
        "U09.COMP.Z6.independent_total_pressure_relation",
        abs(direct_total_ratio - z6["theoretical_total_ratio"]) < 1e-12,
        "Dva neovisna oblika relacije ukupnog tlaka moraju se slagati.",
    )
    temperature_ratio = shock["pressure_ratio"] / density_ratio
    speed_ratio = 1.0 / density_ratio
    energy_before = 1.0 / (g - 1.0) + m**2 / 2.0
    energy_after = temperature_ratio / (g - 1.0) + (m * speed_ratio)**2 / 2.0
    _invariant(out, "U09.COMP.Z6.mass_momentum_energy",
               abs((shock["pressure_ratio"] + g*m*m/density_ratio) - (1.0+g*m*m)) < 1e-12
               and abs(energy_after - energy_before) < 1e-12,
               "Skok mora očuvati tok količine gibanja i ukupnu entalpiju uz isti maseni protok.")
    weak = normal_shock(1.0)
    _invariant(out, "U09.COMP.Z6.vanishing_shock",
               all(abs(value-1.0) < 1e-12 for value in weak.values()),
               "Pri M1=1 skok nestaje: M2 i oba omjera tlakova moraju biti 1.")
    _invariant(out, "U09.COMP.Z6.measurement_decision",
               z6["normalized_difference"] < 1.0,
               "Zadani podatci moraju zadovoljiti objavljeni kriterij kombinirane standardne nesigurnosti.")

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
