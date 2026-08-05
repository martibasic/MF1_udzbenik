"""Validiraj i, po zadanim postavkama, izvrsi sve nastavne notebooke.

Notebook se ucitava i izvrsava u memoriji; izvorna ``.ipynb`` datoteka ne
mijenja se i izlazi se ne zapisuju u repozitorij. Popis je kanonski definiran u
``verification_manifest.json`` pa novi ili nestali notebook rusi provjeru.
"""

from __future__ import annotations

import argparse
import asyncio
import ast
import json
import os
from pathlib import Path
import re
import time
from typing import Any
import warnings

import qa_audit


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = REPO_ROOT / "notebooks"


def _source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else str(source)


def validate_notebook(path: Path) -> list[str]:
    """Provjeri JSON, Python sintaksu i pedagoško-numerički ugovor."""

    issues: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path.name}: nije valjan notebook JSON: {exc}"]

    if notebook.get("nbformat") != 4:
        issues.append(f"{path.name}: ocekuje se nbformat=4.")
    cells = notebook.get("cells")
    if not isinstance(cells, list):
        return issues + [f"{path.name}: polje cells nije lista."]

    code_count = 0
    assert_count = 0
    imported_roots: set[str] = set()
    notebook_text: list[str] = []
    for index, cell in enumerate(cells, start=1):
        if not isinstance(cell, dict):
            continue
        source_text = _source_text(cell)
        notebook_text.append(source_text)
        if cell.get("cell_type") != "code":
            continue
        code_count += 1
        if cell.get("outputs"):
            issues.append(
                f"{path.name} celija {index}: spremljeni izlaz mora se očistiti."
            )
        if cell.get("execution_count") is not None:
            issues.append(
                f"{path.name} celija {index}: execution_count mora biti null."
            )
        try:
            with warnings.catch_warnings():
                # Escape sekvence u Matplotlib/LaTeX oznakama mogu dati
                # SyntaxWarning, ali nisu sintaksna pogreska notebooka.
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(source_text, f"{path.name}#cell-{index}", "exec")
                compile(tree, f"{path.name}#cell-{index}", "exec")
            for node in ast.walk(tree):
                if isinstance(node, ast.Assert):
                    assert_count += 1
                elif isinstance(node, ast.Import):
                    imported_roots.update(
                        alias.name.split(".", 1)[0] for alias in node.names
                    )
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported_roots.add(node.module.split(".", 1)[0])
        except SyntaxError as exc:
            issues.append(
                f"{path.name} celija {index}: Python sintaksna pogreska: {exc.msg}"
            )
    if code_count == 0:
        issues.append(f"{path.name}: nema nijednu code celiju.")
        return issues

    text = "\n".join(notebook_text)
    required_stages = {
        "Predvidi": r"predvid",
        "Izračunaj": r"izračun|izracun",
        "Provjeri": r"provjer",
    }
    for label, pattern in required_stages.items():
        if not re.search(pattern, text, re.IGNORECASE):
            issues.append(f"{path.name}: nedostaje faza „{label}”.")
    if not re.search(
        r"nesigurn|konverg|osjetljiv|rezidual|pogrešk|vremensk|numerič",
        text,
        re.IGNORECASE,
    ):
        issues.append(
            f"{path.name}: nema analize pogreške, konvergencije, "
            "osjetljivosti, reziduala ili nesigurnosti."
        )
    if assert_count < 2:
        issues.append(
            f"{path.name}: treba najmanje dvije neovisne assert provjere; "
            f"nađeno {assert_count}."
        )
    unsupported = sorted(imported_roots - {"numpy", "matplotlib"})
    if unsupported:
        issues.append(
            f"{path.name}: ovisnosti izvan pregledničkog ugovora: {unsupported}"
        )
    if re.search(r"np\.random\.(?!default_rng\s*\(\s*\d+\s*\))", text):
        issues.append(
            f"{path.name}: slučajni račun mora rabiti default_rng s fiksnim seedem."
        )
    return issues


