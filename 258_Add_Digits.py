class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        n = 0
        for i in num:
            n += int(i)

        if len(str(n)) > 1:
            return self.addDigits(n)
        else:
            return n


print Solution().addDigits(38)
