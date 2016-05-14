class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        mat = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        if obstacleGrid[-1][-1]==1:
            return 0
        mat[1][1]=1
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                if not obstacleGrid[i - 2][j - 1]:
                    mat[i][j] += mat[i - 1][j]
                if not obstacleGrid[i - 1][j - 2]:
                    mat[i][j] += mat[i][j - 1]

        return mat[n][m]


print Solution().uniquePathsWithObstacles([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])
