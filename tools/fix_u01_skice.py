"""Faza 3 — sistemski i per-file popravci U01 SVG skica.

Sistemski (svi U01 SVG-ovi koji imaju ove obrasce):
1. Vode gradient bottom stop: #7fb3d3 -> #5b9ec9
2. Kote (markeri, linije, tekstovi): #3a3a3a i #4a4a4a -> #b7600c

Per-file kritični popravci (Codex regressions od pre-Faza-1 stanja):
- val2: F_1 plava -> crvena (ulazna sila treba biti crvena)
- val3: F_p plava -> crvena
- ch1:  F_p plava -> crvena
- most: F_p plava -> crvena
        + Codex je vratio stari oznake — popraviti:
          F_p01 -> F_pod, A_p01 -> A_pod, p_t3n -> p_min
        + ukloniti rendered top-level title (ne pocinje s "U[0-9]+" pa
          strip_svg_titles.py ga nije uhvatio)
- presa: ukloniti rendered title

Idempotentno.
"""
from __future__ import annotations

import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets" / "print"


# ---------- 1. Sistemski (svi U01 SVG-ovi) ----------

def apply_systemic(text: str) -> tuple[str, int]:
    """Vrati (new_text, broj_promjena)."""
    n = 0
    # Vode gradient
    if "#7fb3d3" in text:
        text = text.replace("#7fb3d3", "#5b9ec9")
        n += 1
    # Kote: siva -> smeda
    for old in ("#3a3a3a", "#4a4a4a"):
        if old in text:
            cnt = text.count(old)
            text = text.replace(old, "#b7600c")
            n += cnt
    return text, n


# ---------- 2. Per-file: F_force plava -> crvena ----------
# Vrijedi za:
#   val2: F_1 (ulazna sila pumpe)
#   val3: F_p (sila na pumpni klip)
#   ch1:  F_p (sila na pumpni klip)
#   most: F_p (sila na pumpni klip)
#
# Pristup: pronaci "Sila Fx prema dolje" komentar pa
# unutar bloka 4-6 linija zamijeniti:
#   - stroke="#1565c0" -> stroke="#c0392b"
#   - fill="#1565c0" (u <text>) -> fill="#c0392b"
#   - marker-end="url(#PFXaBl)" -> "url(#PFXaR)"

def fix_force_palette_block(text: str, comment_marker: str) -> tuple[str, int]:
    """Pronaci komentar 'Sila Fx prema dolje' i pretvoriti naredne 5 linija plave -> crvene.

    Vraca (new_text, count).
    """
    pattern = re.compile(
        rf"({re.escape(comment_marker)}\s*-->)\n"
        r"(\s+<line[^/]*?stroke=\"#1565c0\"[^/]*?marker-end=\"url\(#([A-Za-z0-9_]+)Bl\)\"[^/]*?/>)\n"
        r"(\s+<text[^>]*fill=\"#1565c0\"[^>]*>[^<]*</text>)\n"
        r"(\s+<text[^>]*fill=\"#1565c0\"[^>]*>[^<]*</text>)",
        re.MULTILINE,
    )

    def replace(m: re.Match) -> str:
        prefix_match = m.group(3)
        new_line = m.group(2).replace('stroke="#1565c0"', 'stroke="#c0392b"').replace(
            f'marker-end="url(#{prefix_match}Bl)"',
            f'marker-end="url(#{prefix_match}R)"',
        )
        new_text1 = m.group(4).replace('fill="#1565c0"', 'fill="#c0392b"')
        new_text2 = m.group(5).replace('fill="#1565c0"', 'fill="#c0392b"')
        return f"{m.group(1)}\n{new_line}\n{new_text1}\n{new_text2}"

    new, n = pattern.subn(replace, text)
    return new, n


# ---------- 3. Per-file: regression oznaka u most ----------

def fix_most_oznake(text: str) -> tuple[str, int]:
    """Popraviti F_p01 -> F_pod, A_p01 -> A_pod, p_t3n -> p_min u most SVG-u.

    Codex je koristio Unicode subscript znakove:
      &#8346; = ₚ
      &#x2080; = ₀
      &#x2081; = ₁
      &#x2083; = ₃
      &#8345; = ₙ
      &#8348; = ₜ
    Pa je F_p01 zapisan kao F&#8346;&#x2080;&#x2081; (Fₚ₀₁).
    Tekst zadatka koristi F_pod, A_pod, p_min — pa treba zamijeniti.

    Zamjena ide preko <tspan> radi tocnijeg rendering subscripta:
      F<tspan baseline-shift="sub" font-size="0.7em">pod</tspan>
    """
    n = 0
    # F_p01 -> F_pod
    if "F&#8346;&#x2080;&#x2081;" in text:
        text = text.replace(
            "F&#8346;&#x2080;&#x2081;",
            'F<tspan baseline-shift="sub" font-size="0.7em">pod</tspan>',
        )
        n += 1
    # A_p01 -> A_pod
    if "A&#8346;&#x2080;&#x2081;" in text:
        text = text.replace(
            "A&#8346;&#x2080;&#x2081;",
            'A<tspan baseline-shift="sub" font-size="0.7em">pod</tspan>',
        )
        n += 1
    # p_t3n -> p_min
    # original sekvenca: p&#8348;&#x2083;&#8345;
    if "p&#8348;&#x2083;&#8345;" in text:
        text = text.replace(
            "p&#8348;&#x2083;&#8345;",
            'p<tspan baseline-shift="sub" font-size="0.7em">min</tspan>',
        )
        n += 1
    return text, n


