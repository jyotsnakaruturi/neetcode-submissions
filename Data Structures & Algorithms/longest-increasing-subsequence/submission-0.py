class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        t=[0]*n
        for i in range (1,n):
            for j in range (i):
                if nums[j]<nums[i] and t[j]+1 > t[i]:
                    t[i]=t[j]+1
        return max(t)+1

        