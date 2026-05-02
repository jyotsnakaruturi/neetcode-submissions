"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[]
        end=[]
        room=0
        max_room=0
        s=0
        e=0

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        while s < len(intervals):
            if start[s] < end[e]:
                room+=1
                s+=1
            else:
                room-=1
                e+=1
            max_room=max(max_room,room)
        return max_room