# ---------- 4. Ukloniti rendered top-level titles ----------

def remove_top_titles(text: str, file_name: str) -> tuple[str, int]:
    """Ukloniti top-level <text> naslove koje strip_svg_titles.py nije uhvatio.

    Pattern: <text> na vrhu canvasa (y < 80) s vecim font-size (>= 16) i koji NIJE
    panel-labela.

    Za jednostavnost i sigurnost: ovdje rucno uklanjamo poznate naslove iz most i presa.
    """
    n = 0
    if "most_podizanje" in file_name:
        # Linije 43-44: Naslov + podnaslov
        old = (
            '  <text x="336" y="42" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="17" font-weight="700" fill="#1a2530" text-anchor="middle">'
            'Hidrauli&#269;no podizanje mosta pri zamjeni le&#382;aja</text>\n'
            '  <text x="336" y="60" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11.5" fill="#5a6a78" text-anchor="middle">'
            'G = 480 kN, n = 4 podiza&#269;a (d = 110 mm), ru&#269;na pumpa (d&#8346; = 22 mm, F&#8346; = 500 N)</text>\n'
        )
        if old in text:
            text = text.replace(old, "")
            n += 2
    if "presa_savijanje" in file_name:
        # Linija 39
        old = (
            '  <text x="490" y="44" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="17" font-weight="700" fill="#1a2530" text-anchor="middle">'
            'Hidrauli&#269;na pre&#353;a – presjek (d&#x2081; = 32 mm, d&#x2082; = 128 mm, omjer 1:4)</text>\n'
        )
        if old in text:
            text = text.replace(old, "")
            n += 1
    return text, n


# ---------- 5. Legenda fix ----------
# val2, val3, ch1: legend square colors za "ulazna sila F_x" treba crvena
# (Codex je u legendi imao plavu, semantička greška)

def fix_legend(text: str, file_name: str) -> tuple[str, int]:
    """Razdvojiti legendu: ulazna sila crvena, tlak plavi."""
    n = 0

    if "val2_hidraulicna_dizalica" in file_name:
        # Original line: <rect x="48" y="422" width="12" height="12" fill="#1565c0" rx="2"/>
        #                <text ...>ulazna sila F₁, tlak p</text>
        # Treba: dvije zasebne stavke — crvena (F_1) i plava (tlak)
        old = (
            '  <rect x="48" y="422" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="65" y="433" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">ulazna sila F₁, tlak p</text>\n'
        )
        new = (
            '  <rect x="48" y="422" width="12" height="12" fill="#c0392b" rx="2"/>\n'
            '  <text x="65" y="433" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">ulazna sila F₁</text>\n'
            '  <rect x="142" y="422" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="159" y="433" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">tlak p</text>\n'
        )
        if old in text:
            text = text.replace(old, new)
            n += 1

    if "val3_dvostruki_podizac" in file_name:
        old = (
            '  <rect x="832" y="450" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="849" y="461" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">tlak p / sila F&#8346;</text>\n'
        )
        new = (
            '  <rect x="832" y="450" width="12" height="12" fill="#c0392b" rx="2"/>\n'
            '  <text x="849" y="461" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">ulazna F&#8346;</text>\n'
            '  <rect x="893" y="450" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="910" y="461" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">tlak p</text>\n'
        )
        if old in text:
            text = text.replace(old, new)
            n += 1

    if "ch1_dvostruka_platforma" in file_name:
        old = (
            '  <rect x="820" y="468" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="837" y="479" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">tlak p / F&#8346;</text>\n'
        )
        new = (
            '  <rect x="820" y="468" width="12" height="12" fill="#c0392b" rx="2"/>\n'
            '  <text x="837" y="479" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">ulazna F&#8346;</text>\n'
            '  <rect x="880" y="468" width="12" height="12" fill="#1565c0" rx="2"/>\n'
            '  <text x="897" y="479" font-family="\'Segoe UI\',Arial,sans-serif" '
            'font-size="11" fill="#5a6a78">tlak p</text>\n'
        )
        if old in text:
            text = text.replace(old, new)
            n += 1

    return text, n


# ---------- Main ----------

FORCE_COMMENTS = {
    "u01_val2_hidraulicna_dizalica.svg": "Sila F1 prema dolje",
    "u01_val3_dvostruki_podizac.svg": "Sila Fp prema dolje",
    "u01_ch1_dvostruka_platforma_manometar.svg": "Sila Fp prema dolje",
    "u01_fig_most_podizanje.svg": "Fp arrow down",
}


def main() -> None:
    files = sorted(ASSETS.glob("u01_*.svg"))
    total_changes = 0
    report = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        before = text
        changes = 0

        # 1. Sistemski
        text, n = apply_systemic(text)
        changes += n

        # 2. F_force plava -> crvena
        comment = FORCE_COMMENTS.get(f.name)
        if comment:
            text, n = fix_force_palette_block(text, comment)
            changes += n

        # 3. Most regression oznake
        if "most_podizanje" in f.name:
            text, n = fix_most_oznake(text)
            changes += n

        # 4. Ukloniti rendered title (most, presa)
        text, n = remove_top_titles(text, f.name)
        changes += n

        # 5. Legenda fix
        text, n = fix_legend(text, f.name)
        changes += n

        if text != before:
            f.write_text(text, encoding="utf-8")
            total_changes += changes
            report.append((f.name, changes))
        else:
            report.append((f.name, 0))

    print(f"fix_u01_skice: {len(files)} datoteka, {total_changes} ukupnih promjena.")
    for name, n in report:
        print(f"  {name}: {n}")


if __name__ == "__main__":
    main()
