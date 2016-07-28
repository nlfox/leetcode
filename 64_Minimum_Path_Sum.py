class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        d = [[float("inf") for j in xrange(n)] for i in xrange(m)]
        d[0][0] = grid[0][0]
        chk = lambda i,j:float("inf") if (i < 0 or j< 0 or i==m or j==n) else d[i][j]
        for i in xrange(m):
            for j in xrange(n):
                if not (i==0 and j==0):
                    d[i][j] = grid[i][j] + min(chk(i-1,j),chk(i,j-1))
        return d[-1][-1]