"""Pokreni sve numericke provjere i iskreno izvijesti o pokrivenosti.

Runner ukljucuje regresijski niz modula U01--U14, pet zasebnih kanonskih modula,
strukturni audit verifiera, fizikalne golden invarijante i zatvoreni manifest
pokrivenosti. Rupa, self-comparison tautologija, nestabilan task anchor ili
numericki FAIL ruse CI.

Pokretanje:
    python tools/verify_all.py
"""

from __future__ import annotations

import importlib
import json
from pathlib import Path
import sys
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS = REPO_ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import qa_audit  # noqa: E402  (tools/ je namjerno dodan u sys.path)
import verify_physics  # noqa: E402


LEGACY_CHAPTERS = [f"u{i:02d}" for i in range(1, 15)]


def _print_failures(results: list[dict[str, Any]]) -> None:
    for result in results:
        if result.get("status") != "OK":
            print(f"           - {result.get('id', '?')}: {result.get('details', '')}")


def run() -> int:
    infrastructure_issues: list[str] = []
    missing: list[str] = []
    all_results: list[dict[str, Any]] = []

    try:
        manifest = qa_audit.load_manifest()
        static_report = qa_audit.audit_static(manifest)
        infrastructure_issues.extend(static_report["issues"])
    except (OSError, json.JSONDecodeError, qa_audit.ManifestError) as exc:
        print(f"verify_all: manifest ERROR: {exc}")
        return 1

    manifest_chapters = [item["id"].lower() for item in manifest["chapters"]]
    if manifest_chapters != LEGACY_CHAPTERS:
        infrastructure_issues.append(
            "LEGACY_CHAPTERS i manifest nisu uskladeni: "
            f"{LEGACY_CHAPTERS} != {manifest_chapters}"
        )

    supplemental = manifest.get("supplemental_chapters", [])
    verifier_chapters = [*manifest["chapters"], *supplemental]

    print(
        f"verify_all: scanning {len(verifier_chapters)} numeric modules "
        f"({len(LEGACY_CHAPTERS)} legacy + {len(supplemental)} new-source); "
        "declared chapters without module="
        f"{len(manifest.get('known_unverified_chapters', []))}\n"
    )
    for chapter in verifier_chapters:
        chapter_code = chapter["id"].lower()
        module_name = chapter["module"]
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError as exc:
            if exc.name == module_name:
                missing.append(chapter_code)
            else:
                infrastructure_issues.append(
                    f"{chapter['id']}: modulu nedostaje ovisnost {exc.name!r}."
                )
            print(f"  [{chapter_code}]  IMPORT ERROR: {exc}")
            continue
        except Exception as exc:  # pragma: no cover - zastita CI runnera
            infrastructure_issues.append(
                f"{chapter['id']}: import {module_name} nije uspio: "
                f"{type(exc).__name__}: {exc}"
            )
            print(f"  [{chapter_code}]  IMPORT ERROR: {type(exc).__name__}: {exc}")
            continue

        if not hasattr(module, "verify"):
            infrastructure_issues.append(f"{module_name} nema verify().")
            print(f"  [{chapter_code}]  ERROR    (nema verify())")
            continue

        try:
            results = module.verify()
        except Exception as exc:  # pragma: no cover - zastita CI runnera
            infrastructure_issues.append(
                f"{chapter['id']}: verify() se srusio: {type(exc).__name__}: {exc}"
            )
            print(f"  [{chapter_code}]  CRASH    {type(exc).__name__}: {exc}")
            continue

        if not isinstance(results, list):
            infrastructure_issues.append(f"{module_name}.verify() nije vratio listu.")
            print(f"  [{chapter_code}]  ERROR    (verify() nije lista)")
            continue

        all_results.extend(results)
        chapter_failures = [
            result for result in results
            if not isinstance(result, dict) or result.get("status") != "OK"
        ]
        status = "OK" if not chapter_failures else "FAIL"
        print(
            f"  [{chapter_code}]  {status:7s}  "
            f"raw_checks={len(results)}  fail={len(chapter_failures)}"
        )
        _print_failures([item for item in chapter_failures if isinstance(item, dict)])

    try:
        physics_results = verify_physics.verify()
    except Exception as exc:  # pragma: no cover - zastita CI runnera
        physics_results = []
        infrastructure_issues.append(
            f"verify_physics se srusio: {type(exc).__name__}: {exc}"
        )

    physics_failures = [
        result for result in physics_results if result.get("status") != "OK"
    ]
    result_report = qa_audit.audit_results(manifest, all_results)
    infrastructure_issues.extend(result_report["issues"])
    numeric_failures = result_report["failed"]

    print("\nCoverage (ne mjesati s brojem sirovih PASS zapisa):")
    print(
        "  Canonical public task contracts:      "
        f"{static_report['canonical_task_count']}/90 (manifest schema v2)"
    )
    print(f"  Raw chapter results:                 {result_report['raw_result_count']}")
    print(
        "  Hard-coded target comparisons:       "
        f"{result_report['golden_result_count']}"
    )
    print(
        "  Dimension / limit / invariant checks: "
        f"{result_report['invariant_result_count']}"
    )
    print(
        "  Self-comparison results (UNVERIFIED): "
        f"{result_report['gap_result_count']}"
    )
    print(f"  Independent physics golden checks:   {len(physics_results)}")
    print(
        "  Declared exercise coverage gaps:      "
        f"{result_report['declared_exercise_gaps']}"
    )
    print(
        "  Declared modern-example gaps:         "
        f"{result_report['declared_example_gaps']}"
    )
    print(
        "  New chapters without verify module:   "
        f"{result_report['declared_chapter_gaps']}"
    )
    print(
        "  Known tautological code locations:    "
        f"{len(static_report['self_comparisons'])}"
    )

    if numeric_failures:
        print("\nNumericki FAIL:")
        for result in numeric_failures:
            print(f"  - {result.get('id', '?')}: {result.get('details', '')}")
    if physics_failures:
        print("\nPhysics golden FAIL:")
        for result in physics_failures:
            print(f"  - {result['id']}: {result.get('details', '')}")
    if infrastructure_issues:
        print("\nQA infrastructure FAIL:")
        for issue in infrastructure_issues:
            print(f"  - {issue}")
    if missing:
        print(f"\nMissing modules: {', '.join(missing)}")

    failed = bool(
        numeric_failures
        or physics_failures
        or infrastructure_issues
        or missing
    )
    if failed:
        print("\nSTATUS: FAIL")
        return 1

    print(
        "\nSTATUS: PASS -- nema numerickih FAIL-ova, self-comparison "
        "tautologija ni deklariranih rupa."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
