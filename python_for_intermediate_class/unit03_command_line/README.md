# Unit 03: Command Line Basics and Python Arguments

## Purpose

This unit teaches students how to use the command line to run Python scripts and pass information into programs using arguments.

In Unit 01, students moved from notebooks to `.py` files. In Unit 02, students created a reusable learning library. In this unit, students connect those skills by running scripts from the terminal and building small command-line interfaces, also called CLIs.

## Learning Goals

By the end of this unit, students should be able to:

- explain what the terminal, shell, prompt, command, option, flag, and argument are;
- navigate folders from the command line;
- run Python scripts from the repository root;
- write a small `.py` CLI program and call it repeatedly with different arguments;
- explain how `sys.argv` receives raw command-line arguments;
- explain why command-line input starts as strings;
- use `argparse` to create friendly command-line programs;
- create positional arguments, optional arguments, short options, boolean flags, defaults, choices, and typed arguments;
- use `--help` to learn a CLI program;
- import and reuse the Unit 02 learning library from a Unit 03 command-line script.

## Files in This Folder

| File | Purpose |
|---|---|
| `README.md` | Full lesson guide for command-line basics and Python arguments. |
| `CLI_CHEAT_SHEET.md` | Quick reference for common terminal, Python, virtual environment, and Git commands. |
| `command_line_components.py` | Beginner-friendly script that teaches `sys.argv` and shows every raw command-line component. |
| `build_your_first_cli.py` | Step-by-step first CLI program students can copy, modify, run, and rerun with different arguments. |
| `study_points_cli.py` | Practical `argparse` CLI that uses the Unit 02 study library. |
| `multi_session_cli.py` | More advanced `argparse` example using repeated arguments and subcommands. |

## Necessary CLI Commands for This Unit

Run all commands from the repository root unless the instruction says otherwise.

### Check Your Location

```bash
pwd
```

### List Course Folders

```bash
ls python_for_intermediate_class
```

### Open Unit 03 Folder

```bash
cd python_for_intermediate_class/unit03_command_line
```

### Go Back to Repository Root

```bash
cd ../..
```

### Check Python

```bash
python --version
```

If needed:

```bash
python3 --version
```

### Run the Raw Argument Demo

```bash
python python_for_intermediate_class/unit03_command_line/command_line_components.py Maya 30 --completed
```

### Ask the Raw Argument Demo for Help

```bash
python python_for_intermediate_class/unit03_command_line/command_line_components.py --help
```

### Run the First Student-Written CLI Pattern

```bash
python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Maya 14 Python
```

### Rerun the Same Code with Different Arguments

```bash
python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Aisha 15 Python --repeat 3 --excited
```

### Ask the First CLI Pattern for Help

```bash
python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py --help
```

### Run the Practical Study Points CLI

```bash
python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Python imports" 35 --completed --student Maya
```

### Ask the Practical CLI for Help

```bash
python python_for_intermediate_class/unit03_command_line/study_points_cli.py --help
```

### Run the Multi-Session CLI Summary

```bash
python python_for_intermediate_class/unit03_command_line/multi_session_cli.py summary --student Maya --session "Python imports:35:true" --session "Data models:25:false"
```

### Run the Multi-Session CLI Template Command

```bash
python python_for_intermediate_class/unit03_command_line/multi_session_cli.py template --student Maya
```

## Command-Line Vocabulary

| Word | Meaning | Example |
|---|---|---|
| Terminal | App where you type commands. | VS Code terminal, Terminal.app, Windows Terminal. |
| Shell | Program that interprets commands. | Bash, Zsh, PowerShell. |
| Prompt | Text displayed before your command. | `$`, `%`, `PS C:\Users\Maya>`. |
| Working directory | Folder where the command runs. | `/workspace/python-101`. |
| Command | Program or shell action being run. | `python`, `cd`, `git`. |
| Argument | Information passed to a command. | `app.py`, `Maya`, `30`. |
| Option | Named argument that changes behavior. | `--student Maya`. |
| Flag | Boolean option that is on when present. | `--completed`. |
| Positional argument | Argument identified by position/order. | `"Python imports" 35`. |
| Path | Address of a file or folder. | `python_for_intermediate_class/unit03_command_line/study_points_cli.py`. |

## Anatomy of a Command

Command:

```bash
python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Python imports" 35 --completed --student Maya
```

Breakdown:

| Piece | Component | Job |
|---|---|---|
| `python` | Command | Starts Python. |
| `python_for_intermediate_class/unit03_command_line/study_points_cli.py` | Script path | Tells Python which file to run. |
| `"Python imports"` | First positional argument | Topic name. Quotes keep words together. |
| `35` | Second positional argument | Study minutes. |
| `--completed` | Boolean flag | Marks the session as completed. |
| `--student Maya` | Optional argument | Gives a student name. |

## Student Workflow: Write Code, Then Call It from the CLI

A command-line program is still normal Python code. The difference is that input can come from the terminal instead of from `input()` or hard-coded variables.

