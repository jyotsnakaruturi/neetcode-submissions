class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        min_heap=[]
        for c in count:
            heapq.heappush(min_heap,(count[c],c))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        l=[]
        while min_heap:
            l.append(heapq.heappop(min_heap)[1])
        return l

        