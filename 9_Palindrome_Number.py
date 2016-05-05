class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1]==str(x)


print Solution().isPalindrome(-2147483648)