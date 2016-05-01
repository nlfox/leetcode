class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapChar = {}
        mapCharRev = {}
        s = list(s)
        t = list(t)
        for index, char in enumerate(s):
            if mapChar.has_key(char):
                s[index] = mapChar[char]
                continue
            else:
                if mapCharRev.has_key(t[index]):
                    return False
                mapCharRev[t[index]] = char
                mapChar[char] = t[index]

                s[index] = t[index]
        return s == t


s = Solution()
print s.isIsomorphic("app", "add")
