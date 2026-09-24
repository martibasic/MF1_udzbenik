"""Build isolation, failed-render preservation, and concurrent-build regressions."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_workspace import build_lock, render


class RenderWorkspaceTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT / 'tools/tmp'
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='render-test-', dir=parent)
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.put('.gitignore', 'tools/tmp/\n.quarto/\n_site/\n_book/\n')
        self.put('source/chapter.md', 'Saved work, including uncommitted changes.')
        self.put('.quarto/preview-state', 'preview must keep this cache')
        self.put('_site/index.html', 'previous successful web')
        self.put('_site/jlite/keep.txt', 'separately built JupyterLite')
        self.put('_site/downloads/book.pdf', 'separately built PDF download')
        self.original_run = subprocess.run
        self.workspaces = []
        self.calls = 0

    def tearDown(self):
        self.temp.cleanup()

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf8')

    def fake_quarto(self, command, **kwargs):
        if command[0] != 'test-quarto':
            return self.original_run(command, **kwargs)
        work = Path(kwargs['cwd'])
        self.workspaces.append(work)
        self.calls += 1
        self.assertNotEqual(work, self.root)
        self.assertTrue(work.is_relative_to(self.root / 'tools/tmp'))
        self.assertEqual((work / 'source/chapter.md').read_text(), 'Saved work, including uncommitted changes.')
        self.assertFalse((work / '.quarto/preview-state').exists())
        self.assertEqual(kwargs['env']['TYPST_IGNORE_SYSTEM_FONTS'], 'true')
        self.assertEqual(kwargs['env']['TYPST_IGNORE_EMBEDDED_FONTS'], 'false')
        self.assertNotIn('TYPST_FONT_PATHS', kwargs['env'])
        (work / '.quarto').mkdir(exist_ok=True)
        (work / '.quarto/render-state').write_text('isolated renderer')
        output = work / ('_book' if 'typst' in command else '_site')
        output.mkdir(exist_ok=True)
        (output / ('book.pdf' if 'typst' in command else 'index.html')).write_text('new successful output')
        return subprocess.CompletedProcess(command, 0)

    def test_success_keeps_preview_cache_and_separate_artifacts(self):
        with patch('render_workspace.run_render', side_effect=self.fake_quarto):
            render(self.root, 'all', 'test-quarto')
        self.assertEqual(self.calls, 3)
        self.assertEqual(len(set(self.workspaces)), 1)
        self.assertFalse(self.workspaces[0].exists())
        self.assertEqual((self.root / '.quarto/preview-state').read_text(), 'preview must keep this cache')
        self.assertFalse((self.root / '.quarto/render-state').exists())
        self.assertEqual((self.root / '_site/index.html').read_text(), 'new successful output')
        self.assertEqual((self.root / '_book/book.pdf').read_text(), 'new successful output')
        self.assertTrue((self.root / '_site/jlite/keep.txt').exists())
        self.assertTrue((self.root / '_site/downloads/book.pdf').exists())

    def test_failed_second_render_preserves_previous_outputs(self):
        def fail_second(command, **kwargs):
            result = self.fake_quarto(command, **kwargs)
            if command[0] == 'test-quarto' and self.calls == 2:
                raise subprocess.CalledProcessError(1, command)
            return result
        with patch('render_workspace.run_render', side_effect=fail_second):
            with self.assertRaisesRegex(ValueError, 'Logs and workspace preserved'):
                render(self.root, 'web', 'test-quarto')
        self.assertEqual((self.root / '_site/index.html').read_text(), 'previous successful web')
        self.assertFalse(self.workspaces[0].exists())
        saved = list((self.root / 'tools/tmp/render-diagnostics').glob('failed-*'))
        self.assertEqual(len(saved), 1)
        self.assertEqual((saved[0] / 'source/chapter.md').read_text(), 'Saved work, including uncommitted changes.')

    def test_timeout_preserves_previous_outputs_and_diagnostic_workspace(self):
        def timeout(command, **kwargs):
            self.fake_quarto(command, **kwargs)
            raise subprocess.TimeoutExpired(command, 600)
        with patch('render_workspace.run_render', side_effect=timeout):
            with self.assertRaisesRegex(ValueError, 'timed out'):
                render(self.root, 'pdf', 'test-quarto')
        self.assertFalse((self.root / '_book').exists())
        self.assertEqual((self.root / '_site/index.html').read_text(), 'previous successful web')
        self.assertTrue(list((self.root / 'tools/tmp/render-diagnostics').glob('failed-*/_book/book.pdf')))
        self.assertFalse(self.workspaces[0].exists())

    def test_edit_during_render_prevents_publishing_mixed_versions(self):
        def edit(command, **kwargs):
            result = self.fake_quarto(command, **kwargs)
            if command[0] == 'test-quarto':
                self.put('source/chapter.md', 'New edit while render is running')
            return result
        with patch('render_workspace.run_render', side_effect=edit):
            with self.assertRaisesRegex(ValueError, 'Inputs changed during rendering'):
                render(self.root, 'pdf', 'test-quarto')
        self.assertFalse((self.root / '_book').exists())
        self.assertEqual((self.root / 'source/chapter.md').read_text(), 'New edit while render is running')

    def test_second_process_is_blocked_then_lock_is_released(self):
        code = (f'import sys; from pathlib import Path; sys.path.insert(0, {str(ROOT / "scripts")!r}); '
                'from render_workspace import build_lock\n'
                f'with build_lock(Path({str(self.root)!r})):\n print("acquired")\n')
        with build_lock(self.root):
            blocked = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
        self.assertNotEqual(blocked.returncode, 0)
        self.assertIn('Another book build is running', blocked.stderr)
        released = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True)
        self.assertEqual(released.returncode, 0, released.stderr)


if __name__ == '__main__':
    unittest.main()
