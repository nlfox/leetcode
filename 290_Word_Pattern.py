class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        dr = {}
        s = str.split(' ')
        if len(s) != len(pattern):
            return False
        for i in xrange(len(pattern)):
            if d.has_key(pattern[i]):
                if d[pattern[i]] == s[i]:
                    continue
                else:
                    return False
            else:
                if dr.has_key(s[i]):
                    return False
                d[pattern[i]] = s[i]
                dr[s[i]] = d[pattern[i]]

        return True


print Solution().wordPattern("abba", "dog dog dog dog")
