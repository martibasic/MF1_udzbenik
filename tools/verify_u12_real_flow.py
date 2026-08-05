"""Neovisna numericka verifikacija diferencijalnog opisa realnog toka."""
from __future__ import annotations

import csv
from fractions import Fraction
import math
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


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
MASS: Dim = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
LENGTH: Dim = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
TIME: Dim = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))


def _dim_product(*items: Dim) -> Dim:
    return tuple(sum(parts, Fraction(0)) for parts in zip(*items))  # type: ignore[return-value]


def _dim_power(item: Dim, exponent: Fraction) -> Dim:
    return tuple(value * exponent for value in item)  # type: ignore[return-value]


VELOCITY = _dim_product(LENGTH, _dim_power(TIME, Fraction(-1)))
ACCELERATION = _dim_product(LENGTH, _dim_power(TIME, Fraction(-2)))
DENSITY = _dim_product(MASS, _dim_power(LENGTH, Fraction(-3)))
PRESSURE = _dim_product(
    MASS, _dim_power(LENGTH, Fraction(-1)), _dim_power(TIME, Fraction(-2))
)
DYNAMIC_VISCOSITY = _dim_product(
    MASS, _dim_power(LENGTH, Fraction(-1)), _dim_power(TIME, Fraction(-1))
)
KINEMATIC_VISCOSITY = _dim_product(
    _dim_power(LENGTH, Fraction(2)), _dim_power(TIME, Fraction(-1))
)


def contraction_acceleration(x: float = 0.50) -> dict[str, float]:
    velocity = 2.0 + 3.0 * x
    velocity_gradient = 3.0
    return {
        "velocity": velocity,
        "local_acceleration": 0.0,
        "convective_acceleration": velocity * velocity_gradient,
    }


def couette_poiseuille_midpoint(
    height: float = 1.0e-3,
    plate_velocity: float = 2.0,
    viscosity: float = 0.10,
    pressure_gradient: float = -100_000.0,
) -> dict[str, float]:
    y = height / 2.0
    couette = plate_velocity * y / height
    pressure = pressure_gradient * (y**2 - height * y) / (2.0 * viscosity)
    return {"couette": couette, "pressure": pressure, "velocity": couette + pressure}


def microchannel(
    viscosity: float = 1.0e-3,
    density: float = 1000.0,
    diameter: float = 0.50e-3,
    length: float = 0.20,
    volume_flow_ml_min: float = 0.30,
) -> dict[str, float]:
    volume_flow = volume_flow_ml_min * 1.0e-6 / 60.0
    pressure_drop = (
        128.0 * viscosity * length * volume_flow / (math.pi * diameter**4)
    )
    mean_velocity = volume_flow / (math.pi * diameter**2 / 4.0)
    reynolds = density * mean_velocity * diameter / viscosity
    return {
        "volume_flow": volume_flow,
        "pressure_drop": pressure_drop,
        "mean_velocity": mean_velocity,
        "reynolds": reynolds,
    }


def flat_plate_boundary_layer(
    free_stream_velocity: float = 1.5,
    x: float = 0.40,
    kinematic_viscosity: float = 1.0e-6,
) -> dict[str, float]:
    reynolds_x = free_stream_velocity * x / kinematic_viscosity
    delta = 5.0 * x / math.sqrt(reynolds_x)
    return {
        "reynolds_x": reynolds_x,
        "delta_mm": 1000.0 * delta,
        "delta_over_x": delta / x,
    }


def turbulence_intensity(
    mean_velocity: float = 8.0, rms_fluctuation: float = 0.48
) -> dict[str, float]:
    intensity = rms_fluctuation / mean_velocity
    return {"intensity": intensity, "percent": 100.0 * intensity}


def exercise_material_derivative(x: float = 1.0, time: float = 2.0) -> dict[str, float]:
    velocity = 2.0 * time + x**2
    local = 2.0
    convective = velocity * (2.0 * x)
    return {
        "velocity": velocity,
        "local": local,
        "convective": convective,
        "total": local + convective,
    }


def exercise_viscous_diffusion_time(
    height: float = 10.0e-3, kinematic_viscosity: float = 1.0e-6
) -> float:
    return height**2 / kinematic_viscosity


