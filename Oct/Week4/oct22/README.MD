**# Day 22: Classic Binary Search**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `binary_search.py` | Repeatedly divide the sorted search range in half using `lo + (hi - lo) // 2` until the target is found or the range is empty. | O(log n) | O(1) |
| Primary 2 | `search_insert_position.py` | Use binary search to find the target's index or the position where it should be inserted to maintain sorted order. | O(log n) | O(1) |
| Primary 3 | `first_bad_version.py` | Use binary search to find the first bad version by checking whether each midpoint is good or bad. | O(log n) | O(1) |