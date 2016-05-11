class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max = float("inf")
        if not amount:
            return 0
        d = [max for i in xrange(amount + 1)]
        d[0] = 1
        for i in coins:
            if i < amount:
                d[i] = 1
        for i in xrange(1, amount + 1):
            ls = [1 + d[i - j] if i > j else max for j in coins]
            d[i] = min(ls)

        return d[amount] if d[amount] != max else -1


print Solution().coinChange([1, 2, 5], amount=11)
