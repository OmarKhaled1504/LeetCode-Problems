class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        mink=max(piles)
        while(l<=r):
            k=(l+r)//2
            summ = 0
            for p in piles:
                summ+=math.ceil(p/k)
            if(summ<=h):
                mink = min(mink,k)
                r=k-1
            else:
                l=k+1
        return mink
            