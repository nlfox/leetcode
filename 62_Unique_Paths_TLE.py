class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.m = m
        self.n = n
        self.cnt = 0
        self.dfs(1, 1)
        return self.cnt

    def dfs(self, x, y):
        if (x == self.m and y == self.n):
            self.cnt += 1
            return
        else:
            if x + 1 <= self.m:
                self.dfs(x + 1, y)
            if y + 1 <= self.n:
                self.dfs(x, y + 1)
        return


print Solution().uniquePaths(1, 2)
