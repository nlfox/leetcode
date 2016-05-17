class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        num = len(ratings)
        candy = [1 for i in xrange(num)]
        for i in xrange(1, num):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
            else:
                continue
        for i in range(0, num - 1)[::-1]:
            if ratings[i] > ratings[i + 1] :
                candy[i] = max(candy[i + 1] + 1,candy[i])
            else:
                continue
        return sum(candy)


print Solution().candy([4,2,3,4,1])
