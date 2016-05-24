class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        if num==0:
            return False
        return int(bin(num)[3:]) == 0 and bin(num)[3:].count('0') % 2 == 0


print Solution().isPowerOfFour(5)
