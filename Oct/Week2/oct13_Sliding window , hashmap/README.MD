# Day 13: Sliding Window + HashMap

## Folder Contents & Summary

| Type | File | Approach | Time | Space |
|------|------|----------|------|--------|
| Primary 1 | Contains Duplicate II.py | Store the last seen index of each number in a hashmap. If the same number appears again within distance `k`, return `True`. | O(n) | O(n) |
| Primary 2 | Find All Anagrams in a String.py | Use a fixed-size sliding window and maintain character frequencies. When the window frequencies match the pattern frequencies, record the starting index. | O(n) | O(1) |
| Primary 3 | Permutation in String.py | Maintain a sliding window of length `len(s1)` and compare frequency arrays. A match indicates that a permutation of `s1` exists in `s2`. | O(n) | O(1) |
