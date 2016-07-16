class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        else:
            for i in xrange(len(nums)):
                if nums[i-1]<= nums[i] >= nums[(i+1)%len(nums)]:
                    return i