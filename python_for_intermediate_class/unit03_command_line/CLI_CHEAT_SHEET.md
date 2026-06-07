# Unit 03 Command Line Cheat Sheet

This cheat sheet summarizes the terminal commands and Python command-line ideas used in Unit 03.

## 1. What Is the Command Line?

The **command line** is a text-based way to control your computer. Instead of clicking folders and buttons, you type commands.

Common names:

| Name | Meaning |
|---|---|
| Terminal | General app for typing commands. |
| Shell | Program that reads your commands, such as Bash, Zsh, PowerShell, or Command Prompt. |
| Prompt | The text shown before you type, often ending with `$`, `%`, or `>`. |
| Working directory | The folder where your command runs right now. |
| Command | The program or built-in shell action you run. |
| Argument | Extra information passed to a command. |
| Option / flag | A named argument that changes behavior, such as `--help` or `-m`. |

## 2. Folder Navigation Commands

| Task | macOS / Linux / Git Bash | Windows PowerShell | Example |
|---|---|---|---|
| Show current folder | `pwd` | `pwd` | `pwd` |
| List files | `ls` | `Get-ChildItem` or `ls` | `ls` |
| List hidden files | `ls -a` | `Get-ChildItem -Force` | `ls -a` |
| Change folder | `cd folder_name` | `cd folder_name` | `cd python_for_intermediate_class` |
| Go up one folder | `cd ..` | `cd ..` | `cd ..` |
| Go home | `cd ~` | `cd ~` | `cd ~` |
| Clear screen | `clear` | `Clear-Host` or `cls` | `clear` |

## 3. File and Folder Commands

| Task | macOS / Linux / Git Bash | Windows PowerShell | Example |
|---|---|---|---|
| Create folder | `mkdir name` | `mkdir name` | `mkdir practice_cli` |
| Create empty file | `touch file.py` | `New-Item file.py` | `touch notes.txt` |
| Copy file | `cp old new` | `Copy-Item old new` | `cp app.py backup_app.py` |
| Move or rename | `mv old new` | `Move-Item old new` | `mv old_name.py new_name.py` |
| Remove file | `rm file.py` | `Remove-Item file.py` | `rm scratch.py` |
| Show file text | `cat file.txt` | `Get-Content file.txt` | `cat README.md` |

> Be careful with remove commands. Deleted files may not go to the recycle bin.

## 4. Python Commands

| Task | Command |
|---|---|
| Check Python version | `python --version` |
| Alternative version command | `python3 --version` |
| Run a Python script | `python path/to/script.py` |
| Run a module | `python -m module_name` |
| Open Python interactive mode | `python` |
| Exit interactive mode | `exit()` |
| Install a package | `python -m pip install package_name` |
| Show installed packages | `python -m pip list` |

For this repository, run Unit 03 examples from the repository root:

```bash
python python_for_intermediate_class/unit03_command_line/command_line_components.py Maya 30 --completed
python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Maya 14 Python
python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Python imports" 35 --completed --student Maya
```

If your system uses `python3`, replace `python` with `python3`.

## 5. Command Anatomy

Example command:

```bash
python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Python imports" 35 --completed --student Maya
```

| Part | Name | Meaning |
|---|---|---|
| `python` | Command / program | Runs the Python interpreter. |
| `python_for_intermediate_class/unit03_command_line/study_points_cli.py` | Script path | The Python file to execute. |
| `"Python imports"` | Positional argument | Topic text. Quotes keep two words together as one value. |
| `35` | Positional argument | Study minutes. The script converts it to an integer. |
| `--completed` | Optional flag | A boolean switch. Present means `True`; absent means `False`. |
| `--student Maya` | Optional argument | Named option with a value. |


## 6. Write Code, Then Call It from the CLI

Basic student pattern:

```python
import argparse

parser = argparse.ArgumentParser(description="Say hello.")
parser.add_argument("name", help="person to greet")
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args()

for _ in range(args.times):
    print(f"Hello, {args.name}!")
```

Run the same file multiple ways:

```bash
python hello_cli.py Maya
python hello_cli.py Maya --times 3
python hello_cli.py Leo --times 2
```

Each run creates new parsed values in `args`.

## 7. Arguments: The Big Idea

An **argument** is information you give to a command.

Python receives command-line arguments in `sys.argv`:

```python
import sys
print(sys.argv)
```

If you run:

```bash
python script.py apple banana
```

Python sees something like:

```python
['script.py', 'apple', 'banana']
```

Important detail:

- `sys.argv[0]` is the script name.
- `sys.argv[1]` is the first user argument.
- All values arrive as strings until you convert them.

## 8. Positional Arguments vs Optional Arguments

| Type | Example | Required? | Best For |
|---|---|---:|---|
| Positional argument | `topic 30` | Usually yes | Main information the command needs. |
| Optional argument | `--student Maya` | Usually no | Settings or extra details. |
| Short option | `-s Maya` | Usually no | Fast typing after students know the command. |
| Boolean flag | `--completed` | No | Turning a feature on or off. |

## 9. Quoting Rules

Use quotes when an argument contains spaces:

```bash
python app.py "Python imports"
```

Without quotes, the shell splits words:

```bash
python app.py Python imports
```

The program receives two arguments: `Python` and `imports`.

## 10. Helpful Shell Symbols

| Symbol | Name | Use |
|---|---|---|
| `.` | Current folder | `python ./app.py` |
| `..` | Parent folder | `cd ..` |
| `~` | Home folder | `cd ~` |
| `/` | Path separator on macOS/Linux | `folder/file.py` |
| `\` | Common path separator on Windows | `folder\file.py` |
| `*` | Wildcard | `*.py` means Python files. |
| `>` | Redirect output | `python app.py > output.txt` |
| `>>` | Append output | `python app.py >> output.txt` |
| `|` | Pipe output | `python app.py | more` |

## 11. Virtual Environment Commands

Create a virtual environment:

```bash
python -m venv .venv
```

Activate on macOS / Linux / Git Bash:

```bash
source .venv/bin/activate
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Deactivate:

```bash
deactivate
```

Install packages inside the environment:

```bash
python -m pip install pytest
```

Save dependencies:

```bash
python -m pip freeze > requirements.txt
```

Install saved dependencies:

```bash
python -m pip install -r requirements.txt
```

## 12. Git Commands Students Need Soon

| Task | Command |
|---|---|
| Check repository status | `git status` |
| See file changes | `git diff` |
| Stage all changes | `git add .` |
| Commit staged changes | `git commit -m "message"` |
| See commit history | `git log --oneline` |

## 13. Debugging Command-Line Problems

| Problem | Common Cause | Fix |
|---|---|---|
| `python: command not found` | Python is not on PATH or command is `python3`. | Try `python3 --version`. |
| `No such file or directory` | Wrong folder or wrong path. | Run `pwd`, `ls`, then check the path. |
| `ModuleNotFoundError` | Python cannot find an imported package/module. | Run from the correct folder or install the package. |
| Argument with spaces is split | Missing quotes. | Use `"two words"`. |
| Number behaves like text | CLI values are strings. | Convert with `int()` or use `argparse type=int`. |
| Optional flag ignored | Flag name misspelled. | Run the command with `--help`. |

## 14. Best Practices

- Run commands from the project root when paths in lessons assume the repository root.
- Prefer `python -m pip ...` instead of plain `pip ...` so pip belongs to the same Python interpreter.
- Add `--help` to CLI programs so users can learn commands by themselves.
- Use `argparse` for real scripts instead of manually reading many `sys.argv` positions.
- Validate user input and show friendly error messages.
- Keep reusable logic in a library, then build a CLI file that imports that library.
