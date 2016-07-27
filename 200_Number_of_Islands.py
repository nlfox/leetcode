class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.grid = [[int(j) for j in list(i)] for i in grid]
        self.count = 1
        self.cur = 0
        self.height = len(grid)
        self.width = len(grid[0])
        g = []
        for i in xrange(self.height):
            for j in xrange(self.width):
                if self.check(i, j) == 0:
                    continue
                else:
                    m = max([self.check(i - 1, j), self.check(i + 1, j), self.check(i, j + 1), self.check(i, j - 1)])
                    if m == 1:
                        self.count += 1
                        self.grid[i][j] = self.count
                    elif m == 0:
                        self.count += 1
                        self.grid[i][j] = self.count
                    else:
                        self.grid[i][j] = m
                    if self.check(i - 1, j) == 1:
                        self.grid[i - 1][j] = self.count
                    if self.check(i + 1, j) == 1:
                        self.grid[i + 1][j] = self.count
                    if self.check(i, j - 1) == 1:
                        self.grid[i][j - 1] = self.count
                    if self.check(i, j + 1) == 1:
                        self.grid[i][j + 1] = self.count

        return self.count - 1

    def check(self, x, y):
        if x == -1 or y == -1 or x == self.height or y == self.width:
            return 0
        else:
            return self.grid[x][y]


print Solution().numIslands(["10111","10101","11101"])
