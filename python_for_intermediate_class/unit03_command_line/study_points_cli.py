"""Command-line interface for one study session.

This script demonstrates argparse while reusing the Unit 02 library.

Run from the repository root:

    python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Python imports" 35 --completed --student Maya
    python python_for_intermediate_class/unit03_command_line/study_points_cli.py "Data models" 25 --student Maya --format compact
    python python_for_intermediate_class/unit03_command_line/study_points_cli.py --help

Command-line concepts demonstrated:
    - positional arguments: topic, minutes
    - optional argument: --student / -s
    - boolean flag: --completed
    - choices: --format text or compact
    - type conversion: minutes becomes an int
    - default values: student and format have defaults
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


UNIT02_FOLDER = Path(__file__).resolve().parents[1] / "unit02_create_your_own_library"
sys.path.insert(0, str(UNIT02_FOLDER))

from student_learning_library import StudyLibrary, StudySession, estimate_study_points


def build_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for this CLI."""
    parser = argparse.ArgumentParser(
        description="Calculate study points for one command-line study session.",
        epilog="Tip: use quotes around topics with spaces, such as \"Python imports\".",
    )

    parser.add_argument(
        "topic",
        help="study topic, such as 'Python imports'",
    )
    parser.add_argument(
        "minutes",
        type=int,
        help="number of minutes studied; must be greater than 0",
    )
    parser.add_argument(
        "-s",
        "--student",
        default="Student",
        help="student name used in the report; default: Student",
    )
    parser.add_argument(
        "--completed",
        action="store_true",
        help="mark the study session as completed",
    )
    parser.add_argument(
        "--format",
        choices=["text", "compact"],
        default="text",
        help="output style; choose text or compact; default: text",
    )

    return parser


def build_text_report(student: str, session: StudySession) -> str:
    """Use the Unit 02 StudyLibrary class to build a readable report."""
    library = StudyLibrary(student_name=student)
    library.add_session(session)
    return library.build_report()


def build_compact_report(student: str, session: StudySession) -> str:
    """Build a short one-line report for terminal output."""
    points = estimate_study_points(session.minutes, session.completed)
    status = "completed" if session.completed else "not completed"
    return (
        f"{student}: {session.topic} | {session.minutes} min | "
        f"{points} points | {status}"
    )


def main(argv: list[str] | None = None) -> None:
    """Parse command-line arguments and print the study report."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.minutes <= 0:
        parser.error("minutes must be greater than 0")

    session = StudySession(
        topic=args.topic,
        minutes=args.minutes,
        completed=args.completed,
    )

    if args.format == "compact":
        print(build_compact_report(args.student, session))
    else:
        points = estimate_study_points(session.minutes, session.completed)
        print(f"Study points for this session: {points}")
        print()
        print(build_text_report(args.student, session))


if __name__ == "__main__":
    main()
