class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        maxe=float('-inf')
        for i in nums:
            cur += i
            maxe=max(maxe,cur)
            if cur <=0:
                cur=0
        return maxe

        

