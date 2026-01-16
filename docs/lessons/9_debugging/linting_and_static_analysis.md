---
title: Linting and Static Analysis
chapter: Debugging
chapter_number: 9
lesson_number: 4
---

# Linting and Static Analysis
Linters and static analyzers help detect style issues, bugs, and anti-patterns before runtime.

## What They Do
- Enforce style conventions (PEP8 for Python).
- Detect possible errors (unused variables, unreachable code).
- Suggest improvements (complexity, typing).

## Popular Tools
- Python: `flake8`, `pylint`, `mypy` (static typing)
- JavaScript: `eslint`

Run a simple check with flake8:

```bash
flake8 path/to/file.py
```

## Interpreting Warnings
Not all warnings are errors — assess severity and fix relevant issues. Configure tool rules to match project preferences.

## Exercises
1. Run `flake8` on a small Python file and fix three reported issues.
2. Add `mypy` type hints to a function and demonstrate fixing a type mismatch reported by `mypy`.

