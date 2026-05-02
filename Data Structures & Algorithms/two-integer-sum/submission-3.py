class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i in range (len(nums)):
            t=target-nums[i]
            if t in l:
                return [l[t],i]
             
            l[nums[i]]=i
        return False