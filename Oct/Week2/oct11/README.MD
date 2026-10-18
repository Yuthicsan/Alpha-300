# Day 11: Fixed-Size Sliding Window

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `maximum_average_subarray_i.py` | Calculate the sum of the first `k` elements, then slide the window by adding the incoming element and subtracting the outgoing element. Track the maximum window sum. | O(n) | O(1) |
| Primary 2 | `max_sum_subarray_of_size_k.py` | Maintain a running sum for a window of size `k`, updating it with each incoming and outgoing element to find the maximum sum. | O(n) | O(1) |
| Primary 3 | `mean_of_array_after_removing_some_elements.py` | Sort the array, remove the required number of smallest and largest elements, and calculate the mean of the remaining elements. | O(n log n) | O(n)* |

