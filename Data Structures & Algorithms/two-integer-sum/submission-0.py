class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        sol=[]
        for i in range (len(nums)):
            if nums[i] not in l:
                l.append(target-nums[i])
            else:
                sol.append(l.index(nums[i]))
                sol.append(i)
                return sol
        