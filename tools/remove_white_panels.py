#!/usr/bin/env python3
"""
remove_white_panels.py

Uklanja SAMO vanjski (parent) dekorativni okvir slike — onaj koji obuhvaća
gotovo cijeli viewBox i samo uokviruje crtež, bez semantičkog doprinosa.

NE dira ugniježđene panele (formula box s jednadžbama, result badge,
step-boxove, callout-e) — oni nose sadržaj i ostaju.

Kriteriji za UKLANJANJE (svi moraju biti ispunjeni):
  1. rx >= 6                       (zaobljeni rubovi)
  2. fill je svijetli              (min RGB kanal > 224 — bijeli i blagi tonovi)
  3. width  >= 0.88 * viewBox_W    (pokriva gotovo cijelu širinu)
  4. height >= 0.82 * viewBox_H    (pokriva gotovo cijelu visinu)

Tako se hvata isključivo vanjski okvir (npr. 952×492 u 980×520 viewBoxu),
a unutarnji paneli (npr. 280×300 formula box) ostaju netaknuti.

Datoteke s dvostupčanim rasporedom (dva pol-široka panela, bez jedinstvenog
vanjskog okvira) ostaju netaknute — ondje nema "parent" okvira za brisanje.
"""

from __future__ import annotations

import glob
import re
import xml.etree.ElementTree as ET

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('cc', 'http://creativecommons.org/ns#')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd')

SVG_NS = '{http://www.w3.org/2000/svg}'

HEX6_RE = re.compile(r'^#([0-9a-fA-F]{6})$')

# Prag "svijetli": najtamniji RGB kanal mora biti iznad ovog broja.
# #f0f7ff -> min 240, #fbfdff -> min 251, #f4f9fd -> min 244, #ffffff -> 255.
LIGHT_MIN_CHANNEL = 224

# Udio viewBoxa koji parent okvir mora pokriti
MIN_WIDTH_FRAC = 0.88
MIN_HEIGHT_FRAC = 0.82


def is_light_fill(fill: str) -> bool:
    m = HEX6_RE.match(fill.strip())
    if not m:
        return False
    h = m.group(1)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return min(r, g, b) > LIGHT_MIN_CHANNEL


def get_float(elem: ET.Element, attr: str, default: float = 0.0) -> float:
    try:
        return float(elem.get(attr, default))
    except (ValueError, TypeError):
        return default


def is_parent_frame(elem: ET.Element, vb_w: float, vb_h: float) -> bool:
    local = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
    if local != 'rect':
        return False
    if get_float(elem, 'rx', 0.0) < 6.0:
        return False
    if not is_light_fill(elem.get('fill', 'none')):
        return False
    w = get_float(elem, 'width', 0.0)
    h = get_float(elem, 'height', 0.0)
    return w >= MIN_WIDTH_FRAC * vb_w and h >= MIN_HEIGHT_FRAC * vb_h


def process_file(path: str) -> tuple[int, list[str]]:
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    try:
        tree = ET.parse(path, parser)
    except ET.ParseError as e:
        return 0, [f'XML parse error: {e}']

    root = tree.getroot()
    vb = root.get('viewBox', '')
    try:
        parts = [float(v) for v in vb.split()]
        vb_w, vb_h = parts[2], parts[3]
    except Exception:
        return 0, ['nema valjanog viewBoxa']

    removed = []
    # Tražimo samo među direktnom djecom roota (parent okvir je uvijek tu).
    for elem in list(root):
        if callable(elem.tag):
            continue
        if is_parent_frame(elem, vb_w, vb_h):
            fill = elem.get('fill', '')
            w = elem.get('width', '?')
            h = elem.get('height', '?')
            removed.append(f'parent okvir fill={fill} {w}×{h} (viewBox {vb_w:.0f}×{vb_h:.0f})')
            root.remove(elem)

    if removed:
        tree.write(path, encoding='unicode', xml_declaration=False)

    return len(removed), removed


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Skeniram {len(files)} SVG datoteka za vanjski (parent) okvir...\n')

    removed_files = 0
    untouched = []
    total_removed = 0

    for path in files:
        fname = path.replace('\\', '/').split('/')[-1]
        try:
            n, log = process_file(path)
            if n > 0:
                print(f'  {fname}: {n} okvir(a) uklonjen(o)')
                for msg in log:
                    print(f'    – {msg}')
                removed_files += 1
                total_removed += n
            else:
                untouched.append(fname)
        except Exception as e:
            print(f'  GREŠKA {fname}: {e}')

    print(f'\nGotovo: {total_removed} parent okvira uklonjeno iz {removed_files} datoteka.')

    if untouched:
        print(f'\nBez promjene ({len(untouched)} datoteka — nemaju jedinstveni vanjski okvir '
              f'ili je raspored dvostupčan):')
        for fname in untouched:
            print(f'    · {fname}')


if __name__ == '__main__':
    main()
