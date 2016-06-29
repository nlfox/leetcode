class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right, mid = 0, len(nums), 0
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
                if right >= 0:
                    if nums[right] < target:
                        return right + 1
                else:
                    return 0
            elif nums[mid] < target:
                left = mid + 1
                if left < len(nums):
                    if nums[left] > target:
                        return left
                else:
                    return len(nums)
            else:
                return mid


print Solution().searchInsert([1, 3], 2)
