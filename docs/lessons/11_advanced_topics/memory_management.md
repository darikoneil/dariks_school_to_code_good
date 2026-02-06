---
title: Memory Management
chapter: Advanced Topics
chapter_number: 11
lesson_number: 4
---

# Memory Management
Understanding how programs allocate and free memory helps avoid leaks and reduce peak usage.

## Allocation and Garbage Collection
High-level languages often provide automatic memory management (garbage collection). In Python, reference counting and a cyclic GC are used.

## Profiling Memory
Use tools like `tracemalloc` or external profilers to find memory hotspots.

```python
import tracemalloc
tracemalloc.start()
# run workload
print(tracemalloc.get_traced_memory())
```

## Common Sources of Leaks
- Long-lived caches holding references
- Global variables
- Detached cycles not reclaimed until GC runs
