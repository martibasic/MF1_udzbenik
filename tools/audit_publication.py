"""Strogi audit kanonskoga javnog izdanja udžbenika MF1.

Za razliku od numeričkih verifiera, ovaj alat provjerava autorski i
publikacijski ugovor: 15 kanonskih poglavlja, inventar primjera i zadataka,
raspodjelu razina, stabilne i jedinstvene oznake, slike, citate te poveznice
na notebookove. Namjerno čita samo izvore uključene iz nove javne strukture;
stari URL-ovi mogu ostati kao preusmjerenja bez udvostručavanja sadržaja.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import fnmatch
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = REPO_ROOT / "chapters"
SOURCE_DIR = REPO_ROOT / "source"
QUARTO_CONFIG = REPO_ROOT / "_quarto.yml"

CANONICAL_WRAPPERS = [
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
APPENDIX_WRAPPERS = [
    "d01_sazetak_formula_i_oznaka.qmd",
    "d02_pojmovnik.qmd",
    "d03_tipicne_pogreske_po_poglavljima.qmd",
    "d04_numericka_mehanika_fluida.qmd",
    "d05_literatura.qmd",
    "d06_kljuc_kontrolnih_rezultata.qmd",
]
EXPECTED_HOURS = [8, 9, 9, 8, 11, 10, 10, 10, 9, 10, 9, 10, 12, 9, 9]

EXPECTED_LEVELS = Counter({"T1": 2, "T2": 2, "T3": 1, "T4": 1})
INCLUDE_RE = re.compile(r"\{\{<\s*include\s+(\.\./source/[^\s>}]+)\s*>\}\}")
EXAMPLE_RE = re.compile(r"\{#(ex-[A-Za-z0-9_-]+)\b")
TASK_RE = re.compile(r"\{#(task-[A-Za-z0-9_-]+)\b")
LEVEL_RE = re.compile(r"(?:\[\*\*|Razina:\s*)(T[1-4])")
PANDOC_ID_RE = re.compile(r"\{#([A-Za-z][A-Za-z0-9_-]*)\b")
FIGURE_RE = re.compile(
    r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?:\s+[^)]*)?\)"
    r'''(?:\{(?P<attrs>(?:[^}"']+|"[^"]*"|'[^']*')*)\})?'''
)
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"'][^>]*>", re.I)
HTML_ALT_RE = re.compile(r"<img\b[^>]*\balt=[\"']([^\"']*)[\"'][^>]*>", re.I)
CITATION_RE = re.compile(r"(?<![\w@])@([A-Za-z][A-Za-z0-9_.:-]*)")
BIB_KEY_RE = re.compile(r"^\s*@\w+\s*\{\s*([^,\s]+)\s*,", re.M)
INTERNAL_ALT_RE = re.compile(r"\b(?:Val|CH)\s*\d+\b|\b(?:val|ch)[-_]?\d+\b")
JUPYTERLITE_RE = re.compile(
    r"https://martibasic\.github\.io/MF1_udzbenik/jlite/lab/index\.html\?path="
    r"([A-Za-z0-9_.-]+\.ipynb)"
)
DISPLAY_EQUATION_RE = re.compile(
    r"\$\$(?P<body>.*?)\$\$(?:[ \t]*\{#(?P<id>eq-[A-Za-z0-9_-]+)\})?",
    re.S,
)
WORKLOAD_RE = re.compile(
    r"\*\*Procijenjeno vrijeme rada uz udžbenik:\*\*\s*(\d+)\s+sati",
    re.I,
)
HINT_HEADING_RE = re.compile(r"(?m)^\s*###\s+Naputak\s*$")
RESULT_HEADING_RE = re.compile(r"(?m)^\s*###\s+Kontrolni rezultat\s*$")
HINT_KEY_RE = re.compile(r'data-hint-key="true"')
ANSWER_KEY_RE = re.compile(r'data-answer-key="true"')

XREF_PREFIXES = ("eq-", "fig-", "sec-", "tbl-", "lst-", "thm-", "ex-", "task-")


@dataclass(frozen=True)
class Chapter:
    number: int
    wrapper: Path
    source: Path
    text: str


def _rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def _project_sequence(config_text: str, key: str) -> list[str]:
    """Pročitaj jednostavan listovni ključ iz odjeljka ``project``.

    Projektna konfiguracija namjerno koristi blokovne YAML liste. Ovaj mali
    parser ne pokušava zamijeniti YAML parser, nego auditira upravo taj javni
    ugovor bez uvođenja još jedne ovisnosti u izvorne provjere.
    """

    lines = config_text.splitlines()
    header = f"  {key}:"
    try:
        start = next(index for index, line in enumerate(lines) if line == header)
    except StopIteration:
        return []
    items: list[str] = []
    for line in lines[start + 1 :]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indentation = len(line) - len(line.lstrip(" "))
        if indentation <= 2:
            break
        match = re.match(r"^\s{4}-\s+(.+?)\s*$", line)
        if match:
            item = match.group(1).split(" #", 1)[0].strip().strip("\"'")
            items.append(item.replace("\\", "/"))
    return items


def _audit_quarto_contract() -> tuple[dict[str, object], list[str]]:
    issues: list[str] = []
    if not QUARTO_CONFIG.is_file():
        return {}, ["nedostaje _quarto.yml"]
    config_text = QUARTO_CONFIG.read_text(encoding="utf-8")
    render_patterns = _project_sequence(config_text, "render")
    resources = _project_sequence(config_text, "resources")
    if not render_patterns:
        issues.append("_quarto.yml nema čitljiv project.render popis")
    expected_inputs = [
        "index.qmd",
        "chapters/u00_kako_koristiti_udzbenik.qmd",
        *(f"chapters/{name}" for name in CANONICAL_WRAPPERS),
        *(f"chapters/{name}" for name in APPENDIX_WRAPPERS),
        "chapters/za_ispis.qmd",
        "za_ispis.qmd",
    ]
    for expected in expected_inputs:
        if not any(fnmatch.fnmatchcase(expected, pattern) for pattern in render_patterns):
            issues.append(f"_quarto.yml project.render ne obuhvaća {expected}")

    leaked_resources = [
        item
        for item in resources
        if item.lstrip("./").lower() == "source"
        or item.lstrip("./").lower().startswith("source/")
    ]
    if leaked_resources:
        issues.append(
            "kanonski source/ ne smije biti javni Quarto resource: "
            + ", ".join(leaked_resources)
        )
    for required in ("assets/**", "data/cfd/**"):
        if required not in resources:
            issues.append(f"_quarto.yml project.resources ne sadrži {required}")
    return {
        "render_pattern_count": len(render_patterns),
        "public_resource_count": len(resources),
    }, issues


def load_chapters() -> tuple[list[Chapter], list[str]]:
    chapters: list[Chapter] = []
    issues: list[str] = []
    for number, wrapper_name in enumerate(CANONICAL_WRAPPERS, start=1):
        wrapper = CHAPTER_DIR / wrapper_name
        if not wrapper.is_file():
            issues.append(f"U{number:02}: nedostaje kanonski omotač {_rel(wrapper)}")
            continue
        wrapper_text = wrapper.read_text(encoding="utf-8")
        matches = INCLUDE_RE.findall(wrapper_text)
        if len(matches) != 1:
            issues.append(
                f"U{number:02}: kanonski omotač mora imati točno jedan source include; "
                f"nađeno {len(matches)}"
            )
            continue
        source = (wrapper.parent / matches[0]).resolve()
        if SOURCE_DIR.resolve() not in source.parents:
            issues.append(f"U{number:02}: include izlazi iz source/: {_rel(source)}")
            continue
        if not source.is_file():
            issues.append(f"U{number:02}: nedostaje uključeni izvor {_rel(source)}")
            continue
        chapters.append(
            Chapter(number, wrapper, source, source.read_text(encoding="utf-8"))
        )
    return chapters, issues


def _resolve_asset(chapter: Chapter, raw_path: str) -> Path | None:
    if raw_path.startswith(("http://", "https://", "data:")):
        return None
    path_without_fragment = raw_path.split("#", 1)[0].split("?", 1)[0]
    return (chapter.wrapper.parent / path_without_fragment).resolve()


def _bibliography_keys() -> set[str]:
    bibliography = REPO_ROOT / "references.bib"
    if not bibliography.is_file():
        return set()
    return set(BIB_KEY_RE.findall(bibliography.read_text(encoding="utf-8")))


def _svg_accessibility(path: Path) -> list[str]:
    issues: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        return [f"{_rel(path)}: SVG nije valjan XML ({exc})"]

    local = lambda tag: tag.rsplit("}", 1)[-1]
    children = list(root)
    titles = [child for child in children if local(child.tag) == "title"]
    descriptions = [child for child in children if local(child.tag) == "desc"]
    if "viewBox" not in root.attrib:
        issues.append(f"{_rel(path)}: SVG nema viewBox")
    if root.attrib.get("role") != "img":
        issues.append(f"{_rel(path)}: SVG mora imati role=\"img\"")
    if not titles or not "".join(titles[0].itertext()).strip():
        issues.append(f"{_rel(path)}: SVG nema smislen title")
    if not descriptions or not "".join(descriptions[0].itertext()).strip():
        issues.append(f"{_rel(path)}: SVG nema smislen desc")
    labelled = set(root.attrib.get("aria-labelledby", "").split())
    title_ids = {item.attrib.get("id") for item in titles if item.attrib.get("id")}
    desc_ids = {
        item.attrib.get("id") for item in descriptions if item.attrib.get("id")
    }
    if not title_ids or not desc_ids or not (title_ids | desc_ids).issubset(labelled):
        issues.append(
            f"{_rel(path)}: aria-labelledby mora upućivati na title i desc"
        )
    tiny_sizes: list[float] = []
    for element in root.iter():
        raw_size = element.attrib.get("font-size", "").strip()
        if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", raw_size):
            # Relativni tspan indeksi (npr. 0.7em) nasljeđuju veličinu roditelja.
            continue
        size = float(raw_size)
        if 0 < size < 9:
            tiny_sizes.append(size)
    if tiny_sizes:
        issues.append(
            f"{_rel(path)}: tekst u SVG-u manji je od 9 jedinica "
            f"(minimum {min(tiny_sizes):g})"
        )
    return issues


def audit() -> tuple[dict[str, object], list[str]]:
    chapters, issues = load_chapters()
    quarto_report, quarto_issues = _audit_quarto_contract()
    issues.extend(quarto_issues)
    all_ids: list[tuple[str, str]] = []
    cited_keys: set[str] = set()
    referenced_svgs: set[Path] = set()
    jupyterlite_notebooks: set[str] = set()
    chapter_rows: list[dict[str, object]] = []
    equation_count = 0

    for chapter in chapters:
        code = f"U{chapter.number:02}"
        examples = EXAMPLE_RE.findall(chapter.text)
        tasks = TASK_RE.findall(chapter.text)
        levels = LEVEL_RE.findall(chapter.text)
        # Razine u tekstu prije liste zadataka mogu pripadati primjerima; zadnjih
        # šest pripada šest zadataka po autorskom ugovoru.
        task_levels = levels[-len(tasks) :] if tasks else []
        if not 5 <= len(examples) <= 7:
            issues.append(
                f"{code}: očekuje se 5–7 riješenih primjera; nađeno {len(examples)}"
            )
        if len(tasks) != 6:
            issues.append(f"{code}: očekuje se točno 6 zadataka; nađeno {len(tasks)}")
        if Counter(task_levels) != EXPECTED_LEVELS:
            issues.append(
                f"{code}: razine zadataka moraju biti 2×T1, 2×T2, T3 i T4; "
                f"nađeno {dict(Counter(task_levels))}"
            )
        if not any(
            marker in chapter.text
            for marker in ("mf1-samoprovjera", "mf1-questions", "Konceptualna provjera")
        ):
            issues.append(f"{code}: nedostaje konceptualna samoprovjera bez formule")
        if "mf1-zavrsni-okvir" not in chapter.text:
            issues.append(f"{code}: nedostaje završni okvir granica i poruke modela")

        hint_headings = len(HINT_HEADING_RE.findall(chapter.text))
        hint_keys = len(HINT_KEY_RE.findall(chapter.text))
        result_headings = len(RESULT_HEADING_RE.findall(chapter.text))
        answer_keys = len(ANSWER_KEY_RE.findall(chapter.text))
        if hint_headings != hint_keys:
            issues.append(
                f"{code}: svaki naputak mora biti označen za odvojeni ispis; "
                f"naslovi={hint_headings}, oznake={hint_keys}"
            )
        if result_headings != answer_keys:
            issues.append(
                f"{code}: svaki kontrolni rezultat mora biti označen za odvojeni ispis; "
                f"naslovi={result_headings}, oznake={answer_keys}"
            )

        workload = WORKLOAD_RE.findall(chapter.text)
        expected_hours = EXPECTED_HOURS[chapter.number - 1]
        if workload != [str(expected_hours)]:
            issues.append(
                f"{code}: procijenjeno vrijeme mora biti {expected_hours} sati; "
                f"nađeno {workload or 'ništa'}"
            )

        equations = list(DISPLAY_EQUATION_RE.finditer(chapter.text))
        equation_count += len(equations)
        for ordinal, equation in enumerate(equations, start=1):
            if equation.group("id") is None:
                issues.append(
                    f"{code}: prikazna jednadžba {ordinal} nema stabilni eq-* ID"
                )

        for item_id in PANDOC_ID_RE.findall(chapter.text):
            all_ids.append((item_id, code))

        for match in FIGURE_RE.finditer(chapter.text):
            alt = re.sub(r"\s+", " ", match.group("alt")).strip()
            attrs = match.group("attrs") or ""
            if not alt:
                issues.append(f"{code}: slika bez alternativnog teksta")
            if INTERNAL_ALT_RE.search(alt):
                issues.append(f"{code}: alternativni tekst s internom oznakom: {alt!r}")
            if "#fig-" not in attrs:
                issues.append(f"{code}: slika nema stabilni fig-* ID: {alt[:70]!r}")
            if not re.search(r'(?:^|\s)fig-alt=["\']', attrs):
                issues.append(f"{code}: slika nema eksplicitni fig-alt: {alt[:70]!r}")
            asset = _resolve_asset(chapter, match.group("path"))
            if asset is not None:
                if not asset.is_file():
                    issues.append(f"{code}: nedostaje slika {_rel(asset)}")
                elif asset.suffix.lower() == ".svg":
                    referenced_svgs.add(asset)

        html_alts = HTML_ALT_RE.findall(chapter.text)
        for alt in html_alts:
            if not alt.strip():
                issues.append(f"{code}: HTML slika bez alternativnog teksta")
            if INTERNAL_ALT_RE.search(alt):
                issues.append(f"{code}: HTML alt s internom oznakom: {alt!r}")
        for raw_path in HTML_IMAGE_RE.findall(chapter.text):
            asset = _resolve_asset(chapter, raw_path)
            if asset is not None and not asset.is_file():
                issues.append(f"{code}: nedostaje HTML slika {_rel(asset)}")

        for key in CITATION_RE.findall(chapter.text):
            if not key.startswith(XREF_PREFIXES):
                cited_keys.add(key)
        jupyterlite_notebooks.update(JUPYTERLITE_RE.findall(chapter.text))
        chapter_rows.append(
            {
                "chapter": code,
                "source": _rel(chapter.source),
                "examples": len(examples),
                "tasks": len(tasks),
                "levels": task_levels,
            }
        )

    # Dodaci su dio javnoga izdanja i dijele isti prostor stabilnih ID-jeva.
    # Njihovi primjeri i zadatci ne ulaze u nastavnu matricu glavnih poglavlja.
    appendix_count = 0
    for appendix_name in APPENDIX_WRAPPERS:
        wrapper = CHAPTER_DIR / appendix_name
        code = appendix_name[:3].upper()
        if not wrapper.is_file():
            issues.append(f"{code}: nedostaje javni omotač {_rel(wrapper)}")
            continue
        matches = INCLUDE_RE.findall(wrapper.read_text(encoding="utf-8"))
        if len(matches) != 1:
            issues.append(f"{code}: omotač mora imati točno jedan source include")
            continue
        source = (wrapper.parent / matches[0]).resolve()
        if not source.is_file():
            issues.append(f"{code}: nedostaje uključeni izvor {_rel(source)}")
            continue
        appendix_count += 1
        text = source.read_text(encoding="utf-8")
        for item_id in PANDOC_ID_RE.findall(text):
            all_ids.append((item_id, code))
        for key in CITATION_RE.findall(text):
            if not key.startswith(XREF_PREFIXES):
                cited_keys.add(key)
        equations = list(DISPLAY_EQUATION_RE.finditer(text))
        equation_count += len(equations)
        for ordinal, equation in enumerate(equations, start=1):
            if equation.group("id") is None:
                issues.append(
                    f"{code}: prikazna jednadžba {ordinal} nema stabilni eq-* ID"
                )

    matrix = REPO_ROOT / "docs" / "kurikularna_matrica.md"
    if not matrix.is_file():
        issues.append("nedostaje docs/kurikularna_matrica.md")
    else:
        matrix_rows: dict[int, int] = {}
        for line in matrix.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\|\s*(\d+)\s*\|.*\|\s*(\d+)\s*\|\s*$", line)
            if match:
                matrix_rows[int(match.group(1))] = int(match.group(2))
        expected_matrix = {0: 2, **dict(enumerate(EXPECTED_HOURS, start=1))}
        if matrix_rows != expected_matrix:
            issues.append(
                "kurikularna matrica nema kanonsku raspodjelu 145 sati: "
                f"{matrix_rows}"
            )
        elif sum(matrix_rows.values()) != 145:
            issues.append(
                f"kurikularna matrica zbraja {sum(matrix_rows.values())}, ne 145 sati"
            )

    introduction = SOURCE_DIR / "u00_kako_koristiti_udzbenik.md"
    if not introduction.is_file() or not re.search(
        r"\b145\s+sati rada uz udžbenik\b",
        introduction.read_text(encoding="utf-8") if introduction.is_file() else "",
        re.I,
    ):
        issues.append("U00 mora navesti ukupno 145 sati rada uz udžbenik")

    duplicates = {
        item_id: locations
        for item_id, locations in (
            (item_id, [code for found, code in all_ids if found == item_id])
            for item_id in {found for found, _ in all_ids}
        )
        if len(locations) > 1
    }
    for item_id, locations in sorted(duplicates.items()):
        issues.append(f"duplicirani stabilni ID #{item_id}: {', '.join(locations)}")

    total_examples = sum(int(row["examples"]) for row in chapter_rows)
    if not 80 <= total_examples <= 90:
        issues.append(
            f"glavni tekst mora imati 80–90 riješenih primjera; nađeno {total_examples}"
        )

    bibliography_keys = _bibliography_keys()
    if not bibliography_keys:
        issues.append("references.bib nedostaje ili nema čitljivih zapisa")
    for key in sorted(cited_keys - bibliography_keys):
        issues.append(f"citat @{key} nema zapis u references.bib")

    for svg in sorted(referenced_svgs):
        issues.extend(_svg_accessibility(svg))

    notebook_inventory = {
        path.name for path in (REPO_ROOT / "notebooks").glob("u??_*.ipynb")
    }
    missing_jlite = sorted(notebook_inventory - jupyterlite_notebooks)
    stale_jlite = sorted(jupyterlite_notebooks - notebook_inventory)
    if missing_jlite:
        issues.append(
            "notebookovi bez javne JupyterLite poveznice: " + ", ".join(missing_jlite)
        )
    if stale_jlite:
        issues.append(
            "JupyterLite poveznice na nepostojeće notebookove: "
            + ", ".join(stale_jlite)
        )

    report: dict[str, object] = {
        "chapters": chapter_rows,
        "chapter_count": len(chapters),
        "appendix_count": appendix_count,
        "example_count": total_examples,
        "task_count": sum(int(row["tasks"]) for row in chapter_rows),
        "stable_id_count": len(all_ids),
        "equation_count": equation_count,
        "workload_hours": 2 + sum(EXPECTED_HOURS),
        "referenced_svg_count": len(referenced_svgs),
        "citation_count": len(cited_keys),
        "jupyterlite_count": len(jupyterlite_notebooks),
        **quarto_report,
    }
    return report, issues


def main() -> int:
    report, issues = audit()
    print("Kanonska struktura MF1")
    for row in report["chapters"]:
        levels = ",".join(row["levels"])
        print(
            f"  {row['chapter']}: primjeri={row['examples']}, "
            f"zadatci={row['tasks']} [{levels}]"
        )
    print(
        "Ukupno: "
        f"poglavlja={report['chapter_count']}, primjeri={report['example_count']}, "
        f"zadatci={report['task_count']}, ID-jevi={report['stable_id_count']}, "
        f"jednadžbe={report['equation_count']}, dodaci={report['appendix_count']}, "
        f"sati={report['workload_hours']}, SVG={report['referenced_svg_count']}, "
        f"citati={report['citation_count']}, "
        f"JupyterLite={report['jupyterlite_count']}, "
        f"render-obrasci={report.get('render_pattern_count', 0)}, "
        f"javni-resursi={report.get('public_resource_count', 0)}"
    )
    if issues:
        print("\nPublication audit FAIL:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("\nPublication audit PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
