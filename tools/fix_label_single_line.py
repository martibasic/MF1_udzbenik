#!/usr/bin/env python3
"""
fix_label_single_line.py

Standardizira formate labela na svim SVG skicama:
  SIMBOL   →   SIMBOL = IZNOS   (jedan redak, znak jednakosti)
  IZNOS

Algoritam:
  1. Pronadi parove (simbol, vrijednost) koji su razdvojeni u dva <text>
     elementa (isti ili blizak x, y razlika 0–30 px).
  2. Za svaki par:
     a. Ako vrijednost ne pocinje s =, ≈, ≤, ≥ → dodaj "= " ispred
     b. Ako su na razlicitim redovima (dy > 0):
        - Pomakni vrijednost na isti y kao simbol
        - Ako su na istom x, pomakni vrijednost udesno (da ne preklapa simbol)
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

# Uzorak koji je sigurno vrijednost: broj + mjerna jedinica
VAL_RE = re.compile(
    r'^[\d,]+\s*'
    r'(mm|cm|m²|m³|m/s|m³/s|m|kN|N|kPa|MPa|Pa|kg|min⁻\xb9|cSt|W|kW|kJ|%|l/s|L/s|bar)',
    re.IGNORECASE
)
APPROX_RE = re.compile(r'^[≈≤≥]\s*[\d,]+')

# Simbol: 1–6 znakova, bez broja, moze biti greek ili s subscriptom
SYM_RE = re.compile(
    r'^[\wΑ-ωΔδτμνρσₐ₀-₉ΣΩ⁻²³_]{1,7}$'
)

# Znakovi koji znace "vec ima operator usporedbe" - ne treba dodavati =
HAS_OP = re.compile(r'^[=≈≤≥<>]')


class CommentTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


def plain_text(elem):
    """Rekonstruiraj plain text iz <text> elementa (ukljucujuci tspan)."""
    parts = [elem.text or '']
    for ch in elem:
        if not callable(ch.tag):
            parts.append(ch.text or '')
            parts.append(ch.tail or '')
    return ''.join(parts).strip()


def set_text_content(elem, new_content):
    """
    Postavi novi tekstualni sadrzaj elementa.
    Ako elem nema djece: direktno postavi elem.text.
    Ako ima djece (tspan): ostavi tspan djecu, dodaj 'last_tspan.tail'.
    """
    children = [c for c in elem if not callable(c.tag)]
    if not children:
        # Jednostavan slucaj: direktan tekst
        elem.text = new_content
    else:
        # Postoji tspan - dodaj novi sadrzaj kao tail zadnjeg djeteta
        # (ili kao novi tspan ako se sadrzaj treba neovisno stilizirati)
        last_child = children[-1]
        # Zadrzi simbol u djeci, dodaj " = vrijednost" kao tail
        # Postavi tail zadnjeg djeteta
        last_tail = (last_child.tail or '').strip()
        if not last_tail:
            last_child.tail = new_content
        else:
            last_child.tail = new_content  # overwrite


def estimated_sym_width(sym_text, font_size=11.0):
    """
    Aproksimativna sirina simbola u px.
    Gruba procjena: 0.65 * font_size po znaku za neprefiksirane (bez tspan).
    """
    # Prebroji samo "vidljive" znakove (bez unicode subscript koji su manji)
    # Grubo: 8-10px po znaku za font_size 11-13
    char_count = len(sym_text)
    return max(10, char_count * 0.62 * font_size)


def fix_svg(path):
    parser = ET.XMLParser(target=CommentTreeBuilder())
    tree = ET.parse(path, parser)
    root = tree.getroot()

    # Prikupi sve text elemente u redoslijedu (iter() cita DFS)
    texts = [e for e in root.iter(SVG_NS + 'text') if not callable(e.tag)]

    # Izgradi parent mapu
    parent_map = {}
    for parent in root.iter():
        for child in parent:
            parent_map[child] = parent

    fixed = 0
    skip_next = set()  # indeksi text elemenata koji su vec obradeni

    for i, t in enumerate(texts[:-1]):
        if i in skip_next:
            continue

        sym = plain_text(t)
        if not SYM_RE.match(sym):
            continue

        nxt = texts[i + 1]
        if i + 1 in skip_next:
            continue

        val = plain_text(nxt)

        # Vec ima operator?
        if HAS_OP.match(val):
            # Ima operator, ali mozda je na drugom retku - samo pomakni ako dy > 0
            need_eq = False
        elif VAL_RE.match(val) or APPROX_RE.match(val):
            need_eq = True
        else:
            continue

        # Provjeri prostornu blizinu
        try:
            sy = float(t.get('y', 0))
            ny = float(nxt.get('y', 0))
            sx = float(t.get('x', 0))
            nx = float(nxt.get('x', 0))
        except ValueError:
            continue

        dy = abs(ny - sy)
        dx = abs(nx - sx)

        # Kriterij para: isti/slican x i y razlika <= 30px
        # ILI dy=0 i dx > 0 ali mali dy
        if not (dy <= 30 or (dy <= 50 and dx <= 30)):
            continue

        # --- PRIMIJENI POPRAVAK ---

        # 1. Dodaj "= " ako fali
        if need_eq:
            new_val = '= ' + val
        else:
            new_val = val  # vec ima operator (≈ itd)

        # 2. Postavi isti y kao simbol (ako su na razlicitim redovima)
        if dy > 1:
            nxt.set('y', str(sy))

        # 3. Pomakni x udesno ako su na istom x (da ne preklapa simbol)
        if dx <= 10 and dy > 1:
            fs = float(t.get('font-size', 11))
            offset = estimated_sym_width(sym, fs) + 4
            new_x = sx + offset
            nxt.set('x', str(round(new_x, 1)))

        # 4. Upisi novi sadrzaj vrijednosti
        set_text_content(nxt, new_val)

        fixed += 1
        skip_next.add(i + 1)

    if fixed > 0:
        tree.write(path, encoding='unicode', xml_declaration=False)

    return fixed


def main():
    pattern = 'assets/print/u*.svg'
    files = sorted(glob.glob(pattern))
    print(f'Obradujem {len(files)} SVG datoteka...\n')

    total_files = 0
    total_fixed = 0

    for path in files:
        try:
            n = fix_svg(path)
            if n > 0:
                fname = path.replace('\\', '/').split('/')[-1]
                print(f'  {fname}: {n} labela popravljeno')
                total_files += 1
                total_fixed += n
        except Exception as e:
            print(f'  GRESKA {path}: {e}')

    print(f'\nGotovo: {total_files} datoteka, {total_fixed} labela standardizirano.')

    if total_files > 0:
        print('\nIspravljam namespace prefikse...')
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', 'tools/fix_svg_ns.py'],
            capture_output=True, text=True
        )
        print(result.stdout.strip())


if __name__ == '__main__':
    main()
