class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r= len(heights) -1
        maxe =0
        while l < r:
            length = min(heights[l], heights[r])
            breath = r-l
            maxe = max(maxe,length*breath)
            if heights[l] <  heights[r]:
                l+=1
            else:
                r-=1
        return maxe