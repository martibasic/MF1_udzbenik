"""One fail-fast publication pipeline for GitHub Actions, local builds and pre-push."""
from importlib import metadata
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def run(command):
    started = time.monotonic()
    print('\n> ' + ' '.join(map(str, command)), flush=True)
    subprocess.run(command, cwd=ROOT, check=True, stdin=subprocess.DEVNULL)
    print(f'PASS ({time.monotonic() - started:.1f}s): {command[1]}', flush=True)


def prepare_environment():
    # Portable project-local tools take precedence without modifying the user's PATH.
    paths = [ROOT / 'tools/tmp/ci/quarto/bin', ROOT / '.tools-ci/node', Path(sys.executable).parent]
    os.environ['PATH'] = os.pathsep.join(str(p) for p in paths if p.is_dir()) + os.pathsep + os.environ['PATH']
    os.environ['MPLBACKEND'] = 'Agg'
    os.environ['PYTHONUTF8'] = '1'
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    os.environ['PYTHONUNBUFFERED'] = '1'
    os.environ['QUARTO_PYTHON'] = sys.executable
    import yaml
    workflow = yaml.safe_load((ROOT / '.github/workflows/publish.yml').read_text(encoding='utf-8'))
    setup = {step.get('uses', '').split('@')[0]: step.get('with', {})
             for step in workflow['jobs']['build']['steps'] if 'uses' in step}
    expected_python = str(setup['actions/setup-python']['python-version'])
    expected_node = str(setup['actions/setup-node']['node-version'])
    expected_quarto = str(setup['quarto-dev/quarto-actions/setup']['version'])
    actual_python = '.'.join(map(str, sys.version_info[:2]))
    errors = []
    if actual_python != expected_python:
        errors.append(f'Python {expected_python} required, found {actual_python}')
    executables = {}
    for name, expected in [('node', expected_node), ('quarto', expected_quarto)]:
        command = shutil.which(name)
        if not command:
            errors.append(f'{name} not found')
            continue
        actual = subprocess.check_output([command, '--version'], text=True).strip().lstrip('v')
        if (actual.split('.')[0] if name == 'node' else actual) != expected:
            errors.append(f'{name} {expected} required, found {actual}')
        executables[name] = command
        print(f'{name}: {actual}', flush=True)
    for line in (ROOT / 'requirements.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        name, expected = line.split('==')
        try:
            actual = metadata.version(name)
        except metadata.PackageNotFoundError:
            actual = 'missing'
        if actual != expected:
            errors.append(f'{name}=={expected} required, found {actual}')
    if errors:
        raise ValueError('CI environment mismatch:\n' + '\n'.join(errors)
                         + '\nSee docs/lokalni-ci.md; no checks were skipped.')
    executables['npm'] = shutil.which('npm')
    if not executables['npm']:
        raise ValueError('npm not found')
    print(f'Python: {sys.version.split()[0]}; all pinned Python dependencies match.', flush=True)
    return executables


def main():
    started = time.monotonic()
    commands = prepare_environment()
    py, node = sys.executable, commands['node']
    # Always install from the committed lockfile, also in the local pre-push hook.
    run([commands['npm'], 'ci', '--ignore-scripts'])
    steps = [
        [py, 'tools/test_pre_push.py'],
        [py, 'tools/verify_all.py'],
        [py, 'tools/test_book_model.py'],
        [py, 'tools/test_render_workspace.py'],
        [py, 'tools/test_render_process.py'],
        [py, 'tools/test_component_visibility.py'],
        [py, 'tools/audit_architecture.py'],
        [py, 'tools/audit_publication.py'],
        [py, 'tools/audit_typst.py'],
        [py, 'tools/audit_sketch_design.py'],
        [node, 'tools/audit_print_layouts.mjs'],
        [py, 'scripts/normalize_public_text.py'],
        [py, 'scripts/generate_qr_assets.py'],
        [py, 'scripts/generate_exercise_key.py'],
        [py, 'tools/validate_cfd_vv.py'],
        [py, 'tools/test_legacy_notebook_generator.py'],
        [py, 'tools/execute_notebooks.py', '--timeout', '120'],
        [py, 'tools/test_interactive_labs.py'],
        [py, 'scripts/build_book.py', '--render', 'all'],
        [py, 'tools/audit_pdf.py'],
        [py, 'tools/audit_pdf_layout.py'],
    ]
    for command in steps:
        run(command)
    download = ROOT / '_site/downloads/mehanika-fluida-1.pdf'
    download.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / '_book/mehanika-fluida-1.pdf', download)
    for command in [
        [py, '-m', 'jupyterlite_core.app', 'build', '--config=jupyter_lite_config.py',
         '--contents', 'notebooks', '--output-dir', '_site/jlite'],
        [py, 'tools/audit_jupyterlite.py', '_site/jlite'],
        [node, 'tools/audit_interactive_labs.mjs', '_site'],
        [py, 'tools/audit_rendered_site.py', '_site'],
        [py, 'tools/audit_rendered_model.py', '_site'],
        [node, 'tools/audit_print_site.mjs', '_site'],
        [node, 'tools/audit_viewports.mjs', '_site'],
    ]:
        run(command)
    for name in ['_site/index.html', '_site/downloads/mehanika-fluida-1.pdf', '_site/jlite/lab/index.html']:
        if not (ROOT / name).is_file() or (ROOT / name).stat().st_size == 0:
            raise ValueError(f'Missing publication artifact: {name}')
    print(f'\nPublication checks PASS ({time.monotonic() - started:.0f} s).', flush=True)


if __name__ == '__main__':
    # The same convenience entry point works from a normal terminal and the hook.
    venv = ROOT / '.venv-ci' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    if venv.is_file() and Path(sys.prefix).resolve() != (ROOT / '.venv-ci').resolve():
        raise SystemExit(subprocess.call([str(venv), str(Path(__file__).resolve()), *sys.argv[1:]]))
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'Publication checks FAILED: {error}', file=sys.stderr)
        raise SystemExit(1)
