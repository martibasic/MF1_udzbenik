"""Change only the registry; exercise actual shared/HTML/Typst Lua filters."""
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.by_id = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data:
            self.by_id[data['id']] = data


class ComponentVisibilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='visibility-', dir=ROOT / 'tools/tmp')
        self.root = Path(self.temp.name)
        for name in ('filters', 'components', 'assets', 'design-system'):
            (self.root / name).mkdir()
        for path in (ROOT / 'filters').glob('*.lua'):
            shutil.copy2(path, self.root / 'filters' / path.name)
        for name in ('assets/book-model.json', 'assets/content-index.json', 'design-system/tokens.json'):
            shutil.copy2(ROOT / name, self.root / name)
        (self.root / 'assets/pdf-figures').mkdir()
        (self.root / 'assets/pdf-figures/manifest.json').write_text('{"figures":{}}')
        self.registry = json.loads((ROOT / 'components/registry.json').read_text(encoding='utf8'))
        # A new component proves the PDF adapter does not rely on legacy names.
        self.registry['components']['TestNote'] = {
            'classes': ['mf1-test-note'], 'html': 'section', 'pdf_mode': 'panel',
            'label': 'Test note', 'accent': 'mf1-muted',
        }
        self.source = '\n\n'.join(
            f'## Heading {i} {{#heading-{i} .unnumbered}}\n\n'
            f'::: {{#component-{i} .{class_name}}}\nVISIBILITYBODY{i}\n:::'
            for i, class_name in enumerate(('mf1-priprema', 'mf1-samoprovjera', 'mf1-test-note'))
        )

    def tearDown(self):
        self.temp.cleanup()

    def run_filter(self, target):
        (self.root / 'components/registry.json').write_text(json.dumps(self.registry), encoding='utf8')
        adapter = 'mf1-html-components.lua' if target == 'html5' else 'mf1-typst-author-blocks.lua'
        command = [shutil.which('quarto'), 'pandoc', '-f', 'markdown', '-t', target,
                   '--lua-filter', 'filters/mf1-components.lua', '--lua-filter', 'filters/' + adapter]
        return subprocess.run(command, input=self.source, cwd=self.root,
                              text=True, encoding='utf8', capture_output=True, check=True).stdout

    def test_registry_alone_controls_each_target_and_preceding_heading(self):
        for policy in ([], ['web'], ['pdf'], ['print'], ['web', 'pdf', 'print'], None):
            with self.subTest(policy=policy):
                for name in ('Preparation', 'SelfCheck', 'TestNote'):
                    component = self.registry['components'][name]
                    if policy is None:
                        component.pop('visibility', None)
                    else:
                        component['visibility'] = policy
                elements = Elements(self.run_filter('html5')).by_id
                typst = self.run_filter('typst')
                allowed = ['web', 'pdf', 'print'] if policy is None else policy
                for i in range(3):
                    attrs = elements[f'component-{i}']
                    for target in ('web', 'print'):
                        self.assertEqual('mf1-hidden-' + target in attrs.get('class', '').split(), target not in allowed)
                    self.assertEqual('hidden' in attrs, not ({'web', 'print'} & set(allowed)))
                    self.assertEqual(f'VISIBILITYBODY{i}' in typst, 'pdf' in allowed)
                    self.assertEqual(f'Heading {i}' in typst, 'pdf' in allowed)
                    self.assertIn(f'heading-{i}', elements)  # old incoming links keep an anchor

    def test_invalid_target_is_rejected(self):
        self.registry['components']['Preparation']['visibility'] = ['typo']
        with self.assertRaises(subprocess.CalledProcessError) as failure:
            self.run_filter('html5')
        self.assertIn('Unknown visibility target', failure.exception.stderr)

    def test_quarto_loader_resolves_registry_from_calling_adapter(self):
        (self.root / 'components/registry.json').write_text(json.dumps(self.registry), encoding='utf8')
        (self.root / '_quarto.yml').write_text(
            'project:\n  type: default\nformat: html\nfilters:\n'
            '  - filters/mf1-components.lua\n'
            '  - at: post-quarto\n    path: filters/mf1-html-components.lua\n', encoding='utf8')
        (self.root / 'fixture.qmd').write_text(self.source, encoding='utf8')
        result = subprocess.run([shutil.which('quarto'), 'render', 'fixture.qmd'], cwd=self.root,
                                text=True, encoding='utf8', capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        elements = Elements((self.root / 'fixture.html').read_text(encoding='utf8')).by_id
        self.assertIn('hidden', elements['component-0'])
        self.assertIn('hidden', elements['component-1'])
        self.assertNotIn('hidden', elements['component-2'])


if __name__ == '__main__':
    unittest.main()
