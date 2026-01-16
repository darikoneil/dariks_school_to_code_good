---
title: literals
chapter: Expressions
chapter_number: 2
lesson_number: 0
---

# Literals
Literals are fixed values written directly in source code. They represent concrete values
(rather than computations) and are the simplest form of expression.

Common literal categories:
- Numeric (integers, floats, scientific notation)
- String and character
- Boolean and null-like values (`True`/`False`, `None` / `[]`)
- Collection literals (lists, tuples, dictionaries, arrays)

=== "Python"

    ```python
    # Numeric literals
    a = 123
    b = 1_000_000   # underscores for readability
    c = 3.14
    d = 1e-3        # scientific notation

    # String literals
    s1 = 'single quoted'
    s2 = "double quoted"
    s3 = '''triple-quoted
    multi-line string'''
    raw = r"C:\path\to\file"  # raw string avoids escapes

    # Boolean and None
    flag = True
    nothing = None

    # Collection literals
    lst = [1, 2, 3]
    tpl = (1, 2)
    dct = {'a': 1, 'b': 2}
    ```

=== "Matlab"

    ```matlab
    % Numeric literals
    a = 123;
    b = 1e-3;      % scientific notation

    % Array and matrix literals
    v = [1 2 3];   % row vector
    M = [1 2; 3 4];

    % Strings / chars
    s = "hello";  % string array (newer MATLAB)
    c = 'c';        % character

    % Logical
    flag = true;
    empty = [];
    ```

## Gotchas
- Underscores in numeric literals are for readability and ignored by the parser in Python.
- Floating-point literals represent approximations; printing may show rounding artifacts (e.g., 0.1 + 0.2).
- Mutable default arguments: using collection literals as default parameter values in Python functions can cause surprising state sharing between calls. Prefer `None` and create a new collection inside the function.
- Matlab: `[1]` vs `1` — scalars are also 1x1 arrays; pay attention when indexing and when mixing row/column vectors.

## Exercises
1. In Python, create a triple-quoted string that spans three lines and contains both single and double quotes without needing escapes.
2. Write a Python function with a default argument `items=[]` and explain why this can be problematic; fix it.
3. In Matlab, define a 2x2 matrix literal and extract the second column.
