---
title: defining classes
chapter: Classes & Objects
chapter_number: 6
lesson_number: 0
---

# Defining Classes
Classes group data and behavior into a single blueprint. Instances (objects) are created from classes
and hold their own state. Object-oriented design helps model real-world concepts and encapsulate related functions.

=== "Python"

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

        def __repr__(self):
            return f"Point({self.x}, {self.y})"
    ```

=== "Matlab"

    ```matlab
    classdef Point
      properties
        x
        y
      end
      methods
        function obj = Point(x, y)
          obj.x = x;
          obj.y = y;
        end
        function obj = move(obj, dx, dy)
          obj.x = obj.x + dx;
          obj.y = obj.y + dy;
        end
      end
    end
    ```

## Gotchas
- Remember to initialize instance state (Python `__init__`, Matlab constructor).
- Be explicit about `self` / returning modified objects (Matlab methods often return the modified object for value-like semantics).
- Keep classes focused; don't cram unrelated behavior into a single class.
