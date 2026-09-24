class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j=0
        q = deque()
        res = []
        for i in range (len(nums)):

            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
             
            if j > q[0]:
                q.popleft()
            if (i-j+1) == k:
                res.append(nums[q[0]])
                j+=1
        return res