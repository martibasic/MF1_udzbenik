"""Check rendered typography, object numbering, QR modules and bibliography.

These checks inspect the final PDF, complementing the source SVG viewport
audit and human review. They do not certify physical accuracy of diagrams.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
QR_COLOUR = (17 / 255, 24 / 255, 39 / 255)
FIGURE_TOKENS = json.loads((ROOT / "assets/figure-tokens.json").read_text(encoding="utf-8"))
PDF_TOKENS = json.loads((ROOT / "design-system/tokens.json").read_text(encoding="utf-8"))["pdf"]


def typography_issues(document: pymupdf.Document) -> list[str]:
    """Measure rendered titles and equation numbers, not just style declarations.

    The original CRLF regression put a heading number on its own line. A grid
    must now put actual title text on the number's baseline. This also catches
    broken multi-line headings without relying on a particular page count.
    """
    issues = []
    title_keys = ("h1_pt", "h2_pt", "h3_pt", "h4_pt", "label_pt",
                  "example_title_pt", "block_title_pt")
    if any(PDF_TOKENS[key] <= PDF_TOKENS["font_size_pt"] for key in title_keys):
        issues.append("svi strukturni naslovi moraju biti veći od osnovnog teksta")
    sizes = {PDF_TOKENS[key] for key in title_keys}
    margin = PDF_TOKENS["margin_x_mm"] * 72 / 25.4
    equations = []
    exercise_labels = []
    key_labels = []
    chapter = None
    starts = {page: title.split(".", 1)[0]
              for level, title, page in document.get_toc() if level == 1}
    numbered_titles = 0
    first_body = next((page for level, title, page in document.get_toc()
                       if level == 1), 1)
    for number, page in enumerate(document, 1):
        if number in starts:
            chapter = starts[number]
        spans = [s for b in page.get_text("dict")["blocks"]
                 for line in b.get("lines", []) for s in line["spans"]
                 if s["text"].strip()]
        body = [s for s in spans if 55 < s["bbox"][1] and s["bbox"][3] < 790]
        for span in body:
            text = span["text"].strip()
            label = re.match(r"^([PZ]\d+)\.", text)
            if label and span["font"] == "LibertinusSerif-Bold":
                if chapter and chapter.isdigit():
                    exercise_labels.append((chapter, label[1]))
                elif chapter == "F":
                    key_labels.append(label[1])
            if (span["bbox"][0] > 470
                    and re.fullmatch(r"\((?:\d+|[A-F])\.\d+\)", text)):
                equations.append(text[1:-1])
            if (number < first_body or "LibertinusSerif-Bold" != span["font"]
                    or span["size"] < PDF_TOKENS["h4_pt"] - .05
                    or not re.fullmatch(r"(?:\d+|[A-F])(?:\.\d+)*\.?", text)):
                continue
            numbered_titles += 1
            if not any(abs(other["size"] - span["size"]) < .05
                       and abs(other["origin"][1] - span["origin"][1]) < 1
                       and other["bbox"][0] >= span["bbox"][2]
                       and re.search(r"[A-Za-zČĆŽŠĐčćžšđ]", other["text"])
                       for other in body):
                issues.append(f"str. {number}: broj naslova {text} nema naslov u istom retku")
        if number >= first_body and body:
            last = max(body, key=lambda span: span["origin"][1])
            # The standalone appendix divider is intentional, like part pages.
            if (last["text"].strip() != "Dodaci" and "Bold" in last["font"]
                    and any(abs(last["size"] - size) < .05 for size in sizes)):
                issues.append(f"str. {number}: naslov ostaje bez sadržaja: {last['text']}")
            if last["text"].strip() == "Vrati se na zadatak":
                issues.append(f"str. {number}: naslov ključa ostaje samo uz povratnu poveznicu")
        # Check ink-bearing characters: even MuPDF word boxes can include a
        # trailing space or combine an accent with text on another baseline.
        # Allow 3 pt optical overhang; headers and folios live outside the frame.
        chars = [c for b in page.get_text("rawdict")["blocks"]
                 for line in b.get("lines", []) for span in line["spans"]
                 for c in span["chars"] if c["c"].strip()]
        for char in chars:
            x0, y0, x1, y1 = char["bbox"]
            if (55 < y0 and y1 < 790
                    and (x0 < margin - 3 or x1 > page.rect.width - margin + 3)):
                issues.append(f"str. {number}: tekst izlazi iz stupca: {char['c']}")
                break
    index = json.loads((ROOT / "assets/content-index.json").read_text(encoding="utf8"))
    expected = Counter(obj["number"] for obj in index["objects"].values()
                       if obj["kind"] == "Equation")
    actual = Counter(equations)
    if actual != expected:
        issues.append(f"numeracija jednadžbi: nedostaje {dict(expected - actual)}; "
                      f"višak {dict(actual - expected)}")
    expected_labels = Counter(
        (index["documents"][obj["document"]]["number"], obj["label"])
        for obj in index["objects"].values() if obj["kind"] in ("Example", "Problem"))
    actual_labels = Counter(exercise_labels)
    if actual_labels != expected_labels:
        issues.append(f"P/Z naslovi po poglavljima: nedostaje {dict(expected_labels - actual_labels)}; "
                      f"višak {dict(actual_labels - expected_labels)}")
    expected_key = Counter(obj["label"] for obj in index["objects"].values()
                           if obj["kind"] == "Problem")
    if Counter(key_labels) != expected_key:
        issues.append("ključ rezultata nema sve Z oznake prema indeksu")
    if numbered_titles < 150:
        issues.append(f"provjereno samo {numbered_titles} numeriranih naslova")
    return issues


def equation_issues(document: pymupdf.Document) -> list[str]:
    issues = []
    for page_number, page in enumerate(document, 1):
        chars = [c for b in page.get_text("rawdict")["blocks"] if b["type"] == 0
                 for line in b["lines"] for s in line["spans"] for c in s["chars"]]
        string = "".join(c["c"] for c in chars)
        # Equation numbers occupy the right margin; inline references do not.
        right_chars = [(i, c, pymupdf.Rect(c["bbox"])) for i, c in enumerate(chars)
                       if c["bbox"][2] > 466 and c["c"].strip()]
        for match in re.finditer(r"\((?:\d+|[A-F])\.\d+\)", string):
            selected = chars[match.start():match.end()]
            rect = pymupdf.Rect(selected[0]["bbox"])
            for char in selected[1:]:
                rect |= pymupdf.Rect(char["bbox"])
            if rect.x0 < 470 or rect.x1 < 500:
                continue
            neighbours = []
            for index, char, box in right_chars:
                if match.start() <= index < match.end():
                    continue
                if (min(box.y1, rect.y1) - max(box.y0, rect.y0) > 3
                        and box.x1 > rect.x0 - 4 and box.x0 < rect.x1 + 4):
                    neighbours.append(char["c"])
            if neighbours:
                issues.append(f"str. {page_number}: razmak uz {match[0]} manji od 4 pt "
                              f"({''.join(neighbours)!r})")
    return issues


def qr_issues(document: pymupdf.Document) -> tuple[int, list[str]]:
    issues = []
    checked = 0
    links = [(index, link["uri"]) for index, page in enumerate(document)
             for link in page.get_links() if "uri" in link]
    for path in sorted((ROOT / "assets/qr").glob("*.svg")):
        root = ET.fromstring(path.read_text(encoding="utf-8"))
        namespace = {"s": "http://www.w3.org/2000/svg"}
        description = root.find("s:desc", namespace)
        if description is None or not description.text.startswith("Poveznica: "):
            issues.append(f"{path.name}: nedostaje izvorna QR poveznica")
            continue
        url = description.text.removeprefix("Poveznica: ")
        size = int(root.attrib["viewBox"].split()[2])
        dark_path = root.find("s:path", namespace)
        cells = {(int(x), int(y)) for x, y in re.findall(
            r"M(\d+) (\d+)h1v1H\d+z", dark_path.attrib["d"])}
        if not cells:
            issues.append(f"{path.name}: nepoznat oblik QR SVG-a")
            continue
        pages = sorted({index for index, target in links if target == url})
        if len(pages) != 1:
            issues.append(f"{path.name}: očekuje se jedna stranica s JupyterLite poveznicom; "
                          f"nađeno {len(pages)}")
            continue
        page = document[pages[0]]
        notebook = url.split("?path=", 1)[1]
        if not any("colab.research.google.com/" in target and target.endswith(notebook)
                   for index, target in links if index == pages[0]):
            issues.append(f"str. {pages[0] + 1}: nedostaje Colab poveznica za {notebook}")
        candidates = []
        for drawing in page.get_drawings():
            colour, rect = drawing.get("fill"), drawing["rect"]
            if (colour and len(colour) == 3
                    and max(abs(a - b) for a, b in zip(colour, QR_COLOUR)) < .002
                    and 45 < rect.width < 85 and abs(rect.width - rect.height) < .2
                    and len(drawing["items"]) > 100):
                candidates.append(rect)
        found = False
        errors = []
        for rect in candidates:
            pitch = rect.width / (size - 8)
            full = pymupdf.Rect(rect.x0 - 4 * pitch, rect.y0 - 4 * pitch,
                               rect.x1 + 4 * pitch, rect.y1 + 4 * pitch)
            if not page.rect.contains(full):
                errors.append("QR prelazi rub stranice")
                continue
            if abs(full.width - 28 * 72 / 25.4) > .5:
                errors.append("QR nije veličine 28 mm")
                continue
            scale = 4
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=full,
                                    colorspace=pymupdf.csGRAY, alpha=False)
            pixels = pixmap.samples
            mismatches = 0
            for y in range(size):
                for x in range(size):
                    px = int((full.x0 + (x + .5) * pitch) * scale) - pixmap.x
                    py = int((full.y0 + (y + .5) * pitch) * scale) - pixmap.y
                    actual = pixels[py * pixmap.stride + px] < 128
                    mismatches += actual != ((x, y) in cells)
            if mismatches == 0:
                found = True
                break
            errors.append(f"{mismatches} pogrešnih modula")
        if found:
            checked += 1
        else:
            issues.append(f"str. {pages[0] + 1}, {path.name}: nedostaje ispravan vidljivi QR "
                          f"({'; '.join(errors) or 'nema QR geometrije'})")
    if checked != 17:
        issues.append(f"provjereno {checked}/17 vidljivih QR kodova")
    return checked, issues


def bibliography_issues(document: pymupdf.Document) -> list[str]:
    chapters = {title: page for level, title, page in document.get_toc() if level == 1}
    starts = [page for title, page in chapters.items() if title.startswith("E.")]
    ends = [page for title, page in chapters.items() if title.startswith("F.")]
    if len(starts) != 1 or len(ends) != 1:
        return ["nedostaju PDF odredišta dodataka E i F"]
    text = "\n".join(document[i].get_text() for i in range(starts[0] - 1, ends[0] - 1))
    heading = text.find("Bibliografski zapisi")
    numbers = re.findall(r"(?m)^\[(\d+)\]", text[heading:]) if heading >= 0 else []
    if numbers != [str(i) for i in range(1, 19)]:
        return [f"E.7 mora sadržavati svih 18 bibliografskih zapisa; nađene oznake {numbers}"]
    after_key = "\n".join(document[i].get_text() for i in range(ends[0] - 1, len(document)))
    if re.search(r"(?m)^\[1\]", after_key):
        return ["bibliografija se ponavlja iza dodatka F"]
    return []


def orphan_and_overflow_issues(document: pymupdf.Document) -> list[str]:
    issues = []
    for number, page in enumerate(document, 1):
        spans = [s for b in page.get_text("dict")["blocks"] if b["type"] == 0
                 for line in b["lines"] for s in line["spans"]]
        drawings = page.get_drawings()
        for span in spans:
            # Native caption size comes from the same print token as Typst.
            caption_size = FIGURE_TOKENS["figure-caption-size"]
            if (span["color"] == 0x536577 and abs(span["size"] - caption_size) < .1
                    and re.match(r"Slika\s+\d+\.\d+:", span["text"])
                    and (span["bbox"][1] < 100 or (
                        span["bbox"][1] < 200 and not any(
                            d["rect"].width > 2 and d["rect"].height > 2
                            and d["rect"].y1 > 65 and d["rect"].y0 < span["bbox"][1]
                            for d in drawings)))):
                # Trailing legend text alone must not count as the diagram.
                issues.append(f"str. {number}: opis slike bez panela iznad njega: {span['text']}")
            if span["text"].strip() and span["bbox"][3] > page.rect.height + 1:
                issues.append(f"str. {number}: tekst prelazi donji rub stranice")
                break
        notebook_links = [link["uri"] for link in page.get_links()
                          if "uri" in link and "/jlite/" in link["uri"]]
        for url in notebook_links:
            notebook = url.split("?path=", 1)[-1]
            text = page.get_text()
            if not any(label in text for label in (notebook, "Interaktivni prikaz", "Numerički pokus")):
                issues.append(f"str. {number}: QR/poveznica odvojeni od opisa bilježnice {notebook}")
    return issues


def figure_font_issues(document: pymupdf.Document) -> list[str]:
    """SVG labels remain PDF text: check their actual physical size after layout."""
    issues = []
    count = 0
    for number, page in enumerate(document, 1):
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    # Body/math/monospace fonts are independent of diagram labels.
                    if span["font"].startswith(("Libertinus", "NewCM", "DejaVuSansMono")):
                        continue
                    if not span["text"].strip():
                        continue
                    count += 1
                    if span["size"] < FIGURE_TOKENS["figure-small-label-size"] - .03:
                        issues.append(f"str. {number}: oznaka skice {span['size']:.2f} pt: {span['text']}")
    if count < 3000:
        issues.append(f"nađeno samo {count} tekstnih raspona skica; provjeriti ugrađivanje SVG-a")
    return issues


def audit(path: Path) -> tuple[int, list[str]]:
    with pymupdf.open(path) as document:
        checked, issues = qr_issues(document)
        issues.extend(equation_issues(document))
        issues.extend(bibliography_issues(document))
        issues.extend(orphan_and_overflow_issues(document))
        issues.extend(figure_font_issues(document))
        issues.extend(typography_issues(document))
    return checked, issues


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", nargs="?", type=Path, default=ROOT / "_book/mehanika-fluida-1.pdf")
    args = parser.parse_args()
    checked, issues = audit(args.pdf)
    if issues:
        print("PDF layout FAIL:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print(f"PDF layout PASS: {checked} raster-checked QR codes with links, equation clearance, "
          "18 bibliography entries in E.7, captions and QR descriptions kept with content; "
          "figure labels >= 9 pt; heading baselines, column bounds, equation numbers and P/Z labels match.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