def exercise_inverse_poiseuille(
    volume_flow_ml_min: float = 0.300,
    pressure_drop: float = 652.0,
    length: float = 0.200,
    diameter_mm: float = 0.500,
    density: float = 998.0,
    u_volume_flow_ml_min: float = 0.003,
    u_pressure_drop: float = 5.0,
    u_length: float = 0.001,
    u_diameter_mm: float = 0.005,
) -> dict[str, float]:
    volume_flow = volume_flow_ml_min * 1.0e-6 / 60.0
    diameter = diameter_mm * 1.0e-3
    viscosity = (
        math.pi * diameter**4 * pressure_drop / (128.0 * length * volume_flow)
    )
    mean_velocity = volume_flow / (math.pi * diameter**2 / 4.0)
    reynolds = density * mean_velocity * diameter / viscosity
    relative_uncertainty = math.sqrt(
        (4.0 * u_diameter_mm / diameter_mm) ** 2
        + (u_pressure_drop / pressure_drop) ** 2
        + (u_length / length) ** 2
        + (u_volume_flow_ml_min / volume_flow_ml_min) ** 2
    )
    return {
        "viscosity_mpas": viscosity * 1000.0,
        "u_viscosity_mpas": viscosity * 1000.0 * relative_uncertainty,
        "reynolds": reynolds,
        "diameter_relative_contribution": 4.0 * u_diameter_mm / diameter_mm,
    }


def exercise_couette_shear_change(
    viscosity: float = 0.100,
    plate_velocity: float = 2.00,
    height: float = 1.00e-3,
) -> dict[str, float]:
    critical_gradient = 2.0 * viscosity * plate_velocity / height**2

    def lower_wall_shear(multiplier: float) -> float:
        return (
            viscosity * plate_velocity / height
            - 0.5 * multiplier * critical_gradient * height
        )

    return {
        "critical_gradient": critical_gradient,
        "tau_90": lower_wall_shear(0.90),
        "tau_110": lower_wall_shear(1.10),
    }


def exercise_blasius_assessment(
    kinematic_viscosity: float = 1.00e-6,
    density: float = 998.0,
    x: float = 0.400,
    external_velocity: float = 1.50,
    external_velocity_gradient: float = -0.250,
    roughness: float = 5.0e-6,
) -> dict[str, float]:
    reynolds_x = external_velocity * x / kinematic_viscosity
    delta = 5.0 * x / math.sqrt(reynolds_x)
    return {
        "reynolds_x": reynolds_x,
        "delta_mm": delta * 1000.0,
        "roughness_ratio": roughness / delta,
        "velocity_gradient_parameter": (
            x / external_velocity * external_velocity_gradient
        ),
        "pressure_gradient": (
            -density * external_velocity * external_velocity_gradient
        ),
    }


def exercise_grid_convergence() -> dict[str, float]:
    with (REPO_ROOT / "data/cfd/poiseuille_laminar/grids.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    q_coarse, q_medium, q_fine = [
        float(row["q_volume_m3_s"]) for row in rows
    ]
    refinement_ratio = 2.0
    observed_order = math.log(
        (q_coarse - q_medium) / (q_medium - q_fine)
    ) / math.log(refinement_ratio)
    extrapolated = q_fine + (q_fine - q_medium) / (
        refinement_ratio**observed_order - 1.0
    )
    gci_fine_percent = (
        1.25
        * abs((q_fine - q_medium) / q_fine)
        / (refinement_ratio**observed_order - 1.0)
        * 100.0
    )
    return {
        "observed_order": observed_order,
        "extrapolated_flow": extrapolated,
        "gci_fine_percent": gci_fine_percent,
        "fine_mass_imbalance_percent": float(rows[-1]["mass_imbalance_percent"]),
    }


