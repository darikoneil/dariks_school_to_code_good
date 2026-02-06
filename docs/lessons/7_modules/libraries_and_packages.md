---
title: libraries and packages
chapter: Modules & Packages
chapter_number: 7
lesson_number: 1
---

# Libraries and Packages
Libraries provide reusable functionality; packages bundle related modules and subpackages.
Use package managers to install third-party libraries and organize your code into packages.

=== "Python"

    ```python
    # Use pip to install a package
    # pip install requests

    import requests
    r = requests.get('https://example.com')
    print(r.status_code)
    ```

    # Example package layout
    mypkg/
      __init__.py
      utils.py
      core.py

=== "Matlab"

    ```matlab
    % Add library folders to MATLAB path or install toolbox
    addpath('mylib')
    help mylib
    ```

## Gotchas
- Keep dependencies minimal and document them in a `requirements.txt` or `pyproject.toml`.
- Semantic versioning: use pinned versions for reproducible environments where necessary.
- For Matlab, prefer toolboxes or documented add-ons for portability.
