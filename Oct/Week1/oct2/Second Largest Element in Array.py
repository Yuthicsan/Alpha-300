class Solution:
    def getSecondLargest(self, arr):
        first = -1
        second = -1
        for i in arr :
            if i>first :
                second = first
                first = i
            elif i>second and first != i :
                second = i 
        return second
        