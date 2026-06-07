# Intermediate Course: Practical Python Programming

This folder contains the standalone outline for the **Intermediate Course: Practical Python Programming**.

The course is for students who already know beginner Python concepts such as variables, conditions, loops, strings, files, lists, dictionaries, functions, NumPy basics, and basic classes.

The main goal is to move from notebook-based practice to real Python project development using `.py` files, folders, Git, virtual environments, tests, logs, data files, APIs, reports, and simple apps.

---

## Course Summary

| Item | Description |
|---|---|
| Course level | Intermediate |
| Estimated duration | 14 teaching weeks plus setup preparation |
| Estimated time | About 2 hours per week |
| Main format | Python scripts, modules, command line work, and small projects |
| Final outcome | Students can build a structured Python application, prepare data for presentation, and present it as a portfolio project |

By the end of this course, students should be able to:

- create and run Python projects outside notebooks
- organize code into folders, scripts, and reusable modules
- use VS Code as a development editor
- use the terminal for common project commands
- create and activate a Python virtual environment
- install packages with `pip`
- save dependencies in `requirements.txt`
- use Git for version control
- create a GitHub account and upload a project repository
- write basic unit tests
- add logging and error handling
- read and write JSON and CSV files
- create simple charts and reports
- build a simple Streamlit app
- call an external API and process JSON responses
- plan, build, and present an intermediate Python capstone project

---

## Unit Sequence Overview

The setup unit should be completed before the main course starts. The remaining units should be taught in order because each unit depends on the workflow and project structure from earlier units.

| Sequence | Week | Unit / Project | Topic | Main Output |
|---:|---:|---|---|---|
| 0 | Before Week 1 | Setup Preparation | VS Code, Python, Git, GitHub, and virtual environment basics | Student computer is ready for development |
| 1 | Week 1 | [Unit 01 Part 1](unit01_notebook_to_py/) | From Notebook to `.py` Files | A working Python script converted from notebook-style code |
| 2 | Week 2 | [Unit 02](unit02_create_your_own_library/) | Create Your Own Library with a Data Model | A reusable package imported by a script and notebook |
| 3 | Week 3 | [Unit 03](unit03_command_line/) | Command Line Basics | Students can navigate folders and run scripts from terminal |
| 4 | Week 4 | [Unit 04](unit04_venv_git/) | Git and Virtual Environment | A Git-tracked Python project with `venv` and `requirements.txt` |
| 5 | Week 5 | Unit 05 Part 1 | Error Handling and Debugging | Safer code using exceptions and debugging habits |
| 6 | Week 6 | Unit 05 Part 2 | Testing, Logging, JSON, and CSV | Basic tests, log file, and saved data files |
| 7 | Week 7 | Project 1 | Structured CLI Project | A command-line application using Units 01-05 |
| 8 | Week 8 | [Unit 06](unit06_data_analysis_bridge/) | Data Preparation and Analysis Bridge | Clean Project 1 data and prepare summaries for reports, charts, Streamlit, APIs, and capstone planning |
| 9 | Week 9 | Unit 07 Part 1 | Visualization and Reports | Charts and a written summary report |
| 10 | Week 10 | Unit 07 Part 2 | Streamlit Basics | A simple local Streamlit app |
| 11 | Week 11 | Unit 08 Part 1 | API Basics | A script that calls an API and reads JSON |
| 12 | Week 12 | Unit 08 Part 2 | API App with Error Handling | A small API-powered app with safer failures |
| 13 | Week 13 | Capstone Planning | Intermediate Capstone Design | Project plan, folder structure, feature list, and data flow |
| 14 | Week 14 | Capstone Build | Intermediate Capstone Project | Completed practical Python application and presentation |


---

## Available Unit Materials

| Unit | Folder | Materials |
|---|---|---|
| Unit 01 Part 1 | [`unit01_notebook_to_py/`](unit01_notebook_to_py/) | Notebook lesson, script example, and best-practice notes for moving from `.ipynb` to `.py` files. |
| Unit 02 | [`unit02_create_your_own_library/`](unit02_create_your_own_library/) | Notebook lesson, script example, and reusable package that exports a function, class, and data model. |
| Unit 03 | [`unit03_command_line/`](unit03_command_line/) | Command-line cheat sheet, first student-written CLI pattern, raw argument demo, and argparse examples that reuse the Unit 02 library. |
| Unit 04 | [`unit04_venv_git/`](unit04_venv_git/) | Detailed Markdown lesson for virtual environments, Git setup, step-by-step workflows, troubleshooting, and a command cheat sheet. |
| Unit 05 | Planned lesson folder | Error handling, debugging, testing, logging, JSON, and CSV lessons that prepare students for Project 1. |
| Unit 06 | [`unit06_data_analysis_bridge/`](unit06_data_analysis_bridge/) | Markdown lesson plan that connects the structured CLI project to visualization, Streamlit, APIs, and the capstone. |

