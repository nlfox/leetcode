class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2:
            return min(1+self.integerReplacement(n-1),2+self.integerReplacement((n+1)/2))
        else:
            return 1+self.integerReplacement(n/2)