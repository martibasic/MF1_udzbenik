"""Render saved project inputs away from Quarto preview's working cache."""
from contextlib import contextmanager
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from render_process import run_render


@contextmanager
def build_lock(root):
    """An OS lock is released on failure/termination; no stale PID lock files."""
    path = root / 'tools/tmp/render.lock'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+b') as handle:
        try:
            if os.fstat(handle.fileno()).st_size == 0:
                handle.write(b'0')
                handle.flush()
            handle.seek(0)
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise ValueError('Another book build is running. Wait for it to finish; preview may remain open.') from exc
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == 'nt':
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def input_files(root):
    """Include saved, uncommitted work, never caches or installed dependencies."""
    listing = subprocess.check_output(
        ['git', 'ls-files', '-co', '--exclude-standard', '-z'], cwd=root
    ).decode('utf8').split('\0')
    excluded = {'.git', '.quarto', '_site', '_book', '_freeze', 'node_modules', '__pycache__'}
    files = []
    for name in sorted(set(listing) - {''}):
        relative = Path(name)
        if any(part in excluded for part in relative.parts) or name.startswith('tools/tmp/'):
            continue
        source = root / relative
        if source.is_symlink() or not source.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Render input must be a regular project file: {name}')
        if source.is_file():
            files.append(name)
    return files


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@contextmanager
def snapshot(root):
    root = root.resolve()
    parent = root / 'tools/tmp'
    if not parent.resolve().is_relative_to(root):
        raise ValueError('Temporary build directory escapes the project.')
    parent.mkdir(parents=True, exist_ok=True)
    # Staying under the project also lets Node resolve its installed packages
    # from the ancestor node_modules without copying or linking dependencies.
    work = Path(tempfile.mkdtemp(prefix='render-', dir=parent)).resolve()
    assert work.is_relative_to(parent.resolve()) and work != parent.resolve()
    try:
        hashes = {}
        for name in input_files(root):
            source, target = root / name, work / name
            before = digest(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            if digest(target) != before or digest(source) != before:
                raise ValueError(f'Input changed while taking build snapshot: {name}. Run the build again.')
            hashes[name] = before
        yield work, hashes
    finally:
        # Only remove the exact workspace created above, never an inferred
        # output directory or a link into the user's project.
        if not work.is_symlink() and work.resolve().is_relative_to(parent.resolve()):
            shutil.rmtree(work)


def verify_inputs(root, hashes):
    current = input_files(root)
    changed = set(current) ^ set(hashes)
    changed.update(name for name in set(current) & set(hashes) if digest(root / name) != hashes[name])
    if changed:
        raise ValueError('Inputs changed during rendering; outputs were not published. Run again: '
                         + ', '.join(sorted(changed)[:8]))


def publish_outputs(root, work, names):
    """Copy completed render files, preserving JupyterLite and PDF downloads.

    Individual files are replaced atomically so preview never reads a partly
    written HTML/CSS file. This is not a directory-wide atomic deployment.
    """
    for name in names:
        source, destination = work / name, root / name
        if not source.is_dir():
            raise ValueError(f'Render did not produce {name}; existing outputs preserved.')
        if not destination.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Output escapes the project: {destination}')
    for name in names:
        for source in sorted((work / name).rglob('*')):
            if not source.is_file():
                continue
            target = root / name / source.relative_to(work / name)
            if not target.resolve().is_relative_to((root / name).resolve()):
                raise ValueError(f'Output file escapes its directory: {target}')
            target.parent.mkdir(parents=True, exist_ok=True)
            descriptor, temporary = tempfile.mkstemp(prefix='.mf1-', dir=target.parent)
            try:
                os.close(descriptor)
                shutil.copy2(source, temporary)
                os.replace(temporary, target)
            finally:
                Path(temporary).unlink(missing_ok=True)


def render(root, target, quarto):
    with snapshot(root) as (work, hashes):
        print(f'Isolated Quarto build: {work}', flush=True)
        diagnostics = root / 'tools/tmp/render-diagnostics'
        environment = os.environ.copy()
        # Embedded Libertinus/NewCM, bundled Quarto icons and the repository's
        # Liberation Sans are identical on a developer PC and a clean runner.
        environment['TYPST_IGNORE_SYSTEM_FONTS'] = 'true'
        environment['TYPST_IGNORE_EMBEDDED_FONTS'] = 'false'
        environment.pop('TYPST_FONT_PATHS', None)
        stages = []
        if target in ('web', 'all'):
            stages.extend([
                ('web', ['render', '--to', 'html']),
                ('print', ['render', 'chapters/za_ispis.qmd', '--profile', 'print', '--to', 'html', '--no-clean']),
            ])
        if target in ('pdf', 'all'):
            stages.append(('pdf', ['render', '--profile', 'pdf', '--to', 'typst', '-M', 'keep-typ:true']))
        try:
            for name, arguments in stages:
                run_render([quarto, *arguments], cwd=work, env=environment,
                           log_path=diagnostics / f'{name}.log')
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            diagnostics.mkdir(parents=True, exist_ok=True)
            saved = Path(tempfile.mkdtemp(prefix='failed-', dir=diagnostics))
            shutil.copytree(work, saved, dirs_exist_ok=True)
            raise ValueError(f'Render failed: {exc}. Logs and workspace preserved in {diagnostics}; '
                             'previous published outputs were not changed.') from exc
        verify_inputs(root, hashes)
        outputs = ['_site', '_book'] if target == 'all' else ['_site' if target == 'web' else '_book']
        publish_outputs(root, work, outputs)
        print('Published completed render: ' + ', '.join(outputs), flush=True)
