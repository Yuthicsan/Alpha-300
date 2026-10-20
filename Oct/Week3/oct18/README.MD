**# Day 18: Merge Sort (Implement from Scratch, Recursive)**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `merge_sort.py` | Recursively divide the array into halves, sort each half, and merge the sorted halves. | O(n log n) | O(n) |
| Primary 2 | `merge_two_sorted_arrays.py` | Use two pointers to merge two sorted arrays into one sorted result. | O(n + m) | O(n + m) |
| Primary 3 | `count_inversions.py` | Count inversions during the merge step whenever an element from the right half precedes remaining elements in the left half. | O(n log n) | O(n) |