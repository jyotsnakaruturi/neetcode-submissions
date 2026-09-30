class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        maxarea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind,he = stack.pop()
                maxarea = max(maxarea,(i-ind)*he)
                start = ind
            stack.append((start,h))
        n=len(heights)
        for i,h in stack:
            maxarea = max(maxarea,h*(n-i))
        return maxarea