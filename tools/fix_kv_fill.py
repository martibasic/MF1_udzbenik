#!/usr/bin/env python3
"""
fix_kv_fill.py
Uklanja fill s kontrolnih ploha i kontrolnih volumena:
  - svi zatvoreni oblici (rect, polygon, ellipse, circle, closed path)
    koji imaju stroke-dasharray dobivaju fill="none"
  - fill-opacity se uklanja ako postoji

Razlog: dashed zatvoreni oblici = KV/CS indikatori. Fill prekriva
geometriju ispod. Dashed rub ostaje vidljiv i jasno označava granicu.
"""

import xml.etree.ElementTree as ET
import glob
import re
import subprocess
import sys

ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('cc', 'http://creativecommons.org/ns#')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd')

SVG_NS = '{http://www.w3.org/2000/svg}'
AREA_TAGS = {'rect', 'polygon', 'ellipse', 'circle'}


class CommentTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def is_closed_path(d):
    return bool(re.search(r'[Zz]', d))


def fix_kv_fills_in_root(root):
    changed = 0
    for elem in root.iter():
        if callable(elem.tag):
            continue
        local = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag

        # Preskoci line i polyline (nisu zatvoreni oblici)
        if local in ('line', 'polyline', 'text', 'tspan', 'defs',
                     'marker', 'linearGradient', 'radialGradient',
                     'pattern', 'stop', 'title', 'desc', 'metadata'):
            continue

        # Provjeri stroke-dasharray
        dasharray = elem.get('stroke-dasharray', '')
        if not dasharray:
            continue

        # Provjeri je li zatvoreni oblik
        is_area = local in AREA_TAGS
        if not is_area and local == 'path':
            d = elem.get('d', '')
            if d and is_closed_path(d):
                is_area = True

        if not is_area:
            continue

        # Postavi fill na none
        current_fill = elem.get('fill', '')
        fill_opacity = elem.get('fill-opacity', '')

        if current_fill == 'none' and not fill_opacity:
            continue  # već ispravno

        old_fill = current_fill or '(nema)'
        elem.set('fill', 'none')
        if fill_opacity:
            del elem.attrib['fill-opacity']
        changed += 1
        print(f'    fill {old_fill!r} → none  ({local})')

    return changed


def process_file(path):
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(path, parser)
    root = tree.getroot()

    n = fix_kv_fills_in_root(root)
    if n > 0:
        tree.write(path, encoding='unicode', xml_declaration=False)
    return n


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Pregledam {len(files)} SVG datoteka...\n')

    total_files = 0
    total_changed = 0

    for path in files:
        try:
            n = process_file(path)
            if n > 0:
                print(f'  ✓ {path.split(chr(92))[-1]}  — {n} oblika')
                total_files += 1
                total_changed += n
        except Exception as e:
            print(f'  ✗ GREŠKA {path}: {e}')

    print(f'\nGotovo: {total_files} datoteka, {total_changed} oblika popravljeno.')

    if total_files > 0:
        print('\nIspravljam namespace prefikse...')
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', 'tools/fix_svg_ns.py'],
            capture_output=True, text=True
        )
        print(result.stdout.strip())


if __name__ == '__main__':
    main()
