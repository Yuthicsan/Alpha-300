**# Day 25: Binary Search Variants — Peak + Mountain**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `find_peak_element.py` | Use binary search to compare the middle element with its neighbor and move toward the rising slope to find a peak. | O(log n) | O(1) |
| Primary 2 | `peak_index_mountain_array.py` | Use binary search to find the maximum element in a mountain array by checking the slope around the midpoint. | O(log n) | O(1) |
| Primary 3 | `find_in_mountain_array.py` | Find the peak using binary search, then search the ascending and descending portions with appropriate binary search variants. | O(log n) | O(1) auxiliary |