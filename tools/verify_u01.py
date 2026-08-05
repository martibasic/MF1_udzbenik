"""Numericka verifikacija U01: Osnove fluida i Pascalov zakon.

Pokriva:
- Kratki primjer (T1): Gustoca, specificna tezina, relativna gustoca
- Primjer 1 (T2): Optereceni klip
- Primjer 2 (T2): Servisna hidraulicna dizalica
- Cjeloviti zadatak 1 (T3): Dvostruka platforma s rucnom pumpom
- Primjer hidraulicne kocnice i primjer robotske stege
- Zadaci za vjezbu 1-6 (T1-T4)

Svaki racun reprodukuje brojeve navedene u source/u01_*.md i verificira
da odstupanje od deklariranih vrijednosti nije vece od TOLERANCIJA (rel.).
"""
from __future__ import annotations

import math
from typing import Any

TOLERANCIJA = 0.01  # 1% relativno odstupanje zbog zaokruzivanja u tekstu


def _close(value: float, target: float, rel: float = TOLERANCIJA) -> bool:
    if target == 0:
        return abs(value) < rel
    return abs(value - target) / abs(target) <= rel


def _check(
    results: list[dict],
    rid: str,
    value: float,
    target: float,
    unit: str = "",
    rel: float = TOLERANCIJA,
) -> None:
    ok = _close(value, target, rel)
    status = "OK" if ok else "FAIL"
    details = f"{value:.4g} vs {target:.4g} {unit}".strip()
    results.append({"id": rid, "status": status, "details": "" if ok else details})


def _invariant(results: list[dict], rid: str, condition: bool, details: str) -> None:
    results.append({
        "id": rid,
        "status": "OK" if condition else "FAIL",
        "verification": "invariant",
        "details": "" if condition else details,
    })


# ------------ Kratki primjer: Gustoca ----------------
def primjer_kratki(rho: float = 860.0, g: float = 9.81, rho_voda: float = 1000.0):
    gamma = rho * g
    s_r = rho / rho_voda
    return {"gamma": gamma, "s_r": s_r}


# ------------ Primjer 1: Optereceni klip ----------------
def primjer_1(d_k: float = 0.16, G: float = 3600.0, A_2_cm2: float = 450.0):
    A_k = math.pi * d_k**2 / 4
    p = G / A_k
    A_2 = A_2_cm2 * 1e-4
    F_2 = p * A_2
    return {"A_k": A_k, "p": p, "F_2": F_2}


# ------------ Primjer 2: Servisna hidraulicna dizalica ----------------
def primjer_2(A_1_cm2: float = 6.0, A_2_cm2: float = 210.0, F_1: float = 150.0, s_1: float = 0.18):
    A_1 = A_1_cm2 * 1e-4
    A_2 = A_2_cm2 * 1e-4
    p = F_1 / A_1
    F_2 = p * A_2
    s_2 = (A_1 / A_2) * s_1
    return {"p": p, "F_2": F_2, "s_2": s_2}


# ------------ Primjer 3: Dvostruki podizac ----------------
def primjer_3(G: float = 24000.0, A_L_cm2: float = 150.0, A_p_cm2: float = 6.0, s_L: float = 0.020):
    A_L = A_L_cm2 * 1e-4
    A_p = A_p_cm2 * 1e-4
    p = G / (2 * A_L)
    F_p = p * A_p
    s_p = 2 * A_L * s_L / A_p
    return {"p": p, "F_p": F_p, "s_p": s_p}


# ------------ Cjeloviti zadatak 1: Dvostruka platforma s rucnom pumpom ----------------
def cjeloviti_1(F_p: float = 460.0, A_p_cm2: float = 5.0, A_L_cm2: float = 150.0,
                s_L: float = 0.025, s_h: float = 0.180):
    A_p = A_p_cm2 * 1e-4
    A_L = A_L_cm2 * 1e-4
    p = F_p / A_p
    F_L = p * A_L
    G = 2 * F_L
    Delta_V = 2 * A_L * s_L
    s_p_total = Delta_V / A_p
    n = math.ceil(s_p_total / s_h)
    return {"p": p, "F_L": F_L, "G": G, "s_p_total": s_p_total, "n": n}


