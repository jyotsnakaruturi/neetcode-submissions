import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i] = 1+count.get(i,0)
        min_heap=[]
        for v,c in count.items():
            heapq.heappush(min_heap,(c,v))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        l=[]
        while min_heap:
            l.append(heapq.heappop(min_heap)[1])
        return l

        