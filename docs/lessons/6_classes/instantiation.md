---
title: instantiation
chapter: Classes & Objects
chapter_number: 6
lesson_number: 3
---

# Instantiation
Instantiation creates objects from classes. Understand constructors, default values, and
how multiple instances maintain independent state.

=== "Python"

    ```python
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

    p1 = Point(1,2)
    p2 = Point()
    p1.x = 10  # p2.x remains 0
    ```

=== "Matlab"

    ```matlab
    p1 = Point(1,2);
    p2 = Point();
    p1.x = 10; % p2.x remains default
    ```

## Gotchas
- Beware of shared mutable defaults if class-level objects are used as defaults.
- Constructors should validate inputs and establish invariants.
- In some languages, object creation may be expensive; consider factory functions or pooling for hot paths.
