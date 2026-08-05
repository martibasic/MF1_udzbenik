"""Provjeri da JupyterLite izlaz stvarno sadrži Python kernel i bilježnice."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_EXTENSIONS = {
    "@jupyterlite/pyodide-kernel-extension",
    "@jupyter-widgets/jupyterlab-manager",
}
EXPECTED_NOTEBOOKS = 17
REPO_ROOT = Path(__file__).resolve().parents[1]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", default="_site/jlite")
    args = parser.parse_args()
    root = Path(args.output).resolve()
    issues: list[str] = []

    required_files = [
        root / "lab" / "index.html",
        root / "jupyter-lite.json",
        root / "api" / "contents" / "all.json",
    ]
    for path in required_files:
        if not path.is_file() or path.stat().st_size == 0:
            issues.append(f"nedostaje ili je prazan {path.as_posix()}")

    config: dict[str, object] = {}
    contents: dict[str, object] = {}
    if (root / "jupyter-lite.json").is_file():
        try:
            loaded = json.loads((root / "jupyter-lite.json").read_text("utf-8"))
            if isinstance(loaded, dict):
                config = loaded
            else:
                issues.append("jupyter-lite.json na vrhu nije JSON objekt")
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(f"jupyter-lite.json nije valjan JSON: {exc}")
    if (root / "api" / "contents" / "all.json").is_file():
        try:
            loaded = json.loads(
                (root / "api" / "contents" / "all.json").read_text("utf-8")
            )
            if isinstance(loaded, dict):
                contents = loaded
            else:
                issues.append("contents/all.json na vrhu nije JSON objekt")
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(f"contents/all.json nije valjan JSON: {exc}")

    data = config.get("jupyter-config-data", {})
    if not isinstance(data, dict):
        issues.append("jupyter-config-data nije JSON objekt")
        data = {}
    raw_extensions = data.get("federated_extensions", [])
    if not isinstance(raw_extensions, list):
        issues.append("federated_extensions nije JSON popis")
        raw_extensions = []
    extension_entries = [
        item
        for item in raw_extensions
        if isinstance(item, dict) and isinstance(item.get("name"), str)
    ]
    extensions = {str(item["name"]) for item in extension_entries}
    missing_extensions = sorted(REQUIRED_EXTENSIONS - extensions)
    if missing_extensions:
        issues.append(
            "JupyterLite nema obvezne pregledničke ekstenzije: "
            + ", ".join(missing_extensions)
        )

    for extension_name in sorted(REQUIRED_EXTENSIONS & extensions):
        entry = next(
            item for item in extension_entries if item.get("name") == extension_name
        )
        load = entry.get("load")
        if not isinstance(load, str) or not load.strip():
            issues.append(f"ekstenzija {extension_name} nema ulaznu JavaScript datoteku")
            continue
        extension_asset = (
            root / "extensions" / extension_name / load.split("?", 1)[0]
        ).resolve()
        try:
            extension_asset.relative_to(root)
        except ValueError:
            issues.append(f"ekstenzija {extension_name} upućuje izvan JupyterLitea")
            continue
        if not extension_asset.is_file() or extension_asset.stat().st_size == 0:
            issues.append(
                f"nedostaje ulazna datoteka ekstenzije {extension_name}: "
                f"{extension_asset.as_posix()}"
            )

    plugin_settings = data.get("litePluginSettings", {})
    if not isinstance(plugin_settings, dict):
        issues.append("litePluginSettings nije JSON objekt")
        plugin_settings = {}
    if "@jupyterlite/pyodide-kernel-extension:kernel" not in plugin_settings:
        issues.append("JupyterLite nema konfiguriran Pyodide Python kernel")
    if data.get("defaultKernelName") != "python":
        issues.append("zadani JupyterLite kernel nije 'python'")

    kernel_settings = plugin_settings.get(
        "@jupyterlite/pyodide-kernel-extension:kernel", {}
    )
    if not isinstance(kernel_settings, dict):
        issues.append("postavke Pyodide kernela nisu JSON objekt")
    else:
        piplite_urls = kernel_settings.get("pipliteUrls", [])
        if not isinstance(piplite_urls, list) or not piplite_urls:
            issues.append("Pyodide kernel nema lokalni piplite indeks")
        else:
            for raw_url in piplite_urls:
                if not isinstance(raw_url, str):
                    issues.append("pipliteUrls sadrži vrijednost koja nije URL")
                    continue
                split = urlsplit(raw_url)
                if split.scheme or split.netloc:
                    continue
                relative = unquote(split.path)
                if relative.startswith("./"):
                    relative = relative[2:]
                target = (root / relative).resolve()
                try:
                    target.relative_to(root)
                except ValueError:
                    issues.append(f"piplite indeks izlazi iz JupyterLitea: {raw_url!r}")
                    continue
                if not target.is_file() or target.stat().st_size == 0:
                    issues.append(f"nedostaje lokalni piplite indeks {raw_url!r}")

    entries = contents.get("content", []) if isinstance(contents, dict) else []
    if not isinstance(entries, list):
        issues.append("contents/all.json polje content nije popis")
        entries = []
    notebook_names = [
        str(item.get("name"))
        for item in entries
        if isinstance(item, dict) and str(item.get("name", "")).endswith(".ipynb")
    ]
    if len(notebook_names) != len(set(notebook_names)):
        issues.append("contents/all.json sadrži duplicirane bilježnice")
    notebooks = set(notebook_names)
    source_paths = {
        path.name: path for path in (REPO_ROOT / "notebooks").glob("u??_*.ipynb")
    }
    source_notebooks = set(source_paths)
    if len(source_notebooks) != EXPECTED_NOTEBOOKS:
        issues.append(
            f"izvorni inventar ima {len(source_notebooks)} umjesto "
            f"{EXPECTED_NOTEBOOKS} bilježnica"
        )
    if notebooks != source_notebooks:
        missing = sorted(source_notebooks - notebooks)
        extra = sorted(notebooks - source_notebooks)
        issues.append(
            f"inventar bilježnica nije jednak izvoru; nedostaje={missing}, višak={extra}"
        )

    built_paths = {
        path.name: path for path in (root / "files").glob("u??_*.ipynb")
    }
    built_notebooks = set(built_paths)
    if built_notebooks != source_notebooks:
        missing = sorted(source_notebooks - built_notebooks)
        extra = sorted(built_notebooks - source_notebooks)
        issues.append(
            f"datoteke bilježnica nisu jednake izvoru; nedostaje={missing}, višak={extra}"
        )
    for name in sorted(source_notebooks & built_notebooks):
        if _sha256(source_paths[name]) != _sha256(built_paths[name]):
            issues.append(f"JupyterLite bilježnica je zastarjela ili izmijenjena: {name}")

    if issues:
        print("JupyterLite audit FAIL:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(
        "JupyterLite audit PASS: "
        f"notebookovi={len(notebooks)}, ekstenzije={len(extensions)}, Python=Pyodide"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
