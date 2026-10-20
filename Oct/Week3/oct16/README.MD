**# Day 16: Selection Sort (Implement from Scratch)**

**## Folder Contents & Summary**

| Type      | File                                  | Approach                                                                                                                   | Time              | Space |
| --------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----- |
| Primary 1 | `selection_sort.py`                   | Use nested loops to scan the unsorted portion, manually identify the smallest element, and swap it with the first unsorted element. | O(n²)             | O(1)  |
| Primary 2 | `find_k_smallest_elements_selection.py` | Manually find the smallest remaining element for each of the first `k` positions and swap it into place.                   | O(nk)             | O(1)  |
| Primary 3 | `sort_characters_by_frequency_manual.py` | Count character frequencies using a dictionary, then repeatedly select the character with the highest remaining frequency. | O(n + u²)         | O(u)  |