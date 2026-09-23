"""Validate the shared content model and its generated presentation contracts."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from book_model import documents, load_book
from build_book import compile_book
from content_index import nodes, parse_source


def preservation(baseline:Path, model):
    """Verify this migration against the pre-refactor sources, including exact TeX."""
    aliases={title:key for key,doc in model['documents'].items() for title in [doc['title'],*doc.get('title_aliases',[])]}
    count=0
    for doc in documents(model):
        old_path=baseline/doc['source'];new_path=ROOT/doc['source']
        old=old_path.read_text(encoding='utf8');new=new_path.read_text(encoding='utf8')
        expected=re.sub(r'(<p class="mf1-box-label">)P\d+\.\s*',r'\1',old)
        expected=re.sub(r'(?m)^(###\s+)Z\d+\.\s+(.+\{#task-)',r'\1\2',expected)
        expected=re.sub(r'<span class="mf1-ch-ref"><span class="mf1-ch-code">pog\.\s*\d+</span><span class="mf1-ch-title">([^<]+)</span></span>',
            lambda m:'[]{.mf1-chapter-ref target="'+aliases[m[1]]+'"}',expected) if doc['kind']!='appendix' else expected
        if doc.get('role')=='glossary':
            new=new.replace('::: {.mf1-glossary}\n\n','')
            new=re.sub(r'\n\n:::\s*$','\n',new)
        if expected.strip()!=new.strip():raise ValueError(f'Unexpected content change: {doc["source"]}')
        old_math=Counter(n['c'][1] for n in nodes(parse_source(old_path)['blocks']) if n['t']=='Math')
        new_math=Counter(n['c'][1] for n in nodes(parse_source(new_path)['blocks']) if n['t']=='Math')
        if old_math!=new_math:raise ValueError(f'Mathematical content changed: {doc["source"]}')
        ids=lambda s:Counter(re.findall(r'\{#([\w-]+)',s))
        if ids(old)!=ids(new):raise ValueError(f'Stable source IDs changed: {doc["source"]}')
        count+=sum(new_math.values())
    print(f'Preservation PASS: {len(documents(model))} sources, {count} identical math expressions and unchanged stable IDs.')


def audit():
    model=load_book();compile_book(write=False)
    index=json.loads((ROOT/'assets/content-index.json').read_text(encoding='utf8'))
    registry=json.loads((ROOT/'components/registry.json').read_text(encoding='utf8'))['components']
    required={'ChapterHeader','SectionHeader','Figure','Equation','Example','Problem','Solution','Assumptions','Given','Required','Interpretation','EngineeringContext','NumericalBridge','MathDerivation','Important','Warning','Summary','InteractiveFigure','Table','GlossaryTerm','Reference'}
    if required-set(registry):raise ValueError('Missing semantic components: '+str(required-set(registry)))
    classes=[name for component in registry.values() for name in component.get('classes',[])]
    if len(classes)!=len(set(classes)):raise ValueError('A source class maps to more than one component')
    for name,component in registry.items():
        if 'visibility' in component:
            policy=component['visibility']
            if not isinstance(policy,list) or any(target not in ('web','pdf','print') for target in policy):
                raise ValueError('Invalid component visibility: '+name)
    for doc in documents(model):
        source=(ROOT/doc['source']).read_text(encoding='utf8')
        if re.search(r'<p class="mf1-box-label">P\d+\. ',source):raise ValueError('Manually numbered example: '+doc['source'])
        if doc['kind']=='chapter' and re.search(r'^### Z\d+\. ',source,re.M):raise ValueError('Manually numbered problem: '+doc['source'])
        for target in re.findall(r'\.mf1-chapter-ref target="([^"]+)"',source):
            if target not in model['documents']:raise ValueError('Missing chapter reference: '+target)
        previous=1
        for section in index['documents'][doc['id']]['sections']:
            if section['level']>previous+1:raise ValueError(f'{doc["id"]}: heading jump to {section["title"]}')
            previous=section['level']
    for identifier,obj in index['objects'].items():
        if identifier!=obj['id'] or obj['document'] not in model['documents']:raise ValueError('Invalid object identity: '+identifier)
        if obj['kind'] in ('Example','Problem') and obj.get('level') not in ('T1','T2','T3','T4'):raise ValueError('Missing semantic level: '+identifier)
        if obj['kind']=='Equation' and not obj.get('latex'):raise ValueError('Empty equation: '+identifier)
        if obj['kind']=='Figure':
            if not obj.get('caption') or not obj.get('alt'):raise ValueError('Missing caption/alt: '+identifier)
            path=ROOT/model['documents'][obj['document']]['path']
            if not (path.parent/obj['source']).resolve().is_file():raise ValueError('Missing figure asset: '+identifier)
    for path in (ROOT/'styles').glob('*.css'):
        css=path.read_text(encoding='utf8')
        if '!important' in css and path.name not in ('utilities.css','print.css'):raise ValueError('Unscoped CSS override: '+str(path))
        if re.search(r'#[ud]\d{2}[_-]|#pojmovnik-',css):raise ValueError('Chapter-specific CSS: '+str(path))
    print('Architecture audit PASS: one hierarchy, generated views, semantic components, object IDs, references, levels and style layers.')
    print('Object inventory:',index['counts'])
    return model


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--baseline',type=Path);args=parser.parse_args()
    try:
        model=audit()
        if args.baseline:preservation(args.baseline,model)
    except ValueError as exc:raise SystemExit('Architecture audit FAIL: '+str(exc)) from exc
