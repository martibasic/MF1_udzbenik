"""Strukturni audit numerickih provjera i njihove stvarne pokrivenosti.

Ovaj modul namjerno razlikuje tri razine:

* ``golden``: izracun se usporeduje s neovisnom, deklariranom vrijednoscu;
* ``invariant``: provjerava se samo fizikalno/matematicko svojstvo;
* ``gap``: postoji kod ili rezultat, ali nema neovisne provjere odgovora.

Self-comparison tautologije i neklasificirane rupe nisu prihvatljiv dug: audit
ih otkriva staticki i release provjera mora pasti dok ih se ne zamijeni stvarnim
golden rezultatom ili postenim fizikalnim invarijantnim ugovorom.
"""

from __future__ import annotations

import ast
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any, Iterable

import generate_verification_manifest as manifest_generator


REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = Path(__file__).with_name("verification_manifest.json")
RESULT_ID_RE = re.compile(r"^(?:U\d{2}|QA)\.[A-Za-z0-9_.-]+$")
EXERCISE_ID_RE = re.compile(
    r"^((?:U\d{2})(?:\.[A-Z][A-Z0-9_-]*)*)\.(Z\d+)(?:\.|$)"
)
EXPECTED_SUPPLEMENTAL_CHAPTERS = [
    "U05.CANON",
    "U09.COMP",
    "U12.REAL",
    "U13.CANON",
    "U15",
]
EXPECTED_EXERCISES = {f"Z{index}" for index in range(1, 7)}
TASK_ANCHOR_RE = re.compile(r"\{#(task-[A-Za-z0-9_-]+)")


