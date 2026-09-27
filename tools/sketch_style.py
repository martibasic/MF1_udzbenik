"""Shared authoring contract for the textbook's technical SVG figures."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / 'assets/figure-tokens.json').read_text(encoding='utf8'))
PALETTE = TOKENS['palette']
FLUID_PAINTS = {PALETTE[key] for key in ('fluid', 'second-fluid', 'mercury', 'gas', 'solution', 'mixture')}


def check_scene_canvas(name, root, count):
    """Check the packed canvas against its reviewed logical scenes.

    Cropping removed prose must not drop a scene or scale its physical geometry.
    Browser audits additionally measure every actual glyph and geometric extent.
    """
    layout = json.loads((ROOT / 'assets/print-layouts.json').read_text(encoding='utf8'))[name]
    x, y, width, height = map(float, root.get('viewBox').split())
    assert (x, y) == (0, 0) and width > 0 and height > 0, name
    scenes = [e for e in root if re.search(r'-scene-\d+$', e.get('id', ''))]
    assert len(scenes) == len(layout['panels']) == count, name
    for scene, (left, top, w, h, *_) in zip(scenes, layout['panels']):
        assert re.fullmatch(r'translate\([-\d.]+ [-\d.]+\)', scene.get('transform', '')), name
        assert 0 <= left < left+w <= width and 0 <= top < top+h <= height, name
    for i, a in enumerate(layout['panels']):
        for b in layout['panels'][i+1:]:
            assert a[0]+a[2] <= b[0] or b[0]+b[2] <= a[0] or a[1]+a[3] <= b[1] or b[1]+b[3] <= a[1], name


def check_uniform_fluid(element, attribute='fill'):
    """One spatially uniform material colour; connectivity is checked separately.

    Replaces the old mandatory-gradient contract after the explicitly requested
    minimalist redesign. A colour gradient must not imply an uncomputed field.
    """
    colour = element.get(attribute)
    if colour not in FLUID_PAINTS:
        raise AssertionError(f"{element.get('id')}: expected uniform fluid {attribute}, got {colour!r}")
