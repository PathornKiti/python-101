"""Unit tests for the Unit 05 study records app.

Run from the repository root with:

    python -m unittest python_for_intermediate_class.unit05_error_logging_testing_data.tests.test_student_records_app
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from python_for_intermediate_class.unit05_error_logging_testing_data.student_records_app import (
    StudyRecord,
    add_record,
    completed_topics,
    load_records_csv,
    load_records_json,
    save_records_csv,
    save_records_json,
    total_minutes,
)


class TestStudentRecordsApp(unittest.TestCase):
    """Tests for validation, summaries, and file handling."""

    def test_add_record_accepts_valid_record(self) -> None:
        record = StudyRecord("Maya", "Testing", 25, True)

        records = add_record([], record)

        self.assertEqual(records, [record])

    def test_add_record_rejects_zero_minutes(self) -> None:
        record = StudyRecord("Maya", "Testing", 0, True)

        with self.assertRaises(ValueError):
            add_record([], record)

    def test_summary_helpers(self) -> None:
        records = [
            StudyRecord("Maya", "Logging", 20, True),
            StudyRecord("Maya", "CSV", 35, False),
        ]

        self.assertEqual(total_minutes(records), 55)
        self.assertEqual(completed_topics(records), ["Logging"])

    def test_json_round_trip(self) -> None:
        records = [StudyRecord("Maya", "JSON", 30, True)]

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "records.json"
            save_records_json(records, path)
            loaded_records = load_records_json(path)

        self.assertEqual(loaded_records, records)

    def test_csv_round_trip(self) -> None:
        records = [StudyRecord("Maya", "CSV", 30, False)]

        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "records.csv"
            save_records_csv(records, path)
            loaded_records = load_records_csv(path)

        self.assertEqual(loaded_records, records)


if __name__ == "__main__":
    unittest.main()
