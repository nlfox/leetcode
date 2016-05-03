class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(n):
            matrix[i]=matrix[i][::-1]
        print matrix


s = Solution()
print s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
