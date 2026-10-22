**# Day 26: Binary Search on Rotated Array**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `search_rotated_sorted_array.py` | Use binary search to identify the sorted half and determine which half may contain the target. | O(log n) | O(1) |
| Primary 2 | `find_minimum_rotated_sorted_array.py` | Compare the middle element with the rightmost element to locate the minimum in a rotated sorted array without duplicates. | O(log n) | O(1) |
| Primary 3 | `find_rotation_count.py` | Use binary search to find the index of the minimum element, which gives the number of rotations in a rotated sorted array without duplicates. | O(log n) | O(1) |