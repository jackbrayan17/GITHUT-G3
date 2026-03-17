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

## Where files are stored

Project root:

```text
C:\Users\Jack Brayan\Documents\New project
```

Important locations:

- `data/raw/` for original datasets
- `data/processed/` for cleaned or derived datasets
- `src/models/` for model code
- `tests/` for test files
- `scripts/setup.ps1` for local environment setup
- `scripts/create-member-branch.ps1` for creating a team branch

## How to run the project

Open PowerShell in the project folder and run:

```powershell
cd "C:\Users\Jack Brayan\Documents\New project"
.\scripts\setup.ps1
.\.venv\Scripts\Activate.ps1
pytest
pre-commit run --all-files
```

What these commands do:

- `setup.ps1` installs Git LFS, Python development packages, and Git hooks
- `Activate.ps1` activates the local virtual environment
- `pytest` runs the test suite
- `pre-commit run --all-files` runs formatting and lint checks

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

## Full Git workflow

Use all commands below from:

```powershell
cd "C:\Users\Jack Brayan\Documents\New project"
```

### 1. Check repository state

```powershell
git status
git branch
git branch -a
git remote -v
```

### 2. Switch branches

Switch to `main`:

```powershell
git switch main
```

Switch to your personal branch:

```powershell
git switch team/jack
```

If the branch does not exist yet:

```powershell
git switch -c team/jack
```

If the branch exists on GitHub but not locally:

```powershell
git fetch origin
git switch --track origin/team/jack
```

### 3. Create a branch for a team member

Use the helper script:

```powershell
.\scripts\create-member-branch.ps1 -MemberName jack
```

If Git says the branch already exists:

```powershell
git switch team/jack
```

### 4. Get the latest changes

Update `main`:

```powershell
git switch main
git pull origin main
```

Update your own branch:

```powershell
git switch team/jack
git pull origin team/jack
```

Bring the latest `main` into your branch before opening a pull request:

```powershell
git switch main
git pull origin main
git switch team/jack
git merge main
```

### 5. Add, commit, and push work

Check changes:

```powershell
git status
```

Stage all changes:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Add regression model"
```

If `pre-commit` modifies files during commit:

```powershell
git add .
git commit -m "Add regression model"
```

First push of a branch:

```powershell
git push -u origin team/jack
```

Later pushes:

```powershell
git push
```

### 6. Create and publish the GitHub repository

After creating an empty repository on GitHub:

```powershell
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

Publish a member branch:

```powershell
git push -u origin team/jack
```

### 7. Work with large datasets using Git LFS

Put the dataset in:

```text
data/raw/
```

Then add and commit it:

```powershell
git add .gitattributes
git add data/raw/your-dataset.csv
git commit -m "Add dataset with Git LFS"
git push
```

Check tracked LFS files:

```powershell
git lfs ls-files
```

### 8. Simulated team process

Project lead:

```powershell
git init
git branch -m main
git remote add origin https://github.com/USERNAME/REPO.git
git add .
git commit -m "Initial project setup"
git push -u origin main
```

Jack:

```powershell
git switch -c team/jack
git add .
git commit -m "Implement regression model"
git push -u origin team/jack
```

Mary:

```powershell
git switch main
git pull origin main
git switch -c team/mary
git add .
git commit -m "Add preprocessing pipeline"
git push -u origin team/mary
```

Jack updates before opening a pull request:

```powershell
git switch main
git pull origin main
git switch team/jack
git merge main
git push
```

After a branch is merged:

```powershell
git switch main
git pull origin main
git branch -d team/jack
git push origin --delete team/jack
```

### 9. Useful daily Git commands

```powershell
git status
git log --oneline --graph --all
git diff
git diff --staged
git stash
git stash pop
```

### 10. If you worked on the wrong branch

Save your changes temporarily:

```powershell
git stash
```

Switch to the correct branch and restore:

```powershell
git switch team/jack
git stash pop
```

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
