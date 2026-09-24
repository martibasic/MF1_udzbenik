$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ciPython = Join-Path $repoRoot ".venv-ci/Scripts/python.exe"
if (-not (Test-Path -LiteralPath $ciPython)) { $ciPython = "python" }
Push-Location $repoRoot
try {
    & $ciPython scripts/check_publication.py
    if ($LASTEXITCODE -ne 0) { throw "Objavni CI nije prošao (izlazni kod $LASTEXITCODE)." }
}
finally { Pop-Location }
