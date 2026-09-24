"""Exercise the renderer watchdog with real child processes."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from render_process import run_render


class RenderProcessTests(unittest.TestCase):
    def run_child(self, code, directory, **kwargs):
        run_render([sys.executable, '-u', '-c', code], cwd=directory, env=None,
                   log_path=Path(directory) / 'render.log', heartbeat=0.1, **kwargs)

    def test_success_keeps_partial_lines_and_utf8(self):
        with tempfile.TemporaryDirectory() as directory:
            output = io.StringIO()
            with redirect_stdout(output):
                self.run_child("import sys; sys.stdout.buffer.write('Čekanje bez novog retka'.encode('utf8'))", directory)
            self.assertIn('Čekanje bez novog retka', output.getvalue())
            self.assertIn('Render PASS', output.getvalue())
            self.assertEqual((Path(directory) / 'render.log').read_text(encoding='utf8'), 'Čekanje bez novog retka')

    def test_failure_is_not_reported_as_pass(self):
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(io.StringIO()) as output:
            with self.assertRaises(subprocess.CalledProcessError) as caught:
                self.run_child("print('compile error'); raise SystemExit(7)", directory)
            self.assertEqual(caught.exception.returncode, 7)
            self.assertNotIn('Render PASS', output.getvalue())
            self.assertIn('compile error', (Path(directory) / 'render.log').read_text())

    def test_timeout_stops_child_and_grandchild(self):
        with tempfile.TemporaryDirectory() as directory, redirect_stdout(io.StringIO()) as output:
            # A compiler grandchild must not survive to overwrite outputs later.
            child = "import time; from pathlib import Path; time.sleep(2); Path('orphan.txt').write_text('bad')"
            code = ("import subprocess, sys, time; "
                    f"subprocess.Popen([sys.executable, '-c', {child!r}]); "
                    "print('compiler started', flush=True); time.sleep(30)")
            started = time.monotonic()
            with self.assertRaises(subprocess.TimeoutExpired):
                self.run_child(code, directory, timeout=0.8)
            self.assertLess(time.monotonic() - started, 5)
            time.sleep(2.1)
            self.assertFalse((Path(directory) / 'orphan.txt').exists())
            self.assertIn('compiler started', (Path(directory) / 'render.log').read_text())
            self.assertIn('Render RUNNING', output.getvalue())


if __name__ == '__main__':
    unittest.main()
