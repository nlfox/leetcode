class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in xrange(n)]
        width = n
        height = n
        times = n / 2 if n % 2 == 0 else (n + 1) / 2
        y, x, c = 0, 0, 1

        for i in xrange(times):
            for _ in xrange(width):
                matrix[y][x] = c
                x += 1
                c += 1

            x -= 1
            y += 1
            height -= 1

            for _ in xrange(height):
                matrix[y][x] = c
                y += 1
                c += 1
            y -= 1
            x -= 1
            width -= 1


            for _ in xrange(width):
                matrix[y][x] = c
                x -= 1
                c += 1
            x += 1
            y -= 1
            height -= 1

            for _ in xrange(height):
                matrix[y][x] = c
                y -= 1
                c += 1
            y += 1
            x += 1
            width -= 1


        return matrix


print Solution().generateMatrix(1)
