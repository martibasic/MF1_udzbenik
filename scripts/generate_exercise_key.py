"""Generiraj tiskani kljuc smjernica i kontrolnih rezultata iz zadataka.

Web prikazuje isti rezultat tek nakon otvaranja sklopivog bloka. Typst skriva
rezultat uz zadatak, a ovaj dodatak ga okuplja na jednome mjestu. Bez
``--write`` skripta provjerava je li generirani izvor aktualan.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from book_model import load_book, documents
BOOK = load_book()
BOOK_CHAPTERS = documents(BOOK, kind="chapter")


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "source" / "d06_kljuc_kontrolnih_rezultata.md"
WRAPPERS = [Path(doc["path"]).name for doc in BOOK_CHAPTERS]

INCLUDE_RE = re.compile(r"\{\{<\s*include\s+\.\./source/([^ >]+)\s*>\}\}")
TITLE_RE = re.compile(r'^title:\s*["\'](?P<title>.+?)["\']\s*$', re.MULTILINE)
HEADING_TASK_RE = re.compile(
    r"(?m)^###\s+(?:Z(?P<number>\d+)\.\s+)?(?P<title>.+?)\s+"
    r"\{#(?P<id>task-[A-Za-z0-9-]+)\s+\.unnumbered\s+\.unlisted\}\s*$"
)
TASK_LEVEL_RE = re.compile(
    r"(?m)^\[Razina:\s*(?P<level>T[1-4])\]\{\.mf1-task-level\}\s*$"
)
TASK_ANCHOR_RE = re.compile(r"(?m)^.*\{#task-[A-Za-z0-9-]+\b[^}]*\}.*$")
HINT_RE = re.compile(
    r"(?ms)^[ \t]*::: \{\.callout-(?:note|tip)[^\n]*data-hint-key=\"true\"[^\n]*\}\s*\n"
    r"[ \t]*### (?:Naputak|Smjernica)\s*\n\s*(?P<hint>.*?)\n[ \t]*:::\s*$"
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
    if cut < 0:
        cut = value.find(" ")
        if cut < 0:
            return value
    # Finish any formula crossing the summary boundary, even if it exceeds
    # the preferred length. Cutting TeX leaves broken math in HTML and PDF.
    for formula in re.finditer(r"(?<!\\)\$(?:\\.|[^\\$])*\$", value):
        if formula.start() < cut < formula.end():
            cut = formula.end()
            break
    return value[:cut].rstrip(" ,;:") + ("…" if cut < len(value) else "")


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
        heading = HEADING_TASK_RE.fullmatch(anchor_line)
        if not heading:
            raise ValueError(f"Nepodržan zapis zadatka u {path.name}: {anchor_line}")
        number = str(index + 1)
        level_match = TASK_LEVEL_RE.search(chunk)
        if not level_match:
            raise ValueError(f"Zadatak {heading.group('id')} nema razinu")
        prompt = re.split(
            r"(?m)^\s*:{3,}\s*(?:\{|$)|^###\s+|^\[Razina:", chunk, maxsplit=1
        )[0]
        hint_match = HINT_RE.search(chunk)
        answer_match = ANSWER_RE.search(chunk)
        # Višedijelni odgovor može izričito tražiti cijeli tekst u tiskanom
        # ključu kako skraćivanje ne bi uklonilo konačnu odluku ili njezin uvjet.
        complete_answer = bool(answer_match and 'data-key-full="true"'
                               in answer_match.group(0).splitlines()[0])
        tasks.append(
            {
                "number": number,
                "title": heading.group("title"),
                "level": level_match.group("level"),
                "id": heading.group("id"),
                "prompt": compact(prompt),
                "hint": compact(hint_match.group("hint"), 500) if hint_match else "",
                "answer": compact(answer_match.group("answer"),
                                  len(answer_match.group("answer")) if complete_answer else 500)
                if answer_match
                else "Nema jednoga kontrolnog broja. Vrednuju se izbor modela i pretpostavki, zatvaranje bilance, provjera valjanosti te jasno iskazana nesigurnost ili podatci koji nedostaju.",
            }
        )
    return tasks


def build(root=ROOT) -> str:
    lines = [
        "<!-- Generirano skriptom scripts/generate_exercise_key.py; ne uređivati ručno. -->",
        "",
        "## Ključ smjernica i kontrolnih rezultata",
        "",
        "Pronađi poglavlje i oznaku zadatka Z1–Z6. Uz svaki zadatak nalaze se kratka smjernica, kontrolni rezultat ili kriterij te poveznica na puni iskaz.",
        "",
        "Rezultat usporedi tek nakon vlastitog pokušaja. Provjeri i model, pretpostavke, jedinice te barem jednu neovisnu fizikalnu vezu. Otvoreni dijelovi zadataka T3 i T4 mogu imati više prihvatljivih odgovora.",
        "",
    ]
    seen: set[str] = set()
    total = 0
    for chapter in documents(load_book(root), kind="chapter"):
        wrapper_name = Path(chapter["path"]).name
        title = chapter["title"]
        chapter_tasks = tasks_from_source(root / chapter["source"])
        if not chapter_tasks:
            raise ValueError(f"Nema zadataka u javnom poglavlju {wrapper_name}")
        lines.extend([f"## {title}", ""])
        for task in chapter_tasks:
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
                    f"### Z{task['number']}. {task['title']} {{#{key_id} .unnumbered .unlisted}}",
                    "",
                    f"[Vrati se na zadatak]({wrapper_name}#{task['id']})",
                    "",
                    f"**Sažetak.** {prompt}",
                    "",
                    *(
                        [f"**Smjernica postupka.** {hint}", ""]
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
            f"Ključ obuhvaća {total} zadataka iz poglavlja 1–15. Pri prijavi pogreške navedi poglavlje, oznaku zadatka i poveznicu na njega.",
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
