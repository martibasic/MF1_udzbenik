#!/usr/bin/env python3
"""
fix_text_overflow.py

Detektira i popravlja preklapanja teksta s granicama panela u SVG skicama.

Što detektira:
  1. Tekst čiji baseline prelazi donji rub panela (y > panel_bottom - 6)
  2. Tekst čiji vrh je iznad gornje granice panela (y - fs < panel_top + 6)
  3. Tekst koji vodoravno prelazi desnu granicu panela za ≥1 px
  4. Tekst koji vodoravno prelazi lijevu granicu panela za ≥1 px

Što popravlja:
  - Vertikalni overflow → pomak y za minimalni potreban iznos
  - Horizontalni overflow → smanjenje font-size za 1–2 px (do min 9)

Što NE dotiče:
  - Tekst u transform grupama (relativne koordinate – presloženo za automatski fix)
  - Tekst izvan svakog panela (kote, oznake na geometriji)
  - Promjene veće od 2 px na font-size (previše agresivno)
"""

from __future__ import annotations

import glob
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('cc', 'http://creativecommons.org/ns#')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd')

SVG_NS = '{http://www.w3.org/2000/svg}'

# Minimalni odmak teksta od ruba panela (px)
MIN_MARGIN = 6

# Minimalna veličina fonta (px) – ispod ovoga ne idemo
MIN_FONT_SIZE = 9.0

# Maksimalni dozvoljeni vertikalni pomak (px) – iznad ovoga ne dirati
MAX_Y_FIX = 20.0

# Prosječna širina znaka po fontu kao udio font-size (Segoe UI procjena)
# Razlikujemo uske/široke znakove
WIDE_CHARS = set('mwWMΩΣ')
NARROW_CHARS = set('ilI.,:;!|f ')


def char_width_factor(ch: str) -> float:
    if ch in WIDE_CHARS:
        return 0.78
    if ch in NARROW_CHARS:
        return 0.38
    if ord(ch) > 127:
        return 0.65  # greek, unicode
    return 0.60


def estimate_text_width(elem: ET.Element, font_size: float) -> float:
    """Procijeni širinu teksta u pixelima (bez renderiranja)."""
    total = 0.0

    def process_text(text: str, fs: float) -> float:
        w = 0.0
        for ch in (text or ''):
            w += char_width_factor(ch) * fs
        return w

    total += process_text(elem.text, font_size)

    for tspan in elem:
        if callable(tspan.tag):
            continue
        ts_fs = font_size
        fs_attr = tspan.get('font-size', '')
        if 'em' in fs_attr:
            try:
                ts_fs = font_size * float(fs_attr.replace('em', ''))
            except ValueError:
                pass
        elif fs_attr:
            try:
                ts_fs = float(fs_attr)
            except ValueError:
                pass
        # Subscript/superscript zauzimaju manje prostora horizontalno
        if tspan.get('baseline-shift') in ('sub', 'super'):
            ts_fs *= 0.85
        total += process_text(tspan.text, ts_fs)
        total += process_text(tspan.tail, font_size)  # tail se renderira punim fontom

    return total


def get_float(elem: ET.Element, attr: str, default: float = 0.0) -> float:
    try:
        return float(elem.get(attr, default))
    except (ValueError, TypeError):
        return default


class PanelRect:
    """Četverokut koji predstavlja panel (formula box, result badge, itd.)"""
    __slots__ = ('x', 'y', 'w', 'h')

    def __init__(self, x: float, y: float, w: float, h: float):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def x2(self) -> float:
        return self.x + self.w

    @property
    def y2(self) -> float:
        return self.y + self.h

    def contains_center(self, tx: float, ty: float) -> bool:
        """Provjeri je li centar teksta (tx, ty) unutar panela.

        Horizontalna tolerancija: 0 px (strogo – sprječava lažne pozitive).
        Vertikalna tolerancija: 8 px (malo više jer text y je baseline).
        """
        y_margin = 8
        return (self.x <= tx <= self.x2 and
                self.y - y_margin <= ty <= self.y2 + y_margin)

    def __repr__(self):
        return f'Panel({self.x},{self.y},{self.w}×{self.h})'


def find_panels(root: ET.Element) -> list[PanelRect]:
    """
    Pronađi sve rect elemente koji izgledaju kao info paneli:
    - Imaju fill i stroke atribute
    - Nisu prehitno mali (w>80, h>30)
    - Ne prolaze kroz cijeli SVG (nisu pozadina)
    - Direktna djeca SVG roota (ne unutar transform grupa)
    """
    panels = []
    viewbox = root.get('viewBox', '0 0 1000 600')
    try:
        vb = [float(v) for v in viewbox.split()]
        svg_w = vb[2]
        svg_h = vb[3]
    except Exception:
        svg_w, svg_h = 1000, 600

    for elem in root:
        if callable(elem.tag):
            continue
        local = elem.tag.split('}')[-1]
        if local != 'rect':
            continue
        fill = elem.get('fill', '')
        stroke = elem.get('stroke', '')
        if not fill or not stroke or fill == 'none':
            continue
        rx = get_float(elem, 'rx', 0)
        w = get_float(elem, 'width', 0)
        h = get_float(elem, 'height', 0)
        x = get_float(elem, 'x', 0)
        y = get_float(elem, 'y', 0)

        # Preskoči prevelike (cijeli SVG background) i premale
        if w < 80 or h < 30:
            continue
        if w > svg_w * 0.98 or h > svg_h * 0.98:
            continue
        # Preskoči header barove (visina <= 40 px) – oni nisu pravi paneli
        if h <= 40:
            continue

        panels.append(PanelRect(x, y, w, h))

    return panels


