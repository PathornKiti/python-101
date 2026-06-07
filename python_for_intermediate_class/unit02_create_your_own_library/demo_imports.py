"""Demo script for importing from a student-created library.

Run this file from the repository root with:

    python python_for_intermediate_class/unit02_create_your_own_library/demo_imports.py

This script imports three different object types from the same library:

- function: estimate_study_points
- class: StudyLibrary
- data model: StudySession
"""

from __future__ import annotations

from student_learning_library import StudyLibrary, StudySession, estimate_study_points


def main() -> None:
    """Create study sessions and print a progress report."""
    python_session = StudySession(topic="Python imports", minutes=35, completed=True)
    model_session = StudySession(topic="Data models", minutes=25, completed=False)

    first_session_points = estimate_study_points(
        python_session.minutes,
        python_session.completed,
    )

    library = StudyLibrary(student_name="Maya")
    library.add_session(python_session)
    library.add_session(model_session)

    print(f"First session points: {first_session_points}")
    print()
    print(library.build_report())


if __name__ == "__main__":
    main()
