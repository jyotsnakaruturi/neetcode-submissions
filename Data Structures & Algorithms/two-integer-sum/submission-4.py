class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for ind, val in enumerate (nums):
            diff=target-val
            if diff in l:
                return [l[diff],ind]
            l[val]=ind
        return False