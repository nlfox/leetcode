class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i for i in s.strip().split(" ") if i != ""][::-1])

s=Solution()
print s.reverseWords("   a   b ")