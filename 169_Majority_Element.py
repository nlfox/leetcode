class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums) / 2
        for i in set(nums):
            if nums.count(i) > m:
                return i


print Solution().majorityElement([1, 2, 2, 2,2, 3, 3])
