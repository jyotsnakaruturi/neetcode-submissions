class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper (self,nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

#This line handles the circular constraint:

#nums[0] → if there’s only one house, just rob it.

#self.helper(nums[1:]) → rob from house 1 to last (ignore first house).

#self.helper(nums[:-1]) → rob from house 0 to second-last (ignore last house).