class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in xrange(num):
            res.append(bin(i)[2:].count('1'))
        return res
