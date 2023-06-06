class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        longest = 0
        for i in ns:
            if((i-1) in ns):
                continue
            else:
                l = 1
                j=i
                while((j+1) in ns):
                    l+=1
                    j+=1
                if l > longest:
                    longest = l
        return longest
                
        