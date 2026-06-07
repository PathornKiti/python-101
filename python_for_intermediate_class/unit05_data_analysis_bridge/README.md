# Unit 05: Data Preparation and Analysis Bridge

## Purpose

This unit fills the missing middle step between the structured command-line project and the later visualization, Streamlit, API, and capstone units.

After Project 1, students have a working CLI application that stores data in JSON or CSV. Before they make charts or dashboards, they need to learn how to inspect that data, clean it, summarize it, and explain what it means.

Unit 05 helps students turn "my app saves data" into "my app produces data I can trust, analyze, present, and reuse."

## Why This Unit Belongs Here

| Course Position | What Students Already Have | What Unit 05 Adds | What It Prepares Students For |
|---|---|---|---|
| After Units 01-04 and Project 1 | Scripts, modules, imports, Git, `venv`, tests, logging, JSON or CSV storage, and a structured CLI project | Clean data files, reusable analysis functions, summary tables, and short written findings | Visualization, reports, Streamlit dashboards, API data processing, and capstone project planning |

## Learning Goals

By the end of this unit, students should be able to:

- load data saved by their Project 1 CLI application;
- inspect JSON or CSV records for missing, duplicated, invalid, or inconsistent values;
- separate raw data from cleaned data;
- write small reusable summary functions;
- create useful metrics such as totals, counts, averages, top categories, and date-based summaries;
- test at least one summary function with `pytest`;
- write a short analysis note that explains what the data shows;
- prepare cleaned data and summary tables for charts, reports, Streamlit, APIs, and the capstone.

## Files in This Folder

This folder currently contains the Markdown teaching plan for the missing Unit 05. Suggested lesson files can be added as the unit is developed.

| File or Folder | Purpose |
|---|---|
| `README.md` | Unit overview, sequence bridge, learning goals, suggested structure, and teaching plan. |
| `analysis_notes.md` | Suggested student-written summary of findings, data quality problems, and next steps. |
| `analyze_project_data.py` | Suggested script for loading, cleaning, and summarizing Project 1 data. |
| `data/raw_sample.csv` | Suggested raw sample data copied or exported from Project 1. |
| `data/cleaned_sample.csv` | Suggested cleaned version of the sample data. |
| `tests/test_analysis_helpers.py` | Suggested tests for summary and cleaning helper functions. |

## Seamless Connection From Earlier Units

| Earlier Unit | Skill Students Bring Into Unit 05 | How Unit 05 Reuses It |
|---|---|---|
| Unit 01: `.py` files | Functions, scripts, and `main()` workflow | Put analysis steps in a runnable script instead of only in a notebook. |
| Unit 02: library design | Reusable functions, classes, and data models | Keep cleaning and summary logic reusable instead of copying code into every report. |
| Unit 03: command line, Git, and `venv` | Terminal commands, project folders, dependency files, and commits | Run analysis scripts from the terminal and track data-processing changes with Git. |
| Unit 04: testing, debugging, logging, JSON, and CSV | Safer code, tests, logs, and saved data | Validate data, test summary functions, and load the JSON or CSV files from Project 1. |
| Project 1: structured CLI app | A practical application with stored records | Use real project data as the source for cleaning and analysis. |

## Seamless Connection To Later Units

| Later Unit | What Unit 05 Provides | Why It Helps |
|---|---|---|
| Unit 06 Part 1: Visualization and Reports | Cleaned data and summary tables | Charts become easier because data is already organized and meaningful. |
| Unit 06 Part 2: Streamlit Basics | Reusable summary functions and clean display data | The dashboard can focus on interaction and presentation instead of messy data handling. |
| Unit 07 Part 1: API Basics | A pattern for reading, validating, and summarizing structured data | Students can apply the same pattern to JSON returned by APIs. |
| Unit 07 Part 2: API App with Error Handling | Data quality habits and fallback thinking | Students are better prepared for missing fields, failed requests, and inconsistent external data. |
| Capstone Planning and Build | Metrics, questions, data flow, and analysis notes | Students can choose stronger capstone features because they understand their data pipeline. |

## Suggested Folder Structure

```text
unit05_data_analysis_bridge/
  README.md
  analysis_notes.md
  analyze_project_data.py
  data/
    raw_sample.csv
    cleaned_sample.csv
  tests/
    test_analysis_helpers.py
```

If students are continuing directly from Project 1, they may also place the analysis files inside their existing project:

```text
project01_structured_cli_app/
  main.py
  tracker/
    __init__.py
    models.py
    storage.py
    reports.py
    analysis.py
  data/
    raw_records.csv
    cleaned_records.csv
  tests/
    test_analysis.py
```

## Suggested 2-Hour Teaching Plan

| Time | Activity | Purpose | Output |
|---:|---|---|---|
| 0:00-0:10 | Review Project 1 data | Remind students where their JSON or CSV data comes from | Identify one raw data file to analyze |
| 0:10-0:30 | Inspect records | Find missing, duplicated, invalid, or inconsistent values | Short list of data quality problems |
| 0:30-0:55 | Clean data | Fix or remove records using clear rules | Cleaned dataset saved separately from raw data |
| 0:55-1:20 | Write summary functions | Create totals, counts, averages, or grouped summaries | Reusable analysis helpers |
| 1:20-1:35 | Add one test | Check that one summary function returns the expected result | Basic `pytest` test for analysis logic |
| 1:35-1:50 | Write analysis notes | Explain what the data shows and what is still uncertain | `analysis_notes.md` draft |
| 1:50-2:00 | Preview next unit | Connect summaries to charts, reports, Streamlit, APIs, and capstone metrics | Clear bridge to Unit 06 |

## Practice Tasks

1. Choose one JSON or CSV file from Project 1.
2. Write down three questions the data could answer.
3. Find at least two data quality problems.
4. Create a cleaned version of the file without overwriting the raw file.
5. Write one function that returns a useful summary metric.
6. Write one `pytest` test for that summary function.
7. Create a short `analysis_notes.md` file with:
   - what data was used;
   - what was cleaned;
   - one important summary;
   - one limitation or warning;
   - one chart or dashboard idea for Unit 06.

## Best Practice Checklist

Before moving to Unit 06, check that:

- raw data and cleaned data are stored separately;
- cleaning rules are written clearly;
- summary logic is inside reusable functions;
- at least one important summary function has a test;
- analysis code does not break the original CLI project;
- the summary output can become a chart, table, report section, or dashboard value;
- students can explain how this data could support their capstone project.
