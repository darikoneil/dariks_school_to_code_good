---
title: Version Control Basics
chapter: Git
chapter_number: 11
lesson_number: 1
---

# Version Control Basics
Version control systems record changes to files over time so you can recall specific versions later. Git is a distributed version control system commonly used for source code.

## Core Concepts
- Repository (repo): a directory tracked by Git.
- Commit: a snapshot of changes with a message and metadata.
- Branch: a named pointer to a commit, used to isolate work.
- Remote: a hosted copy of a repo (for example, GitHub).

## Minimal Workflow
A typical local workflow looks like:

```bash
# initialize a repo
git init
# stage and commit changes
git add .
git commit -m "Initial commit"
# add remote and push
git remote add origin <url>
git push -u origin main
```

## Best Practices
- Commit small, logical changes with clear messages.
- Use branches for features and bugfixes.
- Pull regularly to integrate remote changes before pushing.

## Gotchas
- Commits are local until pushed to a remote.
- Rewriting published history (git rebase --force) can disrupt collaborators.
