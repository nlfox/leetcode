class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s) - 9):
            if d.has_key(s[i:i + 10]):
                d[s[i:i + 10]] += 1
            else:
                d[s[i:i + 10]] = 1
        return [k for k,v in d.items() if v>1]
print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
