---
title: Test-Driven Development
chapter: Testing
chapter_number: 10
lesson_number: 3
---

# Test-Driven Development (TDD)
TDD is a development workflow where you write tests before implementing functionality.

## The Cycle
1. Red: write a failing test for the desired behavior.
2. Green: implement the minimal code to pass the test.
3. Refactor: clean up while keeping tests green.

## Benefits and Trade-offs
- Encourages small incremental design and good test coverage.
- Can slow initial development and may encourage over-testing internal details.

## Example (outline)
- Write `assert add([1,2]) == 3` (failing).
- Implement `def add(items): return sum(items)`.
- Refactor to handle edge cases and keep tests green.
