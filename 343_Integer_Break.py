# coding=utf-8
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        if (n == 2):
            return 1
        if (n == 3):
            return 2
        return self.iBrec(n)

    def iBrec(self, n):
        if (n == 3):
            return 3
        if (n == 2):
            return 2
        if (n == 1):
            return 1
        if (n % 2 == 0):
            return max(self.iBrec(n / 2) ** 2, self.iBrec((n + 2) / 2) * self.iBrec((n - 2) / 2))
            # n 为偶数
        else:
            return max(self.iBrec((n - 1) / 2) * self.iBrec((n + 1) / 2) ,self.iBrec((n - 3) / 2) * self.iBrec((n + 3) / 2))
            # n 为奇数


s = Solution()
print s.integerBreak(9)
