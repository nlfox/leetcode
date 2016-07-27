class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[float("inf") for i in xrange(len(j))] for j in triangle[:-1]]
        dp.append(triangle[-1])
        for i in range(len(triangle)-1)[::-1]:
            for j in xrange(len(triangle[i])):
                dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        return dp[0][0]