"""Teach the raw components of a command-line call with sys.argv.

This file is intentionally beginner-friendly and verbose. It shows what Python
receives from the shell before a real parser such as argparse organizes the
values.

Try from the repository root:

    python python_for_intermediate_class/unit03_command_line/command_line_components.py Maya 30 --completed
    python python_for_intermediate_class/unit03_command_line/command_line_components.py "Python imports" 35 --completed
    python python_for_intermediate_class/unit03_command_line/command_line_components.py --help

Key lesson:
    Every value in sys.argv starts as text, even when it looks like a number.
"""

from __future__ import annotations

import sys
from pathlib import Path


HELP_TEXT = """
Unit 03 raw command-line component demo

Usage:
    python python_for_intermediate_class/unit03_command_line/command_line_components.py NAME MINUTES [--completed]

Examples:
    python python_for_intermediate_class/unit03_command_line/command_line_components.py Maya 30 --completed
    python python_for_intermediate_class/unit03_command_line/command_line_components.py "Python imports" 35

This demo does not use argparse because its purpose is to show raw sys.argv.
For a real CLI, see study_points_cli.py.
""".strip()


def print_heading(title: str) -> None:
    """Print a visible lesson section heading."""
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def explain_command_environment() -> None:
    """Explain where the command is running."""
    print_heading("1. Command environment")
    print(f"Current working directory: {Path.cwd()}")
    print(f"Python executable: {sys.executable}")
    print(
        "The working directory matters because relative paths are calculated "
        "from this folder."
    )


def explain_sys_argv() -> None:
    """Print each raw command-line value Python received."""
    print_heading("2. Raw sys.argv values")
    print("sys.argv is a list of strings received from the shell.")
    print(f"Full sys.argv list: {sys.argv!r}")
    print()

    for index, value in enumerate(sys.argv):
        if index == 0:
            role = "script path/name"
        else:
            role = f"user argument #{index}"
        print(f"sys.argv[{index}] = {value!r}  <-- {role}")


def explain_manual_parsing() -> None:
    """Show how manual parsing works and why argparse is usually better."""
    print_heading("3. Manual parsing example")

    user_arguments = sys.argv[1:]
    print(f"User arguments only: {user_arguments!r}")

    if len(user_arguments) < 2:
        print("This demo expects at least NAME and MINUTES after the script path.")
        print("Run with --help to see example commands.")
        return

    name = user_arguments[0]
    raw_minutes = user_arguments[1]
    completed = "--completed" in user_arguments

    print(f"Name/topic argument: {name!r}")
    print(f"Raw minutes argument: {raw_minutes!r}")
    print(f"Completed flag present? {completed}")
    print(f"Type before conversion: {type(raw_minutes).__name__}")

    if raw_minutes.isdigit():
        minutes = int(raw_minutes)
        print(f"Converted minutes: {minutes}")
        print(f"Type after conversion: {type(minutes).__name__}")
    else:
        print("Minutes could not be converted because it is not all digits.")

    print(
        "Manual parsing is okay for tiny demos, but it becomes messy when a "
        "program has many options. Use argparse for real CLI programs."
    )


def explain_cli_terms() -> None:
    """Teach common command-line component vocabulary."""
    print_heading("4. Important command-line terms")

    terms = [
        ("command", "The program or shell action you run, such as python."),
        ("script path", "The .py file Python should execute."),
        ("positional argument", "A value understood by its order."),
        ("optional argument", "A named setting such as --student Maya."),
        ("flag", "A true/false option such as --completed."),
        ("working directory", "The folder where your command starts."),
        ("quote", "Characters that keep words with spaces together."),
    ]

    for term, meaning in terms:
        print(f"{term:22} {meaning}")


def main() -> None:
    """Run the lesson demo."""
    if "--help" in sys.argv or "-h" in sys.argv:
        print(HELP_TEXT)
        return

    explain_command_environment()
    explain_sys_argv()
    explain_manual_parsing()
    explain_cli_terms()


if __name__ == "__main__":
    main()