Use this workflow every time you create a small CLI program:

1. **Create or open a `.py` file.** Example: `build_your_first_cli.py`.
2. **Import `argparse`.** This gives Python a clean way to understand command-line arguments.
3. **Create a parser.** The parser describes what values the user may type.
4. **Add arguments.** Use positional arguments for required values and optional arguments for settings.
5. **Parse this run.** `args = parser.parse_args()` reads the values typed in the terminal for the current run.
6. **Use `args.name`, `args.age`, or other parsed values in regular Python code.**
7. **Run the file from the terminal.** Change only the command arguments to create different results.
8. **Rerun with `--help`.** Check whether your CLI explains itself clearly.

Minimal pattern:

```python
import argparse

parser = argparse.ArgumentParser(description="Say hello from the command line.")
parser.add_argument("name", help="person to greet")
parser.add_argument("--times", type=int, default=1, help="number of greetings")
args = parser.parse_args()

for _ in range(args.times):
    print(f"Hello, {args.name}!")
```

If this code is saved in `hello_cli.py`, you can call it like this:

```bash
python hello_cli.py Maya
python hello_cli.py Maya --times 3
python hello_cli.py Leo --times 2
```

The file stays the same. Each run passes new arguments, and `parse_args()` creates a new `args` object for that run.

## Arguments in Python: `sys.argv`

The lowest-level way to read command-line arguments is `sys.argv`.

```python
import sys
print(sys.argv)
```

If the user runs:

```bash
python script.py Maya 30 --completed
```

Python receives a list similar to:

```python
['script.py', 'Maya', '30', '--completed']
```

Important rules:

1. `sys.argv[0]` is the script path/name.
2. `sys.argv[1]` is the first value typed after the script name.
3. Command-line values arrive as strings.
4. If you need a number, convert it with `int()` or use `argparse` with `type=int`.
5. Manual `sys.argv` parsing is useful for learning, but `argparse` is better for real tools.

## Arguments in Python: `argparse`

`argparse` is Python's built-in tool for creating command-line interfaces.

It helps with:

- automatic `--help` pages;
- required positional arguments;
- optional arguments;
- short options like `-s`;
- boolean flags;
- data conversion with `type=int`;
- allowed values with `choices=[...]`;
- default values;
- clear error messages.

Example pattern:

```python
import argparse

parser = argparse.ArgumentParser(description="Explain what the script does.")
parser.add_argument("topic", help="Study topic")
parser.add_argument("minutes", type=int, help="Minutes studied")
parser.add_argument("--completed", action="store_true", help="Mark task completed")
args = parser.parse_args()

print(args.topic)
print(args.minutes)
print(args.completed)
```

## Common `argparse` Components

| Component | Example | Meaning |
|---|---|---|
| `ArgumentParser` | `argparse.ArgumentParser(...)` | Creates the CLI parser. |
| Description | `description="..."` | Text shown in `--help`. |
| Positional argument | `add_argument("topic")` | Required by position. |
| Optional argument | `add_argument("--student")` | Named value. |
| Short option | `add_argument("-s", "--student")` | Short and long names. |
| Type conversion | `type=int` | Converts text to integer. |
| Default value | `default="Student"` | Used when option is missing. |
| Boolean flag | `action="store_true"` | `False` by default, `True` when present. |
| Choices | `choices=["text", "json"]` | Restricts accepted values. |
| Repeated option | `action="append"` | Collects multiple uses into a list. |
| Subcommand | `subparsers.add_parser("summary")` | Creates commands inside your program. |

## Why Reuse Unit 02?

A good CLI file should focus on user input and output. The real reusable logic should live in a library.

Unit 02 already has a library with:

```python
from student_learning_library import StudyLibrary, StudySession, estimate_study_points
```

Unit 03 imports that library in `study_points_cli.py` and `multi_session_cli.py`. This demonstrates a common project pattern:

1. library code handles important logic;
2. CLI code receives command-line arguments;
3. CLI code calls the library;
4. CLI code prints results for the user.

## Practice Tasks

1. Run every command in the **Necessary CLI Commands** section.
2. Run `command_line_components.py` with your own name and favorite topic.
3. Run `study_points_cli.py` with and without `--completed`.
4. Change `--format text` to `--format compact` in `study_points_cli.py`.
5. Try an invalid format and read the error message.
6. Add a new optional argument to `study_points_cli.py`, such as `--goal-minutes`.
7. Add another subcommand to `multi_session_cli.py`, such as `points`.
8. Explain to a partner the difference between a positional argument and a flag.

## Best Practice Checklist

Before calling a Python file a good CLI script, check that:

- users can run it from the terminal;
- `--help` explains what the command does;
- required inputs are clear;
- optional settings have helpful names;
- numbers use `type=int` or another converter;
- invalid input produces useful messages;
- reusable logic is imported from a library instead of copied;
- the script has a `main()` function;
- the bottom of the file uses `if __name__ == "__main__":`.
