class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxe=float('-inf')
        s=0
        for i in nums:
            s+=i
            maxe=max(maxe,s)
            if s<0:
                s=0
        return maxe


 