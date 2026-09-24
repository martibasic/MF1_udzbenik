"""Refuse a push unless its exact, clean HEAD passes the shared publication build."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args, root=ROOT):
    return subprocess.check_output(['git', *args], cwd=root, text=True, encoding='utf-8').strip()


def push_commits(lines, root=ROOT):
    commits = set()
    for line in lines:
        fields = line.split()
        if len(fields) != 4:
            raise ValueError('Invalid pre-push ref input; push stopped.')
        _, local_sha, _, _ = fields
        if set(local_sha) == {'0'}:  # A deletion sends no code to build.
            continue
        commits.add(git('rev-parse', '--verify', local_sha + '^{commit}', root=root))
    return commits


def require_clean_head(commits, root=ROOT):
    head = git('rev-parse', 'HEAD', root=root)
    if commits != {head}:
        raise ValueError('Push stopped: check out the commit being pushed and push one commit tip at a time.')
    if git('status', '--porcelain', '--untracked-files=all', root=root):
        raise ValueError('Push stopped: commit or set aside all changes first. Tests must cover the exact pushed commit.')
    return head


def main():
    commits = push_commits(sys.stdin)
    if not commits:
        return 0
    head = require_clean_head(commits)
    print(f'Pre-push: full publication checks for {head[:12]} (no cached pass).', flush=True)
    environment = os.environ.copy()
    for key in git('rev-parse', '--local-env-vars').splitlines():
        environment.pop(key, None)
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/check_publication.py')],
                            cwd=ROOT, stdin=subprocess.DEVNULL, env=environment)
    if result.returncode:
        print('Push stopped: publication checks failed.', file=sys.stderr)
        return 1
    require_clean_head({head})  # Detect edits or a new commit made during the build.
    print('Pre-push PASS: tested commit is still current and clean.', flush=True)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
