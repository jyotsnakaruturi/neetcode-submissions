from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()      # will store indexes in decreasing order of values
        l = 0            # left pointer
        res = []         # to store results

        for r in range(len(nums)):   # r moves automatically
            # 1. Remove smaller values from the back 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Remove elements that are outside the window
            if q[0] < l:
                q.popleft()

            # 3. When window size is exactly k
            if r - l + 1 == k:
                res.append(nums[q[0]])  # q[0] is the index of max element
                l += 1                  # slide the window

        return res
