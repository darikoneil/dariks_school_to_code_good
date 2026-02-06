---
title: encapsulation
chapter: Classes & Objects
chapter_number: 6
lesson_number: 2
---

# Encapsulation
Encapsulation hides internal details and exposes a minimal interface. It prevents external code
from depending on internal representation and helps maintain invariants.

=== "Python"

    ```python
    class BankAccount:
        def __init__(self, balance=0):
            self._balance = balance  # underscore signals "private"

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount

        def balance(self):
            return self._balance
    ```

=== "Matlab"

    ```matlab
    classdef BankAccount
      properties (Access = private)
        balance = 0;
      end
      methods
        function obj = deposit(obj, amount)
          if amount > 0
            obj.balance = obj.balance + amount;
          end
        end
        function b = getBalance(obj)
          b = obj.balance;
        end
      end
    end
    ```

## Gotchas
- Python's privacy is by convention (`_` vs `__` name mangling) — it does not enforce access.
- Use property getters/setters when you need to validate assignments or compute values on access.
- In Matlab, `Access = private` enforces visibility rules more strictly.
