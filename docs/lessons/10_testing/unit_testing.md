---
title: Unit Testing
chapter: Testing
chapter_number: 10
lesson_number: 1
---

# Unit Testing
Unit tests check small units of code in isolation. They should be fast and deterministic.

## Principles
- Test one behavior per test.
- Arrange, Act, Assert structure.
- Use fixtures to set up and tear down repeated state.

## Example (pytest)

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
```

Run with:

```bash
pytest -q
```

## Gotchas
- Tests that depend on external services are brittle (use mocks).
- Flaky tests (time-dependent, order-dependent) reduce confidence.

## Exercises
1. Write unit tests for a `divide(a, b)` function, including a test for division by zero using pytest's `raises`.
2. Convert a simple class into testable pieces and write tests for its public methods.

