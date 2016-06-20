class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        a = [False for i in xrange(n + 2)]
        for i in nums:
            a[i] = True
        for i in xrange(1, n + 1):
            if not a[i]:
                return i


print Solution().firstMissingPositive([1])