# ------------ Primjer Presa za savijanje cijevi ----------------
def primjer_presa(d_1: float = 0.032, d_2: float = 0.128, F_1: float = 320.0, s_1: float = 0.080):
    A_1 = math.pi * d_1**2 / 4
    A_2 = math.pi * d_2**2 / 4
    omjer = A_2 / A_1
    p = F_1 / A_1
    F_2 = p * A_2
    s_2 = (A_1 / A_2) * s_1
    return {"A_1": A_1, "A_2": A_2, "omjer": omjer, "p": p, "F_2": F_2, "s_2": s_2}


# ------------ Primjer Most: hidraulicno podizanje ----------------
def primjer_most(G_total: float = 480000.0, n_pod: int = 4, d_pod: float = 0.110,
                 d_pump: float = 0.022, F_pump: float = 500.0):
    F_pod = G_total / n_pod
    A_pod = math.pi * d_pod**2 / 4
    p_min = F_pod / A_pod
    A_p = math.pi * d_pump**2 / 4
    p_p = F_pump / A_p
    return {"F_pod": F_pod, "A_pod": A_pod, "p_min": p_min, "A_p": A_p, "p_p": p_p}


def primjer_robot_stega(d_p: float = 0.014, F_p: float = 420.0,
                         d_s: float = 0.028, n: int = 6):
    A_p = math.pi * d_p**2 / 4
    A_s = math.pi * d_s**2 / 4
    p = F_p / A_p
    F_s = p * A_s
    return {"A_p": A_p, "p": p, "A_s": A_s, "F_s": F_s, "F_total": n * F_s}


# ------------ Zadaci za vjezbu ----------------
def zadatak_1(d_1: float = 0.028, d_2: float = 0.140, F_1: float = 180.0, s_1: float = 0.120):
    A_1 = math.pi * d_1**2 / 4
    A_2 = math.pi * d_2**2 / 4
    p = F_1 / A_1
    F_2 = p * A_2
    s_2 = (A_1 / A_2) * s_1
    return {"p": p, "F_2": F_2, "s_2": s_2}


def zadatak_2(d: float = 0.024, F: float = 95.0, D: float = 0.072):
    A_1 = math.pi * d**2 / 4
    A_2 = math.pi * D**2 / 4
    p = F / A_1
    F_2 = p * A_2
    return {"p": p, "F_2": F_2}


def zadatak_3(p: float = 2.4e6, d: float = 0.052, F_target: float = 8000.0):
    A = math.pi * d**2 / 4
    F = p * A
    A_new = F_target / p
    d_new = math.sqrt(4 * A_new / math.pi)
    return {"F": F, "d_new": d_new}


def zadatak_4(m: float = 1350.0, D: float = 0.095, d: float = 0.018, s: float = 0.160,
              Delta_z: float = 0.045, g: float = 9.81):
    G = m * g
    A_D = math.pi * D**2 / 4
    A_d = math.pi * d**2 / 4
    p = G / (2 * A_D)
    F_p = p * A_d
    n_continuous = 2 * A_D * Delta_z / (A_d * s)
    n_full = math.ceil(n_continuous)
    return {"p": p, "F_p": F_p, "n": n_full,
            "n_continuous": n_continuous}


def zadatak_5(d: float = 0.025, F_p: float = 420.0, D: float = 0.140, Delta_z: float = 0.030):
    A_d = math.pi * d**2 / 4
    A_D = math.pi * D**2 / 4
    p = F_p / A_d
    G = 2 * p * A_D
    s_p = 2 * A_D * Delta_z / A_d
    return {"p": p, "G": G, "s_p": s_p}


