class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        left, right = 0, l
        try:
            while (left <= right):
                medium = (left + right) / 2
                if target > nums[medium]:
                    left = medium + 1
                    continue
                elif target < nums[medium]:
                    right = medium - 1
                    continue
                else:
                    right, left = medium, medium
                    while right < l and target == nums[right]:
                        right += 1
                    while left >= 0 and target == nums[left]:
                        left -= 1
                    return [left + 1, right - 1]
        except:
            return [-1, -1]
        return [-1, -1]
