class Solution(object):
    def dfs(self, l, level, res):
        lenL = len(l)
        if lenL > (12 - level * 3) or lenL < (3 - level):
            return
        if lenL == 0 and level == 4:
            self.res.append(".".join(res))
            return
        j = 4
        if (lenL <= 3):
            j = lenL + 1
        for i in xrange(1, j):
            if (i == 3 and 100 <= int(l[0:i]) <= 255) or (i == 2 and 10 <= int(l[0:i]) <= 99) or (
                            i == 1 and 0 <= int(l[0:i]) <= 9):
                self.dfs(l[i:], level + 1, res + [l[0:i]])
            else:
                return
        return

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        if len(s) < 4:
            return []
        for i in xrange(1, 4):
            if (i == 3 and 100 <= int(s[0:i]) <= 255) or (i == 2 and 10 <= int(s[0:i]) <= 99) or (
                            i == 1 and 0 <= int(s[0:i]) <= 9):
                self.dfs(s[i:], 1, [s[0:i]])
        return self.res


s = Solution()
print s.restoreIpAddresses("010010")
