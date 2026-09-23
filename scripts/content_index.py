"""Derived, searchable object index; canonical Markdown remains authoritative."""
from __future__ import annotations

from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata

from book_model import ROOT, documents, load_book


def plain(value):
    if isinstance(value,list):return ''.join(plain(item) for item in value)
    if not isinstance(value,dict):return ''
    tag,content=value.get('t'),value.get('c')
    if tag in ('Str','Code'):return content if isinstance(content,str) else content[-1]
    if tag in ('Space','SoftBreak','LineBreak'):return ' '
    if tag=='Math':return content[-1]
    if tag in ('Span','Link','Image'):return plain(content[1])
    if tag in ('RawInline','RawBlock'):return html.unescape(re.sub('<[^>]+>','',content[1]))
    return plain(content)


def nodes(value):
    if isinstance(value,dict):
        if 't' in value:yield value
        yield from nodes(value.get('c'))
    elif isinstance(value,list):
        for item in value:yield from nodes(item)


def term_id(text):
    folded=unicodedata.normalize('NFKD',text.casefold())
    folded=''.join(c for c in folded if not unicodedata.combining(c))
    return 'term-'+re.sub(r'[^\w]+','-',folded,flags=re.UNICODE).strip('-')


def parse_source(path,root=ROOT):
    quarto=shutil.which('quarto')
    if not quarto:
        candidate=Path('C:/Program Files/Quarto/bin/quarto.exe')
        if candidate.exists():quarto=str(candidate)
        else:raise ValueError('Quarto is required to index canonical Markdown.')
    digest=hashlib.sha256(path.read_bytes()+b'\nmarkdown-pandoc-quarto-1.9.37-v1').hexdigest()
    cache=root/'tools/tmp/content-ast'/f'{digest}.json'
    if not cache.exists():
        cache.parent.mkdir(parents=True,exist_ok=True)
        run=subprocess.run([quarto,'pandoc',str(path),'--from','markdown','--to','json'],capture_output=True,check=True)
        cache.write_bytes(run.stdout)
    return json.loads(cache.read_text(encoding='utf8'))


def build_index(root=ROOT):
    model=load_book(root)
    figure_manifest=json.loads((root/'assets/pdf-figures/manifest.json').read_text(encoding='utf8'))['figures']
    result={'schema_version':1,'documents':{},'objects':{},'terms':{},'references':[]}
    kinds=Counter()
    for doc in documents(model):
        path=root/doc['source'];source=path.read_text(encoding='utf8');ast=parse_source(path,root)
        record={**doc,'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'sections':[],'objects':[]}
        result['documents'][doc['id']]=record
        counters=Counter()
        def add(identifier,kind,**data):
            if identifier in result['objects']:raise ValueError(f'Duplicate object ID: {identifier}')
            counters[kind]+=1;kinds[kind]+=1
            number= f"{doc['number']}.{counters[kind]}"
            result['objects'][identifier]={'id':identifier,'kind':kind,'document':doc['id'],'number':number,**data}
            record['objects'].append(identifier)
        # Display equations use Quarto's attribute following the TeX block.
        for match in re.finditer(r'\$\$(.*?)\$\$\s*\{#(eq-[^\s}]+)[^}]*\}',source,re.S):
            add(match[2],'Equation',latex=match[1].strip())
        for node in nodes(ast['blocks']):
            if node['t']=='Figure':
                attr,caption,body=node['c'];identifier=attr[0]
                image=next((n for n in nodes(body) if n['t']=='Image'),None)
                if not identifier or not image:continue
                attrs=dict(image['c'][0][2]);asset=image['c'][2][0]
                print_type=figure_manifest.get(Path(asset).name,{}).get('kind','standard')
                add(identifier,'Figure',caption=plain(caption[1]),alt=attrs.get('fig-alt',plain(image['c'][1])),source=asset,
                    type=attrs.get('figure-type',print_type),variants={'web':asset,'print_manifest':'assets/pdf-figures/manifest.json'})
            if node['t']=='Table' and node['c'][0][0].startswith('tbl-'):
                add(node['c'][0][0],'Table',caption=plain(node['c'][1][1]))
        for node in nodes(ast['blocks']):
            if node['t']!='Div' or not node['c'][0][0].startswith('ex-'):continue
            attr,body=node['c'];attrs=dict(attr[2])
            label=attrs.get('title') or (plain(body[1]) if len(body)>1 else plain(body))
            label=html.unescape(label).strip()
            level=re.search(r'\bT[1-4]\b',label)
            title=re.sub(r'^P\d+\.\s*','',re.sub(r'\s*T[1-4]\s*$','',label)).strip()
            add(attr[0],'Example',title=title,level=attrs.get('level') or (level[0] if level else None),label=f'P{counters["Example"]+1}')
        tasks=list(re.finditer(r'^###\s+(?:Z\d+\.\s+)?(.+?)\s*\{#(task-[^\s}]+)[^}]*\}',source,re.M))
        for i,match in enumerate(tasks):
            body=source[match.end():tasks[i+1].start() if i+1<len(tasks) else len(source)]
            level=re.search(r'\[Razina:\s*(T[1-4])\]',body)
            add(match[2],'Problem',title=re.sub(r'^Z\d+\.\s*','',match[1]),level=level[1] if level else None,label=f'Z{i+1}')
        section_counters=[0]*6
        def headings(blocks,inside_component=False):
            for block in blocks:
                if block['t']=='Div':
                    classes=block['c'][0][1]
                    component=inside_component or any(c in ('mf1-we','mf1-gp','mf1-po','mf1-ch') or c.startswith('callout-') for c in classes)
                    headings(block['c'][1],component)
                elif block['t']=='Header':
                    level,attr,title=block['c'];identifier,classes,_=attr
                    if inside_component or 'unnumbered' in classes or 'mf1-step' in classes:continue
                    section_counters[level-1]+=1
                    for deeper in range(level,6):section_counters[deeper]=0
                    number=None if doc['kind']=='frontmatter' else doc['number']+'.'+'.'.join(str(n) for n in section_counters[1:level])
                    record['sections'].append({'id':identifier,'level':level,'title':plain(title),'number':number})
        headings(ast['blocks'])
        for target in re.findall(r'(?<![\w@])@((?:eq|fig|tbl|sec|ex|task)-[\w-]+)',source):
            result['references'].append({'document':doc['id'],'target':target})
        # Glossary rows remain one table in canonical Markdown. Anchors are
        # derived from terms, not their row number, so reordering is harmless.
        if any(node['t']=='Header' and plain(node['c'][2])=='Pojmovnik' for node in ast['blocks']):
            for line in source.splitlines():
                if not line.startswith('|') or line.startswith(('|---','| Pojam')):continue
                cells=[v.strip() for v in line.strip('|').split('|')]
                if len(cells)<3:continue
                key=term_id(re.sub(r'[*$]','',cells[0]))
                result['terms'][key]={'id':key,'term':cells[0],'document':doc['id']}
    known=set(result['objects']) | {s['id'] for d in result['documents'].values() for s in d['sections']}
    missing=[r for r in result['references'] if r['target'] not in known]
    if missing:raise ValueError(f'Unresolved content references: {missing}')
    result['counts']=dict(kinds)
    return result
