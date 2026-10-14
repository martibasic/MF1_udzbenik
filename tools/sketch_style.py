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


# Vector arrow semantics (standard of 14 October 2026, requested by the author).
# One vector colour; the physical kind of a vector is carried by line weight,
# arrowhead and dash so that force and velocity differ also in monochrome print.
# Widths are in canonical SVG units; the print generator scales them uniformly.
VECTOR_STYLES = {
    'force':            {'width': (2.4, 3.4), 'head': 'filled', 'dashed': False},
    'moment':           {'width': (2.4, 3.4), 'head': 'filled', 'dashed': False},
    'velocity':         {'width': (1.3, 2.0), 'head': 'open',   'dashed': False},
    'angular-velocity': {'width': (1.3, 2.0), 'head': 'open',   'dashed': False},
    'acceleration':     {'width': (1.6, 2.4), 'head': 'filled', 'dashed': True},
    'pressure':         {'width': (0.8, 1.6), 'head': 'filled', 'dashed': False},
    'unit':             {'width': (0.8, 1.6), 'head': 'filled', 'dashed': False},
}
# Arrows that are not physical vectors keep auxiliary/contour colours.
NONVECTOR_ARROW_ROLES = {'dimension', 'axis', 'leader', 'streamline', 'path', 'diagram'}


def check_arrow_semantics(root):
    """Return issues for arrows whose physical kind is undeclared or mis-styled."""
    parent = {child: node for node in root.iter() for child in node}
    ids = {e.get('id'): e for e in root.iter() if e.get('id')}

    def inherited(e, attribute, default=None):
        while e is not None:
            if e.get(attribute) is not None:
                return e.get(attribute)
            e = parent.get(e)
        return default

    def head_kind(marker):
        heads = [h for h in marker.iter() if h is not marker and h.tag.split('}')[-1] in ('path', 'polygon', 'polyline', 'line')]
        if not heads:
            return None
        kinds = {'open' if h.get('fill', inherited(h, 'fill', 'black')) == 'none' else 'filled' for h in heads}
        return kinds.pop() if len(kinds) == 1 else 'mixed'

    issues = []
    for e in root.iter():
        refs = [e.get(a) for a in ('marker-start', 'marker-end') if e.get(a)]
        if not refs:
            continue
        name = e.get('id') or f"<{e.tag.split('}')[-1]} d={(e.get('d') or '')[:24]!r}>"
        kind = e.get('data-mf1-vector')
        stroke = inherited(e, 'stroke')
        if kind is None:
            role = e.get('data-mf1-role')
            if role not in NONVECTOR_ARROW_ROLES:
                issues.append(f'{name}: arrow without data-mf1-vector or a non-vector data-mf1-role')
            elif stroke == PALETTE['vector']:
                issues.append(f'{name}: non-vector arrow ({role}) uses the vector colour')
            continue
        style = VECTOR_STYLES.get(kind)
        if style is None:
            issues.append(f'{name}: unknown vector kind {kind!r}')
            continue
        if stroke != PALETTE['vector']:
            issues.append(f'{name}: {kind} vector must use the vector colour')
        try:
            width = float(inherited(e, 'stroke-width', '1'))
        except ValueError:
            width = -1
        lo, hi = style['width']
        if not lo <= width <= hi:
            issues.append(f'{name}: {kind} line weight {width} outside {lo}–{hi}')
        dashed = inherited(e, 'stroke-dasharray', 'none') not in ('none', '')
        if dashed != style['dashed']:
            issues.append(f'{name}: {kind} vector must {"" if style["dashed"] else "not "}be dashed')
        for ref in refs:
            marker = ids.get(ref[5:-1]) if ref.startswith('url(#') else None
            if marker is None:
                continue
            if head_kind(marker) != style['head']:
                issues.append(f'{name}: {kind} vector needs an {style["head"]} arrowhead')
    return issues
