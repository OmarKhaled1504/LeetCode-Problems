import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newlist = np.array(matrix).flatten()
        l,r = 0, len(newlist) - 1
        while(l<=r):
            med = (l+r)//2
            if(target == newlist[med]):
                return True
            elif(target > newlist[med]):
                l=med+1
            else:
                r=med-1
        return False
        
    