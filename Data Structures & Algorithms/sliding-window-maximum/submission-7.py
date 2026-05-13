class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res =[]
        maxe = float('-inf')
        for r in range (len(nums)):
            if maxe < nums[r]:
                maxe =  nums[r]
                index = r
            if r-l+1 == k and l <= index <= r:
                res.append(maxe)
                l=l+1
        return res

        