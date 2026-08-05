$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$previousMatplotlibBackend = [Environment]::GetEnvironmentVariable("MPLBACKEND", "Process")

function Resolve-PythonCommand {
    foreach ($candidate in @("python", "python3")) {
        $command = Get-Command $candidate -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -ne $command) {
            return $command.Source
        }
    }
    throw "Nije pronađen Python (pokušani su 'python' i 'python3')."
}

function Assert-NativeSuccess {
    param([Parameter(Mandatory = $true)][string]$Step)

    if ($LASTEXITCODE -ne 0) {
        throw "Korak '$Step' završio je izlaznim kodom $LASTEXITCODE."
    }
}

$pythonCommand = Resolve-PythonCommand

Push-Location $repoRoot
try {
    & $pythonCommand tools/verify_all.py
    Assert-NativeSuccess "provjera numerike"
    & $pythonCommand tools/verify_physics.py
    Assert-NativeSuccess "provjera fizikalnih invarijanti"
    & $pythonCommand tools/qa_audit.py
    Assert-NativeSuccess "audit neovisnosti verifiera"
    & $pythonCommand tools/audit_publication.py
    Assert-NativeSuccess "audit strukture publikacije"
    & $pythonCommand tools/audit_typst.py
    Assert-NativeSuccess "audit nativnih Typst autorskih blokova"
    & $pythonCommand scripts/normalize_public_text.py
    Assert-NativeSuccess "provjera normaliziranog javnog teksta"
    & $pythonCommand scripts/generate_qr_assets.py
    Assert-NativeSuccess "provjera QR resursa"
    & $pythonCommand scripts/generate_exercise_key.py
    Assert-NativeSuccess "provjera ključa zadataka"
    if (Test-Path "tools/validate_cfd_vv.py") {
        & $pythonCommand tools/validate_cfd_vv.py
        Assert-NativeSuccess "provjera CFD V&V podataka"
    }
    $env:MPLBACKEND = "Agg"
    & $pythonCommand tools/execute_notebooks.py --timeout 120
    Assert-NativeSuccess "izvršavanje nastavnih bilježnica"

    # Stariji buildovi kopirali su kanonski Markdown kao javni resurs. Ukloni
    # samo taj točno određeni generirani direktorij prije novoga HTML rendera.
    $siteDir = [IO.Path]::GetFullPath((Join-Path $repoRoot "_site"))
    $stalePublicSourceDir = [IO.Path]::GetFullPath(
        (Join-Path $siteDir "source")
    )
    $siteBoundary = $siteDir.TrimEnd(
        [IO.Path]::DirectorySeparatorChar,
        [IO.Path]::AltDirectorySeparatorChar
    ) + [IO.Path]::DirectorySeparatorChar
    if (-not $stalePublicSourceDir.StartsWith($siteBoundary, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Odbijeno čišćenje izvan _site: $stalePublicSourceDir"
    }
    if (Test-Path -LiteralPath $stalePublicSourceDir -PathType Container) {
        Remove-Item -LiteralPath $stalePublicSourceDir -Recurse -Force
    }

    # Quarto renderi dijele radnu predmemoriju i zato se namjerno izvode redom.
    quarto render
    Assert-NativeSuccess "HTML render"
    quarto render --profile pdf
    Assert-NativeSuccess "Typst PDF render"
    & $pythonCommand tools/audit_pdf.py
    Assert-NativeSuccess "audit nativnog PDF-a"

    $bookDir = Join-Path $repoRoot "_book"
    $pdfSource = Join-Path $bookDir "mehanika-fluida-1.pdf"
    $downloadDir = Join-Path $siteDir "downloads"
    $pdfTarget = Join-Path $downloadDir "mehanika-fluida-1.pdf"

    if (-not (Test-Path -LiteralPath $pdfSource -PathType Leaf)) {
        throw "PDF nije generiran na očekivanoj putanji: $pdfSource"
    }
    New-Item -ItemType Directory -Force -Path $downloadDir | Out-Null
    Copy-Item -LiteralPath $pdfSource -Destination $pdfTarget -Force

    & $pythonCommand -m jupyterlite_core.app build --config=jupyter_lite_config.py --contents notebooks --output-dir _site/jlite
    Assert-NativeSuccess "JupyterLite build"
    & $pythonCommand tools/audit_jupyterlite.py _site/jlite
    Assert-NativeSuccess "audit JupyterLitea"
    & $pythonCommand tools/audit_rendered_site.py _site
    Assert-NativeSuccess "audit renderiranog sitea"
    npm run audit:viewports -- _site
    Assert-NativeSuccess "viewport i WCAG audit"

    Write-Host "HTML, nativni PDF i JupyterLite uspješno su izgrađeni."
}
finally {
    if ($null -eq $previousMatplotlibBackend) {
        Remove-Item Env:MPLBACKEND -ErrorAction SilentlyContinue
    }
    else {
        $env:MPLBACKEND = $previousMatplotlibBackend
    }
    Pop-Location
}
