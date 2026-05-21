#!/usr/bin/env python3
"""Zamijeni U00-U13 i D01-D04 šifre s ljudski čitljivim referencama."""
import re
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent / "source"

U_LABEL = {f"U{n:02d}": f"pog. {n}" for n in range(0, 14)}
D_LABEL = {"D01": "dod. A", "D02": "dod. B", "D03": "dod. C", "D04": "dod. D"}


def to_label(code: str) -> str:
    if code in U_LABEL:
        return U_LABEL[code]
    if code in D_LABEL:
        return D_LABEL[code]
    return code


def replace_alt_prefix(text: str) -> str:
    # ![U01 ... ](...) -> ![... ](...) i ![D03 ...](...) -> ![...](...)
    return re.sub(r"!\[(U\d{2}|D\d{2}) ", "![", text)


def replace_span_codes(text: str) -> str:
    # <span class="mf1-ch-code">U01</span> -> <span class="mf1-ch-code">pog. 1</span>
    def repl(m: re.Match) -> str:
        return f'<span class="mf1-ch-code">{to_label(m.group(1))}</span>'

    return re.sub(
        r'<span class="mf1-ch-code">(U\d{2}|D\d{2})</span>',
        repl,
        text,
    )


def replace_range(text: str) -> str:
    # U01-U02, U01–U02, U01 - U02 -> pog. 1–2 (only when both prefixes match)
    def repl_u(m: re.Match) -> str:
        a = int(m.group(1))
        b = int(m.group(2))
        return f"pog. {a}–{b}"

    text = re.sub(r"U(\d{2})\s*[\-–]\s*U(\d{2})", repl_u, text)

    def repl_d(m: re.Match) -> str:
        d1 = D_LABEL[f"D{m.group(1)}"].split(". ")[1]
        d2 = D_LABEL[f"D{m.group(2)}"].split(". ")[1]
        return f"dod. {d1}–{d2}"

    text = re.sub(r"D(0[1-4])\s*[\-–]\s*D(0[1-4])", repl_d, text)
    return text


def replace_single(text: str) -> str:
    # U01 -> pog. 1 (samostalno, ne unutar lowercase paths)
    def repl(m: re.Match) -> str:
        return to_label(m.group(1))

    return re.sub(r"\b(U\d{2}|D0[1-4])\b", repl, text)


def process(text: str) -> str:
    text = replace_alt_prefix(text)
    text = replace_span_codes(text)
    text = replace_range(text)
    text = replace_single(text)
    return text


def main() -> None:
    changed = 0
    for md in sorted(SOURCE_DIR.glob("*.md")):
        original = md.read_text(encoding="utf-8")
        updated = process(original)
        if original != updated:
            md.write_text(updated, encoding="utf-8")
            print(f"Updated: {md.name}")
            changed += 1
    print(f"\nTotal files updated: {changed}")


if __name__ == "__main__":
    main()
