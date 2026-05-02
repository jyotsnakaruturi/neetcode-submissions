class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed={};
        for i in range(len(nums)):
            if target - nums[i] in needed:
                return [needed[target-nums[i]],i]
            else:
                needed[nums[i]]=i;
        