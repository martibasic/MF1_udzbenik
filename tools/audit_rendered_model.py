"""Check rendered HTML against the canonical object index, including browser print."""
from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]


class Node:
    def __init__(self,tag='',attrs=()):
        self.tag=tag;self.attrs=dict(attrs);self.children=[]
    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child,Node):yield from child.walk()
    def text(self):
        return ''.join(c.text() if isinstance(c,Node) else c for c in self.children)
    def find(self,**attrs):
        return next((n for n in self.walk() if all(n.attrs.get(k)==v for k,v in attrs.items())),None)


class Page(HTMLParser):
    void={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self,path):
        super().__init__(convert_charrefs=True);self.root=Node();self.stack=[self.root]
        self.feed(path.read_text(encoding='utf8'))
        self.nodes=list(self.root.walk())
        self.ids={n.attrs['id']:n for n in self.nodes if n.attrs.get('id')}
    def handle_starttag(self,tag,attrs):
        node=Node(tag,attrs);self.stack[-1].children.append(node)
        if tag not in self.void:self.stack.append(node)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag:self.stack=self.stack[:i];break
    def handle_data(self,data):self.stack[-1].children.append(data)


def audit(site):
    index=json.loads((ROOT/'assets/content-index.json').read_text(encoding='utf8'))
    collection=Page(site/'chapters/za_ispis.html');errors=[];checked=0
    for doc in index['documents'].values():
        page=Page(site/Path(doc['path']).with_suffix('.html'))
        main=next(n for n in page.nodes if n.tag=='main')
        if sum(n.tag=='h1' for n in main.walk())!=1:errors.append(doc['id']+': expected one chapter H1')
        for current,label in ((page,doc['id']),(collection,'print/'+doc['id'])):
            for key in doc['objects']:
                obj=index['objects'][key];node=current.ids.get(key)
                if node is None:
                    errors.append(f'{label}: missing {key}');continue
                if obj['kind']=='Problem':
                    node=next((n for n in current.nodes if n.attrs.get('data-object-id')==key),node)
                if node.attrs.get('data-number')!=obj['number']:
                    errors.append(f'{label}/{key}: data-number {node.attrs.get("data-number")} != {obj["number"]}')
                if obj['kind']=='Equation':
                    expected='\\tag{'+obj['number']+'}'
                    if expected not in node.text():errors.append(f'{label}/{key}: missing visible {expected}')
                elif obj['kind'] in ('Figure','Table'):
                    caption=next((n for n in node.walk() if n.tag in ('figcaption','caption')),None)
                    if not caption or not re.match(r'(Slika|Tablica)\s+'+re.escape(obj['number'])+r'\b',caption.text().strip()):
                        errors.append(f'{label}/{key}: wrong caption number: {caption.text()[:65] if caption else "absent"}')
                else:
                    if node.attrs.get('data-level')!=obj['level']:errors.append(f'{label}/{key}: missing semantic level')
                    if not node.text().strip().startswith(obj['label']+'.'):errors.append(f'{label}/{key}: missing visible {obj["label"]}')
                checked+=1
            for section in doc['sections']:
                if current is collection:
                    scope=current.ids['print-'+doc['id']]
                    # Quarto suffixes implicit IDs which repeat between chapters.
                    # Scope and canonical number identify the same section.
                    node=next((n for n in scope.walk() if n.tag=='h'+str(section['level']) and
                               (n.attrs.get('data-number')==section['number'] if section['number'] else n.text().strip()==section['title'])),None)
                else:node=current.ids.get(section['id'])
                if node is None:errors.append(f'{label}: missing section {section["id"]}');continue
                heading=next((n for n in node.walk() if re.fullmatch('h[1-6]',n.tag)),None)
                if not heading:errors.append(f'{label}: missing heading {section["id"]}');continue
                number=next((n.text() for n in heading.walk() if 'header-section-number' in n.attrs.get('class','').split()),'')
                if number!=(section['number'] or ''):errors.append(f'{label}/{section["id"]}: heading {number} != {section["number"]}')
    home=Page(site/'index.html')
    main=next(n for n in home.nodes if n.tag=='main')
    if sum(n.tag=='h1' for n in main.walk())!=1:errors.append('home: expected one H1')
    if errors:raise ValueError('\n'.join(errors))
    print(f'Rendered model PASS: {checked} numbered objects in WEB/PRINT, all chapter sections and semantic levels agree.')


if __name__=='__main__':
    try:audit(Path(sys.argv[1] if len(sys.argv)>1 else ROOT/'_site'))
    except ValueError as exc:raise SystemExit('Rendered model FAIL:\n'+str(exc)) from exc
