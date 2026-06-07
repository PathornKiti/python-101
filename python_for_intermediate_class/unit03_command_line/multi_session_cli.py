"""Command-line interface with repeated options and subcommands.

This file demonstrates more components that are common in real command-line
programs:

- subcommands: summary and template
- repeated options: --session can be used more than once
- default values: --student defaults to Student
- simple input format parsing: topic:minutes:completed

Run from the repository root:

    python python_for_intermediate_class/unit03_command_line/multi_session_cli.py template --student Maya

    python python_for_intermediate_class/unit03_command_line/multi_session_cli.py summary --student Maya --session "Python imports:35:true" --session "Data models:25:false"

The session format is:

    "topic:minutes:completed"

Examples:

    "Python imports:35:true"
    "Data models:25:false"
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


UNIT02_FOLDER = Path(__file__).resolve().parents[1] / "unit02_create_your_own_library"
sys.path.insert(0, str(UNIT02_FOLDER))

from student_learning_library import StudyLibrary, StudySession


def parse_completed(raw_value: str) -> bool:
    """Convert common true/false text into a Boolean value."""
    normalized = raw_value.strip().lower()
    if normalized in {"true", "t", "yes", "y", "1", "completed"}:
        return True
    if normalized in {"false", "f", "no", "n", "0", "incomplete"}:
        return False
    raise argparse.ArgumentTypeError(
        "completed must be true/false, yes/no, 1/0, completed, or incomplete"
    )


def parse_session(raw_session: str) -> StudySession:
    """Parse one topic:minutes:completed value into a StudySession."""
    pieces = raw_session.split(":")
    if len(pieces) != 3:
        raise argparse.ArgumentTypeError(
            "session must use the format 'topic:minutes:completed'"
        )

    topic, raw_minutes, raw_completed = pieces
    topic = topic.strip()

    try:
        minutes = int(raw_minutes)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("session minutes must be an integer") from exc

    completed = parse_completed(raw_completed)

    try:
        return StudySession(topic=topic, minutes=minutes, completed=completed)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level parser and its subcommands."""
    parser = argparse.ArgumentParser(
        description="Build reports for one or more study sessions.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    template_parser = subparsers.add_parser(
        "template",
        help="print example commands and session formats",
    )
    template_parser.add_argument(
        "-s",
        "--student",
        default="Student",
        help="student name to place in the example",
    )

    summary_parser = subparsers.add_parser(
        "summary",
        help="summarize repeated --session values",
    )
    summary_parser.add_argument(
        "-s",
        "--student",
        default="Student",
        help="student name used in the report",
    )
    summary_parser.add_argument(
        "--session",
        action="append",
        type=parse_session,
        required=True,
        metavar="TOPIC:MINUTES:COMPLETED",
        help="study session; repeat this option for multiple sessions",
    )

    return parser


def print_template(student: str) -> None:
    """Print examples that students can copy and edit."""
    print("Session format:")
    print('  "topic:minutes:completed"')
    print()
    print("Example summary command:")
    print(
        "  python python_for_intermediate_class/unit03_command_line/"
        f"multi_session_cli.py summary --student {student} "
        '--session "Python imports:35:true" '
        '--session "Data models:25:false"'
    )


def print_summary(student: str, sessions: list[StudySession]) -> None:
    """Use the Unit 02 StudyLibrary class to print a multi-session report."""
    library = StudyLibrary(student_name=student)
    for session in sessions:
        library.add_session(session)

    print(library.build_report())
    print()
    print("Detailed sessions:")
    for index, session in enumerate(sessions, start=1):
        completed = "yes" if session.completed else "no"
        print(
            f"{index}. {session.topic} | "
            f"{session.minutes} min | completed: {completed}"
        )


def main(argv: list[str] | None = None) -> None:
    """Parse subcommands and run the selected command."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "template":
        print_template(args.student)
    elif args.command == "summary":
        print_summary(args.student, args.session)
    else:
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
