class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range (n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=n-1
             
            while l < r:
                summ = nums[i]+nums[r]+nums[l]
                if summ < 0:
                    l+=1
                elif summ > 0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
