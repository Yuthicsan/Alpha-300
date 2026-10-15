# Day 5: Set Membership + Missing

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `intersection_of_two_arrays.py` | Store elements from one array for membership checks, then manually traverse the other array to collect common unique elements without using set operations. | O(n + m) average | O(n + m) |
| Primary 2 | `missing_number.py` | Calculate the expected sum of numbers from `0` to `n` and subtract the actual array sum to find the missing number. | O(n) | O(1) |
| Primary 3 | `find_all_numbers_disappeared_in_an_array.py` | Track which numbers appear in the array, then manually check the range from `1` to `n` to identify missing numbers. | O(n) average | O(n) |
