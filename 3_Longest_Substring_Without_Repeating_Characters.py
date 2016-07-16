class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        d = {}
        l = 0
        r = 0
        m = 0
        while r <= (len(s) - 1):
            if s[r] in d:
                t = d[s[r]]
                d[s[r]] = r
                if (r - l) > m:
                    m = r - l
                l = max(t + 1, l)
                r += 1
            else:
                d[s[r]] = r
                r += 1
        if (r - l) > m:
            m = r - l
        return m
