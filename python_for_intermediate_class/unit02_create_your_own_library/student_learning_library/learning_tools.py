"""Small reusable library for tracking study sessions.

Students can import these objects from another script or notebook:

- function: estimate_study_points
- class: StudyLibrary
- data model: StudySession
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StudySession:
    """Data model representing one study session.

    Args:
        topic: The skill, lesson, or subject practiced by the student.
        minutes: The number of minutes spent studying. Must be positive.
        completed: Whether the student finished the planned study task.
    """

    topic: str
    minutes: int
    completed: bool = False

    def __post_init__(self) -> None:
        """Validate study session data after the model is created."""
        if not self.topic.strip():
            raise ValueError("topic must not be empty")
        if self.minutes <= 0:
            raise ValueError("minutes must be greater than 0")


def estimate_study_points(minutes: int, completed: bool = False) -> int:
    """Return simple study points based on minutes and completion.

    Students earn 1 point for every 10 minutes of study. They earn 2 bonus
    points when the planned task is completed.
    """
    if minutes <= 0:
        raise ValueError("minutes must be greater than 0")

    points = minutes // 10
    if completed:
        points += 2
    return points


class StudyLibrary:
    """Collect and summarize study sessions for one student."""

    def __init__(self, student_name: str) -> None:
        """Create an empty study library for a student."""
        if not student_name.strip():
            raise ValueError("student_name must not be empty")

        self.student_name = student_name
        self.sessions: list[StudySession] = []

    def add_session(self, session: StudySession) -> None:
        """Add one StudySession data model to the library."""
        self.sessions.append(session)

    def total_minutes(self) -> int:
        """Return the total number of minutes studied."""
        return sum(session.minutes for session in self.sessions)

    def total_points(self) -> int:
        """Return total study points for every saved session."""
        return sum(
            estimate_study_points(session.minutes, session.completed)
            for session in self.sessions
        )

    def completed_topics(self) -> list[str]:
        """Return topics from sessions marked as completed."""
        return [session.topic for session in self.sessions if session.completed]

    def build_report(self) -> str:
        """Build a readable progress report for the student."""
        completed = self.completed_topics()
        completed_text = ", ".join(completed) if completed else "None yet"

        return (
            f"Study report for {self.student_name}\n"
            f"Sessions: {len(self.sessions)}\n"
            f"Total minutes: {self.total_minutes()}\n"
            f"Total points: {self.total_points()}\n"
            f"Completed topics: {completed_text}"
        )
