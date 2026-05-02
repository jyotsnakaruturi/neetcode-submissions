class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xor=n
        for i in range (n):
            s=i^nums[i]
            xor ^=s
        return xor
             