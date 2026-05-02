class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        l=r=0
        fartest=0
        while r < len(nums)-1:
            for i in range (l,r+1):
                fartest = max(fartest,nums[i]+i)
            l=r+1
            r=fartest
            jumps+=1
        return jumps
         