def execute_notebook(path: Path, timeout: int) -> tuple[bool, str]:
    """Izvrsi notebook u cistom kernelu i odbaci generirane izlaze."""

    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError as exc:  # pragma: no cover - ovisi o lokalnom okruzenju
        return False, f"nedostaje ovisnost {exc.name!r}; instalirati requirements.txt"

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        # Generator je nastao prije obveznog nbformat cell-id polja. ID-jevi se
        # dodaju deterministicki samo kopiji u memoriji; izvor se ne prepisuje.
        for index, cell in enumerate(raw.get("cells", []), start=1):
            cell.setdefault("id", f"mf1-cell-{index:03d}")
            if isinstance(cell.get("source"), list):
                cell["source"] = "".join(cell["source"])
        notebook = nbformat.from_dict(raw)
        nbformat.validate(notebook)
        if os.name == "nt":  # izbjegava dodatnu ZMQ selector dretvu na Windowsu
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        client = NotebookClient(
            notebook,
            timeout=timeout,
            kernel_name="python3",
            allow_errors=False,
            resources={"metadata": {"path": str(path.parent)}},
        )
        client.execute()
    except Exception as exc:  # ispisuje se sazetak; izvorna datoteka ostaje ista
        return False, f"{type(exc).__name__}: {exc}"
    return True, ""


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Provjeri inventar, JSON i Python sintaksu bez pokretanja kernela.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Najdulje trajanje jedne celije u sekundama (zadano: 120).",
    )
    parser.add_argument(
        "--notebook",
        action="append",
        default=[],
        help="Izvrsi samo navedeni notebook iz manifesta; opcija se moze ponoviti.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if args.timeout <= 0:
        print("ERROR: --timeout mora biti pozitivan.")
        return 2

    try:
        manifest = qa_audit.load_manifest()
    except Exception as exc:
        print(f"ERROR: manifest se ne moze ucitati: {exc}")
        return 1

    declared = manifest["notebooks"]
    planned = [item["name"] for item in manifest.get("planned_notebooks", [])]
    allowed = set(declared) | set(planned)
    inventory = {path.name for path in NOTEBOOK_DIR.glob("u??_*.ipynb")}
    selected = args.notebook or (declared + [name for name in planned if name in inventory])
    unknown = sorted(set(selected) - allowed)
    if unknown:
        print(f"ERROR: notebook nije u manifestu: {unknown}")
        return 2

    missing_required = sorted(set(declared) - inventory)
    unexpected = sorted(inventory - allowed)
    missing_selected = sorted(set(selected) - inventory)
    if missing_required or unexpected or missing_selected:
        print("ERROR: notebook inventar i manifest nisu uskladeni.")
        print(f"  nedostaje obveznih: {missing_required}")
        print(f"  izvan manifesta:    {unexpected}")
        print(f"  odabrano, ne postoji: {missing_selected}")
        return 1

    validation_issues: list[str] = []
    for name in selected:
        validation_issues.extend(validate_notebook(NOTEBOOK_DIR / name))
    if validation_issues:
        print("Notebook validation FAIL:")
        for issue in validation_issues:
            print(f"  - {issue}")
        return 1

    if args.validate_only:
        pending = len(set(planned) - inventory)
        if planned:
            print(
                f"Notebook validation: OK ({len(selected)} prisutnih; "
                f"{pending} planiranih jos nema)"
            )
        else:
            print(f"Notebook validation: OK ({len(selected)}/{len(declared)} obveznih)")
        return 0

    os.environ.setdefault("MPLBACKEND", "Agg")
    failures: list[str] = []
    total_start = time.perf_counter()
    for name in selected:
        path = NOTEBOOK_DIR / name
        start = time.perf_counter()
        ok, details = execute_notebook(path, args.timeout)
        elapsed = time.perf_counter() - start
        if ok:
            print(f"  [OK]   {name:42s} {elapsed:6.2f} s")
        else:
            failures.append(f"{name}: {details}")
            print(f"  [FAIL] {name:42s} {elapsed:6.2f} s")

    elapsed_total = time.perf_counter() - total_start
    print(
        f"\nNotebook execution: ok={len(selected) - len(failures)}, "
        f"fail={len(failures)}, total={elapsed_total:.2f} s"
    )
    if failures:
        for failure in failures:
            print(f"  - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
