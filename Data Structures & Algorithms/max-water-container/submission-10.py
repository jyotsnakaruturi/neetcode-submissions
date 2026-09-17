class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r = len(heights)-1
        max_c=0
        while l<r:
            maxe = min(heights[l],heights[r])*(r-l)
            max_c=max(maxe,max_c)
            if l<r and heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_c

        