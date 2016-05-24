class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        d = {chr(65 + i): i + 1 for i in xrange(26)}
        f = 0
        c = 1
        for i in s[::-1]:
            f += d[i] * c
            c *= 26
        return f


print Solution().titleToNumber("")
