class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        ll=[[]for i in range (len(nums)+1)]
        for i in nums:
            l[i]=l.get(i,0)+1
        for key,value in l.items():
            ll[value].append(key)
        res=[]
        for i in range (len(ll)-1,0,-1):
            for j in  ll[i]:
                res.append(j)
                if len(res)==k:
                    return res
                     
         
        