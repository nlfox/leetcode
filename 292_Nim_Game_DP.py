class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = [False, True, True, True, False]
        for i in xrange(4, n + 1):
            if d[i - 1] or d[i - 2] or d[i - 3]:
                d.append(True)
            else:
                d.append(False)
        return d[n]
print Solution().canWinNim(8)