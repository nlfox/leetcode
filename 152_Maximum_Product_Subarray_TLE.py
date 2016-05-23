class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenNums = len(nums)
        if not nums:
            return 0
        if lenNums == 1:
            return nums[0]
        d = [1, nums[0]] + [0] * (lenNums - 1)

        for i in xrange(lenNums):
            if nums[i] == 0:
                return max(self.maxProduct(nums[0:i]), self.maxProduct(nums[i + 1:]))
            d[i + 1] = d[i] * nums[i]
        m = -float("inf")

        for i in xrange(lenNums + 1):
            tm = max([d[i] / d[j] for j in xrange(i + 1)])
            if tm > m:
                m = tm
        return m


print Solution().maxProduct([0,2])
