class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ls=[1]*(len(nums)+1)
         
        rs=[1]*(len(nums)+1)

        for i in range(len(nums)-1,-1,-1):
            ls[i]=ls[i+1]*nums[i]
         
        for i in range(1,len(nums)+1):
            rs[i]=rs[i-1]*nums[i-1]
        
        
        res=[]
        for i in range (len(nums)):
            r=ls[i+1]*rs[i]
            res.append(r)
        return res

        