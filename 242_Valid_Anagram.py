class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        print s,t
        return t == s


s = Solution()
print s.isAnagram("anagram", "nagaram")
