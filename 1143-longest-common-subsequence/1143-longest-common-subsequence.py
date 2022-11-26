class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        import numpy as np
        c=np.zeros((len(text1)+1,len(text2)+1))
   
        for i in range(1,len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j],c[i][j-1]) 
        return int(c[len(text1)][len(text2)])