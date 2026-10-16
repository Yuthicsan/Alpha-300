# Day 6: Prefix Sum Basics

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `running_sum_1d_array.py` | Build a prefix sum array manually by maintaining a running total and storing it after processing each element. | O(n) | O(n) |
| Primary 2 | `find_pivot_index.py` | Calculate the total sum, then traverse the array while tracking the left sum and deriving the right sum to find an index where both are equal. | O(n) | O(1) |
| Primary 3 | `range_sum_query_immutable.py` | Precompute prefix sums using a loop, then answer each range-sum query by subtracting the prefix before the left boundary from the prefix at the right boundary. | O(n) preprocessing, O(1) per query | O(n) |

