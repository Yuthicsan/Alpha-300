**# Day 19: Quick Sort (Implement from Scratch)**

**## Folder Contents & Summary**

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `quick_sort.py` | Implement Quick Sort using pivot selection, partitioning, and recursive sorting of both partitions. | O(n log n) average, O(n²) worst | O(log n) average, O(n) worst |
| Primary 2 | `quick_sort_3_way_partition.py` | Partition the array into elements smaller than, equal to, and greater than the pivot to handle duplicates efficiently. | O(n log n) average, O(n²) worst | O(log n) average, O(n) worst |
| Primary 3 | `kth_largest_element.py` | Use Quickselect partitioning to locate the kth-largest element without fully sorting the array. | O(n) average, O(n²) worst | O(1) auxiliary, excluding recursion stack if recursive |