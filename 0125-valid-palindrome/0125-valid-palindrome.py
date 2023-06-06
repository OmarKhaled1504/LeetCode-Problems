import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
             
        
        s =''.join(ch for ch in s if ch.isalnum())
        l, r = 0, len(s)-1
        
        for i in range(int(len(s)/2)):
            
            if(s[l]==s[r]):
                l+=1
                r-=1   
            else:
                return False
        return True