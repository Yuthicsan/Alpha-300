# Day 7: Array Rotation

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `rotate_array.py` | Normalize the rotation count and rotate the array in-place using three reversals: the whole array, the first section, and the remaining section. | O(n) | O(1) |
| Primary 2 | `rotate_array_by_k_steps.py` | Use the three-reversal technique to shift elements by `k` steps without creating another array or using slicing. | O(n) | O(1) |
| Primary 3 | `reverse_array_in_groups.py` | Divide the array into consecutive groups and reverse each group in-place using two pointers, including the final incomplete group if present. | O(n) | O(1) auxiliary space |

