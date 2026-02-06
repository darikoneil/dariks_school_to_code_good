---
title: return values
chapter: Functions & Scripts
chapter_number: 4
lesson_number: 2
---

# Return Values
Functions can return values to their caller. Understanding how and when to return
values (vs. mutating inputs or printing) is key to writing reusable code.

=== "Python"

    ```python
    def add(a, b):
        return a + b

    # Multiple returns (tuples)
    def divmod_pair(a, b):
        return a // b, a % b

    q, r = divmod_pair(7, 3)

    # Returning None implicitly
    def noisy(a):
        print(a)
    x = noisy(5)  # x is None
    ```

=== "Matlab"

    ```matlab
    % Single return
    function s = greet(name)
      s = ["Hello, " name];
    end

    % Multiple outputs
    function [q, r] = divmod_pair(a, b)
      q = floor(a / b);
      r = mod(a, b);
    end

    % If a function has no outputs, calling it returns nothing
    ```

## Gotchas
- Returning mutable objects vs copying: returning a reference to a mutable object may allow callers to mutate internal state.
- Implicit `None` (Python) or no output (Matlab) can confuse callers expecting a value — document return types.
- Multiple outputs (Matlab) vs tuple unpacking (Python) have slightly different calling conventions.
