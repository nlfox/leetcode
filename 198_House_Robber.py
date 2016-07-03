class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        d[-1] = 0
        d[-2] = 0
        for i, v in enumerate(nums):
            d[i] = max(d[i - 1], d[i - 2] + v)
        return d[len(nums) - 1]
