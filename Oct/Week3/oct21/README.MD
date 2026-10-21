**# Day 21: Sorting Consolidation + Dutch Flag**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `sort_colors_3_way_partition.py` | Use three pointers (`low`, `mid`, and `high`) to partition 0s, 1s, and 2s in a single pass. | O(n) | O(1) |
| Primary 2 | `wiggle_sort.py` | Rearrange elements in-place so they follow the pattern `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. | O(n) | O(1) |
| Primary 3 | `sort_array_by_increasing_frequency.py` | Count element frequencies manually and arrange elements by increasing frequency, breaking ties by decreasing value. | O(n + u log u) | O(n + u) |