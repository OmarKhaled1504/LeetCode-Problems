class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ''
        for c in s:
            if c.isalnum():
                s2 += c.lower()
        return s2 == s2[::-1]