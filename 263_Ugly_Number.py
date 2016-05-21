class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        flag = False
        if num == 0:
            return False
        s = [num]
        while s != [] and flag != True:
            n = s[-1]
            s.pop()
            if n == 1:
                flag = True
            for i in [2, 3, 5]:
                if n % i == 0:
                    s.append(n / i)
        return flag

print Solution().isUgly(18)
