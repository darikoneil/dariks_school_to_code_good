---
title: Debugging Tools
chapter: Debugging
chapter_number: 9
lesson_number: 3
---

# Debugging Tools
There are many tools that help you inspect program state and find bugs: interactive debuggers, logging, and IDE features.

## Interactive Debuggers
Set breakpoints, step into functions, and inspect variables.

Python example:

```python
import pdb
pdb.set_trace()
# or run: python -m pdb your_script.py
```

## Logging vs Print
Logging is more flexible than print-debugging: you can set levels and direct output to files.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("starting")
```

## IDE and Browser Tools
- IDEs (PyCharm, VS Code) provide visual breakpoints and variable watches.
- Browser devtools help debug front-end JavaScript.