def zadatak_6(A_L_cm2: float = 95.0, d: float = 0.022, F_p: float = 360.0,
              Delta_z: float = 0.018, eta_F: float = 0.86,
              u_eta_F: float = 0.04, eta_V: float = 0.90,
              u_eta_V: float = 0.03):
    A_p = math.pi * d**2 / 4
    A_L = A_L_cm2 * 1e-4
    p = F_p / A_p
    G = 3 * p * A_L
    s_p = 3 * A_L * Delta_z / A_p
    return {
        "p": p,
        "G": G,
        "s_p": s_p,
        "G_useful": eta_F * G,
        "G_useful_min": (eta_F - u_eta_F) * G,
        "s_actual": s_p / eta_V,
        "s_actual_max": s_p / (eta_V - u_eta_V),
    }


# ------------ Faza 1.5 dodatak: Hidraulicna kocnica vozila (P T2) ----------------
def primjer_kocnica(F_n: float = 300.0, i_polug: float = 5.0, d_M: float = 0.020,
                    d_f: float = 0.035, d_r: float = 0.030):
    F_M = i_polug * F_n
    A_M = math.pi * d_M**2 / 4
    A_f = math.pi * d_f**2 / 4
    A_r = math.pi * d_r**2 / 4
    p = F_M / A_M
    F_f = p * A_f
    F_r = p * A_r
    F_uk = 2 * F_f + 2 * F_r
    k_pojacanje = F_uk / F_n
    return {"F_M": F_M, "p": p, "F_f": F_f, "F_r": F_r, "F_uk": F_uk, "k": k_pojacanje}


