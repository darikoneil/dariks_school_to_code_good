---
title: scripts vs functions
chapter: Functions & Scripts
chapter_number: 4
lesson_number: 3
---

# Scripts vs Functions
Scripts are sequences of statements executed top-to-bottom; functions encapsulate behavior
with parameters and (optionally) return values. Prefer functions for reusable logic; use
scripts for simple one-off tasks or as program entrypoints.

=== "Python"

    ```python
    # script: top-level code executed on import/run
    print('this runs when the file is executed')

    # function: encapsulated behavior
    def main():
        print('main called')

    if __name__ == '__main__':
        main()
    ```

=== "Matlab"

    ```matlab
    % script.m contains top-level statements and affects the base workspace
    a = 1;
    disp(a)

    % function files define functions and have their own local workspace
    function out = myfunc(x)
      out = x + 1;
    end
    ```

## Gotchas
- In Python, top-level code runs on import; guard execution with `if __name__ == '__main__'`.
- Matlab scripts operate in the base workspace and can unintentionally overwrite variables; prefer functions for reusable code.
- Use functions for unit-testable logic and scripts for orchestration.

## Exercises
1. Convert a small script that prints numbers 1..5 into a function that returns a list of those numbers.
2. Write a Python module with a `main()` function and the `if __name__ == '__main__'` guard.
3. In Matlab, show how a variable defined in a script becomes visible in the base workspace but remains local in a function.

