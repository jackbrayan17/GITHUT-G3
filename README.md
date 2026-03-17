# Collaborative ML Project

This repository is prepared for a team working on machine learning code in parallel, with support for:

- per-member Git branches
- `pre-commit` checks before each commit
- Git LFS for datasets and model artifacts larger than 50 MB
- a basic Python project layout for models, experiments, and tests

## Repository layout

```text
.
|-- .github/
|-- data/
|   |-- processed/
|   |-- raw/
|   `-- README.md
|-- notebooks/
|-- scripts/
|-- src/
|   `-- models/
|-- tests/
|-- .gitattributes
|-- .gitignore
|-- .pre-commit-config.yaml
|-- pyproject.toml
`-- requirements-dev.txt
```

## First-time local setup

Run the bootstrap script from PowerShell:

```powershell
.\scripts\setup.ps1
```

That script will:

- install Git LFS locally for this machine
- install development dependencies
- install the `pre-commit` Git hooks

## Team workflow

1. The project lead creates the GitHub repository and pushes `main`.
2. The lead invites collaborators from the repository settings.
3. Each collaborator creates a personal branch:

```powershell
.\scripts\create-member-branch.ps1 -MemberName jack
```

This creates a branch like `team/jack`.

4. Each member works only on their branch and opens a pull request into `main`.
5. Code review happens before merge.

## GitHub commands

After creating an empty GitHub repository, connect this local repository:

```powershell
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

To create and publish a member branch:

```powershell
git checkout team/jack
git push -u origin team/jack
```

## Large datasets

Any file in these paths is tracked by Git LFS:

- `data/raw/`
- `models/`
- `artifacts/`
- common binary dataset/model formats such as `.csv`, `.parquet`, `.pkl`, `.joblib`, `.pt`

If a dataset is larger than 50 MB, place it in `data/raw/`.

## Pre-commit checks

The configured hooks run:

- whitespace cleanup
- end-of-file fixes
- YAML validation
- large-file detection
- Ruff linting
- Ruff formatting

Run the hooks manually:

```powershell
pre-commit run --all-files
```

## Minimal development loop

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pre-commit install
pytest
```
