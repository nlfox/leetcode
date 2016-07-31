class BIT(object):
    def __init__(self, n):
        self.nums = [0] * (n + 1)

    def update(self, i, v):
        while i < len(self.nums):
            self.nums[i] += v
            i += (i & -i)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.nums[i]
            i -= (i & -i)
        return s


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {v: i for i, v in enumerate(sorted(set(nums)))}
        t = BIT(len(nums))
        res = []
        for i in xrange(len(nums) - 1, -1, -1):
            res.append(t.sum(d[nums[i]]))
            t.update(d[nums[i]] + 1, 1)
        return res[::-1]
