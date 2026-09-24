class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j=0
        res = []
        maxe = 0
        for i in range (len(nums)):
            maxe = max(maxe,nums[i])
            if (i-j+1) == k:
                res.append(maxe)
                if maxe == nums[j]:
                    maxe = 0
                j+=1
        return res

        