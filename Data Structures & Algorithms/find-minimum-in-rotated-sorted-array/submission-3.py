class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        hight=len(nums)-1
        ans = float('inf')
        while low<=hight:
            mid=(low+hight)//2
            if nums[low]<=nums[mid]:
                ans=min(nums[low],ans)
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                hight=mid-1
        return ans


        