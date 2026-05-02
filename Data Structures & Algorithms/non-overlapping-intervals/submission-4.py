class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end=intervals[0][1]
        c=0
        n=len(intervals)
        for i in range (1,n):
            if end <= intervals[i][0]:
                end = intervals[i][1]
            else:
                c +=1
                end = min(end,intervals[i][1])
        return c