class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = 0
        for i in xrange(len(nums)):
            if i > m:
                return False
            else:
                m = max(m,i+nums[i])
        return True