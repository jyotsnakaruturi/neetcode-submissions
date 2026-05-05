class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        for i in range (len(nums)):
             
            num=nums[i]
            c=1
            while num-1 in nums:
                num = num-1
                c+=1
                count = max(count,c)
        return count
        