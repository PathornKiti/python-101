"""A first command-line program students can copy and modify.

Goal of this file:
    Students should learn the complete workflow:

    1. write Python code in a .py file;
    2. save the file;
    3. run the file from the terminal;
    4. pass different arguments on each run;
    5. let Python parse those arguments;
    6. use the parsed values inside normal Python code.

Try these commands from the repository root:

    python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Maya 14 Python
    python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Leo 16 JavaScript --excited
    python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py Aisha 15 Python --repeat 3 --excited
    python python_for_intermediate_class/unit03_command_line/build_your_first_cli.py --help

Notice that the code does not change between runs. Only the command-line
arguments change. That is the main reason command-line programs are useful.
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Describe every command-line argument this program accepts."""
    parser = argparse.ArgumentParser(
        description="Create a short student coding profile from CLI arguments.",
    )

    # Positional arguments are required and are read by order.
    parser.add_argument("name", help="student name, such as Maya")
    parser.add_argument("age", type=int, help="student age as a whole number")
    parser.add_argument(
        "favorite_language",
        help="favorite programming language, such as Python",
    )

    # Optional arguments are named. They can appear in different positions.
    parser.add_argument(
        "--repeat",
        type=int,
        default=1,
        help="how many times to print the profile; default: 1",
    )
    parser.add_argument(
        "--excited",
        action="store_true",
        help="add a more excited ending when this flag is present",
    )

    return parser


def build_profile(name: str, age: int, favorite_language: str, excited: bool) -> str:
    """Use parsed command-line values in regular Python code."""
    ending = "Let's build something awesome!" if excited else "Let's keep practicing."
    return (
        f"Student profile: {name} is {age} years old and is learning "
        f"{favorite_language}. {ending}"
    )


def main(argv: list[str] | None = None) -> None:
    """Parse arguments for this run and print the requested profile."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.age <= 0:
        parser.error("age must be greater than 0")
    if args.repeat <= 0:
        parser.error("--repeat must be greater than 0")

    profile = build_profile(
        name=args.name,
        age=args.age,
        favorite_language=args.favorite_language,
        excited=args.excited,
    )

    for _ in range(args.repeat):
        print(profile)


if __name__ == "__main__":
    main()
