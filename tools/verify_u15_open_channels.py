"""Neovisna numericka verifikacija poglavlja o otvorenim tokovima."""
from __future__ import annotations

from fractions import Fraction
import math


G = 9.81


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
LENGTH: Dim = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
TIME: Dim = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
DIMLESS: Dim = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))


def _dim_product(*items: Dim) -> Dim:
    return tuple(sum(parts, Fraction(0)) for parts in zip(*items))  # type: ignore[return-value]


def _dim_power(item: Dim, exponent: Fraction) -> Dim:
    return tuple(value * exponent for value in item)  # type: ignore[return-value]


VELOCITY = _dim_product(LENGTH, _dim_power(TIME, Fraction(-1)))
ACCELERATION = _dim_product(LENGTH, _dim_power(TIME, Fraction(-2)))
DISCHARGE = _dim_product(_dim_power(LENGTH, Fraction(3)), _dim_power(TIME, Fraction(-1)))
UNIT_DISCHARGE = _dim_product(_dim_power(LENGTH, Fraction(2)), _dim_power(TIME, Fraction(-1)))


def froude_channel(
    width: float = 2.0,
    discharge: float = 3.0,
    depth: float = 0.80,
    gravity: float = G,
) -> dict[str, float]:
    velocity = discharge / (width * depth)
    wave_speed = math.sqrt(gravity * depth)
    return {"velocity": velocity, "froude": velocity / wave_speed, "wave_speed": wave_speed}


def critical_section(
    width: float = 4.0,
    discharge: float = 8.0,
    gravity: float = G,
) -> dict[str, float]:
    unit_discharge = discharge / width
    critical_depth = (unit_discharge**2 / gravity) ** (1.0 / 3.0)
    critical_velocity = unit_discharge / critical_depth
    froude = critical_velocity / math.sqrt(gravity * critical_depth)
    return {
        "unit_discharge": unit_discharge,
        "critical_depth": critical_depth,
        "minimum_energy": 1.5 * critical_depth,
        "critical_velocity": critical_velocity,
        "froude": froude,
    }


def specific_energy(depth: float, unit_discharge: float, gravity: float = G) -> float:
    return depth + unit_discharge**2 / (2.0 * gravity * depth**2)


def froude_rectangular(depth: float, unit_discharge: float, gravity: float = G) -> float:
    velocity = unit_discharge / depth
    return velocity / math.sqrt(gravity * depth)


def _bisect_root(function, lower: float, upper: float) -> float:
    f_lower = function(lower)
    f_upper = function(upper)
    if f_lower == 0.0:
        return lower
    if f_upper == 0.0:
        return upper
    if f_lower * f_upper > 0.0:
        raise ValueError("Interval ne omeđuje korijen.")
    for _ in range(100):
        midpoint = (lower + upper) / 2.0
        f_midpoint = function(midpoint)
        if f_lower * f_midpoint <= 0.0:
            upper = midpoint
            f_upper = f_midpoint
        else:
            lower = midpoint
            f_lower = f_midpoint
    return (lower + upper) / 2.0


def alternative_depths(
    unit_discharge: float = 1.5,
    energy: float = 1.20,
    gravity: float = G,
) -> dict[str, float]:
    critical_depth = (unit_discharge**2 / gravity) ** (1.0 / 3.0)
    minimum_energy = 1.5 * critical_depth
    if energy <= minimum_energy:
        raise ValueError("Za dvije grane mora vrijediti E > E_min.")

    equation = lambda depth: specific_energy(depth, unit_discharge, gravity) - energy
    shallow = _bisect_root(equation, critical_depth * 1.0e-9, critical_depth)
    upper = max(energy, critical_depth) * 2.0
    while equation(upper) < 0.0:
        upper *= 2.0
    deep = _bisect_root(equation, critical_depth, upper)
    return {
        "deep_depth": deep,
        "shallow_depth": shallow,
        "deep_froude": froude_rectangular(deep, unit_discharge, gravity),
        "shallow_froude": froude_rectangular(shallow, unit_discharge, gravity),
        "critical_depth": critical_depth,
        "minimum_energy": minimum_energy,
    }


