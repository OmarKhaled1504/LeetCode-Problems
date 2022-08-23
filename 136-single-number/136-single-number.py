class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sin = set()
        for i in nums:
            if i in sin:
                sin.remove(i)
            else:
                sin.add(i)
        return sin.pop()
            
