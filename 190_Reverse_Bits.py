class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(bin(n)[2:].zfill(32)[::-1],2)


print Solution().reverseBits(43261596)