class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        flag = True
        l = [str(i) for i in range(1, n + 1)]
        res = []
        k -= 1
        while flag:
            nt = math.factorial(n - 1)
            t = k / nt
            res.append(l[t])
            k = k % nt
            l.pop(t)
            n -= 1
            if (n == 0):
                flag = False
        return ''.join(res)


s = Solution()
print s.getPermutation(3, 1)
