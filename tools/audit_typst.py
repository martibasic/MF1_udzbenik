#!/usr/bin/env python3
"""Read-only contract audit for native MF1 Typst authoring blocks."""

from __future__ import annotations

import re
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "_quarto-pdf.yml"
FILTER = ROOT / "filters" / "mf1-typst-author-blocks.lua"
COMPONENT = ROOT / "assets" / "typst" / "mf1-author-blocks.typ"
MODEL = ROOT / 'filters/mf1-component-model.lua'

REQUIRED_CLASSES = (
    "mf1-we",
    "mf1-ch",
    "mf1-temelj",
    "mf1-izvod",
    "mf1-fizikalno-znacenje",
    "mf1-granica-modela",
    "mf1-numerika",
    "mf1-dublje",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for path in (CONFIG, FILTER, COMPONENT, MODEL):
        if not path.is_file():
            fail(f"nedostaje {path.relative_to(ROOT)}")

    config = CONFIG.read_text(encoding="utf-8")
    filter_text = FILTER.read_text(encoding="utf-8")
    component = COMPONENT.read_text(encoding="utf-8")
    component_model = MODEL.read_text(encoding='utf8')
    if 'mf1-component-model.lua' not in filter_text or 'components/registry.json' not in component_model:
        fail('PDF adapter nije povezan sa zajedničkim registrom komponenti')
    if "components.visible(components.kind(div), 'pdf')" not in filter_text:
        fail('PDF adapter ne primjenjuje zajedničko pravilo vidljivosti')

    if "assets/typst/mf1-author-blocks.typ" not in config:
        fail("Typst komponenta nije uključena u PDF profil")
    if "filters/mf1-typst-author-blocks.lua" not in config:
        fail("Lua filter nije uključen u PDF profil")

    source_text = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted((ROOT / "source").glob("*.md"))
    )
    counts: dict[str, int] = {}
    registry = json.loads((ROOT / 'components/registry.json').read_text(encoding='utf8'))['components']
    mapped = {name: component for component in registry.values() for name in component.get('classes', [])}
    for class_name in REQUIRED_CLASSES:
        if class_name not in mapped or not mapped[class_name].get('pdf_mode'):
            fail(f"Zajednički registar nema PDF mapiranje klase .{class_name}")
        count = len(re.findall(rf"^:::\s+\{{[^}}]*\.{re.escape(class_name)}(?:\s|\}})", source_text, re.MULTILINE))
        counts[class_name] = count

    required_typst_contract = (
        "#let mf1-author-block",
        '#let mf1-level',
        '#let mf1-minor-heading',
        'mode == "example"',
        'Para = render_minor_heading',
        'Span = render_span',
        "breakable: true",
        "first-line-indent: 0pt",
        "sticky: true",
    )
    for token in required_typst_contract:
        if token not in component and token not in filter_text:
            fail(f"Typst ugovor nema obvezni zapis: {token}")

    ignored = subprocess.run(
        ["git", "check-ignore", "-q", str(COMPONENT.relative_to(ROOT))],
        cwd=ROOT,
        check=False,
    )
    if ignored.returncode == 0:
        fail("Typst komponenta je ignorirana i ne bi ušla u clean checkout")
    if ignored.returncode not in (0, 1):
        fail("git check-ignore nije moguće izvršiti")

    summary = ", ".join(f".{name}={count}" for name, count in counts.items())
    print(f"PASS: nativni Typst autorski blokovi ({summary}); komponenta nije ignorirana.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
