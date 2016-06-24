class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.d = {}
        return self.rec(n)

    def rec(self, n):
        s = 0
        for i in str(n):
            s += int(i) * int(i)
        if self.d.has_key(s):
            return False
        elif s == 1:
            return True
        else:
            self.d[s] = True
            return self.rec(s)
print Solution().isHappy(19)