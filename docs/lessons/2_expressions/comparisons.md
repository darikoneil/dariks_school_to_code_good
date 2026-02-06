---
title: comparisons
chapter: Expressions
chapter_number: 2
lesson_number: 3
---

# Comparisons
Comparisons (also called relational operators) let programs decide how values relate to each other.
They produce boolean results (true/false) and are the basic building blocks for conditionals and filters.

Common comparison operators:

- `==`  equal to
- `!=` or `~=` not equal to (Matlab uses `~=`)
- `<`   less than
- `>`   greater than
- `<=`  less than or equal to
- `>=`  greater than or equal to
- 'is'  identity comparison (Python only)
- 'is not'  identity negation (Python only)
- 'in'  membership test (Python only)
- ':=' assignment (not a comparison, but often confused with `==`)

- Comparison
  - Purpose: compare two values and produce a boolean result.
  - Examples: `==`, `!=` (or `~=`), `<`, `<=`, `>`, `>=`.
  - Notes: comparison operators are used in conditionals and filtering.


=== "Python"

    ```python
    # Basic comparisons
    a = 5
    b = 3
    print(a == b)  # False
    print(a != b)  # True
    print(a > b)   # True

    # Chained comparisons
    x = 4
    print(1 < x <= 10)  # True (evaluates as 1 < x and x <= 10)

    # 'is' checks identity, not equality
    s1 = "hello"
    s2 = "hello"
    print(s1 == s2)  # True (same contents)
    print(s1 is s2)  # May be True or False depending on interning (identity)

    # Comparing different types can be surprising
    print(0 == False)    # True (bool is a subclass of int)
    print([] == False)   # False
    ```

=== "Matlab"

    ```matlab
    % Basic comparisons
    a = 5;
    b = 3;
    disp(a == b)   % 0 (false)
    disp(a ~= b)   % 1 (true)
    disp(a > b)    % 1 (true)

    % Element-wise comparisons for arrays
    A = [1, 2, 3];
    B = [1, 0, 4];
    C = A > B;     % [0 1 0]

    % Range checks
    x = 4;
    disp(1 < x && x <= 10) % true (logical short-circuit with scalars)
    ```

## Gotchas
1. **Floating-point comparisons**: exact equality is fragile (e.g., `0.1 + 0.2 == 0.3` 
   may be False). Prefer a tolerance (abs(a-b) < eps).
2. **Identity vs equality**: `is` (Python) checks object identity, not value equality.
3. **Chained comparisons**: are evaluated left-to-right but are concise and useful; 
   beware when mixing side-effecting expressions.
4. **Type coercion**: some languages coerce types during comparison (Python treats 
   bools as ints; other languages differ).
5. **Array comparisons**: in Matlab and NumPy, comparisons on arrays produce 
   element-wise boolean arrays — make sure to reduce with `all()`/`any()` when needed.