def hydraulic_jump(
    upstream_depth: float = 0.25,
    upstream_velocity: float = 6.0,
    gravity: float = G,
) -> dict[str, float]:
    upstream_froude = upstream_velocity / math.sqrt(gravity * upstream_depth)
    depth_ratio = 0.5 * (math.sqrt(1.0 + 8.0 * upstream_froude**2) - 1.0)
    downstream_depth = upstream_depth * depth_ratio
    energy_loss = (downstream_depth - upstream_depth) ** 3 / (
        4.0 * upstream_depth * downstream_depth
    )
    unit_discharge = upstream_velocity * upstream_depth
    return {
        "upstream_froude": upstream_froude,
        "depth_ratio": depth_ratio,
        "downstream_depth": downstream_depth,
        "energy_loss": energy_loss,
        "unit_discharge": unit_discharge,
    }


def manning_channel(
    width: float = 3.0,
    depth: float = 1.0,
    friction_slope: float = 0.001,
    clean_n: float = 0.015,
    vegetated_n: float = 0.025,
) -> dict[str, float]:
    area = width * depth
    wetted_perimeter = width + 2.0 * depth
    hydraulic_radius = area / wetted_perimeter

    def discharge(n: float) -> float:
        return area * hydraulic_radius ** (2.0 / 3.0) * math.sqrt(friction_slope) / n

    clean_discharge = discharge(clean_n)
    vegetated_discharge = discharge(vegetated_n)
    return {
        "area": area,
        "wetted_perimeter": wetted_perimeter,
        "hydraulic_radius": hydraulic_radius,
        "clean_discharge": clean_discharge,
        "vegetated_discharge": vegetated_discharge,
        "capacity_drop_percent": 100.0 * (1.0 - vegetated_discharge / clean_discharge),
    }


def exercise_froude(
    width: float = 1.5,
    discharge: float = 1.2,
    depth: float = 0.60,
    gravity: float = G,
) -> dict[str, float]:
    velocity = discharge / (width * depth)
    return {"velocity": velocity, "froude": velocity / math.sqrt(gravity * depth)}


def exercise_critical_depth(
    unit_discharge: float = 3.0, gravity: float = G
) -> dict[str, float]:
    critical_depth = (unit_discharge**2 / gravity) ** (1.0 / 3.0)
    return {"critical_depth": critical_depth, "minimum_energy": 1.5 * critical_depth}


def exercise_trapezoidal_section(
    bottom_width: float = 2.40,
    side_slope: float = 1.50,
    depth: float = 0.900,
    discharge: float = 3.60,
    gravity: float = G,
) -> dict[str, float]:
    area = depth * (bottom_width + side_slope * depth)
    top_width = bottom_width + 2.0 * side_slope * depth
    wetted_perimeter = bottom_width + 2.0 * depth * math.sqrt(1.0 + side_slope**2)
    hydraulic_depth = area / top_width
    hydraulic_radius = area / wetted_perimeter
    velocity = discharge / area
    froude = velocity / math.sqrt(gravity * hydraulic_depth)
    return {
        "area": area,
        "top_width": top_width,
        "wetted_perimeter": wetted_perimeter,
        "hydraulic_depth": hydraulic_depth,
        "hydraulic_radius": hydraulic_radius,
        "velocity": velocity,
        "froude": froude,
    }


