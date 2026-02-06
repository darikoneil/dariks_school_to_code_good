---
title: Error Types
chapter: Debugging
chapter_number: 9
lesson_number: 1
---

# Error Types
Errors come in several flavors. Understanding their categories helps diagnose problems quickly.

## Categories
- Syntax Errors: mistakes in the code's structure that prevent parsing.
- Runtime Errors: occur while the program is running (exceptions).
- Semantic Errors (Logic Errors): program runs but produces incorrect results.

## Examples (Python)

```python
# SyntaxError: missing colon
# def foo()
#     pass

# Runtime / TypeError example
x = 'a'
# x + 1  # TypeError: can only concatenate str (not "int") to str

# Semantic error example
def average(items):
    return sum(items) / len(items)  # incorrect if len(items) == 0
```

## Using Tracebacks
Tracebacks show the call stack and the error message. Read from the bottom up to find the origin.

## Gotchas
- Catching too broad an exception (e.g., bare `except:`) can hide bugs.
