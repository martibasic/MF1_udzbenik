"""Popravi XML konformancu SVG datoteka u assets/print/.

Codex je generirao SVG-ove s necistim XML komentarima (`<!-- ... -- ... -->`)
koji krse XML spec (`--` nije dopusten unutar komentara). Browser-i to tolerira,
ali stroge XML parser-e (Python xml.etree, validatori) to lome.

Skripta:
  1. Detektira sve `<!--`...`-->` komentare.
  2. Unutar svakog komentara zamijenjuje `--` (dva ili vise crtica) s `==`.
  3. Provjeri preostali `<!--` bez `-->` na istom redu => visemjesni komentar,
     zatim trazi `-->` u sljedecim linijama.

Idempotentna i sigurna.
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS = REPO_ROOT / "assets" / "print"


COMMENT_RE = re.compile(r"<!--(.*?)-->", re.DOTALL)


def _sanitize_comment_body(body: str) -> str:
    """Zamijeni svaku sekvencu od 2+ crtica s `==` (isti broj znakova)."""
    return re.sub(r"-{2,}", lambda m: "=" * len(m.group(0)), body)


def fix_svg(text: str) -> tuple[str, int]:
    """Vrati (popravljen_tekst, broj_popravljenih_komentara)."""
    fixes = 0

    def replace(m: re.Match) -> str:
        nonlocal fixes
        body = m.group(1)
        fixed = _sanitize_comment_body(body)
        if fixed != body:
            fixes += 1
        return f"<!--{fixed}-->"

    new = COMMENT_RE.sub(replace, text)
    return new, fixes


def process() -> int:
    total_fixed = 0
    files_touched = 0
    failures: list[tuple[str, str]] = []

    for svg in sorted(ASSETS.glob("*.svg")):
        original = svg.read_text(encoding="utf-8")
        new, fixes = fix_svg(original)
        if fixes > 0:
            svg.write_text(new, encoding="utf-8")
            files_touched += 1
            total_fixed += fixes

        # validate
        try:
            ET.fromstring(new)
        except ET.ParseError as exc:
            failures.append((svg.name, str(exc)[:120]))

    print(f"fix_svg_xml: {files_touched} datoteka popravljeno, {total_fixed} komentara sredeno.")
    if failures:
        print()
        print(f"JOS NEVALJANIH ({len(failures)}):")
        for name, err in failures:
            print(f"  {name}: {err}")
        return 1
    print("Sve SVG datoteke su sad XML-valjane.")
    return 0


if __name__ == "__main__":
    sys.exit(process())
