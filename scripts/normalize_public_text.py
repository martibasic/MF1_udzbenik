"""Normalize public chapter references and remove internal production labels.

The transformation is intentionally narrow and idempotent. It derives chapter
numbers from the visible chapter title, so references survive the v2 reorder.
Run with ``--write`` to update canonical Markdown or without it as a CI check.
"""

from __future__ import annotations

import argparse
import html
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"

CHAPTER_BY_TITLE = {
    "Osnove fluida i Pascalov zakon": 1,
    "Viskoznost, površinska napetost i kapilarnost": 2,
    "Reologija, viskoznost i međupovršinske pojave": 2,
    "Hidrostatička raspodjela tlaka i manometrija": 3,
    "Relativno mirovanje fluida": 4,
    "Hidrostatske sile na ravne plohe": 5,
    "Zakrivljene plohe i rastav sila": 5,
    "Hidrostatske sile na ravne i zakrivljene plohe": 5,
    "Uzgon, plivanje i stabilnost": 6,
    "Uzgon, plivanje i početni stabilitet": 6,
    "Kontrolni volumen i kontinuitet": 7,
    "Kinematika, kontrolni volumen i kontinuitet": 7,
    "Bernoullijeva jednadžba idealnog fluida": 8,
    "Energijska jednadžba i Bernoulli": 8,
    "Kompresibilni idealni tok": 9,
    "Količina gibanja i sile strujanja": 10,
    "Količina i moment količine gibanja": 10,
    "Bezdimenzijski brojevi, dimenzijska analiza i sličnost": 11,
    "Dimenzijska analiza i sličnost": 11,
    "Diferencijalni opis realnog toka": 12,
    "Realni Bernoulli i gubici": 13,
    "Bernoullijeva jednadžba realnog fluida i gubici": 13,
    "Cjevovodi": 13,
    "Strujanje u cjevovodima i proračun mreže": 13,
    "Gubitci, cjevovodi, crpke i mreže": 13,
    "Pokretne lopatice i potisak": 14,
    "Turbostrojevi i propulzija": 14,
    "Otvoreni tokovi": 15,
}
CANONICAL_TITLE_BY_CHAPTER = {
    1: "Osnove fluida i Pascalov zakon",
    2: "Reologija, viskoznost i međupovršinske pojave",
    3: "Hidrostatička raspodjela tlaka i manometrija",
    4: "Relativno mirovanje fluida",
    5: "Hidrostatske sile na ravne i zakrivljene plohe",
    6: "Uzgon, plivanje i početni stabilitet",
    7: "Kinematika, kontrolni volumen i kontinuitet",
    8: "Energijska jednadžba i Bernoulli",
    9: "Kompresibilni idealni tok",
    10: "Količina i moment količine gibanja",
    11: "Dimenzijska analiza i sličnost",
    12: "Diferencijalni opis realnog toka",
    13: "Gubitci, cjevovodi, crpke i mreže",
    14: "Turbostrojevi i propulzija",
    15: "Otvoreni tokovi",
}

