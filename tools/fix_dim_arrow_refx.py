#!/usr/bin/env python3
"""
fix_dim_arrow_refx.py

Postavlja refX svakog smeđeg (#b7600c) dimenzijskog markera na x-koordinatu
vrha trokuta (rightmost x u path d=). Time vrh strelice TOČNO dodiruje
produljnu liniju (tik-crtu), bez preklapa i bez praznine.

Vrijedi za oba orijentacijska tipa:
  orient="auto"                → marker-end (desna strelica)
  orient="auto-start-reverse"  → marker-start (lijeva strelica)

Dokaz:
  Za orient="auto" (0° rotacija): točka (refX, refY) = vrh trokuta → sjeda točno
    na krajnju točku linije. ✓
  Za orient="auto-start-reverse" (180° rotacija oko refPointa):
    S refX=tip_x: rotacija 180° oko (tip_x, refY) ostavlja vrh na istom mjestu
    ali trokut sad gleda lijevo. Vrh i dalje sjeda točno na attachment točku. ✓
"""

import xml.etree.ElementTree as ET
import glob
import re
import subprocess
import sys

# Registracija namespace-a (sprječava ns0: prefiks u zapisu)
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
ET.register_namespace('dc', 'http://purl.org/dc/elements/1.1/')
ET.register_namespace('cc', 'http://creativecommons.org/ns#')
ET.register_namespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
ET.register_namespace('inkscape', 'http://www.inkscape.org/namespaces/inkscape')
ET.register_namespace('sodipodi', 'http://sodipodi.sourceforge.net/DTD/sodipodi-0.0.dtd')

SVG_NS = '{http://www.w3.org/2000/svg}'
BROWN = '#b7600c'


class CommentTreeBuilder(ET.TreeBuilder):
    """ET TreeBuilder koji čuva XML komentare."""
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def path_tip_x(d):
    """
    Vraća x-koordinatu vrha (rightmost point) iz trokutastog path-a.
    Npr. 'M0,0 L0,6 L7,3 z' → 7.0
    """
    pairs = re.findall(r'(-?[\d.]+),(-?[\d.]+)', d)
    if not pairs:
        return None
    xs = [float(x) for x, y in pairs]
    tip = max(xs)
    # Vrati kao int-string ako je cijeli broj
    return tip


def refx_str(val):
    """Formatira float u string (bez .0 ako je cijeli)."""
    return str(int(val)) if val == int(val) else str(val)


def fix_svg_markers(svg_path):
    """
    U danom SVG-u pronalazi sve smeđe dim markere i ispravlja refX.
    Vraća broj izmijenjenih markera.
    """
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(svg_path, parser)
    root = tree.getroot()

    changed = 0

    for defs in root.iter(SVG_NS + 'defs'):
        for marker in defs.iter(SVG_NS + 'marker'):
            for child in list(marker):
                if callable(child.tag):
                    continue
                local = child.tag.split('}')[-1] if '}' in child.tag else child.tag
                if local != 'path':
                    continue
                if child.get('fill', '') != BROWN:
                    continue
                d = child.get('d', '')
                if not d:
                    continue
                tip_x = path_tip_x(d)
                if tip_x is None:
                    continue
                target_refx = refx_str(tip_x)
                old_refx = marker.get('refX', '')
                if old_refx != target_refx:
                    marker.set('refX', target_refx)
                    changed += 1

    if changed > 0:
        tree.write(svg_path, encoding='unicode', xml_declaration=False)

    return changed


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Provjeram {len(files)} SVG datoteka...\n')

    total_files = 0
    total_markers = 0

    for path in files:
        try:
            n = fix_svg_markers(path)
            if n > 0:
                print(f'  ✓ {path}  — {n} markera popravljeno')
                total_files += 1
                total_markers += n
        except Exception as e:
            print(f'  ✗ GREŠKA {path}: {e}')

    print(f'\nGotovo: {total_files} datoteka, {total_markers} markera ispravljeno.')

    if total_files > 0:
        print('\nIspravljam namespace prefikse...')
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', 'tools/fix_svg_ns.py'],
            capture_output=True, text=True
        )
        print(result.stdout.strip())
        if result.returncode != 0:
            print('GREŠKA namespace fix:', result.stderr)


if __name__ == '__main__':
    main()
