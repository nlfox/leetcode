class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import math
        r = n
        if m == 0 or n == 0:
            return 0
        nz_num = math.log(m, 2)
        if nz_num.is_integer():
            nz_num += 1
        else:
            nz_num = math.ceil(nz_num)
        nz_num = 2 ** nz_num - m
        if n - m > nz_num:
            return 0
        for i in xrange(m, n):
            r &= i
        return r


print Solution().rangeBitwiseAnd(4, 6)
