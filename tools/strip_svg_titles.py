r"""Ukloni top-level naslove iz SVG-ova u assets/print/.

Pravilo iz protokola (Faza 1):
  caption u Markdownu pokriva ulogu naslova; SVG ne smije imati
  vlastiti naslov u rendered-u (`<text>` element s tekstom "U.. - ...").

Skripta uklanja:
  1. `<text>` elemente ciji tekst pocinje s "U[0-9]+ " ili "U[0-9]+\s[–-]"
     (chapter-named naslov, npr. "U10 – Realni Bernoulli i gubici").
  2. `<text>` elemente koji su NEPOSREDNO ispod takvog naslova u SVG
     izvoru (u sljedecoj liniji), uz uvjet da nemaju font-weight="700"
     i da nisu chapter-named (= najvjerojatnije podnaslov).

Ne dira:
  - `<title>` accessibility elemente (vazno za screen reader)
  - panel labele unutar viseclanih figura (one nemaju U.. prefiks)

Idempotentno: ako naslov vec ne postoji, ne mijenja se ni jedan bajt.

Usage:
    py tools/strip_svg_titles.py        # primijeni
    py tools/strip_svg_titles.py --check # samo izvjestaj, exit 1 ako bi se mijenjalo
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS = REPO_ROOT / "assets" / "print"
LOG = REPO_ROOT / "tools" / "strip_svg_titles.log"


# Element: <text ...>U10 – ...</text>  (može početi razmacima i biti na vise linija)
# Dopusta inner <tspan> elemente i HTML entitete (&#x2013;) kao naslov sadrzaj.
TITLE_RE = re.compile(
    r'^\s*<text\b[^>]*>\s*'
    r'(U\d+[\s–—\-]\s?|U\d+\s?&#x2013;|U\d+\s?&#x2014;)'
    r'(?:[^<]|<tspan[^>]*>[^<]*</tspan>)*'
    r'</text>\s*\n',
    re.MULTILINE,
)


def is_subtitle_candidate(line: str) -> bool:
    """Provjeri je li sljedeca linija najvjerojatnije podnaslov.

    Heuristika:
    - linija sadrzi <text ...>...</text>
    - NE sadrzi font-weight="700" (podnaslov je obicno bez bolda)
    - tekst NE pocinje s U[0-9]+ (drugi panel/lab)
    - fill je sivi ton (`#5..` ili `#6..` ili `#7..`) ILI font-size je manji
    """
    if "<text" not in line or "</text>" not in line:
        return False
    if 'font-weight="700"' in line:
        return False
    # extract text content
    m = re.search(r">([^<]+)</text>", line)
    if not m:
        return False
    text = m.group(1).strip()
    if re.match(r"^U\d+\b", text):
        return False
    # heuristika: subtitle obicno ima sivi fill (#5xx, #6xx, #7xx, ili "#516677" tip)
    fill_m = re.search(r'fill="(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})"', line)
    if fill_m:
        fill = fill_m.group(1).lower()
        # sivi tonovi: prosjek RGB komponenti blizu i nije ekstrem
        if len(fill) == 7:
            r = int(fill[1:3], 16)
            g = int(fill[3:5], 16)
            b = int(fill[5:7], 16)
            avg = (r + g + b) / 3
            # sivi = RGB komponente medjusobno blizu i avg u srednjem rasponu
            if max(r, g, b) - min(r, g, b) < 30 and 50 < avg < 180:
                return True
    # ili font-size manje od 14 (podnaslov je obicno ~12-13)
    fs_m = re.search(r'font-size="(\d+(?:\.\d+)?)"', line)
    if fs_m and float(fs_m.group(1)) <= 14:
        return True
    return False


def strip_titles(svg: str) -> tuple[str, int]:
    """Vrati (novi_svg, broj_uklonjenih)."""
    lines = svg.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    removed = 0
    while i < len(lines):
        line = lines[i]
        # provjeri je li ova linija naslov
        if TITLE_RE.match(line):
            removed += 1
            i += 1
            # provjeri sljedecu liniju kao kandidat za podnaslov
            if i < len(lines) and is_subtitle_candidate(lines[i]):
                removed += 1
                i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out), removed


def process(check_only: bool = False) -> int:
    svgs = sorted(ASSETS.glob("*.svg"))
    changed = 0
    log_lines: list[str] = []
    for svg_path in svgs:
        original = svg_path.read_text(encoding="utf-8")
        new, removed = strip_titles(original)
        if removed > 0:
            log_lines.append(f"{svg_path.name}: -{removed} naslov(a)/podnaslov(a)")
            changed += 1
            if not check_only:
                svg_path.write_text(new, encoding="utf-8")

    LOG.write_text("\n".join(log_lines) + ("\n" if log_lines else ""), encoding="utf-8")

    print(f"strip_svg_titles: {len(svgs)} skenirano, {changed} promijenjeno.")
    print(f"Log: {LOG}")
    return 1 if (check_only and changed > 0) else 0


if __name__ == "__main__":
    sys.exit(process("--check" in sys.argv))
