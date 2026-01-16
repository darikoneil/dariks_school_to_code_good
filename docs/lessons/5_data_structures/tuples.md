---
title: tuples
chapter: Data Structures
chapter_number: 5
lesson_number: 1
---

# Tuples
Tuples are ordered, immutable collections. They are useful when you want a fixed sequence
that should not change (for example, coordinates or records).

=== "Python"

    ```python
    # Creation
    t = (1, 2, 3)
    single = (1,)  # trailing comma for single-element tuple

    # Indexing
    first = t[0]

    # Immutable: methods that would mutate return new values
    s = (1, 2) + (3,)

    # Useful for unpacking
    x, y, z = t
    ```

=== "Matlab"

    ```matlab
    % MATLAB does not have a tuple type; use fixed-size vectors or cell arrays for heterogenous data
    t = [1 2 3];  % numeric tuple-like
    c = {"a", 1, true};  % heterogeneous cell array
    ```

## Gotchas
- Tuples are immutable in Python; attempting to assign to an index raises an error.
- Use tuples as keys in dictionaries when you need composite keys.
- In Matlab, cell arrays can hold heterogeneous types similar to tuples but use different indexing (`{}` vs `()`).

## Exercises
1. Create a tuple of three strings and unpack them into variables.
2. Use a tuple as a dictionary key in Python to count occurrences of coordinate pairs.
3. In Matlab, create a cell array with mixed types and access the second element.

