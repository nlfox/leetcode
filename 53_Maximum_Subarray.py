class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp, res = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            tmp = max(tmp + nums[i], nums[i])
            res = max(tmp, res)
        return res

s = Solution()
print s.maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4])
