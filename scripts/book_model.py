"""Shared, presentation-independent model of the textbook (standard library only)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def load_book(root: Path = ROOT) -> dict[str, Any]:
    model = json.loads((root / 'content/book.json').read_text(encoding='utf-8'))
    validate_book(model, root)
    return model


def documents(model: dict[str, Any], *, kind: str | None = None) -> list[dict[str, Any]]:
    """Numbers are positions, never identities. Appendices have a separate counter."""
    result = []
    for identifier in model['frontmatter']:
        result.append(dict(model['documents'][identifier], id=identifier, kind='frontmatter', number='0', part=None))
    number = 0
    for part in model['parts']:
        for identifier in part['chapters']:
            number += 1
            result.append(dict(model['documents'][identifier], id=identifier, kind='chapter', number=str(number), part=part['id']))
    for number, identifier in enumerate(model['appendices']):
        result.append(dict(model['documents'][identifier], id=identifier, kind='appendix', number=chr(65 + number), part=None))
    return [doc for doc in result if kind is None or doc['kind'] == kind]


def validate_book(model: dict[str, Any], root: Path = ROOT) -> None:
    if model.get('schema_version') != 1:
        raise ValueError('Unsupported book model schema')
    for key,expected in (('book',dict),('documents',dict),('parts',list),('frontmatter',list),('appendices',list)):
        if not isinstance(model.get(key),expected):raise ValueError(f'Invalid book model field: {key}')
    part_ids=[]
    for part in model['parts']:
        if not part.get('id') or not part.get('title') or not isinstance(part.get('chapters'),list):
            raise ValueError('Every part needs an ID, title and chapter list')
        part_ids.append(part['id'])
    if len(part_ids)!=len(set(part_ids)):raise ValueError('Duplicate part ID')
    if len(model['frontmatter'])>1 or len(model['appendices'])>26:
        raise ValueError('This numbering policy supports one chapter 0 and appendices A–Z')
    roles=[doc['role'] for doc in model['documents'].values() if doc.get('role')]
    if len(roles)!=len(set(roles)):raise ValueError('Duplicate document role')
    identifiers = model['frontmatter'] + [key for part in model['parts'] for key in part['chapters']] + model['appendices']
    if len(identifiers) != len(set(identifiers)) or set(identifiers) != set(model['documents']):
        raise ValueError('Every document must occur exactly once in the book hierarchy')
    for field in ('path', 'source'):
        paths = [doc[field] for doc in model['documents'].values()]
        if len(paths) != len(set(paths)):
            raise ValueError(f'Duplicate document {field}')
        for value in paths:
            target = (root / value).resolve()
            if not target.is_relative_to(root.resolve()):
                raise ValueError(f'Path escapes project: {value}')
            if field == 'source' and not target.is_file():
                raise ValueError(f'Missing canonical source: {value}')
    for key, doc in model['documents'].items():
        if not doc.get('title', '').strip():
            raise ValueError(f'{key}: missing title')


def verification_chapters(model: dict[str, Any] | None = None) -> list[dict[str, str]]:
    return [dict(id=doc['id'].upper(), source=doc['source'], verifier_module=doc['verification']['module'],
                 verifier_namespace=doc['verification']['namespace'])
            for doc in documents(model or load_book(), kind='chapter') if 'verification' in doc]
