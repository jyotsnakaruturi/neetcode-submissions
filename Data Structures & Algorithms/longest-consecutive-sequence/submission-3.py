class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxe=0
        for i in nums:
            num=i
            cur=1
            while num-1 in nums:
                cur+=1
                num=num-1
            maxe=max(maxe,cur)
        return maxe
