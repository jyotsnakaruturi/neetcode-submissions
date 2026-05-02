class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin=1
        curmax=1
        res=nums[0]
        for num in nums:
            temp=curmax*num
            curmax=max(curmax*num,num,curmin*num)
            curmin=min(temp,num,curmin*num)
            res=max(res,curmax)
        return res

        