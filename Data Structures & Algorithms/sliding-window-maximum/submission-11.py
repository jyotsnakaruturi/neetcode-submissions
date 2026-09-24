class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j=0
        res = []
        maxe = 0
        for i in range (len(nums)):
            if (i-j+1) == k:
                maxe = max(nums[j:i+1])
                res.append(maxe)
                j+=1
        return res

        