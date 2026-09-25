"""Check the shared SVG contract and run the independent geometry verifiers.

The visual review and source-to-figure decisions remain an editorial assessment;
this audit only makes the machine-checkable part reproducible in publication CI.
"""
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from sketch_style import ROOT, PALETTE, TOKENS


def main():
    used = set()
    for source in (ROOT / 'source').glob('*.md'):
        used.update(re.findall(r'\.\./assets/print/([^\s)]+\.svg)', source.read_text(encoding='utf8')))
    issues = []
    boundaries = 0
    for name in sorted(used):
        root = ET.parse(ROOT / 'assets/print' / name).getroot()
        ids = {e.get('id'): e for e in root.iter() if e.get('id')}
        def fail(message): issues.append(f'{name}: {message}')
        for e in root.iter():
            tag = e.tag.split('}')[-1]
            if tag in ('linearGradient', 'radialGradient', 'filter', 'image'):
                fail(f'nontechnical/decorative rendering: {tag}')
            for attribute in ('fill', 'stroke'):
                colour = e.get(attribute)
                if colour and colour not in ('none', 'transparent', 'currentColor'):
                    if colour.startswith('url(#'):
                        target = ids.get(colour[5:-1])
                        if target is None or not target.tag.endswith('pattern'):
                            fail(f'invalid material pattern {colour}')
                    elif colour not in PALETTE.values():
                        fail(f'colour outside shared palette: {colour}')
            if 'font-family' in e.attrib and e.get('font-family') != TOKENS['figure-font-family']:
                fail('inconsistent label font')
            if tag == 'text' and e.get('fill') != PALETTE['ink']:
                fail('text must retain dark, colour-independent contrast')
            if e.get('data-mf1-role') == 'control-volume':
                boundaries += 1
                if e.get('fill') != 'none' or not e.get('stroke-dasharray'):
                    fail('control boundary is not a distinct unfilled dashed line')
                if tag == 'path' and not e.get('d', '').strip().upper().endswith('Z'):
                    fail(f'open control boundary: {e.get("id")}')
            for attribute in ('marker-start', 'marker-end'):
                if attribute not in e.attrib: continue
                marker = ids.get(e.get(attribute)[5:-1])
                if marker is None:
                    fail('missing arrowhead')
                    continue
                for head in marker:
                    colour = head.get('fill') if head.get('fill', 'none') != 'none' else head.get('stroke')
                    if colour != e.get('stroke'):
                        fail(f'arrowhead does not match its line: {e.get("id", attribute)}')
        # Distinctions that must remain readable in monochrome.
        for a,b in [('u09egl_egl','u09egl_hgl'),('u09v2_jet1','u09v2_jet3'),('u13ex_z4pump','u13ex_z4system')]:
            if a in ids and b in ids and ids[a].get('stroke-dasharray') == ids[b].get('stroke-dasharray'):
                fail(f'{a}/{b}: curves cannot depend only on colour')
        bars = [e for e in root.iter() if e.get('data-mf1-role') == 'energy-component']
        if bars and (len(bars) != 6 or len({e.get('fill') for e in bars}) != 3):
            fail('energy columns must distinguish all three contributions')
    if issues:
        print('\n'.join(issues), file=sys.stderr)
        return 1
    print(f'SVG design PASS: {len(used)} figures, {boundaries} explicit control boundaries.')
    for script in sorted((ROOT / 'tools').glob('check_u*_sketch_geometry.py')):
        subprocess.run([sys.executable, '-X', 'utf8', str(script)], cwd=ROOT, check=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
