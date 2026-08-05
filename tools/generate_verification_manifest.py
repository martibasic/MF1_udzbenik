"""Generiraj strojno citljiv ugovor za svih 90 javnih zadataka MF1.

Postojeci dio ``verification_manifest.json`` i dalje inventarizira 19 izvrsnih
verifier modula. Ova skripta deterministicki gradi dodatni kanonski sloj iz
javnih izvora i AST-a verifiera. Bez ``--write`` radi kao stroga provjera
zastarjelosti; s ``--write`` osvjezava samo generirana polja sheme v2.

Granica parsera namjerno je konzervativna: puni Markdown teksta zadatka ostaje
autoritativan, a strukturiraju se samo nedvosmisleni skalarni brojevi iz inline
matematike. Nizovi, intervali, krivulje i simbolicki podatci ostaju navedeni u
``unparsed_numeric_math`` umjesto da im se izmisli znacenje ili jedinica.
"""

from __future__ import annotations

import argparse
import ast
from copy import deepcopy
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tools" / "verification_manifest.json"

# Javni broj poglavlja nije uvijek jednak povijesnom namespaceu verifiera.
# Ova je tablica jedina eksplicitna migracijska veza javnog toka U01--U15.
CANONICAL_CHAPTERS: list[dict[str, str]] = [
    {"id": "U01", "source": "source/u01_osnove_fluida_i_pascalov_zakon.md", "verifier_module": "verify_u01", "verifier_namespace": "U01"},
    {"id": "U02", "source": "source/u02_viskoznost_povrsinska_napetost_i_kapilarnost.md", "verifier_module": "verify_u02", "verifier_namespace": "U02"},
    {"id": "U03", "source": "source/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md", "verifier_module": "verify_u03", "verifier_namespace": "U03"},
    {"id": "U04", "source": "source/u04_relativno_mirovanje_fluida.md", "verifier_module": "verify_u04", "verifier_namespace": "U04"},
    {"id": "U05", "source": "source/u05_hidrostatske_sile_na_plohe.md", "verifier_module": "verify_u05_integrated", "verifier_namespace": "U05.CANON"},
    {"id": "U06", "source": "source/u07_uzgon_plivanje_i_stabilnost.md", "verifier_module": "verify_u07", "verifier_namespace": "U07"},
    {"id": "U07", "source": "source/u08_kontrolni_volumen_i_kontinuitet.md", "verifier_module": "verify_u08", "verifier_namespace": "U08"},
    {"id": "U08", "source": "source/u09_bernoullijeva_jednadzba_idealnog_fluida.md", "verifier_module": "verify_u09", "verifier_namespace": "U09"},
    {"id": "U09", "source": "source/u09_kompresibilni_idealni_tok.md", "verifier_module": "verify_u09_compressible", "verifier_namespace": "U09.COMP"},
    {"id": "U10", "source": "source/u11_kolicina_gibanja_i_sile_strujanja.md", "verifier_module": "verify_u11", "verifier_namespace": "U11"},
    {"id": "U11", "source": "source/u14_bezdimenzijski_brojevi_dimenzijska_analiza_i_slicnost.md", "verifier_module": "verify_u14", "verifier_namespace": "U14"},
    {"id": "U12", "source": "source/u12_diferencijalni_opis_realnog_toka.md", "verifier_module": "verify_u12_real_flow", "verifier_namespace": "U12.REAL"},
    {"id": "U13", "source": "source/u13_gubici_cjevovodi_crpke_i_mreze.md", "verifier_module": "verify_u13_integrated", "verifier_namespace": "U13.CANON"},
    {"id": "U14", "source": "source/u12_pokretne_lopatice_i_potisak.md", "verifier_module": "verify_u12", "verifier_namespace": "U12"},
    {"id": "U15", "source": "source/u15_otvoreni_tokovi.md", "verifier_module": "verify_u15_open_channels", "verifier_namespace": "U15"},
]

