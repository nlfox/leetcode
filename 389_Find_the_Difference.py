import string


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = {i:0 for i in string.lowercase}
        for i in list(s):
            m[i] += 1
        for j in list(t):
            m[j] -= 1
        for i,v in m.iteritems():
            if v == -1:
                return i