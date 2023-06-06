import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        before = 1
        after = 1
        
        for i in range(len(nums)):
            ans[i] *= before
            before *= nums[i]
            ans[len(nums)-i-1] *= after
            after *= nums[len(nums)-i-1]
        return ans
    