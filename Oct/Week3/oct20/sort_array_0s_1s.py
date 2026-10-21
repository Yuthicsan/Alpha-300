class Solution:
    def segregate0and1(self, arr):
        zeros = 0
        for i in arr:
            if i == 0:
                zeros += 1
        for j in range(len(arr)):
            if j < zeros:
                arr[j] = 0
            else:
                arr[j] = 1
                
        return arr