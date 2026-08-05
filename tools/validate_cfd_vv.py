"""Read-only validator za nastavne CFD V&V podatke u ``data/cfd``.

Provjerava strukturu, tri mreze, masenu bilancu, reziduale, fizikalni monitor,
tro-mrezni GCI, analiticke/reference vrijednosti i provenancu. Javni profilni
arhiv provjerava se odvojeno: stvarne mjerne i FUN3D vrijednosti jesu prisutne,
a nedostupni reziduali, monitori i masena bilanca moraju ostati izricito oznaceni.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import json
import math
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_ROOT = REPO_ROOT / "data" / "cfd"
GRID_ORDER = ("coarse", "medium", "fine")
EXPECTED_CASES = {
    "poiseuille_laminar",
    "venturi_diffuser",
    "hydrofoil_experiment",
}


class Audit:
    def __init__(self) -> None:
        self.issues: list[str] = []
        self.notes: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.issues.append(message)

    def close(
        self,
        value: float,
        target: float,
        message: str,
        *,
        rel: float = 1e-8,
        abs_tol: float = 1e-12,
    ) -> None:
        if not math.isfinite(value) or not math.isclose(
            value, target, rel_tol=rel, abs_tol=abs_tol
        ):
            self.issues.append(f"{message}: {value:.12g} != {target:.12g}")


def _load_json(path: Path, audit: Audit) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        audit.issues.append(f"Nedostaje {path}")
        return {}
    except json.JSONDecodeError as exc:
        audit.issues.append(f"Nevaljan JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        audit.issues.append(f"JSON korijen nije objekt: {path}")
        return {}
    return value


def _load_csv(path: Path, audit: Audit) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            if reader.fieldnames is None:
                audit.issues.append(f"CSV nema zaglavlje: {path}")
                return []
    except FileNotFoundError:
        audit.issues.append(f"Nedostaje {path}")
        return []
    if not rows:
        audit.issues.append(f"CSV nema podatkovnih redaka: {path}")
    return rows


def _float(row: dict[str, str], key: str, where: str, audit: Audit) -> float:
    try:
        value = float(row[key])
    except (KeyError, TypeError, ValueError):
        audit.issues.append(f"{where}: nedostaje/nevaljan broj u stupcu {key}")
        return math.nan
    if not math.isfinite(value):
        audit.issues.append(f"{where}: {key} nije konacan broj")
    return value


def _safe_case_dir(data_root: Path, relative: str, audit: Audit) -> Path:
    candidate = (data_root / relative).resolve()
    root = data_root.resolve()
    audit.require(
        candidate == root or root in candidate.parents,
        f"Putanja slucaja izlazi iz data/cfd: {relative}",
    )
    return candidate


def _validate_provenance(
    case_id: str,
    case: dict[str, Any],
    provenance: dict[str, Any],
    audit: Audit,
) -> None:
    audit.require(
        provenance.get("case_id") == case_id,
        f"{case_id}: provenance case_id nije uskladen",
    )
    audit.require(
        provenance.get("data_classification") == case.get("data_classification"),
        f"{case_id}: data_classification nije uskladen s provenancom",
    )
    audit.require(
        isinstance(provenance.get("external_measurements_used"), bool),
        f"{case_id}: provenance mora navesti external_measurements_used",
    )
    limitations = provenance.get("limitations")
    audit.require(
        isinstance(limitations, list) and len(limitations) >= 2,
        f"{case_id}: provenance mora navesti barem dva ogranicenja",
    )


def _validate_grid_sequence(
    case_id: str,
    rows: list[dict[str, str]],
    acceptance: dict[str, Any],
    audit: Audit,
) -> dict[str, dict[str, str]]:
    by_grid = {row.get("grid_id", ""): row for row in rows}
    required_count = int(acceptance.get("required_grids", 3))
    audit.require(
        len(rows) == required_count == 3,
        f"{case_id}: ocekuju se tocno tri mrezna retka",
    )
    audit.require(
        set(by_grid) == set(GRID_ORDER),
        f"{case_id}: grid_id mora biti coarse/medium/fine",
    )
    if set(by_grid) != set(GRID_ORDER):
        return by_grid

    cells = [_float(by_grid[g], "cells", f"{case_id}/{g}", audit) for g in GRID_ORDER]
    sizes = [
        _float(by_grid[g], "h_over_h_fine", f"{case_id}/{g}", audit)
        for g in GRID_ORDER
    ]
    audit.require(
        cells[0] < cells[1] < cells[2],
        f"{case_id}: broj celija mora rasti coarse -> fine",
    )
    audit.require(
        sizes[0] > sizes[1] > sizes[2] > 0,
        f"{case_id}: h mora padati coarse -> fine",
    )
    if all(math.isfinite(value) and value > 0 for value in sizes):
        audit.close(
            sizes[0] / sizes[1],
            sizes[1] / sizes[2],
            f"{case_id}: omjer profinjenja nije jednolik",
            rel=1e-6,
        )

    max_imbalance = float(acceptance["max_mass_imbalance_percent"])
    for grid_id in GRID_ORDER:
        row = by_grid[grid_id]
        where = f"{case_id}/{grid_id}"
        mass_in = _float(row, "mass_flow_in_kg_s", where, audit)
        mass_out = _float(row, "mass_flow_out_kg_s", where, audit)
        reported = _float(row, "mass_imbalance_percent", where, audit)
        denominator = max(abs(mass_in), abs(mass_out))
        if denominator > 0 and all(math.isfinite(x) for x in (mass_in, mass_out)):
            calculated = 100.0 * abs(mass_in - mass_out) / denominator
            audit.close(
                reported,
                calculated,
                f"{where}: prijavljeni maseni debalans",
                rel=1e-8,
                abs_tol=1e-10,
            )
        audit.require(
            math.isfinite(reported) and reported <= max_imbalance,
            f"{where}: maseni debalans {reported} % prelazi {max_imbalance} %",
        )
    return by_grid


def _validate_history(
    case_id: str,
    rows: list[dict[str, str]],
    grid_rows: dict[str, dict[str, str]],
    case: dict[str, Any],
    audit: Audit,
) -> None:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("grid_id", "")].append(row)
    audit.require(
        set(grouped) == set(GRID_ORDER),
        f"{case_id}: history mora pokriti coarse/medium/fine",
    )
    acceptance = case["acceptance"]
    for grid_id in GRID_ORDER:
        history = grouped.get(grid_id, [])
        if not history:
            continue
        where = f"{case_id}/{grid_id}/history"
        audit.require(len(history) >= 4, f"{where}: trebaju barem cetiri zapisa")
        iterations = [int(_float(row, "iteration", where, audit)) for row in history]
        audit.require(
            all(a < b for a, b in zip(iterations, iterations[1:])),
            f"{where}: iteracije nisu strogo rastuce",
        )
        continuity = [
            _float(row, "continuity_residual_l2", where, audit) for row in history
        ]
        momentum = [
            _float(row, "momentum_residual_l2", where, audit) for row in history
        ]
        audit.require(
            all(value > 0 for value in continuity + momentum),
            f"{where}: reziduali moraju biti pozitivni",
        )
        audit.require(
            continuity[-1]
            <= float(acceptance["max_final_continuity_residual_l2"]),
            f"{where}: zavrsni rezidual kontinuiteta je previsok",
        )
        audit.require(
            momentum[-1] <= float(acceptance["max_final_momentum_residual_l2"]),
            f"{where}: zavrsni rezidual momenta je previsok",
        )
        min_orders = float(acceptance["min_residual_reduction_orders"])
        if continuity[-1] > 0 and momentum[-1] > 0:
            audit.require(
                math.log10(continuity[0] / continuity[-1]) >= min_orders,
                f"{where}: kontinuitet nije pao za {min_orders} redova",
            )
            audit.require(
                math.log10(momentum[0] / momentum[-1]) >= min_orders,
                f"{where}: moment nije pao za {min_orders} redova",
            )

        names = {row.get("primary_monitor_name", "") for row in history}
        audit.require(
            len(names) == 1 and "" not in names,
            f"{where}: mora postojati jedan imenovani fizikalni monitor",
        )
        monitors = [
            _float(row, "primary_monitor_value", where, audit) for row in history
        ]
        if len(monitors) >= 2 and monitors[-1] != 0:
            last_change = 100.0 * abs(monitors[-1] - monitors[-2]) / abs(monitors[-1])
            audit.require(
                last_change
                <= float(acceptance["max_last_monitor_change_percent"]),
                f"{where}: zadnja promjena monitora {last_change:.4g} % je previsoka",
            )

        if grid_id in grid_rows and names:
            monitor_name = next(iter(names))
            if monitor_name in grid_rows[grid_id]:
                target = _float(grid_rows[grid_id], monitor_name, where, audit)
            elif monitor_name == "q_out_m3_s" and case_id == "poiseuille_laminar":
                density = float(case["fluid_si"]["density_kg_m3"])
                target = _float(
                    grid_rows[grid_id], "mass_flow_out_kg_s", where, audit
                ) / density
            else:
                target = math.nan
                audit.issues.append(
                    f"{where}: monitor {monitor_name!r} nema vezu s grids.csv"
                )
            if math.isfinite(target):
                audit.close(
                    monitors[-1],
                    target,
                    f"{where}: zavrsni monitor nije jednak integralnom rezultatu",
                    rel=1e-8,
                    abs_tol=1e-12,
                )


def _validate_uncertainty(
    case_id: str,
    uncertainty: dict[str, Any],
    grid_rows: dict[str, dict[str, str]],
    audit: Audit,
) -> None:
    audit.require(
        uncertainty.get("case_id") == case_id,
        f"{case_id}: uncertainty case_id nije uskladen",
    )
    audit.require(
        uncertainty.get("status") == "quantified",
        f"{case_id}: uncertainty status mora biti quantified",
    )
    audit.require(
        bool(uncertainty.get("method_reference")),
        f"{case_id}: nedostaje izvor metode nesigurnosti",
    )
    audit.require(
        bool(uncertainty.get("scope")),
        f"{case_id}: nedostaje opseg nesigurnosti",
    )
    audit.require(
        isinstance(uncertainty.get("not_included"), list)
        and bool(uncertainty.get("not_included")),
        f"{case_id}: treba navesti sto nije ukljuceno u nesigurnost",
    )
    ratio = float(uncertainty.get("refinement_ratio", math.nan))
    safety = float(uncertainty.get("safety_factor", math.nan))
    audit.require(ratio > 1, f"{case_id}: refinement_ratio mora biti > 1")
    audit.require(safety >= 1, f"{case_id}: safety_factor mora biti >= 1")
    metrics = uncertainty.get("metrics")
    audit.require(
        isinstance(metrics, list) and bool(metrics),
        f"{case_id}: treba barem jedna GCI metrika",
    )
    if not isinstance(metrics, list) or not grid_rows:
        return

    for metric in metrics:
        name = metric.get("name", "")
        where = f"{case_id}/uncertainty/{name or '?'}"
        audit.require(bool(name), f"{where}: metrika nema ime")
        try:
            coarse = float(metric["coarse"])
            medium = float(metric["medium"])
            fine = float(metric["fine"])
            declared_order = float(metric["observed_order"])
            declared_gci = float(metric["gci_fine_percent"])
        except (KeyError, TypeError, ValueError):
            audit.issues.append(f"{where}: nevaljana tro-mrezna metrika")
            continue
        for grid_id, value in zip(GRID_ORDER, (coarse, medium, fine)):
            if grid_id in grid_rows and name in grid_rows[grid_id]:
                audit.close(
                    value,
                    _float(grid_rows[grid_id], name, where, audit),
                    f"{where}: vrijednost {grid_id} nije uskladena s grids.csv",
                )
            else:
                audit.issues.append(
                    f"{where}: stupac {name!r} ne postoji u grids.csv"
                )
        d32 = coarse - medium
        d21 = medium - fine
        audit.require(
            d32 * d21 > 0,
            f"{where}: niz nije monotono konvergentan",
        )
        if d21 == 0 or d32 == 0 or ratio <= 1:
            continue
        observed_order = math.log(abs(d32 / d21)) / math.log(ratio)
        denominator = ratio**observed_order - 1.0
        if fine == 0 or denominator == 0:
            audit.issues.append(f"{where}: GCI nije definiran")
            continue
        gci = safety * abs(fine - medium) / abs(fine) / abs(denominator) * 100.0
        audit.close(
            declared_order,
            observed_order,
            f"{where}: observed_order",
            rel=1e-7,
        )
        audit.close(
            declared_gci,
            gci,
            f"{where}: gci_fine_percent",
            rel=1e-7,
        )
        reference_key = (
            "analytical_value" if "analytical_value" in metric else "reference_value"
        )
        if reference_key in metric:
            reference = float(metric[reference_key])
            errors = [abs(value - reference) for value in (coarse, medium, fine)]
            audit.require(
                errors[0] > errors[1] > errors[2],
                f"{where}: pogreska prema referenci ne pada coarse -> fine",
            )
            if reference != 0 and "fine_error_vs_reference_percent" in metric:
                signed_error = 100.0 * (fine - reference) / reference
                audit.close(
                    float(metric["fine_error_vs_reference_percent"]),
                    signed_error,
                    f"{where}: fine_error_vs_reference_percent",
                    rel=1e-7,
                )


def _validate_poiseuille(
    case_dir: Path,
    case: dict[str, Any],
    grid_rows: dict[str, dict[str, str]],
    audit: Audit,
) -> None:
    geometry = case["geometry_m"]
    fluid = case["fluid_si"]
    boundary = case["boundary_conditions"]
    reference = case["analytical_reference"]
    diameter = float(geometry["diameter"])
    radius = float(geometry["radius"])
    length = float(geometry["length"])
    density = float(fluid["density_kg_m3"])
    viscosity = float(fluid["dynamic_viscosity_pa_s"])
    delta_p = float(boundary["pressure_drop_pa"])
    area = math.pi * diameter**2 / 4.0
    mean_velocity = delta_p * diameter**2 / (32.0 * viscosity * length)
    volume_flow = area * mean_velocity
    expected = {
        "area_m2": area,
        "mean_velocity_m_s": mean_velocity,
        "centerline_velocity_m_s": 2.0 * mean_velocity,
        "volume_flow_m3_s": volume_flow,
        "mass_flow_kg_s": density * volume_flow,
        "pressure_drop_pa": delta_p,
        "wall_shear_pa": 8.0 * viscosity * mean_velocity / diameter,
        "reynolds_diameter": density * mean_velocity * diameter / viscosity,
    }
    for key, target in expected.items():
        audit.close(
            float(reference[key]),
            target,
            f"poiseuille_laminar/reference/{key}",
            rel=1e-10,
        )
    audit.close(radius, diameter / 2.0, "poiseuille_laminar: radius", rel=1e-12)

    for grid_id, row in grid_rows.items():
        where = f"poiseuille_laminar/{grid_id}"
        q_grid = _float(row, "q_volume_m3_s", where, audit)
        u_grid = _float(row, "u_mean_m_s", where, audit)
        mass_in = _float(row, "mass_flow_in_kg_s", where, audit)
        delta_p_grid = _float(row, "delta_p_pa", where, audit)
        q_error = _float(row, "q_rel_error_percent", where, audit)
        audit.close(mass_in, density * q_grid, f"{where}: rho*Q", rel=1e-10)
        audit.close(u_grid, q_grid / area, f"{where}: Q/A", rel=1e-10)
        audit.close(delta_p_grid, delta_p, f"{where}: nametnuti pad tlaka")
        audit.close(
            q_error,
            100.0 * (q_grid - volume_flow) / volume_flow,
            f"{where}: relativna pogreska protoka",
            rel=1e-9,
        )

    profile_rows = _load_csv(case_dir / case["files"]["profile"], audit)
    radii: list[float] = []
    for index, row in enumerate(profile_rows, start=2):
        where = f"poiseuille_laminar/velocity_profile.csv:{index}"
        x = _float(row, "r_over_R", where, audit)
        analytic = _float(row, "u_analytic_m_s", where, audit)
        radii.append(x)
        target = 2.0 * mean_velocity * (1.0 - x**2)
        audit.close(analytic, target, f"{where}: analiticki profil", rel=1e-10)
        errors: list[float] = []
        for grid_id in GRID_ORDER:
            value = _float(row, f"u_{grid_id}_m_s", where, audit)
            errors.append(abs(value - analytic))
        if analytic != 0:
            audit.require(
                errors[0] > errors[1] > errors[2],
                f"{where}: profil ne konvergira coarse -> fine",
            )
    if radii:
        audit.close(radii[0], 0.0, "Poiseuille profil mora poceti na osi")
        audit.close(radii[-1], 1.0, "Poiseuille profil mora zavrsiti na stijenci")
        audit.require(
            all(a < b for a, b in zip(radii, radii[1:])),
            "Poiseuille r/R mora strogo rasti",
        )


def _validate_venturi(
    case: dict[str, Any],
    grid_rows: dict[str, dict[str, str]],
    audit: Audit,
) -> None:
    geometry = case["geometry_m"]
    fluid = case["fluid_si"]
    boundary = case["boundary_conditions"]
    reference = case["reference_model"]
    density = float(fluid["density_kg_m3"])
    viscosity = float(fluid["dynamic_viscosity_pa_s"])
    d_in = float(geometry["inlet_diameter"])
    d_throat = float(geometry["throat_diameter"])
    q = float(boundary["inlet_volume_flow_m3_s"])
    p_in = float(boundary["inlet_static_pressure_pa"])
    k_loss = float(reference["loss_coefficient_throat_basis"])
    a_in = math.pi * d_in**2 / 4.0
    a_throat = math.pi * d_throat**2 / 4.0
    v_in = q / a_in
    v_throat = q / a_throat
    dyn_throat = 0.5 * density * v_throat**2
    pressure_drop = 0.5 * density * (v_throat**2 - v_in**2)
    loss = k_loss * dyn_throat
    p_throat = p_in - pressure_drop
    p_out = p_in - loss
    expected = {
        "inlet_area_m2": a_in,
        "throat_area_m2": a_throat,
        "inlet_velocity_m_s": v_in,
        "throat_velocity_m_s": v_throat,
        "reynolds_inlet": density * v_in * d_in / viscosity,
        "reynolds_throat": density * v_throat * d_throat / viscosity,
        "ideal_inlet_to_throat_pressure_drop_pa": pressure_drop,
        "prescribed_total_pressure_loss_pa": loss,
        "throat_static_pressure_pa": p_throat,
        "outlet_static_pressure_pa": p_out,
        "pressure_recovery_coefficient": (p_out - p_throat) / dyn_throat,
    }
    for key, target in expected.items():
        audit.close(
            float(reference[key]),
            target,
            f"venturi_diffuser/reference/{key}",
            rel=1e-10,
        )

    for grid_id, row in grid_rows.items():
        where = f"venturi_diffuser/{grid_id}"
        dp = _float(row, "delta_p_inlet_throat_pa", where, audit)
        grid_loss = _float(row, "total_pressure_loss_pa", where, audit)
        pth = _float(row, "p_throat_pa", where, audit)
        pout = _float(row, "p_outlet_pa", where, audit)
        recovery = _float(row, "pressure_recovery_coefficient", where, audit)
        q_in = _float(row, "q_in_m3_s", where, audit)
        q_out = _float(row, "q_out_m3_s", where, audit)
        mass_in = _float(row, "mass_flow_in_kg_s", where, audit)
        mass_out = _float(row, "mass_flow_out_kg_s", where, audit)
        dp_error = _float(row, "delta_p_rel_error_percent", where, audit)
        loss_error = _float(row, "loss_rel_error_percent", where, audit)
        audit.close(mass_in, density * q_in, f"{where}: ulazni rho*Q", rel=1e-10)
        audit.close(mass_out, density * q_out, f"{where}: izlazni rho*Q", rel=1e-10)
        audit.close(pth, p_in - dp, f"{where}: tlak u grlu", rel=1e-10)
        audit.close(pout, p_in - grid_loss, f"{where}: izlazni tlak", rel=1e-10)
        audit.close(
            recovery,
            (pout - pth) / dyn_throat,
            f"{where}: koeficijent oporavka",
            rel=1e-10,
        )
        audit.close(
            dp_error,
            100.0 * (dp - pressure_drop) / pressure_drop,
            f"{where}: relativna pogreska pada tlaka",
            rel=1e-9,
        )
        audit.close(
            loss_error,
            100.0 * (grid_loss - loss) / loss,
            f"{where}: relativna pogreska gubitka",
            rel=1e-9,
        )


def _validate_placeholder(
    case_dir: Path,
    case_id: str,
    case: dict[str, Any],
    uncertainty: dict[str, Any],
    provenance: dict[str, Any],
    audit: Audit,
) -> None:
    audit.require(
        case.get("data_available") is False,
        f"{case_id}: placeholder mora imati data_available=false",
    )
    csv_files = sorted(path.name for path in case_dir.rglob("*.csv"))
    audit.require(
        not csv_files,
        f"{case_id}: placeholder ne smije sadrzavati CSV podatke: {csv_files}",
    )
    audit.require(
        uncertainty.get("status") == "not_available"
        and bool(uncertainty.get("reason")),
        f"{case_id}: mora objasniti zasto nesigurnost nije dostupna",
    )
    audit.require(
        isinstance(uncertainty.get("required_future_components"), list)
        and len(uncertainty.get("required_future_components", [])) >= 5,
        f"{case_id}: nedostaje buduci budzet mjerne nesigurnosti",
    )
    audit.require(
        provenance.get("measurements_copied") is False
        and provenance.get("curve_digitization_performed") is False,
        f"{case_id}: placeholder mora potvrditi da mjerenja nisu prepisana",
    )
    sources = provenance.get("candidate_primary_sources")
    audit.require(
        isinstance(sources, list) and len(sources) >= 1,
        f"{case_id}: treba navesti barem jedan kandidat primarnog izvora",
    )
    if isinstance(sources, list):
        for index, source in enumerate(sources, start=1):
            for field in ("title", "url", "suitability", "decision"):
                audit.require(
                    bool(source.get(field)),
                    f"{case_id}: kandidat izvora #{index} nema {field}",
                )


def _validate_reference_profile(
    case_dir: Path,
    case_id: str,
    case: dict[str, Any],
    uncertainty: dict[str, Any],
    provenance: dict[str, Any],
    audit: Audit,
) -> None:
    """Provjeri javne NASA TMR tablice bez izmisljanja nedostupnih dijagnostika."""

    audit.require(
        case.get("data_classification") == "public_reference_archive"
        and case.get("data_available") is True,
        f"{case_id}: referentni arhiv mora biti javno klasificiran i dostupan",
    )
    audit.require(
        provenance.get("external_measurements_used") is True
        and provenance.get("measurements_copied") is True
        and provenance.get("curve_digitization_performed") is False,
        f"{case_id}: provenijenca mora razlikovati tablicne podatke od digitizacije",
    )
    sources = provenance.get("sources")
    audit.require(
        isinstance(sources, list) and len(sources) >= 3,
        f"{case_id}: trebaju izvori definicije, mjerenja i CFD tablice",
    )

    grids = _load_csv(case_dir / case["files"]["grids"], audit)
    by_grid = {row.get("grid_id", ""): row for row in grids}
    audit.require(
        len(grids) == 3 and set(by_grid) == set(GRID_ORDER),
        f"{case_id}: NASA TMR izbor mora sadrzavati coarse/medium/fine",
    )
    expected = {
        "coarse": (919809.0, 1.091180300, 0.01224883495),
        "medium": (3674625.0, 1.091279297, 0.01222892955),
        "fine": (14689281.0, 1.091301077, 0.01222408822),
    }
    cl_values: list[float] = []
    cd_values: list[float] = []
    cells_values: list[float] = []
    for grid_id in GRID_ORDER:
        if grid_id not in by_grid:
            continue
        row = by_grid[grid_id]
        where = f"{case_id}/{grid_id}"
        cells = _float(row, "cells", where, audit)
        h = _float(row, "h_sqrt_inverse_cells", where, audit)
        cl = _float(row, "cl", where, audit)
        cd = _float(row, "cd", where, audit)
        cdp = _float(row, "cd_pressure", where, audit)
        cdv = _float(row, "cd_viscous", where, audit)
        target_cells, target_cl, target_cd = expected[grid_id]
        audit.close(cells, target_cells, f"{where}: izvorni broj celija")
        audit.close(cl, target_cl, f"{where}: izvorni CL", rel=1e-10)
        audit.close(cd, target_cd, f"{where}: izvorni CD", rel=1e-10)
        audit.close(h, math.sqrt(1.0 / cells), f"{where}: h=sqrt(1/N)", rel=5e-4)
        audit.close(cd, cdp + cdv, f"{where}: CD=CDp+CDv", rel=1e-9)
        audit.require(
            row.get("source_code") == "FUN3D" and row.get("grid_family") == "II",
            f"{where}: ocekivani su FUN3D rezultati obitelji II",
        )
        cells_values.append(cells)
        cl_values.append(cl)
        cd_values.append(cd)
    audit.require(
        len(cells_values) == 3 and cells_values[0] < cells_values[1] < cells_values[2],
        f"{case_id}: mreze moraju biti sustavno profinjene",
    )

    spatial = uncertainty.get("spatial_discretization", {})
    if len(cd_values) == 3:
        d32 = cd_values[0] - cd_values[1]
        d21 = cd_values[1] - cd_values[2]
        audit.require(d32 * d21 > 0, f"{case_id}: CD mora monotono konvergirati")
        if d32 * d21 > 0:
            order = math.log(abs(d32 / d21)) / math.log(2.0)
            gci = (
                1.25
                * abs(cd_values[2] - cd_values[1])
                / abs(cd_values[2])
                / (2.0**order - 1.0)
                * 100.0
            )
            cd_uncertainty = spatial.get("cd", {})
            audit.close(
                float(cd_uncertainty.get("observed_order", math.nan)),
                order,
                f"{case_id}: opazeni red CD",
                rel=1e-10,
            )
            audit.close(
                float(cd_uncertainty.get("gci_fine_percent", math.nan)),
                gci,
                f"{case_id}: GCI CD",
                rel=1e-10,
            )
    if len(cl_values) == 3:
        d32 = cl_values[0] - cl_values[1]
        d21 = cl_values[1] - cl_values[2]
        audit.require(d32 * d21 > 0, f"{case_id}: CL mora monotono konvergirati")
        if d32 * d21 > 0:
            order = math.log(abs(d32 / d21)) / math.log(2.0)
            gci = (
                1.25
                * abs(cl_values[2] - cl_values[1])
                / abs(cl_values[2])
                / (2.0**order - 1.0)
                * 100.0
            )
            cl_uncertainty = spatial.get("cl", {})
            audit.require(
                cl_uncertainty.get("gci_reported") is True,
                f"{case_id}: GCI CL mora biti prijavljen za monotoni niz",
            )
            audit.close(
                float(cl_uncertainty.get("observed_order", math.nan)),
                order,
                f"{case_id}: opazeni red CL",
                rel=1e-10,
            )
            audit.close(
                float(cl_uncertainty.get("gci_fine_percent", math.nan)),
                gci,
                f"{case_id}: GCI CL",
                rel=1e-10,
            )

    measurements = _load_csv(
        case_dir / case["files"]["experimental_forces"], audit
    )
    audit.require(
        len(measurements) == 18,
        f"{case_id}: ocekuje se 18 Ladsonovih tocaka zone 120 grit",
    )
    selected = [
        row
        for row in measurements
        if math.isclose(_float(row, "alpha_deg", case_id, audit), 10.10)
    ]
    audit.require(len(selected) == 1, f"{case_id}: nedostaje mjerna tocka 10,10 deg")
    if selected:
        row = selected[0]
        audit.close(_float(row, "cl", case_id, audit), 1.0775, f"{case_id}: Ladson CL")
        audit.close(_float(row, "cd", case_id, audit), 0.01175, f"{case_id}: Ladson CD")
        comparison = case.get("comparison_measurement", {})
        audit.close(float(comparison.get("cl", math.nan)), 1.0775, f"{case_id}: usporedni CL")
        audit.close(float(comparison.get("cd", math.nan)), 0.01175, f"{case_id}: usporedni CD")

    diagnostics = case.get("archival_diagnostics", {})
    for key in (
        "solver_residual_history_available",
        "force_monitor_history_available",
        "mass_imbalance_available",
    ):
        audit.require(
            diagnostics.get(key) is False,
            f"{case_id}: nedostupna arhivska dijagnostika {key} ne smije se izmisljati",
        )
    audit.require(
        bool(diagnostics.get("consequence"))
        and uncertainty.get("experimental_uncertainty", {}).get(
            "available_in_distributed_force_file"
        )
        is False,
        f"{case_id}: ogranicenje validacijske presude mora biti izricito",
    )


def _validate_ready_case(
    case_dir: Path,
    case_id: str,
    case: dict[str, Any],
    uncertainty: dict[str, Any],
    provenance: dict[str, Any],
    audit: Audit,
) -> None:
    audit.require(
        case.get("data_classification")
        in {"synthetic_analytic", "synthetic_pedagogical"},
        f"{case_id}: spremni nastavni slucaj mora jasno biti oznacen synthetic",
    )
    audit.require(
        provenance.get("external_measurements_used") is False,
        f"{case_id}: sinteticni slucaj ne smije tvrditi da koristi mjerenja",
    )
    audit.require(
        bool(provenance.get("created")) and bool(provenance.get("generator")),
        f"{case_id}: provenance mora navesti datum i generator",
    )
    audit.require(
        isinstance(provenance.get("construction"), dict)
        and bool(provenance.get("construction")),
        f"{case_id}: provenance mora opisati konstrukciju podataka",
    )
    grids = _load_csv(case_dir / case["files"]["grids"], audit)
    grid_rows = _validate_grid_sequence(
        case_id, grids, case.get("acceptance", {}), audit
    )
    history = _load_csv(case_dir / case["files"]["history"], audit)
    _validate_history(case_id, history, grid_rows, case, audit)
    _validate_uncertainty(case_id, uncertainty, grid_rows, audit)
    if case_id == "poiseuille_laminar":
        _validate_poiseuille(case_dir, case, grid_rows, audit)
    elif case_id == "venturi_diffuser":
        _validate_venturi(case, grid_rows, audit)


def validate(data_root: Path) -> tuple[Audit, int, int]:
    audit = Audit()
    manifest = _load_json(data_root / "manifest.json", audit)
    audit.require(
        manifest.get("schema_version") == 1,
        "data/cfd/manifest.json mora imati schema_version=1",
    )
    case_entries = manifest.get("cases")
    audit.require(isinstance(case_entries, list), "Manifest cases mora biti lista")
    if not isinstance(case_entries, list):
        return audit, 0, 0
    ids = [entry.get("case_id") for entry in case_entries]
    audit.require(len(ids) == len(set(ids)), "Manifest ima duplicirane case_id oznake")
    audit.require(
        set(ids) == EXPECTED_CASES and len(ids) == 3,
        f"Manifest mora sadrzavati tocno tri slucaja: {sorted(EXPECTED_CASES)}",
    )

    ready_count = 0
    reference_count = 0
    for entry in case_entries:
        case_id = entry.get("case_id", "?")
        status = entry.get("status")
        case_dir = _safe_case_dir(data_root, str(entry.get("path", "")), audit)
        audit.require(case_dir.is_dir(), f"{case_id}: ne postoji mapa {case_dir}")
        if status == "ready":
            required_key = "required_ready_case_files"
        elif status == "reference_ready":
            required_key = "required_reference_case_files"
        else:
            required_key = "required_placeholder_files"
        for filename in manifest.get(required_key, []):
            audit.require(
                (case_dir / filename).is_file(),
                f"{case_id}: nedostaje obvezna datoteka {filename}",
            )
        readme = case_dir / "README.md"
        if readme.is_file():
            audit.require(
                len(readme.read_text(encoding="utf-8").strip()) >= 100,
                f"{case_id}: README je prazan ili prekratak",
            )

        case = _load_json(case_dir / "case.json", audit)
        uncertainty = _load_json(case_dir / "uncertainty.json", audit)
        provenance = _load_json(case_dir / "provenance.json", audit)
        audit.require(
            case.get("case_id") == case_id,
            f"{case_id}: case.json case_id nije uskladen",
        )
        audit.require(
            case.get("status") == status,
            f"{case_id}: status manifesta i case.json nije uskladen",
        )
        _validate_provenance(case_id, case, provenance, audit)

        before = len(audit.issues)
        if status == "ready":
            ready_count += 1
            _validate_ready_case(
                case_dir, case_id, case, uncertainty, provenance, audit
            )
            detail = "3 grids, conservation/residual/monitor/GCI"
        elif status == "reference_ready":
            reference_count += 1
            _validate_reference_profile(
                case_dir, case_id, case, uncertainty, provenance, audit
            )
            detail = "public experiment + 3 FUN3D grids; archive diagnostics flagged"
        elif status == "placeholder":
            _validate_placeholder(case_dir, case_id, case, uncertainty, provenance, audit)
            detail = "placeholder, no numerical CSV"
        else:
            audit.issues.append(f"{case_id}: nepoznat status {status!r}")
            detail = f"unknown status {status!r}"
        marker = "OK" if len(audit.issues) == before else "FAIL"
        audit.notes.append(f"[{marker}] {case_id}: {detail}")

    return audit, ready_count, reference_count


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-root",
        type=Path,
        default=DEFAULT_DATA_ROOT,
        help="Alternativna data/cfd mapa za read-only provjeru.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    audit, ready_count, reference_count = validate(args.data_root.resolve())
    for note in audit.notes:
        print(note)
    print(
        f"\nCFD V&V inventory: ready={ready_count}, "
        f"reference={reference_count}, issues={len(audit.issues)}"
    )
    if audit.issues:
        for issue in audit.issues:
            print(f"  - {issue}")
        return 1
    print("STATUS: PASS (referentni profil ima javne podatke i navedene arhivske praznine)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
