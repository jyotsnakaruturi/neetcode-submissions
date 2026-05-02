class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre,suf=0,0
        res=nums[0]
        n=len(nums)
        for i in range (len(nums)):
            pre=nums[i]*(pre or 1)
            suf=nums[n-1-i]*(suf or 1)
            res=max(res,max(pre,suf))
        return res

        