class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        for i in range (len(nums)):
            c=0
            num=nums[i]
            while num-1 in nums:
                num = num-1
                c+=1
                count = max(count,c)
        return count+1
        