#!/usr/bin/env python3
"""
detect_box_geometry_overlap.py

Detektira isti razred greške kao u u02_val2: formula/info/result box (svijetli
zaobljeni okvir koji bi smio sadržavati SAMO tekst) preklapa se s nacrtanom
geometrijom (linije, putanje, poligoni, krugovi, stijenke = stroked rect-ovi).

Ovo NE popravlja — samo prijavljuje prioritetnu listu jer svaki popravak
zahtijeva individualnu geometrijsku prosudbu.

Logika:
  1. "Content box" = rect s rx>=6 i fill-om iz skupa tipičnih boja
     formula/result/info kutija (svijetlo plavi/zeleni/žuti/crveni tintovi).
     Veliki panel-background (#f8fafc, #fbfdff, #ffffff) se NE broji — on
     legitimno sadrži geometriju.
  2. Za svaki content box, provjeri presijeca li interijer (umanjen za 4 px)
     bilo koja crtačka primitiva: <line>, <path>, <polygon>, <circle>,
     ili <rect> sa stroke-om koji NIJE content box (= geometrijska stijenka).
  3. Prijavi presjeke.
"""

from __future__ import annotations

import glob
import re
import xml.etree.ElementTree as ET

SVG_NS = '{http://www.w3.org/2000/svg}'

# Fill-ovi tipični za formula/result/info kutije (NE za panel-background).
BOX_FILLS = {
    '#eaf4fb', '#e8f5e9', '#eaf6ee', '#f0f7ff', '#fde8e8', '#fff7e6',
    '#f5f9fd', '#f4f9fd', '#fdf8f2', '#f1f9f3', '#fdf2f2', '#f7fbfd',
    '#eef6ff', '#f0fff4', '#fff7f0', '#fdecea', '#f8f4f9', '#fafcff',
}
# Panel-background fill-ovi koje IGNORIRAMO (smiju sadržavati geometriju).
PANEL_BG_FILLS = {'#f8fafc', '#fbfdff', '#ffffff', '#f4f6f8', '#f4f6f9'}


def gf(elem, attr, default=0.0):
    try:
        return float(elem.get(attr, default))
    except (ValueError, TypeError):
        return default


def local(elem):
    return elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag


class Box:
    __slots__ = ('x', 'y', 'w', 'h', 'fill')

    def __init__(self, x, y, w, h, fill):
        self.x, self.y, self.w, self.h, self.fill = x, y, w, h, fill

    @property
    def x2(self):
        return self.x + self.w

    @property
    def y2(self):
        return self.y + self.h


def elem_bbox(elem):
    """Vrati (x1,y1,x2,y2) bounding box crtačke primitive ili None."""
    t = local(elem)
    if t == 'line':
        x1, y1 = gf(elem, 'x1'), gf(elem, 'y1')
        x2, y2 = gf(elem, 'x2'), gf(elem, 'y2')
        return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    if t == 'rect':
        x, y = gf(elem, 'x'), gf(elem, 'y')
        return (x, y, x + gf(elem, 'width'), y + gf(elem, 'height'))
    if t == 'circle':
        cx, cy, r = gf(elem, 'cx'), gf(elem, 'cy'), gf(elem, 'r')
        return (cx - r, cy - r, cx + r, cy + r)
    if t == 'polygon' or t == 'polyline':
        pts = re.findall(r'(-?[\d.]+)[ ,]+(-?[\d.]+)', elem.get('points', ''))
        if not pts:
            return None
        xs = [float(p[0]) for p in pts]
        ys = [float(p[1]) for p in pts]
        return (min(xs), min(ys), max(xs), max(ys))
    if t == 'path':
        nums = re.findall(r'-?[\d.]+', elem.get('d', ''))
        if len(nums) < 2:
            return None
        coords = [float(n) for n in nums]
        xs = coords[0::2]
        ys = coords[1::2]
        if not xs or not ys:
            return None
        return (min(xs), min(ys), max(xs), max(ys))
    return None


def overlaps(box, bb, margin=4.0):
    """Presijeca li bbox unutrašnjost boxa (umanjenu za margin)?"""
    bx1, by1 = box.x + margin, box.y + margin
    bx2, by2 = box.x2 - margin, box.y2 - margin
    ex1, ey1, ex2, ey2 = bb
    # Mora postojati stvarni presjek površina (ne samo dodir)
    ix = min(bx2, ex2) - max(bx1, ex1)
    iy = min(by2, ey2) - max(by1, ey1)
    return ix > 1.0 and iy > 1.0


def is_content_box(elem):
    if local(elem) != 'rect':
        return False
    if gf(elem, 'rx') < 6:
        return False
    fill = (elem.get('fill') or '').strip().lower()
    return fill in BOX_FILLS


def process_file(path):
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        return [f'XML parse error: {e}']
    root = tree.getroot()

    elems = [e for e in root.iter() if not callable(e.tag)]
    boxes = [Box(gf(e, 'x'), gf(e, 'y'), gf(e, 'width'), gf(e, 'height'),
                 (e.get('fill') or '').lower())
             for e in elems if is_content_box(e)]
    if not boxes:
        return []

    findings = []
    for box in boxes:
        hits = 0
        for e in elems:
            t = local(e)
            if t not in ('line', 'rect', 'circle', 'polygon', 'polyline', 'path'):
                continue
            # Preskoči sam content box i panel-background
            if is_content_box(e):
                continue
            fill = (e.get('fill') or '').strip().lower()
            if fill in PANEL_BG_FILLS:
                continue
            # rect bez stroke-a i bez geometrijskog fill-a preskačemo ako je svijetli
            bb = elem_bbox(e)
            if bb is None:
                continue
            if overlaps(box, bb):
                hits += 1
        if hits > 0:
            findings.append(
                f'box fill={box.fill} [{box.x:.0f},{box.y:.0f} '
                f'{box.w:.0f}×{box.h:.0f}] ← {hits} geom. presjek(a)'
            )
    return findings


def main():
    files = sorted(glob.glob('assets/print/u*.svg'))
    flagged = []
    for path in files:
        fname = path.replace('\\', '/').split('/')[-1]
        try:
            f = process_file(path)
            if f:
                flagged.append((fname, f))
        except Exception as e:
            print(f'GREŠKA {fname}: {e}')

    if not flagged:
        print('Nema prijavljenih preklapanja formula-box ↔ geometrija.')
        return

    print(f'Prijavljeno {len(flagged)} datoteka s mogućim box↔geometrija preklapanjem:\n')
    for fname, items in flagged:
        print(f'  {fname}')
        for it in items:
            print(f'      {it}')


if __name__ == '__main__':
    main()
