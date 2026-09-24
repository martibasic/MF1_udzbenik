"""Exercise the actual hook against disposable local Git repositories; no network."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from pre_push import push_commits, require_clean_head


class PrePushTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='mf1-hook-')
        self.root = Path(self.temp.name) / 'working copy'
        self.remote = Path(self.temp.name) / 'remote.git'
        self.root.mkdir()
        self.env = os.environ.copy()
        # Git hooks can inherit these; the tests must never operate on the real repo.
        for key in list(self.env):
            if key.startswith('GIT_'):
                self.env.pop(key)
        self.env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + self.env['PATH']
        self.git('init', '-q')
        self.git('config', 'user.name', 'Hook test')
        self.git('config', 'user.email', 'hook-test@example.invalid')
        self.git('config', 'core.hooksPath', '.githooks')
        (self.root / '.githooks').mkdir()
        (self.root / 'scripts').mkdir()
        shutil.copy2(ROOT / '.githooks/pre-push', self.root / '.githooks/pre-push')
        (self.root / '.githooks/pre-push').chmod(0o755)
        shutil.copy2(ROOT / 'scripts/pre_push.py', self.root / 'scripts/pre_push.py')
        (self.root / '.gitignore').write_text('called\n__pycache__/\n', encoding='utf-8')
        self.write_runner(0)
        self.commit()
        subprocess.run(['git', 'init', '--bare', '-q', str(self.remote)], env=self.env, check=True)

    def tearDown(self):
        # TemporaryDirectory uses only the exact path it created.
        self.temp.cleanup()

    def git(self, *args, check=True):
        return subprocess.run(['git', *args], cwd=self.root, env=self.env, check=check,
                              capture_output=True, text=True, encoding='utf-8')

    def write_runner(self, exit_code, extra=''):
        (self.root / 'scripts/check_publication.py').write_text(
            "from pathlib import Path\nimport sys\n"
            "p=Path('called'); p.write_text(p.read_text()+'x' if p.exists() else 'x')\n"
            + extra + f'\nsys.exit({exit_code})\n', encoding='utf-8')

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')

    def push(self):
        return self.git('push', str(self.remote), 'HEAD:refs/heads/test', check=False)

    def test_success_repeats_full_checks_on_next_push(self):
        self.assertEqual(self.push().returncode, 0)
        (self.root / 'next').write_text('next')
        self.commit()
        self.assertEqual(self.push().returncode, 0)
        self.assertEqual((self.root / 'called').read_text(), 'xx')

    def test_failed_check_blocks_real_git_push(self):
        self.write_runner(3)
        self.commit()
        result = self.push()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('publication checks failed', result.stderr)
        refs = self.git('ls-remote', str(self.remote)).stdout
        self.assertEqual(refs, '')

    def test_untracked_and_staged_changes_block_before_tests(self):
        (self.root / 'uncommitted').write_text('dirty')
        self.assertNotEqual(self.push().returncode, 0)
        self.git('add', 'uncommitted')
        self.assertNotEqual(self.push().returncode, 0)
        self.assertFalse((self.root / 'called').exists())

    def test_edit_during_build_blocks_push(self):
        self.write_runner(0, "Path('changed-during-build').write_text('changed')\n")
        self.commit()
        self.assertNotEqual(self.push().returncode, 0)
        self.assertTrue((self.root / 'called').exists())

    def test_another_tip_cannot_use_current_worktree(self):
        old = self.git('rev-parse', 'HEAD').stdout.strip()
        (self.root / 'next').write_text('next')
        self.commit()
        with self.assertRaises(ValueError):
            require_clean_head({old}, root=self.root)
        result = self.git('push', str(self.remote), old + ':refs/heads/old', check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / 'called').exists())

    def test_tags_deletion_and_malformed_input(self):
        head = self.git('rev-parse', 'HEAD').stdout.strip()
        self.git('tag', '-am', 'tag fixture', 'v-test')
        tag = self.git('rev-parse', 'v-test').stdout.strip()
        self.assertEqual(push_commits([f'refs/tags/v-test {tag} refs/tags/v-test {"0"*40}'], root=self.root), {head})
        self.assertEqual(push_commits([f'(delete) {"0"*40} refs/heads/old {head}'], root=self.root), set())
        with self.assertRaises(ValueError):
            push_commits(['malformed'], root=self.root)


if __name__ == '__main__':
    unittest.main(verbosity=2)
