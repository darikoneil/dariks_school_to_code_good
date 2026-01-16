---
title: Expressions - Fundamentals
chapter: Expressions
chapter_number: 2
lesson_number: 0
---
# Expressions

Recall, from the introduction lesson, that a program is made up of instructions 
(operators, functions, methods) that manipulate variables & data structures stored 
in memory and some logic that determines the order of execution (control flow). These 
instructions can be broadly categorized into **expressions** and **statements**.

`1. Expressions`
:   An expression is a piece of code that the programming language **evaluates** to  
produce a value. Expressions are the building blocks of programs: they combine values,
variables, operators, and function calls to compute results that programs use or store.

`2. Statements`
:   A statement is a complete instruction that performs an action, such as assigning 
values to variables or controlling the flow of execution. Statements may contain  
expressions, but their primary purpose is to **do** something rather than to produce 
a value.

!!! Tip "Expressions vs. Statements"

    Expressions *are* something, statements *do* something.

> For a deeper discussion of statements (assignment, control-flow statements, scope, 
> and side effects),  see the companion lesson: `../..
> /lessons/3_control_flow/statements.md`.


## Core components of expressions

- Literals: fixed values such as `42`, `3.14`, or `"hello"`.
- Variables: names that evaluate to values (e.g., `x`, `total`).
- Operators: arithmetic (`+`, `-`, `*`, `/`), comparison (`==`, `<`), boolean  
  (`and`, `or`, `not`), and more.
- Function calls: `f(x)` is an expression whose value is whatever `f` returns.
- Attribute access and indexing: `obj.attr`, `arr[0]` produce values and can appear 
  inside larger expressions.
- Parentheses: group sub-expressions and override the default evaluation order.


## Examples (Python)

=== "Python"
    ```python
    # simple arithmetic expression
    area = width * height

    # expressions inside other expressions
    average = (a + b + c) / 3

    # string expression
    greeting = "Hello, " + name

    # boolean expressions and short-circuiting
    result = config_enabled and do_work()  # do_work() only runs if config_enabled  
    is True

    # function calls and indexing inside expressions
    value = process(items[0])
    ```