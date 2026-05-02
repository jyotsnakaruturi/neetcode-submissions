class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                curr=i
                strik=1
                while curr+1 in nums:
                    curr+=1
                    strik+=1
                longest=max(longest,strik)
        return longest
        