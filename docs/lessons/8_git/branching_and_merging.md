---
title: Branching and Merging
chapter: Git
chapter_number: 8
lesson_number: 2
---

# Branching and Merging
Branches let you develop features in isolation and keep the main line of development stable. Merging integrates changes from one branch into another.

## Branching
Create a new branch and switch to it:

```bash
git checkout -b feature/my-feature
```

List branches (current branch marked with *):

```bash
git branch
```

Delete a branch locally:

```bash
git branch -d feature/my-feature
```

## Merging
To merge a feature branch into `main`:

```bash
git checkout main
git merge feature/my-feature
```

If Git cannot automatically combine changes you'll get a merge conflict that must be resolved by editing the conflicting files, staging, and committing.

## Resolving Conflicts
- Git marks conflicts with <<<<<<<, =======, >>>>>>> markers inside files.
- Edit to choose or combine changes, then run `git add <file>` and `git commit` to finish.

## Rebase vs Merge
Rebasing rewrites commits to create a linear history:

```bash
git checkout feature/my-feature
git rebase main
```

Use rebase to keep history linear for private branches; avoid rebasing public/shared branches.

## Exercises
1. Create a branch `experiment`, make a change in it, merge it into `main`, and inspect history with `git log --oneline --graph`.
2. Simulate a simple conflict by changing the same line in `main` and a branch, then resolve the conflict and complete the merge.

