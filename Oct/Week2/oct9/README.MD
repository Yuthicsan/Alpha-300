# Day 9: Two Pointers Same Direction (Read + Write)

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `move_zeroes.py` | Use a read pointer to scan the array and a write pointer to place each non-zero element in its correct position, then fill the remaining positions with zeros. | O(n) | O(1) |
| Primary 2 | `remove_duplicates_from_sorted_array.py` | Scan the sorted array using a read pointer and use a write pointer to store each new unique element in-place. | O(n) | O(1) |
| Primary 3 | `remove_element.py` | Read each element and overwrite the next write position only when the element does not match the value to remove. | O(n) | O(1) |

