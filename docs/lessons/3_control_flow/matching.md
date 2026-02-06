---
title: matching
chapter: Control Flow
chapter_number: 3
lesson_number: 2
---

# Matching
Matching (switch/case, `match`/`case`) provides a concise way to dispatch behavior based on
value or structure. It is often clearer than long `if`/`elif`/`elseif` chains when handling
many distinct cases, and modern languages (Python 3.10+) support structural pattern matching.

=== "Python"

    ```python
    # Literal matching (Python 3.10+)
    command = "start"
    match command:
        case "start":
            print("starting")
        case "stop":
            print("stopping")
        case _:
            print("unknown")

    # Matching tuples
    point = (0, 0)
    match point:
        case (0, 0):
            print("origin")
        case (x, y):
            print(f"point at {x},{y}")

    # Matching mapping-like structures
    data = {"type": "user", "id": 42}
    match data:
        case {"type": "user", "id": uid}:
            print(f"user {uid}")
        case _:
            print("other")
    ```

=== "Matlab"

    ```matlab
    % switch/case for value matching
    cmd = 'start';
    switch cmd
      case 'start'
        disp('starting')
      case 'stop'
        disp('stopping')
      otherwise
        disp('unknown')
    end

    % Matlab does not have structural pattern matching; use isequal or conditional checks
    point = [0 0];
    if isequal(point, [0 0])
      disp('origin')
    elseif numel(point) == 2
      x = point(1); y = point(2);
      disp(["point at " num2str(x) "," num2str(y)])
    end

    % Dispatch using a map of function handles
    handlers = containers.Map({'start','stop'},{@()disp('start'), @()disp('stop')});
    key = 'start';
    if isKey(handlers, key)
      handlers(key)();
    else
      disp('unknown')
    end
    ```

## Gotchas
- Python `match` is syntax introduced in 3.10 and uses pattern semantics (not simple equality): ensure your interpreter supports it.
- Patterns can capture variables; be careful about accidental captures.
- Matlab `switch` tests values for equality; it is not structural matching. For complex patterns, combine `if`/`elseif` with `isequal` or use a dispatch table.
- Overusing `match`/`switch` for complex logic can make code harder to test — prefer small functions per case.
