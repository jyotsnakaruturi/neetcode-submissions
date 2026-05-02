class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevend=intervals[0][1]
        res=0
        for i in intervals[1:]:
            if prevend <= i[0]:
                prevend=i[1]
            else:
                res+=1
                prevend=min(i[1],prevend)
        return res