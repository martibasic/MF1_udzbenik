"""Generiraj tiskani kljuc naputaka i kontrolnih rezultata iz zadataka.

Web prikazuje isti rezultat tek nakon otvaranja sklopivog bloka. Typst skriva
rezultat uz zadatak, a ovaj dodatak ga okuplja na jednome mjestu. Bez
``--write`` skripta provjerava je li generirani izvor aktualan.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "source" / "d06_kljuc_kontrolnih_rezultata.md"
WRAPPERS = [
    "u01_osnove_fluida_i_pascalov_zakon.qmd",
    "u02_viskoznost_povrsinska_napetost_i_kapilarnost.qmd",
    "u03_hidrostaticka_raspodjela_tlaka_i_manometrija.qmd",
    "u04_relativno_mirovanje_fluida.qmd",
    "u05_hidrostatske_sile_na_plohe.qmd",
    "u06_uzgon_plivanje_i_stabilnost.qmd",
    "u07_kinematika_kontrolni_volumen_i_kontinuitet.qmd",
    "u08_energijska_jednadzba_i_bernoulli.qmd",
    "u09_kompresibilni_idealni_tok.qmd",
    "u10_kolicina_i_moment_kolicine_gibanja.qmd",
    "u11_dimenzijska_analiza_i_slicnost.qmd",
    "u12_diferencijalni_opis_realnog_toka.qmd",
    "u13_gubici_cjevovodi_crpke_i_mreze.qmd",
    "u14_turbostrojevi_i_propulzija.qmd",
    "u15_otvoreni_tokovi.qmd",
]

INCLUDE_RE = re.compile(r"\{\{<\s*include\s+\.\./source/([^ >]+)\s*>\}\}")
TITLE_RE = re.compile(r'^title:\s*["\'](?P<title>.+?)["\']\s*$', re.MULTILINE)
TASK_RE = re.compile(
    r"(?m)^(?P<number>\d+)\.\s+\[\*\*(?P<level>T[1-4])\*\*\]"
    r"\{#(?P<id>task-[A-Za-z0-9-]+)\}\s+(?P<prompt>.+)$"
)
HEADING_TASK_RE = re.compile(
    r"(?m)^###\s+(?P<title>.+?)\s+\{#(?P<id>task-[A-Za-z0-9-]+)\}\s*$"
)
HEADING_LEVEL_RE = re.compile(
    r"(?m)^\*\*Razina:\s*(?P<level>T[1-4])\.\*\*\s*(?P<prompt>.*)$"
)
TASK_ANCHOR_RE = re.compile(r"(?m)^.*\{#task-[A-Za-z0-9-]+\}.*$")
HINT_RE = re.compile(
    r"(?ms)^[ \t]*::: \{\.callout-(?:note|tip)[^\n]*data-hint-key=\"true\"[^\n]*\}\s*\n"
    r"[ \t]*### Naputak\s*\n\s*(?P<hint>.*?)\n[ \t]*:::\s*$"
)
ANSWER_RE = re.compile(
    r"(?ms)^[ \t]*::: \{\.callout-(?:note|tip)[^\n]*data-answer-key=\"true\"[^\n]*\}\s*\n"
    r"[ \t]*### Kontrolni rezultat\s*\n\s*(?P<answer>.*?)\n[ \t]*:::\s*$"
)


def compact(text: str, limit: int = 240) -> str:
    value = re.sub(r"\s+", " ", text.strip())
    if len(value) <= limit:
        return value
    cut = value.rfind(" ", 0, limit - 1)
    return value[: max(cut, 1)].rstrip(" ,;:") + "…"


def portable_xrefs(text: str, wrapper_name: str) -> str:
    """Pretvori lokalne Pandoc xrefove u veze koje rade i u izdvojenom D06."""

    return re.sub(
        r"\[-@(?P<id>(?:eq|fig|tbl|sec)-[A-Za-z0-9_-]+)\]",
        lambda match: (
            f"[odgovarajući izraz]({wrapper_name}#{match.group('id')})"
        ),
        text,
    )


def tasks_from_source(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    matches = list(TASK_ANCHOR_RE.finditer(text))
    tasks: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        anchor_line = match.group(0)
        chunk = text[match.end() : end]
        ordered = TASK_RE.fullmatch(anchor_line)
        heading = HEADING_TASK_RE.fullmatch(anchor_line)
        if ordered:
            number = ordered.group("number")
            level = ordered.group("level")
            task_id = ordered.group("id")
            prompt = ordered.group("prompt")
        elif heading:
            level_match = HEADING_LEVEL_RE.search(chunk)
            if not level_match:
                raise ValueError(f"Zadatak {heading.group('id')} nema razinu")
            statement_start = level_match.end()
            statement_tail = chunk[statement_start:]
            statement_tail = re.split(
                r"(?m)^\s*:{3,}\s*(?:\{|$)|^###\s+", statement_tail, maxsplit=1
            )[0]
            number = str(len(tasks) + 1)
            level = level_match.group("level")
            task_id = heading.group("id")
            statement = " ".join(
                part for part in (level_match.group("prompt"), statement_tail) if part.strip()
            )
            prompt = f"{heading.group('title')} — {statement}"
        else:
            raise ValueError(f"Nepodržan zapis zadatka u {path.name}: {anchor_line}")
        hint_match = HINT_RE.search(chunk)
        answer_match = ANSWER_RE.search(chunk)
        tasks.append(
            {
                "number": number,
                "level": level,
                "id": task_id,
                "prompt": compact(prompt),
                "hint": compact(hint_match.group("hint"), 500) if hint_match else "",
                "answer": compact(answer_match.group("answer"), 500)
                if answer_match
                else "Nema jednoga kontrolnog broja. Vrednuju se izbor modela i pretpostavki, zatvaranje bilance, provjera valjanosti te jasno iskazana nesigurnost ili podatci koji nedostaju.",
            }
        )
    return tasks


def build() -> str:
    lines = [
        "<!-- Generirano skriptom scripts/generate_exercise_key.py; ne uređivati ručno. -->",
        "",
        "## Ključ naputaka i kontrolnih rezultata",
        "",
        "Ovaj dodatak odvaja naputke i kontrolne rezultate od teksta zadatka u tiskanom izdanju. Ne zamjenjuje postupak: prije provjere treba zapisati model, pretpostavke, jedinice i barem jednu neovisnu fizikalnu provjeru. Otvoreni T3/T4 zadatci namjerno nemaju jedinstven broj.",
        "",
    ]
    seen: set[str] = set()
    total = 0
    for wrapper_name in WRAPPERS:
        wrapper = ROOT / "chapters" / wrapper_name
        wrapper_text = wrapper.read_text(encoding="utf-8")
        title_match = TITLE_RE.search(wrapper_text)
        title = title_match.group("title") if title_match else wrapper.stem
        chapter_tasks: list[dict[str, str]] = []
        for source_name in INCLUDE_RE.findall(wrapper_text):
            chapter_tasks.extend(tasks_from_source(ROOT / "source" / source_name))
        if not chapter_tasks:
            raise ValueError(f"Nema zadataka u javnom poglavlju {wrapper_name}")
        lines.extend([f"## {title}", ""])
        for local_number, task in enumerate(chapter_tasks, start=1):
            if task["id"] in seen:
                raise ValueError(f"Duplicirani stabilni ID: {task['id']}")
            seen.add(task["id"])
            total += 1
            key_id = f"key-{task['id']}"
            prompt = portable_xrefs(task["prompt"], wrapper_name)
            hint = portable_xrefs(task["hint"], wrapper_name)
            answer = portable_xrefs(task["answer"], wrapper_name)
            lines.extend(
                [
                    f"### Zadatak {local_number} · {task['level']} {{#{key_id}}}",
                    "",
                    f"[Vrati se na zadatak]({wrapper_name}#{task['id']})",
                    "",
                    f"**Sažetak.** {prompt}",
                    "",
                    *(
                        [f"**Naputak.** {hint}", ""]
                        if hint
                        else []
                    ),
                    f"**Kontrolni rezultat ili kriterij.** {answer}",
                    "",
                ]
            )
    lines.extend(
        [
            "::: {.mf1-mini-summary}",
            '<p class="mf1-box-label">Opseg ključa</p>',
            "",
            f"Ključ obuhvaća {total} zadataka iz javnog toka U01–U15. Pogrešku u rezultatu prijavite prema stabilnom ID-ju zadatka kroz errata obrazac.",
            ":::",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    expected = build()
    actual = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else None
    if actual == expected:
        print("Kljuc kontrolnih rezultata je aktualan.")
        return 0
    if args.write:
        OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
        print(f"Azuriran: {OUTPUT.relative_to(ROOT)}")
        return 0
    print(f"Zastario ili nedostaje: {OUTPUT.relative_to(ROOT)}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
