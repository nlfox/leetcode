class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        l = []
        for i, v in enumerate(s):
            if v in vowel:
                l.append(i)
        lRev = l[::-1]
        for i in xrange(len(l) / 2):
            s[l[i]], s[lRev[i]] = s[lRev[i]], s[l[i]]
        return ''.join(s)


print Solution().reverseVowels("leetcode")
