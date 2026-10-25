**# Day 29: Sort + Merge Intervals**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `merge_intervals.py` | Use a custom sorting algorithm to order intervals by start time, then merge overlapping intervals by updating the end time. | O(n log n) | O(n) |
| Primary 2 | `insert_interval.py` | Insert the new interval into the sorted intervals and merge overlapping intervals without using built-in sorting. | O(n) | O(n) |
| Primary 3 | `non_overlapping_intervals.py` | Use a custom sorting algorithm to order intervals by end time, then greedily remove overlapping intervals to maximize the number of non-overlapping intervals. | O(n log n) | O(n) |