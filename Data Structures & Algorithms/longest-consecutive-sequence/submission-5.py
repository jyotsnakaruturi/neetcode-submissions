class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        maxe=0
        for i in range  (n):
            num=nums[i]
            c=1
            while num-1 in nums:
                num=num-1
                c+=1
            maxe=max(maxe,c)
        return maxe

