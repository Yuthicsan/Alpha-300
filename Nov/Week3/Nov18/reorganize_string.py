class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            
        items = [[count, ch] for ch, count in freq.items()]
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] >= right[j][0]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        sorted_items = merge_sort(items)
        
        if sorted_items[0][0] > (n + 1) // 2:
            return ""
            
        res = [""] * n
        idx = 0
        for count, ch in sorted_items:
            for _ in range(count):
                res[idx] = ch
                idx += 2
                if idx >= n:
                    idx = 1
                    
        return "".join(res)