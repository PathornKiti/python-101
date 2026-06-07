# Unit 05: Error Handling, Logging, Testing, JSON, and CSV

## Purpose

This unit wraps the Week 5 and Week 6 skills into one study folder. Students learn how to make Python programs safer, easier to debug, and easier to check before moving into Project 1.

Beginner programs often stop when one unexpected value appears. Intermediate programs should validate input, handle expected errors, write useful log messages, save structured data, and include tests for important helper functions.

## Learning Goals

By the end of this unit, students should be able to:

- explain why programs should validate data before saving it;
- raise `ValueError` when a function receives invalid data;
- use `try` and `except` around operations that can fail, such as reading files;
- write log messages with Python's built-in `logging` module;
- save and load data with JSON;
- save and load table-style data with CSV;
- write small unit tests with Python's built-in `unittest` module;
- run a script and test file from the terminal;
- connect safer code habits to the upcoming structured CLI project.

## Files in This Folder

| File or Folder | Purpose |
|---|---|
| `README.md` | Unit overview, study plan, commands, and practice tasks. |
| `unit05_error_logging_testing_data.ipynb` | Notebook lesson with explanations, examples, and guided practice. |
| `student_records_app.py` | Runnable study script that demonstrates validation, error handling, logging, JSON, CSV, and summaries. |
| `tests/test_student_records_app.py` | Unit tests for validation, summaries, and JSON/CSV round trips. |
| `data/` | Folder where the script writes sample JSON and CSV files. |
| `logs/` | Folder where the script writes the example log file. |

## Suggested Folder Structure

```text
unit05_error_logging_testing_data/
  README.md
  unit05_error_logging_testing_data.ipynb
  student_records_app.py
  data/
    study_records.json
    study_records.csv
  logs/
    unit05_app.log
  tests/
    test_student_records_app.py
```

The `data` and `logs` output files are created when the script runs.

## Key Vocabulary

| Word | Meaning |
|---|---|
| Exception | A Python error object that appears when something goes wrong while code is running. |
| Raise | To intentionally create an exception when data is invalid. |
| Handle | To respond to an expected exception with `try` and `except`. |
| Logging | Writing timestamped messages that help explain what the program did. |
| JSON | A structured text format that is useful for nested data and API-style records. |
| CSV | A table-style text format that is useful for rows and columns. |
| Unit test | A small automated check for one function or behavior. |
| Round trip | Saving data to a file and loading it back to confirm the result still matches. |

## How to Run the Script

From the repository root, run:

```bash
python python_for_intermediate_class/unit05_error_logging_testing_data/student_records_app.py
```

If your computer uses `python3`, run:

```bash
python3 python_for_intermediate_class/unit05_error_logging_testing_data/student_records_app.py
```

Expected output will look similar to this:

```text
Records: 3
Total minutes: 85
Completed topics: Error handling, Logging

Saved JSON: .../data/study_records.json
Saved CSV: .../data/study_records.csv
Log file: .../logs/unit05_app.log
```

## How to Run the Tests

From the repository root, run:

```bash
python -m unittest python_for_intermediate_class.unit05_error_logging_testing_data.tests.test_student_records_app
```

You can also run the tests with `pytest` if it is installed:

```bash
python -m pytest python_for_intermediate_class/unit05_error_logging_testing_data/tests
```

## Two-Part Teaching Plan

### Part 1: Error Handling and Logging

| Time | Activity | Output |
|---:|---|---|
| 0:00-0:15 | Review common failures: blank names, zero minutes, missing files, broken JSON | List of expected errors |
| 0:15-0:35 | Add validation with `raise ValueError` | Safer helper function |
| 0:35-0:55 | Use `try` and `except` for expected failures | Program continues after a handled problem |
| 0:55-1:15 | Configure logging and write `info`, `warning`, and `error` messages | Log file created in `logs/` |
| 1:15-2:00 | Practice debugging by reading terminal output and log output | Students can explain what happened |

### Part 2: Testing, JSON, and CSV

| Time | Activity | Output |
|---:|---|---|
| 0:00-0:20 | Convert records to dictionaries | Data is ready for files |
| 0:20-0:45 | Save and load JSON | `data/study_records.json` |
| 0:45-1:10 | Save and load CSV | `data/study_records.csv` |
| 1:10-1:35 | Write tests for validation and summary helpers | Passing test methods |
| 1:35-2:00 | Write round-trip tests for JSON and CSV | Confidence that saved data can be loaded again |

## Practice Tasks

1. Add one invalid sample record with `minutes=0` and observe how the script handles it.
2. Open the log file and find the warning or error message.
3. Add a new summary function named `average_minutes`.
4. Add a unit test for `average_minutes`.
5. Add a new field such as `date` or `difficulty` to `StudyRecord`.
6. Update both JSON and CSV saving so the new field is included.
7. Run the script and tests again after each change.

## Best Practice Checklist

Before using this pattern in Project 1, check that:

- reusable logic is inside functions;
- data is validated before it is saved;
- expected file problems are handled with clear messages;
- logs explain important program actions;
- JSON and CSV files are saved in a `data/` folder;
- tests cover both normal and invalid examples;
- tests use temporary files instead of overwriting real student data;
- terminal commands work from the repository root.
