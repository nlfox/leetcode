class Solution(object):

    def coinChange(self, coins, amount):

        """

        :type coins: List[int]

        :type amount: int

        :rtype: int

        """

        d = [-1 for i in xrange(amount)]

        for i in coins:

            d[i] = 1

        for i in xrange(1,amount+1):

            for j in xrange(1,i):

                if d[j] < 0:

                    continue

                d[j] = min(d[j],d[j]+d[i-j])
