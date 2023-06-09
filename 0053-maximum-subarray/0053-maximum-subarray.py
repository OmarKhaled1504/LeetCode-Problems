class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        summ = 0
        for n in nums:
            summ+=n
            ans=max(summ,ans)
            if summ<0:
                summ=0
        return ans