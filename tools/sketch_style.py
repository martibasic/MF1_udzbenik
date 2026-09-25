"""Shared authoring contract for the textbook's technical SVG figures."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / 'assets/figure-tokens.json').read_text(encoding='utf8'))
PALETTE = TOKENS['palette']
FLUID_PAINTS = {PALETTE[key] for key in ('fluid', 'second-fluid', 'mercury', 'gas', 'solution', 'mixture')}


def check_uniform_fluid(element, attribute='fill'):
    """One spatially uniform material colour; connectivity is checked separately.

    Replaces the old mandatory-gradient contract after the explicitly requested
    minimalist redesign. A colour gradient must not imply an uncomputed field.
    """
    colour = element.get(attribute)
    if colour not in FLUID_PAINTS:
        raise AssertionError(f"{element.get('id')}: expected uniform fluid {attribute}, got {colour!r}")