def exercise_measured_jump(
    discharge: float = 1.800,
    width: float = 1.200,
    upstream_depth: float = 0.250,
    downstream_depth: float = 1.220,
    discharge_uncertainty: float = 0.018,
    width_uncertainty: float = 0.003,
    upstream_depth_uncertainty: float = 0.003,
    downstream_depth_uncertainty: float = 0.008,
    gravity: float = G,
) -> dict[str, float]:
    unit_discharge = discharge / width
    unit_discharge_uncertainty = math.sqrt(
        (discharge_uncertainty / width) ** 2
        + (discharge * width_uncertainty / width**2) ** 2
    )

    def momentum_function(depth: float) -> float:
        return depth**2 / 2.0 + unit_discharge**2 / (gravity * depth)

    residual = momentum_function(downstream_depth) - momentum_function(upstream_depth)
    derivative_y1 = -(
        upstream_depth
        - unit_discharge**2 / (gravity * upstream_depth**2)
    )
    derivative_y2 = (
        downstream_depth
        - unit_discharge**2 / (gravity * downstream_depth**2)
    )
    derivative_q = 2.0 * unit_discharge / gravity * (
        1.0 / downstream_depth - 1.0 / upstream_depth
    )
    residual_uncertainty = math.sqrt(
        (derivative_y1 * upstream_depth_uncertainty) ** 2
        + (derivative_y2 * downstream_depth_uncertainty) ** 2
        + (derivative_q * unit_discharge_uncertainty) ** 2
    )
    upstream_froude = (
        unit_discharge
        / upstream_depth
        / math.sqrt(gravity * upstream_depth)
    )
    conjugate_depth = upstream_depth / 2.0 * (
        math.sqrt(1.0 + 8.0 * upstream_froude**2) - 1.0
    )
    return {
        "unit_discharge": unit_discharge,
        "unit_discharge_uncertainty": unit_discharge_uncertainty,
        "residual": residual,
        "residual_uncertainty": residual_uncertainty,
        "normalized_residual": abs(residual) / residual_uncertainty,
        "conjugate_depth": conjugate_depth,
    }


def _manning_trapezoid_discharge(
    depth: float,
    manning_n: float,
    bottom_width: float,
    side_slope: float,
    friction_slope: float,
) -> float:
    area = depth * (bottom_width + side_slope * depth)
    wetted_perimeter = (
        bottom_width + 2.0 * depth * math.sqrt(1.0 + side_slope**2)
    )
    hydraulic_radius = area / wetted_perimeter
    return (
        area
        * hydraulic_radius ** (2.0 / 3.0)
        * math.sqrt(friction_slope)
        / manning_n
    )


def exercise_climate_channel(
    bottom_width: float = 3.00,
    side_slope: float = 2.00,
    friction_slope: float = 0.00150,
    structural_depth: float = 1.50,
    minimum_freeboard: float = 0.300,
    design_discharge: float = 8.00,
    basin_width: float = 5.00,
    jump_upstream_depth: float = 0.350,
    allowable_conjugate_depth: float = 1.40,
    gravity: float = G,
) -> dict[str, tuple[float, ...] | float]:
    roughness = (0.018, 0.026, 0.035)
    roughness_uncertainty = (0.001, 0.002, 0.004)
    allowable_depth = structural_depth - minimum_freeboard

    def capacity(depth: float, manning_n: float) -> float:
        return _manning_trapezoid_discharge(
            depth,
            manning_n,
            bottom_width,
            side_slope,
            friction_slope,
        )

    def normal_depth(manning_n: float) -> float:
        return _bisect_root(
            lambda depth: capacity(depth, manning_n) - design_discharge,
            1.0e-9,
            3.0 * structural_depth,
        )

    def jump_depth(discharge: float) -> float:
        unit_discharge = discharge / basin_width
        upstream_froude = (
            unit_discharge
            / jump_upstream_depth
            / math.sqrt(gravity * jump_upstream_depth)
        )
        return jump_upstream_depth / 2.0 * (
            math.sqrt(1.0 + 8.0 * upstream_froude**2) - 1.0
        )

    mean_capacities = tuple(capacity(allowable_depth, n) for n in roughness)
    conservative_roughness = tuple(
        n + 2.0 * uncertainty
        for n, uncertainty in zip(roughness, roughness_uncertainty)
    )
    conservative_capacities = tuple(
        capacity(allowable_depth, n) for n in conservative_roughness
    )
    normal_depths = tuple(normal_depth(n) for n in roughness)
    freeboards = tuple(structural_depth - depth for depth in normal_depths)
    capacity_jump_depths = tuple(jump_depth(flow) for flow in mean_capacities)
    return {
        "mean_capacities": mean_capacities,
        "conservative_capacities": conservative_capacities,
        "normal_depths": normal_depths,
        "freeboards": freeboards,
        "design_jump_depth": jump_depth(design_discharge),
        "capacity_jump_depths": capacity_jump_depths,
        "robust_state_count": float(
            sum(flow >= design_discharge for flow in conservative_capacities)
        ),
        "basin_exceedance_count": float(
            sum(depth > allowable_conjugate_depth for depth in capacity_jump_depths)
        ),
    }