class ManifestError(ValueError):
    """Manifest je sintakticki valjan JSON, ali semanticki nije potpun."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ManifestError(message)


def _validate_provenance(value: Any, label: str) -> None:
    _require(isinstance(value, dict), f"{label}: provenance mora biti objekt.")
    _require(
        isinstance(value.get("kind"), str) and bool(value["kind"].strip()),
        f"{label}: provenance.kind mora biti neprazan tekst.",
    )
    _require(
        isinstance(value.get("line"), int) and value["line"] > 0,
        f"{label}: provenance.line mora biti pozitivan cijeli broj.",
    )


def _validate_canonical_tasks(data: dict[str, Any]) -> None:
    chapters = data.get("canonical_chapters")
    _require(
        chapters == manifest_generator.CANONICAL_CHAPTERS,
        "canonical_chapters ne odgovara kanonskoj migracijskoj tablici generatora.",
    )
    tasks = data.get("canonical_tasks")
    _require(isinstance(tasks, list), "canonical_tasks mora biti lista.")
    _require(len(tasks) == 90, f"canonical_tasks mora imati 90 zapisa; nađeno {len(tasks)}.")

    expected_chapters = [f"U{index:02d}" for index in range(1, 16)]
    chapter_counts: Counter[str] = Counter()
    chapter_levels: dict[str, Counter[str]] = {
        chapter: Counter() for chapter in expected_chapters
    }
    task_ids: list[str] = []
    result_ids: list[str] = []
    module_inventory = {
        item["module"]: item["id"]
        for item in [*data.get("chapters", []), *data.get("supplemental_chapters", [])]
    }
    chapter_contracts = {item["id"]: item for item in chapters}

    for index, task in enumerate(tasks, start=1):
        label = f"canonical_tasks[{index}]"
        _require(isinstance(task, dict), f"{label} mora biti objekt.")
        task_id = task.get("id")
        _require(
            isinstance(task_id, str) and re.fullmatch(r"task-[A-Za-z0-9_-]+", task_id) is not None,
            f"{label}.id nije stabilni task-* ID: {task_id!r}.",
        )
        task_ids.append(task_id)
        chapter = task.get("chapter")
        _require(chapter in expected_chapters, f"{task_id}: nevaljano javno poglavlje {chapter!r}.")
        chapter_counts[chapter] += 1
        ordinal = task.get("ordinal")
        _require(
            isinstance(ordinal, int) and 1 <= ordinal <= 6,
            f"{task_id}: ordinal mora biti 1--6.",
        )
        level = task.get("level")
        _require(level in {"T1", "T2", "T3", "T4"}, f"{task_id}: nevaljana razina {level!r}.")
        chapter_levels[chapter][level] += 1

        source = task.get("source")
        _require(isinstance(source, dict), f"{task_id}: source mora biti objekt.")
        expected_source = chapter_contracts[chapter]["source"]
        _require(source.get("path") == expected_source, f"{task_id}: pogrešan source.path.")
        _require(
            isinstance(source.get("line"), int) and source["line"] > 0,
            f"{task_id}: source.line mora biti pozitivan cijeli broj.",
        )
        _require(source.get("anchor") == f"#{task_id}", f"{task_id}: source.anchor nije usklađen.")

        statement = task.get("statement")
        _require(isinstance(statement, dict), f"{task_id}: statement mora biti objekt.")
        markdown = statement.get("markdown")
        _require(isinstance(markdown, str) and bool(markdown.strip()), f"{task_id}: nedostaje tekst zadatka.")
        _require(statement.get("authoritative") is True, f"{task_id}: statement mora biti autoritativan.")
        expected_hash = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
        _require(statement.get("sha256") == expected_hash, f"{task_id}: statement.sha256 nije valjan.")

        inputs = task.get("input_data")
        _require(isinstance(inputs, dict), f"{task_id}: input_data mora biti objekt.")
        _require(inputs.get("parse_status") == "conservative_partial", f"{task_id}: nepoznat parse_status.")
        _require(inputs.get("authoritative_fallback") == "statement.markdown", f"{task_id}: nema autoritativni fallback.")
        _require(isinstance(inputs.get("scalars"), list), f"{task_id}: scalars mora biti lista.")
        _require(
            bool(inputs["scalars"]),
            f"{task_id}: samostalni zadatak nema nijedan parsirani brojčani ulaz; "
            "konceptualni cilj mora biti vezan uz potpuno zadani problemski slučaj.",
        )
        _require(
            isinstance(inputs.get("unparsed_numeric_math"), list)
            and all(isinstance(item, str) and item for item in inputs["unparsed_numeric_math"]),
            f"{task_id}: unparsed_numeric_math mora biti lista nepraznih tekstova.",
        )
        for scalar_index, scalar in enumerate(inputs["scalars"], start=1):
            scalar_label = f"{task_id}.scalar[{scalar_index}]"
            _require(isinstance(scalar, dict), f"{scalar_label} mora biti objekt.")
            _require(
                scalar.get("symbol") is None or isinstance(scalar.get("symbol"), str),
                f"{scalar_label}: symbol mora biti tekst ili null.",
            )
            _require(
                isinstance(scalar.get("value"), (int, float)) and math.isfinite(scalar["value"]),
                f"{scalar_label}: value mora biti konačan broj.",
            )
            _require(
                isinstance(scalar.get("normalized_unit"), str) and bool(scalar["normalized_unit"]),
                f"{scalar_label}: nedostaje jedinica ili oznaka '1'.",
            )
            _require(
                scalar.get("provenance") == "task_statement_inline_math",
                f"{scalar_label}: nevaljana provenijencija.",
            )
            si = scalar.get("si")
            if si is None:
                _require(
                    isinstance(scalar.get("si_note"), str) and bool(scalar["si_note"]),
                    f"{scalar_label}: si=null zahtijeva objašnjenje.",
                )
            else:
                _require(isinstance(si, dict), f"{scalar_label}: si mora biti objekt ili null.")
                _require(
                    isinstance(si.get("value"), (int, float)) and math.isfinite(si["value"]),
                    f"{scalar_label}: si.value mora biti konačan broj.",
                )
                _require(
                    isinstance(si.get("unit"), str) and bool(si["unit"]),
                    f"{scalar_label}: si.unit mora biti neprazan.",
                )

        assumptions = task.get("assumptions")
        _require(isinstance(assumptions, dict), f"{task_id}: assumptions mora biti objekt.")
        for assumption_kind in ("explicit", "defaults"):
            items = assumptions.get(assumption_kind)
            _require(isinstance(items, list), f"{task_id}: assumptions.{assumption_kind} mora biti lista.")
            for item_index, item in enumerate(items, start=1):
                item_label = f"{task_id}.assumptions.{assumption_kind}[{item_index}]"
                _require(isinstance(item, dict), f"{item_label} mora biti objekt.")
                _require(isinstance(item.get("text"), str) and bool(item["text"]), f"{item_label}: nema teksta.")
                _validate_provenance(item.get("provenance"), item_label)
        expected_explicit_status = (
            "declared_and_extracted"
            if assumptions["explicit"]
            else "none_identified_in_statement_or_hint"
        )
        expected_default_status = (
            "declared_in_chapter_exercise_preamble"
            if assumptions["defaults"]
            else "none_declared_in_chapter_exercise_preamble"
        )
        _require(
            assumptions.get("explicit_status") == expected_explicit_status,
            f"{task_id}: explicit_status nije usklađen sa zapisima.",
        )
        _require(
            assumptions.get("default_status") == expected_default_status,
            f"{task_id}: default_status nije usklađen sa zapisima.",
        )
        _require(
            isinstance(assumptions.get("provenance_policy"), str)
            and bool(assumptions["provenance_policy"]),
            f"{task_id}: nedostaje assumptions.provenance_policy.",
        )

        control = task.get("published_control")
        _require(isinstance(control, dict), f"{task_id}: published_control mora biti objekt.")
        _require(control.get("kind") in {"numeric", "invariant_criterion"}, f"{task_id}: nevaljan control.kind.")
        control_provenance = control.get("provenance")
        _require(isinstance(control_provenance, dict), f"{task_id}: control provenance mora biti objekt.")
        _require(control_provenance.get("path") == expected_source, f"{task_id}: control provenance path nije usklađen.")
        _require(
            isinstance(control_provenance.get("line"), int) and control_provenance["line"] > 0,
            f"{task_id}: control provenance line nije valjan.",
        )

        verifier = task.get("verifier")
        _require(isinstance(verifier, dict), f"{task_id}: verifier mora biti objekt.")
        chapter_contract = chapter_contracts[chapter]
        module = verifier.get("module")
        _require(module == chapter_contract["verifier_module"], f"{task_id}: pogrešan verifier modul.")
        _require(module in module_inventory, f"{task_id}: verifier modul nije u inventaru 19 modula.")
        expected_exercise = f"{chapter_contract['verifier_namespace']}.Z{ordinal}"
        _require(verifier.get("exercise_id") == expected_exercise, f"{task_id}: pogrešan verifier.exercise_id.")
        contracts = verifier.get("result_contracts")
        ids = verifier.get("result_ids")
        _require(isinstance(contracts, list) and bool(contracts), f"{task_id}: nema result_contracts.")
        _require(isinstance(ids, list) and bool(ids), f"{task_id}: nema result_ids.")
        contract_ids = [item.get("result_id") for item in contracts if isinstance(item, dict)]
        _require(contract_ids == ids, f"{task_id}: result_ids i result_contracts nisu usklađeni.")
        _require(len(ids) == len(set(ids)), f"{task_id}: duplicirani result-ID-jevi.")
        _require(
            all(isinstance(result_id, str) and result_id.startswith(expected_exercise + ".") for result_id in ids),
            f"{task_id}: result-ID izlazi iz pripadajućega exercise namespacea.",
        )
        result_ids.extend(ids)
        golden_contracts = [item for item in contracts if item.get("verification") == "golden"]
        invariant_contracts = [item for item in contracts if item.get("verification") == "invariant"]
        _require(len(golden_contracts) + len(invariant_contracts) == len(contracts), f"{task_id}: nepoznata klasifikacija rezultata.")
        _require(
            bool(golden_contracts),
            f"{task_id}: samostalni zadatak nema neovisnu usporedbu s fiksnim "
            "objavljenim rezultatom; same invarijante ne dokazuju da je postavka potpuna.",
        )
        expected_classification = "golden" if golden_contracts else "invariant"
        _require(verifier.get("classification") == expected_classification, f"{task_id}: pogrešna klasifikacija.")
        if golden_contracts:
            _require(control.get("kind") == "numeric" and isinstance(control.get("markdown"), str) and bool(control["markdown"]), f"{task_id}: golden zadatak mora imati objavljeni kontrolni rezultat.")
            tolerance = task.get("tolerance")
            _require(isinstance(tolerance, dict) and tolerance.get("kind") == "per_result", f"{task_id}: golden zadatak mora imati per-result tolerancije.")
            tolerance_ids = [item.get("result_id") for item in tolerance.get("contracts", []) if isinstance(item, dict)]
            _require(tolerance_ids == [item["result_id"] for item in golden_contracts], f"{task_id}: tolerancije ne pokrivaju sve golden rezultate.")
            for contract in golden_contracts:
                _require(isinstance(contract.get("unit"), str) and bool(contract["unit"]), f"{contract.get('result_id')}: nedostaje jedinični ugovor.")
                tol = contract.get("tolerance")
                _require(isinstance(tol, dict) and tol.get("kind") in {"relative", "absolute"}, f"{contract.get('result_id')}: nevaljana tolerancija.")
                _require(isinstance(tol.get("value"), (int, float)) and tol["value"] >= 0, f"{contract.get('result_id')}: tolerancija nije nenegativan broj.")
        else:
            _require(control.get("kind") == "invariant_criterion", f"{task_id}: invarijantni zadatak mora imati kriterij.")
            _require(
                bool(control.get("markdown")) or bool(control.get("reason_if_absent")),
                f"{task_id}: nedostaje objavljeni kriterij ili razlog izostanka broja.",
            )
            tolerance = task.get("tolerance")
            _require(isinstance(tolerance, dict) and tolerance.get("kind") == "not_numeric" and bool(tolerance.get("reason")), f"{task_id}: invarijantni zadatak mora objasniti zašto nema numeričku toleranciju.")
        for contract in invariant_contracts:
            _require(bool(contract.get("criterion_expression")), f"{contract.get('result_id')}: nedostaje izvršni kriterij.")

        independent = task.get("independent_check")
        _require(isinstance(independent, dict), f"{task_id}: independent_check mora biti objekt.")
        _require(
            independent.get("kind") in {"executed_invariant", "independent_recalculation_with_unit_contract"},
            f"{task_id}: nepoznata vrsta independent_check.",
        )
        independent_ids = independent.get("verifier_result_ids")
        _require(isinstance(independent_ids, list) and bool(independent_ids), f"{task_id}: independent_check nema result-ID-jeve.")
        _require(set(independent_ids).issubset(ids), f"{task_id}: independent_check navodi tuđe result-ID-jeve.")
        if invariant_contracts:
            _require(independent.get("kind") == "executed_invariant", f"{task_id}: postojeće invarijante moraju biti primarni neovisni ugovor.")
        else:
            _require(independent.get("kind") == "independent_recalculation_with_unit_contract", f"{task_id}: golden zadatak mora imati jedinični cross-check.")

    _require(len(task_ids) == len(set(task_ids)), "canonical_tasks sadrži duplicirane javne task ID-jeve.")
    _require(len(result_ids) == len(set(result_ids)), "Jedan verifier result-ID pripisan je više javnih zadataka.")
    _require(chapter_counts == Counter({chapter: 6 for chapter in expected_chapters}), f"Svako javno poglavlje mora imati šest zadataka: {chapter_counts}.")
    expected_levels = Counter({"T1": 2, "T2": 2, "T3": 1, "T4": 1})
    for chapter, levels in chapter_levels.items():
        _require(levels == expected_levels, f"{chapter}: pogrešna matrica razina {dict(levels)}.")


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 2:
        raise ManifestError("Podrzan je samo schema_version=2.")

    chapters = data.get("chapters")
    if not isinstance(chapters, list):
        raise ManifestError("Polje 'chapters' mora biti lista.")

    chapter_ids = [item.get("id") for item in chapters]
    expected = [f"U{i:02d}" for i in range(1, 15)]
    if chapter_ids != expected:
        raise ManifestError(
            f"Poglavlja moraju biti tocno {expected}; pronadeno je {chapter_ids}."
        )

    supplemental = data.get("supplemental_chapters")
    if not isinstance(supplemental, list):
        raise ManifestError("Polje 'supplemental_chapters' mora biti lista.")
    supplemental_ids = [item.get("id") for item in supplemental]
    if supplemental_ids != EXPECTED_SUPPLEMENTAL_CHAPTERS:
        raise ManifestError(
            "Dodatni verifieri moraju biti tocno "
            f"{EXPECTED_SUPPLEMENTAL_CHAPTERS}; pronadeno je {supplemental_ids}."
        )

    all_ids = chapter_ids + supplemental_ids
    if len(all_ids) != len(set(all_ids)):
        raise ManifestError("Oznake poglavlja/verifiera moraju biti jedinstvene.")

    for chapter in supplemental:
        required = chapter.get("published_numeric_results")
        if not isinstance(required, list) or not required:
            raise ManifestError(
                f"{chapter['id']}: 'published_numeric_results' mora biti neprazna lista."
            )
        if len(required) != len(set(required)):
            raise ManifestError(
                f"{chapter['id']}: duplicirani published_numeric_results."
            )
        invalid = [
            result_id for result_id in required
            if not isinstance(result_id, str)
            or not result_id.startswith(f"{chapter['id']}.")
            or not RESULT_ID_RE.fullmatch(result_id)
        ]
        if invalid:
            raise ManifestError(
                f"{chapter['id']}: nevaljane oznake objavljenih rezultata: {invalid}"
            )
        example_groups = chapter.get("published_example_groups")
        if not isinstance(example_groups, list) or not example_groups:
            raise ManifestError(
                f"{chapter['id']}: 'published_example_groups' mora biti neprazna lista."
            )
        if len(example_groups) != len(set(example_groups)) or any(
            not isinstance(group, str) or not re.fullmatch(r"P\d+", group)
            for group in example_groups
        ):
            raise ManifestError(
                f"{chapter['id']}: nevaljane ili duplicirane grupe primjera."
            )

    for chapter in [*chapters, *supplemental]:
        coverage = chapter.get("exercise_coverage")
        if not isinstance(coverage, dict):
            raise ManifestError(f"{chapter['id']}: nedostaje exercise_coverage.")
        declared_exercises: list[str] = []
        for level in ("golden", "invariant", "gap"):
            items = coverage.get(level)
            if not isinstance(items, list):
                raise ManifestError(
                    f"{chapter['id']}: exercise_coverage.{level} mora biti lista."
                )
            declared_exercises.extend(items)
        if set(declared_exercises) != EXPECTED_EXERCISES or len(
            declared_exercises
        ) != len(EXPECTED_EXERCISES):
            raise ManifestError(
                f"{chapter['id']}: ocekuju se tocno Z1--Z6, dobiveno "
                f"{declared_exercises}."
            )
        if coverage.get("gap") or coverage.get("missing_checks"):
            raise ManifestError(
                f"{chapter['id']}: release manifest ne smije sadrzavati rupe."
            )
        anchors = chapter.get("exercise_anchors")
        if not isinstance(anchors, list) or len(anchors) != 6:
            raise ManifestError(
                f"{chapter['id']}: exercise_anchors mora sadrzavati sest ID-jeva."
            )
        if len(anchors) != len(set(anchors)) or any(
            not isinstance(anchor, str) or not anchor.startswith("task-")
            for anchor in anchors
        ):
            raise ManifestError(
                f"{chapter['id']}: exercise_anchors nisu jedinstveni stabilni ID-jevi."
            )

    if data.get("known_unverified_examples"):
        raise ManifestError("Release manifest ne smije imati neprovjerene primjere.")
    if data.get("known_unverified_chapters"):
        raise ManifestError("Release manifest ne smije imati neprovjerena poglavlja.")
    generation = data.get("generation")
    if not isinstance(generation, dict) or generation.get("generated_fields") != [
        "chapters[].exercise_coverage",
        "chapters[].published_numeric_results",
        "supplemental_chapters[].exercise_coverage",
        "supplemental_chapters[].published_numeric_results",
        "canonical_chapters",
        "canonical_tasks",
    ]:
        raise ManifestError("Nedostaje ugovor generatora za canonical_tasks.")
    _validate_canonical_tasks(data)
    return data


def _verifier_chapters(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return [*manifest["chapters"], *manifest.get("supplemental_chapters", [])]


def _same_expression(left: ast.AST, right: ast.AST) -> bool:
    return ast.dump(left, include_attributes=False) == ast.dump(
        right, include_attributes=False
    )


def find_self_comparisons(path: Path) -> list[dict[str, Any]]:
    """Pronadi pozive ``_check(..., x, x, ...)`` bez izvrsavanja modula."""

    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    findings: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or len(node.args) < 4:
            continue
        if not isinstance(node.func, ast.Name) or node.func.id != "_check":
            continue
        if not _same_expression(node.args[2], node.args[3]):
            continue
        findings.append(
            {
                "line": node.lineno,
                "id_expression": ast.unparse(node.args[1]),
                "value_expression": ast.unparse(node.args[2]),
            }
        )
    return sorted(findings, key=lambda item: item["line"])


def _exercise_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    mapping: dict[str, dict[str, Any]] = {}
    valid_levels = ("golden", "invariant", "gap")
    for chapter in _verifier_chapters(manifest):
        coverage = chapter.get("exercise_coverage", {})
        missing = set(coverage.get("missing_checks", []))
        seen_local: set[str] = set()
        for level in valid_levels:
            for short_id in coverage.get(level, []):
                if not re.fullmatch(r"Z\d+", short_id):
                    raise ManifestError(
                        f"Nevaljana oznaka zadatka {chapter['id']}.{short_id}."
                    )
                if short_id in seen_local:
                    raise ManifestError(
                        f"Zadatak {chapter['id']}.{short_id} naveden je vise puta."
                    )
                seen_local.add(short_id)
                stable_id = f"{chapter['id']}.{short_id}"
                mapping[stable_id] = {
                    "level": level,
                    "check_expected": short_id not in missing,
                }
        unknown_missing = missing - seen_local
        if unknown_missing:
            raise ManifestError(
                f"{chapter['id']}: missing_checks nisu u coverage popisu: "
                f"{sorted(unknown_missing)}"
            )
    return mapping


def audit_static(manifest: dict[str, Any]) -> dict[str, Any]:
    """Provjeri datoteke, izvore, notebook inventar i AST tautologije."""

    issues: list[str] = []
    self_findings: list[dict[str, Any]] = []

    _exercise_map(manifest)

    try:
        expected_tasks = manifest_generator.build_canonical_tasks(manifest)
    except (OSError, SyntaxError, ValueError) as exc:
        expected_tasks = []
        issues.append(f"Generiranje canonical_tasks nije uspjelo: {exc}")
    if expected_tasks and manifest.get("canonical_tasks") != expected_tasks:
        issues.append(
            "canonical_tasks je zastario u odnosu na javne izvore ili AST verifiera; "
            "pokreni python tools/generate_verification_manifest.py --write."
        )

    for chapter in _verifier_chapters(manifest):
        source = REPO_ROOT / chapter["source"]
        module_path = REPO_ROOT / "tools" / f"{chapter['module']}.py"
        if not source.is_file():
            issues.append(f"{chapter['id']}: nedostaje izvor {chapter['source']}")
        else:
            source_text = source.read_text(encoding="utf-8")
            actual_anchors = TASK_ANCHOR_RE.findall(source_text)
            expected_anchors = chapter["exercise_anchors"]
            if actual_anchors != expected_anchors:
                issues.append(
                    f"{chapter['id']}: task anchori izvora ne odgovaraju manifestu; "
                    f"ocekivano {expected_anchors}, pronadeno {actual_anchors}."
                )
        if not module_path.is_file():
            issues.append(f"{chapter['id']}: nedostaje modul {module_path.name}")
            continue

        actual = find_self_comparisons(module_path)
        expected = Counter(chapter.get("known_self_comparisons", []))
        observed = Counter(item["id_expression"] for item in actual)
        if observed != expected:
            added = list((observed - expected).elements())
            removed = list((expected - observed).elements())
            if added:
                issues.append(
                    f"{chapter['id']}: nove/nepoznate self-comparison provjere: {added}"
                )
            if removed:
                issues.append(
                    f"{chapter['id']}: manifest jos ocekuje uklonjene tautologije: {removed}"
                )
        for item in actual:
            self_findings.append(
                {"chapter": chapter["id"], "path": str(module_path), **item}
            )

    for example in manifest.get("known_unverified_examples", []):
        source = REPO_ROOT / example["source"]
        if not source.is_file():
            issues.append(f"{example['id']}: nedostaje izvor {example['source']}")
            continue
        text = source.read_text(encoding="utf-8")
        if example["anchor"] not in text:
            issues.append(
                f"{example['id']}: izvor vise ne sadrzi anchor {example['anchor']!r}; "
                "azurirati manifest i verifier zajedno."
            )

    for chapter_gap in manifest.get("known_unverified_chapters", []):
        source = REPO_ROOT / chapter_gap["source"]
        if not source.is_file():
            issues.append(
                f"{chapter_gap['id']}: nedostaje deklarirani novi izvor "
                f"{chapter_gap['source']}"
            )

    notebook_dir = REPO_ROOT / "notebooks"
    declared = set(manifest.get("notebooks", []))
    planned_items = manifest.get("planned_notebooks", [])
    planned = {item["name"] for item in planned_items}
    duplicated = sorted(declared & planned)
    if duplicated:
        issues.append(f"Notebook je istodobno obvezan i planiran: {duplicated}")
    for item in planned_items:
        source = REPO_ROOT / item["source"]
        if not source.is_file():
            issues.append(
                f"Planirani notebook {item['name']} upucuje na nepostojeci "
                f"izvor {item['source']}"
            )
    present = {path.name for path in notebook_dir.glob("u??_*.ipynb")}
    missing = sorted(declared - present)
    extra = sorted(present - declared - planned)
    if missing:
        issues.append(f"Nedostaju deklarirani notebooci: {missing}")
    if extra:
        issues.append(f"Notebooci izvan manifesta: {extra}")

    return {
        "issues": issues,
        "self_comparisons": self_findings,
        "canonical_task_count": len(manifest.get("canonical_tasks", [])),
        "notebook_count": len(present),
        "planned_notebook_count": len(planned),
        "pending_planned_notebooks": sorted(planned - present),
        "unverified_chapter_count": len(
            manifest.get("known_unverified_chapters", [])
        ),
    }


def _exercise_task_id(result_id: str) -> str | None:
    match = EXERCISE_ID_RE.match(result_id)
    if not match:
        return None
    return f"{match.group(1)}.{match.group(2)}"


def audit_results(
    manifest: dict[str, Any], results: Iterable[dict[str, Any]]
) -> dict[str, Any]:
    """Klasificiraj izvrsene provjere bez pripisivanja pokrivenosti rupama."""

    issues: list[str] = []
    exercise_map = _exercise_map(manifest)
    result_list = list(results)
    ids: list[str] = []
    results_by_task: dict[str, list[dict[str, Any]]] = {}

    for index, result in enumerate(result_list, start=1):
        if not isinstance(result, dict):
            issues.append(f"Rezultat #{index} nije rjecnik.")
            continue
        result_id = result.get("id")
        status = result.get("status")
        verification = result.get("verification")
        if not isinstance(result_id, str) or not RESULT_ID_RE.fullmatch(result_id):
            issues.append(f"Nestabilna/nevaljana oznaka rezultata: {result_id!r}")
            continue
        ids.append(result_id)
        if status not in {"OK", "FAIL"}:
            issues.append(f"{result_id}: nepoznat status {status!r}")
        if verification not in {None, "golden", "invariant"}:
            issues.append(
                f"{result_id}: nepoznata vrsta verifikacije {verification!r}"
            )

        task_id = _exercise_task_id(result_id)
        if task_id is not None:
            results_by_task.setdefault(task_id, []).append(result)
            if task_id not in exercise_map:
                issues.append(f"{result_id}: zadatak nije deklariran u manifestu.")

    duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
    if duplicates:
        issues.append(f"Duplicirane oznake rezultata: {duplicates}")

    canonical_contracts = {
        contract["result_id"]: contract["verification"]
        for task in manifest.get("canonical_tasks", [])
        for contract in task["verifier"]["result_contracts"]
    }
    actual_by_id = {
        result["id"]: result
        for result in result_list
        if isinstance(result, dict) and isinstance(result.get("id"), str)
    }
    missing_canonical_results = sorted(set(canonical_contracts) - set(actual_by_id))
    if missing_canonical_results:
        issues.append(
            "Kanonski task ugovori bez izvršenoga result-ID-ja: "
            f"{missing_canonical_results}"
        )
    for result_id, expected_level in canonical_contracts.items():
        result = actual_by_id.get(result_id)
        if result is None:
            continue
        actual_level = result.get("verification", "golden")
        if actual_level != expected_level:
            issues.append(
                f"{result_id}: manifest očekuje {expected_level}, izvršenje vraća "
                f"{actual_level}."
            )

    for task_id, meta in exercise_map.items():
        task_results = results_by_task.get(task_id, [])
        present = bool(task_results)
        if meta["check_expected"] and not present:
            issues.append(f"{task_id}: manifest ocekuje provjeru, ali nema rezultata.")
        if not meta["check_expected"] and present:
            issues.append(
                f"{task_id}: manifest ga vodi bez provjere, ali rezultat postoji; "
                "klasificirati novu provjeru."
            )
        if not present:
            continue
        result_levels = {
            item.get("verification", "golden") for item in task_results
        }
        if meta["level"] == "golden" and "golden" not in result_levels:
            issues.append(
                f"{task_id}: deklariran je golden, ali nema neovisnu golden usporedbu."
            )
        if meta["level"] == "invariant" and result_levels != {"invariant"}:
            issues.append(
                f"{task_id}: nedovoljno zadani zadatak smije imati samo "
                "invarijantne provjere."
            )

    for chapter in manifest.get("supplemental_chapters", []):
        prefix = f"{chapter['id']}."
        required = set(chapter["published_numeric_results"])
        chapter_results = [
            item for item in result_list
            if isinstance(item, dict)
            and isinstance(item.get("id"), str)
            and item["id"].startswith(prefix)
        ]
        unlabeled = sorted(
            item["id"] for item in chapter_results
            if item.get("verification") not in {"golden", "invariant"}
        )
        if unlabeled:
            issues.append(
                f"{chapter['id']}: novi rezultati bez eksplicitne klasifikacije: "
                f"{unlabeled}"
            )
        present_golden = {
            item["id"] for item in chapter_results
            if item.get("verification") == "golden"
        }
        missing_published = sorted(required - present_golden)
        unexpected_golden = sorted(present_golden - required)
        if missing_published:
            issues.append(
                f"{chapter['id']}: nema provjere objavljenih brojeva: "
                f"{missing_published}"
            )
        if unexpected_golden:
            issues.append(
                f"{chapter['id']}: golden rezultati nisu deklarirani u manifestu: "
                f"{unexpected_golden}"
            )
        declared_example_groups = set(chapter["published_example_groups"])
        present_example_groups = {
            result_id[len(prefix):].split(".", 1)[0]
            for result_id in present_golden
            if re.match(r"P\d+\.", result_id[len(prefix):])
        }
        if present_example_groups != declared_example_groups:
            issues.append(
                f"{chapter['id']}: grupe golden primjera ne odgovaraju manifestu; "
                f"ocekivano {sorted(declared_example_groups)}, pronadeno "
                f"{sorted(present_example_groups)}."
            )

    counts = {"golden": 0, "invariant": 0, "gap": 0}
    for result in result_list:
        result_id = result.get("id", "") if isinstance(result, dict) else ""
        task_id = _exercise_task_id(result_id)
        if task_id is None:
            level = result.get("verification", "golden") if isinstance(result, dict) else "golden"
            if level in counts:
                counts[level] += 1
        elif task_id in exercise_map:
            declared_level = exercise_map[task_id]["level"]
            if declared_level == "gap":
                counts["gap"] += 1
            else:
                actual_level = (
                    result.get("verification", "golden")
                    if isinstance(result, dict)
                    else "golden"
                )
                counts[actual_level] += 1

    failed = [
        item for item in result_list
        if isinstance(item, dict) and item.get("status") != "OK"
    ]
    declared_exercise_gaps = sum(
        1 for meta in exercise_map.values() if meta["level"] == "gap"
    )
    declared_example_gaps = len(manifest.get("known_unverified_examples", []))
    declared_chapter_gaps = len(manifest.get("known_unverified_chapters", []))
    return {
        "issues": issues,
        "raw_result_count": len(result_list),
        "golden_result_count": counts["golden"],
        "invariant_result_count": counts["invariant"],
        "gap_result_count": counts["gap"],
        "declared_exercise_gaps": declared_exercise_gaps,
        "declared_example_gaps": declared_example_gaps,
        "declared_task_gaps": declared_exercise_gaps + declared_example_gaps,
        "declared_chapter_gaps": declared_chapter_gaps,
        "failed": failed,
    }


def main() -> int:
    try:
        manifest = load_manifest()
        report = audit_static(manifest)
    except (OSError, json.JSONDecodeError, ManifestError) as exc:
        print(f"QA manifest ERROR: {exc}")
        return 1

    print(
        f"Numericki moduli u manifestu: {len(_verifier_chapters(manifest))} "
        f"({len(manifest['chapters'])} naslijedenih + "
        f"{len(manifest.get('supplemental_chapters', []))} novih)"
    )
    print(
        "Strojno citljivi kanonski zadatci: "
        f"{report['canonical_task_count']}/90 (schema v2)"
    )
    print(f"Notebooci u inventaru: {report['notebook_count']}")
    if report["planned_notebook_count"]:
        print(
            f"Planirani notebooci: {report['planned_notebook_count']} "
            f"(ceka: {len(report['pending_planned_notebooks'])})"
        )
    print(
        "Nova poglavlja bez numerickog modula: "
        f"{report['unverified_chapter_count']}"
    )
    print(
        "Poznate self-comparison lokacije: "
        f"{len(report['self_comparisons'])} (za release mora biti 0)"
    )
    for item in report["self_comparisons"]:
        path = Path(item["path"]).relative_to(REPO_ROOT)
        print(
            f"  - {path}:{item['line']}  {item['id_expression']}  "
            f"usporeduje {item['value_expression']} sa samim sobom"
        )

    if report["issues"]:
        print("\nQA audit FAIL:")
        for issue in report["issues"]:
            print(f"  - {issue}")
        return 1

    print("\nQA audit: OK, nema novih ili neprijavljenih strukturnih rupa.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
