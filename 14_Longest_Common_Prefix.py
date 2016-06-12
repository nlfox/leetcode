class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        l = min([len(s) for s in strs])
        for i in xrange(l):
            t = strs[0][i]
            for s in strs:
                if s[i] != t:
                    return strs[0][0:i]
        return strs[0][0:l]


print Solution().longestCommonPrefix(["a"])
