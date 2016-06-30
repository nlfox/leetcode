class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1
        s = "1"
        last = "1"
        c = 0
        for i in xrange(n):
            st = s
            s = ""
            for i in st:
                if i == last:
                    c += 1
                else:
                    s += (str(c) + last)
                    last = i
                    c = 1
            s += (str(c) + last)
            last = s[0]
            c = 0
        return s


print Solution().countAndSay(3)