REF_RE = re.compile(
    r'(<span class="mf1-ch-ref"><span class="mf1-ch-code">pog\.\s*)'
    r'\d+'
    r'(</span><span class="mf1-ch-title">(?P<title>[^<]+)</span></span>)'
)
ALT_RE = re.compile(r"!\[(?:Val|CH)\s*\d+\s*[-–—]\s*([^\]]+)\]")
TASK_ANCHOR_RE = re.compile(
    r'<span id="(?P<id>task-[A-Za-z0-9-]+)"></span>\*\*(?P<level>T[1-4])\*\*'
)
COLAB_LINK_RE = re.compile(
    r'<a class="mf1-interaktivno-veza" '
    r'href="https://colab\.research\.google\.com/github/martibasic/'
    r'MF1_udzbenik/blob/main/notebooks/(?P<notebook>[^"]+\.ipynb)" '
    r'target="_blank" rel="noopener">Otvori interaktivni prikaz</a>'
)
LEGACY_TASK_RE = re.compile(
    r"(?m)^(?P<number>\d+\.\s+)\*\*(?P<level>T[1-4])\*\*\s+(?P<prompt>.+)$"
)
HINT_WITH_ANSWER_RE = re.compile(
    r"(?m)^[\t ]+\*\*(?:Natuknica|Naputak):\*\*\s*"
    r"(?P<hint>.*?)\s*\(Rješenje:\s*(?P<answer>.+)\)\s*$"
)
INLINE_CONTROL_RESULT_RE = re.compile(
    r"(?m)^(?P<task>\d+\.\s+\[\*\*T[1-4]\*\*\]\{#task-[A-Za-z0-9-]+\}.*?)"
    r"\s+\*\(Kontrolni rezultat:\s*(?P<answer>.+)\)\*\s*$"
)
HINT_CALLOUT_RE = re.compile(
    r"(?ms)^(?P<indent>[ \t]*)::: \{"
    r"(?P<attrs>\.callout-(?:note|tip)(?![^}\n]*data-hint-key)[^}\n]*)\}\s*\n"
    r"(?P=indent)### Naputak\s*\n(?P<body>.*?)"
    r"^(?P=indent):::\s*$"
)
RESULT_CALLOUT_RE = re.compile(
    r"(?ms)^(?P<indent>[ \t]*)::: \{"
    r"(?P<attrs>\.callout-(?:note|tip)(?![^}\n]*data-answer-key)[^}\n]*)\}\s*\n"
    r"(?P=indent)### Kontrolni rezultat\s*\n(?P<body>.*?)"
    r"^(?P=indent):::\s*$"
)
LEGACY_EXAMPLE_RE = re.compile(
    r"(?m)^::: \{\.(?P<class>mf1-(?:we|ch))\}\s*\n"
    r"(?P<label><p class=\"mf1-box-label\">(?P<title>[^\n]+)</p>)$"
)
MARKDOWN_IMAGE_RE = re.compile(
    r"(?m)^(?P<image>!\[(?P<alt>[^\]]*)\]\((?P<target>[^)]+)\))"
    r'''(?P<attrs>\{(?:[^}"']+|"[^"]*"|'[^']*')*\})?[ \t]*$'''
)
IMAGE_BLOCK_SPACING_RE = re.compile(
    r"(?m)^(?P<line>!\[[^\r\n]*\]\([^\r\n]*)[ \t]*\r?\n"
    r"(?=[^\r\n])"
)
JUPYTERLITE_ROOT = (
    "https://martibasic.github.io/MF1_udzbenik/jlite/lab/index.html?path="
)

# Kanonski broj poglavlja nije uvijek jednak starom prefiksu izvornog
# dokumenta: npr. nekadasnji U07 danas je javni U06. Ova je karta zato javno
# autorsko sucelje, a ne pomocna pretpostavka izvedena iz imena datoteke.
CANONICAL_SOURCE_CHAPTER = {
    "u01_osnove_fluida_i_pascalov_zakon.md": "u01",
    "u02_viskoznost_povrsinska_napetost_i_kapilarnost.md": "u02",
    "u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md": "u03",
    "u04_relativno_mirovanje_fluida.md": "u04",
    "u05_hidrostatske_sile_na_plohe.md": "u05",
    "u07_uzgon_plivanje_i_stabilnost.md": "u06",
    "u08_kontrolni_volumen_i_kontinuitet.md": "u07",
    "u09_bernoullijeva_jednadzba_idealnog_fluida.md": "u08",
    "u09_kompresibilni_idealni_tok.md": "u09",
    "u11_kolicina_gibanja_i_sile_strujanja.md": "u10",
    "u14_bezdimenzijski_brojevi_dimenzijska_analiza_i_slicnost.md": "u11",
    "u12_diferencijalni_opis_realnog_toka.md": "u12",
    "u13_gubici_cjevovodi_crpke_i_mreze.md": "u13",
    "u12_pokretne_lopatice_i_potisak.md": "u14",
    "u15_otvoreni_tokovi.md": "u15",
}
CANONICAL_SOURCE_TOPIC = {
    "u01_osnove_fluida_i_pascalov_zakon.md": "svojstva-tlak",
    "u02_viskoznost_povrsinska_napetost_i_kapilarnost.md": "reologija",
    "u03_hidrostaticka_raspodjela_tlaka_i_manometrija.md": "hidrostatika",
    "u04_relativno_mirovanje_fluida.md": "relativno-mirovanje",
    "u05_hidrostatske_sile_na_plohe.md": "sile-plohe",
    "u07_uzgon_plivanje_i_stabilnost.md": "uzgon-stabilitet",
    "u08_kontrolni_volumen_i_kontinuitet.md": "kinematika-kv",
    "u09_bernoullijeva_jednadzba_idealnog_fluida.md": "energijska-bilanca",
    "u09_kompresibilni_idealni_tok.md": "kompresibilni-tok",
    "u11_kolicina_gibanja_i_sile_strujanja.md": "momentum",
    "u14_bezdimenzijski_brojevi_dimenzijska_analiza_i_slicnost.md": "slicnost",
    "u12_diferencijalni_opis_realnog_toka.md": "realni-tok",
    "u13_gubici_cjevovodi_crpke_i_mreze.md": "cjevovodi",
    "u12_pokretne_lopatice_i_potisak.md": "turbostrojevi",
    "u15_otvoreni_tokovi.md": "otvoreni-tokovi",
}
PUBLIC_APPENDIX_TOPIC = {
    "d04_numericka_mehanika_fluida.md": "cfd-vv",
}


