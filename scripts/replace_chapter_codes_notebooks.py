#!/usr/bin/env python3
"""Zamijeni U/D šifre u notebooks/ — README.md i .ipynb datoteke."""
import re
from pathlib import Path

NB_DIR = Path(__file__).resolve().parent.parent / "notebooks"


def strip_u(code: str) -> str:
    return str(int(code[1:]))


def strip_d(code: str) -> str:
    return {"D01": "A", "D02": "B", "D03": "C", "D04": "D"}[code]


def process(text: str) -> str:
    # "Poglavlje U01:" / "poglavlja U01" / "poglavlju U01" / "U poglavlju U01"
    text = re.sub(
        r"(?i)(poglavlj[euia]) U(\d{2})",
        lambda m: f"{m.group(1)} {int(m.group(2))}",
        text,
    )
    # bare U01–U13 (table cells, ranges, inline mentions) -> pog. N
    text = re.sub(
        r"U(\d{2})\s*[\-–]\s*U(\d{2})",
        lambda m: f"pog. {int(m.group(1))}–{int(m.group(2))}",
        text,
    )
    text = re.sub(
        r"\bU(\d{2})\b",
        lambda m: f"pog. {int(m.group(1))}",
        text,
    )
    text = re.sub(
        r"\bD(0[1-4])\b",
        lambda m: f"dod. {strip_d('D' + m.group(1))}",
        text,
    )
    return text


def main() -> None:
    changed = 0
    for path in sorted(list(NB_DIR.glob("*.md")) + list(NB_DIR.glob("*.ipynb"))):
        original = path.read_text(encoding="utf-8")
        updated = process(original)
        if original != updated:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated: {path.name}")
            changed += 1
    print(f"\nTotal files updated: {changed}")


if __name__ == "__main__":
    main()
