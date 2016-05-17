class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            s = int("-" + str(abs(x))[::-1])
            return s if s >= -2147483647 else 0

        else:
            s = int(str(x)[::-1])
            return s if s <= 2147483647 else 0


print Solution().reverse(-2147483648)
