class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res=[]
        for i in intervals:
            if res and i[0]<= res[-1][1] :
                ress=res[-1]
                res.pop()
                res.append([(min(ress[0],i[0])),max(ress[1],i[1])])
            else:
                res.append(i)
        return res