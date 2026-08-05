"""Provjeri stvarni nativni PDF udžbenika nakon Quarto/Typst rendera.

Audit namjerno otvara konačni PDF, a ne međuizvor. Provjerava format svih
stranica, opseg knjige, metapodatke, tekstualnu ekstrakciju sadržaja i svih
glavnih poglavlja te u memoriji rasterizira tri udaljene stranice knjige.
Rasteri se ne zapisuju na disk.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import unicodedata

try:
    import pymupdf
except ImportError as exc:  # pragma: no cover - poruka služi neispravnom okruženju
    raise SystemExit(
        "Nedostaje PyMuPDF; instalirajte pinane ovisnosti iz requirements.txt."
    ) from exc


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF = REPO_ROOT / "_book" / "mehanika-fluida-1.pdf"

EXPECTED_TITLE = "Mehanika fluida 1"
EXPECTED_AUTHOR = "Martina Bašić"
MIN_PAGES = 240
MAX_PAGES = 380
MIN_FILE_SIZE = 1_000_000
MIN_TEXT_CHARACTERS = 250_000

# ISO 216 A4 u PDF točkama (72 pt/in). Tolerancija pokriva zaokruživanje
# MediaBoxa različitih PDF proizvođača, ali ne prihvaća Letter ili A5.
A4_WIDTH_PT = 595.276
A4_HEIGHT_PT = 841.890
PAGE_TOLERANCE_PT = 1.0

CHAPTER_TITLES = (
    "1. Osnove fluida i Pascalov zakon",
    "2. Viskoznost, površinska napetost i kapilarnost",
    "3. Hidrostatička raspodjela tlaka i manometrija",
    "4. Relativno mirovanje fluida",
    "5. Hidrostatske sile na ravne i zakrivljene plohe",
    "6. Uzgon, plivanje i početni stabilitet",
    "7. Kinematika, kontrolni volumen i kontinuitet",
    "8. Energijska jednadžba i Bernoulli",
    "9. Kompresibilni idealni tok",
    "10. Količina i moment količine gibanja",
    "11. Dimenzijska analiza i sličnost",
    "12. Diferencijalni opis realnog toka",
    "13. Gubitci, cjevovodi, crpke i mreže",
    "14. Turbostrojevi i propulzija",
    "15. Otvoreni tokovi",
)
TOC_MARKERS = (
    "Sadržaj",
    "Osnove fluida i Pascalov zakon",
    "Energijska jednadžba i Bernoulli",
    "Otvoreni tokovi",
    "Dodaci",
)
RASTER_CHAPTERS = (
    CHAPTER_TITLES[0],
    CHAPTER_TITLES[7],
    CHAPTER_TITLES[-1],
)


def _normalise(text: str) -> str:
    """Ujednači Unicode i razmake bez gubitka hrvatskih znakova."""

    return re.sub(
        r"\s+",
        " ",
        unicodedata.normalize("NFC", text).replace("\u00a0", " "),
    ).strip().casefold()


def _metadata_issue(metadata: dict[str, str | None], key: str, expected: str) -> str | None:
    actual = (metadata.get(key) or "").strip()
    if _normalise(actual) != _normalise(expected):
        return f"metapodatak {key} mora biti {expected!r}; nađeno {actual!r}"
    return None


def _a4_issues(document: pymupdf.Document) -> list[str]:
    invalid: list[str] = []
    for index, page in enumerate(document, start=1):
        media = page.mediabox
        width = float(media.width)
        height = float(media.height)
        if (
            abs(width - A4_WIDTH_PT) > PAGE_TOLERANCE_PT
            or abs(height - A4_HEIGHT_PT) > PAGE_TOLERANCE_PT
        ):
            invalid.append(f"str. {index}: {width:.2f} × {height:.2f} pt")
    if not invalid:
        return []
    preview = "; ".join(invalid[:8])
    suffix = f"; još {len(invalid) - 8}" if len(invalid) > 8 else ""
    return [f"MediaBox nije portretni A4 na {len(invalid)} stranica ({preview}{suffix})"]


def _chapter_destinations(document: pymupdf.Document) -> tuple[dict[str, int], list[str]]:
    destinations: dict[str, int] = {}
    for level, title, page_number, *_rest in document.get_toc(simple=True):
        if level == 1:
            destinations[_normalise(title)] = int(page_number)

    issues: list[str] = []
    selected: dict[str, int] = {}
    for title in RASTER_CHAPTERS:
        page_number = destinations.get(_normalise(title))
        if page_number is None:
            issues.append(f"PDF kazalo nema odredište za raster-provjeru {title!r}")
        elif not 1 <= page_number <= document.page_count:
            issues.append(
                f"nevaljano odredište kazala za {title!r}: stranica {page_number}"
            )
        else:
            selected[title] = page_number
    return selected, issues


def _raster_issues(
    document: pymupdf.Document, destinations: dict[str, int]
) -> tuple[list[dict[str, object]], list[str]]:
    rows: list[dict[str, object]] = []
    issues: list[str] = []
    for title in RASTER_CHAPTERS:
        page_number = destinations.get(title)
        if page_number is None:
            continue
        page = document.load_page(page_number - 1)
        pixmap = page.get_pixmap(
            matrix=pymupdf.Matrix(1.0, 1.0),
            colorspace=pymupdf.csGRAY,
            alpha=False,
            annots=True,
        )
        samples = pixmap.samples
        ink_pixels = sum(value < 245 for value in samples)
        ink_ratio = ink_pixels / len(samples) if samples else 0.0
        text_characters = len(re.sub(r"\s+", "", page.get_text("text")))
        rows.append(
            {
                "page": page_number,
                "width": pixmap.width,
                "height": pixmap.height,
                "ink_ratio": ink_ratio,
                "text_characters": text_characters,
            }
        )
        if pixmap.width < 500 or pixmap.height < 750:
            issues.append(
                f"raster str. {page_number} ima neočekivanu veličinu "
                f"{pixmap.width} × {pixmap.height} px"
            )
        if ink_ratio < 0.005 or text_characters < 100:
            issues.append(
                f"raster str. {page_number} izgleda prazan: "
                f"udio nebijelih piksela={ink_ratio:.3%}, znakovi={text_characters}"
            )
    if len(rows) != len(RASTER_CHAPTERS):
        issues.append(
            f"rasterizirano je {len(rows)} od obvezne {len(RASTER_CHAPTERS)} stranice"
        )
    return rows, issues


def audit(pdf_path: Path) -> tuple[dict[str, object], list[str]]:
    issues: list[str] = []
    report: dict[str, object] = {
        "path": pdf_path,
        "pymupdf_version": pymupdf.__version__,
    }
    if not pdf_path.is_file():
        return report, [f"PDF ne postoji: {pdf_path}"]
    file_size = pdf_path.stat().st_size
    report["file_size"] = file_size
    if file_size < MIN_FILE_SIZE:
        issues.append(
            f"PDF je neuobičajeno malen ({file_size} B; minimum {MIN_FILE_SIZE} B)"
        )

    try:
        document = pymupdf.open(pdf_path)
    except Exception as exc:  # PyMuPDF izlaže više tipova za oštećene PDF-ove
        return report, [f"PDF se ne može otvoriti: {exc}"]

    try:
        if document.needs_pass:
            issues.append("PDF je zaštićen lozinkom")
        page_count = document.page_count
        report["page_count"] = page_count
        if not MIN_PAGES <= page_count <= MAX_PAGES:
            issues.append(
                f"broj stranica {page_count} nije u ugovorenom rasponu "
                f"{MIN_PAGES}–{MAX_PAGES}"
            )

        metadata = document.metadata or {}
        report["title"] = metadata.get("title", "")
        report["author"] = metadata.get("author", "")
        for key, expected in (("title", EXPECTED_TITLE), ("author", EXPECTED_AUTHOR)):
            issue = _metadata_issue(metadata, key, expected)
            if issue:
                issues.append(issue)

        issues.extend(_a4_issues(document))

        page_texts = [page.get_text("text") for page in document]
        full_text = _normalise("\n".join(page_texts))
        toc_text = _normalise("\n".join(page_texts[: min(8, page_count)]))
        text_character_count = len(re.sub(r"\s+", "", full_text))
        report["text_character_count"] = text_character_count
        if text_character_count < MIN_TEXT_CHARACTERS:
            issues.append(
                "tekstualna ekstrakcija je neuobičajeno kratka: "
                f"{text_character_count} znakova (minimum {MIN_TEXT_CHARACTERS})"
            )
        for marker in TOC_MARKERS:
            if _normalise(marker) not in toc_text:
                issues.append(f"tekstualno kazalo ne sadrži {marker!r}")
        for title in CHAPTER_TITLES:
            if _normalise(title) not in full_text:
                issues.append(f"tekstualna ekstrakcija ne sadrži poglavlje {title!r}")

        destinations, destination_issues = _chapter_destinations(document)
        issues.extend(destination_issues)
        raster_rows, raster_issues = _raster_issues(document, destinations)
        report["rasters"] = raster_rows
        issues.extend(raster_issues)
    finally:
        document.close()

    return report, issues


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdf",
        nargs="?",
        type=Path,
        default=DEFAULT_PDF,
        help="putanja PDF-a (zadano: _book/mehanika-fluida-1.pdf)",
    )
    args = parser.parse_args()
    pdf_path = args.pdf.resolve()
    report, issues = audit(pdf_path)

    try:
        shown_path = pdf_path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        shown_path = str(pdf_path)
    print(
        "PDF audit: "
        f"datoteka={shown_path}, stranice={report.get('page_count', 0)}, "
        f"veličina={report.get('file_size', 0)} B, "
        f"tekst={report.get('text_character_count', 0)} znakova, "
        f"PyMuPDF={report['pymupdf_version']}"
    )
    for row in report.get("rasters", []):
        print(
            f"  raster str. {row['page']}: {row['width']} × {row['height']} px, "
            f"nebijelo={row['ink_ratio']:.2%}, tekst={row['text_characters']}"
        )
    if issues:
        print("PDF audit FAIL:")
        for issue in dict.fromkeys(issues):
            print(f"  - {issue}")
        return 1
    print("PDF audit PASS: sve stranice su A4, metapodatci i sadržaj su potpuni.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
