class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        d = [0] * n
        for i in xrange(n):
            xr = filter(lambda a: nums[a] < nums[i], xrange(i))
            if xr:
                d[i] = max([d[k] for k in xr]) + 1
            else:
                d[i] = 1
        return max(d)