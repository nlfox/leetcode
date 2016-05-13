class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        res = []
        for i in s:
            i = string.lower(i)
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                res.append(i)
        print res
        return res == res[::-1]


print Solution().isPalindrome("0P")
