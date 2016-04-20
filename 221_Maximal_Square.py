class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        self.max = 0
        self.matrix = [[int(i) for i in j] for j in matrix]
        length = len(matrix)
        try:
            width = len(matrix[0])
        except:
            return 0
        for i in xrange(length):
            for j in xrange(width):
                if (self.matrix[i][j] == 1):
                    for size in xrange(1, min(length - i + 1, width - j + 1)):
                        if not self.findSquare(i, j, size):
                            break
        return self.max

    def findSquare(self, x, y, size):
        for i in xrange(size):
            for j in xrange(size):
                if (self.matrix[x + i][y + j] == 0):
                    return False
        if (size > self.max):
            self.max = size
        return True


s = Solution()
print s.maximalSquare([[1, 0, 1, 0, 0],
                       [1, 0, 1, 1, 1],
                       [1, 0, 1, 0, 1],
                       [1, 0, 1, 1, 1],
                       [1, 0, 1, 1, 1]]
                      )
