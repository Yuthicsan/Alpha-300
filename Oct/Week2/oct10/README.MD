# Day 10: Two Pointers from Both Ends (Merge)

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `merge_sorted_array.py` | Use pointers at the ends of both sorted arrays and fill the destination array from the back, placing the larger element first. | O(m + n) | O(1) auxiliary space |
| Primary 2 | `squares_of_a_sorted_array.py` | Compare the absolute values at both ends of the sorted array and place the larger square at the end of the result array. | O(n) | O(n) |
| Primary 3 | `sort_array_by_parity.py` | Use two pointers from opposite ends to move even numbers toward the beginning and odd numbers toward the end by swapping misplaced elements. | O(n) | O(1) auxiliary space |

