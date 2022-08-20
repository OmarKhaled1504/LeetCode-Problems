class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[0] == target or target==i[len(i)-1]:
                return True
            elif target>i[0] and target<i[len(i)-1]:
                    for j in i:
                        if target == j:
                            return True
        return False
                