class Solution:
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        arr = []
        for ch in freq:
            arr.append([ch, freq[ch]])
        n = len(arr)
        for i in range(n-1):
            min = i 
            for j in range(i+1 , n):
                if arr[j] < arr[min]:
                    min = j
            if min != i:
                arr[i] , arr[min] = arr[min] , arr[i]
        ans = ""
        for ch, count in arr:
            ans = ans+ ch * count
        return ans