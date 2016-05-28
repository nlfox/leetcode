class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        i = 0
        j = 0
        while i < nums_len:
            if nums[i] == 0:
                i += 1
                continue
            nums[j] = nums[i]
            j += 1
            i += 1
        while j != i:
            nums[j] = 0
            j += 1


s = [1, 0, 2, 0, 3, 0, 4, 0, 5]
Solution().moveZeroes(s)
print s
