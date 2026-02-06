---
title: Statements
chapter: Control Flow
chapter_number: 3
lesson_number: 0
---
# Statements

A statement tells the computer to do something. Where an expression evaluates to a value, a statement performs an action: it assigns a value, controls the flow of execution, or produces an observable effect (like printing to the screen).

Although many languages keep a strict distinction between expressions and statements, some languages blur the line (for example, C-family assignment returns a value; Python's "walrus" operator `:=` introduces expression-style assignment). This lesson focuses on the statement-level constructs that structure programs.

## Why statements matter

- Statements organize program behavior: they change state, make decisions, and repeat work.
- Understanding statements is essential for controlling program flow, debugging, and reasoning about scope and side effects.
- Many bugs arise from incorrect ordering of statements or misunderstanding the effects of mutation.

## Simple statements

Simple statements are single-line units that perform a small action.

- Expression statements: an expression used as a statement (e.g., a function call whose return value is ignored).
- Assignment: binds a value to a name. In many beginner-focused materials this is written as `name = expression`.
- Augmented assignment: shortcuts combining an operation and assignment (`x += 1`, `total *= factor`).
- Multiple-assignment / tuple-unpacking: assign several names at once (`a, b = b, a`).

Examples (Python)

=== "Python"
    ```python
    # expression statement (call for side effect)
    print("Hello")

    # assignment
    x = 10

    # augmented assignment
    x += 5  # equivalent to x = x + 5

    # multiple assignment / swap
    a, b = 1, 2
    a, b = b, a  # swap values
    ```

## Compound statements and blocks

Compound statements contain other statements and typically control the flow of execution.

- Conditionals: `if`, `elif`, `else` choose which statements run.
- Loops: `for` and `while` repeat statements until a condition changes.
- Exception handling: `try`, `except`, `finally` manage errors and cleanup.
- Context managers: `with` (in languages that support them) create scoped behavior.

Blocks group statements together. In some languages blocks are delimited with braces (`{ ... }`); in Python they are created by indentation.

Examples (Python)

=== "Python"
    ```python
    # conditional
    if x > 0:
        print("positive")
    else:
        print("non-positive")

    # loop
    for i in range(3):
        print(i)

    # try/except
    try:
        risky()
    except ValueError as e:
        handle(e)
    finally:
        cleanup()
    ```

## Control-flow keywords

- `return` — exit a function and optionally provide a value.
- `break` — exit the nearest loop early.
- `continue` — skip to the next iteration of the loop.
- `pass` — a no-op statement used as a placeholder.
- `import` / `from` — bring modules and names into scope (statement form in many languages).

Examples (Python)

=== "Python"
    ```python
    def find_first_positive(items):
        for x in items:
            if x > 0:
                return x
        return None

    for n in numbers:
        if should_skip(n):
            continue
        if is_done(n):
            break
    ```

## Assignment details and variable lifetime

Assignment creates or updates a binding between a name and a value. Important points:

- Assignment does not "copy" semantics for immutable types; it binds a name to a value (the implementation details vary by language).
- Scope determines where a binding is visible: local, nonlocal/enclosing, module, and global scopes are common.
- Lifetime is the period during which a binding remains valid; garbage-collected languages free memory when no reachable references remain.

Examples (Python)

=== "Python"
    ```python
    # local binding
    def f():
        x = 1  # x is local to f

    # modifying an outer binding (explicit in Python)
    def outer():
        x = 0
        def inner():
            nonlocal x
            x += 1
        inner()
    ```

## Statements vs expressions across languages

- Expression-oriented languages (e.g., many functional languages) favor expressions everywhere — control-flow constructs return values.
- Statement-oriented languages (e.g., classical Python, pre-walrus) separate actions (statements) from value-producing expressions.
- Many modern languages mix both approaches; understanding which constructs yield values helps when porting code or reading other languages.

Quick note: In Python the assignment statement does not itself yield a value. The walrus operator `:=` allows assignment as part of an expression, which can be convenient but should be used judiciously to keep code readable.

## Side effects and best practices

- Statements are the usual place where side effects happen (mutating data, performing I/O, changing global state).
- Favor small functions that minimize side effects; keep pure computations as expressions where possible — this makes reasoning and testing easier.
- Keep statements simple and clear: one primary action per statement is a helpful guideline.

## Common pitfalls

- Assuming assignments to an object mutate the outer variable in every language.
- Relying on implicit fall-through or unspecified evaluation order.
- Overusing expression-style assignment (e.g., chaining assignments that hide intent).

## Examples and patterns

=== "Python"
    ```python
    # swapping values without temporary variable
    a, b = b, a

    # accumulate in a loop
    total = 0
    for x in items:
        total += x

    # guard clause for clarity
    if not prepared():
        return  # early exit keeps the happy path unindented
    ```

## Links and further reading

- See `../../lessons/2_expressions/fundamentals.md` for the expressions overview (short contrast between expressions and statements).
- See `../../lessons/2_expressions/variables.md` for basic variable usage and literals.
- Related: `../../lessons/2_expressions/operators.md` for operator precedence and operator behavior.

