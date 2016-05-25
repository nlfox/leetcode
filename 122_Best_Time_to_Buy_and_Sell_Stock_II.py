class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        d = {0: 0}
        last = prices[0]
        m = 0
        total = 0
        for idx in xrange(1, len(prices)):
            s = prices[idx] - last
            if s < 0:
                d[idx] = 0
                total += m
                m = 0
            else:
                d[idx] = max(s, d[idx - 1] + s)
            last = prices[idx]
            if d[idx] > m:
                m = d[idx]
        total += m
        return total


print Solution().maxProfit([1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 6, 1, 6])
