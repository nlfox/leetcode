# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intvs = sorted(intervals,key=lambda x:x.start)
        p = 0
        res = []
        l = len(intvs)
        while p < l-1:
            if intvs[p].end >= intvs[p+1].start:
                intvs[p].end = max(intvs[p].end,intvs[p+1].end)
                intvs.pop(p+1)
                l -= 1
            else:
                p += 1
        return intvs