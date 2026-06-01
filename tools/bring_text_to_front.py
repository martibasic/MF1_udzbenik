#!/usr/bin/env python3
"""
bring_text_to_front.py

Premješta SVE <text> elemente na apsolutni kraj SVG dokumenta
(iza svih ostalih elemenata, uključujući dimenzijske linije i okvire).

Zašto: bring_dims_to_front.py premještava elemente sa smeđom bojom
(uključujući okvire s brown stroke-om) na kraj. Ako su text elementi
ispred tih okvira, okviri ih prekrivaju. Ova skripta osigurava da je
tekst uvijek posljednji iscrtani sloj → uvijek vidljiv iznad svakog
pozadinskog elementa.

Redosljed renderiranja koji se postiže:
  1. structural (defs, title, desc)
  2. pozadine, geometrija, gradijenti, hatch
  3. dimenzijske linije (from bring_dims_to_front)
  4. okviri panela (brown rects - premješteni bring_dims_to_front)
  5. TEXT (sve labele, kote, formule) ← uvijek na vrhu
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


class CommentTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def bring_text_to_front_in_container(container):
    """
    Premješta sve <text> direktne djece containera na kraj.
    Vraca broj premještenih text elemenata.
    Cuva redoslijed medusobno (relativni redosljed medu text elementima ostaje isti).
    """
    children = list(container)
    structural = []   # defs, title, desc, metadata
    texts = []        # svi <text> elementi
    others = []       # sve ostalo (geometrija, rects, linije, komentari)

    for child in children:
        if callable(child.tag):  # XML komentar
            others.append(child)
            continue
        local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if local in ('defs', 'title', 'desc', 'metadata'):
            structural.append(child)
        elif local == 'text':
            texts.append(child)
        else:
            others.append(child)

    if not texts:
        return 0  # nema text elemenata, nema sto raditi

    # Preuredi: structural → ostalo (geometrija + okviri) → tekst
    for child in children:
        container.remove(child)
    for child in structural + others + texts:
        container.append(child)

    return len(texts)


def process_file(path):
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(path, parser)
    root = tree.getroot()

    n = bring_text_to_front_in_container(root)

    # Obradi i top-level <g> grupe (ako postoje)
    for child in list(root):
        if callable(child.tag):
            continue
        local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if local == 'g':
            n += bring_text_to_front_in_container(child)

    if n > 0:
        tree.write(path, encoding='unicode', xml_declaration=False)

    return n


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Premještam text elemente na vrh u {len(files)} SVG datoteka...\n')

    changed_files = 0
    total_texts = 0

    for path in files:
        try:
            n = process_file(path)
            if n > 0:
                fname = path.replace('\\', '/').split('/')[-1]
                print(f'  ✓ {fname}  — {n} text elemenata premješteno na kraj')
                changed_files += 1
                total_texts += n
        except Exception as e:
            print(f'  ✗ GREŠKA {path}: {e}')

    print(f'\nGotovo: {changed_files} datoteka, {total_texts} text elemenata sada na vrhu.')

    if changed_files > 0:
        print('\nIspravljam namespace prefikse...')
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', 'tools/fix_svg_ns.py'],
            capture_output=True, text=True
        )
        print(result.stdout.strip())


if __name__ == '__main__':
    main()
