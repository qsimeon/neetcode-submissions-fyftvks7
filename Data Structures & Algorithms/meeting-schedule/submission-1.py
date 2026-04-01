"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        timeSet = set()
        for rng in intervals:
            for i in range(rng.start, rng.end):
                if i in timeSet:
                    return False
                timeSet.add(i)
        return True
