---
title: iterations
chapter: Control Flow
chapter_number: 3
lesson_number: 1
---

# Iteration
Iteration (loops) allow a program to repeat work: processing items, accumulating results,
or running until a condition changes. Use loops for repeated tasks; prefer vectorized
operations (Matlab, NumPy) when they are simpler and faster.

=== "Python"

    ```python
    # for over a list
    names = ["Alice", "Bob", "Carol"]
    for name in names:
        print(name)

    # range-based loop
    for i in range(5):  # 0..4
        print(i)

    # enumerate to get index and value
    for i, v in enumerate(names):
        print(i, v)

    # while loop
    n = 5
    while n > 0:
        print(n)
        n -= 1

    # break and continue
    for x in [1, -1, 3, 0]:
        if x < 0:
            continue
        if x == 0:
            break
        print(x)
    ```

=== "Matlab"

    ```matlab
    % for loop with range (1-based)
    for i = 1:5
      disp(i)
    end

    % for over array (column iteration)
    A = [10 20 30];
    for v = A
      disp(v)
    end

    % while loop
    n = 5;
    while n > 0
      disp(n)
      n = n - 1;
    end

    % break and continue
    for x = [1 -1 3 0]
      if x < 0
        continue
      end
      if x == 0
        break
      end
      disp(x)
    end

    % Vectorized alternative example (prefer when possible)
    vals = [1 2 3 4]; weights = [0.1 0.2 0.3 0.4];
    s = sum(vals .* weights);  % no explicit loop
    ```

## Gotchas
- Indexing origin: Python is 0-based; Matlab is 1-based. Off-by-one errors are common.
- Modifying a list/array while iterating it can lead to skipped elements or unexpected behavior.
- `while` loops can become infinite; ensure the loop condition will eventually be false.
- Prefer vectorized operations in Matlab and NumPy for performance and clarity when operating on arrays.

## Exercises
1. Use a `for` loop in Python to compute the sum of numbers 1 through 100.
2. Use `enumerate` to print the index and value of each element in a list.
3. In Matlab, write a `for` loop that computes the cumulative sum of a vector.
4. Rewrite a `while` loop that counts down from 10 to 1 into a `for` loop (Python).
5. Find the first negative number in a list using a loop and `break`.
