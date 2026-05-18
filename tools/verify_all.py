"""Runner za sve `verify_uXX.py` provjere primjera i zadataka.

Koristi se kroz Fazu 1 (vidi `~/.claude/plans/pro-itaj-to-u-folderu-federated-moore.md`).
Svaki `tools/verify_uXX.py` izvozi funkciju `verify()` koja vraca listu rezultata u
formatu `{"id": "PrimjerX.Y", "status": "OK"|"FAIL", "details": "..."}`.

Modul izostane => preskace se i biljezi se kao "missing".

Pokretanje:
    py tools/verify_all.py
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS = REPO_ROOT / "tools"
sys.path.insert(0, str(TOOLS))

CHAPTERS = [f"u{i:02d}" for i in range(1, 14)]


def run() -> int:
    total_ok = 0
    total_fail = 0
    missing = []

    print(f"verify_all: scanning {len(CHAPTERS)} chapters\n")

    for ch in CHAPTERS:
        module_name = f"verify_{ch}"
        try:
            mod = importlib.import_module(module_name)
        except ModuleNotFoundError:
            missing.append(ch)
            print(f"  [{ch}]  missing  (no tools/{module_name}.py)")
            continue
        except Exception as e:
            print(f"  [{ch}]  IMPORT ERROR: {type(e).__name__}: {e}")
            total_fail += 1
            continue

        if not hasattr(mod, "verify"):
            print(f"  [{ch}]  ERROR    (module {module_name} has no verify())")
            total_fail += 1
            continue

        try:
            results = mod.verify()
        except Exception as e:
            print(f"  [{ch}]  CRASH    {type(e).__name__}: {e}")
            total_fail += 1
            continue

        ch_ok = sum(1 for r in results if r["status"] == "OK")
        ch_fail = sum(1 for r in results if r["status"] != "OK")
        total_ok += ch_ok
        total_fail += ch_fail
        status = "OK" if ch_fail == 0 else "FAIL"
        print(f"  [{ch}]  {status:7s}  ok={ch_ok}  fail={ch_fail}")
        for r in results:
            if r["status"] != "OK":
                print(f"           - {r['id']}: {r.get('details', '')}")

    print()
    print(f"Total ok:     {total_ok}")
    print(f"Total fail:   {total_fail}")
    print(f"Missing mod:  {len(missing)} ({', '.join(missing) if missing else '-'})")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
