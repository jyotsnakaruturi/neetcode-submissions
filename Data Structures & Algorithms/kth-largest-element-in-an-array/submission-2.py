class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=len(nums)
        n=l-k+1
        heapq.heapify(nums)
        while n>0:
            a=heapq.heappop(nums)
            n-=1
        return a
         
        