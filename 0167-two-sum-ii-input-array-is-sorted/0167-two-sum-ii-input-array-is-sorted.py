class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1
        for i in range(len(numbers)):
            summ = numbers[l]+numbers[r]
            if(summ == target):
                return [l+1, r+1]
            elif(target - summ>0):
                l+=1
            else:
                r-=1
            
        