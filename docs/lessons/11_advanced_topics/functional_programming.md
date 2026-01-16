---
title: Functional Programming
chapter: Advanced Topics
chapter_number: 11
lesson_number: 2
---

# Functional Programming
Functional programming (FP) emphasizes pure functions, immutability, and higher-order functions.

## Core Ideas
- Pure functions: no side effects, same output for same input.
- Immutability: prefer creating new values instead of mutating.
- Higher-order functions: functions that accept or return functions.

## Examples (Python)

```python
# map/filter/reduce
nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums))
filtered = list(filter(lambda x: x % 2 == 1, nums))
```

## When to Use FP
FP makes reasoning about code easier and is useful for parallelism, but sometimes imperative code is clearer for simple tasks.

## Exercises
1. Refactor an imperative loop that computes squares into a functional pipeline using `map`.
2. Write a pure function that returns a new list with duplicates removed without mutating the input.

