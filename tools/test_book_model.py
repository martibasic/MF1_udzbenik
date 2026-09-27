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
    def test_exercise_fields_in_both_formats(self):
        index=json.loads((ROOT/'assets/content-index.json').read_text(encoding='utf8'))
        example=next(o for o in index['objects'].values() if o['kind']=='Example')
        problem=next(o for o in index['objects'].values() if o['kind']=='Problem')
        source=f'''::: {{#{example['id']} .mf1-we title="Example"}}
**Tekst zadatka.** Input A.

**Traži se:** Request A.

**Rješenje**

Method A.

**Provjera i tumačenje**

Check A.
:::

::: {{.mf1-vjezbe-list}}
### Task {{#{problem['id']} .unnumbered .unlisted}}

**Tekst zadatka**

Input B.

**Traži se**

7. First request.
8. Final request.

:::: {{.content-visible .mf1-hint-online when-format="html"}}
Hint B.
::::

[Razina: T2]{{.mf1-task-level}}
:::
'''
        command=[shutil.which('quarto'),'pandoc','-f','markdown','--lua-filter',str(ROOT/'filters/mf1-components.lua')]
        html=subprocess.run(command+['-t','html5','--lua-filter',str(ROOT/'filters/mf1-html-components.lua')],
                            input=source,text=True,encoding='utf8',capture_output=True,check=True).stdout
        from audit_rendered_model import Page,Node
        parser=Page.__new__(Page);super(Page,parser).__init__(convert_charrefs=True)
        parser.root=Node();parser.stack=[parser.root];parser.feed(html)
        task=next(n for n in parser.root.walk() if n.attrs.get('data-object-id')==problem['id'])
        fields=[n for n in task.walk() if n.attrs.get('data-component') in ('Statement','Required')]
        self.assertEqual([n.attrs['data-component'] for n in fields],['Statement','Required'])
        self.assertIn('Final request.',fields[1].text())
        self.assertNotIn('Hint B.',fields[1].text())
        self.assertNotIn('Razina:',fields[1].text())
        typst=subprocess.run(command+['-t','typst','--lua-filter',str(ROOT/'filters/mf1-typst-author-blocks.lua')],
                             input=source,text=True,encoding='utf8',capture_output=True,check=True).stdout
        self.assertEqual(typst.count('#mf1-minor-heading(['),6)
        self.assertNotIn('Tekst zadatka.',typst)
        self.assertNotIn('Traži se:',typst)
        self.assertIn('First request.',typst)
        self.assertIn('Final request.',typst)
        self.assertIn('#mf1-task-level',typst)
        self.assertIn('#mf1-exercise-body[',typst)
        self.assertEqual(typst.count('#set enum('),1)
        self.assertRegex(typst,r'start:\s*7')

    def test_editorial_contract_rejects_missing_or_reordered_fields(self):
        from audit_publication import editorial_field_issues
        fields=['Tekst zadatka','Traži se','Rješenje','Provjera i tumačenje']
        source='::: {#ex-test .mf1-we}\n'+'\n\n'.join('**'+f+'**\n\nContent.' for f in fields)+'\n:::\n'
        source+='### Task {#task-test}\n\n**Tekst zadatka**\n\nInput.\n\n**Traži se**\n\nRequest.\n:::: {.content-visible}\nHint.\n::::\n'
        self.assertEqual(editorial_field_issues(source),[])
        self.assertEqual(len(editorial_field_issues(source.replace('**Tekst zadatka**','**Podatci**'))),2)
        self.assertEqual(len(editorial_field_issues(source.replace('**Tekst zadatka**','**Zadano**'))),2)
        self.assertTrue(editorial_field_issues(source.replace('**Rješenje**','**Traži se**')))

    def test_answer_key_summary_omits_exercise_field_labels(self):
        from generate_exercise_key import tasks_from_source
        model=load_book()
        for chapter in documents(model,kind='chapter'):
            for task in tasks_from_source(ROOT/chapter['source']):
                self.assertNotIn('**Zadano**',task['prompt'])
                self.assertNotIn('**Tekst zadatka**',task['prompt'])
                self.assertNotIn('**Traži se**',task['prompt'])
                self.assertEqual(task['prompt'].count('$')%2,0)

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
