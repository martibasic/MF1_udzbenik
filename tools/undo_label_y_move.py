#!/usr/bin/env python3
"""
undo_label_y_move.py  v2

Poništava sve y-pomake koje je uveo fix_label_single_line.py.
Zadrzava jedino "= " prefiks koji je bio dodan (to ostaje).

Kriterij za "pomaknutu" labelu:
  - simbol i vrijednost su na ISTOM y (dy < 2)
  - vrijednost je desno od simbola za mali odmak (0 < dx < 45)
    (to je upravo ono sto je fix_label_single_line postavio kao estimated_sym_width)
  - vrijednost pocinje s "= " (sto je fix_label_single_line dodao)

Za sve takve parove:
  - Pomakni vrijednost DOLJE za 16 px (vrati na originalni raspored)
  - Vrati x na isti kao simbol (dx -> 0)
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

SYM_RE = re.compile(r'^[\wΑ-ωΔδτμνρσ₀-₉ΣΩ]{1,7}$')


class CommentTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def plain_text(elem):
    parts = [elem.text or '']
    for ch in elem:
        if not callable(ch.tag):
            parts.append(ch.text or '')
            parts.append(ch.tail or '')
    return ''.join(parts).strip()


def fix_svg(path):
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(path, parser)
    root = tree.getroot()

    texts = [e for e in root.iter(SVG_NS + 'text') if not callable(e.tag)]
    restored = 0
    skip = set()

    for i, t in enumerate(texts[:-1]):
        if i in skip:
            continue

        sym = plain_text(t)
        if not SYM_RE.match(sym):
            continue

        nxt = texts[i + 1]
        if i + 1 in skip:
            continue

        val = plain_text(nxt)

        # Vrijednost mora pocinjati s "= " (dodano prethodnim skriptom)
        if not val.startswith('= '):
            continue

        try:
            sy = float(t.get('y', 0))
            ny = float(nxt.get('y', 0))
            sx = float(t.get('x', 0))
            nx = float(nxt.get('x', 0))
        except ValueError:
            continue

        dy = abs(ny - sy)
        dx = nx - sx  # koliko je vrijednost desno od simbola

        # Kriterij: pomaknut par (isti y, mali x odmak desno, vrijednost ima "= ")
        if not (dy < 2 and 0 < dx < 45):
            continue

        # Vrati na 2 retka: pomakni vrijednost dolje za 16px, x na isti kao simbol
        nxt.set('y', str(round(sy + 16, 1)))
        nxt.set('x', str(sx))

        restored += 1
        skip.add(i + 1)

    if restored > 0:
        tree.write(path, encoding='unicode', xml_declaration=False)

    return restored


def main():
    files = sorted(glob.glob('assets/print/u*.svg'))
    print(f'Trazim pomaknutih labela u {len(files)} SVG datoteka...\n')

    total = 0
    for path in files:
        try:
            n = fix_svg(path)
            if n > 0:
                fname = path.replace('\\', '/').split('/')[-1]
                print(f'  {fname}: {n} labela vráceno na 2 retka')
                total += n
        except Exception as e:
            print(f'  GRESKA {path}: {e}')

    print(f'\nUkupno: {total} y-pomaka poništeno.')

    if total > 0:
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', 'tools/fix_svg_ns.py'],
            capture_output=True, text=True
        )
        print(result.stdout.strip())


if __name__ == '__main__':
    main()
