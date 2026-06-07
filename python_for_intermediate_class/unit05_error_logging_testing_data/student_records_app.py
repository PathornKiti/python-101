"""Unit 05 study app: error handling, logging, tests, JSON, and CSV.

Run this file from the repository root with:

    python python_for_intermediate_class/unit05_error_logging_testing_data/student_records_app.py

This example is intentionally small and beginner-friendly. It shows how one
script can validate data, handle expected errors, write log messages, and save
records in both JSON and CSV formats.
"""

from __future__ import annotations

import csv
import json
import logging
from dataclasses import asdict, dataclass
from json import JSONDecodeError
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
JSON_PATH = DATA_DIR / "study_records.json"
CSV_PATH = DATA_DIR / "study_records.csv"
LOG_PATH = LOG_DIR / "unit05_app.log"


@dataclass
class StudyRecord:
    """A single study record saved by the learning tracker."""

    student: str
    topic: str
    minutes: int
    completed: bool


def configure_logging(log_path: Path = LOG_PATH) -> None:
    """Configure the app logger to write readable messages to a file."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        force=True,
    )


def validate_record(record: StudyRecord) -> None:
    """Validate one study record before saving it.

    Raises:
        ValueError: If any field has an invalid value.
    """
    if not record.student.strip():
        raise ValueError("student name cannot be blank")
    if not record.topic.strip():
        raise ValueError("topic cannot be blank")
    if record.minutes <= 0:
        raise ValueError("minutes must be greater than 0")


def add_record(records: list[StudyRecord], record: StudyRecord) -> list[StudyRecord]:
    """Return a new list with a validated record added."""
    validate_record(record)
    updated_records = [*records, record]
    logging.info("Added record for %s on %s", record.student, record.topic)
    return updated_records


def records_to_dicts(records: list[StudyRecord]) -> list[dict[str, object]]:
    """Convert StudyRecord objects to dictionaries for JSON and CSV output."""
    return [asdict(record) for record in records]


def parse_bool(value: object) -> bool:
    """Convert JSON or CSV boolean-style values to a real bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def dict_to_record(row: dict[str, object]) -> StudyRecord:
    """Convert a dictionary loaded from a file into a StudyRecord."""
    return StudyRecord(
        student=str(row["student"]),
        topic=str(row["topic"]),
        minutes=int(row["minutes"]),
        completed=parse_bool(row["completed"]),
    )


def save_records_json(records: list[StudyRecord], path: Path = JSON_PATH) -> None:
    """Save study records to a JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records_to_dicts(records), indent=2), encoding="utf-8")
    logging.info("Saved %s records to JSON: %s", len(records), path)


def load_records_json(path: Path = JSON_PATH) -> list[StudyRecord]:
    """Load study records from JSON, returning an empty list for common failures."""
    try:
        raw_records = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        logging.warning("JSON file was not found: %s", path)
        return []
    except JSONDecodeError:
        logging.error("JSON file could not be decoded: %s", path)
        return []

    records = [dict_to_record(row) for row in raw_records]
    logging.info("Loaded %s records from JSON: %s", len(records), path)
    return records


def save_records_csv(records: list[StudyRecord], path: Path = CSV_PATH) -> None:
    """Save study records to a CSV file with a header row."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["student", "topic", "minutes", "completed"])
        writer.writeheader()
        writer.writerows(records_to_dicts(records))
    logging.info("Saved %s records to CSV: %s", len(records), path)


def load_records_csv(path: Path = CSV_PATH) -> list[StudyRecord]:
    """Load study records from CSV, returning an empty list if the file is missing."""
    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = [dict_to_record(row) for row in reader]
    except FileNotFoundError:
        logging.warning("CSV file was not found: %s", path)
        return []

    logging.info("Loaded %s records from CSV: %s", len(records), path)
    return records


def total_minutes(records: list[StudyRecord]) -> int:
    """Return the total number of study minutes across all records."""
    return sum(record.minutes for record in records)


def completed_topics(records: list[StudyRecord]) -> list[str]:
    """Return topics from records marked as completed."""
    return [record.topic for record in records if record.completed]


def build_summary(records: list[StudyRecord]) -> str:
    """Build a short text summary for terminal output."""
    topics = completed_topics(records)
    completed_text = ", ".join(topics) if topics else "None yet"
    return (
        f"Records: {len(records)}\n"
        f"Total minutes: {total_minutes(records)}\n"
        f"Completed topics: {completed_text}"
    )


def main() -> None:
    """Run a tiny workflow that saves, loads, logs, and summarizes records."""
    configure_logging()
    logging.info("Unit 05 app started")

    records: list[StudyRecord] = []
    sample_records = [
        StudyRecord(student="Maya", topic="Error handling", minutes=30, completed=True),
        StudyRecord(student="Maya", topic="Logging", minutes=20, completed=True),
        StudyRecord(student="Maya", topic="JSON and CSV", minutes=35, completed=False),
    ]

    for record in sample_records:
        try:
            records = add_record(records, record)
        except ValueError as error:
            logging.error("Could not add record: %s", error)
            print(f"Skipping invalid record: {error}")

    save_records_json(records)
    save_records_csv(records)

    loaded_records = load_records_json()
    print(build_summary(loaded_records))
    print(f"\nSaved JSON: {JSON_PATH}")
    print(f"Saved CSV: {CSV_PATH}")
    print(f"Log file: {LOG_PATH}")

    logging.info("Unit 05 app finished")


if __name__ == "__main__":
    main()
