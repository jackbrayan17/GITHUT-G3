Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "Installing Git LFS hooks..."
git lfs install

Write-Host "Creating virtual environment if missing..."
if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

Write-Host "Installing development dependencies..."
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements-dev.txt

Write-Host "Installing pre-commit hooks..."
& ".\.venv\Scripts\pre-commit.exe" install

Write-Host "Setup complete."
