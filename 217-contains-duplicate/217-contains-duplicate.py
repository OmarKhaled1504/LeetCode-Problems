class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dups = set()
        for num in nums:
            if num in dups:
                return True
            dups.add(num)
        return False