class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.dfs(s, [])
        return self.res
    def dfs(self, s, arr):
        s_len = len(s)
        if s_len == 0:
            self.res.append(arr)
        for i in xrange(1,s_len+1):
            if s[0:i] == s[0:i][::-1]:
                self.dfs(s[i:], arr + [s[0:i]])
        return


print Solution().partition("a")
