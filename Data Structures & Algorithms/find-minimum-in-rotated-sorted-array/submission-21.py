class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        k = nums[0]
        res = nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= k:
                l = mid+1
            else:
                res = nums[mid]
                r = mid-1
        return res

        