class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for i in xrange(n + 1)]
        t = 1
        while t != int(n ** 0.5) + 1:
            dp[t * t] = 1
            t += 1
        for i in xrange(1, n + 1):
            for j in xrange(1, int(i**0.5)):
                dp[i] = min(dp[i], 1 + dp[i - j*j])
            pass
        return dp[n]


print Solution().numSquares(9975)
