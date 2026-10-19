# Day 14: Window + Condition Tracking

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary 1 | `max_consecutive_ones_iii.py` | Maintain a sliding window and track the number of zeros. Shrink the window when the zero count exceeds `k`, and record the longest valid window. | O(n) | O(1) |
| Primary 2 | `longest_repeating_character_replacement.py` | Track character frequencies and the maximum frequency in the current window. Shrink the window when replacements required exceed `k`, and update the longest valid length. | O(n) | O(1) |
| Primary 3 | `longest_substring_without_repeating_characters.py` | Track the most recent index of each character and move the left pointer forward when a repeated character appears inside the current window. | O(n) | O(min(n, charset)) |
