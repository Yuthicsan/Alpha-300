class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {}
        for i, ch in enumerate(order):
            rank[ch] = i
        chars = list(s)
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                rank_l = rank.get(left[i], 26)
                rank_r = rank.get(right[j], 26)
                if rank_l <= rank_r:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        sorted_chars = merge_sort(chars)
        return "".join(sorted_chars)