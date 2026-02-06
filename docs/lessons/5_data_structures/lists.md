---
title: lists
chapter: Data Structures
chapter_number: 5
lesson_number: 0
---

# Lists
Lists (also called arrays or sequences in some languages) are ordered collections of values.
They are useful when you need an indexed, iterable container that can grow or shrink.

=== "Python"

    ```python
    # Creation
    lst = [1, 2, 3]
    empty = []

    # Indexing and slicing
    first = lst[0]
    tail = lst[1:]

    # Mutating
    lst.append(4)
    lst[1] = 20

    # Comprehensions
    squares = [x*x for x in range(5)]

    # Iteration
    for i, v in enumerate(lst):
        print(i, v)
    ```

=== "Matlab"

    ```matlab
    % Row vector as a list
    lst = [1 2 3];
    empty = [];

    % Indexing (1-based)
    first = lst(1);
    tail = lst(2:end);

    % Grow by concatenation
    lst = [lst 4];

    % Iterate
    for i = 1:numel(lst)
      disp([i lst(i)])
    end
    ```

## Gotchas
- Lists are mutable in Python; assigning one list to another name creates a shared reference.
- Slicing in Python creates a shallow copy; modifying the slice doesn't change the original list.
- Matlab vectors are 1-based and are arrays by default; use cell arrays `{}` for heterogeneous collections.
- Avoid using mutable objects as default function arguments in Python.
