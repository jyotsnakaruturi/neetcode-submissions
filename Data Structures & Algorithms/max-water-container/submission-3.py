class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        maxarea=0
        while l<r:
            h=min(heights[l],heights[r])
            maxarea=max(maxarea,h*(r-l))
            if heights[r]<heights[l]:
                r-=1
            else:
                l+=1
        return maxarea
         
         