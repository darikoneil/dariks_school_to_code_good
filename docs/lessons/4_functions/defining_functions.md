---
title: defining functions
chapter: Functions & Scripts
chapter_number: 4
lesson_number: 0
---

# Defining Functions
Functions package behavior into reusable units with a name, parameters, and a body.
They improve readability, avoid repetition, and make testing simpler.

=== "Python"

    ```python
    def greet(name):
        return f"Hello, {name}"

    # Multiple returns
    def divmod_pair(a, b):
        return a // b, a % b
    q, r = divmod_pair(7, 3)

    # Docstring
    def add(a, b):
        """Return the sum of a and b."""
        return a + b
    ```

=== "Matlab"

    ```matlab
    % Define a function in its own file (greet.m) or as a local function
    function s = greet(name)
      s = ["Hello, " name];
    end

    % Multiple outputs
    function [q, r] = divmod_pair(a, b)
      q = floor(a / b);
      r = mod(a, b);
    end
    ```

## Gotchas
- In Python, functions are first-class values (they can be passed around and assigned).
- Matlab functions usually live in their own files or as local/subfunctions; be aware of file naming conventions.
- Keep functions small and focused — prefer many small functions to one large function.

## Exercises
1. Write a Python function `square(x)` that returns x squared.
2. Write a Matlab function that takes a vector and returns its mean and standard deviation.
3. In Python, add a docstring to a function and show how to access it with `help()`.

