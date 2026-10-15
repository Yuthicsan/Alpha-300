class Solution:
    def frequencyCount(self, arr):
        freq = {}
        for i in arr :
            if i in freq :
                freq[i] += 1
            else :
                freq[i] = 1
        
        ans = []
        for i in range (1 ,len(arr) + 1) :
            if i in freq :
                ans.append(freq[i])
            else :
                ans.append(0)
        return ans