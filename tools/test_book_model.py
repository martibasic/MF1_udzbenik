"""Regression tests for content movement, identity and cross-reference integrity."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import subprocess
import shutil
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from book_model import documents, load_book, validate_book
from content_index import build_index
from build_book import figure_text_width


class BookModelTests(unittest.TestCase):
    def test_typed_components_render_without_custom_html(self):
        index=json.loads((ROOT/'assets/content-index.json').read_text(encoding='utf8'))
        example=next(o for o in index['objects'].values() if o['kind']=='Example')
        problems=[o for o in index['objects'].values() if o['kind']=='Problem'][:2]
        source=f'::: {{#{example["id"]} .mf1-we title="Typed title" level="{example["level"]}"}}\n**Zadano.** Data.\n\n**Rješenje.** Method.\n:::\n\n::: {{.mf1-vjezbe-list}}\n'
        for obj in problems:
            source+=f'### Task {{#{obj["id"]} .unnumbered .unlisted}}\n\nBody for {obj["id"]}.\n\n[Razina: {obj["level"]}]{{.mf1-task-level}}\n\n'
        source+=':::\n\n@'+example['id']+'\n'
        result=subprocess.run([shutil.which('quarto'),'pandoc','-f','markdown','-t','html5','--section-divs',
             '--lua-filter',str(ROOT/'filters/mf1-components.lua'),'--lua-filter',str(ROOT/'filters/mf1-html-components.lua')],
             input=source,text=True,encoding='utf8',capture_output=True,check=True)
        from audit_rendered_model import Page,Node
        parser=Page.__new__(Page);super(Page,parser).__init__(convert_charrefs=True)
        parser.root=Node();parser.stack=[parser.root];parser.feed(result.stdout)
        nodes=list(parser.root.walk())
        for obj in problems:
            article=next(n for n in nodes if n.attrs.get('data-object-id')==obj['id'])
            self.assertEqual(article.tag,'article')
            self.assertIn('Body for '+obj['id'],re.sub(r'\s+',' ',article.text()))
            self.assertTrue(article.text().strip().startswith(obj['label']+'.'))
        self.assertTrue(any(n.attrs.get('data-component')=='Given' for n in nodes))
        self.assertTrue(any(n.attrs.get('data-component')=='Solution' for n in nodes))
        self.assertIn('primjer '+example['number'],result.stdout)

    def test_physical_figure_canvas_follows_margins(self):
        self.assertEqual(figure_text_width({'paper':'a4','margin_x_mm':26}),447.874)
        self.assertGreater(figure_text_width({'paper':'a4','margin_x_mm':20}),447.874)
        with self.assertRaisesRegex(ValueError,'no content width'):
            figure_text_width({'paper':'a4','margin_x_mm':110})

    def test_chapter_reorder_changes_numbers_not_identity(self):
        model=load_book();before={d['id']:d for d in documents(model)}
        model['parts'][0]['chapters'].reverse()
        after={d['id']:d for d in documents(model)}
        first=model['parts'][0]['chapters'][0]
        self.assertNotEqual(before[first]['number'],after[first]['number'])
        for key in before:
            self.assertEqual(before[key]['path'],after[key]['path'])
            self.assertEqual(before[key]['source'],after[key]['source'])
        self.assertEqual([d['number'] for d in documents(model,kind='appendix')],list('ABCDEF'))

    def test_duplicate_chapter_rejected(self):
        model=load_book();model['parts'][0]['chapters'].append(model['parts'][0]['chapters'][0])
        with self.assertRaisesRegex(ValueError,'exactly once'):validate_book(model)

    def test_path_escape_rejected(self):
        model=load_book();model['documents']['u01']['source']='../outside.md'
        with self.assertRaisesRegex(ValueError,'escapes'):validate_book(model)

    def test_object_reorder_and_missing_reference(self):
        parent=ROOT/'tools/tmp';parent.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(prefix='book-model-',dir=parent) as directory:
            root=Path(directory).resolve();self.assertTrue(root.is_relative_to(parent.resolve()))
            for name in ('content','source','assets/pdf-figures'): (root/name).mkdir(parents=True)
            model={'schema_version':1,'book':{'title':'Test'},'frontmatter':[],
                   'parts':[{'id':'part','title':'Part','chapters':['stable']}],'appendices':[],
                   'documents':{'stable':{'title':'Example chapter','source':'source/chapter.md','path':'chapters/chapter.qmd'}}}
            (root/'content/book.json').write_text(json.dumps(model),encoding='utf8')
            (root/'assets/pdf-figures/manifest.json').write_text('{"figures":{}}',encoding='utf8')
            a='## Alpha {#sec-alpha}\n\n$$ a = 1 $$ {#eq-alpha}\n'
            b='## Beta {#sec-beta}\n\n$$ b = 2 $$ {#eq-beta}\n'
            source=root/'source/chapter.md';source.write_text(a+'\n'+b,encoding='utf8')
            first=build_index(root)
            source.write_text(b+'\n'+a,encoding='utf8');second=build_index(root)
            self.assertEqual(first['objects']['eq-alpha']['number'],'1.1')
            self.assertEqual(second['objects']['eq-alpha']['number'],'1.2')
            self.assertEqual(first['objects']['eq-alpha']['latex'],second['objects']['eq-alpha']['latex'])
            self.assertEqual(first['documents']['stable']['sections'][0]['id'],'sec-alpha')
            self.assertEqual(second['documents']['stable']['sections'][0]['id'],'sec-beta')
            source.write_text(a+'\n@eq-missing\n',encoding='utf8')
            with self.assertRaisesRegex(ValueError,'Unresolved'):build_index(root)
            source.write_text(a+'\n'+a,encoding='utf8')
            with self.assertRaisesRegex(ValueError,'Duplicate object'):build_index(root)


if __name__=='__main__':unittest.main()
