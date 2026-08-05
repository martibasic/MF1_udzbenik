"""Audit statičkog Quarto HTML izlaza nakon potpune izgradnje."""

from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


CANONICAL_HTML = [
    "index.html",
    "chapters/u00_kako_koristiti_udzbenik.html",
    "chapters/u01_osnove_fluida_i_pascalov_zakon.html",
    "chapters/u02_viskoznost_povrsinska_napetost_i_kapilarnost.html",
    "chapters/u03_hidrostaticka_raspodjela_tlaka_i_manometrija.html",
    "chapters/u04_relativno_mirovanje_fluida.html",
    "chapters/u05_hidrostatske_sile_na_plohe.html",
    "chapters/u06_uzgon_plivanje_i_stabilnost.html",
    "chapters/u07_kinematika_kontrolni_volumen_i_kontinuitet.html",
    "chapters/u08_energijska_jednadzba_i_bernoulli.html",
    "chapters/u09_kompresibilni_idealni_tok.html",
    "chapters/u10_kolicina_i_moment_kolicine_gibanja.html",
    "chapters/u11_dimenzijska_analiza_i_slicnost.html",
    "chapters/u12_diferencijalni_opis_realnog_toka.html",
    "chapters/u13_gubici_cjevovodi_crpke_i_mreze.html",
    "chapters/u14_turbostrojevi_i_propulzija.html",
    "chapters/u15_otvoreni_tokovi.html",
    "chapters/d01_sazetak_formula_i_oznaka.html",
    "chapters/d02_pojmovnik.html",
    "chapters/d03_tipicne_pogreske_po_poglavljima.html",
    "chapters/d04_numericka_mehanika_fluida.html",
    "chapters/d05_literatura.html",
    "chapters/d06_kljuc_kontrolnih_rezultata.html",
    "chapters/za_ispis.html",
]
COMPATIBILITY_REDIRECTS = {
    "za_ispis.html": "chapters/za_ispis.html",
    "chapters/u05_hidrostatske_sile_na_ravne_plohe.html": (
        "chapters/u05_hidrostatske_sile_na_plohe.html"
    ),
    "chapters/u06_zakrivljene_plohe_i_rastav_sila.html": (
        "chapters/u05_hidrostatske_sile_na_plohe.html"
    ),
    "chapters/u07_uzgon_plivanje_i_stabilnost.html": (
        "chapters/u06_uzgon_plivanje_i_stabilnost.html"
    ),
    "chapters/u08_kontrolni_volumen_i_kontinuitet.html": (
        "chapters/u07_kinematika_kontrolni_volumen_i_kontinuitet.html"
    ),
    "chapters/u09_bernoullijeva_jednadzba_idealnog_fluida.html": (
        "chapters/u08_energijska_jednadzba_i_bernoulli.html"
    ),
    "chapters/u10_realni_bernoulli_i_gubici.html": (
        "chapters/u13_gubici_cjevovodi_crpke_i_mreze.html"
    ),
    "chapters/u11_kolicina_gibanja_i_sile_strujanja.html": (
        "chapters/u10_kolicina_i_moment_kolicine_gibanja.html"
    ),
    "chapters/u12_pokretne_lopatice_i_potisak.html": (
        "chapters/u14_turbostrojevi_i_propulzija.html"
    ),
    "chapters/u13_cjevovodi.html": (
        "chapters/u13_gubici_cjevovodi_crpke_i_mreze.html"
    ),
    "chapters/u14_bezdimenzijski_brojevi_dimenzijska_analiza_i_slicnost.html": (
        "chapters/u11_dimenzijska_analiza_i_slicnost.html"
    ),
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.lang = ""
        self.details = 0
        self.collapsible_callouts = 0
        self.keyed_task_callouts = 0
        self.headings: list[int] = []
        self.anchors: set[str] = set()
        self.refresh_urls: list[str] = []
        self.canonical_urls: list[str] = []
        self._visible: list[str] = []
        self._ignored_depth = 0
        self._in_main = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag in {"script", "style", "svg"}:
            self._ignored_depth += 1
        if tag == "html":
            self.lang = data.get("lang", "")
        if tag == "main":
            self._in_main = True
        if data.get("id"):
            self.ids.append(data["id"])
            self.anchors.add(data["id"])
        if tag == "a" and data.get("name"):
            self.anchors.add(data["name"])
        if tag in {"a", "link"} and data.get("href"):
            self.links.append((tag, data["href"]))
        if tag == "link" and "canonical" in data.get("rel", "").lower().split():
            if data.get("href"):
                self.canonical_urls.append(data["href"])
        if tag == "meta" and data.get("http-equiv", "").lower() == "refresh":
            match = re.search(
                r"(?:^|;)\s*url\s*=\s*['\"]?([^'\";]+)",
                data.get("content", ""),
                flags=re.IGNORECASE,
            )
            if match:
                self.refresh_urls.append(match.group(1).strip())
        if tag in {"img", "script", "iframe", "source"} and data.get("src"):
            self.links.append((tag, data["src"]))
        if tag == "img":
            self.images.append(data)
        if tag == "details":
            self.details += 1
        classes = set(data.get("class", "").split())
        if tag == "div" and {"callout-collapse", "collapse"}.issubset(classes):
            self.collapsible_callouts += 1
        if tag == "div" and (
            data.get("data-hint-key") == "true"
            or data.get("data-answer-key") == "true"
        ):
            self.keyed_task_callouts += 1
        if self._in_main and re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag in {"script", "style", "svg"}:
            self._ignored_depth -= 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"} and self._ignored_depth:
            self._ignored_depth -= 1
        if tag == "main":
            self._in_main = False

    def handle_data(self, data: str) -> None:
        if not self._ignored_depth:
            self._visible.append(data)

    @property
    def visible_text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self._visible)).strip()


