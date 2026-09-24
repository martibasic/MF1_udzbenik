"""Bounded renderer processes with live logs and process-tree cleanup."""
import os
from pathlib import Path
import signal
import subprocess
import time


def stop_process_tree(process):
    if os.name == 'nt':
        subprocess.run(['taskkill', '/PID', str(process.pid), '/T', '/F'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    process.wait()


def run_render(command, *, cwd, env, log_path, timeout=600, heartbeat=30):
    """Stream output even without newlines; stop the whole tree on timeout.

    A regular log file avoids pipe backpressure and retains the last renderer
    messages if the compiler stalls. The caller preserves the failed workspace.
    """
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    print(f'Render START: {log_path.stem}; limit={timeout}s; log={log_path}', flush=True)
    with log_path.open('wb') as output, log_path.open('rb') as reader:
        process = subprocess.Popen(command, cwd=cwd, env=env, stdin=subprocess.DEVNULL,
                                   stdout=output, stderr=subprocess.STDOUT,
                                   start_new_session=os.name != 'nt',
                                   creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0)
        # An incremental decoder keeps multibyte Croatian text intact across reads.
        import codecs
        decoder = codecs.getincrementaldecoder('utf-8')(errors='replace')
        try:
            while True:
                remaining = timeout - (time.monotonic() - started)
                if remaining <= 0:
                    raise subprocess.TimeoutExpired(command, timeout)
                try:
                    process.wait(timeout=min(heartbeat, remaining))
                except subprocess.TimeoutExpired:
                    print(decoder.decode(reader.read()), end='', flush=True)
                    print(f'\nRender RUNNING: {log_path.stem} ({time.monotonic()-started:.0f}s)', flush=True)
                    continue
                print(decoder.decode(reader.read(), final=True), end='', flush=True)
                if process.returncode:
                    raise subprocess.CalledProcessError(process.returncode, command)
                print(f'Render PASS: {log_path.stem} ({time.monotonic()-started:.1f}s)', flush=True)
                return
        except BaseException:
            stop_process_tree(process)
            print(decoder.decode(reader.read()), end='', flush=True)
            raise
