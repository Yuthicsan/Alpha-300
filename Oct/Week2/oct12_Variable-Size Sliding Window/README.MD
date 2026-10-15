
# Day 12: Variable-Size Sliding Window

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | [Minimum Size Subarray Sum.py](./Minimum%20Size%20Subarray%20Sum.py) | I use two pointers to maintain a sliding window and keep track of its sum. When the sum reaches the target, I check whether the current subarray is the shortest one and shrink the window to see if I can get a smaller result | O(N) | O(1) |
| Primary 2 | [Longest Subarray with Sum K.py](./Longest%20Subarray%20with%20Sum%20K.py) | I use two pointers to maintain a window and track its sum. I expand the window by adding elements and shrink it when the sum exceeds K, keeping track of the longest valid subarray | O(N) | O(1) |
| Primary 3 | [Fruit Into Baskets.py](./Fruit%20Into%20Baskets.py) | I maintain a sliding window containing at most two different types of fruit. If the window contains more than two types, I move the left pointer forward until the condition is satisfied, updating the maximum window length along the way | O(N) | O(1) |