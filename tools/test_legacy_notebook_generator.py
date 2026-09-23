"""Integration checks that legacy templates cannot overwrite teaching notebooks."""

from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "scripts" / "generiraj_notebooke.py"


def snapshot():
    return {
        p.name: hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (ROOT / "notebooks").glob("*.ipynb")
    }


class LegacyExportSafety(unittest.TestCase):
    def setUp(self):
        self.before = snapshot()

    def tearDown(self):
        self.assertEqual(self.before, snapshot(), "Teaching notebooks were modified")

    def run_generator(self, *args):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(GENERATOR), *map(str, args)],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
        )

    def test_default_invocation_does_not_write(self):
        result = self.run_generator()
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("--archive-output", result.stderr)

    def test_publication_destinations_are_rejected(self):
        for relative in ("notebooks", "notebooks/new-archive", "source", "_site", "."):
            with self.subTest(destination=relative):
                result = self.run_generator("--archive-output", ROOT / relative)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertIn("Arhivski predlošci", result.stderr)

    def test_existing_archive_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            sentinel = Path(folder) / "u01_hidraulicna_presa.ipynb"
            sentinel.write_bytes(b"keep existing work")
            result = self.run_generator("--archive-output", folder)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertEqual(sentinel.read_bytes(), b"keep existing work")
            self.assertEqual(list(Path(folder).iterdir()), [sentinel])

    def test_explicit_separate_export_creates_valid_archive(self):
        scratch = ROOT / "tools" / "tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder:
            destination = Path(folder) / "archive"
            result = self.run_generator("--archive-output", destination)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            files = list(destination.glob("*.ipynb"))
            self.assertEqual(len(files), 13)
            for path in files:
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(notebook["nbformat"], 4)
                self.assertTrue(notebook["cells"])
            # A second invocation must refuse even its own previous output.
            result = self.run_generator("--archive-output", destination)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
