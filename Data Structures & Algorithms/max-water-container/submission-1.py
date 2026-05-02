class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a=0
        n=len(heights)
        left=0
        right=n-1
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            max_a=max(max_a,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_a
        