---
title: attributes and methods
chapter: Classes & Objects
chapter_number: 6
lesson_number: 1
---

# Attributes and Methods
Attributes store object state; methods define behavior. Use instance attributes for per-object
state and class attributes for shared data.

=== "Python"

    ```python
    class Counter:
        step = 1  # class attribute

        def __init__(self, start=0):
            self.value = start  # instance attribute

        def inc(self):
            self.value += self.step

    c = Counter()
    c.inc()
    print(c.value)
    ```

=== "Matlab"

    ```matlab
    classdef Counter
      properties
        value = 0;
      end
      properties (Constant)
        step = 1;
      end
      methods
        function obj = inc(obj)
          obj.value = obj.value + obj.step;
        end
      end
    end
    ```

## Gotchas
- Access class attributes via the class name or `self.__class__` to avoid accidental shadowing.
- In Matlab, class properties have attributes (like `Constant`) that change their behavior.
- Avoid large mutable class-level defaults unless intentionally shared.

## Exercises
1. Create a `Counter` class and demonstrate class vs instance attributes.
2. Add a `reset` method that sets the counter back to zero.
3. In Matlab, declare a read-only property using appropriate attributes.

