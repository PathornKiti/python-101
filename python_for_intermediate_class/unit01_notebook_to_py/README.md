# Unit 01: From Notebook to `.py` Files

## Purpose

This unit helps students move from exploratory notebook work to reusable Python scripts.

A Jupyter notebook (`.ipynb`) is excellent for learning, experimenting, visualizing data, and explaining steps with Markdown. A Python script (`.py`) is better when the same logic needs to be reused, tested, automated, imported, or shared as part of a real project.

## Learning Goals

By the end of this unit, students should be able to:

- explain the difference between notebook-style code and script-style code;
- identify which parts of a notebook should become functions;
- move repeated logic into a `.py` file;
- protect runnable script code with `if __name__ == "__main__":`;
- run a Python file from the terminal;
- keep notebooks clean by importing functions from scripts.

## Files in This Folder

| File | Purpose |
|---|---|
| `unit01_notebook_to_py.ipynb` | Lesson notebook with Markdown explanations, examples, and practice tasks. |
| `notebook_to_py_example.py` | Script version of the lesson example showing best-practice structure. |

## Why Move from `.ipynb` to `.py`?

Move notebook code into `.py` files when the code becomes important enough to reuse.

Common reasons include:

1. **Reusability**: functions in `.py` files can be imported by many notebooks, scripts, or apps.
2. **Testing**: scripts and functions are easier to test with tools such as `pytest`.
3. **Automation**: `.py` files can run from the terminal, a scheduler, or another program.
4. **Version control**: `.py` files are easier to review in Git because changes are plain text.
5. **Project structure**: real applications are usually organized into modules, packages, tests, and entry-point scripts.
6. **Cleaner notebooks**: notebooks can focus on explanation, exploration, and results instead of holding every helper function.

## Recommended Workflow

1. Start in a notebook when exploring a new idea.
2. Find code that is repeated, stable, or important.
3. Convert that code into named functions.
4. Move the functions into a `.py` file.
5. Add docstrings, type hints, and clear variable names.
6. Add a `main()` function for the script workflow.
7. Add `if __name__ == "__main__": main()` so the file can be imported safely.
8. Import the functions back into the notebook when you need explanation, charts, or a report.

## How to Run the Example Script

From the repository root, run:

```bash
python python_for_intermediate_class/unit01_notebook_to_py/notebook_to_py_example.py
```

If your computer uses `python3`, run:

```bash
python3 python_for_intermediate_class/unit01_notebook_to_py/notebook_to_py_example.py
```

## Best Practice Checklist

Before moving notebook code into a `.py` file, check that your code has:

- meaningful function names;
- small functions with one clear job;
- parameters instead of hard-coded values;
- return values instead of unnecessary printing;
- docstrings explaining purpose, inputs, and outputs;
- type hints where helpful;
- no hidden notebook-only variables;
- a `main()` function if the file is meant to run as a script;
- example usage or tests.
