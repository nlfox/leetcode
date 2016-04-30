class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        self.res = []
        if  k==0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        for i in xrange(1, n - k + 2):
            self.dfs(level=1, num=i, l=[i])
        return self.res

    def dfs(self, level, num, l):
        if (level + 1 == self.k):
            for i in xrange(num + 1, self.n - (self.k - (level + 1)) + 1):
                self.res.append(l + [i])
            return
        elif level == 1:
            for i in xrange(num + 1, self.n - (self.k - (level + 1)) + 1):
                self.dfs(level + 1, i, l + [i])
            return
        else:
            for i in xrange(num + 1, self.n - (self.k - (level + 1)) + 1):
                self.dfs(level + 1, i, l + [i])
            return


s = Solution()
print s.combine(2, 1)
