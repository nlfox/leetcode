class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        d = [[0 for j in xrange(n)] for i in xrange(m)]
        d[0][0] = 1
        chk = lambda i,j:0 if (i < 0 or j< 0 or i==m or j==n) else d[i][j]
        for i in xrange(m):
            for j in xrange(n):
                if not (i==0 and j==0):
                    d[i][j] = chk(i-1,j) + chk(i,j-1)
        return d[-1][-1]