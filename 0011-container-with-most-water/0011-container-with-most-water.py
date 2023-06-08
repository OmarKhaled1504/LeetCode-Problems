class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        water = 0
        flag=0
        while(l<r):
            w = min(height[l], height[r])*(r-l)
            if(w>water):
                water = w
            if(height[l]>height[r]):
                r-=1
            else:l+=1
        return water
        