def _target(root: Path, page: Path, raw_url: str) -> tuple[Path, str] | None:
    split = urlsplit(raw_url)
    if split.scheme or split.netloc:
        return None
    path = unquote(split.path)
    if not path:
        resolved = page.resolve()
    elif path.startswith("/"):
        # URL s početnom kosom crtom pripada korijenu objavljenog sitea, a ne
        # korijenu lokalnog datotečnog sustava.
        resolved = (root / path.lstrip("/")).resolve()
    else:
        resolved = (page.parent / path).resolve()
    if path.endswith("/"):
        resolved /= "index.html"
    return resolved, unquote(split.fragment)


def _parse_page(path: Path, cache: dict[Path, PageParser]) -> PageParser:
    resolved = path.resolve()
    if resolved not in cache:
        parsed = PageParser()
        parsed.feed(resolved.read_text(encoding="utf-8"))
        cache[resolved] = parsed
    return cache[resolved]


def _link_issues(
    root: Path,
    page: Path,
    relative: str,
    raw_url: str,
    cache: dict[Path, PageParser],
) -> list[str]:
    found: list[str] = []
    split = urlsplit(raw_url)
    if split.scheme.lower() == "file":
        return [f"{relative}: nedopuštena file: veza {raw_url!r}"]
    local = _target(root, page, raw_url)
    if local is None:
        return found
    target, fragment = local
    try:
        target.relative_to(root)
    except ValueError:
        return [f"{relative}: lokalna veza izlazi iz _site {raw_url!r}"]
    if target.is_dir():
        target /= "index.html"
    if not target.exists():
        return [f"{relative}: mrtva lokalna veza {raw_url!r}"]
    if fragment and target.suffix.lower() in {".html", ".htm"}:
        try:
            target_page = _parse_page(target, cache)
        except (OSError, UnicodeDecodeError) as exc:
            return [f"{relative}: ne mogu pročitati cilj veze {raw_url!r}: {exc}"]
        if fragment not in target_page.anchors:
            found.append(f"{relative}: nepostojeće sidro u vezi {raw_url!r}")
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="_site")
    args = parser.parse_args()
    root = Path(args.site).resolve()
    issues: list[str] = []
    parsed_pages: dict[Path, PageParser] = {}
    total_images = 0
    total_links = 0
    total_details = 0

    leaked_sources = sorted((root / "source").rglob("*.md"))
    if leaked_sources:
        preview = ", ".join(
            path.relative_to(root).as_posix() for path in leaked_sources[:5]
        )
        suffix = f", još {len(leaked_sources) - 5}" if len(leaked_sources) > 5 else ""
        issues.append(
            "kanonski Markdown ne smije biti kopiran u javni izlaz: "
            f"{preview}{suffix}"
        )

    for relative in CANONICAL_HTML:
        page = root / relative
        if not page.is_file() or page.stat().st_size == 0:
            issues.append(f"nedostaje kanonska stranica {relative}")
            continue
        parsed = _parse_page(page, parsed_pages)
        if parsed.lang.lower() not in {"hr", "hr-hr"}:
            issues.append(f"{relative}: html lang nije hrvatski ({parsed.lang!r})")
        duplicates = sorted(
            item for item, count in Counter(parsed.ids).items() if count > 1
        )
        if duplicates:
            issues.append(f"{relative}: duplicirani HTML ID-jevi {duplicates}")
        for index, image in enumerate(parsed.images, start=1):
            # alt="" je valjan za namjerno dekorativnu sliku; nedostatak samog
            # atributa nije. Smislenost sadržajnih opisa provjerava source audit.
            if "alt" not in image:
                issues.append(f"{relative}: slika #{index} nema atribut alt")
        for _tag, raw_url in parsed.links:
            issues.extend(_link_issues(root, page, relative, raw_url, parsed_pages))
        for previous, current in zip(parsed.headings, parsed.headings[1:]):
            if current > previous + 1:
                issues.append(
                    f"{relative}: preskočena razina naslova h{previous} → h{current}"
                )
                break
        visible = parsed.visible_text
        untranslated_patterns = {
            "AUTHOR": r"\bAUTHOR\b",
            "Figure N": r"\bFigure\s+\d+",
        }
        for label, pattern in untranslated_patterns.items():
            if re.search(pattern, visible):
                issues.append(
                    f"{relative}: ostala nelokalizirana oznaka {label!r}"
                )
        total_images += len(parsed.images)
        total_links += len(parsed.links)
        total_details += parsed.details
        total_details += parsed.collapsible_callouts
        if parsed.keyed_task_callouts > parsed.collapsible_callouts:
            issues.append(
                f"{relative}: naputci/rezultati nisu svi sklopivi "
                f"({parsed.keyed_task_callouts} označenih, "
                f"{parsed.collapsible_callouts} sklopivih blokova)"
            )

    for relative, expected_relative in COMPATIBILITY_REDIRECTS.items():
        page = root / relative
        expected = (root / expected_relative).resolve()
        if not page.is_file() or page.stat().st_size == 0:
            issues.append(f"nedostaje kompatibilno preusmjerenje {relative}")
            continue
        parsed = _parse_page(page, parsed_pages)
        for _tag, raw_url in parsed.links:
            issues.extend(_link_issues(root, page, relative, raw_url, parsed_pages))
        resolved_refreshes: list[Path] = []
        for raw_url in parsed.refresh_urls:
            local = _target(root, page, raw_url)
            if local is None:
                continue
            target, _ = local
            if target.is_dir():
                target /= "index.html"
            resolved_refreshes.append(target.resolve())
        if expected not in resolved_refreshes:
            issues.append(
                f"{relative}: meta-refresh ne cilja {expected_relative!r}"
            )
        resolved_canonicals: list[Path] = []
        for raw_url in parsed.canonical_urls:
            local = _target(root, page, raw_url)
            if local is None:
                continue
            target, _ = local
            if target.is_dir():
                target /= "index.html"
            resolved_canonicals.append(target.resolve())
        if expected not in resolved_canonicals:
            issues.append(
                f"{relative}: canonical link ne cilja {expected_relative!r}"
            )
        if not expected.is_file() or expected.stat().st_size == 0:
            issues.append(
                f"{relative}: cilj preusmjerenja ne postoji ({expected_relative})"
            )

    if issues:
        print("Rendered-site audit FAIL:")
        for issue in dict.fromkeys(issues):
            print(f"  - {issue}")
        return 1
    print(
        "Rendered-site audit PASS: "
        f"stranice={len(CANONICAL_HTML)}, slike={total_images}, "
        f"veze={total_links}, sklopivi_blokovi={total_details}, "
        f"preusmjerenja={len(COMPATIBILITY_REDIRECTS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
