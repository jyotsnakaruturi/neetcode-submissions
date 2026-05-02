class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxres=float("-inf")
        res=0
        for i in nums:
            res+=i
            maxres=max(res,maxres)
            if res <=0:
                res=0
            
                
             
            
        return maxres

 