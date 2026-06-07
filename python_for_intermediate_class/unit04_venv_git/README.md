# Unit 04: Virtual Environments and Git

This unit teaches two essential habits for intermediate Python projects:

1. **Virtual environments (`venv`)** keep each project isolated so packages from one project do not break another project.
2. **Git** records project history so you can save progress, compare changes, and safely experiment.

By the end of this unit, students will be able to create a project folder, set up a Python virtual environment, install packages, save dependencies, initialize Git, commit changes, and use a practical command cheat sheet.

---

## Learning Goals

After completing this unit, you should be able to:

- explain why Python projects need virtual environments;
- create a `.venv` folder with Python's built-in `venv` module;
- activate and deactivate a virtual environment on Windows, macOS, and Linux;
- install packages with `pip` inside the active environment;
- create and use a `requirements.txt` file;
- explain what Git tracks and why commits are useful;
- initialize a Git repository;
- create a `.gitignore` file that protects generated files and virtual environments;
- use `git status`, `git add`, `git commit`, `git log`, and `git diff`;
- follow a repeatable workflow for everyday Python project work.

---

## Part 1: What Is a Virtual Environment?

A **virtual environment** is a private Python workspace for one project. It contains its own Python executable and installed packages.

Without a virtual environment, packages may be installed globally on your computer. That can cause problems:

- Project A may need an older version of a package.
- Project B may need a newer version of the same package.
- Installing or upgrading a package for one project may accidentally break another project.
- It becomes harder to share the project because nobody knows which packages are required.

A virtual environment solves this by keeping project dependencies separate.

### Recommended Folder Name

Use this folder name for the environment:

```text
.venv
```

The dot at the beginning means it is a hidden-style project support folder. It should stay inside the project but should **not** be committed to Git.

---

## Part 2: What Is Git?

**Git** is a version control system. It saves snapshots of your project over time.

A Git snapshot is called a **commit**. Each commit records:

- which files changed;
- what the changes were;
- when the change happened;
- who made the change;
- a message explaining the reason for the change.

Git helps you answer questions like:

- What changed since yesterday?
- Which files are ready to save?
- Can I undo an experiment?
- What did I change before submitting my project?
- How can I share my work on GitHub later?

---

## Part 3: Suggested Project Structure

For this lesson, create a small practice project with this structure:

```text
venv_git_practice/
├── .gitignore
├── README.md
├── requirements.txt
└── app.py
```

After creating a virtual environment, your folder may also contain `.venv/`:

```text
venv_git_practice/
├── .venv/
├── .gitignore
├── README.md
├── requirements.txt
└── app.py
```

The `.venv/` folder should exist on your computer, but Git should ignore it.

---

## Part 4: Step-by-Step Virtual Environment Setup

### Step 1: Open a Terminal

Open the terminal in VS Code or use your system terminal.

In VS Code:

1. Open your project folder.
2. Select **Terminal** from the top menu.
3. Select **New Terminal**.

### Step 2: Create a Project Folder

```bash
mkdir venv_git_practice
cd venv_git_practice
```

### Step 3: Check Your Python Version

On Windows, try:

```bash
python --version
```

On macOS or Linux, try:

```bash
python3 --version
```

You should see a Python 3 version.

### Step 4: Create the Virtual Environment

On Windows, try:

```bash
python -m venv .venv
```

On macOS or Linux, try:

```bash
python3 -m venv .venv
```

This creates a `.venv` folder inside the project.

