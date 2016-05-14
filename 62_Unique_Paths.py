class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        mat = [[1 if j == 1 else 0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        mat[1] = [1] * (m + 1)
        for i in xrange(2, n + 1):
            for j in xrange(2, m + 1):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        return mat[n][m]


print Solution().uniquePaths(10, 10)
