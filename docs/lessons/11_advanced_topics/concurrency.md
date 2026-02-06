---
title: Concurrency
chapter: Advanced Topics
chapter_number: 11
lesson_number: 3
---

# Concurrency
Concurrency lets your program do multiple things at once. Common models include threads, processes, and async I/O.

## Threads vs Processes vs Async
- Threads share memory within a process; use locks to synchronize access.
- Processes have separate memory; communication uses IPC.
- Async uses an event loop and cooperative multitasking (async/await).

## Race Conditions and Synchronization
Protect shared state with locks or use message-passing to avoid shared mutable state.

## Example (Python sketch)

```python
import threading

counter = 0
lock = threading.Lock()

def worker():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
```
