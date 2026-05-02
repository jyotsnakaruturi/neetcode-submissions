class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        ans=nums[0]
        while low<=high:
            mid=(low+high)//2
            if nums[0] <= nums[mid]:
                low = mid +1
            else:
                ans=nums[mid]
                high=mid-1
        return ans


        