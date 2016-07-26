class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        d = {-1: 0, -2: 0}
        tmp = nums[0]
        nums[0] = 0
        for i, v in enumerate(nums):
            d[i] = max(d[i - 1], d[i - 2] + v)
        r1 = d[len(nums) - 1]
        nums[0] = tmp
        tmp = nums[-1]
        nums[-1]=0
        d = {-1: 0, -2: 0}
        for i, v in enumerate(nums):
            d[i] = max(d[i - 1], d[i - 2] + v)
        r2 = d[len(nums) - 1]
        return max(r1,r2)