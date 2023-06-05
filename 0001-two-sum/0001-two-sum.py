import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = sorted(nums)
        l,r = 0 ,len(nums)-1
        
        for i in range(len(nums)):
            summ = nums2[l] + nums2[r]
            if(target-summ==0):
                if(nums2[l]==nums2[r]):
                    nums = np.array(nums)
                    return(np.where(nums == nums2[l])[0])
                else:
                  return [nums.index(nums2[r]),nums.index(nums2[l])]
            elif(target-summ<0):
                r-=1
            else:
                l+=1       