### Step 5: Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```bat
.venv\Scripts\activate.bat
```

#### macOS or Linux

```bash
source .venv/bin/activate
```

When activation works, your terminal prompt usually starts with `(.venv)`.

Example:

```text
(.venv) student@computer venv_git_practice %
```

### Step 6: Upgrade `pip`

Run this after activating the environment:

```bash
python -m pip install --upgrade pip
```

Using `python -m pip` is a good habit because it connects `pip` to the currently active Python interpreter.

### Step 7: Install a Package

Install the `requests` package as a practice dependency:

```bash
python -m pip install requests
```

### Step 8: Check Installed Packages

```bash
python -m pip list
```

You should see `requests` and its helper packages.

### Step 9: Save Dependencies

Create a `requirements.txt` file:

```bash
python -m pip freeze > requirements.txt
```

This file records the exact package versions installed in the environment.

### Step 10: Reinstall Dependencies Later

If another student, teacher, or computer needs the same packages, they can run:

```bash
python -m pip install -r requirements.txt
```

### Step 11: Deactivate the Environment

When finished working, run:

```bash
deactivate
```

The `(.venv)` label should disappear from the terminal prompt.

---

## Part 5: Step-by-Step Git Setup

### Step 1: Check Git Installation

```bash
git --version
```

If Git is installed, the terminal prints a version number.

### Step 2: Configure Your Name and Email

Do this once on your computer:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check your settings:

```bash
git config --global --list
```

### Step 3: Initialize a Git Repository

Inside the `venv_git_practice` folder, run:

```bash
git init
```

This creates a hidden `.git/` folder. The `.git/` folder stores project history.

### Step 4: Create a `.gitignore` File

Create a `.gitignore` file:

```bash
touch .gitignore
```

On Windows Command Prompt, if `touch` does not work, use:

```bat
type nul > .gitignore
```

Add these lines to `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
.vscode/
```

Important: `.venv/` should be ignored because it can be large and can be recreated from `requirements.txt`.

### Step 5: Create a Simple Python File

Create `app.py`:

```python
import requests

print("Virtual environments and Git are ready!")
print("Requests package version:", requests.__version__)
```

Run it while the virtual environment is active:

```bash
python app.py
```

### Step 6: Create a Project README

Create `README.md`:

```markdown
# Venv Git Practice

This is a practice project for learning Python virtual environments and Git.
```

### Step 7: Check Git Status

```bash
git status
```

Git should show new untracked files such as:

- `.gitignore`
- `README.md`
- `requirements.txt`
- `app.py`

It should **not** show `.venv/` if `.gitignore` is correct.

### Step 8: Stage Files

```bash
git add .gitignore README.md requirements.txt app.py
```

Staging means choosing files for the next commit.

### Step 9: Review Staged Files

```bash
git status
```

The staged files should appear under changes to be committed.

### Step 10: Commit the Work

```bash
git commit -m "Set up Python virtual environment practice project"
```

A commit saves a snapshot of the staged files.

### Step 11: View Commit History

```bash
git log --oneline
```

This shows a short list of commits.

---

## Part 6: Daily Workflow for Python Projects

Use this workflow each time you work on a Python project.

### 1. Open the Project Folder

```bash
cd path/to/your/project
```

### 2. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Missing Dependencies

If the project has a `requirements.txt` file, run:

```bash
python -m pip install -r requirements.txt
```

### 4. Work on Your Code

Edit Python files, Markdown files, and data files.

### 5. Run the Program

```bash
python app.py
```

### 6. Check Git Status

```bash
git status
```

### 7. Review Changes

```bash
git diff
```

### 8. Stage Good Changes

```bash
git add app.py README.md
```

Or stage all current changes:

```bash
git add .
```

### 9. Commit with a Clear Message

```bash
git commit -m "Improve practice app output"
```

### 10. Deactivate When Finished

```bash
deactivate
```

---

## Part 7: Understanding Important Files and Folders

| Item | Should Git Track It? | Why? |
|---|---:|---|
| `app.py` | Yes | This is source code. |
| `README.md` | Yes | This explains the project. |
| `requirements.txt` | Yes | This tells others which packages to install. |
| `.gitignore` | Yes | This tells Git what not to track. |
| `.venv/` | No | This is generated locally and can be recreated. |
| `__pycache__/` | No | This is generated automatically by Python. |
| `.env` | No | This may contain private secrets such as API keys. |

---

## Part 8: Common Problems and Fixes

### Problem: `python` Command Does Not Work

Try:

```bash
python3 --version
```

If `python3` works, use `python3` when creating the environment:

```bash
python3 -m venv .venv
```

### Problem: PowerShell Blocks Activation

PowerShell may show a script execution policy error. Try this command in PowerShell:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Problem: Package Installed but Python Cannot Import It

Check that the virtual environment is active:

```bash
python -c "import sys; print(sys.executable)"
```

The output path should include `.venv`.

### Problem: `.venv/` Appears in Git Status

Make sure `.gitignore` contains:

```gitignore
.venv/
```

If `.venv/` was already staged by mistake, unstage it:

```bash
git restore --staged .venv
```

### Problem: Commit Fails Because Name or Email Is Missing

Set your Git identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Part 9: Mini Practice Assignment

Create a new project called `weather_notes_practice`.

Your project must include:

- `.venv/` virtual environment;
- `.gitignore` file that ignores `.venv/`;
- `README.md` explaining the project;
- `requirements.txt` containing installed packages;
- `weather_notes.py` Python file;
- at least one Git commit.

Suggested `weather_notes.py` starter code:

```python
from datetime import date

