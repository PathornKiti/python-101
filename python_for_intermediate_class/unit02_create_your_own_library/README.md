# Unit 02: Create Your Own Library with a Data Model

## Purpose

This unit teaches students how to create a small reusable Python library and import it from another `.py` file or notebook.

In beginner Python, many programs are written in one file or one notebook. In intermediate Python, useful code is organized into a library so it can be reused by scripts, notebooks, tests, and applications.

## Learning Goals

By the end of this unit, students should be able to:

- explain what a Python module and package are;
- create a small library folder with `__init__.py`;
- write and import a reusable **function**;
- write and import a reusable **class**;
- write and import a reusable **data model** using `@dataclass`;
- use the same library from both a `.py` script and a `.ipynb` notebook;
- keep demo code separate from reusable library code.

## Files in This Folder

| File or Folder | Purpose |
|---|---|
| `unit02_create_your_own_library.ipynb` | Lesson notebook with explanations, examples, and practice tasks. |
| `demo_imports.py` | Runnable script that imports the function, class, and data model from the library. |
| `student_learning_library/` | Student-created library package used by the script and notebook. |
| `student_learning_library/__init__.py` | Package export file that makes imports easier. |
| `student_learning_library/learning_tools.py` | Main library module containing the function, class, and data model. |

## Key Vocabulary

| Word | Meaning |
|---|---|
| Module | A `.py` file that contains reusable Python code. |
| Package | A folder of Python modules, usually with an `__init__.py` file. |
| Function | Reusable action that accepts input and returns output. |
| Class | Blueprint for objects that combine data and behavior. |
| Data model | A structured object that represents data clearly. In this unit, the data model uses `@dataclass`. |
| Import | A statement that brings code from one module or package into another file. |

## Library Structure

This unit uses the following structure:

```text
unit02_create_your_own_library/
  README.md
  demo_imports.py
  unit02_create_your_own_library.ipynb
  student_learning_library/
    __init__.py
    learning_tools.py
```

The reusable code lives inside `student_learning_library/`. The demo script and notebook import from that library instead of copying the same code again.

## What the Library Exports

The package exports three kinds of objects:

```python
from student_learning_library import StudyLibrary, StudySession, estimate_study_points
```

| Imported object | Object type | Purpose |
|---|---|---|
| `estimate_study_points` | Function | Calculates simple study points from minutes and completion status. |
| `StudyLibrary` | Class | Stores study sessions and builds a progress report. |
| `StudySession` | Data model | Represents one study session with topic, minutes, and completion status. |

## How to Run the Script

From the repository root, run:

```bash
python python_for_intermediate_class/unit02_create_your_own_library/demo_imports.py
```

If your computer uses `python3`, run:

```bash
python3 python_for_intermediate_class/unit02_create_your_own_library/demo_imports.py
```

Expected output will look similar to this:

```text
First session points: 5

Study report for Maya
Sessions: 2
Total minutes: 60
Total points: 7
Completed topics: Python imports
```

## Practice Tasks

1. Add a new `StudySession` for another topic.
2. Mark the new session as completed and compare the points.
3. Add a method to `StudyLibrary` named `average_minutes()`.
4. Import the library in the notebook and create a report for your own name.
5. Create a second module in the package, such as `text_tools.py`, and export one function from it.

## Best Practice Checklist

Before calling your code a library, check that:

- reusable logic is inside functions, classes, or data models;
- demo code is separate from library code;
- imports work from another `.py` file;
- imports work from a notebook;
- names are clear and beginner-friendly;
- functions and methods have docstrings;
- data validation catches impossible values;
- `if __name__ == "__main__":` is used only in runnable scripts.