def find_enclosing_panel(panels: list[PanelRect], tx: float, ty: float,
                          font_size: float) -> Optional[PanelRect]:
    """
    Pronađi najuži panel koji obuhvaća centar teksta.
    Tekst pozicioniran na y (baseline) – centar je otprilike y - font_size/2.
    """
    center_y = ty - font_size * 0.5
    best = None
    best_area = float('inf')
    for p in panels:
        if p.contains_center(tx, center_y):
            area = p.w * p.h
            if area < best_area:
                best = p
                best_area = area
    return best


def fix_svg(path: str) -> tuple[int, list[str]]:
    """
    Popravlja overflow u jednoj SVG datoteci.
    Vraća (broj_popravaka, lista_opisa_promjena).
    """
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    try:
        tree = ET.parse(path, parser)
    except ET.ParseError as e:
        return 0, [f'XML parse error: {e}']

    root = tree.getroot()
    panels = find_panels(root)
    if not panels:
        return 0, []

    changes = []
    n_fixed = 0

    # Pronađi sve top-level text elemente (ne unutar transform grupa)
    for elem in list(root):
        if callable(elem.tag):
            continue
        local = elem.tag.split('}')[-1]
        if local != 'text':
            continue

        try:
            tx = float(elem.get('x', 0))
            ty = float(elem.get('y', 0))
            fs = float(elem.get('font-size', 12))
        except (ValueError, TypeError):
            continue

        anchor = elem.get('text-anchor', 'start')
        panel = find_enclosing_panel(panels, tx, ty, fs)
        if panel is None:
            continue

        # --- VERTIKALNI OVERFLOW ---

        # Tekst je ispod donje granice panela
        text_bottom = ty + fs * 0.2  # dodaj procijenjeni descender
        if text_bottom > panel.y2 - MIN_MARGIN:
            overflow = text_bottom - (panel.y2 - MIN_MARGIN)
            if 0 < overflow <= MAX_Y_FIX:
                new_y = round(ty - overflow, 1)
                elem.set('y', str(new_y))
                changes.append(f'y↑ {ty:.0f}→{new_y:.0f} (donji rub panela {panel.y2:.0f})')
                n_fixed += 1
                ty = new_y

        # Tekst je iznad gornje granice panela (vrh teksta)
        text_top = ty - fs
        if text_top < panel.y + MIN_MARGIN:
            overflow = (panel.y + MIN_MARGIN) - text_top
            if 0 < overflow <= MAX_Y_FIX:
                new_y = round(ty + overflow, 1)
                elem.set('y', str(new_y))
                changes.append(f'y↓ {ty:.0f}→{new_y:.0f} (gornji rub panela {panel.y:.0f})')
                n_fixed += 1
                ty = new_y

        # --- HORIZONTALNI OVERFLOW ---

        text_width = estimate_text_width(elem, fs)

        if anchor == 'middle':
            text_left = tx - text_width / 2
            text_right = tx + text_width / 2
        elif anchor == 'end':
            text_left = tx - text_width
            text_right = tx
        else:  # start
            text_left = tx
            text_right = tx + text_width

        panel_left = panel.x + MIN_MARGIN
        panel_right = panel.x2 - MIN_MARGIN

        overflow_right = text_right - panel_right
        overflow_left = panel_left - text_left

        max_overflow = max(overflow_right, overflow_left)

        # Ako overflow postoji, smanji font-size
        if max_overflow > 0:
            # Koliko trebamo smanjiti font-size da bismo stali?
            # text_width ≈ width_factor × fs × n_chars
            # needed_width = panel_right - panel_left
            available_w = panel_right - panel_left
            if text_width > 0 and available_w > 0:
                # Proporcionalno smanji font-size
                new_fs = fs * (available_w / text_width)
                new_fs = max(MIN_FONT_SIZE, round(new_fs, 1))
                # Ograniči smanjenje na 2 px da bude konzervativno
                new_fs = max(new_fs, fs - 2.0)
                if new_fs < fs:
                    # Formatiranje: izbjegni previše decimala
                    if new_fs == int(new_fs):
                        elem.set('font-size', str(int(new_fs)))
                    else:
                        elem.set('font-size', str(new_fs))
                    changes.append(
                        f'font-size {fs}→{new_fs} '
                        f'(overflow {max_overflow:.1f}px, panel {panel.x:.0f}–{panel.x2:.0f})'
                    )
                    n_fixed += 1

    if n_fixed > 0:
        tree.write(path, encoding='unicode', xml_declaration=False)

    return n_fixed, changes


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Skeniram {len(files)} SVG datoteka za text overflow...\n')

    total_files = 0
    total_fixes = 0

    for path in files:
        fname = path.replace('\\', '/').split('/')[-1]
        try:
            n, log = fix_svg(path)
            if n > 0:
                print(f'  {fname}: {n} popravak(a)')
                for msg in log:
                    print(f'    • {msg}')
                total_files += 1
                total_fixes += n
        except Exception as e:
            print(f'  GREŠKA {fname}: {e}')

    if total_fixes == 0:
        print('Nema pronađenih overflow-a – sve SVG skice su uredne.')
    else:
        print(f'\nGotovo: {total_files} datoteka izmijenjeno, ukupno {total_fixes} popravaka.')

    return total_files


if __name__ == '__main__':
    main()