def slugify_task(prompt: str) -> str:
    text = re.sub(r"\$[^$]*\$", " ", prompt)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))
    words = re.findall(r"[a-z0-9]+", text.lower())
    slug = "-".join(words[:7]).strip("-")
    return slug[:72].rstrip("-") or "zadatak"


def slugify_example(label: str) -> str:
    text = re.sub(r"<(?:span|/span)[^>]*>", " ", label)
    text = re.sub(
        r"^(?:Riješeni primjer|Kratki primjer|Cjeloviti zadatak)\s*[-–—:]\s*",
        "",
        html.unescape(text).strip(),
        flags=re.IGNORECASE,
    )
    return slugify_task(text)


def label_display_equations(text: str, chapter_topic: str) -> str:
    """Dodaj trajne oznake neoznacenim prikaznim jednadzbama.

    ID kombinira trajnu temu poglavlja, naslov najblizeg odjeljka i lokalni
    brojac; ne ovisi o trenutačnom rednom broju poglavlja. Jednom zapisan
    ostaje dio izvora, pa kasnije umetanje jednadzbe ne preimenuje postojece
    oznake. Parser namjerno obrađuje samo Markdown izvan ogradenih kodnih
    blokova.
    """

    lines = text.splitlines(keepends=True)
    used = set(re.findall(r"#(eq-[A-Za-z0-9-]+)", text))
    section = "temelj"
    section_counts: dict[str, int] = {}
    in_code = False
    display_start: int | None = None
    display_section = section

    def fresh_id(topic: str) -> str:
        base_topic = slugify_task(topic)[:48].rstrip("-") or "temelj"
        count = section_counts.get(base_topic, 0) + 1
        while True:
            identifier = f"eq-{chapter_topic}-{base_topic}-{count:02d}"
            if identifier not in used:
                break
            count += 1
        section_counts[base_topic] = count
        used.add(identifier)
        return identifier

    for index, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r"^(```|~~~)", stripped):
            in_code = not in_code
            continue
        if in_code:
            continue

        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", stripped)
        if heading and display_start is None:
            section = heading.group(1)
        box_label = re.search(
            r'<p\s+class="mf1-box-label">(.+?)</p>', stripped, re.I
        )
        if box_label and display_start is None:
            section = box_label.group(1)
        task_anchor = re.search(r"\{#(task-[A-Za-z0-9-]+)\}", stripped)
        if task_anchor and display_start is None:
            section = task_anchor.group(1).removeprefix("task-")

        delimiter_count = line.count("$$")
        if display_start is None:
            if delimiter_count >= 2:
                if "{#eq-" not in line:
                    ending = "\n" if line.endswith("\n") else ""
                    body = line[:-1] if ending else line
                    lines[index] = f"{body} {{#{fresh_id(section)}}}{ending}"
            elif delimiter_count == 1:
                display_start = index
                display_section = section
        elif delimiter_count:
            block = "".join(lines[display_start : index + 1])
            if "{#eq-" not in block:
                ending = "\n" if line.endswith("\n") else ""
                body = line[:-1] if ending else line
                lines[index] = (
                    f"{body} {{#{fresh_id(display_section)}}}{ending}"
                )
            display_start = None

    return "".join(lines)


def widen_exercise_fences(text: str) -> str:
    """Omoguci pravilno ugnjezdivanje sklopivih callouta unutar liste zadataka."""

    output: list[str] = []
    in_exercises = False
    nested = 0
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if not in_exercises and re.fullmatch(
            r":{3,}\s+\{\.mf1-vjezbe-list\}", stripped
        ):
            ending = "\n" if line.endswith("\n") else ""
            output.append('::::: {.mf1-vjezbe-list}' + ending)
            in_exercises = True
            nested = 0
            continue
        if in_exercises:
            # Fenced blocks smiju imati najvise tri vodece praznine. Tri su
            # ujedno nastavna uvlaka iza oznake uredene liste ``1. ``.
            if line.startswith("    "):
                line = line[1:]
            elif line.startswith("\t"):
                line = "   " + line[1:]
            stripped = line.strip()
            if re.fullmatch(r":{3,}\s+\{[^}]+\}", stripped):
                nested += 1
            elif re.fullmatch(r":{3,}", stripped):
                if nested:
                    nested -= 1
                else:
                    ending = "\n" if line.endswith("\n") else ""
                    output.append(":::::" + ending)
                    in_exercises = False
                    continue
        output.append(line)
    return "".join(output)


