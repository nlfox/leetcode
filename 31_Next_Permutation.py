class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last = -65536
        ind = -1
        for i in range(len(nums))[::-1]:
            if nums[i] >= last:
                last = nums[i]
            else:
                ind = i
                break
        ind2 = len(nums) - 1
        for i in range(ind, len(nums)):
            if nums[i] > nums[ind]:
                ind2 = i
        if ind >= 0:
            nums[ind], nums[ind2] = nums[ind2], nums[ind]
        i, j = ind + 1, (len(nums) - 1)
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
