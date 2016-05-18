class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [i - 1 for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                subs = s[j:i]
                if subs == subs[::-1]:
                    # only consider when subs is pal
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
print Solution().minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")