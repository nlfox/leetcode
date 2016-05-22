class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        height = len(matrix)
        width = len(matrix[0])
        if height == 1:
            return matrix[0]
        times = height / 2 if height % 2 == 0 else (height + 1) / 2

        res = []
        x, y = 0, 0
        for i in xrange(times):
            for _ in xrange(width):
                res.append(matrix[y][x])
                x += 1
            x -= 1
            y += 1
            height -= 1

            if height == 0:
                return res

            for _ in xrange(height):
                res.append(matrix[y][x])
                y += 1
            y -= 1
            x -= 1
            width -= 1

            if width == 0:
                return res

            for _ in xrange(width):
                res.append(matrix[y][x])
                x -= 1
            x += 1
            y -= 1
            height -= 1
            if height == 0:
                return res

            for _ in xrange(height):
                res.append(matrix[y][x])
                y -= 1
            y += 1
            x += 1
            width -= 1
            if width == 0:
                return res

        return res


print Solution().spiralOrder(
    [[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]])
