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

## Exercises
1. Use `tracemalloc` to identify a function that increases peak memory and refactor it to reduce allocations.
2. Explain how reference cycles can prevent timely resource release and how to break them.

