Some quick notes for instructors to rewind the repo for a new bootcamp:

1. To rewind to a clean repository:

```
git checkout reset-for-new-bootcamp stats.py test_stats.py
git commit -m "Reset for a new bootcamp YYYY-MM"
git push origin master
```

2. To make the first commit to demonstrate the need for upstream sync

```
git checkout first-commit-for-upstream-sync stats.py
git commit -m "Fixing mean to behave correctly for floats."
```

When at the correct point in the lesson to change the repo:

```
git push origin master
```

