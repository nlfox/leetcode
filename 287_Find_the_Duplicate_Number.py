class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last = nums[0] - 1
        ind = 0
        while ind < len(nums):
            if last == nums[ind]:
                return last
            else:
                last = nums[ind]
                ind += 1
