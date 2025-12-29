# Git Workflow Guide

**Purpose:** Daily Git commands and branching strategy for Stratega
**Goal:** Confident version control without data loss

---

## Daily Commands

### Morning Routine

```bash
# Check what's changed
git status

# Pull latest from remote (if collaborating)
git pull origin main

# See what you did yesterday
git log --oneline -10
```

### During Work

```bash
# Stage specific files
git add filename.py
git add scripts/

# Stage all changes
git add .

# Check what's staged
git status
git diff --staged

# Commit with message
git commit -m "Add ICP scoring logic for Italian contacts"

# Or with longer message
git commit -m "feat: Add ICP scoring v2

- Implemented engagement-based scoring
- Added geography detection
- Split Italy vs International segments"
```

### End of Day

```bash
# Push your commits
git push origin main

# Or if on feature branch
git push origin feature/icp-scoring
```

---

## Branching Workflow

### Create Feature Branch

```bash
# Start from updated main
git checkout main
git pull origin main

# Create and switch to new branch
git checkout -b feature/icp-scoring-v3

# Or in two steps
git branch feature/icp-scoring-v3
git checkout feature/icp-scoring-v3
```

### Work on Branch

```bash
# Normal commits
git add .
git commit -m "Add scoring function"

git add .
git commit -m "Add tests for scoring"

# Push branch to remote
git push -u origin feature/icp-scoring-v3
```

### Merge Branch

```bash
# Switch to main
git checkout main

# Pull latest
git pull origin main

# Merge your branch
git merge feature/icp-scoring-v3

# Push merged main
git push origin main

# Delete branch (optional)
git branch -d feature/icp-scoring-v3
```

---

## Commit Message Format

### Structure

```
<type>: <short description>

<longer description if needed>
```

### Types

| Type | When to Use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code restructure (no new features) |
| `docs` | Documentation only |
| `chore` | Maintenance (dependencies, config) |
| `test` | Adding tests |
| `style` | Formatting (no logic changes) |

### Examples

```bash
# Feature
git commit -m "feat: Add LinkedIn data analyzer"

# Bug fix
git commit -m "fix: Correct Italian name detection pattern"

# Refactor
git commit -m "refactor: Extract scoring logic to separate module"

# Documentation
git commit -m "docs: Add API documentation for scoring endpoint"

# Multi-line
git commit -m "feat: Implement engagement scoring

- Add message volume scoring
- Add connection direction weighting
- Add conversation recency factor
- Integrate with existing ICP model"
```

---

## Handling Changes

### Discard Unstaged Changes

```bash
# Single file
git checkout -- filename.py

# All files
git checkout -- .
```

### Unstage Files

```bash
# Single file
git reset HEAD filename.py

# All files
git reset HEAD
```

### Undo Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```

### Undo Last Commit (Discard Changes)

```bash
git reset --hard HEAD~1
```

---

## Git Stash

### Save Work in Progress

```bash
# Stash changes
git stash

# Stash with message
git stash save "WIP: scoring function"
```

### Retrieve Stashed Work

```bash
# Apply and remove from stash
git stash pop

# Apply and keep in stash
git stash apply
```

### Manage Stashes

```bash
# List stashes
git stash list

# Apply specific stash
git stash apply stash@{2}

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

---

## Viewing History

### Log Commands

```bash
# Basic log
git log

# One line per commit
git log --oneline

# Last 10 commits
git log --oneline -10

# With graph (shows branches)
git log --oneline --graph --all

# Show changes in each commit
git log -p

# Log for specific file
git log --oneline filename.py
```

### Diff Commands

```bash
# Unstaged changes
git diff

# Staged changes
git diff --staged

# Compare branches
git diff main..feature/branch

# Compare commits
git diff abc123..def456

# Show what changed in last commit
git show
```

---

## Merge Conflicts

### When They Happen

Conflicts occur when same lines changed in both branches.

### How to Resolve

```bash
# 1. Git will tell you which files have conflicts
git status

# 2. Open conflicted file, find markers:
<<<<<<< HEAD
your changes
=======
their changes
>>>>>>> feature/branch

# 3. Edit to keep what you want (remove markers)

# 4. Mark as resolved
git add conflicted_file.py

# 5. Complete merge
git commit -m "Resolve merge conflict in scorer.py"
```

### Abort Merge

```bash
git merge --abort
```

---

## .gitignore

### Common Patterns for Stratega

```gitignore
# Python
__pycache__/
*.py[cod]
venv/
.env

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Data files (too large for git)
data/*.csv
data/*.xlsx
*.csv

# Outputs
outputs/
exports/

# Secrets
*.key
credentials.json
secrets/

# Logs
*.log
logs/
```

### Check What Would Be Ignored

```bash
# See what files are ignored
git status --ignored

# Check if specific file is ignored
git check-ignore -v filename
```

---

## Remote Operations

### View Remotes

```bash
git remote -v
```

### Add Remote

```bash
git remote add origin https://github.com/user/repo.git
```

### Fetch vs Pull

```bash
# Fetch: download changes but don't merge
git fetch origin

# Pull: fetch + merge
git pull origin main
```

### Push

```bash
# Push to remote
git push origin main

# Push and set upstream
git push -u origin feature/branch

# Force push (careful!)
git push --force origin branch
```

---

## Common Scenarios

### Accidentally Committed to Main

```bash
# Create branch from current state
git branch feature/my-changes

# Reset main to before your commits
git reset --hard HEAD~3  # Number of commits to undo

# Push corrected main (if pushed)
git push --force origin main

# Switch to your branch
git checkout feature/my-changes
```

### Want to See Old Version

```bash
# View file at specific commit
git show abc123:path/to/file.py

# Checkout file from specific commit
git checkout abc123 -- path/to/file.py
```

### Split Work Across Commits

```bash
# Stage specific lines
git add -p filename.py
# Use 'y' to stage, 'n' to skip, 's' to split

# Commit just those changes
git commit -m "Add scoring logic"

# Stage remaining changes
git add filename.py
git commit -m "Add tests for scoring"
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Status | `git status` |
| Stage all | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push origin main` |
| Pull | `git pull origin main` |
| New branch | `git checkout -b branch-name` |
| Switch branch | `git checkout branch-name` |
| Merge | `git merge branch-name` |
| View log | `git log --oneline -10` |
| Stash | `git stash` |
| Unstash | `git stash pop` |
| Discard changes | `git checkout -- .` |
| Undo commit | `git reset --soft HEAD~1` |

---

## Safety Rules

1. **Commit often** - Small, frequent commits are easier to manage
2. **Pull before push** - Always pull latest before pushing
3. **Branch for features** - Keep main clean
4. **Don't force push to main** - Unless you really know what you're doing
5. **Check status before commit** - Make sure you're committing what you think
6. **Write meaningful messages** - Future you will thank present you

---

*Quick Reference v1.0 - Essential Git for Stratega development*
