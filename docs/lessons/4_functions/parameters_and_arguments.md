---
title: parameters and arguments
chapter: Functions & Scripts
chapter_number: 4
lesson_number: 1
---

# Parameters and Arguments
Parameters name the inputs a function accepts; arguments are the actual values passed.
Understanding positional, keyword (named), default, and variadic parameters makes APIs flexible.

=== "Python"

    ```python
    def f(a, b=2, *args, **kwargs):
        print(a, b, args, kwargs)

    # Call examples
    f(1)
    f(1, 3)
    f(1, 3, 4, 5, x=10)

    # Keyword-only parameters (Python 3)
    def g(a, *, verbose=False):
        if verbose:
            print(a)
    ```

=== "Matlab"

    ```matlab
    % Matlab functions accept positional arguments; use varargin for variable inputs
    function out = f(a, b, varargin)
      disp(a);
      if ~isempty(varargin)
        disp(varargin{1})
      end
    end

    % Name-value pairs are often handled via parser or struct
    ```

## Gotchas
- Default parameter values in Python are evaluated once; avoid mutable defaults.
- Matlab does not have keyword arguments by default; name-value pairs are passed as varargin and parsed manually.
- Be explicit about parameter types and document expected shapes for array inputs.

## Exercises
1. Write a Python function with a default mutable argument and fix it using `None`.
2. Create a Python function that accepts `*args` and returns their product.
3. In Matlab, write a function that accepts variable inputs and prints how many extra arguments were provided.

