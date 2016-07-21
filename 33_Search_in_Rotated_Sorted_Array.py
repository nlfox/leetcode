class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        last = nums[0] - 1
        pivot = 0
        for i in xrange(len(nums)):
            if nums[i] > last:
                last = nums[i]
            else:
                pivot = i
                break
        print pivot
        left, right = 0, len(nums) - 1
        l = len(nums)
        if l == 1:
            return 0 if nums[0] == target else -1
        while left <= right:
            mid = (left + right) / 2
            if nums[(mid + pivot) % l] > target:
                right = mid - 1
            elif nums[(mid + pivot) % l] < target:
                left = mid + 1
            else:
                return (mid + pivot) % l
        return -1
