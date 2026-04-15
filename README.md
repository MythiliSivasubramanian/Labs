# Labs

Hands-on practice labs for building core programming, SQL, and NumPy skills through small focused exercises.

This folder is used for concept practice before moving into larger mini-projects and full projects in separate repositories.

## What is inside

### `01_Python_Labs/`
Python practice exercises focused on logic building and problem solving.

Topics currently included:
- List foundations
- String foundations
- Mixed Python practice
- A data-cleaning workflow scaffold split into small modules

Example practice areas:
- Removing duplicates
- Finding second-largest values
- Filtering even numbers
- Reversing and rotating lists
- String slicing and formatting
- Palindrome and anagram checks
- Word and character frequency analysis

### `02_SQL_Labs/`
SQL foundation exercises using simple practice tables such as `products`, `orders`, and `categories`.

Current work includes:
- Creating tables
- Inserting sample records
- Running basic `SELECT`, `WHERE`, and `ORDER BY` queries

### `03_Numpy/` and `03_Numpy_Labs/`
Introductory NumPy practice for working with arrays and reshaping data.

Current exercises include:
- Creating 1D arrays from Python lists
- Performing element-wise arithmetic
- Reshaping arrays into 2D forms
- Using `-1` in `reshape()` to let NumPy infer dimensions

## How to use these labs

- Open a lab file and run it section by section to understand the logic.
- Modify the sample inputs and observe how the output changes.
- Re-implement the same task using a different approach when possible.
- Use these labs as preparation before starting larger project work.

## Running the files

From the repository root:

```bash
python3 Labs/01_Python_Labs/strings_foundations.py
python3 Labs/01_Python_Labs/lists_foundations.py
python3 Labs/03_Numpy_Labs/01_foundations.py
```

For SQL practice, run the statements in:

```text
Labs/02_SQL_Labs/sql_foundations.sql
```

against a SQLite-compatible environment or your preferred SQL tool.

## Notes

- Some labs are iterative practice versions of the same topic.
- The `data_cleaning/` folder is currently structured as a step-by-step exercise scaffold, with some modules still left empty for future implementation.
