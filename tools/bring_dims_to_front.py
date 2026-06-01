#!/usr/bin/env python3
"""
bring_dims_to_front.py
Prebacuje sve dimenzijske elemente (smeđa boja #b7600c) na kraj SVG dokumenta
(= "bring to front" u SVG render redu) da budu vidljivi iznad fluida i geometrije.

Čuva XML komentare.
"""
import xml.etree.ElementTree as ET
import glob
import sys

# Registracija namespacea za čist ispis bez ns0: prefiksa
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('cc', 'http://creativecommons.org/ns#')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('svg', 'http://www.w3.org/2000/svg')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')

BROWN = '#b7600c'


class CommentTreeBuilder(ET.TreeBuilder):
    """ET TreeBuilder koji čuva XML komentare."""
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def is_dim(elem):
    """
    Vraća True ako je element dimenzijski (smeđa boja).
    IZNIMKA: <rect> i <polygon> s nebrown fill-om su okviri panela —
    ne premještamo ih jer bi pokrili sadržajni tekst unutar okvira.
    Te elemente ostavlja bring_text_to_front.py na kraju.
    """
    if callable(elem.tag):  # Comment node
        return False
    local = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
    stroke = elem.get('stroke', '')
    fill = elem.get('fill', '')

    # Okviri panela (rect/polygon s nebrown fill-om, npr. fill="#fff7f0"):
    # premještanje bi ih stavilo iza text-a koji je vec na kraju → NE premještaj
    if local in ('rect', 'polygon', 'ellipse'):
        return fill == BROWN  # samo ako je fill brown (npr. legenda-swatch)

    return stroke == BROWN or fill == BROWN


def reorder_container(container):
    """
    Premjesti smeđe elemente na kraj child-liste danog containera.
    Vraća broj premještenih elemenata.
    """
    children = list(container)
    structural = []   # defs, title, desc, metadata
    regular = []      # ostali elementi i komentari
    dims = []         # smeđi dimenzijski elementi

    for child in children:
        if callable(child.tag):  # Comment
            regular.append(child)
            continue
        local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if local in ('defs', 'title', 'desc', 'metadata'):
            structural.append(child)
        elif is_dim(child):
            dims.append(child)
        else:
            regular.append(child)

    if not dims:
        return 0

    # Očisti i napuni u redoslijedu: structural → regular → dims
    for child in children:
        container.remove(child)
    for child in structural + regular + dims:
        container.append(child)

    return len(dims)


def process_file(path):
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(path, parser)
    root = tree.getroot()

    moved = reorder_container(root)

    # Obradi i top-level <g> grupe
    for child in list(root):
        if callable(child.tag):
            continue
        local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
        if local == 'g':
            moved += reorder_container(child)

    if moved == 0:
        return 0

    tree.write(path, encoding='unicode', xml_declaration=False)
    return moved


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    if not files:
        print('Nema SVG datoteka za obradu.')
        sys.exit(1)

    print(f'Obradujem {len(files)} SVG datoteka...\n')
    changed_files = 0
    total_moved = 0

    for path in files:
        try:
            n = process_file(path)
            if n > 0:
                print(f'  ✓ {path}  — {n} dimenzijskih elemenata premješteno na kraj')
                changed_files += 1
                total_moved += n
        except Exception as e:
            print(f'  ✗ GREŠKA {path}: {e}')

    print(f'\nGotovo: {changed_files} datoteka promijenjeno, {total_moved} elemenata premješteno na vrh.')


if __name__ == '__main__':
    main()
