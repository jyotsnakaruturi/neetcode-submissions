class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right=len(nums)
        nums.sort()
        n=len(nums)
        left=0
        l=[]
        for i in range (n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                t=nums[left]+nums[right]+nums[i]
                if t==0 :
                    l.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
                    right-=1
                elif t<0:
                    left+=1
                else:
                    right-=1
        return l



        