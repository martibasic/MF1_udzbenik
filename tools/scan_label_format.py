#!/usr/bin/env python3
"""
scan_label_format.py
Pronalazi problematicne labele: simbol i iznos su razdvojeni u dva <text>
elementa bez znaka jednakosti, ili je vrijednost bez = znaka.
"""
import xml.etree.ElementTree as ET
import glob
import re

SVG_NS = '{http://www.w3.org/2000/svg}'

# Vrijednost: pocinje brojem+jedinicom (bez = ispred)
VAL_RE = re.compile(
    r'^[\d,]+\s*(mm|cm|m|kN|N|kPa|MPa|Pa|m/s|m²|m³|kg|min⁻\xb9|'
    r'cSt|W|kJ|%|l/s|L/s|bar)',
    re.IGNORECASE
)
APPROX_RE = re.compile(r'^[≈≤≥]\s*[\d,]+')

# Simbol: kratki tekst (1-6 znakova), bez broja
SYM_RE = re.compile(
    r'^[\wΑ-ωΔδτμνρσ'
    r'₀-₉⁻²³_ΣΩ]{1,6}$'
)


def plain_text(elem):
    parts = [elem.text or '']
    for ch in elem:
        if not callable(ch.tag):
            parts.append(ch.text or '')
            parts.append(ch.tail or '')
    return ''.join(parts).strip()


problems = []

for f in sorted(glob.glob('assets/print/u*.svg')):
    try:
        tree = ET.parse(f)
        root = tree.getroot()
        texts = [e for e in root.iter(SVG_NS + 'text') if not callable(e.tag)]

        for i, t in enumerate(texts[:-1]):
            sym = plain_text(t)
            if not SYM_RE.match(sym):
                continue

            nxt = texts[i + 1]
            val = plain_text(nxt)

            # Vec ima = ili pocinje s istim simbolom → ok
            if '=' in val or val.startswith(sym):
                continue

            if not (VAL_RE.match(val) or APPROX_RE.match(val)):
                continue

            sy = float(t.get('y', 0))
            ny = float(nxt.get('y', 0))
            sx = float(t.get('x', 0))
            nx = float(nxt.get('x', 0))
            dy = abs(ny - sy)
            dx = abs(nx - sx)

            # Prostorno blizi: 2 retka (dy<=25) ili isti red (dy<=50, dx<=30)
            if dy <= 25 or (dy <= 50 and dx <= 30):
                fname = f.replace('\\', '/').split('/')[-1]
                problems.append((fname, sym, val, sx, sy, nx, ny))
    except Exception as e:
        print(f'GRESKA {f}: {e}')

print(f'Pronadeno {len(problems)} split labela bez znaka =:\n')
prev_file = ''
for fname, sym, val, sx, sy, nx, ny in problems:
    if fname != prev_file:
        print(f'  {fname}')
        prev_file = fname
    print(f'    [{sym!r} @ x={sx:.0f},y={sy:.0f}] + [{val!r} @ x={nx:.0f},y={ny:.0f}]  dy={abs(ny-sy):.0f}px')