def verify() -> list[dict[str, str]]:
    out: list[dict[str, str]] = []

    r = froude_channel()
    _check(out, "U15.P1.v", r["velocity"], 1.875, "m/s", abs_tol=0.0005)
    _check(out, "U15.P1.Fr", r["froude"], 0.669, "", abs_tol=0.0005)
    _check(out, "U15.P1.c", r["wave_speed"], 2.80, "m/s", abs_tol=0.005)

    r = critical_section()
    _check(out, "U15.P2.q", r["unit_discharge"], 2.0, "m^2/s", abs_tol=0.05)
    _check(out, "U15.P2.yc", r["critical_depth"], 0.742, "m", abs_tol=0.0005)
    # E_min je u tekstu izracunat iz prethodno zaokruzenog y_c=0.742 m.
    _check(out, "U15.P2.Emin", r["minimum_energy"], 1.113, "m", abs_tol=0.001)
    _check(out, "U15.P2.vc", r["critical_velocity"], 2.70, "m/s", abs_tol=0.005)
    _check(out, "U15.P2.Fr", r["froude"], 1.00, "", abs_tol=0.005)

    r = alternative_depths()
    _check(out, "U15.P3.y_deep", r["deep_depth"], 1.106, "m", abs_tol=0.0005)
    _check(out, "U15.P3.y_shallow", r["shallow_depth"], 0.372, "m", abs_tol=0.0005)
    _check(out, "U15.P3.Fr_deep", r["deep_froude"], 0.412, "", abs_tol=0.0005)
    _check(out, "U15.P3.Fr_shallow", r["shallow_froude"], 2.11, "", abs_tol=0.005)

    r = hydraulic_jump()
    _check(out, "U15.P4.Fr1", r["upstream_froude"], 3.83, "", abs_tol=0.005)
    _check(out, "U15.P4.y2_y1", r["depth_ratio"], 4.94, "", abs_tol=0.005)
    _check(out, "U15.P4.y2", r["downstream_depth"], 1.24, "m", abs_tol=0.005)
    _check(out, "U15.P4.delta_E", r["energy_loss"], 0.774, "m", abs_tol=0.0005)

    r = manning_channel()
    _check(out, "U15.P5.A", r["area"], 3.0, "m^2", abs_tol=0.05)
    _check(out, "U15.P5.P", r["wetted_perimeter"], 5.0, "m", abs_tol=0.05)
    _check(out, "U15.P5.Rh", r["hydraulic_radius"], 0.60, "m", abs_tol=0.005)
    _check(out, "U15.P5.Q_clean", r["clean_discharge"], 4.50, "m^3/s", abs_tol=0.005)
    _check(
        out,
        "U15.P5.Q_vegetated",
        r["vegetated_discharge"],
        2.70,
        "m^3/s",
        abs_tol=0.005,
    )
    _check(
        out,
        "U15.P5.capacity_drop",
        r["capacity_drop_percent"],
        40.0,
        "%",
        abs_tol=0.05,
    )

    r = exercise_froude()
    _check(out, "U15.Z1.v", r["velocity"], 1.33, "m/s", abs_tol=0.005)
    _check(out, "U15.Z1.Fr", r["froude"], 0.55, "", abs_tol=0.005)

    r = exercise_critical_depth()
    _check(out, "U15.Z2.yc", r["critical_depth"], 0.972, "m", abs_tol=0.0005)
    _check(out, "U15.Z2.Emin", r["minimum_energy"], 1.46, "m", abs_tol=0.005)

    r = exercise_trapezoidal_section()
    _check(out, "U15.Z3.A", r["area"], 3.375, "m^2", abs_tol=0.0005)
    _check(out, "U15.Z3.T", r["top_width"], 5.100, "m", abs_tol=0.0005)
    _check(out, "U15.Z3.P", r["wetted_perimeter"], 5.645, "m", abs_tol=0.0005)
    _check(out, "U15.Z3.Dh", r["hydraulic_depth"], 0.6618, "m", abs_tol=0.00005)
    _check(out, "U15.Z3.Rh", r["hydraulic_radius"], 0.5979, "m", abs_tol=0.00005)
    _check(out, "U15.Z3.v", r["velocity"], 1.0667, "m/s", abs_tol=0.00005)
    _check(out, "U15.Z3.Fr", r["froude"], 0.4186, "1", abs_tol=0.00005)

    r = alternative_depths(unit_discharge=2.20, energy=1.600)
    _check(out, "U15.Z4.yc", r["critical_depth"], 0.7902, "m", abs_tol=0.00005)
    _check(out, "U15.Z4.Emin", r["minimum_energy"], 1.1853, "m", abs_tol=0.00005)
    _check(out, "U15.Z4.y_shallow", r["shallow_depth"], 0.4665, "m", abs_tol=0.00005)
    _check(out, "U15.Z4.Fr_shallow", r["shallow_froude"], 2.204, "1", abs_tol=0.0005)
    _check(out, "U15.Z4.y_deep", r["deep_depth"], 1.4887, "m", abs_tol=0.00005)
    _check(out, "U15.Z4.Fr_deep", r["deep_froude"], 0.3867, "1", abs_tol=0.00005)

    r = exercise_measured_jump()
    _check(out, "U15.Z5.q", r["unit_discharge"], 1.5000, "m^2/s", abs_tol=0.00005)
    _check(
        out,
        "U15.Z5.u_q",
        r["unit_discharge_uncertainty"],
        0.01546,
        "m^2/s",
        abs_tol=0.000005,
    )
    _check(out, "U15.Z5.R", r["residual"], -0.01648, "m^2", abs_tol=0.000005)
    _check(
        out,
        "U15.Z5.u_R",
        r["residual_uncertainty"],
        0.02010,
        "m^2",
        abs_tol=0.000005,
    )
    _check(
        out,
        "U15.Z5.normalized_residual",
        r["normalized_residual"],
        0.820,
        "1",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z5.y2_theory",
        r["conjugate_depth"],
        1.2353,
        "m",
        abs_tol=0.00005,
    )

    r = exercise_climate_channel()
    mean_capacities = r["mean_capacities"]
    conservative_capacities = r["conservative_capacities"]
    normal_depths = r["normal_depths"]
    freeboards = r["freeboards"]
    capacity_jump_depths = r["capacity_jump_depths"]
    assert isinstance(mean_capacities, tuple)
    assert isinstance(conservative_capacities, tuple)
    assert isinstance(normal_depths, tuple)
    assert isinstance(freeboards, tuple)
    assert isinstance(capacity_jump_depths, tuple)
    _check(out, "U15.Z6.Qcap_A", mean_capacities[0], 11.759, "m^3/s", abs_tol=0.0005)
    _check(out, "U15.Z6.Qcap_B", mean_capacities[1], 8.141, "m^3/s", abs_tol=0.0005)
    _check(out, "U15.Z6.Qcap_C", mean_capacities[2], 6.047, "m^3/s", abs_tol=0.0005)
    _check(out, "U15.Z6.yn_A", normal_depths[0], 0.985, "m", abs_tol=0.0005)
    _check(out, "U15.Z6.yn_B", normal_depths[1], 1.189, "m", abs_tol=0.0005)
    _check(out, "U15.Z6.yn_C", normal_depths[2], 1.380, "m", abs_tol=0.0005)
    _check(out, "U15.Z6.freeboard_A", freeboards[0], 0.515, "m", abs_tol=0.0005)
    _check(out, "U15.Z6.freeboard_B", freeboards[1], 0.311, "m", abs_tol=0.0005)
    _check(out, "U15.Z6.freeboard_C", freeboards[2], 0.120, "m", abs_tol=0.0005)
    _check(
        out,
        "U15.Z6.Qcap_conservative_A",
        conservative_capacities[0],
        10.583,
        "m^3/s",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.Qcap_conservative_B",
        conservative_capacities[1],
        7.055,
        "m^3/s",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.Qcap_conservative_C",
        conservative_capacities[2],
        4.922,
        "m^3/s",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.y2_design",
        float(r["design_jump_depth"]),
        1.059,
        "m",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.y2_capacity_A",
        capacity_jump_depths[0],
        1.628,
        "m",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.y2_capacity_B",
        capacity_jump_depths[1],
        1.080,
        "m",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.y2_capacity_C",
        capacity_jump_depths[2],
        0.765,
        "m",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U15.Z6.robust_state_count",
        float(r["robust_state_count"]),
        1.0,
        "1",
        abs_tol=0.05,
    )
    _check(
        out,
        "U15.Z6.basin_exceedance_count",
        float(r["basin_exceedance_count"]),
        1.0,
        "1",
        abs_tol=0.05,
    )

    froude_dimension = _dim_product(
        VELOCITY,
        _dim_power(_dim_product(ACCELERATION, LENGTH), Fraction(-1, 2)),
    )
    energy_dimension = _dim_product(
        _dim_power(UNIT_DISCHARGE, Fraction(2)),
        _dim_power(ACCELERATION, Fraction(-1)),
        _dim_power(LENGTH, Fraction(-2)),
    )
    momentum_function_dimension = _dim_product(
        _dim_power(UNIT_DISCHARGE, Fraction(2)),
        _dim_power(ACCELERATION, Fraction(-1)),
        _dim_power(LENGTH, Fraction(-1)),
    )
    manning_n_dimension = _dim_product(
        TIME, _dim_power(LENGTH, Fraction(-1, 3))
    )
    manning_discharge_dimension = _dim_product(
        _dim_power(LENGTH, Fraction(2)),
        _dim_power(LENGTH, Fraction(2, 3)),
        _dim_power(manning_n_dimension, Fraction(-1)),
    )
    _invariant(
        out,
        "U15.INV.dimension_froude",
        froude_dimension == DIMLESS,
        f"Fr ima dimenziju {froude_dimension}, a ne bezdimenzijsku",
    )
    _invariant(
        out,
        "U15.INV.dimension_specific_energy",
        energy_dimension == LENGTH,
        "q^2/(g y^2) nema dimenziju duljine",
    )
    _invariant(
        out,
        "U15.INV.dimension_momentum_function",
        momentum_function_dimension == _dim_power(LENGTH, Fraction(2)),
        "q^2/(g y) nema dimenziju L^2",
    )
    _invariant(
        out,
        "U15.INV.dimension_manning",
        manning_discharge_dimension == DISCHARGE,
        "Manningova relacija uz [n]=T/L^(1/3) nema dimenziju protoka",
    )

    critical = critical_section()
    yc = critical["critical_depth"]
    q = critical["unit_discharge"]
    energy_derivative = 1.0 - q**2 / (G * yc**3)
    _invariant(
        out,
        "U15.INV.critical_depth_limit",
        abs(energy_derivative) < 1.0e-12 and abs(critical["froude"] - 1.0) < 1.0e-12,
        "kriticna dubina ne daje istodobno dE/dy=0 i Fr=1",
    )

    jump = hydraulic_jump()
    y1 = 0.25
    y2 = jump["downstream_depth"]
    q_jump = jump["unit_discharge"]
    momentum_1 = y1**2 / 2.0 + q_jump**2 / (G * y1)
    momentum_2 = y2**2 / 2.0 + q_jump**2 / (G * y2)
    _invariant(
        out,
        "U15.INV.hydraulic_jump_balance",
        abs(momentum_2 / momentum_1 - 1.0) < 1.0e-12
        and y2 > y1
        and jump["energy_loss"] > 0.0,
        "spregnute dubine ne zatvaraju kolicinu gibanja uz pozitivan gubitak energije",
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
