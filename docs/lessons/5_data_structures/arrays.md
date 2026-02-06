---
title: arrays
chapter: Data Structures
chapter_number: 5
lesson_number: 2
---

# Arrays
Arrays are collections of items of the same type, commonly used for numerical computation.
In Python, the `list` is general-purpose; `numpy` arrays provide efficient numeric arrays.
Matlab uses arrays (matrices) as its core data structure.

=== "Python"

    ```python
    # Python lists (general)
    lst = [1, 2, 3]

    # Numpy arrays (numeric)
    import numpy as np
    a = np.array([1, 2, 3])
    b = a * 2  # element-wise

    # Shape and indexing
    a.shape
    a[0]
    ```

=== "Matlab"

    ```matlab
    % Create arrays/matrices
    A = [1 2 3];       % row vector
    M = [1 2; 3 4];    % 2x2 matrix

    % Element-wise operations
    B = A .* 2;

    % Size and indexing
    s = size(M);
    v = M(1,2);
    ```

## Gotchas
- Numpy arrays enforce homogeneous types; mixing types will coerce to a common type.
- Matlab is 1-based indexing; Python/NumPy are 0-based.
- Be careful with shapes (row vs column) when multiplying matrices.
