---
title: conditionals
chapter: Control Flow
chapter_number: 3
lesson_number: 0
---

# Conditionals
Conditionals let programs choose different actions depending on values or conditions.
They are the foundation of branching logic: `if` a condition holds, do something; `else` do something else.

Conditionals use boolean expressions (see the Comparisons lesson) and short-circuiting logic.

=== "Python"

    ```python
    # Simple if
    score = 75
    if score >= 60:
        print("pass")

    # if / else
    x = 7
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

    # if / elif / else chain
    n = -1
    if n < 0:
        print("negative")
    elif n == 0:
        print("zero")
    else:
        print("positive")

    # Truthiness
    items = []
    if items:
        print("has items")
    else:
        print("empty")

    # Ternary expression
    result = "yes" if score > 50 else "no"
    ```

=== "Matlab"

    ```matlab
    % Simple if
    score = 75;
    if score >= 60
      disp('pass')
    end

    % if / else
    x = 7;
    if mod(x,2) == 0
      disp('even')
    else
      disp('odd')
    end

    % if / elseif / else
    n = -1;
    if n < 0
      disp('negative')
    elseif n == 0
      disp('zero')
    else
      disp('positive')
    end

    % Check for empty arrays
    A = [];
    if ~isempty(A)
      disp('has items')
    else
      disp('empty')
    end
    ```

## Gotchas
- Python uses indentation to delimit blocks; Matlab uses `end`. Mixing styles causes syntax errors.
- In Matlab `=` is assignment and `==` is comparison; accidentally using `=` in a conditional will error or assign.
- Truthiness: empty containers are Falsey in Python, and `isempty` is the usual check in Matlab.
- Order matters in `elif`/`elseif` chains — the first matching branch runs.

## Exercises
1. Write a Python function that returns "even" or "odd" for an integer input using an `if`/`else`.
2. In Python, write an `if`/`elif`/`else` that labels an integer as "negative", "zero", or "positive".
3. In Matlab, write a conditional that prints "small", "medium", or "large" for values less than 10, between 10 and 100 (inclusive), and greater than 100.
