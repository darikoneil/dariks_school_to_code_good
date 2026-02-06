---
title: hash map
chapter: Data Structures
chapter_number: 5
lesson_number: 3
---

# Hash Map (Dictionaries)
Hash maps (associative arrays, dictionaries) store key-value pairs and provide fast lookup
by key. They are ideal for mapping names to values, counting, and grouping data.

=== "Python"

    ```python
    # Creation
    d = {'a': 1, 'b': 2}
    empty = {}

    # Access and set
    d['c'] = 3
    v = d.get('x', 0)  # default if missing

    # Iteration
    for k, val in d.items():
        print(k, val)

    # Counting
    from collections import Counter
    cnt = Counter(['a','b','a'])
    ```

=== "Matlab"

    ```matlab
    % containers.Map as a hash map
    keys = {'a','b'};
    vals = {1,2};
    m = containers.Map(keys, vals);

    % Access
    m('c') = 3; % add
    if isKey(m, 'x')
      v = m('x');
    else
      v = 0;
    end
    ```

## Gotchas
- Keys must be hashable (immutable) in Python; lists cannot be keys but tuples can.
- Order: Python 3.7+ preserves insertion order for dicts, but don't rely on it for logic unless intended.
- Matlab `containers.Map` requires matching key/value cell arrays for construction and may be slower than native arrays for numeric-heavy code.
