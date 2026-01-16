---
title: importing
chapter: Modules & Packages
chapter_number: 7
lesson_number: 0
---

# Importing
Modules let you organize code into files; packages group modules. Importing makes symbols from
modules available in your current namespace.

=== "Python"

    ```python
    # import module
    import math
    print(math.sqrt(2))

    # import symbol
    from math import sqrt
    print(sqrt(2))

    # alias
    import numpy as np
    ```

    # Module layout (package)
    - mypkg/
      - __init__.py
      - mod.py

=== "Matlab"

    ```matlab
    % MATLAB uses the path and packages via +foldername
    % Add folder to path or put on MATLAB path
    addpath('mypkg')
    % Call functions in folder
    result = myfunc(1);
    ```

## Gotchas
- Python: circular imports can cause runtime errors; structure modules to avoid mutual dependencies.
- Use absolute imports in packages to be clear; relative imports are useful for internal modules.
- Matlab package folders (starting with `+`) create namespaces; ensure path visibility.

## Exercises
1. Create a small Python package with `__init__.py` and a module, import from it.
2. Demonstrate aliasing a module (`import numpy as np`) and calling a function.
3. In Matlab, add a folder to the path and call a function from it.

