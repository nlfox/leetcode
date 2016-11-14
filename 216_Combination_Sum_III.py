class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.mask = [False] + [True] * 9
        self.res = []
        self.dfs(k, n,1)
        return self.res

    def dfs(self, k, n,m):
        if n == 0 and k == 0:
            self.res += [filter(lambda x: self.mask[x]==False, range(1, 10))]
            return
        #print filter(lambda x: self.mask[x], range(1, n + 1)), ",", k, ",", n
        if n > 0 and k > 0:
            for i in filter(lambda x: self.mask[x], range(m, min(n + 1,10))):
                self.mask[i] = False
                self.dfs(k - 1, n - i,i)
                self.mask[i] = True
        return