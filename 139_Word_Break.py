class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in xrange(len(s)):
            for w in wordDict:
                if  (s[i - len(w) + 1:i + 1] == w) and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]


print Solution().wordBreak("bb",["a","b","bbb","bbbb"])
