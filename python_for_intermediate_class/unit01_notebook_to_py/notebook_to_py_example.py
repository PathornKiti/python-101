"""Unit 01 example: convert notebook-style code into a reusable Python script.

This file is intentionally beginner-friendly. It shows how a small block of
notebook code can become functions, a script entry point, and reusable logic.

Key ideas:
- Keep calculation logic inside functions.
- Use parameters instead of depending on hidden notebook variables.
- Return values from functions so they can be tested and reused.
- Put runnable workflow code inside main().
- Use if __name__ == "__main__" so importing this file does not run the script.
"""

from __future__ import annotations


def calculate_average(scores: list[float]) -> float:
    """Return the average score from a non-empty list of scores.

    Args:
        scores: A list of numeric scores.

    Returns:
        The arithmetic mean of the scores.

    Raises:
        ValueError: If the scores list is empty.
    """
    if not scores:
        raise ValueError("scores must contain at least one number")

    return sum(scores) / len(scores)


def assign_letter_grade(average: float) -> str:
    """Return a simple letter grade for an average score."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def build_student_report(student_name: str, scores: list[float]) -> str:
    """Create a short report for one student.

    This function combines smaller helper functions. In a notebook, this same
    logic might start as several separate cells. In a `.py` file, we give the
    logic a name so it can be reused from a notebook, another script, or a test.
    """
    average = calculate_average(scores)
    grade = assign_letter_grade(average)

    return (
        f"Student: {student_name}\n"
        f"Scores: {scores}\n"
        f"Average: {average:.2f}\n"
        f"Grade: {grade}"
    )


def main() -> None:
    """Run the example workflow when this file is executed directly."""
    student_name = "Maya"
    scores = [88, 92, 79, 95]
    report = build_student_report(student_name, scores)
    print(report)


if __name__ == "__main__":
    main()
