class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while(l<r):
                summ = nums[i] + nums[l] + nums[r]
                if(summ==0):
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    
                elif(summ>0):
                    r-=1
                else:
                    l+=1
            
        return ans
        
                
            