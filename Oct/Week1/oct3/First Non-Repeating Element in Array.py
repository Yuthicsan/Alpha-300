class Solution:
    def firstNonRepeating(self, arr): 
        freq = {}
        for i in arr :
            if i in freq :
                freq[i] += 1
            else :
                freq[i] = 1
        for i in arr :
            if freq[i] == 1:
                return i
        return 0