## Setup Preparation: Step-by-Step

Complete this setup before Week 1. These steps are written for beginners who are moving into intermediate project work.

### Step 1: Install Python

1. Go to the official Python download page: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest stable Python 3 version for your operating system.
3. During installation on Windows, select **Add Python to PATH**.
4. Open a terminal and check the installation:

```bash
python --version
```

If `python` does not work, try:

```bash
python3 --version
```

### Step 2: Install VS Code

1. Go to the official VS Code download page: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download and install VS Code for your operating system.
3. Open VS Code.
4. Install the **Python** extension from Microsoft:
   - Open the Extensions panel.
   - Search for `Python`.
   - Choose the extension published by Microsoft.
   - Click **Install**.
5. Optional but recommended: install the **Pylance** extension for better autocomplete and code checking.

### Step 3: Install Git

1. Go to the official Git download page: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Download and install Git for your operating system.
3. Open a terminal and check the installation:

```bash
git --version
```

4. Set your Git username and email. Use the same email you plan to use for GitHub if possible:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### Step 4: Register for GitHub

1. Go to the GitHub sign-up page: [https://github.com/signup](https://github.com/signup)
2. Create an account with your email address.
3. Verify your email if GitHub asks you to do so.
4. Keep your username and password safe.
5. After registration, you can create repositories at: [https://github.com/new](https://github.com/new)

Students do not need advanced GitHub knowledge at the beginning. At first, they only need to know that GitHub is where they can store and share their code online.

### Step 5: Create a Course Folder

Create one folder for intermediate course projects. Example:

```bash
mkdir intermediate-python
cd intermediate-python
```

Inside this folder, each unit can have its own project folder:

```text
intermediate-python/
  unit01_notebook_to_py/
  unit02_create_your_own_library/
  unit03_command_line/
  unit04_venv_git/
  unit05_testing_logging_data/
  project01_structured_cli_app/
  unit06_data_analysis_bridge/
  unit07_visualization_streamlit/
  unit08_api_app/
  capstone_project/
```

### Step 6: Create a Virtual Environment

A virtual environment keeps project packages separate from the global Python installation.

Create a virtual environment:

```bash
python -m venv .venv
```

If your system uses `python3`, run:

```bash
python3 -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

After activation, the terminal usually shows `(.venv)` at the beginning of the command line.

### Step 7: Install Packages

Install packages only after the virtual environment is activated.

Common packages for this course:

```bash
pip install pytest pandas matplotlib requests streamlit
```

Save the package list:

```bash
pip freeze > requirements.txt
```

Later, another student or teacher can install the same packages with:

```bash
pip install -r requirements.txt
```

### Step 8: Open the Folder in VS Code

From inside the course folder, run:

```bash
code .
```

If `code .` does not work, open VS Code manually and choose **File > Open Folder**.

In VS Code:

1. Open the Command Palette.
2. Search for **Python: Select Interpreter**.
3. Choose the interpreter inside `.venv`.
4. Open a terminal inside VS Code.
5. Confirm that the terminal is using the virtual environment.

### Step 9: Start Git Tracking

Inside the project folder, initialize Git:

```bash
git init
```

Create a `.gitignore` file:

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

Check project status:

```bash
git status
```

Make the first commit:

```bash
git add .
git commit -m "Initial intermediate Python project setup"
```

### Step 10: Upload to GitHub Later

After students understand local Git basics, they can create a GitHub repository and connect it to the local project.

General flow:

1. Create a new repository at [https://github.com/new](https://github.com/new)
2. Copy the repository URL from GitHub.
3. Connect the local project to the GitHub repository:

```bash
git remote add origin YOUR_REPOSITORY_URL
```

4. Push the local project:

```bash
git branch -M main
git push -u origin main
```

Replace `YOUR_REPOSITORY_URL` with the actual repository link from GitHub.

---

## Detailed Teaching Plan

### Unit 00: Setup Preparation

**Goal:** Prepare the student's computer and development workflow.

**Topics:**

- Python installation
- VS Code installation
- VS Code Python extension
- Git installation
- GitHub registration
- project folders
- virtual environments
- package installation
- basic `requirements.txt`

**Practice:**

- Create a folder named `intermediate-python`.
- Create and activate `.venv`.
- Install `pytest`.
- Save `requirements.txt`.
- Open the folder in VS Code.

---

### Unit 01: Systematic Python Project Structure

**Goal:** Move from notebook-style work to structured Python files.

**Part 1: From Notebook to `.py` Files**

- compare notebook cells with script files
- create `main.py`
- run a script from VS Code
- use `if __name__ == "__main__"`
- separate input, processing, and output

**Part 2: Prepare for Library Design**

- identify helper logic that should move into a module
- choose clear names for reusable functions
- keep script workflow separate from reusable logic
- prepare for the package workflow in Unit 02

**Mini outcome:** A working script with functions that are ready to move into a student-created library.

---

### Unit 02: Create Your Own Library with a Data Model

**Goal:** Build a reusable package that can be imported by scripts and notebooks.

- create a package folder with `__init__.py`
- import a function from a student-created library
- import a class from a student-created library
- import a data model from a student-created library
- use `@dataclass` to model structured data
- keep demo code separate from reusable library code

**Suggested folder:**

```text
unit02_create_your_own_library/
  demo_imports.py
  unit02_create_your_own_library.ipynb
  student_learning_library/
    __init__.py
    learning_tools.py
```

**Mini outcome:** A small reusable package imported by both a `.py` script and a notebook.

---

### Unit 03: Command Line Basics

**Goal:** Learn how to use the terminal to navigate project folders and run Python scripts.

- open terminal
- understand current folder
- use `pwd`, `cd`, `mkdir`, and `dir` or `ls`
- run Python files from terminal
- pass simple command-line arguments
- use `sys.argv` and `argparse` for simple CLI inputs

**Materials:** [`unit03_command_line/`](unit03_command_line/) contains a command-line cheat sheet plus `sys.argv` and `argparse` demo scripts that reuse the Unit 02 library.

**Mini outcome:** Students can navigate folders and run Python scripts from the command line.

---

### Unit 04: Git and Virtual Environment

**Goal:** Manage Python projects with version control and isolated dependencies.

- understand why projects use Git
- use `git init`, `git status`, `git add`, and `git commit`
- create `.gitignore`
- create and activate `.venv`
- install packages with `pip`
- create `requirements.txt`

**Materials:** [`unit04_venv_git/`](unit04_venv_git/) contains the full lesson for Git, `.gitignore`, virtual environments, package installation, dependency files, troubleshooting, and a command cheat sheet.

**Mini outcome:** A Git-tracked project with a virtual environment and dependency file.

---

### Unit 05: Testing, Debugging, Logging, JSON, and CSV

**Goal:** Make programs easier to trust, debug, and maintain.

**Part 1: Error Handling and Debugging**

- read Python error messages
- identify common errors
- use `try`, `except`, and `finally`
- raise simple custom errors
- debug with print statements and VS Code debugger

**Part 2: Testing, Logging, JSON, and CSV**

- write simple tests with `pytest`
- test pure functions
- create log messages
- save data to JSON
- read data from JSON
- read and write CSV files

**Suggested folder:**

```text
unit05_testing_logging_data/
  app.py
  data_store.py
  tests/
    test_data_store.py
  data/
    sample.csv
```

**Mini outcome:** A small data program with tests, logs, and JSON or CSV persistence.

---

### Project 1: Structured CLI Project

**Goal:** Apply Units 01-05 in one practical command-line application.

**Possible project ideas:**

- personal expense tracker
- study task tracker
- small inventory manager
- book reading tracker
- simple grade calculator

**Required features:**

- organized project folders
- at least two Python modules
- command-line interaction
- JSON or CSV data storage
- input validation and error handling
- logging
- at least three unit tests
- `requirements.txt`
- Git commits during development

**Suggested folder:**

```text
project01_structured_cli_app/
  README.md
  main.py
  tracker/
    __init__.py
    models.py
    storage.py
    reports.py
  data/
  tests/
  requirements.txt
```

---

### Unit 06: Data Preparation and Analysis Bridge

**Goal:** Turn the CLI project data from Project 1 into clean, trustworthy summaries that can feed the reporting, Streamlit, API, and capstone units.

This unit is intentionally placed after Project 1 and before visualization so students do not jump from saving data directly to making charts. They first learn how to inspect, clean, summarize, and explain the data their own application produces.

**Connection from earlier units:**

- reuse the modules, data model, validation, logging, tests, JSON, and CSV files from Units 01-05 and Project 1
- read saved project data instead of creating disconnected sample data
- keep analysis code separate from input/output code so the project remains organized
- write one or two tests for summary functions before using them in reports

**Connection to later units:**

- create summary tables that become chart inputs in Unit 07 Part 1
- create cleaned datasets that can be displayed in Streamlit in Unit 07 Part 2
- prepare a reusable data-processing pattern before external API data arrives in Unit 08
- help students choose capstone metrics, questions, and data flow before building the final project

**Topics:**

- inspect JSON or CSV files created by the CLI project
- identify missing, duplicated, invalid, or inconsistent records
- clean data with plain Python first and optionally with `pandas` for tabular data
- create summary functions such as totals, counts, averages, top categories, and date-based summaries
- save a cleaned data file separately from raw data
- write a short analysis note explaining what the data shows and what still needs improvement

**Suggested folder:**

```text
unit06_data_analysis_bridge/
  README.md
  analysis_notes.md
  analyze_project_data.py
  data/
    raw_sample.csv
    cleaned_sample.csv
  tests/
    test_analysis_helpers.py
```

**Mini outcome:** A cleaned dataset, reusable summary functions, and a short analysis note that can become charts, reports, dashboards, API comparisons, or capstone metrics.

---

### Unit 07: Visualization, Reports, and Streamlit

**Goal:** Present project results in a clear visual format.

**Part 1: Visualization and Reports**

- summarize data with Python
- create basic charts with `matplotlib`
- create simple tables with `pandas`
- export or save chart images
- write a short report from program output

**Part 2: Streamlit Basics**

- install Streamlit
- create `app.py`
- display text, tables, and charts
- add simple inputs
- run a local Streamlit app

**Mini outcome:** A report script and a simple Streamlit dashboard.

---

### Unit 08: APIs and External Data

**Goal:** Connect Python projects to external data.

**Part 1: API Basics**

- understand what an API is
- use `requests.get`
- read response status codes
- parse JSON responses
- extract selected fields

**Part 2: API App with Error Handling**

- handle failed requests
- handle missing data
- keep API logic in a separate module
- save API results to JSON or CSV
- display API data in a simple report or Streamlit app

**Mini outcome:** A small app that fetches external data, saves it, and displays a useful summary.

---

### Unit 08: Intermediate Capstone Project

**Goal:** Build and present a complete practical Python application.

**Capstone requirements:**

- clear project purpose
- organized folder structure
- reusable modules
- virtual environment and `requirements.txt`
- Git repository
- data stored in JSON, CSV, or from an API
- error handling
- logging
- unit tests for important functions
- report, chart, or Streamlit interface
- final README explaining setup and usage

**Suggested capstone ideas:**

- weather dashboard
- personal finance report app
- study planner with progress charts
- movie or book search app using an API
- local business inventory and sales summary
- fitness tracker with charts

**Final presentation should include:**

1. Problem the project solves
2. Demo of the application
3. Folder structure explanation
4. Important code walkthrough
5. Testing evidence
6. What the student would improve next

---

## Recommended Teaching Order

Use this order to avoid confusing students:

1. Setup tools first: Python, VS Code, Git, GitHub, and virtual environment.
2. Teach `.py` scripts before command-line arguments.
3. Teach modules before larger folder structures.
4. Teach terminal basics before Git commands.
5. Teach virtual environments before installing third-party packages.
6. Teach `requirements.txt` immediately after installing packages.
7. Teach error handling before API calls.
8. Teach tests with small pure functions before testing larger applications.
9. Teach JSON and CSV before API persistence.
10. Teach visualization before Streamlit.
11. Teach basic API calls before API-powered apps.
12. Plan the capstone before students start coding.

---

## Student Checklist

Before starting the capstone, each student should be able to answer **yes** to these questions:

- Can I create and activate a virtual environment?
- Can I install a package with `pip`?
- Can I save dependencies to `requirements.txt`?
- Can I run a Python file from the terminal?
- Can I import a function from another Python file?
- Can I make a Git commit?
- Can I create a GitHub repository?
- Can I write at least one `pytest` test?
- Can I read and write JSON or CSV data?
- Can I create a simple chart?
- Can I call an API and read a JSON response?
- Can I explain my project folder structure?

