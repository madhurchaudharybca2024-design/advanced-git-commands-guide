# Advanced Git Commands and Their Usage

Below are some advanced Git commands used for source control management, along with explanations and practical examples:

---

## 1. `git stash`

**Purpose:**  
Temporarily save changes that are not ready to be committed, allowing you to switch branches or pull updates without losing your work.

**Usage Example:**

```bash
# Save your uncommitted changes
git stash

# List all stashed changes
git stash list

# Apply the most recent stash
git stash apply

# Apply and remove the most recent stash
git stash pop

# Apply a specific stash
git stash apply stash@{1}
```

---

## 2. `git cherry-pick`

**Purpose:**  
Apply the changes introduced by an existing commit onto your current branch. Useful for porting bug fixes or features without merging entire branches.

**Usage Example:**

```bash
# Cherry-pick a commit onto your current branch
git cherry-pick <commit-hash>

# Cherry-pick a range of commits (inclusive)
git cherry-pick <start-commit>^..<end-commit>
```

---

## 3. `git revert`

**Purpose:**  
Create a new commit that undoes the changes made by a previous commit, without modifying the commit history.

**Usage Example:**

```bash
# Revert a specific commit
git revert <commit-hash>

# Revert multiple commits
git revert <oldest-commit-hash>^..<newest-commit-hash>
```

---

## 4. `git reset`

**Purpose:**  
Move the current branch to a different commit, optionally changing the state of the working directory and staging area. There are three modes: `--soft`, `--mixed`, and `--hard`.

**Usage Example:**

```bash
# Reset to a previous commit, keeping changes staged
git reset --soft <commit-hash>

# Reset to a previous commit, unstaging changes but keeping them in the working directory
git reset --mixed <commit-hash>

# Reset to a previous commit, discarding all changes in the staging area and working directory
git reset --hard <commit-hash>
```

---

## Summary Table

| Command        | Description                                    | Example                                |
|----------------|------------------------------------------------|----------------------------------------|
| git stash      | Save uncommitted changes                       | `git stash`                            |
| git cherry-pick| Apply a commit to current branch                | `git cherry-pick abc1234`              |
| git revert     | Undo changes from a specific commit             | `git revert abc1234`                   |
| git reset      | Move HEAD to another commit (various effects)   | `git reset --hard abc1234`             |

---

**Tip:**  
Always check your changes with `git status` before performing advanced operations to avoid data loss.
