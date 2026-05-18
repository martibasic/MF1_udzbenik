"""Lagani preview server: serve project root and auto-generate index of svih SVG-eva po poglavlju.

Pokretanje:
    py tools/preview_server.py
Otvori u browseru: http://localhost:8765/preview.html
"""
from __future__ import annotations

import http.server
import re
import socketserver
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS = REPO_ROOT / "assets" / "print"
SOURCE = REPO_ROOT / "source"
PREVIEW = REPO_ROOT / "preview.html"
PORT = 8765


def regen_preview() -> None:
    """Generira preview.html koja prikazuje sve SVG-ove po poglavlju."""
    chapters = []
    # u00, u01..u13, d01..d03
    for prefix, title_root in [
        ("u00", "U00 — Kako koristiti udžbenik"),
        ("u01", "U01 — Osnove fluida i Pascalov zakon"),
        ("u02", "U02 — Viskoznost, površinska napetost i kapilarnost"),
        ("u03", "U03 — Hidrostatička raspodjela tlaka i manometrija"),
        ("u04", "U04 — Relativno mirovanje fluida"),
        ("u05", "U05 — Hidrostatske sile na ravne plohe"),
        ("u06", "U06 — Zakrivljene plohe i rastav sila"),
        ("u07", "U07 — Uzgon, plivanje i stabilnost"),
        ("u08", "U08 — Kontrolni volumen i kontinuitet"),
        ("u09", "U09 — Bernoullijeva jednadžba idealnog fluida"),
        ("u10", "U10 — Realni Bernoulli i gubici"),
        ("u11", "U11 — Količina gibanja i sile strujanja"),
        ("u12", "U12 — Pokretne lopatice i potisak"),
        ("u13", "U13 — Cjevovodi"),
    ]:
        svgs = sorted(ASSETS.glob(f"{prefix}_*.svg"))
        source_md = next((p for p in SOURCE.glob(f"{prefix}_*.md")), None)
        chapters.append({
            "prefix": prefix,
            "title": title_root,
            "svgs": svgs,
            "source": source_md,
        })

    parts = [
        "<!doctype html>",
        '<html lang="hr">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>MF1 udzbenik — preview SVG-eva</title>",
        "<style>",
        "body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 0; background: #f5f7fa; color: #1a2530; }",
        ".container { max-width: 1400px; margin: 0 auto; padding: 24px; }",
        "header { background: #1a2530; color: #fff; padding: 16px 24px; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }",
        "header h1 { margin: 0; font-size: 18px; font-weight: 600; }",
        "header nav { margin-top: 8px; font-size: 13px; }",
        "header nav a { color: #aed6f1; text-decoration: none; margin-right: 14px; }",
        "header nav a:hover { color: #fff; }",
        "section { margin: 32px 0; background: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }",
        "section h2 { margin: 0 0 4px 0; font-size: 18px; color: #1565c0; }",
        "section .meta { font-size: 12px; color: #5a6a78; margin-bottom: 16px; }",
        ".svg-grid { display: grid; grid-template-columns: 1fr; gap: 20px; }",
        ".svg-card { border: 1px solid #dde3ea; border-radius: 6px; padding: 12px; background: #fafbfc; }",
        ".svg-card .filename { font-family: monospace; font-size: 11px; color: #5a6a78; margin-bottom: 8px; }",
        ".svg-card img { display: block; width: 100%; max-width: 100%; height: auto; border: 1px solid #e8eaed; background: #fff; }",
        ".empty { color: #95a5a6; font-style: italic; padding: 12px; }",
        "</style>",
        "</head>",
        "<body>",
        '<header><h1>MF1 udzbenik — SVG preview</h1>',
        "<nav>",
    ]
    for ch in chapters:
        if ch["svgs"]:
            parts.append(f'<a href="#{ch["prefix"]}">{ch["prefix"].upper()}</a>')
    parts.append("</nav></header>")
    parts.append('<div class="container">')

    for ch in chapters:
        if not ch["svgs"]:
            continue
        parts.append(f'<section id="{ch["prefix"]}">')
        parts.append(f'<h2>{ch["title"]}</h2>')
        parts.append(f'<div class="meta">{len(ch["svgs"])} SVG · izvor: <code>source/{ch["source"].name if ch["source"] else "(nedostaje)"}</code></div>')
        parts.append('<div class="svg-grid">')
        for svg in ch["svgs"]:
            rel = svg.relative_to(REPO_ROOT).as_posix()
            parts.append('<div class="svg-card">')
            parts.append(f'<div class="filename">{svg.name}</div>')
            parts.append(f'<img src="{rel}" alt="{svg.name}">')
            parts.append("</div>")
        parts.append("</div></section>")

    parts.append("</div></body></html>")
    PREVIEW.write_text("\n".join(parts), encoding="utf-8")
    print(f"  preview.html regenerated ({sum(len(c['svgs']) for c in chapters)} SVG entries)")


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Regenerate preview on every request to preview.html
        if self.path in ("/preview.html", "/preview.html?"):
            regen_preview()
        super().do_GET()

    def log_message(self, fmt, *args):
        # Mute default verbose logging
        pass


def main() -> int:
    regen_preview()
    import os
    os.chdir(REPO_ROOT)
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving {REPO_ROOT} at http://localhost:{PORT}/preview.html")
        print("Ctrl+C za stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
