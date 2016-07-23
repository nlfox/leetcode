class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {1: 1, 2: 2}
        for i in xrange(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n]
