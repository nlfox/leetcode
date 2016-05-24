class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n - i):
                return n - i
        return 0


print Solution().hIndex([3, 0, 6, 1, 5, 4, 4])
