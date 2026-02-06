---
title: operators
chapter: Expressions
chapter_number: 2
lesson_number: 2
---

# Operators
Operators combine values and produce new values. They are the core of expressions and
come in several categories: arithmetic, comparison, logical, bitwise, and assignment.

Understanding operator precedence (which operation runs first) and associativity 
(left/right) helps avoid subtle bugs; use parentheses to make intent explicit.

## Operator categories
Below are common categories of operators you will encounter. Each category describes
what the operators do and gives short examples — language syntax varies, but the
concepts are the same.

- Basic math (arithmetic)
  - Purpose: perform numeric calculations (addition, subtraction, multiplication,
    division, modulus, exponentiation).
  - Examples: `+`, `-`, `*`, `/`, `//` (floor division, language-specific), `%`, `**`.
  - Notes: some languages distinguish integer vs floating division; some have
    special operators for matrix or element-wise operations.

- Assignment
  - Purpose: store a value into a variable.
  - Examples: `=` (simple assignment), and related forms below.

- Augmented assignment
  - Purpose: combine an operation with assignment for conciseness and sometimes
    performance.
  - Examples: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`. Equivalent to `x = x + y` but
    shorter and, in some languages, may avoid extra temporaries.

- Logical
  - Purpose: combine or invert boolean values.
  - Examples: `and`, `or`, `not` (language-specific), sometimes `&&`, `||`, `!`.
  - Notes: logical operators may short-circuit (skip evaluating the right-hand
    side) in many languages — this is important when the right-hand side has
    side effects or expensive computations.

- Bitwise
  - Purpose: operate on individual bits of integer values.
  - Examples: `&` (and), `|` (or), `^` (xor), `~` (not), `<<` (left shift), `>>` (right shift).
  - Notes: bitwise operators behave differently from logical operators and do not
    short-circuit; they are useful in low-level programming and some numeric tricks.

- Membership and identity (where applicable)
  - Purpose: test whether a value is contained in a collection (membership) or whether
    two references are the same object (identity).
  - Examples: `in`, `not in`, `is`, `is not` (Python); other languages have
    similar constructs or library functions.

- Precedence and associativity
  - Purpose: determine the order in which operators are applied when several appear
    in one expression.
  - Notes: multiplication has higher precedence than addition in most languages
    (`1 + 2 * 3 == 7`), and parentheses `()` override precedence. When in doubt,
    use parentheses to make intent explicit.


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
1. **Division differences**: Python `/` always produces a float; `//` is floor 
   division.  Matlab `/` and `\` relate to matrix right- and left-division  (they 
   are not simple scalar integer divisions).
2. **Element-wise vs matrix operations**: Matlab distinguishes `*` (matrix multiply) 
   from `.*` (element-wise). A common bug is mixing them when operating on arrays.
3. **Short-circuiting**: `and`/`or` in Python short-circuit (right-hand side may not 
   be  evaluated); bitwise operators `&`/`|` do not short-circuit and operate on 
   bits or element-wise booleans (NumPy).
4. **Operator precedence** can be surprising; parentheses improve readability and 
   correctness.