# ------------ Verify entry point ----------------
def verify() -> list[dict]:
    """Vrati listu rezultata. Svaki rezultat: {id, status, details}."""
    out: list[dict] = []

    # Kratki primjer
    r = primjer_kratki()
    _check(out, "U01.kratki.gamma", r["gamma"], 8437, "N/m^3")
    _check(out, "U01.kratki.s_r", r["s_r"], 0.86)

    # Primjer 1
    r = primjer_1()
    _check(out, "U01.P1.A_k", r["A_k"], 0.0201, "m^2")
    _check(out, "U01.P1.p_Pa", r["p"], 1.79e5, "Pa")
    _check(out, "U01.P1.F_2", r["F_2"], 8060, "N")

    # Primjer 2
    r = primjer_2()
    _check(out, "U01.P2.p_kPa", r["p"] / 1000, 250.0, "kPa")
    _check(out, "U01.P2.F_2", r["F_2"], 5250, "N")
    _check(out, "U01.P2.s_2_mm", r["s_2"] * 1000, 5.1, "mm")

    # Cjeloviti zadatak
    r = cjeloviti_1()
    _check(out, "U01.CH1.p_MPa", r["p"] / 1e6, 0.92, "MPa")
    _check(out, "U01.CH1.F_L", r["F_L"], 13800, "N")
    _check(out, "U01.CH1.G", r["G"], 27600, "N")
    _check(out, "U01.CH1.s_p_total_m", r["s_p_total"], 1.5, "m")
    _check(out, "U01.CH1.n", r["n"], 9, "hodova")

    # Zadaci 1-6: svaki actual ponovno se racuna iz objavljenih ulaza, a target
    # je broj objavljen u rjesenju zadatka.
    z1 = zadatak_1()
    _check(out, "U01.Z1.p_kPa", z1["p"] / 1000, 292.0, "kPa")
    _check(out, "U01.Z1.F_2_kN", z1["F_2"] / 1000, 4.5, "kN")
    _check(out, "U01.Z1.s_2_mm", z1["s_2"] * 1000, 4.8, "mm")
    z2 = zadatak_2()
    _check(out, "U01.Z2.p_kPa", z2["p"] / 1000, 210.0, "kPa")
    _check(out, "U01.Z2.F_2", z2["F_2"], 855.0, "N")
    z3 = zadatak_3()
    _check(out, "U01.Z3.F_kN", z3["F"] / 1000, 5.1, "kN")
    _check(out, "U01.Z3.d_min_mm", z3["d_new"] * 1000, 65.0, "mm")
    z4 = zadatak_4()
    _check(out, "U01.Z4.p_MPa", z4["p"] / 1e6, 0.93, "MPa")
    _check(out, "U01.Z4.F_p", z4["F_p"], 238.0, "N")
    _check(out, "U01.Z4.n", z4["n"], 16.0, "hodova")
    z5 = zadatak_5()
    _check(out, "U01.Z5.p_kPa", z5["p"] / 1000, 856.0, "kPa")
    _check(out, "U01.Z5.G_kN", z5["G"] / 1000, 26.3, "kN")
    _check(out, "U01.Z5.s_p", z5["s_p"], 1.88, "m")
    z6 = zadatak_6()
    _check(out, "U01.Z6.p_kPa", z6["p"] / 1000, 947.0, "kPa")
    _check(out, "U01.Z6.G_kN", z6["G"] / 1000, 27.0, "kN")
    _check(out, "U01.Z6.s_p", z6["s_p"], 1.35, "m")
    _check(out, "U01.Z6.G_useful_kN", z6["G_useful"] / 1000, 23.2, "kN")
    _check(out, "U01.Z6.G_useful_min_kN", z6["G_useful_min"] / 1000, 22.1, "kN")
    _check(out, "U01.Z6.s_actual", z6["s_actual"], 1.50, "m")
    _check(out, "U01.Z6.s_actual_max", z6["s_actual_max"], 1.55, "m")
    _invariant(
        out,
        "U01.Z6.both_requirements",
        z6["G_useful_min"] >= 22e3 and z6["s_actual_max"] <= 1.60,
        "Konzervativni omotac ne zadovoljava oba zahtjeva.",
    )

    area_ratio = (0.140 / 0.028) ** 2
    _invariant(
        out,
        "U01.INV.pascal_force_ratio",
        abs(z1["F_2"] / 180.0 - area_ratio) < 1e-12,
        "F2/F1 nije jednak A2/A1.",
    )
    volume_residual = (
        math.pi * 0.028**2 / 4 * 0.120
        - math.pi * 0.140**2 / 4 * z1["s_2"]
    )
    _invariant(
        out,
        "U01.INV.volume_balance",
        abs(volume_residual) < 1e-15,
        f"Volumna bilanca klipova ima ostatak {volume_residual:.6g} m^3.",
    )
    _invariant(
        out,
        "U01.INV.full_stroke_ceiling",
        z4["n"] - 1 < z4["n_continuous"] <= z4["n"],
        "Broj punih hodova nije strop kontinuiranog broja hodova.",
    )

    # Faza 1.5: Hidraulicna kocnica vozila
    r = primjer_kocnica()
    _check(out, "U01.kocnica.F_M", r["F_M"], 1500, "N")
    _check(out, "U01.kocnica.p_MPa", r["p"] / 1e6, 4.77, "MPa")
    _check(out, "U01.kocnica.F_f_kN", r["F_f"] / 1000, 4.590, "kN")
    _check(out, "U01.kocnica.F_r_kN", r["F_r"] / 1000, 3.375, "kN")
    _check(out, "U01.kocnica.k", r["k"], 53.1)

    r = primjer_robot_stega()
    _check(out, "U01.robot.A_p", r["A_p"], 1.539e-4, "m2", rel=0.02)
    _check(out, "U01.robot.p_MPa", r["p"] / 1e6, 2.73, "MPa", rel=0.02)
    _check(out, "U01.robot.A_s", r["A_s"], 6.158e-4, "m2", rel=0.02)
    _check(out, "U01.robot.F_s_kN", r["F_s"] / 1000, 1.680, "kN", rel=0.02)
    _check(out, "U01.robot.F_total_kN", r["F_total"] / 1000, 10.08, "kN", rel=0.02)

    return out


if __name__ == "__main__":
    results = verify()
    ok = sum(1 for r in results if r["status"] == "OK")
    fail = sum(1 for r in results if r["status"] != "OK")
    for r in results:
        marker = "v" if r["status"] == "OK" else "x"
        print(f"  [{marker}] {r['id']:25s}  {r.get('details', '')}")
    print()
    print(f"Total: ok={ok}, fail={fail}")
