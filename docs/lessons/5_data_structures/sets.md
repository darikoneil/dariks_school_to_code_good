---
title: sets
chapter: Data Structures
chapter_number: 5
lesson_number: 4
---

# Sets
Sets represent unordered collections of unique elements. They are useful for deduplication,
membership tests, and set operations (union, intersection, difference).

=== "Python"

    ```python
    s = {1, 2, 3}
    s.add(4)
    s.discard(2)
    print(3 in s)  # membership

    # Set operations
    a = {1,2,3}
    b = {3,4,5}
    print(a & b)  # intersection
    print(a | b)  # union
    print(a - b)  # difference
    ```

=== "Matlab"

    ```matlab
    % Unique and set operations
    A = [1 2 3 2];
    U = unique(A);        % [1 2 3]
    B = [3 4 5];
    inter = intersect(U, B);
    uni = union(U, B);
    diff = setdiff(U, B);
    ```

## Gotchas
- Sets are unordered; you cannot rely on iteration order.
- Elements must be hashable/eligible for set membership (immutable) in Python.
- Matlab set functions work on arrays and return sorted unique results.