city = input("City: ")
weather = input("Weather today: ")

print(f"{date.today()}: {city} weather note - {weather}")
```

Suggested commit message:

```bash
git commit -m "Create weather notes practice project"
```

---

## Part 10: Cheat Sheet

### Virtual Environment Commands

| Task | Windows PowerShell | macOS/Linux |
|---|---|---|
| Check Python | `python --version` | `python3 --version` |
| Create venv | `python -m venv .venv` | `python3 -m venv .venv` |
| Activate venv | `.\.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Deactivate venv | `deactivate` | `deactivate` |
| Upgrade pip | `python -m pip install --upgrade pip` | `python -m pip install --upgrade pip` |
| Install package | `python -m pip install requests` | `python -m pip install requests` |
| List packages | `python -m pip list` | `python -m pip list` |
| Save dependencies | `python -m pip freeze > requirements.txt` | `python -m pip freeze > requirements.txt` |
| Install dependencies | `python -m pip install -r requirements.txt` | `python -m pip install -r requirements.txt` |

### Git Commands

| Task | Command |
|---|---|
| Check Git version | `git --version` |
| Set name | `git config --global user.name "Your Name"` |
| Set email | `git config --global user.email "your.email@example.com"` |
| Show Git config | `git config --global --list` |
| Start Git in a folder | `git init` |
| Check file status | `git status` |
| Show exact unstaged changes | `git diff` |
| Stage one file | `git add app.py` |
| Stage all changes | `git add .` |
| Unstage a file | `git restore --staged app.py` |
| Commit staged changes | `git commit -m "Message here"` |
| Show commit history | `git log --oneline` |
| Show current branch | `git branch` |

### `.gitignore` Starter Template

```gitignore
# Python virtual environment
.venv/

# Python generated files
__pycache__/
*.pyc

# Environment variables and secrets
.env

# Operating system files
.DS_Store

# Editor settings
.vscode/
```

### Recommended Commit Message Patterns

| Situation | Example Commit Message |
|---|---|
| First project setup | `Set up project structure` |
| Add virtual environment notes | `Add virtual environment instructions` |
| Add Git notes | `Add Git workflow notes` |
| Fix a bug | `Fix package import error` |
| Update documentation | `Update README with setup steps` |
| Add a feature | `Add weather note input` |

---

## Final Student Checklist

Before finishing this unit, confirm that you can do each task:

- [ ] Create a project folder.
- [ ] Create `.venv` with `python -m venv .venv` or `python3 -m venv .venv`.
- [ ] Activate `.venv`.
- [ ] Install a package with `python -m pip install package_name`.
- [ ] Create `requirements.txt`.
- [ ] Create `.gitignore`.
- [ ] Ignore `.venv/` in Git.
- [ ] Run `git init`.
- [ ] Run `git status`.
- [ ] Stage files with `git add`.
- [ ] Commit files with `git commit -m "message"`.
- [ ] View history with `git log --oneline`.
- [ ] Deactivate the virtual environment.

---

## Key Takeaway

Use a virtual environment to keep project packages clean. Use Git to save project history. Together, `venv` and Git are the foundation for professional Python project work.
