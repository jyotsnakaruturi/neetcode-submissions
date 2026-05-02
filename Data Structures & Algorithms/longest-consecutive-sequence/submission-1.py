class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0

        for i in nums:
            if i-1 not in nums:
                curr=i
                striek=1
                while curr+1 in nums:
                    curr=curr+1
                    striek+=1
                longest=max(longest,striek)
        return longest

        