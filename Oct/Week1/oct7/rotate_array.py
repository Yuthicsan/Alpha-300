def rotate(self, nums, k):
    l , r = 0 , len(nums) - 1
    while l < r:
        nums[l] , nums[r] = nums[r] , nums[l]
        l , r = l+1 , r-1