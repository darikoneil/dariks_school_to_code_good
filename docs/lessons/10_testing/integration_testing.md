---
title: Integration Testing
chapter: Testing
chapter_number: 10
lesson_number: 2
---

# Integration Testing
Integration tests verify that multiple components work together correctly.

## Differences from Unit Tests
- Integration tests exercise interactions across modules or services.
- They are slower and require controlled environments.

## Designing Integration Tests
- Use fixtures to start/stop services (databases, web servers).
- Seed test data and clean up after tests.

## Example (conceptual)
A test might start a test database, run a function that writes data, then query the database to assert the end-to-end behavior.

## Gotchas
- Avoid running slow integration tests repeatedly; separate them in CI.
- Networked services add flakiness — use local test doubles or containers.

## Exercises
1. Outline an integration test for a function that writes a user record to a database and sends a notification.
2. Describe how you'd isolate tests that depend on external APIs.

