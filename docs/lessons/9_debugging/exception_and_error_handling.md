---
title: Exception & Error Handling
chapter: Debugging
chapter_number: 9
lesson_number: 2
---

# Exception & Error Handling
Handling exceptions lets your program respond to unexpected conditions without crashing.

## try / except / finally

```python
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")
else:
    print("Parsed OK")
finally:
    print("Always runs")
```

## Raising Exceptions
Use `raise` to signal an error:

```python
if value < 0:
    raise ValueError("value must be non-negative")
```

## Custom Exceptions
Create a specific exception type for domain errors:

```python
class ValidationError(Exception):
    pass

raise ValidationError("bad input")
```

## Best Practices
- Catch specific exception types.
- Log errors with context.
- Use `finally` or context managers for cleanup.

## Exercises
1. Wrap a file open and parse operation in try/except and return a default value on failure.
2. Define a custom exception `ConfigurationError` and raise it when a required setting is missing.

