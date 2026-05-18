"""SVG strukturni normalizator za MF1_udzbenik.

Walks assets/print/*.svg and applies canonical structural fixes:
- Prefixes every id="..." with a deterministic per-file prefix
- Updates url(#...), href="#...", xlink:href="#...", aria-labelledby tokens
- Replaces font-family variants containing "Segoe UI" with canonical
  "'Segoe UI',Arial,sans-serif"
- Adds preserveAspectRatio="xMidYMid meet" and a responsive style attribute
  to the root <svg> if missing

Idempotent: running twice does not introduce further changes.

Usage:
    py tools/svg_normalize.py            # apply changes in place
    py tools/svg_normalize.py --check    # report only, exit 1 if changes needed
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS = REPO_ROOT / "assets" / "print"
LOG_PATH = REPO_ROOT / "tools" / "svg_normalize.log"

CANONICAL_FONT = "'Segoe UI',Arial,sans-serif"


def make_prefix(stem: str) -> str:
    """Short deterministic prefix from filename stem.

    Examples:
        u01_val1_klip_manometar     -> u01v1km
        u01_ch1_dvostruka_platforma -> u01c1dp
        u01_fig_uvod_pregled        -> u01fup
        u01_vjezbe_skice            -> u01vs
    """
    parts = [p for p in stem.split("_") if p]
    out: list[str] = []
    for i, p in enumerate(parts):
        if i == 0:
            out.append(p)
        elif re.fullmatch(r"val\d+", p):
            out.append("v" + p[3:])
        elif re.fullmatch(r"ch\d+", p):
            out.append("c" + p[2:])
        elif p == "fig":
            out.append("f")
        else:
            out.append(p[0])
    return "".join(out)


_ID_RE = re.compile(r'\bid="([^"]+)"')


def find_all_ids(svg: str) -> list[str]:
    return _ID_RE.findall(svg)


def reprefix_ids(svg: str, prefix: str) -> tuple[str, dict[str, str]]:
    """Rename every id so it starts with prefix and update all references.

    If every existing id already starts with prefix, returns svg unchanged.
    """
    ids = find_all_ids(svg)
    if not ids:
        return svg, {}

    mapping: dict[str, str] = {}
    for old in ids:
        if old.startswith(prefix):
            mapping[old] = old
        else:
            mapping[old] = f"{prefix}_{old}"

    if all(k == v for k, v in mapping.items()):
        return svg, {}

    out = svg
    for old in sorted(mapping.keys(), key=len, reverse=True):
        new = mapping[old]
        if old == new:
            continue
        esc = re.escape(old)
        out = re.sub(rf'\bid="{esc}"', f'id="{new}"', out)
        out = re.sub(rf"url\(#{esc}\)", f"url(#{new})", out)
        out = re.sub(rf'(\bhref|xlink:href)="#{esc}"', rf'\1="#{new}"', out)

    def replace_in_aria(m: re.Match[str]) -> str:
        tokens = m.group(1).split()
        new_tokens = [mapping.get(t, t) for t in tokens]
        return f'aria-labelledby="{" ".join(new_tokens)}"'

    out = re.sub(r'aria-labelledby="([^"]+)"', replace_in_aria, out)
    return out, mapping


def fix_font_family(svg: str) -> str:
    """Normalize any font-family attribute mentioning Segoe UI."""

    def repl(m: re.Match[str]) -> str:
        val = m.group(1)
        if "segoe" in val.lower():
            return f'font-family="{CANONICAL_FONT}"'
        return m.group(0)

    return re.sub(r'font-family="([^"]+)"', repl, svg)


def ensure_root_attrs(svg: str) -> str:
    """Add preserveAspectRatio + responsive style to the root <svg> if missing."""
    m = re.search(r"<svg\b([^>]*)>", svg, re.DOTALL)
    if not m:
        return svg

    root_attrs = m.group(1)
    new_attrs = root_attrs

    if "preserveAspectRatio" not in root_attrs:
        new_attrs = new_attrs.rstrip() + ' preserveAspectRatio="xMidYMid meet"'

    if not re.search(r"\bstyle=", root_attrs):
        wm = re.search(r'\bwidth="(\d+)"', root_attrs)
        if not wm:
            vm = re.search(r'\bviewBox="\s*\d+\s+\d+\s+(\d+)', root_attrs)
            max_width = vm.group(1) if vm else "900"
        else:
            max_width = wm.group(1)
        new_attrs = (
            new_attrs.rstrip()
            + f' style="display:block;width:100%;max-width:{max_width}px;height:auto;"'
        )

    if new_attrs == root_attrs:
        return svg
    return svg.replace(m.group(0), f"<svg{new_attrs}>", 1)


def normalize_text(text: str, prefix: str) -> str:
    out, _ = reprefix_ids(text, prefix)
    out = fix_font_family(out)
    out = ensure_root_attrs(out)
    return out


def process(path: Path, check_only: bool) -> tuple[bool, str]:
    original = path.read_text(encoding="utf-8")
    prefix = make_prefix(path.stem)
    new = normalize_text(original, prefix)
    if new == original:
        return False, f"  ok        {path.name}"
    if check_only:
        return True, f"  WOULD FIX {path.name}  (prefix={prefix})"
    path.write_text(new, encoding="utf-8")
    return True, f"  fixed     {path.name}  (prefix={prefix})"


def main() -> int:
    check_only = "--check" in sys.argv

    if not ASSETS.is_dir():
        print(f"FATAL: {ASSETS} not found", file=sys.stderr)
        return 2

    lines: list[str] = []
    changed = 0
    total = 0
    for svg_path in sorted(ASSETS.glob("*.svg")):
        total += 1
        ch, msg = process(svg_path, check_only)
        lines.append(msg)
        if ch:
            changed += 1

    header = (
        f"svg_normalize: {total} files scanned, "
        f"{changed} {'would change' if check_only else 'changed'}."
    )
    lines.insert(0, header)
    lines.insert(1, "")
    LOG_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(header)
    print(f"Log: {LOG_PATH.relative_to(REPO_ROOT)}")
    if check_only and changed > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
