class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = {i + 1: chr(65 + i) for i in xrange(26)}
        res = []
        if n == 0:
            return ""
        while n > 26:
            tm = n % 26
            if tm == 0:
                tm=26
            res.append(d[tm])
            n = (n - tm) / 26
        res.append(d[n])
        return ''.join(res[::-1])


print Solution().convertToTitle(52)