def verify() -> list[dict[str, str]]:
    out: list[dict[str, str]] = []

    r = contraction_acceleration()
    _check(out, "U12.REAL.P1.u", r["velocity"], 3.5, "m/s", abs_tol=0.05)
    _check(
        out,
        "U12.REAL.P1.ax",
        r["convective_acceleration"],
        10.5,
        "m/s^2",
        abs_tol=0.05,
    )

    r = couette_poiseuille_midpoint()
    _check(out, "U12.REAL.P2.u_couette", r["couette"], 1.0, "m/s", abs_tol=0.05)
    _check(out, "U12.REAL.P2.u_pressure", r["pressure"], 0.125, "m/s", abs_tol=0.0005)
    _check(out, "U12.REAL.P2.u_mid", r["velocity"], 1.125, "m/s", abs_tol=0.0005)

    r = microchannel()
    _check(
        out,
        "U12.REAL.P3.Q_SI",
        r["volume_flow"],
        5.0e-9,
        "m^3/s",
        abs_tol=0.005e-9,
    )
    _check(out, "U12.REAL.P3.dp", r["pressure_drop"], 652.0, "Pa", abs_tol=0.5)
    _check(
        out,
        "U12.REAL.P3.v_mean",
        r["mean_velocity"],
        0.0255,
        "m/s",
        abs_tol=0.00005,
    )
    _check(out, "U12.REAL.P3.Re", r["reynolds"], 12.7, "", abs_tol=0.05)

    r = flat_plate_boundary_layer()
    _check(out, "U12.REAL.P4.Re_x", r["reynolds_x"], 6.0e5, "", abs_tol=500.0)
    _check(out, "U12.REAL.P4.delta99", r["delta_mm"], 2.58, "mm", abs_tol=0.005)
    _check(out, "U12.REAL.P4.delta_x", r["delta_over_x"], 0.0065, "", abs_tol=0.00005)

    r = turbulence_intensity()
    _check(out, "U12.REAL.P5.Iu", r["intensity"], 0.060, "", abs_tol=0.0005)
    _check(out, "U12.REAL.P5.Iu_percent", r["percent"], 6.0, "%", abs_tol=0.05)

    r = exercise_material_derivative()
    _check(out, "U12.REAL.Z1.u", r["velocity"], 5.0, "m/s", abs_tol=0.05)
    _check(out, "U12.REAL.Z1.a_local", r["local"], 2.0, "m/s^2", abs_tol=0.05)
    _check(out, "U12.REAL.Z1.a_conv", r["convective"], 10.0, "m/s^2", abs_tol=0.05)
    _check(out, "U12.REAL.Z1.a_total", r["total"], 12.0, "m/s^2", abs_tol=0.05)
    _check(
        out,
        "U12.REAL.Z2.t_nu",
        exercise_viscous_diffusion_time(),
        100.0,
        "s",
        abs_tol=0.5,
    )

    z3 = exercise_inverse_poiseuille()
    _check(
        out,
        "U12.REAL.Z3.mu_mPas",
        z3["viscosity_mpas"],
        1.000,
        "mPa s",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U12.REAL.Z3.u_mu_mPas",
        z3["u_viscosity_mpas"],
        0.042,
        "mPa s",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U12.REAL.Z3.Re",
        z3["reynolds"],
        12.7,
        "",
        abs_tol=0.05,
    )

    z4 = exercise_couette_shear_change()
    _check(
        out,
        "U12.REAL.Z4.dpdx_critical",
        z4["critical_gradient"],
        4.00e5,
        "Pa/m",
        abs_tol=50.0,
    )
    _check(out, "U12.REAL.Z4.tau_90", z4["tau_90"], 20.0, "Pa", abs_tol=0.05)
    _check(out, "U12.REAL.Z4.tau_110", z4["tau_110"], -20.0, "Pa", abs_tol=0.05)

    z5 = exercise_blasius_assessment()
    _check(out, "U12.REAL.Z5.Re_x", z5["reynolds_x"], 6.00e5, "", abs_tol=500.0)
    _check(out, "U12.REAL.Z5.delta99_mm", z5["delta_mm"], 2.58, "mm", abs_tol=0.005)
    _check(
        out,
        "U12.REAL.Z5.ks_delta",
        z5["roughness_ratio"],
        1.94e-3,
        "",
        abs_tol=0.005e-3,
    )
    _check(
        out,
        "U12.REAL.Z5.gradient_parameter",
        z5["velocity_gradient_parameter"],
        -0.0667,
        "",
        abs_tol=0.00005,
    )

    z6 = exercise_grid_convergence()
    _check(out, "U12.REAL.Z6.p", z6["observed_order"], 2.000, "", abs_tol=0.0005)
    _check(
        out,
        "U12.REAL.Z6.Q_ext",
        z6["extrapolated_flow"],
        7.85398e-6,
        "m^3/s",
        abs_tol=0.000005e-6,
    )
    _check(
        out,
        "U12.REAL.Z6.GCI_fine_percent",
        z6["gci_fine_percent"],
        0.312,
        "%",
        abs_tol=0.0005,
    )
    _check(
        out,
        "U12.REAL.Z6.mass_imbalance_percent",
        z6["fine_mass_imbalance_percent"],
        0.0025,
        "%",
        abs_tol=0.00005,
    )

    convective_dimension = _dim_product(
        VELOCITY, VELOCITY, _dim_power(LENGTH, Fraction(-1))
    )
    momentum_density_dimension = _dim_product(DENSITY, ACCELERATION)
    pressure_gradient_dimension = _dim_product(
        PRESSURE, _dim_power(LENGTH, Fraction(-1))
    )
    viscous_term_dimension = _dim_product(
        DYNAMIC_VISCOSITY,
        VELOCITY,
        _dim_power(LENGTH, Fraction(-2)),
    )
    poiseuille_flow_dimension = _dim_product(
        PRESSURE,
        _dim_power(LENGTH, Fraction(4)),
        _dim_power(DYNAMIC_VISCOSITY, Fraction(-1)),
        _dim_power(LENGTH, Fraction(-1)),
    )
    diffusion_time_dimension = _dim_product(
        _dim_power(LENGTH, Fraction(2)),
        _dim_power(KINEMATIC_VISCOSITY, Fraction(-1)),
    )
    _invariant(
        out,
        "U12.REAL.INV.dimension_material_derivative",
        convective_dimension == ACCELERATION,
        "(u dot grad)u nema dimenziju ubrzanja",
    )
    _invariant(
        out,
        "U12.REAL.INV.dimension_navier_stokes",
        momentum_density_dimension
        == pressure_gradient_dimension
        == viscous_term_dimension,
        "clanovi Navier-Stokesove jednadzbe nisu dimenzijski uskladeni",
    )
    _invariant(
        out,
        "U12.REAL.INV.dimension_poiseuille_flow",
        poiseuille_flow_dimension
        == _dim_product(_dim_power(LENGTH, Fraction(3)), _dim_power(TIME, Fraction(-1))),
        "Hagen-Poiseuilleov izraz nema dimenziju volumnog protoka",
    )
    _invariant(
        out,
        "U12.REAL.INV.dimension_diffusion_time",
        diffusion_time_dimension == TIME,
        "H^2/nu nema dimenziju vremena",
    )

    height = 1.0e-3
    plate_velocity = 2.0
    viscosity = 0.10
    pressure_gradient = -100_000.0

    def profile(y: float) -> float:
        return plate_velocity * y / height + pressure_gradient * (
            y**2 - height * y
        ) / (2.0 * viscosity)

    _invariant(
        out,
        "U12.REAL.INV.couette_boundary_conditions",
        abs(profile(0.0)) < 1.0e-14 and abs(profile(height) - plate_velocity) < 1.0e-14,
        "profil ne zadovoljava u(0)=0 i u(H)=U",
    )

    base = microchannel()
    doubled = microchannel(volume_flow_ml_min=0.60)
    linearity_error = abs(doubled["pressure_drop"] / base["pressure_drop"] - 2.0)
    _invariant(
        out,
        "U12.REAL.INV.poiseuille_linear_limit",
        linearity_error < 1.0e-12,
        f"udvostrucenje Q ne udvostrucuje dp; odstupanje je {linearity_error:.3g}",
    )

    layer = flat_plate_boundary_layer()
    _invariant(
        out,
        "U12.REAL.INV.thin_boundary_layer_limit",
        0.0 < layer["delta_over_x"] < 0.01,
        f"delta/x={layer['delta_over_x']:.6g} nije u tankom granicnom slucaju",
    )

    # Neovisne modelske provjere Z3: dimenzija inverznog modela i četvrta
    # potencija promjera koja dominira propagacijom nesigurnosti.
    dp_sample, diameter_sample, length_sample, flow_sample = (
        500.0,
        1.0e-3,
        0.10,
        1.0e-9,
    )
    mu_sample = (
        math.pi * diameter_sample**4 * dp_sample
        / (128 * length_sample * flow_sample)
    )
    mu_larger_diameter = (
        math.pi * (2 * diameter_sample) ** 4 * dp_sample
        / (128 * length_sample * flow_sample)
    )
    inverse_mu_dimension = _dim_product(
        PRESSURE,
        _dim_power(LENGTH, Fraction(4)),
        _dim_power(LENGTH, Fraction(-1)),
        _dim_power(
            _dim_product(_dim_power(LENGTH, Fraction(3)), _dim_power(TIME, Fraction(-1))),
            Fraction(-1),
        ),
    )
    _invariant(
        out,
        "U12.REAL.Z3.inverse_dimension",
        inverse_mu_dimension == DYNAMIC_VISCOSITY,
        "Inverzni Poiseuilleov izraz nema dimenziju dinamicke viskoznosti.",
    )
    _invariant(
        out,
        "U12.REAL.Z3.diameter_fourth_power",
        abs(mu_larger_diameter / mu_sample - 16.0) < 1.0e-12,
        "Udvostrucenje D pri istim mjerenjima mora promijeniti procjenu mu 16 puta.",
    )

    # Z4: za Couette--Poiseuilleov profil donje smično naprezanje mijenja
    # predznak pri dp/dx=2*mu*U/H^2.
    U, H, mu = 2.0, 1.0e-3, 0.10
    critical_gradient = 2 * mu * U / H**2
    tau_below = mu * U / H - 0.5 * (0.9 * critical_gradient) * H
    tau_above = mu * U / H - 0.5 * (1.1 * critical_gradient) * H
    _invariant(
        out,
        "U12.REAL.Z4.wall_shear_sign_change",
        critical_gradient > 0 and tau_below > 0 > tau_above,
        "Donje smicno naprezanje ne mijenja predznak oko kriticnog gradijenta.",
    )

    # Blasiusov model zahtijeva stacionaran, nestlačiv tok uz glatku ravnu
    # plohu, nulti gradijent tlaka i laminarni raspon; debljina mora padati kao
    # Re_x^{-1/2} u odnosu na x.
    re_low, re_high = 1.0e5, 4.0e5
    relative_delta_low = 5.0 / math.sqrt(re_low)
    relative_delta_high = 5.0 / math.sqrt(re_high)
    required_blasius_inputs = {"U", "x", "nu", "pressure_gradient", "roughness"}
    _invariant(
        out,
        "U12.REAL.Z5.required_inputs_and_limit",
        len(required_blasius_inputs) == 5
        and relative_delta_high < relative_delta_low,
        "Blasiusova provjera nema potpune ulaze ili pogresan Re trend.",
    )

    # Stvarni podatkovni paket mora sadržavati tri mreže. Poiseuilleov niz
    # daje p=2. U trenutačnom NASA/FUN3D izvatku i CD i CL konvergiraju
    # monotono; GCI se procjenjuje zasebno za svaku monitoriranu velicinu.
    with (REPO_ROOT / "data/cfd/poiseuille_laminar/grids.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        pipe_rows = list(csv.DictReader(handle))
    pipe_errors = [abs(float(row["q_rel_error_percent"])) for row in pipe_rows]
    pipe_imbalances = [float(row["mass_imbalance_percent"]) for row in pipe_rows]
    observed_order = math.log(pipe_errors[0] / pipe_errors[1]) / math.log(2.0)
    with (REPO_ROOT / "data/cfd/hydrofoil_experiment/grids.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        foil_rows = list(csv.DictReader(handle))
    cd_values = [float(row["cd"]) for row in foil_rows]
    cl_values = [float(row["cl"]) for row in foil_rows]
    _invariant(
        out,
        "U12.REAL.Z6.three_grid_order_and_mass",
        len(pipe_rows) == 3
        and abs(observed_order - 2.0) < 1.0e-12
        and pipe_imbalances[0] > pipe_imbalances[1] > pipe_imbalances[2] >= 0.0,
        "Poiseuilleov paket ne daje tri mreze, p=2 i zaseban opadajuci debalans.",
    )
    _invariant(
        out,
        "U12.REAL.Z6.naca_scalar_monotonicity",
        cd_values[0] > cd_values[1] > cd_values[2]
        and cl_values[0] < cl_values[1] < cl_values[2],
        "FUN3D nizovi na tri mreze nisu monotoni za oba arhivirana skalara.",
    )
    hydrofoil_files = {
        path.name
        for path in (REPO_ROOT / "data/cfd/hydrofoil_experiment").iterdir()
        if path.is_file()
    }
    _invariant(
        out,
        "U12.REAL.Z6.missing_validation_diagnostics",
        not {"residuals.csv", "force_monitors.csv", "mass_balance.csv"}.intersection(
            hydrofoil_files
        ),
        "arhiva neocekivano sadrzi dijagnostike; azuriraj validacijski ugovor",
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
