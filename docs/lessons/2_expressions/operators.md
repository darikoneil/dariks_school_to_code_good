---
title: operators
chapter: Expressions
chapter_number: 2
lesson_number: 2
---

# Operators
Operators combine values and produce new values. They are the core of expressions and
come in several categories: arithmetic, comparison, logical, bitwise, and assignment.

Understanding operator precedence (which operation runs first) and associativity (left/right)
helps avoid subtle bugs; use parentheses to make intent explicit.

=== "Python"

    ```python
    # Arithmetic
    a = 7
    b = 3
    print(a + b)   # 10
    print(a - b)   # 4
    print(a * b)   # 21
    print(a / b)   # 2.333...
    print(a // b)  # 2 (floor division)
    print(a % b)   # 1 (remainder)
    print(a ** b)  # 343 (exponent)

    # Augmented assignment
    x = 2
    x += 3  # x == 5

    # Logical operators
    print(True and False)  # False
    print(True or False)   # True
    print(not True)        # False

    # Bitwise (integers)
    print(5 & 3)  # 1
    print(5 | 3)  # 7
    print(5 ^ 3)  # 6

    # Precedence example
    print(1 + 2 * 3)       # 7
    print((1 + 2) * 3)     # 9
    ```

=== "Matlab"

    ```matlab
    % Arithmetic and matrix operations
    a = 7;
    b = 3;
    disp(a + b)   % 10
    disp(a - b)   % 4
    disp(a * b)   % 21 (matrix multiply for scalars is same)
    disp(a / b)   % 7/3
    disp(a ^ b)   % 343 (power)

    % Element-wise operators (use . for element-wise)
    A = [1 2; 3 4];
    B = [2 0; 1 2];
    C = A .* B;  % element-wise multiply
    D = A * B;   % matrix multiply

    % Logical operators
    disp(true && false)
    disp(true || false)
    disp(~true)

    % Precedence: use parentheses to be clear
    ```

## Gotchas
- Division differences: Python `/` always produces a float; `//` is floor division. Matlab `/` and `\` relate to matrix right- and left-division (they are not simple scalar integer divisions).
- Element-wise vs matrix operations: Matlab distinguishes `*` (matrix multiply) from `.*` (element-wise). A common bug is mixing them when operating on arrays.
- Short-circuiting: `and`/`or` in Python short-circuit (right-hand side may not be evaluated); bitwise operators `&`/`|` do not short-circuit and operate on bits or element-wise booleans (NumPy).
- Operator precedence can be surprising; parentheses improve readability and correctness.

## Exercises
1. In Python, compute ((2 + 3) * 4) ** 2 and explain each step of precedence.
2. In Matlab, given `A = [1 2; 3 4]`, compute element-wise square and matrix square and compare the results.
3. Write a short Python loop that uses `+=` to accumulate a running total of numbers 1 through 10.