def normalize(text: str, source_key: str = "source") -> str:
    def replace_ref(match: re.Match[str]) -> str:
        title = match.group("title").strip()
        number = CHAPTER_BY_TITLE.get(title)
        if number is None:
            return match.group(0)
        canonical_title = CANONICAL_TITLE_BY_CHAPTER[number]
        return (
            f'{match.group(1)}{number}</span><span class="mf1-ch-title">'
            f"{canonical_title}</span></span>"
        )

    text = REF_RE.sub(replace_ref, text)
    text = ALT_RE.sub(r"![\1]", text)
    text = re.sub(
        r'(?m)^::: \{\.callout-note(?:\s+[^}]*)?\}\s*\n'
        r'## Fizikalno značenje\s*$',
        '::: {.mf1-fizikalno-znacenje}\n'
        '<p class="mf1-box-label">Fizikalno značenje</p>',
        text,
    )

    used_example_ids = set(re.findall(r"#(ex-[A-Za-z0-9-]+)", text))

    def add_example_id(match: re.Match[str]) -> str:
        base = (
            f"ex-{source_key.split('_', 1)[0]}-"
            f"{slugify_example(match.group('title'))}"
        )
        identifier = base
        suffix = 2
        while identifier in used_example_ids:
            identifier = f"{base}-{suffix}"
            suffix += 1
        used_example_ids.add(identifier)
        return (
            f"::: {{#{identifier} .{match.group('class')}}}\n"
            f"{match.group('label')}"
        )

    text = LEGACY_EXAMPLE_RE.sub(add_example_id, text)

    used_figure_ids = set(re.findall(r"#(fig-[A-Za-z0-9-]+)", text))

    def add_figure_id(match: re.Match[str]) -> str:
        attrs = (match.group("attrs") or "{}")[1:-1].strip()
        if not re.search(r"#fig-[A-Za-z0-9-]+", attrs):
            base = (
                f"fig-{source_key.split('_', 1)[0]}-"
                f"{slugify_task(match.group('alt').lstrip('-–— '))}"
            )
            identifier = base
            suffix = 2
            while identifier in used_figure_ids:
                identifier = f"{base}-{suffix}"
                suffix += 1
            used_figure_ids.add(identifier)
            attrs = f"#{identifier}" + (f" {attrs}" if attrs else "")

        # Pandoc koristi tekst između uglatih zagrada kao natpis slike kada je
        # prisutan fig-* ID. Eksplicitni fig-alt zato je nužan da bi i stvarni
        # <img> u HTML-u imao pristupačan alternativni opis.
        if not re.search(r"(?:^|\s)fig-alt=", attrs):
            accessible_alt = match.group("alt").strip().replace('"', "&quot;")
            attrs += f' fig-alt="{accessible_alt}"'
        return f"{match.group('image')}{{{attrs}}}"

    text = MARKDOWN_IMAGE_RE.sub(add_figure_id, text)
    text = IMAGE_BLOCK_SPACING_RE.sub(lambda match: f"{match.group('line')}\n\n", text)

    used_task_ids = set(re.findall(r"#(task-[A-Za-z0-9-]+)", text))

    def add_task_id(match: re.Match[str]) -> str:
        base = f"task-{source_key.split('_', 1)[0]}-{slugify_task(match.group('prompt'))}"
        identifier = base
        suffix = 2
        while identifier in used_task_ids:
            identifier = f"{base}-{suffix}"
            suffix += 1
        used_task_ids.add(identifier)
        return (
            f"{match.group('number')}[**{match.group('level')}**]"
            f"{{#{identifier}}} {match.group('prompt')}"
        )

    text = LEGACY_TASK_RE.sub(add_task_id, text)
    text = TASK_ANCHOR_RE.sub(
        lambda match: f"[**{match.group('level')}**]{{#{match.group('id')}}}",
        text,
    )

    def collapse_hint(match: re.Match[str]) -> str:
        hint = match.group("hint").strip()
        answer = match.group("answer").strip()
        return (
            '    :::: {.content-visible .mf1-hint-online when-format="html"}\n'
            '    ::: {.callout-note collapse="true" data-hint-key="true"}\n'
            "    ### Naputak\n\n"
            f"    {hint}\n"
            "    :::\n"
            "    ::::\n\n"
            '    :::: {.content-visible .mf1-answer-online when-format="html"}\n'
            '    ::: {.callout-tip collapse="true" data-answer-key="true"}\n'
            "    ### Kontrolni rezultat\n\n"
            f"    {answer}\n"
            "    :::\n"
            "    ::::")

    text = HINT_WITH_ANSWER_RE.sub(collapse_hint, text)

    def hide_inline_result(match: re.Match[str]) -> str:
        answer = match.group("answer").strip()
        return (
            f"{match.group('task')}\n\n"
            '   :::: {.content-visible when-format="html"}\n'
            '   ::: {.callout-tip collapse="true" data-answer-key="true"}\n'
            "   ### Kontrolni rezultat\n\n"
            f"   {answer}\n"
            "   :::\n"
            "   ::::")

    text = INLINE_CONTROL_RESULT_RE.sub(hide_inline_result, text)

    def wrap_hint_callout(match: re.Match[str]) -> str:
        indent = match.group("indent")
        attrs = match.group("attrs").strip()
        body = match.group("body").rstrip()
        return (
            f'{indent}:::: {{.content-visible .mf1-hint-online when-format="html"}}\n'
            f'{indent}::: {{{attrs} data-hint-key="true"}}\n'
            f"{indent}### Naputak\n{body}\n"
            f"{indent}:::\n{indent}::::"
        )

    def wrap_result_callout(match: re.Match[str]) -> str:
        indent = match.group("indent")
        attrs = match.group("attrs").strip()
        body = match.group("body").rstrip()
        return (
            f'{indent}:::: {{.content-visible .mf1-answer-online when-format="html"}}\n'
            f'{indent}::: {{{attrs} data-answer-key="true"}}\n'
            f"{indent}### Kontrolni rezultat\n{body}\n"
            f"{indent}:::\n{indent}::::"
        )

    text = HINT_CALLOUT_RE.sub(wrap_hint_callout, text)
    text = RESULT_CALLOUT_RE.sub(wrap_result_callout, text)
    text = text.replace(
        ':::: {.content-visible when-format="html"}\n'
        '   ::: {.callout-tip collapse="true" data-answer-key="true"}',
        ':::: {.content-visible .mf1-answer-online when-format="html"}\n'
        '   ::: {.callout-tip collapse="true" data-answer-key="true"}',
    )

    # JupyterLite je primarni put bez prijave; Colab ostaje izricita pricuva.
    original = text

    def add_jupyterlite(match: re.Match[str]) -> str:
        notebook = match.group("notebook")
        if f"../jlite/lab/index.html?path={notebook}" in original:
            return match.group(0).replace(
                "Otvori interaktivni prikaz", "Pričuvno: otvori u Colabu"
            )
        jlite = (
            '<a class="mf1-interaktivno-veza" '
            f'href="../jlite/lab/index.html?path={notebook}">'
            "Pokreni u pregledniku</a>"
        )
        colab = match.group(0).replace(
            "Otvori interaktivni prikaz", "Pričuvno: otvori u Colabu"
        )
        return f"{jlite}\n{colab}"

    text = COLAB_LINK_RE.sub(add_jupyterlite, text)
    text = text.replace(
        'href="../jlite/lab/index.html?path=',
        f'href="{JUPYTERLITE_ROOT}',
    )
    text = widen_exercise_fences(text)
    text = text.replace("Ovaj `CH`", "Ovaj cjeloviti zadatak")
    text = text.replace("Ovaj CH", "Ovaj cjeloviti zadatak")
    text = text.replace("Ovaj `Val`", "Ovaj riješeni primjer")
    text = text.replace("Ovaj Val", "Ovaj riješeni primjer")
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    changed: list[Path] = []
    for path in sorted(SOURCE.glob("*.md")):
        original = path.read_text(encoding="utf-8")
        chapter_code = CANONICAL_SOURCE_CHAPTER.get(path.name)
        source_key = chapter_code or path.stem
        updated = normalize(original, source_key)
        equation_topic = CANONICAL_SOURCE_TOPIC.get(
            path.name, PUBLIC_APPENDIX_TOPIC.get(path.name)
        )
        if equation_topic:
            updated = label_display_equations(updated, equation_topic)
        if updated != original:
            changed.append(path.relative_to(ROOT))
            if args.write:
                path.write_text(updated, encoding="utf-8", newline="\n")

    if changed:
        action = "updated" if args.write else "needs normalization"
        for path in changed:
            print(f"{action}: {path}")
        return 0 if args.write else 1

    print("Public references and alternative text are normalized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
