class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        for i in xrange(l):
            if i != nums[i]:
                return i
        return l


print Solution().missingNumber([0, 1, 2, 4, 5, 6])
