"""Enable the versioned pre-push hook for this clone, without changing global Git config."""
from pathlib import Path
import stat
import subprocess

root = Path(__file__).resolve().parents[1]
current = subprocess.run(['git', 'config', '--get', 'core.hooksPath'], cwd=root,
                         text=True, capture_output=True).stdout.strip()
if current and current != '.githooks':
    raise SystemExit(f'Existing hooksPath {current!r}; integrate its hooks before changing this setting.')
hook = root / '.githooks/pre-push'
hook.chmod(hook.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
subprocess.run(['git', 'config', '--local', 'core.hooksPath', '.githooks'], cwd=root, check=True)
print('Enabled .githooks/pre-push for this clone. Every code push requires the full publication build.')
