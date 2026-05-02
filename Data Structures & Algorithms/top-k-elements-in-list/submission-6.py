class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for i in nums:
           map[i]=map.get(i,0)+1
        maps=sorted(map.items() ,key = lambda item:item[1],reverse = True)
        l=[]
        for i in range (k):
            l.append(maps[i][0])
        return l