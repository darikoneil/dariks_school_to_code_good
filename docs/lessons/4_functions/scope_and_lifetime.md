---
title: scope and lifetime
chapter: Functions & Scripts
chapter_number: 4
lesson_number: 4
---

# Scope and Lifetime
Scope determines where a name is visible; lifetime determines how long a value exists.
Understanding local vs global scope, closures, and lifetime (especially for resources) is important.

=== "Python"

    ```python
    x = 10  # global
    def f():
        y = 5  # local
        print(x, y)

    # Global modification
    def g():
        global x
        x = x + 1

    # Closure
    def make_adder(n):
        def add(x):
            return x + n
        return add
    add3 = make_adder(3)
    print(add3(4))  # 7
    ```

=== "Matlab"

    ```matlab
    % Globals (use sparingly)
    global x
    x = 10;

    function show()
      global x
      disp(x)
    end

    % Nested functions capture variables from outer scope
    function f = make_adder(n)
      f = @() n + 1; % simple closure example
    end
    ```

## Gotchas
- Overusing globals leads to fragile code and hard-to-track bugs.
- Mutable objects referenced in closures can produce surprising results if mutated after closure creation.
- Resource lifetime: open files/sockets should be closed; prefer context managers (Python `with`) or `onCleanup` in Matlab.
