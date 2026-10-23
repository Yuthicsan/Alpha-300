**# Day 27: Binary Search in 2D Matrix**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `search_2d_matrix.py` | Treat the sorted matrix as a one-dimensional sorted array and convert each midpoint index into row and column coordinates. | O(log(m × n)) | O(1) |
| Primary 2 | `row_with_maximum_ones.py` | Use binary search in each row to find the first occurrence of 1 and identify the row with the maximum number of ones. | O(m log n) | O(1) |
| Primary 3 | `peak_element_1d_array.py` | Use binary search to compare the middle element with its neighbors and move toward a peak element. | O(log n) | O(1) |