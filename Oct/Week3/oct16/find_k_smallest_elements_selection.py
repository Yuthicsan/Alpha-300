class Solution: 
    def selectionSort(self, arr, k):
        n = len(arr)
        for i in range(k):
            min = i
            for j in range(i+1 , n):
                if arr[j] < arr[min] :
                    min = j
            if min != i:
                arr[i] , arr[min] = arr[min] , arr[i]
        return arr[:k]