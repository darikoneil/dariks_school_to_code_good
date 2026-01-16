---
title: variables
chapter: Expressions
chapter_number: 2
lesson_number: 1
---

# Variables
Variables are names that refer to values. Assigning a variable binds a name to a value; later
references to the name use the bound value. Variables make programs readable and let us reuse
computed results.

Key ideas:
- Assignment creates or updates a binding (e.g., `x = 3`).
- A name does not permanently carry a type in some languages — the value has a type.
- Mutability: some objects can be changed in-place (lists/arrays), others cannot (tuples, numbers).

=== "Python"

    ```python
    # Simple assignment
    x = 10

    # Multiple assignment / unpacking
    a, b = 1, 2
    a, b = b, a  # swap without a temp variable

    # Rebinding and dynamic typing
    x = 'now a string'

    # Type hints (optional)
    y: int = 5

    # Mutability example
    lst = [1, 2]
    other = lst
    other.append(3)
    print(lst)  # [1, 2, 3] - both names refer to same list

    # Avoid using mutable defaults
    def f(items=None):
        if items is None:
            items = []
        items.append(1)
        return items
    ```

=== "Matlab"

    ```matlab
    % Assignment
    x = 10;

    % Multiple assignment is usually done element-wise or via arrays
    a = 1; b = 2;

    % Variables are workspace bindings; types are often arrays/matrices
    v = [1 2 3];

    % Passing arrays to functions copies or shares depending on the operation (MATLAB uses copy-on-write)
    ```

## Gotchas
- Naming rules: names usually must start with a letter or underscore and cannot be a reserved keyword.
- Shadowing: avoid using names that shadow built-ins (e.g., `list`, `str`, `sum`).
- Mutable vs immutable: unexpected sharing happens when multiple names reference the same mutable object.
- Globals and scope: modifying global variables inside functions requires explicit declarations in many languages.

## Exercises
1. In Python, swap two variables `a` and `b` in a single line without using a temporary variable.
2. Demonstrate with code that lists are mutable by showing two references to the same list and mutating one.
3. In Matlab, create a variable `M` as a 3x3 identity matrix and assign it to `N`; then change one element of `N` and observe `M` (note MATLAB's copy-on-write behavior).