TASK_LINE_RE = re.compile(
    r"(?m)^(?P<line>[^\n]*\{#(?P<id>task-[A-Za-z0-9_-]+)\}[^\n]*)$"
)
LEVEL_RE = re.compile(r"(?:\[\*\*|Razina:\s*)(T[1-4])")
INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)\$(?!\$)")
ASSUMPTION_RE = re.compile(
    r"\b(?:pretpostav\w*|zanemar\w*|uzm\w*|smatra\w*|idealn\w*|"
    r"kvazistacion\w*|stacionar\w*|nestlaciv\w*|neovisn\w*|"
    r"atmosfersk\w*|bez\s+gubitaka|ako\s+nije\s+druk\w*)\b",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(
    r"^[+\-]?\d+(?:(?:\{,\}|[,.])\d+)?(?:\\,\d{3})*"
    r"(?:\s*\\cdot\s*10\^\{?[+\-]?\d+\}?)?"
)


def _compact(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _section_payload(block: str, heading: str) -> tuple[str | None, int | None]:
    """Vrati sadrzaj jednostavnoga Quarto callout odjeljka i relativnu liniju."""

    match = re.search(rf"(?m)^\s*###\s+{re.escape(heading)}\s*$", block)
    if not match:
        return None, None
    lines = block[match.end() :].splitlines()
    payload: list[str] = []
    started = False
    for line in lines:
        stripped = line.strip()
        if not started and not stripped:
            continue
        if stripped in {":::", "::::", ":::::"}:
            break
        started = True
        payload.append(line.strip())
    value = _compact("\n".join(payload))
    return (value or None), _line_number(block, match.start())


def _task_statement(anchor_line: str, following: str) -> str:
    if LEVEL_RE.search(anchor_line):
        return _compact(anchor_line.split("}", 1)[1])

    lines = following.splitlines()
    payload: list[str] = []
    started = False
    for line in lines:
        stripped = line.strip()
        if not started:
            if not stripped:
                continue
            level = re.match(r"\*\*Razina:\s*T[1-4]\.\*\*\s*(.*)", stripped)
            if not level:
                continue
            started = True
            if level.group(1):
                payload.append(level.group(1))
            continue
        if stripped.startswith(":::") or re.match(r"^#{2,}\s", stripped):
            break
        payload.append(stripped)
    return _compact("\n".join(payload))


def _task_preamble(text: str, first_task_offset: int) -> tuple[str, int]:
    headings = list(re.finditer(r"(?mi)^##\s+.*zada(?:t|c).*?$", text[:first_task_offset]))
    if not headings:
        return "", 1
    start = headings[-1].end()
    return text[start:first_task_offset], _line_number(text, start)


def _sentences_with_assumptions(text: str, provenance: str, line: int) -> list[dict[str, Any]]:
    cleaned = re.sub(r"(?m)^\s*:{3,}.*$", " ", text)
    cleaned = _compact(cleaned)
    if not cleaned:
        return []
    candidates = re.split(r"(?<=[.!?;])\s+", cleaned)
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    for candidate in candidates:
        value = candidate.strip(" -*")
        if not value or not ASSUMPTION_RE.search(value) or value in seen:
            continue
        seen.add(value)
        items.append(
            {
                "text": value,
                "provenance": {"kind": provenance, "line": line},
            }
        )
    return items


def _parse_number(raw: str) -> float | None:
    value = raw.replace("{,}", ".").replace(",", ".").replace("\\,", "")
    power = re.search(r"\\cdot\s*10\^\{?([+\-]?\d+)\}?", value)
    if power:
        value = value[: power.start()].strip()
        exponent = int(power.group(1))
    else:
        exponent = 0
    try:
        result = float(value) * 10.0**exponent
    except ValueError:
        return None
    return result if math.isfinite(result) else None


def _normalize_unit(raw: str) -> str:
    value = raw.strip()
    value = re.sub(r"\\(?:text|mathrm)\{([^{}]*)\}", r"\1", value)
    value = value.replace("\\,", "").replace("\\;", "")
    value = re.sub(r"\\(?=\s|$)", "", value)
    value = value.replace("\\cdot", "·").replace("\\circ", "°")
    value = value.replace("\\%", "%")
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\\(?=[A-Za-z])", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace(" ^", "^").replace("/ ", "/")
    if value in {"^°", "°"}:
        return "°"
    if value in {"^°C", "°C"}:
        return "°C"
    return value


# Samo bijela lista nedvosmislenih skalarnih pretvorbi. Ostale se jedinice
# cuvaju tocno kako su zapisane, bez pogadanja fizikalne velicine.
SI_CONVERSIONS: dict[str, tuple[float, float, str]] = {
    "mm": (1e-3, 0.0, "m"),
    "cm": (1e-2, 0.0, "m"),
    "m": (1.0, 0.0, "m"),
    "mm^2": (1e-6, 0.0, "m^2"),
    "cm^2": (1e-4, 0.0, "m^2"),
    "m^2": (1.0, 0.0, "m^2"),
    "mm^3": (1e-9, 0.0, "m^3"),
    "cm^3": (1e-6, 0.0, "m^3"),
    "m^3": (1.0, 0.0, "m^3"),
    "L": (1e-3, 0.0, "m^3"),
    "L/s": (1e-3, 0.0, "m^3/s"),
    "m^3/s": (1.0, 0.0, "m^3/s"),
    "m^2/s": (1.0, 0.0, "m^2/s"),
    "m/s": (1.0, 0.0, "m/s"),
    "mm/s": (1e-3, 0.0, "m/s"),
    "m/s^2": (1.0, 0.0, "m/s^2"),
    "kg": (1.0, 0.0, "kg"),
    "kg/s": (1.0, 0.0, "kg/s"),
    "kg/m^3": (1.0, 0.0, "kg/m^3"),
    "N": (1.0, 0.0, "N"),
    "kN": (1e3, 0.0, "N"),
    "N/m": (1.0, 0.0, "N/m"),
    "Pa": (1.0, 0.0, "Pa"),
    "Pa s": (1.0, 0.0, "Pa s"),
    "kPa": (1e3, 0.0, "Pa"),
    "MPa": (1e6, 0.0, "Pa"),
    "bar": (1e5, 0.0, "Pa"),
    "bar(abs)": (1e5, 0.0, "Pa(abs)"),
    "W": (1.0, 0.0, "W"),
    "kW": (1e3, 0.0, "W"),
    "J/(kg K)": (1.0, 0.0, "J/(kg K)"),
    "s": (1.0, 0.0, "s"),
    "min": (60.0, 0.0, "s"),
    "h": (3600.0, 0.0, "s"),
    "K": (1.0, 0.0, "K"),
    "°C": (1.0, 273.15, "K"),
    "°": (math.pi / 180.0, 0.0, "rad"),
    "rad/s": (1.0, 0.0, "rad/s"),
    "Hz": (1.0, 0.0, "s^-1"),
    "%": (0.01, 0.0, "1"),
}


def _si_value(value: float, unit: str) -> dict[str, Any] | None:
    conversion = SI_CONVERSIONS.get(unit)
    if not conversion:
        return None
    factor, offset, si_unit = conversion
    return {"value": value * factor + offset, "unit": si_unit}


def _input_data(statement: str) -> dict[str, Any]:
    scalars: list[dict[str, Any]] = []
    unparsed: list[str] = []
    for fragment in INLINE_MATH_RE.findall(statement):
        raw = fragment.strip()
        candidate = raw
        symbol: str | None = None
        relation = None
        split = re.match(r"^(?P<symbol>.+?)\s*(?P<relation>=|\\approx)\s*(?P<rhs>.+)$", candidate)
        if split:
            symbol = split.group("symbol").strip()
            relation = split.group("relation")
            candidate = split.group("rhs").strip()

        number_match = NUMBER_RE.match(candidate)
        if not number_match:
            if re.search(r"\d", raw):
                unparsed.append(raw)
            continue
        number_raw = number_match.group(0)
        value = _parse_number(number_raw)
        remainder = candidate[number_match.end() :].strip()
        remainder_has_unit_markup = bool(
            re.search(r"\\(?:text|mathrm)\{", remainder)
            or "\\circ" in remainder
        )
        uncertainty_raw = None
        if remainder.startswith("\\pm"):
            uncertainty_match = NUMBER_RE.match(remainder[3:].strip())
            if uncertainty_match:
                uncertainty_raw = uncertainty_match.group(0)
                remainder = remainder[3:].strip()[uncertainty_match.end() :].strip()

        # Izrazi poput 24-0,012q^2 nisu skalarni ulazi.
        if (
            value is None
            or (remainder and remainder[0] in "+-*/")
            or (
                remainder
                and not remainder_has_unit_markup
                and re.search(r"[A-Za-z]", remainder)
            )
        ):
            unparsed.append(raw)
            continue
        unit = _normalize_unit(remainder)
        if not unit and symbol is None:
            unparsed.append(raw)
            continue
        item: dict[str, Any] = {
            "symbol": symbol,
            "relation": relation or "context_value",
            "value_text": number_raw,
            "value": value,
            "unit_text": remainder or "1",
            "normalized_unit": unit or "1",
            "provenance": "task_statement_inline_math",
        }
        si = _si_value(value, unit) if unit else {"value": value, "unit": "1"}
        if si:
            item["si"] = si
        else:
            item["si"] = None
            item["si_note"] = "Jedinica nije na konzervativnoj bijeloj listi; izvorni zapis ostaje autoritativan."
        if uncertainty_raw is not None:
            uncertainty = _parse_number(uncertainty_raw)
            item["uncertainty_text"] = uncertainty_raw
            item["uncertainty"] = uncertainty
            item["si_uncertainty"] = (
                _si_value(uncertainty, unit) if uncertainty is not None and unit else None
            )
        scalars.append(item)

    return {
        "scalars": scalars,
        "unparsed_numeric_math": list(dict.fromkeys(unparsed)),
        "parse_status": "conservative_partial",
        "authoritative_fallback": "statement.markdown",
    }


def _literal_or_expression(node: ast.AST) -> tuple[Any, str]:
    try:
        return ast.literal_eval(node), "literal"
    except (ValueError, TypeError):
        return ast.unparse(node), "expression"


def _module_constants(tree: ast.Module) -> dict[str, Any]:
    values: dict[str, Any] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        try:
            values[target.id] = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            continue
    return values


def _check_default(tree: ast.Module, constants: dict[str, Any]) -> tuple[str, float] | None:
    function = next(
        (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "_check"),
        None,
    )
    if function is None:
        return None
    positional = function.args.args
    defaults = [None] * (len(positional) - len(function.args.defaults)) + list(function.args.defaults)
    for argument, default in zip(positional, defaults):
        if argument.arg not in {"rel", "abs_tol"} or default is None:
            continue
        if isinstance(default, ast.Name) and default.id in constants:
            return argument.arg, float(constants[default.id])
        value, kind = _literal_or_expression(default)
        if kind == "literal" and isinstance(value, (int, float)):
            return argument.arg, float(value)
    return None


def _call_unit(node: ast.Call) -> str:
    if len(node.args) >= 5 and isinstance(node.args[4], ast.Constant):
        return str(node.args[4].value)
    for keyword in node.keywords:
        if keyword.arg == "unit" and isinstance(keyword.value, ast.Constant):
            return str(keyword.value.value)
    return ""


def _call_tolerance(
    node: ast.Call, default: tuple[str, float] | None
) -> dict[str, Any]:
    for keyword in node.keywords:
        if keyword.arg not in {"rel", "abs_tol"}:
            continue
        value, value_kind = _literal_or_expression(keyword.value)
        return {
            "kind": "relative" if keyword.arg == "rel" else "absolute",
            "value": value,
            "value_kind": value_kind,
            "provenance": "verifier_call_keyword",
        }
    if default is None:
        raise ValueError(f"_check na retku {node.lineno} nema razlucivu toleranciju")
    name, value = default
    return {
        "kind": "relative" if name == "rel" else "absolute",
        "value": value,
        "value_kind": "literal",
        "provenance": "verifier_check_default",
    }


def _verifier_contract(module_name: str) -> list[dict[str, Any]]:
    path = ROOT / "tools" / f"{module_name}.py"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    constants = _module_constants(tree)
    default_tolerance = _check_default(tree, constants)
    contracts: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if node.func.id not in {"_check", "_invariant"} or len(node.args) < 2:
            continue
        if not isinstance(node.args[1], ast.Constant) or not isinstance(node.args[1].value, str):
            continue
        result_id = node.args[1].value
        if node.func.id == "_check":
            target, target_kind = _literal_or_expression(node.args[3])
            contracts.append(
                {
                    "result_id": result_id,
                    "verification": "golden",
                    "target": target,
                    "target_kind": target_kind,
                    "unit": _call_unit(node) or "1",
                    "tolerance": _call_tolerance(node, default_tolerance),
                    "provenance": {"path": path.relative_to(ROOT).as_posix(), "line": node.lineno},
                }
            )
        else:
            condition = ast.unparse(node.args[2]) if len(node.args) >= 3 else ""
            details, details_kind = (
                _literal_or_expression(node.args[3]) if len(node.args) >= 4 else ("", "literal")
            )
            contracts.append(
                {
                    "result_id": result_id,
                    "verification": "invariant",
                    "criterion_expression": condition,
                    "failure_message": details,
                    "failure_message_kind": details_kind,
                    "provenance": {"path": path.relative_to(ROOT).as_posix(), "line": node.lineno},
                }
            )
    return sorted(contracts, key=lambda item: (item["provenance"]["line"], item["result_id"]))


def _independent_check(contracts: list[dict[str, Any]]) -> dict[str, Any]:
    invariants = [item for item in contracts if item["verification"] == "invariant"]
    if invariants:
        return {
            "kind": "executed_invariant",
            "criterion": [item["criterion_expression"] for item in invariants],
            "verifier_result_ids": [item["result_id"] for item in invariants],
            "note": "Izvršava se modelska, bilančna, granična ili dimenzijska tvrdnja bez izmišljanja ciljnoga broja.",
        }

    golden = [item for item in contracts if item["verification"] == "golden"]
    return {
        "kind": "independent_recalculation_with_unit_contract",
        "criterion": (
            "Verifier ponovno računa izlaze iz objavljenih ulaza, uspoređuje ih s "
            "fiksnim ciljevima i za svaki rezultat deklarira izlaznu SI ili "
            "SI-kompatibilnu jedinicu; '1' označuje bezdimenzijsku veličinu."
        ),
        "verifier_result_ids": [item["result_id"] for item in golden],
        "unit_contract": [
            {"result_id": item["result_id"], "unit": item["unit"]} for item in golden
        ],
    }


def _generation_metadata() -> dict[str, Any]:
    return {
        "canonical_tasks_command": "python tools/generate_verification_manifest.py --write",
        "check_command": "python tools/generate_verification_manifest.py",
        "generated_fields": [
            "chapters[].exercise_coverage",
            "chapters[].published_numeric_results",
            "supplemental_chapters[].exercise_coverage",
            "supplemental_chapters[].published_numeric_results",
            "canonical_chapters",
            "canonical_tasks",
        ],
        "parser_contract": {
            "authoritative_text": "canonical_tasks[].statement.markdown",
            "structured_input_scope": "Nedvosmisleni skalarni brojevi u inline matematici teksta zadatka.",
            "not_inferred": [
                "fizikalna veličina iz okolnoga proznog konteksta kada simbol nije naveden",
                "jedinice simboličkih krivulja, nizova, intervala i nepotpunih T3/T4 podataka",
                "prešutne fizikalne pretpostavke koje nisu zapisane u zadatku ili uvodu liste",
            ],
            "si_conversion": "Samo eksplicitna bijela lista nedvosmislenih jedinica; ostalo čuva izvorni zapis i si=null.",
        },
    }


def build_canonical_tasks(manifest: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """Izgradi kanonske task zapise; argument je rezerviran za QA API."""

    del manifest
    tasks: list[dict[str, Any]] = []
    for chapter in CANONICAL_CHAPTERS:
        source_path = ROOT / chapter["source"]
        text = source_path.read_text(encoding="utf-8")
        matches = list(TASK_LINE_RE.finditer(text))
        if len(matches) != 6:
            raise ValueError(
                f"{chapter['id']}: očekuje se šest task anchora u {chapter['source']}, nađeno {len(matches)}"
            )
        preamble, preamble_line = _task_preamble(text, matches[0].start())
        default_assumptions = _sentences_with_assumptions(
            preamble, "chapter_exercise_preamble", preamble_line
        )
        module_contracts = _verifier_contract(chapter["verifier_module"])
        for ordinal, match in enumerate(matches, start=1):
            end = matches[ordinal].start() if ordinal < len(matches) else len(text)
            block = text[match.start() : end]
            anchor_line = match.group("line")
            following = block[len(anchor_line) :]
            level_match = LEVEL_RE.search(block)
            if not level_match:
                raise ValueError(f"{chapter['id']} Z{ordinal}: nema razinu T1--T4")
            statement = _task_statement(anchor_line, following)
            if not statement:
                raise ValueError(f"{chapter['id']} Z{ordinal}: nije izvučen tekst zadatka")
            hint, hint_relative_line = _section_payload(block, "Naputak")
            control, control_relative_line = _section_payload(block, "Kontrolni rezultat")
            prefix = f"{chapter['verifier_namespace']}.Z{ordinal}."
            result_contracts = [
                deepcopy(item) for item in module_contracts if item["result_id"].startswith(prefix)
            ]
            if not result_contracts:
                raise ValueError(f"{chapter['id']} Z{ordinal}: nema verifier result-ID ugovora ({prefix})")
            golden = [item for item in result_contracts if item["verification"] == "golden"]
            invariants = [item for item in result_contracts if item["verification"] == "invariant"]
            if golden and not control:
                raise ValueError(f"{chapter['id']} Z{ordinal}: golden zadatak nema kontrolni rezultat")

            task_line = _line_number(text, match.start())
            explicit = _sentences_with_assumptions(statement, "task_statement", task_line)
            if hint:
                explicit.extend(
                    _sentences_with_assumptions(
                        hint,
                        "task_hint",
                        task_line + (hint_relative_line or 1) - 1,
                    )
                )
            stable_id = match.group("id")
            tasks.append(
                {
                    "id": stable_id,
                    "chapter": chapter["id"],
                    "ordinal": ordinal,
                    "level": level_match.group(1),
                    "source": {
                        "path": chapter["source"],
                        "line": task_line,
                        "anchor": f"#{stable_id}",
                    },
                    "statement": {
                        "markdown": statement,
                        "sha256": hashlib.sha256(statement.encode("utf-8")).hexdigest(),
                        "authoritative": True,
                    },
                    "input_data": _input_data(statement),
                    "assumptions": {
                        "explicit": explicit,
                        "explicit_status": (
                            "declared_and_extracted"
                            if explicit
                            else "none_identified_in_statement_or_hint"
                        ),
                        "defaults": deepcopy(default_assumptions),
                        "default_status": (
                            "declared_in_chapter_exercise_preamble"
                            if default_assumptions
                            else "none_declared_in_chapter_exercise_preamble"
                        ),
                        "provenance_policy": (
                            "Popisi sadrže samo rečenice pronađene u tekstu zadatka, "
                            "naputku ili uvodu liste; ništa se ne izvodi iz domenskoga znanja."
                        ),
                    },
                    "published_control": {
                        "kind": "numeric" if golden else "invariant_criterion",
                        "markdown": control,
                        "reason_if_absent": (
                            None
                            if control
                            else "Otvoreni zadatak nema jedinstven broj; kriterij je izvršni invarijantni ugovor verifiera."
                        ),
                        "provenance": {
                            "path": chapter["source"],
                            "line": (
                                task_line + control_relative_line - 1
                                if control_relative_line is not None
                                else task_line
                            ),
                        },
                    },
                    "tolerance": (
                        {
                            "kind": "per_result",
                            "contracts": [
                                {
                                    "result_id": item["result_id"],
                                    **item["tolerance"],
                                }
                                for item in golden
                            ],
                        }
                        if golden
                        else {
                            "kind": "not_numeric",
                            "reason": "Nema potpunoga numeričkog skupa podataka ni izmišljenoga cilja; prolaz određuju invarijante.",
                        }
                    ),
                    "independent_check": _independent_check(result_contracts),
                    "verifier": {
                        "module": chapter["verifier_module"],
                        "exercise_id": f"{chapter['verifier_namespace']}.Z{ordinal}",
                        "classification": "golden" if golden else "invariant",
                        "result_ids": [item["result_id"] for item in result_contracts],
                        "result_contracts": result_contracts,
                    },
                }
            )
    return tasks


def _refresh_module_inventory(result: dict[str, Any]) -> None:
    """Osvježi izvršni inventar iz AST-a umjesto ručnog popisa ID-jeva.

    Kanonski task sloj i stari modulni sloj moraju gledati isti skup stvarno
    izvršivih ``_check``/``_invariant`` poziva. Time novi golden rezultat ne
    može ostati nedeklariran, niti stari ID preživjeti samo u JSON-u.
    """

    for collection_name in ("chapters", "supplemental_chapters"):
        for chapter in result.get(collection_name, []):
            contracts = _verifier_contract(chapter["module"])
            chapter["published_numeric_results"] = [
                item["result_id"]
                for item in contracts
                if item["verification"] == "golden"
            ]
            golden: list[str] = []
            invariant: list[str] = []
            gap: list[str] = []
            for ordinal in range(1, 7):
                exercise = f"Z{ordinal}"
                prefix = f"{chapter['id']}.{exercise}."
                exercise_contracts = [
                    item for item in contracts if item["result_id"].startswith(prefix)
                ]
                if any(item["verification"] == "golden" for item in exercise_contracts):
                    golden.append(exercise)
                elif any(
                    item["verification"] == "invariant"
                    for item in exercise_contracts
                ):
                    invariant.append(exercise)
                else:
                    gap.append(exercise)
            chapter["exercise_coverage"] = {
                "golden": golden,
                "invariant": invariant,
                "gap": gap,
                "missing_checks": list(gap),
            }


def build_manifest(existing: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(existing)
    result["schema_version"] = 2
    result["generation"] = _generation_metadata()
    _refresh_module_inventory(result)
    result["canonical_chapters"] = deepcopy(CANONICAL_CHAPTERS)
    result["canonical_tasks"] = build_canonical_tasks(existing)

    preferred = [
        "schema_version",
        "scope",
        "generation",
        "chapters",
        "supplemental_chapters",
        "canonical_chapters",
        "canonical_tasks",
        "known_unverified_examples",
        "known_unverified_chapters",
        "notebooks",
    ]
    ordered: dict[str, Any] = {}
    for key in preferred:
        if key in result:
            ordered[key] = result[key]
    for key, value in result.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    existing = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = build_manifest(existing)
    if existing == expected:
        print("Verification manifest schema v2 je aktualan: 90/90 kanonskih zadataka.")
        return 0
    if args.write:
        MANIFEST.write_text(
            json.dumps(expected, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print("Ažuriran tools/verification_manifest.json (schema v2, 90 zadataka).")
        return 0
    print(
        "Verification manifest je zastario. Pokreni "
        "`python tools/generate_verification_manifest.py --write`."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
