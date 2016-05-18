class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.d = {}
        s_len = len(s)
        return self.dp(s)

    def dp(self, s):
        minl = float("inf")
        if not s:
            return 0
        if self.d.has_key(s):
            return self.d[s]
        else:
            if s[::-1] == s:
                self.d[s] = 0
                return 0
            minl = min([self.dp(s[:i]) + self.dp(s[i:]) + 1 for i in xrange(1, len(s))])
            self.d[s] = minl
            return minl


print Solution().minCut(
    "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")
