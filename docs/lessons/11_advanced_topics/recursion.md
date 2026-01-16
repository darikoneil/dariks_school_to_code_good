---
title: Recursion
chapter: Advanced Topics
chapter_number: 11
lesson_number: 1
---

# Recursion
Recursion is when a function calls itself to solve smaller instances of the same problem.

## Basics and Base Case
Every recursive function needs a base case to stop recursion.

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Patterns
- Divide-and-conquer (merge sort)
- Tree recursion (traversing tree structures)

## Limits and Tail Recursion
Python has a recursion depth limit; tail-call optimization is not performed by CPython.

## Exercises
1. Implement a recursive and iterative version of factorial and compare behavior for small inputs.
2. Write a recursive function to compute Fibonacci numbers and discuss its performance characteristics.

